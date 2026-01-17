"""
Ancient DNA & History Genetics Database
Real SNP data for ancient ancestry and historical genetic markers

Features:
1. Neanderthal DNA markers
2. Denisovan DNA markers
3. Ancient European Farmer ancestry
4. Hunter-Gatherer ancestry
5. Steppe/Yamnaya ancestry
6. Ancient pathogen resistance
7. Lactase persistence historical context
8. Blue eye origin markers
9. Light skin adaptation
10. Historical migration markers
"""

from typing import Dict, Any, List, Optional

# Import larger archaic DNA marker set for consistent percentages
try:
    from unique_features_database import ARCHAIC_FUNCTIONAL_GENES
    USE_EXPANDED_ARCHAIC = True
except ImportError:
    USE_EXPANDED_ARCHAIC = False


def get_genotype_key(genotype, dict_keys):
    """Find matching genotype key trying all orientations."""
    if not genotype:
        return None
    genotype = genotype.upper()
    # Try exact
    if genotype in dict_keys:
        return genotype
    # Try reverse
    rev = genotype[::-1]
    if rev in dict_keys:
        return rev
    # Try complement (A<->T, G<->C)
    comp_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    comp = ''.join(comp_map.get(b, b) for b in genotype)
    if comp in dict_keys:
        return comp
    # Try reverse complement
    rev_comp = comp[::-1]
    if rev_comp in dict_keys:
        return rev_comp
    return None


# =============================================================================
# NEANDERTHAL DNA MARKERS
# =============================================================================

