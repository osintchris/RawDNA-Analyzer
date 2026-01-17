#!/usr/bin/env python3
"""
Physical Traits Expanded Database
Comprehensive database for additional physical trait genetics

Features:
1. Height prediction (polygenic)
2. Hair texture (curly, wavy, straight)
3. Hair loss / Male pattern baldness
4. Freckles
5. Dimples
6. Widow's peak
7. Cleft chin
8. Attached vs detached earlobes
9. Tongue rolling ability
10. Finger length ratio (2D:4D)

Data sources:
- GWAS Catalog
- dbSNP (NCBI)
- Published genetics research
- 23andMe research papers
"""

from typing import Dict, Any, List


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
# HEIGHT GENETICS (Polygenic)
# =============================================================================

HEIGHT_GENETICS = {
    'name': 'Height',
    'description': 'Genetic factors contributing to adult height',
    'heritability': 0.80,  # 80% heritable
    'markers': {
        # HMGA2 - major height gene
        'rs1042725': {
            'gene': 'HMGA2',
            'name': 'HMGA2 height variant',
            'chromosome': '12',
            'position': 66221077,
            'effect_size_cm': 0.4,  # Per allele effect
            'genotypes': {
                'CC': {'effect': 'shorter', 'cm_adjustment': -0.4, 'percentile_shift': -5},
                'CT': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'TT': {'effect': 'taller', 'cm_adjustment': 0.4, 'percentile_shift': 5}
            },
            'population_frequency': {'C': 0.50, 'T': 0.50},
            'pmid': '17767157'
        },
        # GDF5 - growth differentiation factor
        'rs143384': {
            'gene': 'GDF5',
            'name': 'GDF5 height variant',
            'chromosome': '20',
            'position': 34025756,
            'effect_size_cm': 0.3,
            'genotypes': {
                'AA': {'effect': 'shorter', 'cm_adjustment': -0.3, 'percentile_shift': -3},
                'AG': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'GG': {'effect': 'taller', 'cm_adjustment': 0.3, 'percentile_shift': 3}
            },
            'population_frequency': {'A': 0.42, 'G': 0.58},
            'pmid': '18758464'
        },
        # ZBTB38 - zinc finger protein
        'rs724016': {
            'gene': 'ZBTB38',
            'name': 'ZBTB38 height variant',
            'chromosome': '3',
            'position': 141142891,
            'effect_size_cm': 0.35,
            'genotypes': {
                'AA': {'effect': 'shorter', 'cm_adjustment': -0.35, 'percentile_shift': -4},
                'AG': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'GG': {'effect': 'taller', 'cm_adjustment': 0.35, 'percentile_shift': 4}
            },
            'population_frequency': {'A': 0.55, 'G': 0.45},
            'pmid': '18758464'
        },
        # LCORL - ligand dependent nuclear receptor corepressor-like
        'rs6449353': {
            'gene': 'LCORL',
            'name': 'LCORL height variant',
            'chromosome': '4',
            'position': 17916292,
            'effect_size_cm': 0.45,
            'genotypes': {
                'CC': {'effect': 'shorter', 'cm_adjustment': -0.45, 'percentile_shift': -5},
                'CG': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'GG': {'effect': 'taller', 'cm_adjustment': 0.45, 'percentile_shift': 5}
            },
            'population_frequency': {'C': 0.60, 'G': 0.40},
            'pmid': '19343178'
        },
        # HHIP - hedgehog interacting protein
        'rs6903956': {
            'gene': 'HHIP',
            'name': 'HHIP height variant',
            'chromosome': '4',
            'position': 145504839,
            'effect_size_cm': 0.25,
            'genotypes': {
                'AA': {'effect': 'shorter', 'cm_adjustment': -0.25, 'percentile_shift': -3},
                'AG': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'GG': {'effect': 'taller', 'cm_adjustment': 0.25, 'percentile_shift': 3}
            },
            'population_frequency': {'A': 0.65, 'G': 0.35},
            'pmid': '18391950'
        },
        # GHR - growth hormone receptor
        'rs6180': {
            'gene': 'GHR',
            'name': 'GHR exon 3 variant',
            'variant_name': 'd3-GHR',
            'chromosome': '5',
            'position': 42701618,
            'effect_size_cm': 0.5,
            'genotypes': {
                'CC': {'effect': 'shorter', 'cm_adjustment': -0.5, 'percentile_shift': -5},
                'CA': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'AA': {'effect': 'taller', 'cm_adjustment': 0.5, 'percentile_shift': 5}
            },
            'population_frequency': {'C': 0.55, 'A': 0.45},
            'pmid': '19396169'
        },
        # NPPC - C-type natriuretic peptide
        'rs6892909': {
            'gene': 'NPPC',
            'name': 'NPPC height variant',
            'variant_name': 'Intronic',
            'chromosome': '2',
            'position': 232544547,
            'effect_size_cm': 0.3,
            'genotypes': {
                'TT': {'effect': 'shorter', 'cm_adjustment': -0.3, 'percentile_shift': -3},
                'TC': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'CC': {'effect': 'taller', 'cm_adjustment': 0.3, 'percentile_shift': 3}
            },
            'population_frequency': {'T': 0.55, 'C': 0.45},
            'pmid': '20881960'
        },
        # FGFR3 - Fibroblast growth factor receptor
        'rs7683707': {
            'gene': 'FGFR3',
            'name': 'FGFR3 height variant',
            'variant_name': 'Intronic',
            'chromosome': '4',
            'position': 1802350,
            'effect_size_cm': 0.35,
            'genotypes': {
                'GG': {'effect': 'shorter', 'cm_adjustment': -0.35, 'percentile_shift': -4},
                'GA': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'AA': {'effect': 'taller', 'cm_adjustment': 0.35, 'percentile_shift': 4}
            },
            'population_frequency': {'G': 0.60, 'A': 0.40},
            'pmid': '18391951'
        },
        # CPLANE1 - Height-associated
        'rs17081935': {
            'gene': 'CPLANE1',
            'name': 'CPLANE1 height variant',
            'variant_name': 'Intronic',
            'chromosome': '5',
            'position': 93442159,
            'effect_size_cm': 0.25,
            'genotypes': {
                'AA': {'effect': 'shorter', 'cm_adjustment': -0.25, 'percentile_shift': -3},
                'AG': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'GG': {'effect': 'taller', 'cm_adjustment': 0.25, 'percentile_shift': 3}
            },
            'population_frequency': {'A': 0.70, 'G': 0.30},
            'pmid': '20881960'
        },
        # DOT1L - Histone methyltransferase
        'rs12986413': {
            'gene': 'DOT1L',
            'name': 'DOT1L height variant',
            'variant_name': 'Intronic',
            'chromosome': '19',
            'position': 2136629,
            'effect_size_cm': 0.3,
            'genotypes': {
                'CC': {'effect': 'shorter', 'cm_adjustment': -0.3, 'percentile_shift': -3},
                'CT': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'TT': {'effect': 'taller', 'cm_adjustment': 0.3, 'percentile_shift': 3}
            },
            'population_frequency': {'C': 0.65, 'T': 0.35},
            'pmid': '20881960'
        },
        # ANAPC13 - Anaphase promoting complex
        'rs6440003': {
            'gene': 'ANAPC13',
            'name': 'ANAPC13 height variant',
            'variant_name': 'Intronic',
            'chromosome': '3',
            'position': 135762065,
            'effect_size_cm': 0.25,
            'genotypes': {
                'TT': {'effect': 'shorter', 'cm_adjustment': -0.25, 'percentile_shift': -3},
                'TC': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'CC': {'effect': 'taller', 'cm_adjustment': 0.25, 'percentile_shift': 3}
            },
            'population_frequency': {'T': 0.55, 'C': 0.45},
            'pmid': '20881960'
        },
        # SCMH1 - Sex comb on midleg homolog
        'rs6060373': {
            'gene': 'SCMH1',
            'name': 'SCMH1 height variant',
            'variant_name': 'Intronic',
            'chromosome': '1',
            'position': 41512330,
            'effect_size_cm': 0.2,
            'genotypes': {
                'CC': {'effect': 'shorter', 'cm_adjustment': -0.2, 'percentile_shift': -2},
                'CT': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'TT': {'effect': 'taller', 'cm_adjustment': 0.2, 'percentile_shift': 2}
            },
            'population_frequency': {'C': 0.60, 'T': 0.40},
            'pmid': '20881960'
        },
        # ESR1 - Estrogen receptor
        'rs3020418': {
            'gene': 'ESR1',
            'name': 'ESR1 height variant',
            'variant_name': 'Intronic',
            'chromosome': '6',
            'position': 152129126,
            'effect_size_cm': 0.25,
            'genotypes': {
                'AA': {'effect': 'shorter', 'cm_adjustment': -0.25, 'percentile_shift': -3},
                'AG': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'GG': {'effect': 'taller', 'cm_adjustment': 0.25, 'percentile_shift': 3}
            },
            'population_frequency': {'A': 0.55, 'G': 0.45},
            'pmid': '18391952'
        },
        # IGF1 - Insulin-like growth factor 1
        'rs35767': {
            'gene': 'IGF1',
            'name': 'IGF1 height variant',
            'variant_name': 'Promoter',
            'chromosome': '12',
            'position': 102874804,
            'effect_size_cm': 0.35,
            'genotypes': {
                'GG': {'effect': 'shorter', 'cm_adjustment': -0.35, 'percentile_shift': -4},
                'GA': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'AA': {'effect': 'taller', 'cm_adjustment': 0.35, 'percentile_shift': 4}
            },
            'population_frequency': {'G': 0.60, 'A': 0.40},
            'pmid': '18391952'
        },
        # ACAN - Aggrecan (cartilage)
        'rs16942341': {
            'gene': 'ACAN',
            'name': 'ACAN height variant',
            'variant_name': 'Intronic',
            'chromosome': '15',
            'position': 89347632,
            'effect_size_cm': 0.3,
            'genotypes': {
                'TT': {'effect': 'shorter', 'cm_adjustment': -0.3, 'percentile_shift': -3},
                'TC': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'CC': {'effect': 'taller', 'cm_adjustment': 0.3, 'percentile_shift': 3}
            },
            'population_frequency': {'T': 0.65, 'C': 0.35},
            'pmid': '22484627'
        },
        # IHH - Indian hedgehog
        'rs6503650': {
            'gene': 'IHH',
            'name': 'IHH height variant',
            'variant_name': 'Intronic',
            'chromosome': '2',
            'position': 219913844,
            'effect_size_cm': 0.25,
            'genotypes': {
                'CC': {'effect': 'shorter', 'cm_adjustment': -0.25, 'percentile_shift': -3},
                'CT': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'TT': {'effect': 'taller', 'cm_adjustment': 0.25, 'percentile_shift': 3}
            },
            'population_frequency': {'C': 0.55, 'T': 0.45},
            'pmid': '20881960'
        },
        # CDK6 - Cell division kinase
        'rs798544': {
            'gene': 'CDK6',
            'name': 'CDK6 height variant',
            'variant_name': 'Intronic',
            'chromosome': '7',
            'position': 92469485,
            'effect_size_cm': 0.2,
            'genotypes': {
                'AA': {'effect': 'shorter', 'cm_adjustment': -0.2, 'percentile_shift': -2},
                'AG': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'GG': {'effect': 'taller', 'cm_adjustment': 0.2, 'percentile_shift': 2}
            },
            'population_frequency': {'A': 0.60, 'G': 0.40},
            'pmid': '20881960'
        },
        # STC2 - Stanniocalcin 2
        'rs10472828': {
            'gene': 'STC2',
            'name': 'STC2 height variant',
            'variant_name': 'Intronic',
            'chromosome': '5',
            'position': 172756612,
            'effect_size_cm': 0.3,
            'genotypes': {
                'TT': {'effect': 'shorter', 'cm_adjustment': -0.3, 'percentile_shift': -3},
                'TC': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'CC': {'effect': 'taller', 'cm_adjustment': 0.3, 'percentile_shift': 3}
            },
            'population_frequency': {'T': 0.55, 'C': 0.45},
            'pmid': '22484627'
        },
        # BMP2 - Bone morphogenetic protein
        'rs235767': {
            'gene': 'BMP2',
            'name': 'BMP2 height variant',
            'variant_name': 'Intronic',
            'chromosome': '20',
            'position': 6745489,
            'effect_size_cm': 0.25,
            'genotypes': {
                'GG': {'effect': 'shorter', 'cm_adjustment': -0.25, 'percentile_shift': -3},
                'GA': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'AA': {'effect': 'taller', 'cm_adjustment': 0.25, 'percentile_shift': 3}
            },
            'population_frequency': {'G': 0.58, 'A': 0.42},
            'pmid': '20881960'
        },
        # PTH1R - Parathyroid hormone receptor
        'rs724577': {
            'gene': 'PTH1R',
            'name': 'PTH1R height variant',
            'variant_name': 'Intronic',
            'chromosome': '3',
            'position': 47000285,
            'effect_size_cm': 0.2,
            'genotypes': {
                'CC': {'effect': 'shorter', 'cm_adjustment': -0.2, 'percentile_shift': -2},
                'CT': {'effect': 'average', 'cm_adjustment': 0, 'percentile_shift': 0},
                'TT': {'effect': 'taller', 'cm_adjustment': 0.2, 'percentile_shift': 2}
            },
            'population_frequency': {'C': 0.60, 'T': 0.40},
            'pmid': '22484627'
        }
    }
}

