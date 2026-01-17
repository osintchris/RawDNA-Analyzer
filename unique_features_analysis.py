#!/usr/bin/env python3
"""
Unique Features Analysis Engine
Provides analysis methods for all unique DNA features:
- Genetic Superpowers
- Survival Scenarios
- Historical Figure Matching
- DNA Time Machine
- Epigenetic Age
- Enhanced Archaic DNA
- Diet & Training Optimization
- Ancestry Story Generation
- Facial Reconstruction
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
import math

from unique_features_database import (
    GENETIC_SUPERPOWERS,
    SURVIVAL_SCENARIOS,
    HISTORICAL_FIGURES,
    MIGRATION_TIMELINE,
    EPIGENETIC_AGE_MARKERS,
    ARCHAIC_FUNCTIONAL_GENES,
    DIET_TRAINING_OPTIMIZER,
    FACIAL_RECONSTRUCTION,
    ANCESTRY_NARRATIVES
)


@dataclass
class SuperpowerResult:
    """Result for a genetic superpower"""
    name: str
    gene: str
    has_superpower: bool
    strength: str  # 'full', 'partial', 'none'
    description: str
    famous_carriers: List[str]
    population_frequency: float
    your_genotype: str
    rarity_percentile: float


@dataclass
class SurvivalResult:
    """Result for survival scenario simulation"""
    scenario: str
    survival_score: int  # 0-100
    rating: str  # 'Excellent', 'Good', 'Average', 'Poor', 'Critical'
    key_advantages: List[Dict[str, Any]]
    key_disadvantages: List[Dict[str, Any]]
    description: str
    markers_analyzed: int


@dataclass
class HistoricalMatchResult:
    """Result for historical figure DNA matching"""
    figure_name: str
    era: str
    location: str
    similarity_score: float  # 0-100
    shared_traits: List[str]
    shared_markers: int
    total_markers: int
    haplogroup_match: bool
    description: str


@dataclass
class FacialReconstructionResult:
    """Result for facial feature reconstruction"""
    feature_category: str
    predictions: Dict[str, Any]
    confidence: float
    markers_found: int


class UniqueFeaturesAnalysisEngine:
    """Analysis engine for all unique DNA features"""

    def __init__(self, snp_dict: Dict[str, str]):
        """Initialize with SNP dictionary"""
        self.snp_dict = snp_dict

    def _standardize_genotype(self, genotype: str) -> str:
        """Standardize genotype to alphabetical order"""
        if len(genotype) == 2:
            return ''.join(sorted(genotype))
        return genotype

    # =========================================================================
    # GENETIC SUPERPOWERS ANALYSIS
    # =========================================================================

    def analyze_superpowers(self) -> Dict[str, Any]:
        """
        Analyze DNA for rare beneficial mutations (superpowers)
        Returns list of superpowers found with strength levels
        """
        results = {
            'superpowers_found': [],
            'partial_superpowers': [],
            'total_analyzed': 0,
            'rarity_score': 0,
            'summary': ''
        }

        total_rarity = 0
        powers_found = 0

        for power_id, power_data in GENETIC_SUPERPOWERS.items():
            power_result = {
                'id': power_id,
                'name': power_data['name'],
                'gene': power_data['gene'],
                'description': power_data['description'],
                'famous_carriers': power_data['famous_carriers'],
                'population_frequency': power_data['population_frequency'],
                'status': 'none',
                'strength': 0,
                'genotypes': [],
                'rarity_percentile': 0
            }

            markers_checked = 0
            positive_markers = 0

            for rsid, marker_data in power_data['markers'].items():
                if rsid not in self.snp_dict:
                    continue

                markers_checked += 1
                user_genotype = self._standardize_genotype(self.snp_dict[rsid])
                superpower_allele = marker_data['superpower_allele']

                # Count superpower alleles in user's genotype
                allele_count = user_genotype.count(superpower_allele)

                power_result['genotypes'].append({
                    'rsid': rsid,
                    'variant_name': marker_data.get('variant_name', ''),
                    'your_genotype': user_genotype,
                    'superpower_allele': superpower_allele,
                    'allele_count': allele_count,
                    'effect': marker_data['effect'],
                    'frequencies': marker_data.get('frequencies', {})
                })

                if allele_count == 2:
                    positive_markers += 1
                    power_result['strength'] = max(power_result['strength'], 100)
                elif allele_count == 1:
                    positive_markers += 0.5
                    power_result['strength'] = max(power_result['strength'], 50)

            results['total_analyzed'] += markers_checked

            if markers_checked > 0:
                # Calculate rarity percentile (how rare this combination is)
                freq = power_data['population_frequency']
                if power_result['strength'] >= 100:
                    power_result['rarity_percentile'] = 100 - (freq * 100)
                    power_result['status'] = 'full'
                    results['superpowers_found'].append(power_result)
                    powers_found += 1
                    total_rarity += (1 - freq)
                elif power_result['strength'] >= 50:
                    power_result['rarity_percentile'] = 100 - (freq * 200)  # Carriers more common
                    power_result['status'] = 'partial'
                    results['partial_superpowers'].append(power_result)
                    total_rarity += (1 - freq) * 0.5

        # Calculate overall rarity score
        if powers_found > 0:
            results['rarity_score'] = min(100, int(total_rarity * 50 + powers_found * 10))

        # Generate summary
        full_count = len(results['superpowers_found'])
        partial_count = len(results['partial_superpowers'])

        if full_count > 0:
            results['summary'] = f"You have {full_count} genetic superpower(s) and are a carrier for {partial_count} more!"
        elif partial_count > 0:
            results['summary'] = f"You carry genes for {partial_count} potential superpower(s)."
        else:
            results['summary'] = "No rare superpower variants detected, but you may have other unique traits."

        return results

    # =========================================================================
    # SURVIVAL SCENARIO SIMULATION
    # =========================================================================

    def analyze_survival_scenarios(self) -> Dict[str, Any]:
        """
        Simulate survival in various historical scenarios
        Returns survival scores and analysis for each scenario
        """
        results = {
            'scenarios': [],
            'best_scenario': None,
            'worst_scenario': None,
            'overall_adaptability': 0
        }

        total_score = 0
        scenario_count = 0

        for scenario_id, scenario_data in SURVIVAL_SCENARIOS.items():
            scenario_result = {
                'id': scenario_id,
                'name': scenario_data['name'],
                'description': scenario_data['description'],
                'time_period': scenario_data['time_period'],
                'survival_score': 50,  # Base score
                'advantages': [],
                'disadvantages': [],
                'markers_analyzed': 0,
                'rating': 'Average'
            }

            bonus_points = 0
            penalty_points = 0

            for rsid, marker_data in scenario_data['markers'].items():
                if rsid not in self.snp_dict:
                    continue

                scenario_result['markers_analyzed'] += 1
                user_genotype = self._standardize_genotype(self.snp_dict[rsid])
                beneficial_allele = marker_data['beneficial_allele']

                allele_count = user_genotype.count(beneficial_allele)
                survival_boost = marker_data['survival_boost']

                trait_result = {
                    'trait': marker_data['trait'],
                    'gene': marker_data['gene'],
                    'your_genotype': user_genotype,
                    'beneficial_allele': beneficial_allele,
                    'effect': marker_data['effect']
                }

                if allele_count == 2:
                    bonus_points += survival_boost
                    trait_result['status'] = 'Optimal'
                    trait_result['boost'] = survival_boost
                    scenario_result['advantages'].append(trait_result)
                elif allele_count == 1:
                    bonus_points += survival_boost * 0.5
                    trait_result['status'] = 'Partial'
                    trait_result['boost'] = survival_boost * 0.5
                    scenario_result['advantages'].append(trait_result)
                else:
                    penalty_points += survival_boost * 0.3
                    trait_result['status'] = 'Absent'
                    trait_result['penalty'] = survival_boost * 0.3
                    scenario_result['disadvantages'].append(trait_result)

            # Calculate final score
            scenario_result['survival_score'] = int(min(100, max(0, 50 + bonus_points - penalty_points)))

            # Determine rating
            score = scenario_result['survival_score']
            if score >= 80:
                scenario_result['rating'] = 'Excellent'
            elif score >= 65:
                scenario_result['rating'] = 'Good'
            elif score >= 50:
                scenario_result['rating'] = 'Average'
            elif score >= 35:
                scenario_result['rating'] = 'Poor'
            else:
                scenario_result['rating'] = 'Critical'

            results['scenarios'].append(scenario_result)
            total_score += scenario_result['survival_score']
            scenario_count += 1

        # Sort and find best/worst
        results['scenarios'].sort(key=lambda x: x['survival_score'], reverse=True)

        if results['scenarios']:
            results['best_scenario'] = results['scenarios'][0]
            results['worst_scenario'] = results['scenarios'][-1]
            results['overall_adaptability'] = int(total_score / scenario_count) if scenario_count > 0 else 50

        return results

    # =========================================================================
    # HISTORICAL FIGURE DNA MATCHING
    # =========================================================================

    def analyze_historical_matches(self, user_haplogroups: Dict[str, str] = None) -> Dict[str, Any]:
        """
        Compare user's DNA to historical figures
        Returns similarity scores and shared traits
        """
        results = {
            'matches': [],
            'closest_match': None,
            'interesting_connections': []
        }

        for figure_id, figure_data in HISTORICAL_FIGURES.items():
            match_result = {
                'id': figure_id,
                'name': figure_data['name'],
                'era': figure_data['era'],
                'location': figure_data['location'],
                'description': figure_data['description'],
                'haplogroups': figure_data['haplogroups'],
                'known_traits': figure_data['traits'],
                'similarity_score': 0,
                'shared_markers': 0,
                'total_markers': 0,
                'shared_traits': [],
                'haplogroup_match': False
            }

            # Check haplogroup matches
            if user_haplogroups:
                # Handle nested haplogroup structure (e.g., {'Y_DNA': {'haplogroup': 'R1b', ...}})
                user_ydna = user_haplogroups.get('Y_DNA', {})
                user_ydna_haplo = user_ydna.get('haplogroup', '') if isinstance(user_ydna, dict) else str(user_ydna)

                user_mtdna = user_haplogroups.get('mtDNA', {})
                user_mtdna_haplo = user_mtdna.get('haplogroup', '') if isinstance(user_mtdna, dict) else str(user_mtdna)

                figure_ydna = figure_data['haplogroups'].get('Y_DNA', '')
                figure_mtdna = figure_data['haplogroups'].get('mtDNA', '')

                if figure_ydna and user_ydna_haplo:
                    if user_ydna_haplo.startswith(figure_ydna[:2] if len(figure_ydna) >= 2 else figure_ydna):
                        match_result['haplogroup_match'] = True
                        match_result['shared_traits'].append(f"Y-DNA lineage ({figure_ydna})")

                if figure_mtdna and user_mtdna_haplo:
                    if user_mtdna_haplo.startswith(figure_mtdna[0] if figure_mtdna else ''):
                        match_result['haplogroup_match'] = True
                        match_result['shared_traits'].append(f"mtDNA lineage ({figure_mtdna})")

            # Check SNP markers
            for rsid, marker_data in figure_data['markers'].items():
                match_result['total_markers'] += 1

                if rsid not in self.snp_dict:
                    continue

                user_genotype = self._standardize_genotype(self.snp_dict[rsid])
                figure_genotype = self._standardize_genotype(marker_data['genotype'])

                if user_genotype == figure_genotype:
                    match_result['shared_markers'] += 1
                    match_result['shared_traits'].append(marker_data['trait'])
                elif len(set(user_genotype) & set(figure_genotype)) > 0:
                    match_result['shared_markers'] += 0.5

            # Calculate similarity score
            if match_result['total_markers'] > 0:
                base_score = (match_result['shared_markers'] / match_result['total_markers']) * 100
                haplogroup_bonus = 15 if match_result['haplogroup_match'] else 0
                match_result['similarity_score'] = min(100, base_score + haplogroup_bonus)

            results['matches'].append(match_result)

        # Sort by similarity
        results['matches'].sort(key=lambda x: x['similarity_score'], reverse=True)

        if results['matches']:
            results['closest_match'] = results['matches'][0]

            # Find interesting connections (score > 50%)
            results['interesting_connections'] = [
                m for m in results['matches']
                if m['similarity_score'] >= 50
            ][:5]

        return results

    # =========================================================================
    # DNA TIME MACHINE / MIGRATION ANALYSIS
    # =========================================================================

    def analyze_time_machine(self, ancestry_results: Dict = None, haplogroups: Dict = None) -> Dict[str, Any]:
        """
        Create a timeline of ancestral migration based on haplogroups and ancestry
        Returns migration paths with dates and locations
        """
        results = {
            'maternal_journey': [],
            'paternal_journey': [],
            'ancestry_timeline': [],
            'key_migrations': [],
            'ancient_origins': {}
        }

        # Analyze mtDNA migration path
        if haplogroups and haplogroups.get('mtDNA'):
            mtdna_data = haplogroups['mtDNA']
            # Handle nested structure
            mtdna = mtdna_data.get('haplogroup', '') if isinstance(mtdna_data, dict) else str(mtdna_data)
            base_haplo = mtdna[0] if mtdna else ''

            # Build migration path
            for haplo, data in MIGRATION_TIMELINE['mtDNA_haplogroups'].items():
                if haplo == base_haplo or (mtdna and mtdna.startswith(haplo)):
                    results['maternal_journey'].append({
                        'haplogroup': haplo,
                        'origin': data['origin'],
                        'age': data['age'],
                        'age_formatted': self._format_years_ago(data['age']),
                        'migration': data['migration']
                    })

        # Analyze Y-DNA migration path
        if haplogroups and haplogroups.get('Y_DNA'):
            ydna_data = haplogroups['Y_DNA']
            # Handle nested structure
            ydna = ydna_data.get('haplogroup', '') if isinstance(ydna_data, dict) else str(ydna_data)
            base_haplo = ydna.split('-')[0] if ydna else ''

            for haplo, data in MIGRATION_TIMELINE['Y_DNA_haplogroups'].items():
                if haplo == base_haplo or (ydna and ydna.startswith(haplo)):
                    results['paternal_journey'].append({
                        'haplogroup': haplo,
                        'origin': data['origin'],
                        'age': data['age'],
                        'age_formatted': self._format_years_ago(data['age']),
                        'migration': data['migration']
                    })

        # Add ancestry timeline based on continental ancestry
        if ancestry_results:
            continental = ancestry_results.get('regional_summary', {})

            for continent, percentage in continental.items():
                if percentage < 5:
                    continue

                time_depths = MIGRATION_TIMELINE['ancestry_time_depths'].get(continent, {})
                for component, data in time_depths.items():
                    results['ancestry_timeline'].append({
                        'component': component.replace('_', ' '),
                        'continent': continent,
                        'era': data['era'],
                        'estimated_percentage': f"{data['percentage_range'][0]}-{data['percentage_range'][1]}%",
                        'your_continental': f"{percentage:.1f}%"
                    })

        # Sort timelines by age
        results['maternal_journey'].sort(key=lambda x: x['age'], reverse=True)
        results['paternal_journey'].sort(key=lambda x: x['age'], reverse=True)

        return results

    def _format_years_ago(self, years: int) -> str:
        """Format years ago into readable string"""
        if years >= 100000:
            return f"{years // 1000:,}+ thousand years ago"
        elif years >= 10000:
            return f"{years // 1000:,} thousand years ago"
        else:
            return f"{years:,} years ago"

    # =========================================================================
    # EPIGENETIC AGE CALCULATION
    # =========================================================================

    def analyze_epigenetic_age(self, chronological_age: int = 30) -> Dict[str, Any]:
        """
        Calculate biological age based on longevity markers
        Returns biological age estimate and factors
        """
        results = {
            'chronological_age': chronological_age,
            'biological_age': chronological_age,
            'age_difference': 0,
            'longevity_score': 50,
            'positive_factors': [],
            'negative_factors': [],
            'telomere_factors': [],
            'dna_repair_factors': [],
            'recommendations': [],
            'markers_analyzed': 0
        }

        age_modifier = 0
        longevity_points = 0

        # Analyze longevity positive markers
        for rsid, marker_data in EPIGENETIC_AGE_MARKERS['longevity_positive'].items():
            if rsid not in self.snp_dict:
                continue

            results['markers_analyzed'] += 1
            user_genotype = self._standardize_genotype(self.snp_dict[rsid])
            beneficial = marker_data['beneficial_allele']

            allele_count = user_genotype.count(beneficial)

            factor = {
                'gene': marker_data['gene'],
                'rsid': rsid,
                'your_genotype': user_genotype,
                'beneficial_allele': beneficial,
                'effect': marker_data['effect']
            }

            if allele_count == 2:
                age_modifier += marker_data['age_modifier']
                longevity_points += 10
                factor['status'] = 'Optimal'
                factor['impact'] = f"{marker_data['age_modifier']:.1f} years younger"
                results['positive_factors'].append(factor)
            elif allele_count == 1:
                age_modifier += marker_data['age_modifier'] * 0.5
                longevity_points += 5
                factor['status'] = 'Partial'
                factor['impact'] = f"{marker_data['age_modifier'] * 0.5:.1f} years younger"
                results['positive_factors'].append(factor)

        # Analyze longevity negative markers
        for rsid, marker_data in EPIGENETIC_AGE_MARKERS['longevity_negative'].items():
            if rsid not in self.snp_dict:
                continue

            results['markers_analyzed'] += 1
            user_genotype = self._standardize_genotype(self.snp_dict[rsid])
            risk = marker_data['risk_allele']

            allele_count = user_genotype.count(risk)

            factor = {
                'gene': marker_data['gene'],
                'rsid': rsid,
                'your_genotype': user_genotype,
                'risk_allele': risk,
                'effect': marker_data['effect']
            }

            if allele_count == 2:
                age_modifier += marker_data['age_modifier']
                longevity_points -= 10
                factor['status'] = 'Risk'
                factor['impact'] = f"+{marker_data['age_modifier']:.1f} years"
                results['negative_factors'].append(factor)
            elif allele_count == 1:
                age_modifier += marker_data['age_modifier'] * 0.5
                longevity_points -= 5
                factor['status'] = 'Carrier'
                factor['impact'] = f"+{marker_data['age_modifier'] * 0.5:.1f} years"
                results['negative_factors'].append(factor)

        # Analyze telomere markers
        for rsid, marker_data in EPIGENETIC_AGE_MARKERS['telomere_maintenance'].items():
            if rsid not in self.snp_dict:
                continue

            results['markers_analyzed'] += 1
            user_genotype = self._standardize_genotype(self.snp_dict[rsid])
            beneficial = marker_data['beneficial_allele']

            allele_count = user_genotype.count(beneficial)

            factor = {
                'gene': marker_data['gene'],
                'rsid': rsid,
                'your_genotype': user_genotype,
                'effect': marker_data['effect']
            }

            if allele_count >= 1:
                modifier = marker_data['age_modifier'] * (allele_count / 2)
                age_modifier += modifier
                longevity_points += 5 * allele_count
                factor['status'] = 'Beneficial'
                factor['impact'] = f"{modifier:.1f} years younger"
            else:
                factor['status'] = 'Neutral'
                factor['impact'] = 'No effect'

            results['telomere_factors'].append(factor)

        # Analyze DNA repair markers
        for rsid, marker_data in EPIGENETIC_AGE_MARKERS['dna_repair'].items():
            if rsid not in self.snp_dict:
                continue

            results['markers_analyzed'] += 1
            user_genotype = self._standardize_genotype(self.snp_dict[rsid])
            beneficial = marker_data['beneficial_allele']

            allele_count = user_genotype.count(beneficial)

            factor = {
                'gene': marker_data['gene'],
                'rsid': rsid,
                'your_genotype': user_genotype,
                'effect': marker_data['effect']
            }

            if allele_count >= 1:
                modifier = marker_data['age_modifier'] * (allele_count / 2)
                age_modifier += modifier
                longevity_points += 3 * allele_count
                factor['status'] = 'Efficient'
            else:
                factor['status'] = 'Standard'

            results['dna_repair_factors'].append(factor)

        # Calculate final biological age
        results['biological_age'] = max(0, chronological_age + age_modifier)
        results['age_difference'] = age_modifier
        results['longevity_score'] = min(100, max(0, 50 + longevity_points))

        # Generate recommendations
        if results['age_difference'] > 0:
            results['recommendations'].append("Focus on anti-inflammatory diet (Mediterranean)")
            results['recommendations'].append("Regular cardiovascular exercise")
            results['recommendations'].append("Consider NAD+ precursors (after consulting doctor)")
        if any(f['gene'] == 'APOE' for f in results['negative_factors']):
            results['recommendations'].append("Extra focus on brain health - omega-3, cognitive exercise")
        if any(f['gene'] == 'MTHFR' for f in results['negative_factors']):
            results['recommendations'].append("Consider methylfolate supplementation")

        return results

    # =========================================================================
    # ENHANCED ARCHAIC DNA ANALYSIS
    # =========================================================================

    def analyze_archaic_dna(self) -> Dict[str, Any]:
        """
        Detailed analysis of Neanderthal and Denisovan DNA with functional effects
        Returns specific genes inherited and their effects
        """
        results = {
            'neanderthal': {
                'percentage_estimate': 0,
                'functional_genes': [],
                'by_category': {},
                'markers_found': 0,
                'total_markers': 0
            },
            'denisovan': {
                'percentage_estimate': 0,
                'functional_genes': [],
                'markers_found': 0,
                'total_markers': 0
            },
            'summary': '',
            'interesting_findings': []
        }

        # Analyze Neanderthal genes
        for category, markers in ARCHAIC_FUNCTIONAL_GENES['neanderthal'].items():
            category_results = []

            for rsid, marker_data in markers.items():
                results['neanderthal']['total_markers'] += 1

                if rsid not in self.snp_dict:
                    continue

                user_genotype = self._standardize_genotype(self.snp_dict[rsid])
                neanderthal_allele = marker_data['neanderthal_allele']

                allele_count = user_genotype.count(neanderthal_allele)

                if allele_count > 0:
                    results['neanderthal']['markers_found'] += 1

                    gene_result = {
                        'rsid': rsid,
                        'gene': marker_data['gene'],
                        'function': marker_data['function'],
                        'effect': marker_data['effect'],
                        'your_genotype': user_genotype,
                        'neanderthal_allele': neanderthal_allele,
                        'copies': allele_count,
                        'category': category
                    }

                    results['neanderthal']['functional_genes'].append(gene_result)
                    category_results.append(gene_result)

                    # Check for interesting findings
                    if marker_data['modern_frequency'] < 0.20:
                        results['interesting_findings'].append({
                            'type': 'neanderthal',
                            'gene': marker_data['gene'],
                            'finding': f"You carry a rare Neanderthal {marker_data['gene']} variant ({marker_data['effect']})"
                        })

            if category_results:
                results['neanderthal']['by_category'][category] = category_results

        # Analyze Denisovan genes
        for category, markers in ARCHAIC_FUNCTIONAL_GENES['denisovan'].items():
            for rsid, marker_data in markers.items():
                results['denisovan']['total_markers'] += 1

                if rsid not in self.snp_dict:
                    continue

                user_genotype = self._standardize_genotype(self.snp_dict[rsid])
                denisovan_allele = marker_data['denisovan_allele']

                allele_count = user_genotype.count(denisovan_allele)

                if allele_count > 0:
                    results['denisovan']['markers_found'] += 1

                    gene_result = {
                        'rsid': rsid,
                        'gene': marker_data['gene'],
                        'function': marker_data['function'],
                        'effect': marker_data['effect'],
                        'your_genotype': user_genotype,
                        'denisovan_allele': denisovan_allele,
                        'copies': allele_count
                    }

                    results['denisovan']['functional_genes'].append(gene_result)

                    # Tibetan altitude adaptation is especially interesting
                    if marker_data['gene'] == 'EPAS1':
                        results['interesting_findings'].append({
                            'type': 'denisovan',
                            'gene': 'EPAS1',
                            'finding': "You carry the Denisovan altitude adaptation gene (EPAS1) - the same variant that allows Tibetans to thrive at high altitudes!"
                        })

        # Calculate marker match rate (what % of our database markers they have)
        if results['neanderthal']['total_markers'] > 0:
            marker_pct = (results['neanderthal']['markers_found'] / results['neanderthal']['total_markers']) * 100
            results['neanderthal']['marker_match_rate'] = round(marker_pct, 1)

            # Estimated actual ancestry (scientific range for non-Africans: 1-4%)
            # Higher marker match = likely higher end of range
            # Average non-African has ~2% Neanderthal
            if marker_pct >= 40:
                results['neanderthal']['percentage_estimate'] = 2.5  # Above average
            elif marker_pct >= 25:
                results['neanderthal']['percentage_estimate'] = 2.0  # Average
            else:
                results['neanderthal']['percentage_estimate'] = 1.5  # Below average

        if results['denisovan']['total_markers'] > 0:
            marker_pct = (results['denisovan']['markers_found'] / results['denisovan']['total_markers']) * 100
            results['denisovan']['marker_match_rate'] = round(marker_pct, 1)

            # Estimated actual ancestry (most non-Oceanians: 0-1%, Oceanians: 3-6%)
            if marker_pct >= 50:
                results['denisovan']['percentage_estimate'] = 1.0  # Above average for non-Oceanians
            elif marker_pct >= 30:
                results['denisovan']['percentage_estimate'] = 0.5  # Some Denisovan
            else:
                results['denisovan']['percentage_estimate'] = 0.2  # Trace

        # Generate summary with both numbers
        neand_match = results['neanderthal'].get('marker_match_rate', 0)
        neand_ancestry = results['neanderthal']['percentage_estimate']
        denis_match = results['denisovan'].get('marker_match_rate', 0)
        denis_ancestry = results['denisovan']['percentage_estimate']

        results['summary'] = f"Neanderthal: ~{neand_ancestry}% of genome ({results['neanderthal']['markers_found']}/{results['neanderthal']['total_markers']} markers). "
        results['summary'] += f"Denisovan: ~{denis_ancestry}% of genome ({results['denisovan']['markers_found']}/{results['denisovan']['total_markers']} markers)."

        return results

    # =========================================================================
    # DIET & TRAINING OPTIMIZATION
    # =========================================================================

    def analyze_diet_training(self) -> Dict[str, Any]:
        """
        Generate personalized diet and training recommendations
        Returns optimized macros, supplements, and workout plans
        """
        results = {
            'diet_recommendations': {
                'macros': {},
                'micronutrients': [],
                'foods_to_emphasize': [],
                'foods_to_limit': []
            },
            'training_recommendations': {
                'optimal_style': '',
                'recovery_profile': '',
                'injury_prevention': [],
                'weekly_structure': []
            },
            'supplement_stack': [],
            'meal_timing': {},
            'caffeine_protocol': {},
            'markers_analyzed': 0
        }

        # Analyze macronutrient response
        fat_response = 'normal'
        carb_response = 'normal'
        protein_response = 'normal'

        # Fat sensitivity
        for rsid, marker_data in DIET_TRAINING_OPTIMIZER['macronutrient_response']['fat_sensitivity'].items():
            if rsid in self.snp_dict:
                results['markers_analyzed'] += 1
                genotype = self._standardize_genotype(self.snp_dict[rsid])
                if genotype in marker_data['alleles']:
                    response = marker_data['alleles'][genotype]
                    fat_response = response['response']
                    results['diet_recommendations']['macros']['fat'] = response['recommendation']

        # Carb sensitivity
        for rsid, marker_data in DIET_TRAINING_OPTIMIZER['macronutrient_response']['carb_sensitivity'].items():
            if rsid in self.snp_dict:
                results['markers_analyzed'] += 1
                genotype = self._standardize_genotype(self.snp_dict[rsid])
                if genotype in marker_data['alleles']:
                    response = marker_data['alleles'][genotype]
                    if response['response'] == 'high':
                        carb_response = 'high'
                    results['diet_recommendations']['macros']['carbs'] = response['recommendation']

        # Protein utilization
        for rsid, marker_data in DIET_TRAINING_OPTIMIZER['macronutrient_response']['protein_utilization'].items():
            if rsid in self.snp_dict:
                results['markers_analyzed'] += 1
                genotype = self._standardize_genotype(self.snp_dict[rsid])
                if genotype in marker_data['alleles']:
                    response = marker_data['alleles'][genotype]
                    protein_response = response['response']
                    results['diet_recommendations']['macros']['protein'] = response['recommendation']

        # Analyze micronutrient needs
        for nutrient, markers in DIET_TRAINING_OPTIMIZER['micronutrient_needs'].items():
            for rsid, marker_data in markers.items():
                if rsid in self.snp_dict:
                    results['markers_analyzed'] += 1
                    genotype = self._standardize_genotype(self.snp_dict[rsid])
                    if genotype in marker_data['alleles']:
                        rec = marker_data['alleles'][genotype]

                        nutrient_rec = {
                            'nutrient': nutrient.replace('_', ' ').title(),
                            'gene': marker_data['gene'],
                            'status': rec.get('status', 'unknown'),
                            'recommendation': rec.get('recommendation', rec.get('dose', ''))
                        }

                        if 'form' in rec:
                            nutrient_rec['preferred_form'] = rec['form']

                        results['diet_recommendations']['micronutrients'].append(nutrient_rec)

                        # Add to supplement stack if needed
                        if rec.get('status') in ['low', 'reduced', 'low_status', 'low_conversion']:
                            results['supplement_stack'].append({
                                'supplement': nutrient.replace('_', ' ').title(),
                                'reason': f"Genetic {rec['status']} - {marker_data['gene']}",
                                'dose': rec.get('dose', rec.get('recommendation', 'Consult practitioner'))
                            })

        # Analyze training response
        muscle_type = 'mixed'
        recovery = 'normal'
        injury_risk = 'normal'

        # Muscle type
        for rsid, marker_data in DIET_TRAINING_OPTIMIZER['training_response']['muscle_type'].items():
            if rsid in self.snp_dict:
                results['markers_analyzed'] += 1
                genotype = self._standardize_genotype(self.snp_dict[rsid])
                if genotype in marker_data['alleles']:
                    response = marker_data['alleles'][genotype]
                    muscle_type = response['type']
                    results['training_recommendations']['optimal_style'] = response['training']
                    results['training_recommendations']['recovery_profile'] = response['recovery']

        # VO2max potential
        for rsid, marker_data in DIET_TRAINING_OPTIMIZER['training_response']['vo2max_potential'].items():
            if rsid in self.snp_dict:
                results['markers_analyzed'] += 1
                genotype = self._standardize_genotype(self.snp_dict[rsid])
                if genotype in marker_data['alleles']:
                    response = marker_data['alleles'][genotype]
                    if not results['training_recommendations']['optimal_style']:
                        results['training_recommendations']['optimal_style'] = response['focus']

        # Injury risk
        for rsid, marker_data in DIET_TRAINING_OPTIMIZER['training_response']['injury_risk'].items():
            if rsid in self.snp_dict:
                results['markers_analyzed'] += 1
                genotype = self._standardize_genotype(self.snp_dict[rsid])
                if genotype in marker_data['alleles']:
                    response = marker_data['alleles'][genotype]
                    results['training_recommendations']['injury_prevention'].append({
                        'gene': marker_data['gene'],
                        'risk': response['risk'],
                        'recommendation': response['recommendation']
                    })

        # Recovery speed
        for rsid, marker_data in DIET_TRAINING_OPTIMIZER['training_response']['recovery_speed'].items():
            if rsid in self.snp_dict:
                results['markers_analyzed'] += 1
                genotype = self._standardize_genotype(self.snp_dict[rsid])
                if genotype in marker_data['alleles']:
                    response = marker_data['alleles'][genotype]
                    recovery = response['recovery']

        # Caffeine timing
        for rsid, marker_data in DIET_TRAINING_OPTIMIZER['training_response']['caffeine_timing'].items():
            if rsid in self.snp_dict:
                results['markers_analyzed'] += 1
                genotype = self._standardize_genotype(self.snp_dict[rsid])
                if genotype in marker_data['alleles']:
                    response = marker_data['alleles'][genotype]
                    results['caffeine_protocol'] = {
                        'metabolism': response['metabolism'],
                        'timing': response['timing'],
                        'gene': marker_data['gene']
                    }

        # Meal timing / chronotype
        for rsid, marker_data in DIET_TRAINING_OPTIMIZER['meal_timing']['chronotype'].items():
            if rsid in self.snp_dict:
                results['markers_analyzed'] += 1
                genotype = self._standardize_genotype(self.snp_dict[rsid])
                if genotype in marker_data['alleles']:
                    response = marker_data['alleles'][genotype]
                    results['meal_timing'] = {
                        'chronotype': response['type'],
                        'eating_window': response['eating_window']
                    }

        # Generate weekly training structure based on muscle type and recovery
        if muscle_type == 'Power/Sprint':
            results['training_recommendations']['weekly_structure'] = [
                'Day 1: Heavy compound lifts (squat, deadlift)',
                'Day 2: Active recovery / mobility',
                'Day 3: Upper body power (bench, rows)',
                'Day 4: Rest',
                'Day 5: Explosive training (jumps, throws)',
                'Day 6: Light cardio / skill work',
                'Day 7: Rest'
            ]
        elif muscle_type == 'Endurance':
            results['training_recommendations']['weekly_structure'] = [
                'Day 1: Long aerobic session',
                'Day 2: Tempo training / threshold work',
                'Day 3: Strength maintenance',
                'Day 4: Easy recovery session',
                'Day 5: Interval training',
                'Day 6: Long easy session',
                'Day 7: Rest or active recovery'
            ]
        else:
            results['training_recommendations']['weekly_structure'] = [
                'Day 1: Upper body strength',
                'Day 2: Lower body strength',
                'Day 3: Cardio / conditioning',
                'Day 4: Rest',
                'Day 5: Full body circuit',
                'Day 6: Aerobic endurance',
                'Day 7: Rest'
            ]

        # Food recommendations based on profile
        if carb_response == 'high':
            results['diet_recommendations']['foods_to_emphasize'].extend([
                'Leafy greens', 'Non-starchy vegetables', 'Lean proteins',
                'Nuts and seeds', 'Berries', 'Legumes'
            ])
            results['diet_recommendations']['foods_to_limit'].extend([
                'White bread/rice', 'Sugary drinks', 'Processed snacks',
                'High-glycemic fruits'
            ])
        else:
            results['diet_recommendations']['foods_to_emphasize'].extend([
                'Whole grains', 'Sweet potatoes', 'Fruits',
                'Lean proteins', 'Vegetables'
            ])

        if fat_response in ['high_sensitivity', 'enhanced']:
            results['diet_recommendations']['foods_to_limit'].extend([
                'Fatty red meat', 'Full-fat dairy', 'Fried foods'
            ])
            results['diet_recommendations']['foods_to_emphasize'].extend([
                'Fish', 'Olive oil', 'Avocado (in moderation)'
            ])

        return results

    # =========================================================================
    # ANCESTRY STORY GENERATION
    # =========================================================================

    def generate_ancestry_story(self, ancestry_results: Dict, haplogroups: Dict = None) -> Dict[str, Any]:
        """
        Generate a narrative story of ancestral history
        Returns personalized ancestry story with historical context
        """
        results = {
            'story_sections': [],
            'timeline': [],
            'key_events': [],
            'full_narrative': ''
        }

        # Get dominant ancestry
        regional = ancestry_results.get('regional_summary', {})

        # Sort by percentage
        sorted_ancestry = sorted(regional.items(), key=lambda x: x[1], reverse=True)

        # Build narrative for each significant ancestry
        full_story = []

        for continent, percentage in sorted_ancestry:
            if percentage < 5:
                continue

            if continent in ANCESTRY_NARRATIVES:
                for component, data in ANCESTRY_NARRATIVES[continent].items():
                    section = {
                        'title': component.replace('_', ' '),
                        'era': data['era'],
                        'narrative': data['narrative'],
                        'lifestyle': data['lifestyle'],
                        'diet': data['diet'],
                        'innovations': data['innovations'],
                        'your_percentage': percentage
                    }
                    results['story_sections'].append(section)

                    results['timeline'].append({
                        'era': data['era'],
                        'event': component.replace('_', ' '),
                        'continent': continent
                    })

                    full_story.append(f"\n## {component.replace('_', ' ')} ({data['era']})\n")
                    full_story.append(data['narrative'])
                    full_story.append(f"\n*Lifestyle:* {data['lifestyle']}")
                    full_story.append(f"\n*Diet:* {data['diet']}")
                    full_story.append(f"\n*Key innovations:* {data['innovations']}")

        # Add haplogroup journey if available
        if haplogroups:
            if haplogroups.get('mtDNA'):
                full_story.append(f"\n## Your Maternal Line (mtDNA: {haplogroups['mtDNA']})\n")
                full_story.append("Your mitochondrial DNA has been passed down from mother to daughter for thousands of generations, tracing an unbroken line back to Africa.")

            if haplogroups.get('Y_DNA'):
                full_story.append(f"\n## Your Paternal Line (Y-DNA: {haplogroups['Y_DNA']})\n")
                full_story.append("Your Y chromosome has been passed from father to son, marking the journey of your direct male ancestors across continents.")

        results['full_narrative'] = '\n'.join(full_story)

        return results

    # =========================================================================
    # FACIAL RECONSTRUCTION
    # =========================================================================

    def analyze_facial_features(self) -> Dict[str, Any]:
        """
        Reconstruct likely facial features from DNA
        Returns predicted facial characteristics with confidence
        """
        results = {
            'face_shape': {},
            'nose': {},
            'eyes': {},
            'lips': {},
            'chin_jaw': {},
            'cheekbones': {},
            'forehead': {},
            'ears': {},
            'hair': {},
            'skin': {},
            'overall_confidence': 0,
            'markers_found': 0,
            'total_markers': 0,
            'summary': {}
        }

        markers_found = 0
        total_markers = 0
        confidence_sum = 0

        # Process each facial feature category
        for category, markers in FACIAL_RECONSTRUCTION.items():
            category_results = {}

            for rsid, marker_data in markers.items():
                total_markers += 1

                if rsid not in self.snp_dict:
                    continue

                markers_found += 1
                user_genotype = self._standardize_genotype(self.snp_dict[rsid])

                if user_genotype in marker_data['alleles']:
                    effect = marker_data['alleles'][user_genotype]
                    importance = marker_data.get('importance', 'medium')

                    # Calculate confidence based on importance
                    conf_modifier = {'high': 1.0, 'medium': 0.7, 'low': 0.4}
                    base_conf = conf_modifier.get(importance, 0.5)

                    prediction = {
                        'trait': marker_data['trait'],
                        'gene': marker_data['gene'],
                        'rsid': rsid,
                        'your_genotype': user_genotype,
                        'prediction': effect.get('effect', effect.get('color', effect.get('tone', 'Unknown'))),
                        'confidence': base_conf,
                        'details': effect
                    }

                    confidence_sum += base_conf

                    # Store in appropriate category
                    category_key = category.replace('_features', '').replace('_', ' ')
                    if category_key not in results:
                        results[category_key] = {}
                    results[category_key][marker_data['trait']] = prediction

        results['markers_found'] = markers_found
        results['total_markers'] = total_markers
        results['overall_confidence'] = (confidence_sum / markers_found * 100) if markers_found > 0 else 0

        # Generate summary predictions
        results['summary'] = self._generate_facial_summary(results)

        return results

    def _generate_facial_summary(self, features: Dict) -> Dict[str, str]:
        """Generate human-readable facial summary"""
        summary = {}

        # Eye color
        if 'eyes' in features and 'Eye color' in features.get('eyes', {}):
            eye_data = features['eyes']['Eye color']
            summary['eye_color'] = eye_data['prediction']

        # Hair
        hair_features = features.get('hair', {})
        hair_desc = []
        if 'Hair color' in hair_features:
            hair_desc.append(hair_features['Hair color']['prediction'])
        if 'Hair thickness' in hair_features:
            hair_desc.append(hair_features['Hair thickness']['prediction'])
        if 'Hair curl' in hair_features:
            hair_desc.append(hair_features['Hair curl']['prediction'])
        if hair_desc:
            summary['hair'] = ', '.join(hair_desc)

        # Skin
        skin_features = features.get('skin', {})
        if 'Skin pigmentation' in skin_features:
            summary['skin_tone'] = skin_features['Skin pigmentation']['prediction']

        # Nose
        nose_features = features.get('nose', {})
        nose_desc = []
        if 'Nose pointiness' in nose_features:
            nose_desc.append(nose_features['Nose pointiness']['prediction'])
        if 'Nose bridge width' in nose_features:
            nose_desc.append(nose_features['Nose bridge width']['prediction'])
        if nose_desc:
            summary['nose'] = ', '.join(nose_desc)

        # Face shape
        face_features = features.get('face shape', {})
        if 'Overall face shape' in face_features:
            summary['face_shape'] = face_features['Overall face shape']['prediction']

        return summary


# =============================================================================
# COMPREHENSIVE MARKER COMPILER - ALL MARKERS FROM ALL DATABASES
# =============================================================================

# Import ALL databases for comprehensive marker compilation
try:
    from expanded_traits import (
        PHYSICAL_TRAITS_EXPANDED,
        HEALTH_TRAITS_EXPANDED,
        PHARMACOGENOMICS_EXPANDED,
        CARRIER_STATUS,
        IMMUNITY_EXPANDED,
        NUTRITION_EXPANDED,
        FITNESS_EXPANDED
    )
    HAS_EXPANDED_TRAITS = True
except ImportError:
    HAS_EXPANDED_TRAITS = False

try:
    from expanded_genetics_database import (
        ATHLETIC_GENES,
        ADAPTATION_GENETICS,
        POLYGENIC_RISK_SCORES,
        LONGEVITY_MARKERS
    )
    HAS_EXPANDED_GENETICS = True
except ImportError:
    HAS_EXPANDED_GENETICS = False

try:
    from advanced_traits_database import (
        FACIAL_FEATURES,
        CHRONOTYPE_GENETICS,
        PAIN_GENETICS,
        ADDICTION_GENETICS,
        MENTAL_GENETICS,
        SENSORY_GENETICS
    )
    HAS_ADVANCED_TRAITS = True
except ImportError:
    HAS_ADVANCED_TRAITS = False


def compile_all_markers(snp_dict: Dict[str, str],
                        superpowers_result: Dict,
                        archaic_result: Dict,
                        diet_result: Dict) -> Dict[str, Any]:
    """
    Compile ALL markers from ALL databases into one sorted list
    Only includes markers where user HAS the relevant variant
    Sorted by rarity (rarest first)
    """
    all_markers = []
    seen_rsids = set()  # Avoid duplicates
    markers_scanned = 0  # Track total markers looked at

    def standardize_genotype(gt):
        """Standardize genotype format"""
        if not gt or gt == '--' or gt == '00':
            return None
        gt = str(gt).upper().strip()
        # Sort alleles for consistency
        if len(gt) == 2:
            return ''.join(sorted(gt))
        return gt

    def check_has_variant(rsid, risk_allele=None):
        """Check if user has the variant allele, return copies count or 0"""
        if rsid not in snp_dict:
            return 0

        gt = standardize_genotype(snp_dict[rsid])
        if not gt:
            return 0

        if risk_allele:
            # Count how many copies of risk allele
            return gt.count(risk_allele.upper())

        # If no specific allele, just confirm they have data
        return 1 if gt and gt != '--' else 0

    def add_marker(rsid, gene, name, effect, category, category_color, origin, rarity,
                   risk_allele=None, require_variant=True, copies_override=None, variant_name=None):
        """Helper to add marker only if user has the variant"""
        nonlocal markers_scanned
        markers_scanned += 1  # Count every attempt

        if rsid in seen_rsids:
            return

        if rsid not in snp_dict:
            return

        user_genotype = standardize_genotype(snp_dict.get(rsid, ''))
        if not user_genotype:
            return

        # Check if user has the variant
        if require_variant and risk_allele:
            copies = check_has_variant(rsid, risk_allele)
            if copies == 0:
                return  # User doesn't have this variant
        else:
            copies = copies_override if copies_override else 1

        seen_rsids.add(rsid)

        # Format rarity label
        if rarity >= 0.50:
            rarity_label = f"{rarity*100:.0f}% (common)"
        elif rarity >= 0.10:
            rarity_label = f"{rarity*100:.0f}% of people"
        elif rarity >= 0.01:
            rarity_label = f"1 in {int(1/rarity):,}"
        else:
            rarity_label = f"1 in {int(1/rarity):,} (very rare)"

        all_markers.append({
            'rsid': rsid,
            'variant_name': variant_name or '',
            'gene': gene,
            'name': name,
            'effect': effect,
            'category': category,
            'category_color': category_color,
            'origin': origin,
            'rarity': rarity,
            'rarity_label': rarity_label,
            'your_genotype': user_genotype,
            'copies': copies
        })

    # =========================================================================
    # 1. SUPERPOWERS (from analysis results - already verified)
    # =========================================================================
    for power in superpowers_result.get('superpowers_found', []):
        add_marker(
            power.get('rsid', 'N/A'), power['gene'], power['name'],
            power.get('description', '')[:150],
            'Superpower', '#22c55e', 'Human (rare)',
            power.get('population_frequency', 0.01),
            require_variant=False, copies_override=2
        )

    for power in superpowers_result.get('partial_superpowers', []):
        add_marker(
            power.get('rsid', 'N/A'), power['gene'], f"{power['name']} (Carrier)",
            power.get('description', '')[:150],
            'Superpower', '#eab308', 'Human (rare)',
            power.get('population_frequency', 0.05),
            require_variant=False, copies_override=1
        )

    # =========================================================================
    # 2. NEANDERTHAL GENES (already verified by archaic analysis)
    # =========================================================================
    for gene in archaic_result.get('neanderthal', {}).get('functional_genes', []):
        freq = 0.20
        for cat_data in ARCHAIC_FUNCTIONAL_GENES.get('neanderthal', {}).values():
            if gene['rsid'] in cat_data:
                freq = cat_data[gene['rsid']].get('modern_frequency', 0.20)
                break
        # These are already verified by archaic analysis, so skip variant check
        add_marker(
            gene['rsid'], gene['gene'], f"Neanderthal {gene['gene']}",
            gene['effect'],
            gene.get('category', 'Archaic').replace('_', ' ').title(),
            '#ef4444', 'Neanderthal', freq,
            require_variant=False, copies_override=gene['copies']
        )

    # =========================================================================
    # 3. DENISOVAN GENES (already verified by archaic analysis)
    # =========================================================================
    for gene in archaic_result.get('denisovan', {}).get('functional_genes', []):
        freq = 0.10
        for cat_data in ARCHAIC_FUNCTIONAL_GENES.get('denisovan', {}).values():
            if gene['rsid'] in cat_data:
                freq = cat_data[gene['rsid']].get('modern_frequency', 0.10)
                break
        add_marker(
            gene['rsid'], gene['gene'], f"Denisovan {gene['gene']}",
            gene['effect'], 'Archaic', '#3b82f6', 'Denisovan', freq,
            require_variant=False, copies_override=gene['copies']
        )

    # =========================================================================
    # 4. TRAITS FROM EXPANDED DATABASES
    # Only include markers where we have effect_allele and user has it
    # =========================================================================
    if HAS_EXPANDED_TRAITS:
        # Physical traits - only if effect_allele defined and user has it
        for trait_name, trait_data in PHYSICAL_TRAITS_EXPANDED.items():
            markers = trait_data.get('markers', {})
            for rsid, marker_info in markers.items():
                effect_allele = marker_info.get('effect_allele') or marker_info.get('risk_allele')
                if effect_allele and rsid in snp_dict:
                    freq = marker_info.get('frequency', 0.30)
                    add_marker(
                        rsid, marker_info.get('gene', trait_name),
                        trait_name.replace('_', ' ').title(),
                        marker_info.get('effect', trait_data.get('description', '')),
                        'Physical', '#a855f7', 'Human', freq,
                        risk_allele=effect_allele, require_variant=True
                    )

        # Health traits
        for trait_name, trait_data in HEALTH_TRAITS_EXPANDED.items():
            markers = trait_data.get('markers', {})
            for rsid, marker_info in markers.items():
                effect_allele = marker_info.get('effect_allele') or marker_info.get('risk_allele')
                if effect_allele and rsid in snp_dict:
                    freq = marker_info.get('frequency', 0.25)
                    add_marker(
                        rsid, marker_info.get('gene', trait_name),
                        trait_name.replace('_', ' ').title(),
                        marker_info.get('effect', trait_data.get('description', '')),
                        'Health', '#06b6d4', 'Human', freq,
                        risk_allele=effect_allele, require_variant=True
                    )

        # Pharmacogenomics - include these as they're about drug response
        for drug_name, drug_data in PHARMACOGENOMICS_EXPANDED.items():
            genes = drug_data.get('genes', {})
            for gene_name, gene_data in genes.items():
                markers = gene_data.get('markers', {})
                for rsid, marker_info in markers.items():
                    effect_allele = marker_info.get('effect_allele') or marker_info.get('variant_allele')
                    if effect_allele and rsid in snp_dict:
                        freq = marker_info.get('frequency', 0.20)
                        add_marker(
                            rsid, gene_name,
                            f"{drug_name} Response ({gene_name})",
                            marker_info.get('effect', f"Affects {drug_name} metabolism"),
                            'Drug Response', '#f97316', 'Human', freq,
                            risk_allele=effect_allele, require_variant=True
                        )

        # Carrier status - ONLY show if user has the carrier allele
        for condition, cond_data in CARRIER_STATUS.items():
            markers = cond_data.get('markers', {})
            for rsid, marker_info in markers.items():
                risk_allele = marker_info.get('risk_allele') or marker_info.get('carrier_allele')
                if risk_allele and rsid in snp_dict:
                    freq = marker_info.get('carrier_frequency', 0.02)
                    add_marker(
                        rsid, marker_info.get('gene', condition),
                        f"{condition.replace('_', ' ').title()} Carrier",
                        marker_info.get('effect', f"Carrier for {condition}"),
                        'Carrier', '#dc2626', 'Human', freq,
                        risk_allele=risk_allele, require_variant=True
                    )

    # =========================================================================
    # 5. SKIP external databases that don't have verified allele info
    # Only use pre-analyzed results from superpowers, archaic, diet
    # =========================================================================

    # =========================================================================
    # 7. DIET/TRAINING MARKERS
    # =========================================================================
    for category, cat_data in DIET_TRAINING_OPTIMIZER.items():
        if isinstance(cat_data, dict):
            for sub_cat, sub_data in cat_data.items():
                if isinstance(sub_data, dict):
                    for rsid, marker_info in sub_data.items():
                        if rsid.startswith('rs') and rsid in snp_dict:
                            gene = marker_info.get('gene', sub_cat)
                            add_marker(
                                rsid, gene,
                                f"Diet: {sub_cat.replace('_', ' ').title()}",
                                f"Affects {sub_cat.replace('_', ' ')}",
                                'Diet/Training', '#f97316', 'Human', 0.30
                            )

    # =========================================================================
    # 8. SURVIVAL SCENARIO MARKERS
    # =========================================================================
    for scenario_name, scenario_data in SURVIVAL_SCENARIOS.items():
        markers = scenario_data.get('genetic_factors', {})
        for rsid, marker_info in markers.items():
            if rsid in snp_dict:
                freq = marker_info.get('frequency', 0.25)
                add_marker(
                    rsid, marker_info.get('gene', scenario_name),
                    f"Survival: {scenario_name.replace('_', ' ').title()}",
                    marker_info.get('effect', marker_info.get('description', '')),
                    'Survival', '#059669', 'Human', freq
                )

    # Sort by rarity (rarest first = lowest frequency)
    all_markers.sort(key=lambda x: x['rarity'])

    # Add rank
    for i, marker in enumerate(all_markers):
        marker['rank'] = i + 1

    # Stats
    stats = {
        'total_markers': len(all_markers),
        'markers_scanned': markers_scanned,  # Total markers we looked at
        'superpowers': len([m for m in all_markers if 'Superpower' in m['category']]),
        'neanderthal': len([m for m in all_markers if m['origin'] == 'Neanderthal']),
        'denisovan': len([m for m in all_markers if m['origin'] == 'Denisovan']),
        'health': len([m for m in all_markers if m['category'] == 'Health']),
        'physical': len([m for m in all_markers if m['category'] == 'Physical']),
        'drug_response': len([m for m in all_markers if m['category'] == 'Drug Response']),
        'rarest': all_markers[0] if all_markers else None,
        'by_category': {},
        'by_origin': {}
    }

    for marker in all_markers:
        cat = marker['category']
        if cat not in stats['by_category']:
            stats['by_category'][cat] = 0
        stats['by_category'][cat] += 1

        origin = marker['origin']
        if origin not in stats['by_origin']:
            stats['by_origin'][origin] = 0
        stats['by_origin'][origin] += 1

    return {
        'markers': all_markers,
        'stats': stats
    }


# =============================================================================
# INTEGRATION FUNCTION
# =============================================================================

def run_unique_features_analysis(snp_dict: Dict[str, str],
                                  ancestry_results: Dict = None,
                                  haplogroups: Dict = None,
                                  chronological_age: int = 30) -> Dict[str, Any]:
    """
    Run all unique feature analyses
    Returns comprehensive results dictionary
    """
    engine = UniqueFeaturesAnalysisEngine(snp_dict)

    # Run individual analyses
    superpowers = engine.analyze_superpowers()
    archaic_dna = engine.analyze_archaic_dna()
    diet_training = engine.analyze_diet_training()

    # Compile all markers
    all_markers = compile_all_markers(snp_dict, superpowers, archaic_dna, diet_training)

    return {
        'superpowers': superpowers,
        'survival_scenarios': engine.analyze_survival_scenarios(),
        'historical_matches': engine.analyze_historical_matches(haplogroups),
        'time_machine': engine.analyze_time_machine(ancestry_results, haplogroups),
        'epigenetic_age': engine.analyze_epigenetic_age(chronological_age),
        'archaic_dna': archaic_dna,
        'diet_training': diet_training,
        'ancestry_story': engine.generate_ancestry_story(ancestry_results or {}, haplogroups),
        'facial_reconstruction': engine.analyze_facial_features(),
        'all_markers': all_markers
    }
