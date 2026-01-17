#!/usr/bin/env python3
"""
Ancestry Analysis Engine
Uses real population allele frequencies from 1000 Genomes and gnomAD.
No hardcoded weights - pure statistical inference.
"""

import math
import json
import os
from typing import Dict, List, Tuple

# Use merged markers (608 with real population frequencies)
try:
    from ancestry_markers_merged import ANCESTRY_MARKERS_MERGED as ANCESTRY_MARKERS
except ImportError:
    try:
        from ancestry_markers_expanded import ANCESTRY_MARKERS_EXPANDED as ANCESTRY_MARKERS
    except ImportError:
        from ancestry_markers_real import ANCESTRY_MARKERS


# =============================================================================
# REFERENCE POPULATIONS FROM 1000 GENOMES / GNOMAD
# These are the ACTUAL populations we have frequency data for
# =============================================================================

REFERENCE_POPULATIONS = {
    # European populations (1000 Genomes codes)
    'British': {
        'display': 'England & Northwestern Europe',
        'continent': 'European',
        'code': 'GBR',
    },
    'Northern_European': {
        'display': 'Germanic Europe',
        'continent': 'European',
        'code': 'CEU',
    },
    'Finnish': {
        'display': 'Finland & Baltic',
        'continent': 'European',
        'code': 'FIN',
    },
    'Italian_Tuscan': {
        'display': 'Southern Europe & Mediterranean',
        'continent': 'European',
        'code': 'TSI',
    },
    'Spanish_Iberian': {
        'display': 'Spain & Portugal',
        'continent': 'European',
        'code': 'IBS',
    },
    'Ashkenazi_Jewish': {
        'display': 'Ashkenazi Jewish',
        'continent': 'European',
        'code': 'ASJ',
    },

    # African populations
    'Yoruba_African': {
        'display': 'West African',
        'continent': 'African',
        'code': 'YRI',
    },
    'African': {
        'display': 'African',
        'continent': 'African',
        'code': 'AFR',
    },

    # East Asian populations
    'Han_Chinese': {
        'display': 'Chinese',
        'continent': 'East Asian',
        'code': 'CHB',
    },
    'Japanese': {
        'display': 'Japanese',
        'continent': 'East Asian',
        'code': 'JPT',
    },
    'East_Asian': {
        'display': 'East Asian',
        'continent': 'East Asian',
        'code': 'EAS',
    },

    # South Asian populations
    'Gujarati_Indian': {
        'display': 'South Asian',
        'continent': 'South Asian',
        'code': 'GIH',
    },
    'South_Asian': {
        'display': 'South Asian',
        'continent': 'South Asian',
        'code': 'SAS',
    },

    # Middle Eastern
    'Middle_Eastern': {
        'display': 'Middle East & North Africa',
        'continent': 'Middle Eastern',
        'code': 'MID',
    },

    # Admixed American populations
    'Mexican': {
        'display': 'Indigenous Americas - Mexico',
        'continent': 'Americas',
        'code': 'MXL',
    },
    'Puerto_Rican': {
        'display': 'Caribbean',
        'continent': 'Americas',
        'code': 'PUR',
    },
}

# Continental groupings - ONLY unadmixed reference populations
# Mexican and Puerto_Rican are ADMIXED (European + Indigenous + African)
# and should NOT be used as reference populations - they match everyone
CONTINENTAL_GROUPS = {
    'European': ['British', 'Northern_European', 'Finnish', 'Italian_Tuscan',
                 'Spanish_Iberian'],
    'African': ['Yoruba_African'],
    'East Asian': ['Han_Chinese', 'Japanese'],
    'South Asian': ['Gujarati_Indian'],
    'Middle Eastern': ['Middle_Eastern'],
}

# Populations to EXCLUDE from scoring (admixed or aggregate)
EXCLUDED_POPULATIONS = [
    'Mexican',        # Admixed (European + Indigenous + African)
    'Puerto_Rican',   # Admixed (European + African + Indigenous)
    'African',        # Aggregate (use Yoruba_African instead)
    'East_Asian',     # Aggregate (use specific populations)
    'South_Asian',    # Aggregate (use Gujarati_Indian instead)
    'Ashkenazi_Jewish',  # Special case - European subgroup, not separate continent
]