# =============================================================================
# EYE COLOR GENETICS
# =============================================================================

EYE_COLOR_GENETICS = {
    'name': 'Eye Color',
    'description': 'Genetic factors determining eye color',
    'markers': {
        # HERC2 - main blue/brown determinant
        'rs12913832': {
            'gene': 'HERC2',
            'name': 'Main eye color determinant',
            'variant_name': 'Intronic enhancer',
            'chromosome': '15',
            'position': 28365618,
            'genotypes': {
                'GG': {'color': 'Brown eyes likely', 'score': 0.95, 'description': 'Strong brown eye genetics'},
                'AG': {'color': 'Brown or hazel likely', 'score': 0.7, 'description': 'Likely brown/hazel, possibly green'},
                'AA': {'color': 'Blue/green eyes likely', 'score': 0.15, 'description': 'Light eye color likely'}
            },
            'population_frequency': {'G': 0.75, 'A': 0.25},
            'pmid': '18172690'
        },
        # OCA2 - Multiple variants
        'rs1800407': {
            'gene': 'OCA2',
            'name': 'OCA2 R419Q',
            'variant_name': 'R419Q',
            'chromosome': '15',
            'position': 28230318,
            'genotypes': {
                'GG': {'color': 'Brown tendency', 'score': 0.8, 'description': 'Typical OCA2'},
                'GA': {'color': 'Green/hazel possible', 'score': 0.5, 'description': 'May lighten eye color'},
                'AA': {'color': 'Green eyes more likely', 'score': 0.3, 'description': 'Associated with green eyes'}
            },
            'population_frequency': {'G': 0.90, 'A': 0.10},
            'pmid': '19270706'
        },
        'rs12896399': {
            'gene': 'OCA2/HERC2',
            'name': 'OCA2 eye color variant',
            'variant_name': 'Intronic',
            'chromosome': '15',
            'position': 28513364,
            'genotypes': {
                'GG': {'color': 'Brown tendency', 'score': 0.7, 'description': 'Darker pigment'},
                'GT': {'color': 'Intermediate', 'score': 0.5, 'description': 'Variable'},
                'TT': {'color': 'Lighter eye tendency', 'score': 0.3, 'description': 'Lighter pigment'}
            },
            'population_frequency': {'G': 0.60, 'T': 0.40},
            'pmid': '18172690'
        },
        # SLC24A4
        'rs12896399': {
            'gene': 'SLC24A4',
            'name': 'SLC24A4 eye color',
            'variant_name': 'Intronic',
            'chromosome': '14',
            'position': 92773663,
            'genotypes': {
                'GG': {'color': 'Darker tendency', 'score': 0.7, 'description': 'More pigment'},
                'GT': {'color': 'Intermediate', 'score': 0.5, 'description': 'Variable'},
                'TT': {'color': 'Lighter tendency', 'score': 0.3, 'description': 'Less pigment'}
            },
            'population_frequency': {'G': 0.55, 'T': 0.45},
            'pmid': '19270706'
        },
        # TYR - tyrosinase
        'rs1393350': {
            'gene': 'TYR',
            'name': 'Tyrosinase eye color',
            'variant_name': 'S192Y',
            'chromosome': '11',
            'position': 89011046,
            'genotypes': {
                'GG': {'color': 'Normal pigment', 'score': 0.6, 'description': 'Typical tyrosinase'},
                'GA': {'color': 'Slightly lighter', 'score': 0.4, 'description': 'Reduced function'},
                'AA': {'color': 'Lighter eyes possible', 'score': 0.25, 'description': 'Further reduced pigment'}
            },
            'population_frequency': {'G': 0.80, 'A': 0.20},
            'pmid': '19300498'
        },
        # IRF4
        'rs12203592': {
            'gene': 'IRF4',
            'name': 'IRF4 pigmentation',
            'variant_name': 'Intronic',
            'chromosome': '6',
            'position': 396321,
            'genotypes': {
                'CC': {'color': 'Darker eyes', 'score': 0.7, 'description': 'More pigmentation'},
                'CT': {'color': 'Intermediate', 'score': 0.5, 'description': 'Variable'},
                'TT': {'color': 'Lighter eyes', 'score': 0.25, 'description': 'Lighter pigmentation, often blue/green'}
            },
            'population_frequency': {'C': 0.85, 'T': 0.15},
            'pmid': '18488026'
        },
        # TYRP1 - Tyrosinase-related protein 1
        'rs1408799': {
            'gene': 'TYRP1',
            'name': 'TYRP1 eye color',
            'variant_name': 'Intronic',
            'chromosome': '9',
            'position': 12703371,
            'genotypes': {
                'CC': {'color': 'Brown eyes', 'score': 0.75, 'description': 'Brown pigmentation'},
                'CT': {'color': 'Hazel possible', 'score': 0.5, 'description': 'Intermediate'},
                'TT': {'color': 'Blue/green more likely', 'score': 0.3, 'description': 'Light eye color'}
            },
            'population_frequency': {'C': 0.70, 'T': 0.30},
            'pmid': '19270706'
        },
        # SLC24A5 - eye color influence
        'rs1426654': {
            'gene': 'SLC24A5',
            'name': 'SLC24A5 eye pigmentation',
            'variant_name': 'A111T',
            'chromosome': '15',
            'position': 48426484,
            'genotypes': {
                'AA': {'color': 'Darker eyes', 'score': 0.8, 'description': 'Strong melanin production'},
                'AG': {'color': 'Variable', 'score': 0.5, 'description': 'Mixed effect'},
                'GG': {'color': 'Lighter possible', 'score': 0.25, 'description': 'Reduced melanin'}
            },
            'population_frequency': {'A': 0.05, 'G': 0.95},
            'pmid': '16357253'
        },
        # LYST - Lysosomal trafficking regulator
        'rs3768056': {
            'gene': 'LYST',
            'name': 'LYST eye color',
            'variant_name': 'Intronic',
            'chromosome': '1',
            'position': 235889135,
            'genotypes': {
                'GG': {'color': 'Brown tendency', 'score': 0.65, 'description': 'More pigment'},
                'GA': {'color': 'Intermediate', 'score': 0.5, 'description': 'Variable'},
                'AA': {'color': 'Lighter tendency', 'score': 0.35, 'description': 'Less pigment'}
            },
            'population_frequency': {'G': 0.60, 'A': 0.40},
            'pmid': '19270706'
        },
        # KITLG - eye color effect
        'rs12821256': {
            'gene': 'KITLG',
            'name': 'KITLG eye color',
            'variant_name': 'Intergenic',
            'chromosome': '12',
            'position': 89328335,
            'genotypes': {
                'TT': {'color': 'Darker eyes', 'score': 0.65, 'description': 'More pigment'},
                'TC': {'color': 'Intermediate', 'score': 0.5, 'description': 'Variable'},
                'CC': {'color': 'Lighter eyes', 'score': 0.3, 'description': 'Less pigment'}
            },
            'population_frequency': {'T': 0.85, 'C': 0.15},
            'pmid': '17999355'
        },
        # DCT - Dopachrome tautomerase
        'rs1407995': {
            'gene': 'DCT',
            'name': 'DCT eye pigmentation',
            'variant_name': 'Intronic',
            'chromosome': '13',
            'position': 94888418,
            'genotypes': {
                'TT': {'color': 'Brown tendency', 'score': 0.6, 'description': 'More eumelanin'},
                'TC': {'color': 'Intermediate', 'score': 0.5, 'description': 'Variable'},
                'CC': {'color': 'Lighter tendency', 'score': 0.4, 'description': 'Less eumelanin'}
            },
            'population_frequency': {'T': 0.55, 'C': 0.45},
            'pmid': '19270706'
        },
        # TPCN2 - Two pore channel 2
        'rs35264875': {
            'gene': 'TPCN2',
            'name': 'TPCN2 eye color',
            'variant_name': 'M484L',
            'chromosome': '11',
            'position': 68655360,
            'genotypes': {
                'AA': {'color': 'Brown eyes', 'score': 0.7, 'description': 'Strong pigment'},
                'AT': {'color': 'Variable', 'score': 0.5, 'description': 'Intermediate'},
                'TT': {'color': 'Lighter eyes', 'score': 0.3, 'description': 'Blue/green possible'}
            },
            'population_frequency': {'A': 0.65, 'T': 0.35},
            'pmid': '18488029'
        }
    }
}