NEANDERTHAL_MARKERS = {
    # BNC2 - skin pigmentation, Neanderthal introgression
    "rs12913832": {
        "gene": "HERC2/OCA2",
        "chromosome": "15",
        "variant_name": "Intronic",
        "function": "Blue/brown eye color - contains ancient variants",
        "neanderthal_allele": None,  # Complex region
        "modern_human_allele": "A",
        "effect": {
            "GG": {"eye_color": "Brown", "ancient_note": "Ancestral variant"},
            "GA": {"eye_color": "Green/Hazel", "ancient_note": "Heterozygous"},
            "AA": {"eye_color": "Blue", "ancient_note": "Derived variant - appeared ~10,000 years ago"}
        }
    },
    # POU2F3 - Neanderthal introgression affecting keratinocytes
    "rs2298754": {
        "gene": "POU2F3",
        "chromosome": "11",
        "variant_name": "Intronic",
        "function": "Keratinocyte differentiation - Neanderthal derived",
        "neanderthal_allele": "T",
        "effect": {
            "TT": {"neanderthal_score": 2, "note": "Neanderthal variant homozygous"},
            "CT": {"neanderthal_score": 1, "note": "Neanderthal variant heterozygous"},
            "CC": {"neanderthal_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.05, "EAS": 0.30}
    },
    # STAT2 - Immune function, Neanderthal introgression
    "rs2066807": {
        "gene": "STAT2",
        "chromosome": "12",
        "variant_name": "Intronic",
        "function": "Immune signaling - Neanderthal introgression",
        "neanderthal_allele": "T",
        "effect": {
            "TT": {"neanderthal_score": 2, "immune_effect": "Neanderthal-type immune response"},
            "CT": {"neanderthal_score": 1, "immune_effect": "Mixed immune response"},
            "CC": {"neanderthal_score": 0, "immune_effect": "Modern human immune response"}
        },
        "population_frequency": {"EUR": 0.25, "AFR": 0.02, "EAS": 0.45}
    },
    # OAS1 - Antiviral defense, Neanderthal introgression
    "rs10774671": {
        "gene": "OAS1",
        "chromosome": "12",
        "variant_name": "Splice variant",
        "function": "Antiviral immune response - Neanderthal variant",
        "neanderthal_allele": "G",
        "effect": {
            "GG": {"neanderthal_score": 2, "antiviral": "Enhanced (Neanderthal variant)"},
            "AG": {"neanderthal_score": 1, "antiviral": "Mixed"},
            "AA": {"neanderthal_score": 0, "antiviral": "Standard modern human"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.03, "EAS": 0.30}
    },
    # TLR1/TLR6/TLR10 cluster - Neanderthal immune genes
    "rs5743618": {
        "gene": "TLR1",
        "chromosome": "4",
        "variant_name": "I602S",
        "function": "Innate immunity - Neanderthal haplotype",
        "neanderthal_allele": "T",
        "effect": {
            "TT": {"neanderthal_score": 2, "note": "Neanderthal TLR variant"},
            "GT": {"neanderthal_score": 1, "note": "Heterozygous"},
            "GG": {"neanderthal_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.25, "AFR": 0.01, "EAS": 0.50}
    },
    # SLC16A11 - Metabolic gene with Neanderthal variant
    "rs13342232": {
        "gene": "SLC16A11",
        "chromosome": "17",
        "variant_name": "Intronic",
        "function": "Lipid metabolism - Neanderthal variant (T2D risk in some populations)",
        "neanderthal_allele": "T",
        "effect": {
            "TT": {"neanderthal_score": 2, "metabolic": "Neanderthal lipid metabolism"},
            "CT": {"neanderthal_score": 1, "metabolic": "Mixed"},
            "CC": {"neanderthal_score": 0, "metabolic": "Modern human"}
        },
        "population_frequency": {"EUR": 0.02, "AFR": 0.01, "EAS": 0.08, "AMR": 0.25}
    },
    # BNC2 - Skin/hair pigmentation Neanderthal
    "rs10756819": {
        "gene": "BNC2",
        "chromosome": "9",
        "variant_name": "Intronic",
        "function": "Skin pigmentation - Neanderthal introgression",
        "neanderthal_allele": "A",
        "effect": {
            "AA": {"neanderthal_score": 2, "pigmentation": "Neanderthal-derived skin variant"},
            "GA": {"neanderthal_score": 1, "pigmentation": "Heterozygous"},
            "GG": {"neanderthal_score": 0, "pigmentation": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.70, "AFR": 0.15, "EAS": 0.85}
    },
    # TLR6 - Part of Neanderthal immune haplotype
    "rs5743810": {
        "gene": "TLR6",
        "chromosome": "4",
        "variant_name": "P249S",
        "function": "Innate immunity TLR6 - Neanderthal haplotype member",
        "neanderthal_allele": "T",
        "effect": {
            "TT": {"neanderthal_score": 2, "note": "Neanderthal TLR6 variant"},
            "CT": {"neanderthal_score": 1, "note": "Heterozygous"},
            "CC": {"neanderthal_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.42, "AFR": 0.06, "EAS": 0.55}
    },
    # TLR10 - Part of Neanderthal TLR cluster
    "rs4129009": {
        "gene": "TLR10",
        "chromosome": "4",
        "variant_name": "N241H",
        "function": "Innate immunity TLR10 - Neanderthal derived",
        "neanderthal_allele": "A",
        "effect": {
            "AA": {"neanderthal_score": 2, "note": "Neanderthal TLR10 variant"},
            "GA": {"neanderthal_score": 1, "note": "Heterozygous"},
            "GG": {"neanderthal_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.02, "EAS": 0.48}
    },
    # OAS3 - Additional antiviral gene, Neanderthal introgression
    "rs1859330": {
        "gene": "OAS3",
        "chromosome": "12",
        "variant_name": "Intronic",
        "function": "Antiviral defense OAS3 - Neanderthal haplotype",
        "neanderthal_allele": "A",
        "effect": {
            "AA": {"neanderthal_score": 2, "antiviral": "Enhanced OAS3 (Neanderthal)"},
            "GA": {"neanderthal_score": 1, "antiviral": "Mixed"},
            "GG": {"neanderthal_score": 0, "antiviral": "Modern human"}
        },
        "population_frequency": {"EUR": 0.30, "AFR": 0.02, "EAS": 0.35}
    },
    # SLC6A11 - GABA transporter, Neanderthal introgression
    "rs2229940": {
        "gene": "SLC6A11",
        "chromosome": "3",
        "variant_name": "Intronic",
        "function": "GABA transporter - Neanderthal introgression affecting neurotransmission",
        "neanderthal_allele": "C",
        "effect": {
            "CC": {"neanderthal_score": 2, "note": "Neanderthal neural variant"},
            "CT": {"neanderthal_score": 1, "note": "Heterozygous"},
            "TT": {"neanderthal_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.15, "AFR": 0.01, "EAS": 0.25}
    },
    # SIRT1 - Metabolic/aging gene with archaic variant
    "rs3758391": {
        "gene": "SIRT1",
        "chromosome": "10",
        "variant_name": "Intronic",
        "function": "Metabolic regulation - contains Neanderthal-derived variants",
        "neanderthal_allele": "C",
        "effect": {
            "CC": {"neanderthal_score": 2, "note": "Neanderthal metabolic variant"},
            "CT": {"neanderthal_score": 1, "note": "Heterozygous"},
            "TT": {"neanderthal_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.25, "AFR": 0.05, "EAS": 0.30}
    },
    # CLOCK - Circadian rhythm, archaic variants
    "rs1801260": {
        "gene": "CLOCK",
        "chromosome": "4",
        "variant_name": "3'-UTR",
        "function": "Circadian clock - may contain archaic introgression",
        "neanderthal_allele": "C",
        "effect": {
            "CC": {"neanderthal_score": 2, "note": "Possible Neanderthal circadian variant"},
            "TC": {"neanderthal_score": 1, "note": "Heterozygous"},
            "TT": {"neanderthal_score": 0, "note": "Common modern variant"}
        },
        "population_frequency": {"EUR": 0.28, "AFR": 0.20, "EAS": 0.15}
    },
    # ZNF365 - Skin/hair, Neanderthal introgression
    "rs10995190": {
        "gene": "ZNF365",
        "chromosome": "10",
        "variant_name": "Intronic",
        "function": "Hair follicle development - Neanderthal introgression",
        "neanderthal_allele": "A",
        "effect": {
            "AA": {"neanderthal_score": 2, "note": "Neanderthal hair follicle variant"},
            "GA": {"neanderthal_score": 1, "note": "Heterozygous"},
            "GG": {"neanderthal_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.65, "AFR": 0.10, "EAS": 0.55}
    },
    # SPAG6 - Sperm motility, archaic introgression
    "rs2479106": {
        "gene": "SPAG6",
        "chromosome": "10",
        "variant_name": "Intronic",
        "function": "Sperm flagella - contains Neanderthal-derived variants",
        "neanderthal_allele": "A",
        "effect": {
            "AA": {"neanderthal_score": 2, "note": "Neanderthal reproductive variant"},
            "AG": {"neanderthal_score": 1, "note": "Heterozygous"},
            "GG": {"neanderthal_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.05, "EAS": 0.40}
    },
    # PDZD8 - Membrane contact sites, Neanderthal
    "rs6504950": {
        "gene": "PDZD8",
        "chromosome": "10",
        "variant_name": "Intronic",
        "function": "Cellular membrane contacts - Neanderthal introgression",
        "neanderthal_allele": "A",
        "effect": {
            "AA": {"neanderthal_score": 2, "note": "Neanderthal variant"},
            "GA": {"neanderthal_score": 1, "note": "Heterozygous"},
            "GG": {"neanderthal_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.40, "AFR": 0.08, "EAS": 0.45}
    },
    # ASB1 - Circadian/sleep, Neanderthal introgression
    "rs4481150": {
        "gene": "ASB1",
        "chromosome": "2",
        "variant_name": "Intronic",
        "function": "Sleep/circadian - Neanderthal introgression",
        "neanderthal_allele": "G",
        "effect": {
            "GG": {"neanderthal_score": 2, "note": "Neanderthal sleep variant"},
            "AG": {"neanderthal_score": 1, "note": "Heterozygous"},
            "AA": {"neanderthal_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.30, "AFR": 0.05, "EAS": 0.35}
    },
    # CACNA1C - Calcium channel, archaic introgression
    "rs1006737": {
        "gene": "CACNA1C",
        "chromosome": "12",
        "variant_name": "Intronic",
        "function": "Calcium channel - contains archaic variants affecting neural function",
        "neanderthal_allele": "A",
        "effect": {
            "AA": {"neanderthal_score": 2, "note": "Archaic neural variant"},
            "AG": {"neanderthal_score": 1, "note": "Heterozygous"},
            "GG": {"neanderthal_score": 0, "note": "Common modern variant"}
        },
        "population_frequency": {"EUR": 0.33, "AFR": 0.10, "EAS": 0.25}
    },
    # HYAL2 - Hyaluronan metabolism, Neanderthal
    "rs2072454": {
        "gene": "HYAL2",
        "chromosome": "3",
        "variant_name": "P250L",
        "function": "Hyaluronan catabolism - Neanderthal variant affecting wound healing",
        "neanderthal_allele": "T",
        "effect": {
            "TT": {"neanderthal_score": 2, "note": "Neanderthal wound healing variant"},
            "CT": {"neanderthal_score": 1, "note": "Heterozygous"},
            "CC": {"neanderthal_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.55, "AFR": 0.15, "EAS": 0.45}
    },
    # NOSTRIN - Blood clotting, Neanderthal introgression
    "rs12569998": {
        "gene": "NOSTRIN",
        "chromosome": "2",
        "variant_name": "Intronic",
        "function": "Nitric oxide trafficking - Neanderthal variant affecting clotting",
        "neanderthal_allele": "A",
        "effect": {
            "AA": {"neanderthal_score": 2, "note": "Neanderthal clotting variant"},
            "GA": {"neanderthal_score": 1, "note": "Heterozygous"},
            "GG": {"neanderthal_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.40, "AFR": 0.05, "EAS": 0.35}
    },
    # PPP1R3B - Glycogen synthesis, Neanderthal
    "rs9987289": {
        "gene": "PPP1R3B",
        "chromosome": "8",
        "variant_name": "Intronic",
        "function": "Glycogen storage - Neanderthal metabolic adaptation",
        "neanderthal_allele": "A",
        "effect": {
            "AA": {"neanderthal_score": 2, "note": "Neanderthal glycogen variant"},
            "AG": {"neanderthal_score": 1, "note": "Heterozygous"},
            "GG": {"neanderthal_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.10, "AFR": 0.02, "EAS": 0.08}
    },
    # LARGE - Glycosylation, archaic introgression
    "rs7545940": {
        "gene": "LARGE",
        "chromosome": "22",
        "variant_name": "Intronic",
        "function": "Protein glycosylation - archaic introgression",
        "neanderthal_allele": "A",
        "effect": {
            "AA": {"neanderthal_score": 2, "note": "Archaic glycosylation variant"},
            "AG": {"neanderthal_score": 1, "note": "Heterozygous"},
            "GG": {"neanderthal_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.08, "EAS": 0.40}
    },
    # DSCAML1 - Neural adhesion, Neanderthal
    "rs2237639": {
        "gene": "DSCAML1",
        "chromosome": "11",
        "variant_name": "Intronic",
        "function": "Neural cell adhesion - Neanderthal introgression",
        "neanderthal_allele": "G",
        "effect": {
            "GG": {"neanderthal_score": 2, "note": "Neanderthal neural adhesion variant"},
            "AG": {"neanderthal_score": 1, "note": "Heterozygous"},
            "AA": {"neanderthal_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.25, "AFR": 0.03, "EAS": 0.30}
    },
    # MTSS1 - Actin binding, Neanderthal introgression
    "rs4795218": {
        "gene": "MTSS1",
        "chromosome": "8",
        "variant_name": "Intronic",
        "function": "Actin cytoskeleton - Neanderthal introgression",
        "neanderthal_allele": "T",
        "effect": {
            "TT": {"neanderthal_score": 2, "note": "Neanderthal cytoskeleton variant"},
            "CT": {"neanderthal_score": 1, "note": "Heterozygous"},
            "CC": {"neanderthal_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.45, "AFR": 0.10, "EAS": 0.50}
    }
}

# =============================================================================
# DENISOVAN DNA MARKERS
# =============================================================================

DENISOVAN_MARKERS = {
    # EPAS1 - High altitude adaptation from Denisovans (Tibetan adaptation)
    "rs1868092": {
        "gene": "EPAS1",
        "chromosome": "2",
        "variant_name": "Intronic",
        "function": "High altitude adaptation - Denisovan introgression",
        "denisovan_allele": "G",
        "effect": {
            "GG": {"denisovan_score": 2, "altitude": "High altitude adapted (Denisovan variant)"},
            "AG": {"denisovan_score": 1, "altitude": "Partial adaptation"},
            "AA": {"denisovan_score": 0, "altitude": "Standard (no Denisovan variant)"}
        },
        "population_frequency": {"EUR": 0.01, "AFR": 0.001, "EAS": 0.05, "TIB": 0.85}
    },
    # TBX15/WARS2 - Body fat distribution, Denisovan introgression
    "rs2298080": {
        "gene": "TBX15",
        "chromosome": "1",
        "variant_name": "Intronic",
        "function": "Body fat distribution - Denisovan derived",
        "denisovan_allele": "C",
        "effect": {
            "CC": {"denisovan_score": 2, "note": "Denisovan body composition variant"},
            "CT": {"denisovan_score": 1, "note": "Heterozygous"},
            "TT": {"denisovan_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.10, "EAS": 0.55}
    },
    # EPAS1 additional SNP - altitude
    "rs13419896": {
        "gene": "EPAS1",
        "chromosome": "2",
        "variant_name": "Intronic",
        "function": "High altitude - additional EPAS1 Denisovan variant",
        "denisovan_allele": "A",
        "effect": {
            "AA": {"denisovan_score": 2, "altitude": "High altitude adapted"},
            "GA": {"denisovan_score": 1, "altitude": "Partial adaptation"},
            "GG": {"denisovan_score": 0, "altitude": "Standard"}
        },
        "population_frequency": {"EUR": 0.02, "AFR": 0.001, "EAS": 0.08, "TIB": 0.78}
    },
    # EGLN1 - Another altitude gene, Denisovan introgression
    "rs186996510": {
        "gene": "EGLN1",
        "chromosome": "1",
        "variant_name": "D4E",
        "function": "Oxygen sensing - Denisovan high altitude adaptation",
        "denisovan_allele": "G",
        "effect": {
            "GG": {"denisovan_score": 2, "altitude": "Denisovan oxygen sensing variant"},
            "AG": {"denisovan_score": 1, "altitude": "Partial adaptation"},
            "AA": {"denisovan_score": 0, "altitude": "Standard"}
        },
        "population_frequency": {"EUR": 0.001, "AFR": 0.001, "EAS": 0.02, "TIB": 0.65}
    },
    # HLA-A - Immune gene with Denisovan introgression
    "rs9260151": {
        "gene": "HLA-A",
        "chromosome": "6",
        "variant_name": "5'-upstream",
        "function": "Immune recognition HLA-A - Denisovan derived variants",
        "denisovan_allele": "G",
        "effect": {
            "GG": {"denisovan_score": 2, "note": "Denisovan immune variant"},
            "AG": {"denisovan_score": 1, "note": "Heterozygous"},
            "AA": {"denisovan_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.15, "AFR": 0.05, "EAS": 0.35, "OCE": 0.55}
    },
    # HLA-B - Immune, Denisovan introgression especially in Oceanians
    "rs2596477": {
        "gene": "HLA-B",
        "chromosome": "6",
        "variant_name": "Intronic",
        "function": "Immune recognition HLA-B - Denisovan variant (high in Oceania)",
        "denisovan_allele": "T",
        "effect": {
            "TT": {"denisovan_score": 2, "note": "Denisovan HLA variant"},
            "CT": {"denisovan_score": 1, "note": "Heterozygous"},
            "CC": {"denisovan_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.05, "AFR": 0.02, "EAS": 0.25, "OCE": 0.50}
    },
    # HLA-C - Denisovan immune introgression
    "rs3094072": {
        "gene": "HLA-C",
        "chromosome": "6",
        "variant_name": "5'-upstream",
        "function": "Immune recognition HLA-C - Denisovan derived",
        "denisovan_allele": "A",
        "effect": {
            "AA": {"denisovan_score": 2, "note": "Denisovan HLA-C variant"},
            "GA": {"denisovan_score": 1, "note": "Heterozygous"},
            "GG": {"denisovan_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.10, "AFR": 0.03, "EAS": 0.30, "OCE": 0.45}
    },
    # VARS2/WARS2 - Mitochondrial tRNA synthetase, Denisovan
    "rs4977575": {
        "gene": "WARS2",
        "chromosome": "1",
        "variant_name": "Intronic",
        "function": "Mitochondrial tRNA - Denisovan metabolic variant",
        "denisovan_allele": "G",
        "effect": {
            "GG": {"denisovan_score": 2, "note": "Denisovan mitochondrial variant"},
            "AG": {"denisovan_score": 1, "note": "Heterozygous"},
            "AA": {"denisovan_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.30, "AFR": 0.10, "EAS": 0.45, "OCE": 0.55}
    },
    # OCA2 - Pigmentation, some Denisovan variants
    "rs4778138": {
        "gene": "OCA2",
        "chromosome": "15",
        "variant_name": "Intronic",
        "function": "Pigmentation - contains Denisovan-derived variants",
        "denisovan_allele": "A",
        "effect": {
            "AA": {"denisovan_score": 2, "note": "Possible Denisovan pigmentation variant"},
            "GA": {"denisovan_score": 1, "note": "Heterozygous"},
            "GG": {"denisovan_score": 0, "note": "Common modern variant"}
        },
        "population_frequency": {"EUR": 0.25, "AFR": 0.40, "EAS": 0.15, "OCE": 0.50}
    },
    # STAT2 - Immune, shared archaic introgression
    "rs2066819": {
        "gene": "STAT2",
        "chromosome": "12",
        "variant_name": "Intronic",
        "function": "Immune signaling - Denisovan introgression (overlaps Neanderthal)",
        "denisovan_allele": "A",
        "effect": {
            "AA": {"denisovan_score": 2, "note": "Archaic immune variant"},
            "GA": {"denisovan_score": 1, "note": "Heterozygous"},
            "GG": {"denisovan_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.20, "AFR": 0.03, "EAS": 0.40, "OCE": 0.45}
    },
    # TNFAIP3 - Immune regulation, Denisovan
    "rs2230926": {
        "gene": "TNFAIP3",
        "chromosome": "6",
        "variant_name": "F127C",
        "function": "NF-kB signaling - Denisovan immune variant",
        "denisovan_allele": "G",
        "effect": {
            "GG": {"denisovan_score": 2, "note": "Denisovan immune regulation variant"},
            "TG": {"denisovan_score": 1, "note": "Heterozygous"},
            "TT": {"denisovan_score": 0, "note": "Common modern variant"}
        },
        "population_frequency": {"EUR": 0.05, "AFR": 0.02, "EAS": 0.15, "OCE": 0.30}
    },
    # PRKCE - Protein kinase, Denisovan introgression in Melanesians
    "rs3777415": {
        "gene": "PRKCE",
        "chromosome": "2",
        "variant_name": "Intronic",
        "function": "Protein kinase - Denisovan variant (Melanesian enriched)",
        "denisovan_allele": "T",
        "effect": {
            "TT": {"denisovan_score": 2, "note": "Denisovan signaling variant"},
            "CT": {"denisovan_score": 1, "note": "Heterozygous"},
            "CC": {"denisovan_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.05, "AFR": 0.02, "EAS": 0.15, "OCE": 0.45}
    },
    # BNC2 - Skin/hair, shared archaic (also Neanderthal)
    "rs2153271": {
        "gene": "BNC2",
        "chromosome": "9",
        "variant_name": "Intronic",
        "function": "Skin pigmentation - shared archaic introgression",
        "denisovan_allele": "T",
        "effect": {
            "TT": {"denisovan_score": 2, "note": "Archaic pigmentation variant"},
            "CT": {"denisovan_score": 1, "note": "Heterozygous"},
            "CC": {"denisovan_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.60, "AFR": 0.15, "EAS": 0.70, "OCE": 0.65}
    },
    # ADARB2 - RNA editing, Denisovan introgression
    "rs3738025": {
        "gene": "ADARB2",
        "chromosome": "10",
        "variant_name": "Intronic",
        "function": "RNA editing enzyme - Denisovan neural variant",
        "denisovan_allele": "T",
        "effect": {
            "TT": {"denisovan_score": 2, "note": "Denisovan RNA editing variant"},
            "CT": {"denisovan_score": 1, "note": "Heterozygous"},
            "CC": {"denisovan_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.08, "AFR": 0.02, "EAS": 0.20, "OCE": 0.40}
    },
    # SETBP1 - Transcription factor, Denisovan
    "rs11083846": {
        "gene": "SETBP1",
        "chromosome": "18",
        "variant_name": "Intronic",
        "function": "Transcription regulation - Denisovan developmental variant",
        "denisovan_allele": "A",
        "effect": {
            "AA": {"denisovan_score": 2, "note": "Denisovan transcription variant"},
            "GA": {"denisovan_score": 1, "note": "Heterozygous"},
            "GG": {"denisovan_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.10, "AFR": 0.03, "EAS": 0.25, "OCE": 0.35}
    },
    # ERCC2 - DNA repair, Denisovan variant
    "rs50871": {
        "gene": "ERCC2",
        "chromosome": "19",
        "variant_name": "D312N",
        "function": "DNA repair - Denisovan variant",
        "denisovan_allele": "A",
        "effect": {
            "AA": {"denisovan_score": 2, "note": "Denisovan DNA repair variant"},
            "GA": {"denisovan_score": 1, "note": "Heterozygous"},
            "GG": {"denisovan_score": 0, "note": "Modern human variant"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.20, "EAS": 0.45, "OCE": 0.50}
    },
    # FADS1/FADS2 - Fatty acid desaturase, archaic introgression
    "rs174570": {
        "gene": "FADS2",
        "chromosome": "11",
        "variant_name": "Intronic",
        "function": "Fatty acid metabolism - Denisovan diet adaptation",
        "denisovan_allele": "C",
        "effect": {
            "CC": {"denisovan_score": 2, "note": "Denisovan fatty acid variant"},
            "CT": {"denisovan_score": 1, "note": "Heterozygous"},
            "TT": {"denisovan_score": 0, "note": "Common modern variant"}
        },
        "population_frequency": {"EUR": 0.30, "AFR": 0.60, "EAS": 0.50, "OCE": 0.55}
    }
}

# =============================================================================
# ANCIENT EUROPEAN FARMER ANCESTRY (Early Neolithic)
# =============================================================================

ANCIENT_FARMER_MARKERS = {
    # LCT - Lactase persistence (spread with farmers)
    "rs4988235": {
        "gene": "LCT",
        "chromosome": "2",
        "variant_name": "-13910C>T",
        "function": "Lactase persistence - spread with Neolithic farmers",
        "farmer_allele": "A",  # Actually derived mutation that allowed milk drinking
        "effect": {
            "AA": {"lactase": "Persistent", "historical": "Derived variant - Neolithic advantage"},
            "GA": {"lactase": "Likely Persistent", "historical": "Carrier of Neolithic mutation"},
            "GG": {"lactase": "Non-Persistent", "historical": "Ancestral - pre-Neolithic state"}
        },
        "population_frequency": {"EUR": 0.75, "AFR": 0.15, "EAS": 0.01}
    },
    # SLC22A4 - Ergothioneine transporter (selected in farmers)
    "rs1050152": {
        "gene": "SLC22A4",
        "chromosome": "5",
        "variant_name": "L503F",
        "function": "Nutrient transport - possibly selected in agricultural populations",
        "effect": {
            "TT": {"farmer_marker": True, "note": "Variant common in farmer descendants"},
            "CT": {"farmer_marker": "Partial", "note": "Heterozygous"},
            "CC": {"farmer_marker": False, "note": "Hunter-gatherer-like"}
        },
        "population_frequency": {"EUR": 0.45, "AFR": 0.10, "EAS": 0.20}
    },
    # NAT2 - Xenobiotic metabolism (diet adaptation)
    "rs1041983": {
        "gene": "NAT2",
        "chromosome": "8",
        "variant_name": "Synonymous",
        "function": "Detoxification - dietary adaptation marker",
        "effect": {
            "CC": {"acetylator": "Fast", "historical": "Agricultural diet adapted"},
            "CT": {"acetylator": "Intermediate", "historical": "Mixed"},
            "TT": {"acetylator": "Slow", "historical": "Hunter-gatherer pattern"}
        },
        "population_frequency": {"EUR": 0.55, "AFR": 0.25, "EAS": 0.85}
    },
    # AMY1 copy number proxy - Salivary amylase (starch digestion)
    "rs4244372": {
        "gene": "AMY1",
        "chromosome": "1",
        "variant_name": "Intronic",
        "function": "Salivary amylase - starch digestion selected in farming populations",
        "effect": {
            "TT": {"amylase": "High", "historical": "Agricultural adaptation - high starch diet"},
            "AT": {"amylase": "Intermediate", "historical": "Mixed"},
            "AA": {"amylase": "Lower", "historical": "Hunter-gatherer pattern"}
        },
        "population_frequency": {"EUR": 0.60, "AFR": 0.45, "EAS": 0.70}
    },
    # FADS1 - Fatty acid metabolism (plant vs meat diet)
    "rs174547": {
        "gene": "FADS1",
        "chromosome": "11",
        "variant_name": "Intronic",
        "function": "Fatty acid synthesis - selected for plant-based diet in farmers",
        "effect": {
            "TT": {"fads_status": "Efficient PUFA synthesis", "historical": "Farmer adaptation (plant diet)"},
            "CT": {"fads_status": "Intermediate", "historical": "Mixed ancestry"},
            "CC": {"fads_status": "Less efficient", "historical": "Meat-based diet adaptation"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.90, "EAS": 0.55}
    },
    # SI - Sucrase-isomaltase (carbohydrate digestion)
    "rs9290264": {
        "gene": "SI",
        "chromosome": "3",
        "variant_name": "Intronic",
        "function": "Sucrose digestion - selected with agriculture",
        "effect": {
            "GG": {"si_function": "Normal", "historical": "Efficient sucrose digestion"},
            "AG": {"si_function": "Normal", "historical": "Heterozygous"},
            "AA": {"si_function": "Possibly reduced", "historical": "Pre-agricultural variant"}
        },
        "population_frequency": {"EUR": 0.70, "AFR": 0.55, "EAS": 0.65}
    },
    # HLA-DQB1 - Celiac disease risk (grain adaptation)
    "rs2187668": {
        "gene": "HLA-DQB1",
        "chromosome": "6",
        "variant_name": "DQ2.5",
        "function": "HLA immune gene - celiac risk (grain-related selection)",
        "effect": {
            "TT": {"celiac_risk": "Elevated", "historical": "Possible recent positive selection"},
            "CT": {"celiac_risk": "Moderate", "historical": "Carrier"},
            "CC": {"celiac_risk": "Lower", "historical": "Non-carrier"}
        },
        "population_frequency": {"EUR": 0.15, "AFR": 0.05, "EAS": 0.02}
    },
    # MGAM - Maltase-glucoamylase (starch)
    "rs4945087": {
        "gene": "MGAM",
        "chromosome": "7",
        "variant_name": "Intronic",
        "function": "Starch digestion enzyme - agricultural adaptation",
        "effect": {
            "AA": {"starch_digestion": "Efficient", "historical": "Farmer diet adaptation"},
            "GA": {"starch_digestion": "Intermediate", "historical": "Heterozygous"},
            "GG": {"starch_digestion": "Standard", "historical": "Pre-agricultural"}
        },
        "population_frequency": {"EUR": 0.55, "AFR": 0.40, "EAS": 0.60}
    },
    # TREH - Trehalase (mushroom digestion, agriculture proxy)
    "rs2276064": {
        "gene": "TREH",
        "chromosome": "11",
        "variant_name": "Intronic",
        "function": "Trehalose digestion - foraging to farming transition",
        "effect": {
            "CC": {"trehalase": "Normal", "historical": "Efficient trehalose metabolism"},
            "CT": {"trehalase": "Normal", "historical": "Heterozygous"},
            "TT": {"trehalase": "Reduced", "historical": "Deficiency risk"}
        },
        "population_frequency": {"EUR": 0.85, "AFR": 0.70, "EAS": 0.90}
    }
}

# =============================================================================
# HUNTER-GATHERER ANCESTRY (WHG/EHG)
# =============================================================================

HUNTER_GATHERER_MARKERS = {
    # HERC2/OCA2 - Blue eyes originated in hunter-gatherers
    "rs12913832": {
        "gene": "HERC2/OCA2",
        "chromosome": "15",
        "variant_name": "Intronic",
        "function": "Blue eye color - originated in Mesolithic hunter-gatherers",
        "whg_allele": "A",  # Blue eye allele found in WHG
        "effect": {
            "AA": {"eye_color": "Blue", "historical": "Western Hunter-Gatherer derived trait"},
            "GA": {"eye_color": "Green/Hazel", "historical": "Mixed ancestry"},
            "GG": {"eye_color": "Brown", "historical": "Ancestral/Farmer typical"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.01, "EAS": 0.01}
    },
    # SLC45A2 - Light skin (partially from WHG)
    "rs16891982": {
        "gene": "SLC45A2",
        "chromosome": "5",
        "variant_name": "L374F",
        "function": "Light skin pigmentation - European adaptation",
        "effect": {
            "GG": {"skin": "Light", "historical": "European derived - found in ancient Europeans"},
            "CG": {"skin": "Intermediate", "historical": "Mixed"},
            "CC": {"skin": "Darker", "historical": "Ancestral variant"}
        },
        "population_frequency": {"EUR": 0.95, "AFR": 0.02, "EAS": 0.05}
    },
    # SLC24A5 - Major skin lightening gene
    "rs1426654": {
        "gene": "SLC24A5",
        "chromosome": "15",
        "variant_name": "A111T",
        "function": "Major European skin lightening - spread with farmers",
        "farmer_derived": True,
        "effect": {
            "AA": {"skin": "Light", "historical": "Derived variant - spread ~8000 years ago"},
            "GA": {"skin": "Intermediate", "historical": "Mixed"},
            "GG": {"skin": "Darker", "historical": "Ancestral (African/Asian)"}
        },
        "population_frequency": {"EUR": 0.999, "AFR": 0.02, "EAS": 0.02}
    },
    # IRF4 - Hair/skin/eye color, WHG heritage
    "rs12203592": {
        "gene": "IRF4",
        "chromosome": "6",
        "variant_name": "Intronic",
        "function": "Pigmentation - light skin/freckling from hunter-gatherer ancestry",
        "whg_allele": "T",
        "effect": {
            "TT": {"pigmentation": "Light/Freckles", "historical": "WHG-associated trait"},
            "CT": {"pigmentation": "Intermediate", "historical": "Mixed"},
            "CC": {"pigmentation": "Standard", "historical": "Farmer-typical"}
        },
        "population_frequency": {"EUR": 0.20, "AFR": 0.01, "EAS": 0.01}
    },
    # OCA2 - Additional pigmentation, WHG
    "rs1800407": {
        "gene": "OCA2",
        "chromosome": "15",
        "variant_name": "R419Q",
        "function": "Eye color modifier - found in WHG",
        "whg_allele": "T",
        "effect": {
            "TT": {"eye_modifier": "Green/Blue enhancer", "historical": "Hunter-gatherer derived"},
            "CT": {"eye_modifier": "Mixed effect", "historical": "Heterozygous"},
            "CC": {"eye_modifier": "Brown tendency", "historical": "Ancestral"}
        },
        "population_frequency": {"EUR": 0.08, "AFR": 0.01, "EAS": 0.01}
    },
    # GRM5 - Neurotransmission, WHG marker
    "rs10762894": {
        "gene": "GRM5",
        "chromosome": "11",
        "variant_name": "Intronic",
        "function": "Glutamate receptor - WHG ancestry marker",
        "whg_allele": "G",
        "effect": {
            "GG": {"whg_marker": True, "historical": "Western Hunter-Gatherer ancestry signal"},
            "AG": {"whg_marker": "Partial", "historical": "Mixed ancestry"},
            "AA": {"whg_marker": False, "historical": "Farmer/other ancestry"}
        },
        "population_frequency": {"EUR": 0.55, "AFR": 0.25, "EAS": 0.30}
    },
    # HERC2 - Additional eye color SNP
    "rs1129038": {
        "gene": "HERC2",
        "chromosome": "15",
        "variant_name": "Intronic",
        "function": "Blue eye color - in LD with rs12913832, WHG derived",
        "whg_allele": "A",
        "effect": {
            "AA": {"eye_color": "Blue", "historical": "Hunter-gatherer derived"},
            "GA": {"eye_color": "Mixed", "historical": "Heterozygous"},
            "GG": {"eye_color": "Brown", "historical": "Ancestral"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.01, "EAS": 0.01}
    },
    # EXOC2 - WHG ancestry marker
    "rs6828137": {
        "gene": "EXOC2",
        "chromosome": "6",
        "variant_name": "Intronic",
        "function": "Exocyst complex - Western Hunter-Gatherer ancestry marker",
        "whg_allele": "A",
        "effect": {
            "AA": {"whg_marker": True, "historical": "WHG ancestry signal"},
            "GA": {"whg_marker": "Partial", "historical": "Mixed"},
            "GG": {"whg_marker": False, "historical": "Non-WHG"}
        },
        "population_frequency": {"EUR": 0.40, "AFR": 0.15, "EAS": 0.20}
    },
    # SH2B3 - Immune/blood cells, selected in WHG
    "rs3184504": {
        "gene": "SH2B3",
        "chromosome": "12",
        "variant_name": "R262W",
        "function": "Blood cell regulation - selected in hunter-gatherers",
        "whg_allele": "T",
        "effect": {
            "TT": {"sh2b3": "WHG variant", "historical": "Hunter-gatherer immune adaptation"},
            "CT": {"sh2b3": "Heterozygous", "historical": "Mixed"},
            "CC": {"sh2b3": "Common variant", "historical": "Ancestral"}
        },
        "population_frequency": {"EUR": 0.50, "AFR": 0.05, "EAS": 0.03}
    }
}

# =============================================================================
# STEPPE/YAMNAYA ANCESTRY MARKERS
# =============================================================================

STEPPE_MARKERS = {
    # KITLG - Hair/eye color, Yamnaya carried derived variants
    "rs12821256": {
        "gene": "KITLG",
        "chromosome": "12",
        "variant_name": "Intronic",
        "function": "Blonde hair - spread with Indo-European migrations",
        "steppe_allele": "C",
        "effect": {
            "CC": {"hair": "Blonde tendency", "historical": "Steppe/Yamnaya associated"},
            "CT": {"hair": "Light brown tendency", "historical": "Heterozygous"},
            "TT": {"hair": "Darker hair tendency", "historical": "Pre-Steppe European"}
        },
        "population_frequency": {"EUR": 0.20, "AFR": 0.02, "EAS": 0.02}
    },
    # R1a/R1b Y-chromosome markers (patrilineal only, represented by autosomal tags)
    # These are proxy SNPs that correlate with Steppe ancestry
    "rs2032652": {
        "gene": "SRY region proxy",
        "chromosome": "X",  # Actually autosomal proxy
        "variant_name": "Proxy",
        "function": "Correlates with Steppe patrilineal lineages",
        "steppe_allele": "C",
        "effect": {
            "presence": {"historical": "Correlated with Bronze Age Steppe expansions"}
        },
        "population_frequency": {"EUR": 0.45, "AFR": 0.05, "EAS": 0.10}
    },
    # HERC2 - Lighter eyes spread from Steppe
    "rs1667394": {
        "gene": "HERC2",
        "chromosome": "15",
        "variant_name": "Intronic",
        "function": "Eye color - Steppe expansion contributed to light eye spread",
        "steppe_allele": "A",
        "effect": {
            "AA": {"eyes": "Light", "historical": "Steppe-associated light eye variant"},
            "GA": {"eyes": "Intermediate", "historical": "Mixed ancestry"},
            "GG": {"eyes": "Darker", "historical": "Pre-Steppe"}
        },
        "population_frequency": {"EUR": 0.80, "AFR": 0.05, "EAS": 0.05}
    },
    # TYRP1 - Blonde hair selected in Steppe
    "rs1408799": {
        "gene": "TYRP1",
        "chromosome": "9",
        "variant_name": "Intronic",
        "function": "Hair color - light pigmentation spread with Steppe",
        "steppe_allele": "C",
        "effect": {
            "CC": {"hair": "Blonde/Light brown", "historical": "Steppe ancestry marker"},
            "CT": {"hair": "Mixed", "historical": "Heterozygous"},
            "TT": {"hair": "Dark", "historical": "Pre-Steppe"}
        },
        "population_frequency": {"EUR": 0.80, "AFR": 0.05, "EAS": 0.15}
    },
    # ASNSD1 - Height, Steppe populations were taller
    "rs11150606": {
        "gene": "ASNSD1",
        "chromosome": "2",
        "variant_name": "Intronic",
        "function": "Height - Steppe populations had tall-associated alleles",
        "steppe_allele": "A",
        "effect": {
            "AA": {"height": "Taller tendency", "historical": "Steppe height selection"},
            "GA": {"height": "Intermediate", "historical": "Mixed"},
            "GG": {"height": "Average", "historical": "Farmer-typical"}
        },
        "population_frequency": {"EUR": 0.55, "AFR": 0.30, "EAS": 0.35}
    },
    # ZBTB38 - Height associated, steppe selection
    "rs724016": {
        "gene": "ZBTB38",
        "chromosome": "3",
        "variant_name": "Intronic",
        "function": "Height regulation - strong Steppe selection signal",
        "steppe_allele": "G",
        "effect": {
            "GG": {"height": "Taller", "historical": "Selected in Steppe populations"},
            "AG": {"height": "Intermediate", "historical": "Mixed"},
            "AA": {"height": "Shorter tendency", "historical": "WHG-like"}
        },
        "population_frequency": {"EUR": 0.65, "AFR": 0.40, "EAS": 0.45}
    },
    # HMGA2 - Height, steppe
    "rs1042725": {
        "gene": "HMGA2",
        "chromosome": "12",
        "variant_name": "3'-UTR",
        "function": "Height - Steppe-associated tall allele",
        "steppe_allele": "C",
        "effect": {
            "CC": {"height": "Taller", "historical": "Steppe expansion spread tall variant"},
            "CT": {"height": "Intermediate", "historical": "Mixed"},
            "TT": {"height": "Shorter", "historical": "Pre-Steppe"}
        },
        "population_frequency": {"EUR": 0.50, "AFR": 0.30, "EAS": 0.25}
    },
    # GHR - Growth hormone receptor, steppe selection
    "rs6184": {
        "gene": "GHR",
        "chromosome": "5",
        "variant_name": "Exon 3 deletion proxy",
        "function": "Growth hormone response - Steppe height selection",
        "steppe_allele": "A",
        "effect": {
            "AA": {"ghr": "Full length", "historical": "Steppe-typical"},
            "GA": {"ghr": "Mixed", "historical": "Heterozygous"},
            "GG": {"ghr": "d3 variant", "historical": "Variable"}
        },
        "population_frequency": {"EUR": 0.75, "AFR": 0.65, "EAS": 0.55}
    },
    # COMT - Neurotransmitter metabolism, EHG/Steppe
    "rs4680": {
        "gene": "COMT",
        "chromosome": "22",
        "variant_name": "V158M",
        "function": "Dopamine metabolism - Steppe population differentiation",
        "steppe_allele": "G",
        "effect": {
            "GG": {"comt": "Val/Val (Warrior)", "historical": "Higher in Steppe descendants"},
            "AG": {"comt": "Val/Met", "historical": "Mixed"},
            "AA": {"comt": "Met/Met (Worrier)", "historical": "More common in farmers"}
        },
        "population_frequency": {"EUR": 0.50, "AFR": 0.70, "EAS": 0.75}
    },
    # ANK3 - Neural, Steppe ancestry marker
    "rs10994336": {
        "gene": "ANK3",
        "chromosome": "10",
        "variant_name": "Intronic",
        "function": "Ankyrin - neural function, Steppe ancestry signal",
        "steppe_allele": "T",
        "effect": {
            "TT": {"steppe_marker": True, "historical": "Steppe ancestry signal"},
            "CT": {"steppe_marker": "Partial", "historical": "Mixed"},
            "CC": {"steppe_marker": False, "historical": "Non-Steppe"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.15, "EAS": 0.20}
    }
}

# =============================================================================
# ANCIENT PATHOGEN RESISTANCE MARKERS
# =============================================================================

PATHOGEN_MARKERS = {
    # CCR5-delta32 - Plague resistance (possibly selected during Black Death)
    "rs333": {
        "gene": "CCR5",
        "chromosome": "3",
        "variant_name": "Delta32",
        "function": "CCR5-delta32 - possible plague/smallpox resistance",
        "historical_context": "May have been selected during plague pandemics",
        "effect": {
            "II": {"ccr5_delta32": "Absent", "hiv_resistance": "Normal susceptibility"},
            "ID": {"ccr5_delta32": "Carrier", "hiv_resistance": "Slower HIV progression"},
            "DD": {"ccr5_delta32": "Homozygous", "hiv_resistance": "HIV resistant", "historical": "Possible plague survivor ancestry"}
        },
        "population_frequency": {"EUR": 0.10, "AFR": 0.001, "EAS": 0.001}
    },
    # TYK2 - Tuberculosis resistance
    "rs34536443": {
        "gene": "TYK2",
        "chromosome": "19",
        "variant_name": "P1104A",
        "function": "TB resistance - P1104A protective variant",
        "protective_allele": "C",
        "effect": {
            "CC": {"tb_resistance": "Enhanced Protection", "tb_risk": "Lower Risk", "historical": "Selected during TB epidemics"},
            "GC": {"tb_resistance": "Partial Protection", "tb_risk": "Slightly Lower Risk", "historical": "Carrier"},
            "GG": {"tb_resistance": "Average (no extra protection)", "tb_risk": "Average Risk", "historical": "Ancestral - most common"}
        },
        "population_frequency": {"EUR": 0.04, "AFR": 0.01, "EAS": 0.01}
    },
    # FUT2 (non-secretor) - Protection from Norovirus and other pathogens
    "rs601338": {
        "gene": "FUT2",
        "chromosome": "19",
        "variant_name": "W154X",
        "function": "Non-secretor status - pathogen resistance",
        "historical_context": "Non-secretors resistant to many GI pathogens",
        "effect": {
            "AA": {"secretor": "Non-Secretor", "pathogen_resistance": "Norovirus resistant", "historical": "Selected during epidemics"},
            "GA": {"secretor": "Secretor (carrier)", "pathogen_resistance": "Normal"},
            "GG": {"secretor": "Secretor", "pathogen_resistance": "Normal susceptibility"}
        },
        "population_frequency": {"EUR": 0.20, "AFR": 0.15, "EAS": 0.05}
    },
    # HBB - Sickle cell (malaria resistance)
    "rs334": {
        "gene": "HBB",
        "chromosome": "11",
        "variant_name": "E6V",
        "function": "Sickle cell trait - malaria resistance",
        "historical_context": "Strongly selected in malaria-endemic regions",
        "effect": {
            "TT": {"sickle_cell": "Normal", "malaria_resistance": "Normal susceptibility"},
            "AT": {"sickle_cell": "Carrier (trait)", "malaria_resistance": "Resistant to severe malaria"},
            "TA": {"sickle_cell": "Carrier (trait)", "malaria_resistance": "Resistant to severe malaria"},
            "AA": {"sickle_cell": "Disease", "malaria_resistance": "Resistant but severe disease"}
        },
        "population_frequency": {"EUR": 0.001, "AFR": 0.15, "EAS": 0.001}
    },
    # G6PD - Malaria resistance (favism)
    "rs1050828": {
        "gene": "G6PD",
        "chromosome": "X",
        "variant_name": "V68M",
        "function": "G6PD deficiency - malaria protection (African variant A-)",
        "historical_context": "Strong malaria selection, causes favism",
        "effect": {
            "TT": {"g6pd": "A- Deficiency (males)", "malaria": "Resistant", "historical": "Malaria-endemic selection"},
            "CT": {"g6pd": "Carrier (females)", "malaria": "Partial protection", "historical": "Heterozygote advantage"},
            "CC": {"g6pd": "Normal", "malaria": "Susceptible", "historical": "Ancestral"}
        },
        "population_frequency": {"EUR": 0.001, "AFR": 0.20, "EAS": 0.05}
    },
    # HBB HbC variant - Malaria resistance
    "rs33930165": {
        "gene": "HBB",
        "chromosome": "11",
        "variant_name": "E6K (HbC)",
        "function": "Hemoglobin C - malaria resistance",
        "historical_context": "West African malaria adaptation",
        "effect": {
            "AA": {"hbc": "HbC disease", "malaria": "Resistant but anemia"},
            "GA": {"hbc": "HbC trait", "malaria": "Strong malaria resistance", "historical": "West African selection"},
            "GG": {"hbc": "Normal HbA", "malaria": "Normal", "historical": "Ancestral"}
        },
        "population_frequency": {"EUR": 0.001, "AFR": 0.15, "EAS": 0.001}
    },
    # DARC/Duffy - Vivax malaria resistance
    "rs2814778": {
        "gene": "DARC",
        "chromosome": "1",
        "variant_name": "GATA-1 binding",
        "function": "Duffy negative - P. vivax malaria resistance",
        "historical_context": "Near-complete fixation in Sub-Saharan Africa",
        "effect": {
            "CC": {"duffy": "Duffy negative", "vivax_malaria": "Resistant", "historical": "African malaria adaptation"},
            "TC": {"duffy": "Weak expression", "vivax_malaria": "Partially resistant", "historical": "Mixed"},
            "TT": {"duffy": "Duffy positive", "vivax_malaria": "Susceptible", "historical": "Ancestral"}
        },
        "population_frequency": {"EUR": 0.001, "AFR": 0.95, "EAS": 0.001}
    },
    # IFITM3 - Influenza resistance
    "rs12252": {
        "gene": "IFITM3",
        "chromosome": "11",
        "variant_name": "Splice",
        "function": "Influenza severity - selected during flu pandemics",
        "historical_context": "May have been selected during 1918 flu",
        "effect": {
            "CC": {"influenza": "Severe susceptibility", "historical": "Risk allele - possibly selected against"},
            "TC": {"influenza": "Intermediate", "historical": "Carrier"},
            "TT": {"influenza": "Normal response", "historical": "Protective"}
        },
        "population_frequency": {"EUR": 0.04, "AFR": 0.08, "EAS": 0.45}
    },
    # IL10 - Sepsis/pathogen response
    "rs1800896": {
        "gene": "IL10",
        "chromosome": "1",
        "variant_name": "-1082G>A",
        "function": "Anti-inflammatory cytokine - pathogen response",
        "historical_context": "Balanced selection from pathogen exposure",
        "effect": {
            "GG": {"il10": "High producer", "historical": "May reduce immunopathology"},
            "AG": {"il10": "Intermediate", "historical": "Balanced"},
            "AA": {"il10": "Low producer", "historical": "Stronger inflammation"}
        },
        "population_frequency": {"EUR": 0.50, "AFR": 0.35, "EAS": 0.30}
    },
    # CASP12 - Sepsis resistance
    "rs497116": {
        "gene": "CASP12",
        "chromosome": "11",
        "variant_name": "Truncation",
        "function": "Caspase-12 - sepsis resistance (most humans lack functional)",
        "historical_context": "Inactive version selected due to sepsis protection",
        "effect": {
            "GG": {"casp12": "Inactive (protective)", "sepsis": "Resistant", "historical": "Selected for sepsis resistance"},
            "AG": {"casp12": "One active copy", "sepsis": "Intermediate", "historical": "Carrier"},
            "AA": {"casp12": "Active (rare)", "sepsis": "Susceptible", "historical": "Ancestral - rare in modern humans"}
        },
        "population_frequency": {"EUR": 0.98, "AFR": 0.75, "EAS": 0.99}
    },
    # TIRAP - Bacterial infection protection
    "rs8177374": {
        "gene": "TIRAP",
        "chromosome": "11",
        "variant_name": "S180L",
        "function": "TLR signaling - protection from severe bacterial infection",
        "historical_context": "Heterozygote advantage against invasive bacteria",
        "effect": {
            "TT": {"tirap": "S180L homozygous", "infection": "Possible immune defects", "historical": "Selected against"},
            "CT": {"tirap": "Heterozygote", "infection": "Protected", "historical": "Balanced selection - plague/TB"},
            "CC": {"tirap": "Wild type", "infection": "Normal", "historical": "Ancestral"}
        },
        "population_frequency": {"EUR": 0.20, "AFR": 0.15, "EAS": 0.05}
    },
    # HLA-B*27 - Ankylosing spondylitis but infection resistance
    "rs4349859": {
        "gene": "HLA-B",
        "chromosome": "6",
        "variant_name": "B*27 tag",
        "function": "HLA-B*27 - infection resistance vs autoimmunity trade-off",
        "historical_context": "Maintained by pathogen-driven selection despite autoimmune cost",
        "effect": {
            "AA": {"hla_b27": "Likely B*27+", "infection": "Enhanced clearance", "historical": "Pathogen selection"},
            "GA": {"hla_b27": "Possible carrier", "infection": "Intermediate", "historical": "Mixed"},
            "GG": {"hla_b27": "B*27-", "infection": "Normal", "historical": "Common"}
        },
        "population_frequency": {"EUR": 0.08, "AFR": 0.02, "EAS": 0.05}
    }
}

# =============================================================================
# LIGHT SKIN ADAPTATION GENES
# =============================================================================

SKIN_ADAPTATION_MARKERS = {
    # SLC24A5 - Major skin lightening (already in hunter-gatherer section)
    # MC1R - Red hair and pale skin
    "rs1805007": {
        "gene": "MC1R",
        "chromosome": "16",
        "variant_name": "R151C",
        "function": "Red hair / pale skin R151C variant",
        "effect": {
            "TT": {"mc1r_status": "Red hair variant homozygous", "historical": "Northern European adaptation"},
            "CT": {"mc1r_status": "Carrier", "historical": "May have red/auburn tones"},
            "CC": {"mc1r_status": "Wild type", "historical": "Normal melanin signaling"}
        },
        "population_frequency": {"EUR": 0.10, "AFR": 0.001, "EAS": 0.001}
    },
    "rs1805008": {
        "gene": "MC1R",
        "chromosome": "16",
        "variant_name": "R160W",
        "function": "Red hair R160W variant",
        "effect": {
            "TT": {"mc1r_status": "Red hair variant homozygous"},
            "CT": {"mc1r_status": "Carrier"},
            "CC": {"mc1r_status": "Wild type"}
        },
        "population_frequency": {"EUR": 0.08, "AFR": 0.001, "EAS": 0.001}
    },
    # TYRP1 - Melanin synthesis
    "rs1408799": {
        "gene": "TYRP1",
        "chromosome": "9",
        "variant_name": "Intronic",
        "function": "Melanin synthesis - European light pigmentation",
        "effect": {
            "CC": {"pigmentation": "Light adapted", "historical": "European derived"},
            "CT": {"pigmentation": "Intermediate", "historical": "Mixed"},
            "TT": {"pigmentation": "Darker", "historical": "Ancestral"}
        },
        "population_frequency": {"EUR": 0.80, "AFR": 0.05, "EAS": 0.15}
    },
    # MC1R - D294H variant (red hair)
    "rs1805009": {
        "gene": "MC1R",
        "chromosome": "16",
        "variant_name": "D294H",
        "function": "Red hair D294H - strong red hair variant",
        "effect": {
            "AA": {"mc1r_status": "Strong red hair variant", "historical": "Northern European"},
            "GA": {"mc1r_status": "Carrier", "historical": "May have red tones"},
            "GG": {"mc1r_status": "Wild type", "historical": "Normal"}
        },
        "population_frequency": {"EUR": 0.02, "AFR": 0.001, "EAS": 0.001}
    },
    # MC1R - V60L (mild lightening)
    "rs1805005": {
        "gene": "MC1R",
        "chromosome": "16",
        "variant_name": "V60L",
        "function": "Mild skin lightening variant",
        "effect": {
            "TT": {"mc1r_status": "V60L homozygous", "historical": "European selected"},
            "GT": {"mc1r_status": "Carrier", "historical": "Mixed"},
            "GG": {"mc1r_status": "Wild type", "historical": "Ancestral"}
        },
        "population_frequency": {"EUR": 0.12, "AFR": 0.01, "EAS": 0.02}
    },
    # TYR - Major tyrosinase
    "rs1042602": {
        "gene": "TYR",
        "chromosome": "11",
        "variant_name": "S192Y",
        "function": "Tyrosinase - lighter pigmentation in Europeans",
        "effect": {
            "AA": {"tyr": "Light pigmentation", "historical": "European adaptation"},
            "CA": {"tyr": "Intermediate", "historical": "Mixed"},
            "CC": {"tyr": "Darker pigmentation", "historical": "Ancestral"}
        },
        "population_frequency": {"EUR": 0.40, "AFR": 0.02, "EAS": 0.03}
    },
    # OCA2 - Blue/brown eye
    "rs1800414": {
        "gene": "OCA2",
        "chromosome": "15",
        "variant_name": "H615R",
        "function": "East Asian light skin variant",
        "effect": {
            "AA": {"oca2": "Light skin (Asian)", "historical": "East Asian specific adaptation"},
            "GA": {"oca2": "Intermediate", "historical": "Mixed"},
            "GG": {"oca2": "Standard", "historical": "Common"}
        },
        "population_frequency": {"EUR": 0.02, "AFR": 0.01, "EAS": 0.65}
    },
    # ASIP - Agouti signaling
    "rs6058017": {
        "gene": "ASIP",
        "chromosome": "20",
        "variant_name": "8818 A>G",
        "function": "Agouti - affects pigmentation pathway",
        "effect": {
            "GG": {"asip": "Darker tendency", "historical": "Ancestral"},
            "AG": {"asip": "Intermediate", "historical": "Mixed"},
            "AA": {"asip": "Lighter tendency", "historical": "Selected in light-adapted populations"}
        },
        "population_frequency": {"EUR": 0.85, "AFR": 0.20, "EAS": 0.75}
    },
    # BNC2 - Freckling and fair skin
    "rs2153271": {
        "gene": "BNC2",
        "chromosome": "9",
        "variant_name": "Intronic",
        "function": "Skin saturation and freckling",
        "effect": {
            "TT": {"bnc2": "Fair/freckled", "historical": "Northern European"},
            "CT": {"bnc2": "Intermediate", "historical": "Mixed"},
            "CC": {"bnc2": "Standard", "historical": "Common"}
        },
        "population_frequency": {"EUR": 0.55, "AFR": 0.10, "EAS": 0.40}
    },
    # SLC24A4 - Hair/eye color
    "rs12896399": {
        "gene": "SLC24A4",
        "chromosome": "14",
        "variant_name": "Intronic",
        "function": "Hair and eye color - European light phenotypes",
        "effect": {
            "TT": {"slc24a4": "Light hair/eyes", "historical": "European adaptation"},
            "GT": {"slc24a4": "Intermediate", "historical": "Mixed"},
            "GG": {"slc24a4": "Darker features", "historical": "Ancestral"}
        },
        "population_frequency": {"EUR": 0.55, "AFR": 0.05, "EAS": 0.10}
    }
}

# =============================================================================
# HISTORICAL MIGRATION MARKERS
# =============================================================================

MIGRATION_MARKERS = {
    # Ancestry Informative Markers (AIMs)
    "rs3827760": {
        "gene": "EDAR",
        "chromosome": "2",
        "variant_name": "V370A",
        "function": "East Asian hair thickness, tooth shape - cold adaptation",
        "migration_context": "Spread with East Asian populations, strong positive selection",
        "effect": {
            "AA": {"edar_variant": "Derived (Asian)", "traits": "Thick hair, shovel-shaped incisors", "historical": "Cold adaptation, spread ~30,000 years ago"},
            "GA": {"edar_variant": "Heterozygous", "traits": "Intermediate"},
            "GG": {"edar_variant": "Ancestral", "traits": "Thinner hair, different tooth morphology"}
        },
        "population_frequency": {"EUR": 0.02, "AFR": 0.01, "EAS": 0.90, "NAT": 0.95}
    },
    # ABCC11 - Earwax type (migration tracking)
    "rs17822931": {
        "gene": "ABCC11",
        "chromosome": "16",
        "variant_name": "G180R",
        "function": "Earwax type - East Asian migration marker",
        "migration_context": "Dry earwax variant spread with East Asian migrations",
        "effect": {
            "TT": {"earwax": "Dry", "body_odor": "Reduced", "historical": "East Asian/Native American derived"},
            "CT": {"earwax": "Wet (likely)", "body_odor": "Normal", "historical": "Heterozygous"},
            "CC": {"earwax": "Wet", "body_odor": "Normal", "historical": "Ancestral (African/European)"}
        },
        "population_frequency": {"EUR": 0.10, "AFR": 0.02, "EAS": 0.85, "NAT": 0.95}
    },
    # ADH1B - Alcohol metabolism (East Asian positive selection)
    "rs1229984": {
        "gene": "ADH1B",
        "chromosome": "4",
        "variant_name": "H48R",
        "function": "Fast alcohol metabolism - East Asian selected",
        "migration_context": "Strong selection in rice-cultivating populations",
        "effect": {
            "TT": {"adh1b": "Very Fast", "historical": "Strong positive selection in East Asia ~10,000 years"},
            "CT": {"adh1b": "Fast", "historical": "Heterozygous"},
            "CC": {"adh1b": "Normal", "historical": "Ancestral variant"}
        },
        "population_frequency": {"EUR": 0.05, "AFR": 0.02, "EAS": 0.70}
    },
    # ALDH2 - Acetaldehyde metabolism (Asian flush)
    "rs671": {
        "gene": "ALDH2",
        "chromosome": "12",
        "variant_name": "E504K",
        "function": "Aldehyde dehydrogenase - East Asian specific",
        "migration_context": "Nearly exclusive to East Asian populations",
        "effect": {
            "AA": {"aldh2": "Inactive (flush)", "historical": "East Asian specific - strong selection signal"},
            "GA": {"aldh2": "Reduced (partial flush)", "historical": "Heterozygous"},
            "GG": {"aldh2": "Normal", "historical": "Ancestral - worldwide"}
        },
        "population_frequency": {"EUR": 0.001, "AFR": 0.001, "EAS": 0.40}
    },
    # SLC24A5 - Skin lightening spread with migrations
    "rs1426654": {
        "gene": "SLC24A5",
        "chromosome": "15",
        "variant_name": "A111T",
        "function": "Major skin lightening - tracked migration routes",
        "migration_context": "Spread from Near East with Neolithic expansion",
        "effect": {
            "AA": {"skin": "Light", "historical": "Neolithic expansion marker"},
            "GA": {"skin": "Intermediate", "historical": "Admixture zone"},
            "GG": {"skin": "Darker", "historical": "Ancestral - Sub-Saharan Africa/East Asia"}
        },
        "population_frequency": {"EUR": 0.999, "AFR": 0.02, "EAS": 0.02, "SAS": 0.90}
    },
    # MCPH1 - Brain size, human-specific selection
    "rs930557": {
        "gene": "MCPH1",
        "chromosome": "8",
        "variant_name": "Intronic",
        "function": "Brain development - positive selection signal",
        "migration_context": "Shows selection signatures in Out-of-Africa migration",
        "effect": {
            "CC": {"mcph1": "Derived allele", "historical": "Positively selected after migration"},
            "CT": {"mcph1": "Heterozygous", "historical": "Mixed"},
            "TT": {"mcph1": "Ancestral", "historical": "More common in Africa"}
        },
        "population_frequency": {"EUR": 0.70, "AFR": 0.30, "EAS": 0.75}
    },
    # ASPM - Brain size, regional selection
    "rs41310927": {
        "gene": "ASPM",
        "chromosome": "1",
        "variant_name": "Intronic",
        "function": "Brain development - shows population differentiation",
        "migration_context": "Frequency differences trace migration patterns",
        "effect": {
            "AA": {"aspm": "Derived", "historical": "Shows selection in Eurasians"},
            "GA": {"aspm": "Heterozygous", "historical": "Mixed"},
            "GG": {"aspm": "Ancestral", "historical": "Higher in Africa"}
        },
        "population_frequency": {"EUR": 0.50, "AFR": 0.10, "EAS": 0.45}
    },
    # EPAS1 - Tibetan altitude (Denisovan migration marker)
    "rs1868092": {
        "gene": "EPAS1",
        "chromosome": "2",
        "variant_name": "Intronic",
        "function": "High altitude - tracks ancient Denisovan admixture",
        "migration_context": "Denisovan DNA from ancient admixture ~50,000 years ago",
        "effect": {
            "GG": {"epas1": "Denisovan-derived", "historical": "Ancient admixture marker"},
            "AG": {"epas1": "One Denisovan copy", "historical": "Partial adaptation"},
            "AA": {"epas1": "Modern human", "historical": "Most common outside Tibet"}
        },
        "population_frequency": {"EUR": 0.01, "AFR": 0.001, "EAS": 0.05, "TIB": 0.85}
    },
    # OPRM1 - Pain/reward, population differences
    "rs1799971": {
        "gene": "OPRM1",
        "chromosome": "6",
        "variant_name": "A118G",
        "function": "Opioid receptor - shows migration-related frequency differences",
        "migration_context": "Strong frequency differentiation between populations",
        "effect": {
            "GG": {"oprm1": "G/G (reduced receptor)", "historical": "Higher in East Asians"},
            "AG": {"oprm1": "Heterozygous", "historical": "Intermediate"},
            "AA": {"oprm1": "A/A (typical)", "historical": "Most common worldwide"}
        },
        "population_frequency": {"EUR": 0.15, "AFR": 0.05, "EAS": 0.40}
    },
    # F5 - Factor V Leiden (European-specific)
    "rs6025": {
        "gene": "F5",
        "chromosome": "1",
        "variant_name": "R506Q",
        "function": "Factor V Leiden - tracks European migrations",
        "migration_context": "Nearly exclusive to European-ancestry populations",
        "effect": {
            "AA": {"f5": "Leiden homozygous", "historical": "European origin"},
            "GA": {"f5": "Leiden carrier", "historical": "European ancestry marker"},
            "GG": {"f5": "Normal", "historical": "Ancestral - worldwide"}
        },
        "population_frequency": {"EUR": 0.05, "AFR": 0.001, "EAS": 0.001}
    },
    # APOE - Lipid metabolism, shows regional selection
    "rs429358": {
        "gene": "APOE",
        "chromosome": "19",
        "variant_name": "C112R (E4)",
        "function": "APOE4 - shows population frequency differences from migration",
        "migration_context": "Higher E4 frequency in populations with foraging ancestry",
        "effect": {
            "CC": {"apoe": "E4 allele", "historical": "Hunter-gatherer associated"},
            "CT": {"apoe": "E4 carrier", "historical": "One copy"},
            "TT": {"apoe": "E3/E2", "historical": "Farmer/agricultural associated"}
        },
        "population_frequency": {"EUR": 0.15, "AFR": 0.25, "EAS": 0.10}
    },
    # TRPM8 - Cold sensing (climate adaptation)
    "rs10166942": {
        "gene": "TRPM8",
        "chromosome": "2",
        "variant_name": "5'-upstream",
        "function": "Cold sensor - climate-driven selection",
        "migration_context": "Frequency correlates with latitude/cold climate",
        "effect": {
            "TT": {"trpm8": "Cold-adapted", "historical": "Selected in northern migrations"},
            "CT": {"trpm8": "Intermediate", "historical": "Mixed"},
            "CC": {"trpm8": "Tropical-adapted", "historical": "Ancestral (equatorial)"}
        },
        "population_frequency": {"EUR": 0.80, "AFR": 0.35, "EAS": 0.65}
    },
    # LPL - Lipid metabolism (diet/climate adaptation)
    "rs328": {
        "gene": "LPL",
        "chromosome": "8",
        "variant_name": "S447X",
        "function": "Lipoprotein lipase - diet-related selection",
        "migration_context": "Frequency differences reflect dietary adaptation",
        "effect": {
            "GG": {"lpl": "447X (beneficial)", "historical": "Selected in some populations"},
            "CG": {"lpl": "Heterozygous", "historical": "Mixed"},
            "CC": {"lpl": "S447 (common)", "historical": "Ancestral"}
        },
        "population_frequency": {"EUR": 0.10, "AFR": 0.05, "EAS": 0.15}
    }
}


# =============================================================================
# MAIN ANALYSIS FUNCTION
# =============================================================================

def analyze_ancient_dna_history(dna_data: dict) -> Dict[str, Any]:
    """
    Perform comprehensive ancient DNA and historical genetics analysis.

    Args:
        dna_data: Dictionary of rsid -> genotype

    Returns:
        Dictionary containing all ancient DNA analysis results
    """
    results = {
        "neanderthal_ancestry": analyze_neanderthal(dna_data),
        "denisovan_ancestry": analyze_denisovan(dna_data),
        "ancient_farmer": analyze_ancient_farmer(dna_data),
        "hunter_gatherer": analyze_hunter_gatherer(dna_data),
        "steppe_ancestry": analyze_steppe(dna_data),
        "pathogen_resistance": analyze_pathogen_history(dna_data),
        "pigmentation_history": analyze_pigmentation_history(dna_data),
        "migration_markers": analyze_migration(dna_data),
        "summary": {}
    }

    # Generate overall summary
    results["summary"] = generate_ancient_summary(results)

    return results


def analyze_neanderthal(dna_data: dict) -> Dict[str, Any]:
    """Analyze Neanderthal ancestry markers using expanded database for accuracy"""
    result = {
        "snps_analyzed": [],
        "neanderthal_score": 0,
        "max_possible_score": 0,
        "percentage_estimate": 0,
        "neanderthal_traits": [],
        "findings": [],
        "markers_found": 0,
        "total_markers": 0
    }

    # Use expanded marker set if available for consistent percentages
    if USE_EXPANDED_ARCHAIC:
        markers_found = 0
        total_markers = 0

        for category, markers in ARCHAIC_FUNCTIONAL_GENES.get('neanderthal', {}).items():
            for rsid, marker_data in markers.items():
                total_markers += 1

                if rsid not in dna_data:
                    continue

                genotype = dna_data[rsid].upper()
                neanderthal_allele = marker_data.get('neanderthal_allele', '')

                if neanderthal_allele in genotype:
                    markers_found += 1
                    copies = genotype.count(neanderthal_allele)

                    result["snps_analyzed"].append({
                        "rsid": rsid,
                        "gene": marker_data.get("gene", ""),
                        "genotype": genotype,
                        "neanderthal_allele": neanderthal_allele
                    })

                    trait = marker_data.get("function", "").split(" - ")[0] if marker_data.get("function") else marker_data.get("effect", "")
                    if trait:
                        result["neanderthal_traits"].append(trait)

                    if copies == 2:
                        result["findings"].append(f"{marker_data.get('gene', rsid)}: Homozygous Neanderthal variant")

        result["markers_found"] = markers_found
        result["total_markers"] = total_markers
        # Also set score fields for UI compatibility
        result["neanderthal_score"] = markers_found
        result["max_possible_score"] = total_markers

        # Calculate both marker match rate and estimated actual ancestry
        if total_markers > 0:
            marker_pct = (markers_found / total_markers) * 100
            result["marker_match_rate"] = round(marker_pct, 1)

            # Estimated actual ancestry (scientific range: 1-4% for non-Africans)
            if marker_pct >= 40:
                result["percentage_estimate"] = 2.5  # Above average
            elif marker_pct >= 25:
                result["percentage_estimate"] = 2.0  # Average
            else:
                result["percentage_estimate"] = 1.5  # Below average
    else:
        # Fallback to original small marker set
        total_score = 0
        max_score = 0

        for rsid, info in NEANDERTHAL_MARKERS.items():
            if rsid in dna_data:
                genotype = dna_data[rsid]
                effects = info.get("effect", {})
                max_score += 2

                result["snps_analyzed"].append({
                    "rsid": rsid,
                    "gene": info.get("gene", ""),
                    "genotype": genotype,
                    "neanderthal_allele": info.get("neanderthal_allele", "")
                })

                _key = get_genotype_key(genotype, effects)
                if _key:
                    effect = effects[_key]
                    score = effect.get("neanderthal_score", 0)
                    total_score += score

                    if score >= 1:
                        trait = info.get("function", "").split(" - ")[0]
                        result["neanderthal_traits"].append(trait)
                        if score == 2:
                            result["findings"].append(f"{info.get('gene', rsid)}: Homozygous Neanderthal variant")

        result["neanderthal_score"] = total_score
        result["max_possible_score"] = max_score

        # RAW DATA
        if max_score > 0:
            marker_pct = (total_score / max_score) * 100
            result["percentage_estimate"] = round(marker_pct, 1)

    return result


def analyze_denisovan(dna_data: dict) -> Dict[str, Any]:
    """Analyze Denisovan ancestry markers using expanded database for accuracy"""
    result = {
        "snps_analyzed": [],
        "denisovan_score": 0,
        "max_possible_score": 0,
        "percentage_estimate": 0,
        "denisovan_traits": [],
        "findings": [],
        "markers_found": 0,
        "total_markers": 0
    }

    # Use expanded marker set if available for consistent percentages
    if USE_EXPANDED_ARCHAIC:
        markers_found = 0
        total_markers = 0

        for category, markers in ARCHAIC_FUNCTIONAL_GENES.get('denisovan', {}).items():
            for rsid, marker_data in markers.items():
                total_markers += 1

                if rsid not in dna_data:
                    continue

                genotype = dna_data[rsid].upper()
                denisovan_allele = marker_data.get('denisovan_allele', '')

                if denisovan_allele in genotype:
                    markers_found += 1
                    copies = genotype.count(denisovan_allele)

                    result["snps_analyzed"].append({
                        "rsid": rsid,
                        "gene": marker_data.get("gene", ""),
                        "genotype": genotype,
                        "denisovan_allele": denisovan_allele
                    })

                    trait = marker_data.get("function", "").split(" - ")[0] if marker_data.get("function") else marker_data.get("effect", "")
                    if trait:
                        result["denisovan_traits"].append(trait)

                    # Special case for EPAS1 altitude adaptation
                    if "EPAS1" in marker_data.get("gene", ""):
                        result["findings"].append("Carry Denisovan-derived high altitude adaptation gene (EPAS1)")

        result["markers_found"] = markers_found
        result["total_markers"] = total_markers
        # Also set score fields for UI compatibility
        result["denisovan_score"] = markers_found
        result["max_possible_score"] = total_markers

        # Calculate both marker match rate and estimated actual ancestry
        if total_markers > 0:
            marker_pct = (markers_found / total_markers) * 100
            result["marker_match_rate"] = round(marker_pct, 1)

            # Estimated actual ancestry (most non-Oceanians: 0-1%, Oceanians: 3-6%)
            if marker_pct >= 50:
                result["percentage_estimate"] = 1.0  # Above average for non-Oceanians
            elif marker_pct >= 30:
                result["percentage_estimate"] = 0.5  # Some Denisovan
            else:
                result["percentage_estimate"] = 0.2  # Trace
    else:
        # Fallback to original small marker set
        total_score = 0
        max_score = 0

        for rsid, info in DENISOVAN_MARKERS.items():
            if rsid in dna_data:
                genotype = dna_data[rsid]
                effects = info.get("effect", {})
                max_score += 2

                result["snps_analyzed"].append({
                    "rsid": rsid,
                    "gene": info.get("gene", ""),
                    "genotype": genotype,
                    "denisovan_allele": info.get("denisovan_allele", "")
                })

                _key = get_genotype_key(genotype, effects)
                if _key:
                    effect = effects[_key]
                    score = effect.get("denisovan_score", 0)
                    total_score += score

                    if score >= 1:
                        if "EPAS1" in info.get("gene", ""):
                            result["denisovan_traits"].append("High altitude adaptation (EPAS1)")
                            result["findings"].append("Carry Denisovan-derived high altitude adaptation gene")

        result["denisovan_score"] = total_score
        result["max_possible_score"] = max_score

        # RAW DATA
        if max_score > 0:
            marker_pct = (total_score / max_score) * 100
            result["percentage_estimate"] = round(marker_pct, 1)

    return result


def analyze_ancient_farmer(dna_data: dict) -> Dict[str, Any]:
    """Analyze ancient European farmer ancestry"""
    result = {
        "snps_analyzed": [],
        "farmer_markers_found": 0,
        "lactase_persistent": "Unknown",
        "neolithic_traits": [],
        "findings": []
    }

    for rsid, info in ANCIENT_FARMER_MARKERS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            effects = info.get("effect", {})

            result["snps_analyzed"].append({
                "rsid": rsid,
                "gene": info.get("gene", ""),
                "genotype": genotype
            })

            _key = get_genotype_key(genotype, effects)
            if _key:

                effect = effects[_key]

                # Lactase persistence
                if "lactase" in effect:
                    result["lactase_persistent"] = effect["lactase"]
                    if effect["lactase"] == "Persistent":
                        result["farmer_markers_found"] += 1
                        result["neolithic_traits"].append("Lactase Persistence")
                        result["findings"].append("Lactase persistence - spread with Neolithic farmers ~7,500 years ago")

                if effect.get("farmer_marker") == True:
                    result["farmer_markers_found"] += 1

    return result


def analyze_hunter_gatherer(dna_data: dict) -> Dict[str, Any]:
    """Analyze hunter-gatherer ancestry markers"""
    result = {
        "snps_analyzed": [],
        "whg_traits": [],
        "blue_eye_origin": "Unknown",
        "light_skin_genes": [],
        "findings": []
    }

    for rsid, info in HUNTER_GATHERER_MARKERS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            effects = info.get("effect", {})

            result["snps_analyzed"].append({
                "rsid": rsid,
                "gene": info.get("gene", ""),
                "genotype": genotype
            })

            _key = get_genotype_key(genotype, effects)
            if _key:

                effect = effects[_key]

                # Blue eyes
                if "eye_color" in effect:
                    result["blue_eye_origin"] = effect["eye_color"]
                    if effect["eye_color"] == "Blue":
                        result["whg_traits"].append("Blue Eyes")
                        result["findings"].append("Blue eye allele - originated in Mesolithic hunter-gatherers ~10,000 years ago")

                # Light skin
                if "skin" in effect:
                    if effect["skin"] == "Light":
                        result["light_skin_genes"].append(info.get("gene", rsid))
                        if info.get("farmer_derived"):
                            result["findings"].append(f"{info.get('gene')}: Light skin variant spread with Neolithic farmers")

    return result


def analyze_steppe(dna_data: dict) -> Dict[str, Any]:
    """Analyze Steppe/Yamnaya ancestry markers"""
    result = {
        "snps_analyzed": [],
        "steppe_markers_found": 0,
        "steppe_traits": [],
        "findings": []
    }

    for rsid, info in STEPPE_MARKERS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            effects = info.get("effect", {})

            result["snps_analyzed"].append({
                "rsid": rsid,
                "gene": info.get("gene", ""),
                "genotype": genotype,
                "steppe_allele": info.get("steppe_allele", "")
            })

            _key = get_genotype_key(genotype, effects)
            if _key:

                effect = effects[_key]

                if "hair" in effect:
                    if "Blonde" in effect["hair"]:
                        result["steppe_markers_found"] += 1
                        result["steppe_traits"].append("Blonde hair tendency")
                        result["findings"].append("Blonde hair variant - spread with Bronze Age Steppe migrations ~5,000 years ago")

    return result


def analyze_pathogen_history(dna_data: dict) -> Dict[str, Any]:
    """Analyze ancient pathogen resistance markers"""
    result = {
        "snps_analyzed": [],
        "protective_variants": [],
        "historical_selection": [],
        "findings": []
    }

    for rsid, info in PATHOGEN_MARKERS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            effects = info.get("effect", {})

            result["snps_analyzed"].append({
                "rsid": rsid,
                "gene": info.get("gene", ""),
                "genotype": genotype
            })

            _key = get_genotype_key(genotype, effects)
            if _key:

                effect = effects[_key]

                # CCR5-delta32
                if "ccr5_delta32" in effect:
                    if effect["ccr5_delta32"] in ["Carrier", "Homozygous"]:
                        result["protective_variants"].append("CCR5-delta32 (plague/HIV)")
                        result["historical_selection"].append("Possibly selected during plague pandemics")
                        result["findings"].append("CCR5-delta32 - may indicate plague survivor ancestry")

                # TB resistance
                if "tb_resistance" in effect:
                    if "Protection" in effect["tb_resistance"]:
                        result["protective_variants"].append("TYK2 (TB resistance)")
                        result["findings"].append("TB-protective variant - you have enhanced defense against tuberculosis")

                # Malaria resistance
                if "sickle_cell" in effect:
                    if effect["sickle_cell"] == "Carrier (trait)":
                        result["protective_variants"].append("Sickle cell trait (malaria)")
                        result["historical_selection"].append("Strong selection in malaria-endemic regions")
                        result["findings"].append("Sickle cell trait - provides malaria resistance")

    return result


def analyze_pigmentation_history(dna_data: dict) -> Dict[str, Any]:
    """Analyze historical pigmentation adaptation"""
    result = {
        "snps_analyzed": [],
        "red_hair_variants": 0,
        "light_skin_adaptation": "Unknown",
        "findings": []
    }

    for rsid, info in SKIN_ADAPTATION_MARKERS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            effects = info.get("effect", {})

            result["snps_analyzed"].append({
                "rsid": rsid,
                "gene": info.get("gene", ""),
                "genotype": genotype
            })

            _key = get_genotype_key(genotype, effects)
            if _key:

                effect = effects[_key]

                # MC1R red hair
                if "mc1r_status" in effect:
                    if "Red hair" in effect["mc1r_status"]:
                        result["red_hair_variants"] += 1
                        if result["red_hair_variants"] >= 2:
                            result["findings"].append("Multiple MC1R variants - Northern European red hair adaptation")

                # Pigmentation adaptation
                if "pigmentation" in effect:
                    if effect["pigmentation"] == "Light adapted":
                        result["light_skin_adaptation"] = "Adapted"

    return result


def analyze_migration(dna_data: dict) -> Dict[str, Any]:
    """Analyze historical migration markers"""
    result = {
        "snps_analyzed": [],
        "east_asian_markers": [],
        "migration_patterns": [],
        "findings": []
    }

    for rsid, info in MIGRATION_MARKERS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            effects = info.get("effect", {})

            result["snps_analyzed"].append({
                "rsid": rsid,
                "gene": info.get("gene", ""),
                "genotype": genotype
            })

            _key = get_genotype_key(genotype, effects)
            if _key:

                effect = effects[_key]

                # EDAR - East Asian marker
                if info.get("gene") == "EDAR":
                    if "Derived (Asian)" in effect.get("edar_variant", ""):
                        result["east_asian_markers"].append("EDAR (hair/teeth)")
                        result["migration_patterns"].append("East Asian ancestry marker")
                        result["findings"].append("EDAR derived variant - cold adaptation spread ~30,000 years ago")

                # Earwax - migration tracking
                if info.get("gene") == "ABCC11":
                    if effect.get("earwax") == "Dry":
                        result["east_asian_markers"].append("ABCC11 (dry earwax)")
                        result["migration_patterns"].append("East Asian/Native American lineage")

    return result


def generate_ancient_summary(results: Dict[str, Any]) -> Dict[str, Any]:
    """Generate overall ancient DNA summary"""
    summary = {
        "archaic_ancestry": [],
        "historical_ancestry_markers": [],
        "selected_traits": [],
        "key_findings": [],
        "historical_context": []
    }

    # Neanderthal
    neanderthal = results.get("neanderthal_ancestry", {})
    if neanderthal.get("neanderthal_score", 0) > 0:
        summary["archaic_ancestry"].append(f"Neanderthal: {neanderthal.get('percentage_estimate', 'Present')}")
        summary["selected_traits"].extend(neanderthal.get("neanderthal_traits", []))

    # Denisovan
    denisovan = results.get("denisovan_ancestry", {})
    if denisovan.get("denisovan_score", 0) > 0:
        denis_pct = denisovan.get('percentage_estimate', 0)
        summary["archaic_ancestry"].append(f"Denisovan: {denis_pct}%")
        summary["selected_traits"].extend(denisovan.get("denisovan_traits", []))

    # Farmer ancestry
    farmer = results.get("ancient_farmer", {})
    if farmer.get("lactase_persistent") == "Persistent":
        summary["historical_ancestry_markers"].append("Neolithic Farmer traits (lactase)")

    # Hunter-gatherer
    whg = results.get("hunter_gatherer", {})
    if whg.get("blue_eye_origin") == "Blue":
        summary["historical_ancestry_markers"].append("Mesolithic Hunter-Gatherer (blue eyes)")

    # Steppe
    steppe = results.get("steppe_ancestry", {})
    if steppe.get("steppe_markers_found", 0) > 0:
        summary["historical_ancestry_markers"].append("Bronze Age Steppe ancestry")

    # Pathogen resistance
    pathogen = results.get("pathogen_resistance", {})
    if pathogen.get("protective_variants"):
        summary["selected_traits"].append(f"Pathogen resistance: {', '.join(pathogen['protective_variants'])}")

    # Compile key findings
    for key in results:
        if key != "summary" and isinstance(results[key], dict):
            findings = results[key].get("findings", [])
            summary["key_findings"].extend(findings)

    # Historical context
    summary["historical_context"] = [
        "Your DNA contains markers from multiple ancient population movements",
        "Archaic ancestry (Neanderthal/Denisovan) provides insights into human evolution",
        "Many traits were selected over thousands of years in response to diet, disease, and climate"
    ]

    return summary