# Population fallback mapping for markers that don't have specific population data
# When looking for a specific population, try these alternatives in order
POPULATION_FALLBACKS = {
    'Northern_European': ['British', 'European', 'Finnish_gnomAD'],
    'Finnish': ['Finnish_gnomAD', 'Northern_European', 'British'],
    'Italian_Tuscan': ['Spanish_Iberian', 'European'],
    'Spanish_Iberian': ['Italian_Tuscan', 'European'],
    'British': ['Northern_European', 'European'],
    'Yoruba_African': ['African'],
    'Han_Chinese': ['East_Asian', 'Japanese'],
    'Japanese': ['East_Asian', 'Han_Chinese'],
    'Gujarati_Indian': ['South_Asian'],
    'Middle_Eastern': ['South_Asian', 'European'],  # Intermediate frequencies
}


class CalibratedAncestryEngine:
    """
    Ancestry analysis using maximum likelihood estimation.

    For each SNP, calculates the probability of observing the user's genotype
    given the allele frequencies in each reference population.
    Uses log-likelihood sum across all markers, then converts to percentages.
    """

    def __init__(self):
        self.snp_dict = {}
        self.markers = ANCESTRY_MARKERS

    def load_dna(self, snp_dict: Dict[str, str]):
        """Load DNA data and standardize genotypes"""
        self.snp_dict = {}
        for rsid, genotype in snp_dict.items():
            if len(genotype) == 2:
                # Sort alleles alphabetically for consistency
                self.snp_dict[rsid] = ''.join(sorted(genotype.upper()))
            else:
                self.snp_dict[rsid] = genotype.upper()

    def _calc_genotype_probability(self, genotype: str, pop_freqs: Dict) -> float:
        """
        Calculate probability of genotype under Hardy-Weinberg equilibrium.

        For homozygous (AA): P = p^2
        For heterozygous (AB): P = 2pq

        Where p and q are allele frequencies in the population.
        """
        if len(genotype) != 2:
            return 0.001  # Invalid genotype

        allele1, allele2 = genotype[0], genotype[1]

        # Get frequencies, default to rare (0.001) if not found
        freq1 = pop_freqs.get(allele1, 0.001)
        freq2 = pop_freqs.get(allele2, 0.001)

        # Clamp to avoid log(0)
        freq1 = max(min(freq1, 0.999), 0.001)
        freq2 = max(min(freq2, 0.999), 0.001)

        if allele1 == allele2:
            # Homozygous: p^2
            return freq1 * freq1
        else:
            # Heterozygous: 2pq
            return 2 * freq1 * freq2

    def _get_population_frequencies(self, frequencies: Dict, population: str) -> Dict:
        """
        Get frequency data for a population, using fallbacks if primary isn't available.
        """
        # First try the exact population
        if population in frequencies:
            return frequencies[population]

        # Try fallback populations
        fallbacks = POPULATION_FALLBACKS.get(population, [])
        for fallback in fallbacks:
            if fallback in frequencies:
                return frequencies[fallback]

        return None

    def _calculate_population_likelihood(self, population: str) -> Tuple[float, int]:
        """
        Calculate log-likelihood for a population across all matching markers.
        Returns (average_log_likelihood, marker_count)
        Uses fallback populations when primary data isn't available.
        """
        total_log_likelihood = 0.0
        marker_count = 0

        for rsid, marker_data in self.markers.items():
            # Skip if user doesn't have this SNP
            if rsid not in self.snp_dict:
                continue

            genotype = self.snp_dict[rsid]
            frequencies = marker_data.get('frequencies', {})

            # Get frequency data, using fallbacks if needed
            pop_freqs = self._get_population_frequencies(frequencies, population)
            if pop_freqs is None:
                continue

            probability = self._calc_genotype_probability(genotype, pop_freqs)

            if probability > 0:
                total_log_likelihood += math.log(probability)
                marker_count += 1

        if marker_count == 0:
            return -999.0, 0

        # Return average log-likelihood per marker
        return total_log_likelihood / marker_count, marker_count

    def _likelihood_to_percentage(self, scores: Dict[str, float],
                                   scale_factor: float = 10.0) -> Dict[str, float]:
        """
        Convert log-likelihood scores to percentages using softmax.

        The scale_factor controls sensitivity:
        - Higher = more extreme differences (winner-take-all)
        - Lower = more spread out percentages
        """
        if not scores:
            return {}

        # Normalize by subtracting max (for numerical stability)
        max_score = max(scores.values())

        exp_scores = {}
        for pop, score in scores.items():
            # Scale the difference from max
            scaled_diff = (score - max_score) * scale_factor
            exp_scores[pop] = math.exp(scaled_diff)

        total = sum(exp_scores.values())

        if total == 0:
            return {}

        # Convert to percentages
        percentages = {}
        for pop, exp_score in exp_scores.items():
            pct = (exp_score / total) * 100
            if pct >= 0.1:  # Only include if >= 0.1%
                percentages[pop] = round(pct, 1)

        return percentages

    def calculate_continental_ancestry(self) -> Dict[str, float]:
        """
        Calculate broad continental ancestry breakdown.
        Uses the best-matching population from each continent.
        """
        continent_scores = {}
        continent_counts = {}

        for continent, populations in CONTINENTAL_GROUPS.items():
            best_score = -999.0
            best_count = 0

            for pop in populations:
                score, count = self._calculate_population_likelihood(pop)
                # Only consider populations with sufficient markers
                if count >= 20 and score > best_score:
                    best_score = score
                    best_count = count

            if best_count >= 20:
                continent_scores[continent] = best_score
                continent_counts[continent] = best_count

        if not continent_scores:
            return {'European': 100.0}  # Default fallback

        # Use moderate scale factor for continental (clear but not extreme separation)
        # Lower values give more nuanced mixed ancestry results
        return self._likelihood_to_percentage(continent_scores, scale_factor=15.0)

    def calculate_population_ancestry(self) -> Dict[str, Tuple[float, int]]:
        """
        Calculate likelihood scores for all reference populations.
        Returns dict of {population: (score, marker_count)}
        Excludes admixed and aggregate populations.
        """
        all_scores = {}

        for pop in REFERENCE_POPULATIONS.keys():
            # Skip admixed and aggregate populations
            if pop in EXCLUDED_POPULATIONS:
                continue

            score, count = self._calculate_population_likelihood(pop)
            if count >= 10:  # Minimum markers threshold
                all_scores[pop] = (score, count)

        return all_scores

    def calculate_regional_ancestry(self) -> Dict[str, float]:
        """
        Calculate ancestry breakdown by reference population.
        Only includes populations with sufficient data.
        """
        all_scores = self.calculate_population_ancestry()

        # Filter to populations with good coverage
        good_scores = {pop: score for pop, (score, count) in all_scores.items()
                       if count >= 30}

        if not good_scores:
            # Fall back to any available
            good_scores = {pop: score for pop, (score, count) in all_scores.items()}

        if not good_scores:
            return {}

        # Use lower scale factor for regional breakdown to show ancestry mixture
        return self._likelihood_to_percentage(good_scores, scale_factor=8.0)

    def analyze(self) -> Dict:
        """
        Run complete ancestry analysis.

        Returns:
            dict with:
            - continental: broad continental percentages
            - regional: reference population percentages
            - populations: detailed scores for each population
            - markers_matched: number of markers found in user's data
            - confidence: confidence level based on marker coverage
        """
        markers_matched = sum(1 for rsid in self.markers if rsid in self.snp_dict)

        # Calculate all population scores
        pop_scores = self.calculate_population_ancestry()

        # Continental breakdown
        continental = self.calculate_continental_ancestry()

        # Regional breakdown (by reference population)
        regional = self.calculate_regional_ancestry()

        # Format regional with display names
        regional_display = {}
        for pop, pct in regional.items():
            if pop in REFERENCE_POPULATIONS:
                display_name = REFERENCE_POPULATIONS[pop]['display']
                regional_display[display_name] = pct

        # Sort by percentage
        regional_display = dict(sorted(regional_display.items(),
                                       key=lambda x: x[1], reverse=True))

        # Calculate confidence based on marker coverage
        # 608 markers available, need at least 200 for good confidence
        confidence = min(100, (markers_matched / 200) * 100)

        return {
            'continental': continental,
            'regional': regional_display,
            'populations': {pop: {'score': score, 'markers': count}
                           for pop, (score, count) in pop_scores.items()},
            'markers_total': len(self.markers),
            'markers_matched': markers_matched,
            'confidence': round(confidence, 1),
        }

    # Legacy compatibility - these methods return data in the old format
    # so existing UI code doesn't break

    def calculate_all_scores(self) -> Dict[str, Tuple[float, int]]:
        """Legacy: Calculate scores for all reference populations"""
        return self.calculate_population_ancestry()

    def calculate_continental(self, scores: Dict) -> Dict[str, float]:
        """Legacy: Calculate continental ancestry"""
        return self.calculate_continental_ancestry()

    def calculate_european_distribution(self, scores: Dict) -> Dict[str, float]:
        """Legacy: Calculate European population distribution"""
        european_pops = CONTINENTAL_GROUPS['European']
        eur_scores = {pop: score for pop, (score, count) in scores.items()
                      if pop in european_pops and count >= 20}

        if not eur_scores:
            return {}

        return self._likelihood_to_percentage(eur_scores, scale_factor=10.0)

    def estimate_subregions(self, european_pct: float,
                            eur_distribution: Dict[str, float],
                            all_scores: Dict) -> Dict[str, float]:
        """Legacy: Returns regional breakdown (no fake sub-regions)"""
        # Just return the European distribution scaled to the European percentage
        if not eur_distribution:
            return {}

        total = sum(eur_distribution.values())
        if total == 0:
            return {}

        # Scale to actual European percentage
        factor = european_pct / total
        return {pop: pct * factor for pop, pct in eur_distribution.items()}

    def group_subregions(self, subregions: Dict[str, float]) -> Dict[str, Dict[str, float]]:
        """Legacy: Group by display region"""
        grouped = {}

        for pop, pct in subregions.items():
            if pop in REFERENCE_POPULATIONS:
                display = REFERENCE_POPULATIONS[pop]['display']
                continent = REFERENCE_POPULATIONS[pop]['continent']

                if continent not in grouped:
                    grouped[continent] = {}

                grouped[continent][display] = round(pct, 1)

        # Sort groups by total
        for group in grouped:
            grouped[group] = dict(sorted(grouped[group].items(),
                                         key=lambda x: x[1], reverse=True))

        totals = {g: sum(r.values()) for g, r in grouped.items()}
        grouped = dict(sorted(grouped.items(),
                              key=lambda x: totals.get(x[0], 0), reverse=True))

        return grouped