# =============================================================================
# SKIN PIGMENTATION GENETICS
# =============================================================================

SKIN_PIGMENTATION_GENETICS = {
    'name': 'Skin Pigmentation',
    'description': 'Genetic factors determining skin pigmentation',
    'markers': {
        # SLC24A5 - Major European depigmentation
        'rs1426654': {
            'gene': 'SLC24A5',
            'name': 'SLC24A5 A111T',
            'variant_name': 'A111T',
            'chromosome': '15',
            'position': 48426484,
            'genotypes': {
                'AA': {'pigment': 'Darker skin (ancestral)', 'score': 0.9, 'description': 'Original human pigmentation'},
                'AG': {'pigment': 'Intermediate', 'score': 0.5, 'description': 'Mixed ancestry'},
                'GG': {'pigment': 'Lighter skin (European)', 'score': 0.1, 'description': 'European depigmentation variant'}
            },
            'population_frequency': {'A': 0.02, 'G': 0.98},  # In Europeans
            'pmid': '16357253'
        },
        # SLC45A2 - MATP
        'rs16891982': {
            'gene': 'SLC45A2',
            'name': 'SLC45A2 L374F',
            'variant_name': 'L374F',
            'chromosome': '5',
            'position': 33951693,
            'genotypes': {
                'CC': {'pigment': 'Darker skin', 'score': 0.85, 'description': 'More melanin'},
                'CG': {'pigment': 'Intermediate', 'score': 0.5, 'description': 'Variable'},
                'GG': {'pigment': 'Lighter skin', 'score': 0.15, 'description': 'European light skin variant'}
            },
            'population_frequency': {'C': 0.05, 'G': 0.95},  # In Europeans
            'pmid': '17999355'
        },
        # MC1R - Multiple variants (also freckles)
        'rs1805007': {
            'gene': 'MC1R',
            'name': 'MC1R R151C',
            'variant_name': 'R151C',
            'chromosome': '16',
            'position': 89919709,
            'genotypes': {
                'CC': {'pigment': 'Normal pigmentation', 'score': 0.6, 'description': 'Typical MC1R'},
                'CT': {'pigment': 'Fair skin tendency', 'score': 0.4, 'description': 'May be fair-skinned/redhead carrier'},
                'TT': {'pigment': 'Very fair skin', 'score': 0.1, 'description': 'Red hair/very fair skin'}
            },
            'population_frequency': {'C': 0.92, 'T': 0.08},
            'pmid': '11197177'
        },
        # KITLG - Skin/hair pigmentation
        'rs12821256': {
            'gene': 'KITLG',
            'name': 'KITLG pigmentation',
            'variant_name': 'Intergenic',
            'chromosome': '12',
            'position': 89328335,
            'genotypes': {
                'TT': {'pigment': 'Darker', 'score': 0.7, 'description': 'More pigmentation'},
                'TC': {'pigment': 'Intermediate', 'score': 0.5, 'description': 'Variable'},
                'CC': {'pigment': 'Lighter', 'score': 0.3, 'description': 'Less pigmentation'}
            },
            'population_frequency': {'T': 0.85, 'C': 0.15},
            'pmid': '17999355'
        },
        # ASIP - Agouti signaling protein
        'rs2424984': {
            'gene': 'ASIP',
            'name': 'ASIP pigmentation',
            'variant_name': 'Upstream',
            'chromosome': '20',
            'position': 32741506,
            'genotypes': {
                'GG': {'pigment': 'Darker tendency', 'score': 0.7, 'description': 'More eumelanin'},
                'GA': {'pigment': 'Intermediate', 'score': 0.5, 'description': 'Variable'},
                'AA': {'pigment': 'Lighter tendency', 'score': 0.3, 'description': 'Less eumelanin'}
            },
            'population_frequency': {'G': 0.55, 'A': 0.45},
            'pmid': '18488028'
        }
    }
}

# =============================================================================
# UNIBROW (MONOBROW) GENETICS
# =============================================================================

UNIBROW_GENETICS = {
    'name': 'Unibrow (Synophrys)',
    'description': 'Genetic tendency for connected eyebrows',
    'markers': {
        # PAX3 - main unibrow gene
        'rs7559271': {
            'gene': 'PAX3',
            'name': 'PAX3 unibrow variant',
            'variant_name': 'Intronic',
            'chromosome': '2',
            'position': 223065200,
            'genotypes': {
                'CC': {'phenotype': 'Unibrow less likely', 'score': 0.2, 'description': 'Eyebrows likely separated'},
                'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'description': 'May have some mid-brow hair'},
                'TT': {'phenotype': 'Unibrow more likely', 'score': 0.8, 'description': 'Eyebrows may connect'}
            },
            'population_frequency': {'C': 0.65, 'T': 0.35},
            'pmid': '26770679'
        }
    }
}

# =============================================================================
# HAIR COLOR GENETICS
# =============================================================================

HAIR_COLOR_GENETICS = {
    'name': 'Hair Color',
    'description': 'Genetic factors determining hair color',
    'markers': {
        # MC1R - red hair
        'rs1805007': {
            'gene': 'MC1R',
            'name': 'MC1R R151C (red hair)',
            'variant_name': 'R151C',
            'chromosome': '16',
            'position': 89919709,
            'genotypes': {
                'CC': {'color': 'Not red', 'score': 0.0, 'description': 'No red hair variant'},
                'CT': {'color': 'Carrier', 'score': 0.3, 'description': 'Red hair carrier - may have reddish tones'},
                'TT': {'color': 'Red hair likely', 'score': 0.9, 'description': 'High likelihood of red hair'}
            },
            'population_frequency': {'C': 0.92, 'T': 0.08},
            'pmid': '11197177'
        },
        'rs1805008': {
            'gene': 'MC1R',
            'name': 'MC1R R160W (red hair)',
            'variant_name': 'R160W',
            'chromosome': '16',
            'position': 89919736,
            'genotypes': {
                'CC': {'color': 'Not red', 'score': 0.0, 'description': 'No red hair variant'},
                'CT': {'color': 'Carrier', 'score': 0.3, 'description': 'Red hair carrier'},
                'TT': {'color': 'Red hair likely', 'score': 0.85, 'description': 'Strong red hair tendency'}
            },
            'population_frequency': {'C': 0.91, 'T': 0.09},
            'pmid': '11197177'
        },
        # KITLG - blonde hair
        'rs12821256': {
            'gene': 'KITLG',
            'name': 'KITLG blonde hair',
            'variant_name': 'Intergenic',
            'chromosome': '12',
            'position': 89328335,
            'genotypes': {
                'TT': {'color': 'Darker hair', 'blonde_score': 0.2, 'description': 'Not associated with blonde'},
                'TC': {'color': 'Variable', 'blonde_score': 0.5, 'description': 'Intermediate'},
                'CC': {'color': 'Blonde tendency', 'blonde_score': 0.8, 'description': 'Associated with blonde hair'}
            },
            'population_frequency': {'T': 0.85, 'C': 0.15},
            'pmid': '24927176'
        },
        # SLC45A2 - hair lightness
        'rs16891982': {
            'gene': 'SLC45A2',
            'name': 'SLC45A2 hair color',
            'variant_name': 'L374F',
            'chromosome': '5',
            'position': 33951693,
            'genotypes': {
                'CC': {'color': 'Dark hair', 'blonde_score': 0.1, 'description': 'More melanin'},
                'CG': {'color': 'Variable', 'blonde_score': 0.4, 'description': 'Intermediate'},
                'GG': {'color': 'Light hair tendency', 'blonde_score': 0.7, 'description': 'Blonde/light brown possible'}
            },
            'population_frequency': {'C': 0.05, 'G': 0.95},  # In Europeans
            'pmid': '17999355'
        },
        # TYRP1 - brown hair
        'rs683': {
            'gene': 'TYRP1',
            'name': 'TYRP1 hair color',
            'variant_name': 'Synonymous',
            'chromosome': '9',
            'position': 12696099,
            'genotypes': {
                'CC': {'color': 'Brown hair tendency', 'score': 0.6, 'description': 'Associated with brown hair'},
                'CA': {'color': 'Variable brown', 'score': 0.5, 'description': 'Intermediate'},
                'AA': {'color': 'Lighter brown/blonde', 'score': 0.35, 'description': 'May have lighter hair'}
            },
            'population_frequency': {'C': 0.55, 'A': 0.45},
            'pmid': '17999355'
        },
        # MC1R - D294H
        'rs1805009': {
            'gene': 'MC1R',
            'name': 'MC1R D294H (red hair)',
            'variant_name': 'D294H',
            'chromosome': '16',
            'position': 89920138,
            'genotypes': {
                'GG': {'color': 'Not red', 'score': 0.0, 'description': 'No red hair variant'},
                'GA': {'color': 'Carrier', 'score': 0.25, 'description': 'Red hair carrier'},
                'AA': {'color': 'Red hair possible', 'score': 0.75, 'description': 'Associated with red hair'}
            },
            'population_frequency': {'G': 0.95, 'A': 0.05}
        },
        # MC1R - V60L
        'rs1805005': {
            'gene': 'MC1R',
            'name': 'MC1R V60L',
            'variant_name': 'V60L',
            'chromosome': '16',
            'position': 89919569,
            'genotypes': {
                'GG': {'color': 'Normal melanin', 'score': 0.5, 'description': 'Typical MC1R function'},
                'GT': {'color': 'Slightly lighter', 'score': 0.4, 'description': 'May lighten hair'},
                'TT': {'color': 'Lighter hair tendency', 'score': 0.3, 'description': 'Associated with lighter hair'}
            },
            'population_frequency': {'G': 0.90, 'T': 0.10}
        },
        # OCA2 - hair color
        'rs1800407': {
            'gene': 'OCA2',
            'name': 'OCA2 R419Q hair',
            'variant_name': 'R419Q',
            'chromosome': '15',
            'position': 28230318,
            'genotypes': {
                'GG': {'color': 'Brown hair tendency', 'score': 0.6, 'description': 'More melanin'},
                'GA': {'color': 'Variable', 'score': 0.45, 'description': 'Intermediate'},
                'AA': {'color': 'Lighter hair', 'score': 0.3, 'description': 'May have lighter hair'}
            },
            'population_frequency': {'G': 0.90, 'A': 0.10}
        },
        # HERC2 - hair darkness
        'rs12913832': {
            'gene': 'HERC2',
            'name': 'HERC2 hair color',
            'variant_name': 'Intronic',
            'chromosome': '15',
            'position': 28365618,
            'genotypes': {
                'GG': {'color': 'Dark hair', 'score': 0.8, 'description': 'Dark pigmentation'},
                'AG': {'color': 'Variable brown', 'score': 0.5, 'description': 'Intermediate'},
                'AA': {'color': 'Blonde/light possible', 'score': 0.2, 'description': 'May have lighter hair'}
            },
            'population_frequency': {'G': 0.75, 'A': 0.25}
        },
        # IRF4 - hair color and graying
        'rs12203592': {
            'gene': 'IRF4',
            'name': 'IRF4 hair pigmentation',
            'variant_name': 'Intronic',
            'chromosome': '6',
            'position': 396321,
            'genotypes': {
                'CC': {'color': 'Dark hair', 'score': 0.7, 'description': 'More melanin'},
                'CT': {'color': 'Variable', 'score': 0.45, 'description': 'Intermediate'},
                'TT': {'color': 'Blonde tendency', 'score': 0.2, 'description': 'Associated with blonde hair'}
            },
            'population_frequency': {'C': 0.85, 'T': 0.15}
        },
        # ASIP - agouti signaling
        'rs6058017': {
            'gene': 'ASIP',
            'name': 'ASIP hair color',
            'variant_name': 'Intronic',
            'chromosome': '20',
            'position': 33558543,
            'genotypes': {
                'AA': {'color': 'Dark hair tendency', 'score': 0.7, 'description': 'More eumelanin'},
                'AG': {'color': 'Variable', 'score': 0.5, 'description': 'Intermediate'},
                'GG': {'color': 'Lighter hair tendency', 'score': 0.3, 'description': 'May have lighter hair'}
            },
            'population_frequency': {'A': 0.60, 'G': 0.40}
        },
        # TYR - tyrosinase hair
        'rs1042602': {
            'gene': 'TYR',
            'name': 'TYR S192Y hair',
            'variant_name': 'S192Y',
            'chromosome': '11',
            'position': 88911696,
            'genotypes': {
                'CC': {'color': 'Normal pigmentation', 'score': 0.5, 'description': 'Typical hair color'},
                'CA': {'color': 'Slightly lighter', 'score': 0.4, 'description': 'May have lighter hair'},
                'AA': {'color': 'Lighter hair', 'score': 0.25, 'description': 'Associated with lighter hair'}
            },
            'population_frequency': {'C': 0.85, 'A': 0.15}
        },
        # SLC24A4 - hair color
        'rs12896399': {
            'gene': 'SLC24A4',
            'name': 'SLC24A4 hair pigment',
            'variant_name': 'Intronic',
            'chromosome': '14',
            'position': 92773663,
            'genotypes': {
                'GG': {'color': 'Dark hair', 'score': 0.65, 'description': 'More melanin'},
                'GT': {'color': 'Variable', 'score': 0.45, 'description': 'Intermediate'},
                'TT': {'color': 'Lighter hair', 'score': 0.3, 'description': 'May have blonde tendencies'}
            },
            'population_frequency': {'G': 0.55, 'T': 0.45}
        },
        # BNC2 - hair and skin
        'rs2153271': {
            'gene': 'BNC2',
            'name': 'BNC2 pigmentation',
            'variant_name': 'Intronic',
            'chromosome': '9',
            'position': 16893389,
            'genotypes': {
                'CC': {'color': 'Dark hair tendency', 'score': 0.6, 'description': 'Darker pigment'},
                'CT': {'color': 'Variable', 'score': 0.45, 'description': 'Intermediate'},
                'TT': {'color': 'Lighter hair tendency', 'score': 0.35, 'description': 'May have lighter hair'}
            },
            'population_frequency': {'C': 0.55, 'T': 0.45}
        },
        # TPCN2 - hair darkness
        'rs35264875': {
            'gene': 'TPCN2',
            'name': 'TPCN2 M484L hair',
            'variant_name': 'M484L',
            'chromosome': '11',
            'position': 68655360,
            'genotypes': {
                'AA': {'color': 'Dark hair', 'score': 0.7, 'description': 'Strong pigment'},
                'AT': {'color': 'Variable', 'score': 0.5, 'description': 'Intermediate'},
                'TT': {'color': 'Lighter hair', 'score': 0.3, 'description': 'May have blonde tendencies'}
            },
            'population_frequency': {'A': 0.65, 'T': 0.35}
        },
        # PIGU - hair pigmentation
        'rs2378249': {
            'gene': 'PIGU',
            'name': 'PIGU hair color',
            'variant_name': 'Intronic',
            'chromosome': '20',
            'position': 33254891,
            'genotypes': {
                'AA': {'color': 'Dark hair', 'score': 0.65, 'description': 'Darker pigment'},
                'AG': {'color': 'Variable', 'score': 0.5, 'description': 'Intermediate'},
                'GG': {'color': 'Lighter hair', 'score': 0.35, 'description': 'May have lighter hair'}
            },
            'population_frequency': {'A': 0.60, 'G': 0.40}
        }
    }
}