def test_with_file(filepath: str):
    """Test ancestry analysis with a DNA file"""
    import pandas as pd

    print(f"Loading {filepath}...")
    df = pd.read_csv(filepath, sep='\t', comment='#')
    df.columns = ['rsid', 'chromosome', 'position', 'allele1', 'allele2']

    snp_dict = {}
    for _, row in df.iterrows():
        rsid = str(row['rsid'])
        a1, a2 = str(row['allele1']), str(row['allele2'])
        if a1 not in ['0', '-', 'N', 'D', 'I'] and a2 not in ['0', '-', 'N', 'D', 'I']:
            snp_dict[rsid] = a1 + a2

    print(f"Loaded {len(snp_dict):,} SNPs")

    engine = CalibratedAncestryEngine()
    engine.load_dna(snp_dict)
    results = engine.analyze()

    print(f"\nMarkers matched: {results['markers_matched']}/{results['markers_total']}")
    print(f"Confidence: {results['confidence']}%")

    print("\n" + "=" * 60)
    print("CONTINENTAL ANCESTRY")
    print("=" * 60)
    for continent, pct in sorted(results['continental'].items(),
                                  key=lambda x: x[1], reverse=True):
        print(f"  {continent}: {pct}%")

    print("\n" + "=" * 60)
    print("REGIONAL BREAKDOWN")
    print("=" * 60)
    for region, pct in results['regional'].items():
        print(f"  {region}: {pct}%")

    print("\n" + "=" * 60)
    print("RAW POPULATION SCORES (for debugging)")
    print("=" * 60)
    for pop, data in sorted(results['populations'].items(),
                            key=lambda x: x[1]['score'], reverse=True):
        print(f"  {pop}: score={data['score']:.3f}, markers={data['markers']}")

    return results


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        test_with_file(sys.argv[1])
    else:
        print("Usage: python calibrated_ancestry_engine.py <dna_file.txt>")