# =============================================================================
# HAIR TEXTURE GENETICS
# =============================================================================

HAIR_TEXTURE_GENETICS = {
    'name': 'Hair Texture',
    'description': 'Genetic factors determining hair curliness',
    'markers': {
        # TCHH - trichohyalin (major curly hair gene)
        'rs11803731': {
            'gene': 'TCHH',
            'name': 'TCHH hair texture',
            'chromosome': '1',
            'position': 152190803,
            'genotypes': {
                'AA': {
                    'phenotype': 'Straight hair likely',
                    'texture_score': 0.2,
                    'description': 'Associated with straighter hair'
                },
                'AT': {
                    'phenotype': 'Wavy hair likely',
                    'texture_score': 0.5,
                    'description': 'Intermediate hair texture'
                },
                'TT': {
                    'phenotype': 'Curly hair likely',
                    'texture_score': 0.8,
                    'description': 'Associated with curlier hair'
                }
            },
            'population_frequency': {'A': 0.85, 'T': 0.15},
            'pmid': '19270700'
        },
        # WNT10A - hair follicle development
        'rs7349332': {
            'gene': 'WNT10A',
            'name': 'WNT10A hair variant',
            'chromosome': '2',
            'position': 219754030,
            'genotypes': {
                'CC': {
                    'phenotype': 'Standard texture',
                    'texture_score': 0.5,
                    'description': 'Normal hair development'
                },
                'CT': {
                    'phenotype': 'Slightly finer hair',
                    'texture_score': 0.4,
                    'description': 'May have finer hair'
                },
                'TT': {
                    'phenotype': 'Finer, possibly straighter',
                    'texture_score': 0.3,
                    'description': 'Associated with finer hair'
                }
            },
            'population_frequency': {'C': 0.65, 'T': 0.35},
            'pmid': '23000148'
        },
        # EDAR - hair thickness
        'rs3827760': {
            'gene': 'EDAR',
            'name': 'EDAR V370A',
            'chromosome': '2',
            'position': 109513601,
            'genotypes': {
                'TT': {
                    'phenotype': 'Typical hair thickness',
                    'thickness': 'Normal',
                    'description': 'Standard hair shaft thickness'
                },
                'TC': {
                    'phenotype': 'Thicker hair',
                    'thickness': 'Increased',
                    'description': 'Hair may be thicker than average'
                },
                'CC': {
                    'phenotype': 'Very thick hair',
                    'thickness': 'Very thick',
                    'description': 'Associated with thicker, coarser hair (common in East Asian ancestry)'
                }
            },
            'population_frequency': {'T': 0.92, 'C': 0.08},  # C is rare in non-Asian populations
            'pmid': '18462017'
        },
        # KRT71 - keratin gene
        'rs12130862': {
            'gene': 'KRT71',
            'name': 'KRT71 curly hair',
            'chromosome': '12',
            'position': 52711820,
            'genotypes': {
                'GG': {
                    'phenotype': 'Straighter hair tendency',
                    'texture_score': 0.3,
                    'description': 'Associated with straight hair'
                },
                'GA': {
                    'phenotype': 'Intermediate texture',
                    'texture_score': 0.5,
                    'description': 'Mixed hair texture influence'
                },
                'AA': {
                    'phenotype': 'Curlier hair tendency',
                    'texture_score': 0.7,
                    'description': 'Associated with curly hair'
                }
            },
            'population_frequency': {'G': 0.70, 'A': 0.30},
            'pmid': '19185283'
        }
    }
}

# =============================================================================
# HAIR LOSS / MALE PATTERN BALDNESS
# =============================================================================

HAIR_LOSS_GENETICS = {
    'name': 'Hair Loss (Androgenetic Alopecia)',
    'description': 'Genetic factors affecting male/female pattern hair loss',
    'markers': {
        # AR gene - androgen receptor (X-linked, major baldness gene)
        'rs6152': {
            'gene': 'AR',
            'name': 'Androgen receptor variant',
            'chromosome': 'X',
            'position': 67544705,
            'genotypes': {
                'AA': {
                    'phenotype': 'Lower baldness risk',
                    'risk_score': 0.3,
                    'description': 'Reduced sensitivity to DHT'
                },
                'AG': {
                    'phenotype': 'Moderate baldness risk',
                    'risk_score': 0.5,
                    'description': 'Intermediate risk (males have single allele)'
                },
                'GG': {
                    'phenotype': 'Higher baldness risk',
                    'risk_score': 0.75,
                    'description': 'Increased sensitivity to DHT effects on hair follicles'
                }
            },
            'population_frequency': {'A': 0.40, 'G': 0.60},
            'pmid': '15902657'
        },
        # Chr20p11 - second major baldness locus
        'rs1160312': {
            'gene': '20p11 locus',
            'name': 'Baldness susceptibility locus',
            'chromosome': '20',
            'position': 22153926,
            'genotypes': {
                'AA': {
                    'phenotype': 'Lower baldness risk',
                    'risk_score': 0.3,
                    'description': 'Protective variant'
                },
                'AG': {
                    'phenotype': 'Moderate risk',
                    'risk_score': 0.5,
                    'description': 'Average risk'
                },
                'GG': {
                    'phenotype': 'Higher baldness risk',
                    'risk_score': 0.7,
                    'description': 'Risk variant'
                }
            },
            'population_frequency': {'A': 0.55, 'G': 0.45},
            'pmid': '18849991'
        },
        # HDAC9 - histone deacetylase
        'rs2180439': {
            'gene': 'HDAC9',
            'name': 'HDAC9 baldness variant',
            'chromosome': '7',
            'position': 18635911,
            'genotypes': {
                'TT': {
                    'phenotype': 'Lower risk',
                    'risk_score': 0.35,
                    'description': 'Protective'
                },
                'TC': {
                    'phenotype': 'Moderate risk',
                    'risk_score': 0.5,
                    'description': 'Average'
                },
                'CC': {
                    'phenotype': 'Higher risk',
                    'risk_score': 0.65,
                    'description': 'Increased risk'
                }
            },
            'population_frequency': {'T': 0.65, 'C': 0.35},
            'pmid': '22693459'
        },
        # WNT10A - hair follicle
        'rs17132543': {
            'gene': 'WNT10A',
            'name': 'WNT10A baldness variant',
            'chromosome': '2',
            'position': 219763855,
            'genotypes': {
                'CC': {
                    'phenotype': 'Lower risk',
                    'risk_score': 0.3,
                    'description': 'Better hair follicle maintenance'
                },
                'CT': {
                    'phenotype': 'Moderate risk',
                    'risk_score': 0.5,
                    'description': 'Average'
                },
                'TT': {
                    'phenotype': 'Higher risk',
                    'risk_score': 0.7,
                    'description': 'May affect hair follicle development'
                }
            },
            'population_frequency': {'C': 0.70, 'T': 0.30},
            'pmid': '22693459'
        }
    }
}

# =============================================================================
# FRECKLES GENETICS
# =============================================================================

FRECKLES_GENETICS = {
    'name': 'Freckles',
    'description': 'Genetic tendency to develop freckles',
    'markers': {
        # MC1R - main freckle/red hair gene
        'rs1805007': {
            'gene': 'MC1R',
            'name': 'MC1R R151C (red hair)',
            'chromosome': '16',
            'position': 89919709,
            'genotypes': {
                'CC': {
                    'phenotype': 'No freckle variant',
                    'freckle_score': 0.2,
                    'description': 'Typical MC1R function'
                },
                'CT': {
                    'phenotype': 'Freckle carrier',
                    'freckle_score': 0.6,
                    'description': 'One copy of freckle variant'
                },
                'TT': {
                    'phenotype': 'Strong freckle tendency',
                    'freckle_score': 0.9,
                    'description': 'Two copies - strong freckle/red hair tendency'
                }
            },
            'population_frequency': {'C': 0.92, 'T': 0.08},
            'pmid': '11197177'
        },
        # MC1R rs1805008
        'rs1805008': {
            'gene': 'MC1R',
            'name': 'MC1R R160W',
            'chromosome': '16',
            'position': 89919736,
            'genotypes': {
                'CC': {
                    'phenotype': 'No variant',
                    'freckle_score': 0.2,
                    'description': 'Typical pigmentation'
                },
                'CT': {
                    'phenotype': 'Freckle carrier',
                    'freckle_score': 0.55,
                    'description': 'May have freckles'
                },
                'TT': {
                    'phenotype': 'Likely freckled',
                    'freckle_score': 0.85,
                    'description': 'Strong freckle tendency'
                }
            },
            'population_frequency': {'C': 0.91, 'T': 0.09},
            'pmid': '11197177'
        },
        # IRF4 - interferon regulatory factor
        'rs12203592': {
            'gene': 'IRF4',
            'name': 'IRF4 pigmentation variant',
            'chromosome': '6',
            'position': 396321,
            'genotypes': {
                'CC': {
                    'phenotype': 'Fewer freckles likely',
                    'freckle_score': 0.25,
                    'description': 'Less sun sensitivity'
                },
                'CT': {
                    'phenotype': 'Moderate freckle tendency',
                    'freckle_score': 0.5,
                    'description': 'Intermediate'
                },
                'TT': {
                    'phenotype': 'More freckles likely',
                    'freckle_score': 0.8,
                    'description': 'Higher sun sensitivity, freckling tendency'
                }
            },
            'population_frequency': {'C': 0.85, 'T': 0.15},
            'pmid': '18488026'
        },
        # BNC2 - basonuclin 2
        'rs10756819': {
            'gene': 'BNC2',
            'name': 'BNC2 freckle variant',
            'chromosome': '9',
            'position': 16798628,
            'genotypes': {
                'GG': {
                    'phenotype': 'Less freckling',
                    'freckle_score': 0.3,
                    'description': 'Lower freckle tendency'
                },
                'GA': {
                    'phenotype': 'Moderate freckling',
                    'freckle_score': 0.5,
                    'description': 'Average'
                },
                'AA': {
                    'phenotype': 'More freckling',
                    'freckle_score': 0.7,
                    'description': 'Higher freckle tendency'
                }
            },
            'population_frequency': {'G': 0.58, 'A': 0.42},
            'pmid': '18488026'
        }
    }
}

# =============================================================================
# DIMPLES GENETICS
# =============================================================================

DIMPLES_GENETICS = {
    'name': 'Dimples',
    'description': 'Genetic tendency for facial dimples',
    'markers': {
        # No definitive SNP for dimples - using associated regions
        'rs6795970': {
            'gene': 'SCN5A region',
            'name': 'Dimple-associated region',
            'chromosome': '3',
            'position': 38620424,
            'genotypes': {
                'AA': {
                    'phenotype': 'Dimples less likely',
                    'dimple_score': 0.2,
                    'description': 'Lower probability of dimples'
                },
                'AG': {
                    'phenotype': 'Dimples possible',
                    'dimple_score': 0.5,
                    'description': 'May have dimples'
                },
                'GG': {
                    'phenotype': 'Dimples more likely',
                    'dimple_score': 0.7,
                    'description': 'Higher probability of dimples'
                }
            },
            'population_frequency': {'A': 0.70, 'G': 0.30},
            'note': 'Dimples are thought to be dominant but exact genetics unclear'
        }
    }
}

# =============================================================================
# WIDOW'S PEAK GENETICS
# =============================================================================

WIDOWS_PEAK_GENETICS = {
    'name': "Widow's Peak",
    'description': 'V-shaped hairline point',
    'markers': {
        # Associated genomic regions
        'rs72948020': {
            'gene': 'PAX3 region',
            'name': "Widow's peak associated",
            'chromosome': '2',
            'position': 223159754,
            'genotypes': {
                'CC': {
                    'phenotype': "Straight hairline likely",
                    'widows_peak_score': 0.2,
                    'description': 'V-shaped hairline less likely'
                },
                'CT': {
                    'phenotype': "Slight peak possible",
                    'widows_peak_score': 0.5,
                    'description': 'May have mild widow\'s peak'
                },
                'TT': {
                    'phenotype': "Widow's peak likely",
                    'widows_peak_score': 0.8,
                    'description': 'More likely to have V-shaped hairline'
                }
            },
            'population_frequency': {'C': 0.75, 'T': 0.25}
        }
    }
}

# =============================================================================
# CLEFT CHIN GENETICS
# =============================================================================

CLEFT_CHIN_GENETICS = {
    'name': 'Cleft Chin',
    'description': 'Chin with Y-shaped dimple',
    'markers': {
        # Associated with facial morphology genes
        'rs6082': {
            'gene': 'MFAP2 region',
            'name': 'Cleft chin associated',
            'chromosome': '1',
            'position': 17380406,
            'genotypes': {
                'AA': {
                    'phenotype': 'Smooth chin likely',
                    'cleft_score': 0.2,
                    'description': 'Cleft chin less likely'
                },
                'AG': {
                    'phenotype': 'Mild cleft possible',
                    'cleft_score': 0.5,
                    'description': 'May have slight chin cleft'
                },
                'GG': {
                    'phenotype': 'Cleft chin likely',
                    'cleft_score': 0.75,
                    'description': 'More likely to have chin cleft'
                }
            },
            'population_frequency': {'A': 0.65, 'G': 0.35}
        }
    }
}

# =============================================================================
# EARLOBE ATTACHMENT GENETICS
# =============================================================================

EARLOBE_GENETICS = {
    'name': 'Earlobe Attachment',
    'description': 'Attached vs free (detached) earlobes',
    'markers': {
        # Main earlobe gene
        'rs10195871': {
            'gene': 'EDAR region',
            'name': 'Earlobe attachment variant',
            'chromosome': '2',
            'position': 109609604,
            'genotypes': {
                'TT': {
                    'phenotype': 'Free (detached) earlobes',
                    'attached_score': 0.2,
                    'description': 'Earlobes hang freely'
                },
                'TC': {
                    'phenotype': 'Intermediate attachment',
                    'attached_score': 0.5,
                    'description': 'Partially attached earlobes'
                },
                'CC': {
                    'phenotype': 'Attached earlobes',
                    'attached_score': 0.8,
                    'description': 'Earlobes attached to head'
                }
            },
            'population_frequency': {'T': 0.55, 'C': 0.45},
            'pmid': '28293654'
        },
        # Secondary earlobe gene
        'rs1129038': {
            'gene': 'HERC2',
            'name': 'HERC2 earlobe influence',
            'chromosome': '15',
            'position': 28356859,
            'genotypes': {
                'AA': {
                    'phenotype': 'Free lobes more likely',
                    'attached_score': 0.3,
                    'description': 'Associated with detached earlobes'
                },
                'AG': {
                    'phenotype': 'Variable',
                    'attached_score': 0.5,
                    'description': 'Intermediate'
                },
                'GG': {
                    'phenotype': 'Attached more likely',
                    'attached_score': 0.7,
                    'description': 'Associated with attached earlobes'
                }
            },
            'population_frequency': {'A': 0.65, 'G': 0.35},
            'pmid': '28293654'
        }
    }
}

# =============================================================================
# TONGUE ROLLING GENETICS
# =============================================================================

TONGUE_ROLLING_GENETICS = {
    'name': 'Tongue Rolling',
    'description': 'Ability to roll tongue into a tube shape',
    'markers': {
        # Note: Twin studies show tongue rolling is NOT purely genetic
        # but there are associated variants
        'rs6944723': {
            'gene': 'Unknown',
            'name': 'Tongue rolling associated',
            'chromosome': '7',
            'position': 35159321,
            'genotypes': {
                'AA': {
                    'phenotype': 'Likely can roll tongue',
                    'rolling_score': 0.75,
                    'description': 'Higher probability of tongue rolling ability'
                },
                'AG': {
                    'phenotype': 'May be able to roll tongue',
                    'rolling_score': 0.55,
                    'description': 'Intermediate - most people can learn'
                },
                'GG': {
                    'phenotype': 'May need practice',
                    'rolling_score': 0.35,
                    'description': 'Lower natural ability but often learnable'
                }
            },
            'population_frequency': {'A': 0.60, 'G': 0.40},
            'note': 'Tongue rolling can be learned - genetics is only partial influence'
        }
    }
}

# =============================================================================
# FINGER LENGTH RATIO (2D:4D) GENETICS
# =============================================================================

FINGER_RATIO_GENETICS = {
    'name': 'Finger Length Ratio (2D:4D)',
    'description': 'Ratio of index to ring finger - related to prenatal testosterone',
    'markers': {
        # Androgen receptor related
        'rs17268285': {
            'gene': 'LIN28B',
            'name': 'LIN28B digit ratio',
            'chromosome': '6',
            'position': 105404946,
            'genotypes': {
                'CC': {
                    'phenotype': 'Lower 2D:4D ratio',
                    'ratio_tendency': 'Lower (more masculine pattern)',
                    'description': 'Ring finger tends to be longer relative to index'
                },
                'CT': {
                    'phenotype': 'Intermediate ratio',
                    'ratio_tendency': 'Average',
                    'description': 'Typical digit ratio'
                },
                'TT': {
                    'phenotype': 'Higher 2D:4D ratio',
                    'ratio_tendency': 'Higher (more feminine pattern)',
                    'description': 'Index and ring fingers more similar length'
                }
            },
            'population_frequency': {'C': 0.55, 'T': 0.45},
            'pmid': '21909115'
        },
        # Another associated variant
        'rs314277': {
            'gene': 'LIN28B',
            'name': 'LIN28B digit ratio #2',
            'chromosome': '6',
            'position': 105443686,
            'genotypes': {
                'CC': {
                    'phenotype': 'Lower ratio tendency',
                    'ratio_tendency': 'Lower',
                    'description': 'Associated with lower 2D:4D'
                },
                'CA': {
                    'phenotype': 'Average ratio',
                    'ratio_tendency': 'Average',
                    'description': 'Typical'
                },
                'AA': {
                    'phenotype': 'Higher ratio tendency',
                    'ratio_tendency': 'Higher',
                    'description': 'Associated with higher 2D:4D'
                }
            },
            'population_frequency': {'C': 0.50, 'A': 0.50},
            'pmid': '21909115'
        }
    }
}


# =============================================================================
# COMPLETE PHYSICAL TRAITS EXPANDED DATABASE
# =============================================================================

PHYSICAL_TRAITS_EXPANDED_DATABASE = {
    'height': HEIGHT_GENETICS,
    'hair_texture': HAIR_TEXTURE_GENETICS,
    'hair_loss': HAIR_LOSS_GENETICS,
    'freckles': FRECKLES_GENETICS,
    'dimples': DIMPLES_GENETICS,
    'widows_peak': WIDOWS_PEAK_GENETICS,
    'cleft_chin': CLEFT_CHIN_GENETICS,
    'earlobes': EARLOBE_GENETICS,
    'tongue_rolling': TONGUE_ROLLING_GENETICS,
    'finger_ratio': FINGER_RATIO_GENETICS
}


# =============================================================================
# ANALYSIS FUNCTIONS
# =============================================================================

def analyze_physical_traits_expanded(dna_data: dict) -> dict:
    """
    Comprehensive expanded physical traits analysis

    Args:
        dna_data: Dictionary of rsid -> genotype

    Returns:
        Dictionary with all expanded physical trait analysis
    """
    results = {
        'height': analyze_height(dna_data),
        'hair_texture': analyze_hair_texture(dna_data),
        'hair_loss': analyze_hair_loss(dna_data),
        'freckles': analyze_freckles(dna_data),
        'dimples': analyze_dimples(dna_data),
        'widows_peak': analyze_widows_peak(dna_data),
        'cleft_chin': analyze_cleft_chin(dna_data),
        'earlobes': analyze_earlobes(dna_data),
        'tongue_rolling': analyze_tongue_rolling(dna_data),
        'finger_ratio': analyze_finger_ratio(dna_data)
    }

    # Calculate overall traits summary
    results['summary'] = generate_physical_summary(results)

    return results


def analyze_height(dna_data: dict) -> dict:
    """Analyze height genetics"""
    result = {
        'percentile_adjustment': 0,
        'cm_adjustment': 0,
        'prediction': 'Average genetic height',
        'markers_found': [],
        'confidence': 0.5,
        'description': ''
    }

    cm_adjustments = []
    percentile_shifts = []

    for rsid, marker_data in HEIGHT_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                cm_adjustments.append(data.get('cm_adjustment', 0))
                percentile_shifts.append(data.get('percentile_shift', 0))
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'effect': data['effect'],
                    'cm_adjustment': data.get('cm_adjustment', 0)
                })

    if cm_adjustments:
        total_cm = sum(cm_adjustments)
        total_percentile = sum(percentile_shifts)
        result['cm_adjustment'] = round(total_cm, 1)
        result['percentile_adjustment'] = round(total_percentile, 0)
        result['confidence'] = min(0.5 + len(cm_adjustments) * 0.05, 0.85)

        if total_cm >= 1.5:
            result['prediction'] = 'Above average height genetics'
            result['description'] = f'Your height variants suggest you are genetically predisposed to be taller than average (approximately +{total_cm:.1f}cm from baseline).'
        elif total_cm <= -1.5:
            result['prediction'] = 'Below average height genetics'
            result['description'] = f'Your height variants suggest you are genetically predisposed to be shorter than average (approximately {total_cm:.1f}cm from baseline).'
        else:
            result['prediction'] = 'Average height genetics'
            result['description'] = 'Your height-related variants are typical, suggesting average height genetics.'

    return result


def analyze_hair_texture(dna_data: dict) -> dict:
    """Analyze hair texture genetics"""
    result = {
        'texture': 'Wavy',
        'texture_score': 0.5,
        'thickness': 'Normal',
        'markers_found': [],
        'description': ''
    }

    texture_scores = []

    for rsid, marker_data in HAIR_TEXTURE_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]

                if 'texture_score' in data:
                    texture_scores.append(data['texture_score'])

                if 'thickness' in data:
                    result['thickness'] = data['thickness']

                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })

    if texture_scores:
        avg_score = sum(texture_scores) / len(texture_scores)
        result['texture_score'] = avg_score

        if avg_score >= 0.7:
            result['texture'] = 'Curly'
            result['description'] = 'Your genetics suggest curly or very wavy hair.'
        elif avg_score >= 0.45:
            result['texture'] = 'Wavy'
            result['description'] = 'Your genetics suggest wavy hair texture.'
        else:
            result['texture'] = 'Straight'
            result['description'] = 'Your genetics suggest straight or slightly wavy hair.'

    return result


def analyze_hair_loss(dna_data: dict) -> dict:
    """Analyze hair loss / baldness genetics"""
    result = {
        'risk_level': 'Average',
        'risk_score': 0.5,
        'markers_found': [],
        'description': '',
        'onset_likelihood': 'Typical'
    }

    risk_scores = []

    for rsid, marker_data in HAIR_LOSS_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                risk_scores.append(data.get('risk_score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })

    if risk_scores:
        avg_risk = sum(risk_scores) / len(risk_scores)
        result['risk_score'] = avg_risk

        if avg_risk >= 0.65:
            result['risk_level'] = 'Higher'
            result['onset_likelihood'] = 'Earlier onset possible'
            result['description'] = 'Your genetics suggest higher susceptibility to androgenetic alopecia (pattern hair loss).'
        elif avg_risk <= 0.4:
            result['risk_level'] = 'Lower'
            result['onset_likelihood'] = 'Later or no significant loss'
            result['description'] = 'Your genetics suggest lower susceptibility to pattern hair loss.'
        else:
            result['risk_level'] = 'Average'
            result['onset_likelihood'] = 'Typical'
            result['description'] = 'Your hair loss genetics are about average.'

    return result


def analyze_freckles(dna_data: dict) -> dict:
    """Analyze freckle genetics"""
    result = {
        'likelihood': 'Average',
        'prediction': 'Average likelihood',
        'freckle_score': 0.5,
        'markers_found': [],
        'description': ''
    }

    freckle_scores = []

    for rsid, marker_data in FRECKLES_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:
                data = genotypes[_key]
                freckle_scores.append(data.get('freckle_score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })

    if freckle_scores:
        avg_score = sum(freckle_scores) / len(freckle_scores)
        result['freckle_score'] = avg_score

        if avg_score >= 0.65:
            result['likelihood'] = 'High'
            result['prediction'] = 'Likely to have freckles'
            result['description'] = 'You likely have or will develop freckles, especially with sun exposure.'
        elif avg_score <= 0.35:
            result['likelihood'] = 'Low'
            result['prediction'] = 'Unlikely to have freckles'
            result['description'] = 'You are less likely to develop freckles.'
        else:
            result['likelihood'] = 'Average'
            result['prediction'] = 'Average likelihood'
            result['description'] = 'You have an average tendency for freckling.'

    return result


def analyze_dimples(dna_data: dict) -> dict:
    """Analyze dimple genetics"""
    result = {
        'likelihood': 'Possible',
        'prediction': 'Possibly present',
        'score': 0.5,
        'markers_found': [],
        'description': 'Dimples are thought to be dominant but genetics is not fully understood.'
    }

    for rsid, marker_data in DIMPLES_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:
                data = genotypes[_key]
                result['score'] = data.get('dimple_score', 0.5)
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })

                if result['score'] >= 0.6:
                    result['likelihood'] = 'Likely'
                    result['prediction'] = 'Likely present'
                    result['description'] = 'You may have facial dimples.'
                elif result['score'] <= 0.35:
                    result['likelihood'] = 'Less likely'
                    result['prediction'] = 'Unlikely'
                    result['description'] = 'You are less likely to have dimples.'

    return result


def analyze_widows_peak(dna_data: dict) -> dict:
    """Analyze widow's peak genetics"""
    result = {
        'likelihood': 'Possible',
        'prediction': 'Possible',
        'score': 0.5,
        'markers_found': [],
        'description': ''
    }

    for rsid, marker_data in WIDOWS_PEAK_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                result['score'] = data.get('widows_peak_score', 0.5)
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })

                if result['score'] >= 0.6:
                    result['likelihood'] = 'Likely'
                    result['prediction'] = 'Likely present'
                    result['description'] = "You likely have a widow's peak (V-shaped hairline)."
                elif result['score'] <= 0.35:
                    result['likelihood'] = 'Less likely'
                    result['prediction'] = 'Unlikely'
                    result['description'] = 'You likely have a straight or rounded hairline.'

    return result


def analyze_cleft_chin(dna_data: dict) -> dict:
    """Analyze cleft chin genetics"""
    result = {
        'likelihood': 'Possible',
        'prediction': 'Possible',
        'score': 0.5,
        'markers_found': [],
        'description': ''
    }

    for rsid, marker_data in CLEFT_CHIN_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                result['score'] = data.get('cleft_score', 0.5)
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })

                if result['score'] >= 0.6:
                    result['likelihood'] = 'Likely'
                    result['prediction'] = 'Likely present'
                    result['description'] = 'You may have a cleft chin (chin dimple).'
                elif result['score'] <= 0.35:
                    result['likelihood'] = 'Less likely'
                    result['prediction'] = 'Unlikely'
                    result['description'] = 'You likely have a smooth chin without a cleft.'

    return result


def analyze_earlobes(dna_data: dict) -> dict:
    """Analyze earlobe attachment genetics"""
    result = {
        'type': 'Variable',
        'prediction': 'Variable',
        'attached_score': 0.5,
        'markers_found': [],
        'description': ''
    }

    scores = []

    for rsid, marker_data in EARLOBE_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                scores.append(data.get('attached_score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })

    if scores:
        avg_score = sum(scores) / len(scores)
        result['attached_score'] = avg_score

        if avg_score >= 0.65:
            result['type'] = 'Attached'
            result['prediction'] = 'Attached'
            result['description'] = 'You likely have attached earlobes (earlobes connected directly to head).'
        elif avg_score <= 0.35:
            result['type'] = 'Free (Detached)'
            result['prediction'] = 'Free (Detached)'
            result['description'] = 'You likely have free (detached) earlobes that hang down.'
        else:
            result['type'] = 'Partially Attached'
            result['prediction'] = 'Partially Attached'
            result['description'] = 'You likely have partially attached earlobes.'

    return result


def analyze_tongue_rolling(dna_data: dict) -> dict:
    """Analyze tongue rolling genetics"""
    result = {
        'ability': 'Possible',
        'prediction': 'Possible',
        'score': 0.55,  # Most people can roll tongue
        'markers_found': [],
        'description': 'Most people can roll their tongue - it can be learned even without genetic predisposition.'
    }

    for rsid, marker_data in TONGUE_ROLLING_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                result['score'] = data.get('rolling_score', 0.55)
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })

                if result['score'] >= 0.65:
                    result['ability'] = 'Likely can'
                    result['prediction'] = 'Likely can roll'
                    result['description'] = 'You likely have natural tongue rolling ability.'
                elif result['score'] <= 0.4:
                    result['ability'] = 'May need practice'
                    result['prediction'] = 'May need practice'
                    result['description'] = 'You may need to practice to roll your tongue, but most people can learn.'

    return result


def analyze_finger_ratio(dna_data: dict) -> dict:
    """Analyze finger length ratio (2D:4D) genetics"""
    result = {
        'tendency': 'Average',
        'prediction': 'Average ratio',
        'description': '',
        'markers_found': []
    }

    tendencies = []

    for rsid, marker_data in FINGER_RATIO_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                tendencies.append(data.get('ratio_tendency', 'Average'))
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'ratio_tendency': data.get('ratio_tendency', 'Average')
                })

    if tendencies:
        lower_count = tendencies.count('Lower') + tendencies.count('Lower (more masculine pattern)')
        higher_count = tendencies.count('Higher') + tendencies.count('Higher (more feminine pattern)')

        if lower_count > higher_count:
            result['tendency'] = 'Lower 2D:4D'
            result['prediction'] = 'Lower ratio (ring finger longer)'
            result['description'] = 'Your genetics suggest a lower digit ratio (ring finger longer than index), associated with higher prenatal testosterone exposure.'
        elif higher_count > lower_count:
            result['tendency'] = 'Higher 2D:4D'
            result['prediction'] = 'Higher ratio (similar length)'
            result['description'] = 'Your genetics suggest a higher digit ratio (index and ring fingers similar length), associated with lower prenatal testosterone exposure.'
        else:
            result['tendency'] = 'Average 2D:4D'
            result['prediction'] = 'Average ratio'
            result['description'] = 'Your genetics suggest a typical digit ratio.'

    return result


def generate_physical_summary(results: dict) -> dict:
    """Generate summary of physical traits"""
    summary = {
        'notable_traits': [],
        'rare_traits': []
    }

    # Height
    height = results.get('height', {})
    if abs(height.get('cm_adjustment', 0)) >= 1:
        if height.get('cm_adjustment', 0) > 0:
            summary['notable_traits'].append('Taller than average genetics')
        else:
            summary['notable_traits'].append('Shorter than average genetics')

    # Hair texture
    hair = results.get('hair_texture', {})
    if hair.get('texture') == 'Curly':
        summary['notable_traits'].append('Curly hair genetics')
    if hair.get('thickness') == 'Very thick':
        summary['notable_traits'].append('Very thick hair (EDAR variant)')
        summary['rare_traits'].append('Thick hair variant')

    # Hair loss
    loss = results.get('hair_loss', {})
    if loss.get('risk_level') == 'Higher':
        summary['notable_traits'].append('Higher hair loss susceptibility')
    elif loss.get('risk_level') == 'Lower':
        summary['notable_traits'].append('Lower hair loss risk')

    # Freckles
    freckles = results.get('freckles', {})
    if freckles.get('likelihood') == 'High':
        summary['notable_traits'].append('High freckling tendency')

    # Other traits
    if results.get('dimples', {}).get('likelihood') == 'Likely':
        summary['notable_traits'].append('Likely has dimples')

    if results.get('widows_peak', {}).get('likelihood') == 'Likely':
        summary['notable_traits'].append("Likely has widow's peak")

    if results.get('cleft_chin', {}).get('likelihood') == 'Likely':
        summary['notable_traits'].append('Likely has cleft chin')

    return summary
