#!/usr/bin/env python3
"""
Reproduction & Fertility Genetics Database
Comprehensive database for reproductive health genetic analysis

Features:
1. Male fertility factors
2. Female fertility / ovarian reserve
3. Menopause timing
4. Twin probability
5. Endometriosis risk
6. PCOS risk
7. Testosterone levels
8. Estrogen metabolism
9. Pregnancy complications risk
10. Reproductive hormone sensitivity

Data sources:
- GWAS Catalog (reproductive genetics studies)
- dbSNP (NCBI)
- Published fertility research
"""

from typing import Dict, Any, List

# =============================================================================
# MALE FERTILITY GENETICS
# =============================================================================

MALE_FERTILITY_GENETICS = {
    'name': 'Male Fertility Factors',
    'description': 'Genetic factors affecting male reproductive health',
    'markers': {
        # FSHR - follicle stimulating hormone receptor
        'rs6166': {
            'gene': 'FSHR',
            'name': 'FSHR Asn680Ser',
            'variant_name': 'N680S',
            'chromosome': '2',
            'position': 49189921,
            'genotypes': {
                'AA': {
                    'phenotype': 'Higher FSH sensitivity',
                    'fertility_score': 0.7,
                    'description': 'Better response to FSH, potentially better sperm production'
                },
                'AG': {
                    'phenotype': 'Normal FSH response',
                    'fertility_score': 0.5,
                    'description': 'Typical hormonal response'
                },
                'GG': {
                    'phenotype': 'Lower FSH sensitivity',
                    'fertility_score': 0.35,
                    'description': 'May need higher FSH levels for optimal function'
                }
            },
            'population_frequency': {'A': 0.45, 'G': 0.55},
            'pmid': '10073974'
        },
        # MTHFR - folate metabolism affects sperm
        'rs1801133': {
            'gene': 'MTHFR',
            'name': 'MTHFR C677T',
            'variant_name': 'A222V',
            'chromosome': '1',
            'position': 11796321,
            'genotypes': {
                'CC': {
                    'phenotype': 'Normal folate metabolism',
                    'fertility_score': 0.7,
                    'description': 'Optimal folate processing for DNA synthesis'
                },
                'CT': {
                    'phenotype': 'Reduced enzyme activity',
                    'fertility_score': 0.5,
                    'description': 'Moderately reduced - ensure adequate folate intake'
                },
                'TT': {
                    'phenotype': 'Significantly reduced activity',
                    'fertility_score': 0.3,
                    'description': 'May benefit from methylfolate supplementation'
                }
            },
            'population_frequency': {'C': 0.65, 'T': 0.35},
            'pmid': '9545414'
        },
        # USP26 - ubiquitin specific peptidase
        'rs4499243': {
            'gene': 'USP26',
            'name': 'USP26 fertility variant',
            'variant_name': 'Intronic',
            'chromosome': 'X',
            'position': 132082689,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal spermatogenesis',
                    'fertility_score': 0.6,
                    'description': 'Typical sperm development'
                },
                'GA': {
                    'phenotype': 'Slightly reduced',
                    'fertility_score': 0.45,
                    'description': 'May have mild effect on sperm'
                },
                'AA': {
                    'phenotype': 'Reduced spermatogenesis risk',
                    'fertility_score': 0.3,
                    'description': 'Associated with reduced sperm count in some studies'
                }
            },
            'population_frequency': {'G': 0.80, 'A': 0.20},
            'pmid': '17329263'
        },
        # DAZL - Deleted in Azoospermia-Like
        'rs10459525': {
            'gene': 'DAZL',
            'name': 'DAZL sperm production',
            'variant_name': 'Intronic',
            'chromosome': '3',
            'position': 16610565,
            'genotypes': {
                'TT': {
                    'phenotype': 'Normal sperm production',
                    'fertility_score': 0.65,
                    'description': 'Typical spermatogenesis'
                },
                'TC': {
                    'phenotype': 'Slightly reduced',
                    'fertility_score': 0.45,
                    'description': 'May have minor effect'
                },
                'CC': {
                    'phenotype': 'Reduced production risk',
                    'fertility_score': 0.3,
                    'description': 'Associated with lower sperm count'
                }
            },
            'population_frequency': {'T': 0.75, 'C': 0.25},
            'pmid': '21949963'
        },
        # TEX11 - Testis Expressed 11
        'rs67511694': {
            'gene': 'TEX11',
            'name': 'TEX11 meiosis gene',
            'variant_name': 'Intronic',
            'chromosome': 'X',
            'position': 70560123,
            'genotypes': {
                'CC': {
                    'phenotype': 'Normal meiosis',
                    'fertility_score': 0.6,
                    'description': 'Typical sperm cell division'
                },
                'CT': {
                    'phenotype': 'Slightly reduced',
                    'fertility_score': 0.45,
                    'description': 'May affect meiosis efficiency'
                },
                'TT': {
                    'phenotype': 'Meiosis defects risk',
                    'fertility_score': 0.25,
                    'description': 'Associated with azoospermia risk'
                }
            },
            'population_frequency': {'C': 0.85, 'T': 0.15},
            'pmid': '26061702'
        },
        # CATSPER1 - Sperm motility channel
        'rs2845570': {
            'gene': 'CATSPER1',
            'name': 'CATSPER1 sperm motility',
            'variant_name': 'Intronic',
            'chromosome': '11',
            'position': 65980123,
            'genotypes': {
                'AA': {
                    'phenotype': 'Normal sperm motility',
                    'fertility_score': 0.65,
                    'description': 'Good calcium signaling in sperm'
                },
                'AG': {
                    'phenotype': 'Slightly reduced motility',
                    'fertility_score': 0.5,
                    'description': 'May have minor motility effect'
                },
                'GG': {
                    'phenotype': 'Reduced motility risk',
                    'fertility_score': 0.3,
                    'description': 'Associated with asthenozoospermia'
                }
            },
            'population_frequency': {'A': 0.70, 'G': 0.30},
            'pmid': '23832394'
        },
        # SPATA16 - Globozoospermia gene
        'rs10841911': {
            'gene': 'SPATA16',
            'name': 'SPATA16 sperm morphology',
            'variant_name': 'Intronic',
            'chromosome': '3',
            'position': 172982341,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal sperm morphology',
                    'fertility_score': 0.6,
                    'description': 'Typical sperm head formation'
                },
                'GA': {
                    'phenotype': 'Normal',
                    'fertility_score': 0.55,
                    'description': 'Carrier status'
                },
                'AA': {
                    'phenotype': 'Morphology risk',
                    'fertility_score': 0.3,
                    'description': 'Risk for abnormal sperm shape'
                }
            },
            'population_frequency': {'G': 0.95, 'A': 0.05},
            'pmid': '17828264'
        },
        # SYCP3 - Synaptonemal complex protein
        'rs28369952': {
            'gene': 'SYCP3',
            'name': 'SYCP3 meiosis',
            'variant_name': 'Intronic',
            'chromosome': '12',
            'position': 121682943,
            'genotypes': {
                'CC': {
                    'phenotype': 'Normal meiosis',
                    'fertility_score': 0.6,
                    'description': 'Normal chromosome pairing'
                },
                'CT': {
                    'phenotype': 'Carrier',
                    'fertility_score': 0.5,
                    'description': 'Carrier for meiosis variant'
                },
                'TT': {
                    'phenotype': 'Meiosis arrest risk',
                    'fertility_score': 0.25,
                    'description': 'Risk for spermatogenic failure'
                }
            },
            'population_frequency': {'C': 0.97, 'T': 0.03},
            'pmid': '17360642'
        },
        # AR - Androgen receptor CAG repeat proxy
        'rs6152': {
            'gene': 'AR',
            'name': 'AR androgen receptor',
            'variant_name': 'E211E',
            'chromosome': 'X',
            'position': 67545785,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal androgen response',
                    'fertility_score': 0.6,
                    'description': 'Typical testosterone sensitivity'
                },
                'GA': {
                    'phenotype': 'Slightly altered',
                    'fertility_score': 0.5,
                    'description': 'Minor variation in androgen response'
                },
                'AA': {
                    'phenotype': 'Altered sensitivity',
                    'fertility_score': 0.4,
                    'description': 'May have altered testosterone response'
                }
            },
            'population_frequency': {'G': 0.65, 'A': 0.35},
            'pmid': '12414817'
        },
        # NR5A1/SF-1 - Steroidogenic factor 1
        'rs1110061': {
            'gene': 'NR5A1',
            'name': 'SF-1 hormone regulation',
            'variant_name': 'D238E',
            'chromosome': '9',
            'position': 127266034,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal steroidogenesis',
                    'fertility_score': 0.6,
                    'description': 'Normal hormone production'
                },
                'GA': {
                    'phenotype': 'Slightly altered',
                    'fertility_score': 0.5,
                    'description': 'Minor effect on hormone levels'
                },
                'AA': {
                    'phenotype': 'Reduced function',
                    'fertility_score': 0.35,
                    'description': 'May affect testosterone production'
                }
            },
            'population_frequency': {'G': 0.90, 'A': 0.10},
            'pmid': '20534580'
        },
        # SPEM1 - Sperm maturation
        'rs7174015': {
            'gene': 'SPEM1',
            'name': 'SPEM1 sperm maturation',
            'variant_name': 'Intronic',
            'chromosome': '15',
            'position': 46237892,
            'genotypes': {
                'AA': {
                    'phenotype': 'Normal maturation',
                    'fertility_score': 0.6,
                    'description': 'Normal sperm development'
                },
                'AG': {
                    'phenotype': 'Normal',
                    'fertility_score': 0.55,
                    'description': 'Typical'
                },
                'GG': {
                    'phenotype': 'Maturation variant',
                    'fertility_score': 0.4,
                    'description': 'May affect sperm maturation'
                }
            },
            'population_frequency': {'A': 0.75, 'G': 0.25},
            'pmid': '24549045'
        },
        # DMRT1 - Testis determination
        'rs755383': {
            'gene': 'DMRT1',
            'name': 'DMRT1 testis development',
            'variant_name': 'Intronic',
            'chromosome': '9',
            'position': 841892,
            'genotypes': {
                'CC': {
                    'phenotype': 'Normal testis function',
                    'fertility_score': 0.6,
                    'description': 'Normal germ cell development'
                },
                'CT': {
                    'phenotype': 'Normal',
                    'fertility_score': 0.55,
                    'description': 'Typical development'
                },
                'TT': {
                    'phenotype': 'Variant',
                    'fertility_score': 0.4,
                    'description': 'May have minor effect'
                }
            },
            'population_frequency': {'C': 0.70, 'T': 0.30},
            'pmid': '24319106'
        }
    }
}

# =============================================================================
# FEMALE FERTILITY / OVARIAN RESERVE
# =============================================================================

FEMALE_FERTILITY_GENETICS = {
    'name': 'Female Fertility Factors',
    'description': 'Genetic factors affecting female reproductive health',
    'markers': {
        # AMH - anti-mullerian hormone
        'rs10407022': {
            'gene': 'AMH',
            'name': 'AMH ovarian reserve variant',
            'variant_name': 'Intronic',
            'chromosome': '19',
            'position': 2249501,
            'genotypes': {
                'TT': {
                    'phenotype': 'Higher ovarian reserve tendency',
                    'fertility_score': 0.7,
                    'description': 'May have higher egg count'
                },
                'TC': {
                    'phenotype': 'Average ovarian reserve',
                    'fertility_score': 0.5,
                    'description': 'Typical egg reserve'
                },
                'CC': {
                    'phenotype': 'Lower ovarian reserve tendency',
                    'fertility_score': 0.35,
                    'description': 'May have lower AMH levels'
                }
            },
            'population_frequency': {'T': 0.55, 'C': 0.45},
            'pmid': '24664130'
        },
        # AMHR2 - AMH receptor
        'rs2002555': {
            'gene': 'AMHR2',
            'name': 'AMHR2 receptor function',
            'variant_name': 'A/G',
            'chromosome': '12',
            'position': 53500234,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal AMH signaling',
                    'fertility_score': 0.6,
                    'description': 'Typical ovarian response to AMH'
                },
                'GA': {
                    'phenotype': 'Slightly altered',
                    'fertility_score': 0.5,
                    'description': 'Minor variation'
                },
                'AA': {
                    'phenotype': 'Altered signaling',
                    'fertility_score': 0.4,
                    'description': 'May have altered ovarian reserve response'
                }
            },
            'population_frequency': {'G': 0.65, 'A': 0.35},
            'pmid': '22291147'
        },
        # FSHR - also important for females
        'rs6165': {
            'gene': 'FSHR',
            'name': 'FSHR Thr307Ala',
            'variant_name': 'T307A',
            'chromosome': '2',
            'position': 49189614,
            'genotypes': {
                'AA': {
                    'phenotype': 'Higher ovarian response',
                    'fertility_score': 0.7,
                    'description': 'Better response to fertility treatments'
                },
                'AG': {
                    'phenotype': 'Normal ovarian response',
                    'fertility_score': 0.5,
                    'description': 'Typical response'
                },
                'GG': {
                    'phenotype': 'Lower ovarian response',
                    'fertility_score': 0.35,
                    'description': 'May need higher FSH doses in IVF'
                }
            },
            'population_frequency': {'A': 0.48, 'G': 0.52},
            'pmid': '10073974'
        },
        # ESR1 - estrogen receptor
        'rs2234693': {
            'gene': 'ESR1',
            'name': 'ESR1 PvuII',
            'variant_name': 'PvuII',
            'chromosome': '6',
            'position': 152163335,
            'genotypes': {
                'TT': {
                    'phenotype': 'Enhanced estrogen response',
                    'fertility_score': 0.65,
                    'description': 'Better estrogen signaling'
                },
                'TC': {
                    'phenotype': 'Normal estrogen response',
                    'fertility_score': 0.5,
                    'description': 'Typical response'
                },
                'CC': {
                    'phenotype': 'Reduced estrogen response',
                    'fertility_score': 0.4,
                    'description': 'May have altered estrogen sensitivity'
                }
            },
            'population_frequency': {'T': 0.45, 'C': 0.55},
            'pmid': '15466653'
        },
        # ESR2 - estrogen receptor beta
        'rs4986938': {
            'gene': 'ESR2',
            'name': 'ESR2 AluI',
            'variant_name': 'AluI',
            'chromosome': '14',
            'position': 64286380,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal ESR2 function',
                    'fertility_score': 0.6,
                    'description': 'Typical ovarian function'
                },
                'GA': {
                    'phenotype': 'Carrier',
                    'fertility_score': 0.5,
                    'description': 'Intermediate'
                },
                'AA': {
                    'phenotype': 'Variant',
                    'fertility_score': 0.4,
                    'description': 'May affect ovarian function'
                }
            },
            'population_frequency': {'G': 0.70, 'A': 0.30},
            'pmid': '16369026'
        },
        # BMP15 - bone morphogenetic protein 15
        'rs17003221': {
            'gene': 'BMP15',
            'name': 'BMP15 ovarian function',
            'variant_name': 'Intronic',
            'chromosome': 'X',
            'position': 50907837,
            'genotypes': {
                'TT': {
                    'phenotype': 'Normal ovarian function',
                    'fertility_score': 0.6,
                    'description': 'Typical follicle development'
                },
                'TC': {
                    'phenotype': 'Carrier',
                    'fertility_score': 0.5,
                    'description': 'May have minor variation'
                },
                'CC': {
                    'phenotype': 'Variant',
                    'fertility_score': 0.35,
                    'description': 'Associated with POI risk'
                }
            },
            'population_frequency': {'T': 0.95, 'C': 0.05},
            'pmid': '15240982'
        },
        # GDF9 - growth differentiation factor 9
        'rs10491279': {
            'gene': 'GDF9',
            'name': 'GDF9 oocyte development',
            'variant_name': 'Intronic',
            'chromosome': '5',
            'position': 132142623,
            'genotypes': {
                'CC': {
                    'phenotype': 'Normal oocyte development',
                    'fertility_score': 0.6,
                    'description': 'Typical egg quality'
                },
                'CT': {
                    'phenotype': 'Carrier',
                    'fertility_score': 0.5,
                    'description': 'Minor variation'
                },
                'TT': {
                    'phenotype': 'Variant',
                    'fertility_score': 0.35,
                    'description': 'May affect egg quality'
                }
            },
            'population_frequency': {'C': 0.90, 'T': 0.10},
            'pmid': '17293724'
        },
        # NOBOX - newborn ovary homeobox
        'rs10958044': {
            'gene': 'NOBOX',
            'name': 'NOBOX ovarian development',
            'variant_name': 'Intronic',
            'chromosome': '7',
            'position': 144394523,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal ovarian development',
                    'fertility_score': 0.6,
                    'description': 'Typical'
                },
                'GA': {
                    'phenotype': 'Carrier',
                    'fertility_score': 0.5,
                    'description': 'Minor variation'
                },
                'AA': {
                    'phenotype': 'POI risk variant',
                    'fertility_score': 0.3,
                    'description': 'Associated with premature ovarian insufficiency'
                }
            },
            'population_frequency': {'G': 0.98, 'A': 0.02},
            'pmid': '19336423'
        },
        # FIGLA - folliculogenesis specific bHLH
        'rs6946417': {
            'gene': 'FIGLA',
            'name': 'FIGLA follicle formation',
            'variant_name': 'Intronic',
            'chromosome': '2',
            'position': 71064532,
            'genotypes': {
                'AA': {
                    'phenotype': 'Normal follicle formation',
                    'fertility_score': 0.6,
                    'description': 'Typical folliculogenesis'
                },
                'AG': {
                    'phenotype': 'Carrier',
                    'fertility_score': 0.5,
                    'description': 'Minor effect'
                },
                'GG': {
                    'phenotype': 'Variant',
                    'fertility_score': 0.35,
                    'description': 'May affect follicle development'
                }
            },
            'population_frequency': {'A': 0.85, 'G': 0.15},
            'pmid': '19050259'
        },
        # LHCGR - LH/CG receptor
        'rs12470652': {
            'gene': 'LHCGR',
            'name': 'LHCGR ovulation response',
            'variant_name': 'N312S',
            'chromosome': '2',
            'position': 48914232,
            'genotypes': {
                'AA': {
                    'phenotype': 'Normal LH response',
                    'fertility_score': 0.6,
                    'description': 'Typical ovulation trigger response'
                },
                'AG': {
                    'phenotype': 'Intermediate',
                    'fertility_score': 0.5,
                    'description': 'Minor variation in LH response'
                },
                'GG': {
                    'phenotype': 'Altered response',
                    'fertility_score': 0.4,
                    'description': 'May need altered LH trigger protocols'
                }
            },
            'population_frequency': {'A': 0.75, 'G': 0.25},
            'pmid': '18445652'
        },
        # FSHB - FSH beta subunit
        'rs10835638': {
            'gene': 'FSHB',
            'name': 'FSHB production',
            'variant_name': '-211G>T',
            'chromosome': '11',
            'position': 30234145,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal FSH production',
                    'fertility_score': 0.6,
                    'description': 'Typical FSH levels'
                },
                'GT': {
                    'phenotype': 'Lower FSH',
                    'fertility_score': 0.45,
                    'description': 'May have lower FSH'
                },
                'TT': {
                    'phenotype': 'Low FSH',
                    'fertility_score': 0.3,
                    'description': 'Associated with lower FSH levels'
                }
            },
            'population_frequency': {'G': 0.85, 'T': 0.15},
            'pmid': '24664130'
        }
    }
}

# =============================================================================
# MENOPAUSE TIMING GENETICS
# =============================================================================

MENOPAUSE_GENETICS = {
    'name': 'Menopause Timing',
    'description': 'Genetic factors affecting age at menopause',
    'markers': {
        # MCM8 - DNA helicase
        'rs16991615': {
            'gene': 'MCM8',
            'name': 'MCM8 menopause variant',
            'chromosome': '20',
            'position': 5948227,
            'genotypes': {
                'AA': {
                    'phenotype': 'Later menopause tendency',
                    'timing': 'May be 1-2 years later than average',
                    'score': 0.7
                },
                'AG': {
                    'phenotype': 'Average timing',
                    'timing': 'Typical menopause age',
                    'score': 0.5
                },
                'GG': {
                    'phenotype': 'Earlier menopause tendency',
                    'timing': 'May be 1-2 years earlier than average',
                    'score': 0.3
                }
            },
            'population_frequency': {'A': 0.92, 'G': 0.08},
            'pmid': '22267201'
        },
        # BRSK1 - serine/threonine kinase
        'rs1172822': {
            'gene': 'BRSK1',
            'name': 'BRSK1 menopause timing',
            'variant_name': 'Intronic',
            'chromosome': '19',
            'position': 55861843,
            'genotypes': {
                'TT': {
                    'phenotype': 'Later menopause',
                    'timing': 'Associated with later onset',
                    'score': 0.65
                },
                'TC': {
                    'phenotype': 'Average timing',
                    'timing': 'Typical',
                    'score': 0.5
                },
                'CC': {
                    'phenotype': 'Earlier menopause',
                    'timing': 'Associated with earlier onset',
                    'score': 0.35
                }
            },
            'population_frequency': {'T': 0.65, 'C': 0.35},
            'pmid': '22267201'
        },
        # HELB - Helicase B
        'rs12294104': {
            'gene': 'HELB',
            'name': 'HELB menopause variant',
            'variant_name': 'Intronic',
            'chromosome': '12',
            'position': 66590000,
            'genotypes': {
                'CC': {
                    'phenotype': 'Later menopause',
                    'timing': '1-2 years later',
                    'score': 0.7
                },
                'CT': {
                    'phenotype': 'Average timing',
                    'timing': 'Typical',
                    'score': 0.5
                },
                'TT': {
                    'phenotype': 'Earlier menopause',
                    'timing': '1-2 years earlier',
                    'score': 0.3
                }
            },
            'population_frequency': {'C': 0.60, 'T': 0.40},
            'pmid': '26414677'
        },
        # EXO1 - Exonuclease 1
        'rs1776148': {
            'gene': 'EXO1',
            'name': 'EXO1 menopause timing',
            'variant_name': 'M439L',
            'chromosome': '1',
            'position': 241689000,
            'genotypes': {
                'AA': {
                    'phenotype': 'Later menopause tendency',
                    'timing': 'Associated with later onset',
                    'score': 0.65
                },
                'AG': {
                    'phenotype': 'Average timing',
                    'timing': 'Typical',
                    'score': 0.5
                },
                'GG': {
                    'phenotype': 'Earlier menopause tendency',
                    'timing': 'Associated with earlier onset',
                    'score': 0.35
                }
            },
            'population_frequency': {'A': 0.55, 'G': 0.45},
            'pmid': '26414677'
        },
        # UIMC1 - Ubiquitin interaction motif
        'rs365132': {
            'gene': 'UIMC1',
            'name': 'UIMC1 menopause variant',
            'variant_name': 'Intronic',
            'chromosome': '5',
            'position': 176424000,
            'genotypes': {
                'TT': {
                    'phenotype': 'Later menopause',
                    'timing': 'Later reproductive span',
                    'score': 0.65
                },
                'TC': {
                    'phenotype': 'Average',
                    'timing': 'Typical timing',
                    'score': 0.5
                },
                'CC': {
                    'phenotype': 'Earlier menopause',
                    'timing': 'Shorter reproductive span',
                    'score': 0.35
                }
            },
            'population_frequency': {'T': 0.60, 'C': 0.40},
            'pmid': '26414677'
        },
        # ASH2L - Trithorax complex
        'rs4886238': {
            'gene': 'ASH2L',
            'name': 'ASH2L menopause timing',
            'variant_name': 'Intronic',
            'chromosome': '8',
            'position': 37860000,
            'genotypes': {
                'GG': {
                    'phenotype': 'Later menopause',
                    'timing': 'Later onset',
                    'score': 0.65
                },
                'GA': {
                    'phenotype': 'Average',
                    'timing': 'Typical',
                    'score': 0.5
                },
                'AA': {
                    'phenotype': 'Earlier menopause',
                    'timing': 'Earlier onset',
                    'score': 0.35
                }
            },
            'population_frequency': {'G': 0.55, 'A': 0.45},
            'pmid': '26414677'
        },
        # FANCA - Fanconi anemia gene
        'rs2278573': {
            'gene': 'FANCA',
            'name': 'FANCA ovarian aging',
            'variant_name': 'Intronic',
            'chromosome': '16',
            'position': 89800000,
            'genotypes': {
                'CC': {
                    'phenotype': 'Later menopause',
                    'timing': 'Later reproductive aging',
                    'score': 0.65
                },
                'CT': {
                    'phenotype': 'Average',
                    'timing': 'Typical aging',
                    'score': 0.5
                },
                'TT': {
                    'phenotype': 'Earlier menopause',
                    'timing': 'Earlier reproductive aging',
                    'score': 0.35
                }
            },
            'population_frequency': {'C': 0.60, 'T': 0.40},
            'pmid': '26414677'
        }
    }
}

# =============================================================================
# TWIN PROBABILITY GENETICS
# =============================================================================

TWIN_GENETICS = {
    'name': 'Twin Probability',
    'description': 'Genetic factors affecting dizygotic (fraternal) twin probability',
    'markers': {
        # FSHB - FSH beta subunit
        'rs11031006': {
            'gene': 'FSHB',
            'name': 'FSHB twin variant',
            'chromosome': '11',
            'position': 30234435,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal twin probability',
                    'twin_odds': '1x baseline',
                    'score': 0.5
                },
                'GA': {
                    'phenotype': 'Slightly increased',
                    'twin_odds': '1.2x baseline',
                    'score': 0.6
                },
                'AA': {
                    'phenotype': 'Increased twin probability',
                    'twin_odds': '1.5x baseline',
                    'score': 0.75,
                    'description': 'Higher FSH may lead to multiple ovulation'
                }
            },
            'population_frequency': {'G': 0.85, 'A': 0.15},
            'pmid': '26968295'
        },
        # SMAD3 - TGF-beta signaling
        'rs17293443': {
            'gene': 'SMAD3',
            'name': 'SMAD3 twin variant',
            'chromosome': '15',
            'position': 67442596,
            'genotypes': {
                'CC': {
                    'phenotype': 'Normal twin probability',
                    'twin_odds': '1x baseline',
                    'score': 0.5
                },
                'CT': {
                    'phenotype': 'Slightly increased',
                    'twin_odds': '1.15x baseline',
                    'score': 0.55
                },
                'TT': {
                    'phenotype': 'Increased probability',
                    'twin_odds': '1.3x baseline',
                    'score': 0.65
                }
            },
            'population_frequency': {'C': 0.80, 'T': 0.20},
            'pmid': '26968295'
        }
    }
}

# =============================================================================
# ENDOMETRIOSIS RISK GENETICS
# =============================================================================

ENDOMETRIOSIS_GENETICS = {
    'name': 'Endometriosis Risk',
    'description': 'Genetic susceptibility to endometriosis',
    'markers': {
        # WNT4 - developmental gene
        'rs7521902': {
            'gene': 'WNT4',
            'name': 'WNT4 endometriosis variant',
            'chromosome': '1',
            'position': 22463951,
            'genotypes': {
                'CC': {
                    'phenotype': 'Lower endometriosis risk',
                    'risk_score': 0.35,
                    'description': 'Protective variant'
                },
                'CA': {
                    'phenotype': 'Average risk',
                    'risk_score': 0.5,
                    'description': 'Typical risk'
                },
                'AA': {
                    'phenotype': 'Higher endometriosis risk',
                    'risk_score': 0.7,
                    'description': 'Increased susceptibility'
                }
            },
            'population_frequency': {'C': 0.70, 'A': 0.30},
            'pmid': '21151130'
        },
        # GREB1 - estrogen-regulated gene
        'rs13394619': {
            'gene': 'GREB1',
            'name': 'GREB1 endometriosis variant',
            'variant_name': 'Intronic',
            'chromosome': '2',
            'position': 11726517,
            'genotypes': {
                'GG': {
                    'phenotype': 'Lower risk',
                    'risk_score': 0.35,
                    'description': 'Reduced risk'
                },
                'GA': {
                    'phenotype': 'Average risk',
                    'risk_score': 0.5,
                    'description': 'Typical'
                },
                'AA': {
                    'phenotype': 'Higher risk',
                    'risk_score': 0.65,
                    'description': 'Increased susceptibility'
                }
            },
            'population_frequency': {'G': 0.55, 'A': 0.45},
            'pmid': '21151130'
        },
        # IL1A - Interleukin 1 alpha (inflammation)
        'rs6542095': {
            'gene': 'IL1A',
            'name': 'IL1A endometriosis inflammation',
            'variant_name': 'Intronic',
            'chromosome': '2',
            'position': 113531000,
            'genotypes': {
                'CC': {
                    'phenotype': 'Lower risk',
                    'risk_score': 0.35,
                    'description': 'Protective'
                },
                'CT': {
                    'phenotype': 'Average risk',
                    'risk_score': 0.5,
                    'description': 'Typical'
                },
                'TT': {
                    'phenotype': 'Higher risk',
                    'risk_score': 0.7,
                    'description': 'Increased inflammation risk'
                }
            },
            'population_frequency': {'C': 0.60, 'T': 0.40},
            'pmid': '22837949'
        },
        # VEZT - vezatin
        'rs10859871': {
            'gene': 'VEZT',
            'name': 'VEZT endometriosis variant',
            'variant_name': 'Intronic',
            'chromosome': '12',
            'position': 95666000,
            'genotypes': {
                'AA': {
                    'phenotype': 'Lower risk',
                    'risk_score': 0.35,
                    'description': 'Protective'
                },
                'AC': {
                    'phenotype': 'Average risk',
                    'risk_score': 0.5,
                    'description': 'Typical'
                },
                'CC': {
                    'phenotype': 'Higher risk',
                    'risk_score': 0.65,
                    'description': 'Increased susceptibility'
                }
            },
            'population_frequency': {'A': 0.55, 'C': 0.45},
            'pmid': '23472165'
        },
        # ID4 - Inhibitor of DNA binding
        'rs7739264': {
            'gene': 'ID4',
            'name': 'ID4 endometriosis variant',
            'variant_name': 'Intronic',
            'chromosome': '6',
            'position': 19842000,
            'genotypes': {
                'TT': {
                    'phenotype': 'Lower risk',
                    'risk_score': 0.35,
                    'description': 'Protective'
                },
                'TC': {
                    'phenotype': 'Average risk',
                    'risk_score': 0.5,
                    'description': 'Typical'
                },
                'CC': {
                    'phenotype': 'Higher risk',
                    'risk_score': 0.65,
                    'description': 'Increased risk'
                }
            },
            'population_frequency': {'T': 0.60, 'C': 0.40},
            'pmid': '21151130'
        },
        # CDKN2B-AS1 - cyclin dependent kinase
        'rs1333049': {
            'gene': 'CDKN2B-AS1',
            'name': 'CDKN2B-AS1 endometriosis',
            'variant_name': 'Intronic',
            'chromosome': '9',
            'position': 22125503,
            'genotypes': {
                'GG': {
                    'phenotype': 'Lower risk',
                    'risk_score': 0.35,
                    'description': 'Protective'
                },
                'GC': {
                    'phenotype': 'Average risk',
                    'risk_score': 0.5,
                    'description': 'Typical'
                },
                'CC': {
                    'phenotype': 'Higher risk',
                    'risk_score': 0.65,
                    'description': 'Increased susceptibility'
                }
            },
            'population_frequency': {'G': 0.55, 'C': 0.45},
            'pmid': '23472165'
        },
        # FN1 - Fibronectin 1
        'rs1250248': {
            'gene': 'FN1',
            'name': 'FN1 endometriosis variant',
            'variant_name': 'Intronic',
            'chromosome': '2',
            'position': 216235000,
            'genotypes': {
                'AA': {
                    'phenotype': 'Lower risk',
                    'risk_score': 0.35,
                    'description': 'Protective'
                },
                'AG': {
                    'phenotype': 'Average risk',
                    'risk_score': 0.5,
                    'description': 'Typical'
                },
                'GG': {
                    'phenotype': 'Higher risk',
                    'risk_score': 0.65,
                    'description': 'Increased cell adhesion risk'
                }
            },
            'population_frequency': {'A': 0.55, 'G': 0.45},
            'pmid': '23472165'
        },
        # ESR1 - Estrogen receptor
        'rs2234693': {
            'gene': 'ESR1',
            'name': 'ESR1 endometriosis',
            'variant_name': 'PvuII',
            'chromosome': '6',
            'position': 152163335,
            'genotypes': {
                'TT': {
                    'phenotype': 'Higher risk',
                    'risk_score': 0.65,
                    'description': 'Enhanced estrogen response'
                },
                'TC': {
                    'phenotype': 'Average risk',
                    'risk_score': 0.5,
                    'description': 'Typical'
                },
                'CC': {
                    'phenotype': 'Lower risk',
                    'risk_score': 0.4,
                    'description': 'Reduced estrogen response'
                }
            },
            'population_frequency': {'T': 0.45, 'C': 0.55},
            'pmid': '15466653'
        }
    }
}

# =============================================================================
# PCOS RISK GENETICS
# =============================================================================

PCOS_GENETICS = {
    'name': 'PCOS Risk',
    'description': 'Genetic susceptibility to polycystic ovary syndrome',
    'markers': {
        # DENND1A - DENN domain containing 1A
        'rs2479106': {
            'gene': 'DENND1A',
            'name': 'DENND1A PCOS variant',
            'variant_name': 'Intronic',
            'chromosome': '9',
            'position': 126619037,
            'genotypes': {
                'GG': {
                    'phenotype': 'Lower PCOS risk',
                    'risk_score': 0.3,
                    'description': 'Protective variant'
                },
                'GA': {
                    'phenotype': 'Average risk',
                    'risk_score': 0.5,
                    'description': 'Typical risk'
                },
                'AA': {
                    'phenotype': 'Higher PCOS risk',
                    'risk_score': 0.7,
                    'description': 'Increased susceptibility'
                }
            },
            'population_frequency': {'G': 0.65, 'A': 0.35},
            'pmid': '22885998'
        },
        # LHCGR - LH receptor
        'rs13405728': {
            'gene': 'LHCGR',
            'name': 'LHCGR PCOS variant',
            'variant_name': 'Intronic',
            'chromosome': '2',
            'position': 48944533,
            'genotypes': {
                'AA': {
                    'phenotype': 'Lower PCOS risk',
                    'risk_score': 0.35,
                    'description': 'Reduced risk'
                },
                'AG': {
                    'phenotype': 'Average risk',
                    'risk_score': 0.5,
                    'description': 'Typical'
                },
                'GG': {
                    'phenotype': 'Higher PCOS risk',
                    'risk_score': 0.65,
                    'description': 'Increased risk'
                }
            },
            'population_frequency': {'A': 0.55, 'G': 0.45},
            'pmid': '21326195'
        },
        # THADA
        'rs13429458': {
            'gene': 'THADA',
            'name': 'THADA PCOS variant',
            'variant_name': 'Intronic',
            'chromosome': '2',
            'position': 43732823,
            'genotypes': {
                'CC': {
                    'phenotype': 'Lower risk',
                    'risk_score': 0.35,
                    'description': 'Protective'
                },
                'CA': {
                    'phenotype': 'Average risk',
                    'risk_score': 0.5,
                    'description': 'Typical'
                },
                'AA': {
                    'phenotype': 'Higher risk',
                    'risk_score': 0.65,
                    'description': 'Increased risk'
                }
            },
            'population_frequency': {'C': 0.70, 'A': 0.30},
            'pmid': '21326195'
        },
        # RAB5B/SUOX - PCOS susceptibility
        'rs705702': {
            'gene': 'RAB5B',
            'name': 'RAB5B PCOS variant',
            'variant_name': 'Intronic',
            'chromosome': '12',
            'position': 56399597,
            'genotypes': {
                'CC': {
                    'phenotype': 'Lower risk',
                    'risk_score': 0.35,
                    'description': 'Protective'
                },
                'CT': {
                    'phenotype': 'Average risk',
                    'risk_score': 0.5,
                    'description': 'Typical'
                },
                'TT': {
                    'phenotype': 'Higher risk',
                    'risk_score': 0.65,
                    'description': 'Increased PCOS risk'
                }
            },
            'population_frequency': {'C': 0.70, 'T': 0.30},
            'pmid': '23303462'
        },
        # C9orf3/SUMO1P1 - PCOS
        'rs3802457': {
            'gene': 'C9orf3',
            'name': 'C9orf3 PCOS variant',
            'variant_name': 'Intronic',
            'chromosome': '9',
            'position': 97738199,
            'genotypes': {
                'TT': {
                    'phenotype': 'Lower risk',
                    'risk_score': 0.35,
                    'description': 'Protective'
                },
                'TC': {
                    'phenotype': 'Average risk',
                    'risk_score': 0.5,
                    'description': 'Typical'
                },
                'CC': {
                    'phenotype': 'Higher risk',
                    'risk_score': 0.65,
                    'description': 'Increased risk'
                }
            },
            'population_frequency': {'T': 0.65, 'C': 0.35},
            'pmid': '22885998'
        },
        # INSR - Insulin receptor (insulin resistance in PCOS)
        'rs2059807': {
            'gene': 'INSR',
            'name': 'INSR insulin receptor',
            'variant_name': 'Intronic',
            'chromosome': '19',
            'position': 7120845,
            'genotypes': {
                'CC': {
                    'phenotype': 'Normal insulin response',
                    'risk_score': 0.4,
                    'description': 'Typical insulin sensitivity'
                },
                'CT': {
                    'phenotype': 'Slightly altered',
                    'risk_score': 0.5,
                    'description': 'Minor variation'
                },
                'TT': {
                    'phenotype': 'Insulin resistance risk',
                    'risk_score': 0.7,
                    'description': 'Associated with insulin resistance in PCOS'
                }
            },
            'population_frequency': {'C': 0.75, 'T': 0.25},
            'pmid': '19369229'
        },
        # FSHR - FSH receptor (ovarian function in PCOS)
        'rs6166': {
            'gene': 'FSHR',
            'name': 'FSHR PCOS variant',
            'variant_name': 'N680S',
            'chromosome': '2',
            'position': 49189921,
            'genotypes': {
                'AA': {
                    'phenotype': 'Better response',
                    'risk_score': 0.35,
                    'description': 'Better FSH sensitivity'
                },
                'AG': {
                    'phenotype': 'Average',
                    'risk_score': 0.5,
                    'description': 'Typical'
                },
                'GG': {
                    'phenotype': 'Poorer response',
                    'risk_score': 0.6,
                    'description': 'May affect ovulation in PCOS'
                }
            },
            'population_frequency': {'A': 0.45, 'G': 0.55},
            'pmid': '10073974'
        },
        # FBN3 - Fibrillin 3 (androgen excess)
        'rs11031006': {
            'gene': 'FBN3',
            'name': 'FBN3 androgen variant',
            'variant_name': 'Intronic',
            'chromosome': '19',
            'position': 8139089,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal',
                    'risk_score': 0.4,
                    'description': 'Typical androgen levels'
                },
                'GA': {
                    'phenotype': 'Carrier',
                    'risk_score': 0.55,
                    'description': 'May have higher androgens'
                },
                'AA': {
                    'phenotype': 'Androgen excess risk',
                    'risk_score': 0.7,
                    'description': 'Associated with hyperandrogenism'
                }
            },
            'population_frequency': {'G': 0.80, 'A': 0.20},
            'pmid': '18385273'
        },
        # YAP1 - Yes-associated protein 1
        'rs11225154': {
            'gene': 'YAP1',
            'name': 'YAP1 PCOS variant',
            'variant_name': 'Intronic',
            'chromosome': '11',
            'position': 101980321,
            'genotypes': {
                'CC': {
                    'phenotype': 'Lower risk',
                    'risk_score': 0.35,
                    'description': 'Protective'
                },
                'CT': {
                    'phenotype': 'Average',
                    'risk_score': 0.5,
                    'description': 'Typical'
                },
                'TT': {
                    'phenotype': 'Higher risk',
                    'risk_score': 0.65,
                    'description': 'Increased risk'
                }
            },
            'population_frequency': {'C': 0.65, 'T': 0.35},
            'pmid': '22885998'
        },
        # HMGA2 - Metabolism and ovarian function
        'rs2272046': {
            'gene': 'HMGA2',
            'name': 'HMGA2 PCOS/metabolism',
            'variant_name': 'Intronic',
            'chromosome': '12',
            'position': 66220743,
            'genotypes': {
                'AA': {
                    'phenotype': 'Lower risk',
                    'risk_score': 0.35,
                    'description': 'Protective'
                },
                'AC': {
                    'phenotype': 'Average',
                    'risk_score': 0.5,
                    'description': 'Typical'
                },
                'CC': {
                    'phenotype': 'Higher risk',
                    'risk_score': 0.65,
                    'description': 'Associated with PCOS'
                }
            },
            'population_frequency': {'A': 0.75, 'C': 0.25},
            'pmid': '22885998'
        },
        # TOX3 - TOX high mobility group box
        'rs4784165': {
            'gene': 'TOX3',
            'name': 'TOX3 PCOS variant',
            'variant_name': 'Intronic',
            'chromosome': '16',
            'position': 52576624,
            'genotypes': {
                'TT': {
                    'phenotype': 'Lower risk',
                    'risk_score': 0.35,
                    'description': 'Protective'
                },
                'TG': {
                    'phenotype': 'Average',
                    'risk_score': 0.5,
                    'description': 'Typical'
                },
                'GG': {
                    'phenotype': 'Higher risk',
                    'risk_score': 0.65,
                    'description': 'Increased PCOS risk'
                }
            },
            'population_frequency': {'T': 0.70, 'G': 0.30},
            'pmid': '22885998'
        },
        # AR - Androgen receptor
        'rs6152': {
            'gene': 'AR',
            'name': 'AR androgen receptor PCOS',
            'variant_name': 'E211E',
            'chromosome': 'X',
            'position': 67545785,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal androgen response',
                    'risk_score': 0.4,
                    'description': 'Typical testosterone sensitivity'
                },
                'GA': {
                    'phenotype': 'Altered response',
                    'risk_score': 0.55,
                    'description': 'May affect androgen effects'
                },
                'AA': {
                    'phenotype': 'Altered sensitivity',
                    'risk_score': 0.6,
                    'description': 'May worsen PCOS symptoms'
                }
            },
            'population_frequency': {'G': 0.65, 'A': 0.35},
            'pmid': '12414817'
        },
        # CYP19A1 - Aromatase (estrogen synthesis)
        'rs2414096': {
            'gene': 'CYP19A1',
            'name': 'Aromatase PCOS',
            'variant_name': 'Intronic',
            'chromosome': '15',
            'position': 51507621,
            'genotypes': {
                'AA': {
                    'phenotype': 'Normal estrogen synthesis',
                    'risk_score': 0.4,
                    'description': 'Typical aromatase function'
                },
                'AG': {
                    'phenotype': 'Intermediate',
                    'risk_score': 0.5,
                    'description': 'Minor variation'
                },
                'GG': {
                    'phenotype': 'Lower aromatase',
                    'risk_score': 0.65,
                    'description': 'May affect estrogen/androgen balance'
                }
            },
            'population_frequency': {'A': 0.65, 'G': 0.35},
            'pmid': '18445652'
        }
    }
}

# =============================================================================
# TESTOSTERONE LEVELS GENETICS
# =============================================================================

TESTOSTERONE_GENETICS = {
    'name': 'Testosterone Levels',
    'description': 'Genetic factors affecting testosterone',
    'markers': {
        # SHBG - sex hormone binding globulin
        'rs12150660': {
            'gene': 'SHBG',
            'name': 'SHBG testosterone variant',
            'chromosome': '17',
            'position': 7534768,
            'genotypes': {
                'TT': {
                    'phenotype': 'Higher free testosterone',
                    'level': 'Above average',
                    'score': 0.7,
                    'description': 'Lower SHBG = more free testosterone'
                },
                'TG': {
                    'phenotype': 'Normal testosterone',
                    'level': 'Average',
                    'score': 0.5,
                    'description': 'Typical levels'
                },
                'GG': {
                    'phenotype': 'Lower free testosterone',
                    'level': 'Below average',
                    'score': 0.3,
                    'description': 'Higher SHBG = less free testosterone'
                }
            },
            'population_frequency': {'T': 0.55, 'G': 0.45},
            'pmid': '21263103'
        },
        # FAM9B - testosterone regulation
        'rs5934505': {
            'gene': 'FAM9B',
            'name': 'FAM9B testosterone',
            'chromosome': 'X',
            'position': 8963775,
            'genotypes': {
                'TT': {
                    'phenotype': 'Higher testosterone tendency',
                    'score': 0.65
                },
                'TC': {
                    'phenotype': 'Normal',
                    'score': 0.5
                },
                'CC': {
                    'phenotype': 'Lower tendency',
                    'score': 0.35
                }
            },
            'population_frequency': {'T': 0.60, 'C': 0.40},
            'pmid': '21263103'
        },
        # AR - Androgen receptor CAG repeat proxy
        'rs6152': {
            'gene': 'AR',
            'name': 'AR androgen sensitivity',
            'variant_name': 'CAG repeat proxy',
            'chromosome': 'X',
            'position': 67545785,
            'genotypes': {
                'GG': {
                    'phenotype': 'Higher androgen sensitivity',
                    'score': 0.7,
                    'description': 'More responsive to testosterone'
                },
                'GA': {
                    'phenotype': 'Normal sensitivity',
                    'score': 0.5
                },
                'AA': {
                    'phenotype': 'Lower sensitivity',
                    'score': 0.35,
                    'description': 'May need higher testosterone for same effect'
                }
            },
            'population_frequency': {'G': 0.55, 'A': 0.45}
        },
        # CYP17A1 - testosterone synthesis
        'rs743572': {
            'gene': 'CYP17A1',
            'name': 'CYP17A1 testosterone synthesis',
            'variant_name': '-34T>C',
            'chromosome': '10',
            'position': 102834167,
            'genotypes': {
                'AA': {
                    'phenotype': 'Higher testosterone production',
                    'score': 0.7
                },
                'AG': {
                    'phenotype': 'Normal production',
                    'score': 0.5
                },
                'GG': {
                    'phenotype': 'Lower production tendency',
                    'score': 0.35
                }
            },
            'population_frequency': {'A': 0.60, 'G': 0.40}
        },
        # HSD17B3 - testosterone conversion
        'rs2066479': {
            'gene': 'HSD17B3',
            'name': 'HSD17B3 testosterone conversion',
            'chromosome': '9',
            'position': 98972821,
            'genotypes': {
                'CC': {
                    'phenotype': 'Efficient T conversion',
                    'score': 0.65
                },
                'CT': {
                    'phenotype': 'Normal conversion',
                    'score': 0.5
                },
                'TT': {
                    'phenotype': 'Less efficient conversion',
                    'score': 0.35
                }
            },
            'population_frequency': {'C': 0.70, 'T': 0.30}
        },
        # SRD5A2 - DHT conversion
        'rs523349': {
            'gene': 'SRD5A2',
            'name': 'SRD5A2 DHT conversion',
            'variant_name': 'V89L',
            'chromosome': '2',
            'position': 31582798,
            'genotypes': {
                'GG': {
                    'phenotype': 'Higher DHT conversion',
                    'score': 0.7,
                    'description': 'More testosterone converted to DHT'
                },
                'GC': {
                    'phenotype': 'Normal conversion',
                    'score': 0.5
                },
                'CC': {
                    'phenotype': 'Lower DHT conversion',
                    'score': 0.35
                }
            },
            'population_frequency': {'G': 0.65, 'C': 0.35}
        },
        # LHCGR - LH receptor
        'rs2293275': {
            'gene': 'LHCGR',
            'name': 'LHCGR testosterone response',
            'chromosome': '2',
            'position': 48694993,
            'genotypes': {
                'GG': {
                    'phenotype': 'Good LH response',
                    'score': 0.65
                },
                'GA': {
                    'phenotype': 'Normal response',
                    'score': 0.5
                },
                'AA': {
                    'phenotype': 'Reduced LH response',
                    'score': 0.35
                }
            },
            'population_frequency': {'G': 0.60, 'A': 0.40}
        },
        # ESR1 - estrogen receptor alpha (affects T feedback)
        'rs2234693': {
            'gene': 'ESR1',
            'name': 'ESR1 PvuII testosterone feedback',
            'chromosome': '6',
            'position': 151842200,
            'genotypes': {
                'TT': {
                    'phenotype': 'Better T regulation',
                    'score': 0.6
                },
                'TC': {
                    'phenotype': 'Normal regulation',
                    'score': 0.5
                },
                'CC': {
                    'phenotype': 'Variable regulation',
                    'score': 0.4
                }
            },
            'population_frequency': {'T': 0.55, 'C': 0.45}
        },
        # CYP19A1 - aromatase (T to E conversion)
        'rs10046': {
            'gene': 'CYP19A1',
            'name': 'CYP19A1 aromatase',
            'chromosome': '15',
            'position': 51533818,
            'genotypes': {
                'CC': {
                    'phenotype': 'Less T to E conversion',
                    'score': 0.65,
                    'description': 'Preserves more testosterone'
                },
                'CT': {
                    'phenotype': 'Normal conversion',
                    'score': 0.5
                },
                'TT': {
                    'phenotype': 'More T to E conversion',
                    'score': 0.35,
                    'description': 'More estrogen from testosterone'
                }
            },
            'population_frequency': {'C': 0.50, 'T': 0.50}
        },
        # GNRH1 - testosterone regulation
        'rs6185': {
            'gene': 'GNRH1',
            'name': 'GnRH testosterone axis',
            'chromosome': '8',
            'position': 25273185,
            'genotypes': {
                'AA': {
                    'phenotype': 'Strong GnRH signaling',
                    'score': 0.65
                },
                'AG': {
                    'phenotype': 'Normal signaling',
                    'score': 0.5
                },
                'GG': {
                    'phenotype': 'Variable signaling',
                    'score': 0.4
                }
            },
            'population_frequency': {'A': 0.70, 'G': 0.30}
        },
        # KISS1 - kisspeptin (HPG axis)
        'rs5780218': {
            'gene': 'KISS1',
            'name': 'KISS1 HPG axis',
            'chromosome': '1',
            'position': 204182983,
            'genotypes': {
                'CC': {
                    'phenotype': 'Good HPG axis function',
                    'score': 0.6
                },
                'CT': {
                    'phenotype': 'Normal function',
                    'score': 0.5
                },
                'TT': {
                    'phenotype': 'Variable function',
                    'score': 0.4
                }
            },
            'population_frequency': {'C': 0.65, 'T': 0.35}
        }
    }
}

# =============================================================================
# ESTROGEN METABOLISM GENETICS
# =============================================================================

ESTROGEN_GENETICS = {
    'name': 'Estrogen Metabolism',
    'description': 'Genetic factors affecting estrogen processing',
    'markers': {
        # CYP1A1 - estrogen hydroxylation
        'rs1048943': {
            'gene': 'CYP1A1',
            'name': 'CYP1A1 Ile462Val',
            'chromosome': '15',
            'position': 74720951,
            'genotypes': {
                'AA': {
                    'phenotype': 'Normal estrogen metabolism',
                    'metabolism': 'Standard',
                    'score': 0.5
                },
                'AG': {
                    'phenotype': 'Increased metabolism',
                    'metabolism': 'Faster clearance',
                    'score': 0.6
                },
                'GG': {
                    'phenotype': 'High estrogen metabolism',
                    'metabolism': 'Rapid clearance',
                    'score': 0.7,
                    'description': 'May metabolize estrogen faster'
                }
            },
            'population_frequency': {'A': 0.85, 'G': 0.15},
            'pmid': '10072410'
        },
        # COMT - estrogen inactivation
        'rs4680': {
            'gene': 'COMT',
            'name': 'COMT Val158Met',
            'chromosome': '22',
            'position': 19963748,
            'genotypes': {
                'GG': {
                    'phenotype': 'Fast estrogen breakdown',
                    'metabolism': 'Rapid COMT activity',
                    'score': 0.7
                },
                'GA': {
                    'phenotype': 'Intermediate metabolism',
                    'metabolism': 'Normal',
                    'score': 0.5
                },
                'AA': {
                    'phenotype': 'Slow estrogen breakdown',
                    'metabolism': 'Slower clearance',
                    'score': 0.3,
                    'description': 'Estrogen may stay active longer'
                }
            },
            'population_frequency': {'G': 0.50, 'A': 0.50},
            'pmid': '17293723'
        }
    }
}

# =============================================================================
# PREGNANCY COMPLICATIONS GENETICS
# =============================================================================

PREGNANCY_COMPLICATIONS_GENETICS = {
    'name': 'Pregnancy Complications',
    'description': 'Genetic factors affecting pregnancy health',
    'markers': {
        # Factor V Leiden - blood clotting
        'rs6025': {
            'gene': 'F5',
            'name': 'Factor V Leiden',
            'chromosome': '1',
            'position': 169549811,
            'genotypes': {
                'CC': {
                    'phenotype': 'Normal clotting',
                    'risk': 'No increased clot risk',
                    'risk_score': 0.2
                },
                'CT': {
                    'phenotype': 'Factor V Leiden carrier',
                    'risk': 'Increased clot risk in pregnancy',
                    'risk_score': 0.65,
                    'description': 'Higher risk of pregnancy-related blood clots'
                },
                'TT': {
                    'phenotype': 'Homozygous Factor V Leiden',
                    'risk': 'Significantly increased clot risk',
                    'risk_score': 0.9,
                    'description': 'Significantly elevated thrombosis risk'
                }
            },
            'population_frequency': {'C': 0.97, 'T': 0.03},
            'pmid': '7989264'
        },
        # Prothrombin G20210A
        'rs1799963': {
            'gene': 'F2',
            'name': 'Prothrombin G20210A',
            'chromosome': '11',
            'position': 46761055,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal clotting',
                    'risk': 'Baseline risk',
                    'risk_score': 0.2
                },
                'GA': {
                    'phenotype': 'Prothrombin mutation carrier',
                    'risk': 'Increased clot risk',
                    'risk_score': 0.6,
                    'description': 'Elevated pregnancy thrombosis risk'
                },
                'AA': {
                    'phenotype': 'Homozygous mutation',
                    'risk': 'High clot risk',
                    'risk_score': 0.85,
                    'description': 'Significantly elevated risk'
                }
            },
            'population_frequency': {'G': 0.98, 'A': 0.02},
            'pmid': '8533762'
        },
        # MTHFR - neural tube defects
        'rs1801133': {
            'gene': 'MTHFR',
            'name': 'MTHFR C677T (pregnancy)',
            'chromosome': '1',
            'position': 11796321,
            'genotypes': {
                'CC': {
                    'phenotype': 'Normal folate metabolism',
                    'risk': 'Normal NTD risk',
                    'risk_score': 0.2
                },
                'CT': {
                    'phenotype': 'Reduced enzyme',
                    'risk': 'Slightly increased NTD risk',
                    'risk_score': 0.4,
                    'description': 'Take adequate folate before/during pregnancy'
                },
                'TT': {
                    'phenotype': 'Significantly reduced',
                    'risk': 'Higher NTD risk if folate deficient',
                    'risk_score': 0.6,
                    'description': 'Important to supplement with methylfolate'
                }
            },
            'population_frequency': {'C': 0.65, 'T': 0.35},
            'pmid': '9545414'
        }
    }
}


# =============================================================================
# COMPLETE REPRODUCTION GENETICS DATABASE
# =============================================================================

REPRODUCTION_GENETICS_DATABASE = {
    'male_fertility': MALE_FERTILITY_GENETICS,
    'female_fertility': FEMALE_FERTILITY_GENETICS,
    'menopause': MENOPAUSE_GENETICS,
    'twins': TWIN_GENETICS,
    'endometriosis': ENDOMETRIOSIS_GENETICS,
    'pcos': PCOS_GENETICS,
    'testosterone': TESTOSTERONE_GENETICS,
    'estrogen': ESTROGEN_GENETICS,
    'pregnancy_complications': PREGNANCY_COMPLICATIONS_GENETICS
}


# =============================================================================
# ANALYSIS FUNCTIONS
# =============================================================================

def normalize_genotype(genotype: str) -> str:
    """
    Normalize genotype to handle orientation differences.
    DNA files may have 'GA' while database has 'AG'.
    Sort alleles alphabetically for consistent matching.
    """
    if not genotype or len(genotype) != 2:
        return genotype
    return ''.join(sorted(genotype.upper()))


def get_complement(genotype: str) -> str:
    """
    Get complementary strand genotype.
    A <-> T, G <-> C
    """
    if not genotype:
        return genotype
    complement_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(complement_map.get(b, b) for b in genotype.upper())


def get_genotype_match(genotype: str, genotypes_dict: dict) -> tuple:
    """
    Find matching genotype in database, handling:
    - Exact match
    - Reversed orientation (AG vs GA)
    - Complementary strand (TT vs AA, GG vs CC)
    Returns (matched_key, data) or (None, None) if no match.
    """
    if not genotype:
        return None, None

    genotype = genotype.upper()

    # Try exact match first
    if genotype in genotypes_dict:
        return genotype, genotypes_dict[genotype]

    # Try reversed (for cases like CT vs TC)
    reversed_gt = genotype[::-1]
    if reversed_gt in genotypes_dict:
        return reversed_gt, genotypes_dict[reversed_gt]

    # Try complementary strand (TT -> AA, GG -> CC, etc.)
    complement = get_complement(genotype)
    if complement in genotypes_dict:
        return complement, genotypes_dict[complement]

    # Try reversed complement
    reversed_complement = complement[::-1]
    if reversed_complement in genotypes_dict:
        return reversed_complement, genotypes_dict[reversed_complement]

    # Try normalized (sorted alphabetically)
    normalized = normalize_genotype(genotype)
    if normalized in genotypes_dict:
        return normalized, genotypes_dict[normalized]

    # Try normalized complement
    normalized_complement = normalize_genotype(complement)
    if normalized_complement in genotypes_dict:
        return normalized_complement, genotypes_dict[normalized_complement]

    return None, None


def analyze_reproduction_genetics(dna_data: dict) -> dict:
    """
    Comprehensive reproduction genetics analysis

    Args:
        dna_data: Dictionary of rsid -> genotype

    Returns:
        Dictionary with all reproduction trait analysis
    """
    results = {
        'male_fertility': analyze_male_fertility(dna_data),
        'female_fertility': analyze_female_fertility(dna_data),
        'menopause_timing': analyze_menopause(dna_data),
        'twin_probability': analyze_twins(dna_data),
        'endometriosis_risk': analyze_endometriosis(dna_data),
        'pcos_risk': analyze_pcos(dna_data),
        'testosterone': analyze_testosterone(dna_data),
        'estrogen_metabolism': analyze_estrogen(dna_data),
        'pregnancy_risks': analyze_pregnancy_risks(dna_data)
    }

    results['summary'] = generate_reproduction_summary(results)
    results['recommendations'] = generate_reproduction_recommendations(results)

    return results


def analyze_male_fertility(dna_data: dict) -> dict:
    """Analyze male fertility genetics"""
    result = {
        'overall': 'Normal',
        'score': 0.5,
        'markers_found': [],
        'description': ''
    }

    scores = []
    for rsid, marker_data in MALE_FERTILITY_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            matched_key, data = get_genotype_match(genotype, marker_data['genotypes'])
            if data:
                scores.append(data.get('fertility_score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid, 'gene': marker_data['gene'],
                    'genotype': genotype, 'phenotype': data['phenotype']
                })

    if scores:
        avg = sum(scores) / len(scores)
        result['score'] = avg
        if avg >= 0.6:
            result['overall'] = 'Favorable'
            result['description'] = 'Your genetics suggest good male reproductive health markers.'
        elif avg <= 0.4:
            result['overall'] = 'May need attention'
            result['description'] = 'Some genetic factors may affect fertility. Consider consultation if trying to conceive.'
        else:
            result['overall'] = 'Normal'
            result['description'] = 'Your male fertility genetics are typical.'

    return result


def analyze_female_fertility(dna_data: dict) -> dict:
    """Analyze female fertility genetics"""
    result = {
        'overall': 'Normal',
        'score': 0.5,
        'ovarian_response': 'Normal',
        'markers_found': [],
        'description': ''
    }

    scores = []
    for rsid, marker_data in FEMALE_FERTILITY_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            matched_key, data = get_genotype_match(genotype, marker_data['genotypes'])
            if data:
                scores.append(data.get('fertility_score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid, 'gene': marker_data['gene'],
                    'genotype': genotype, 'phenotype': data['phenotype']
                })

    if scores:
        avg = sum(scores) / len(scores)
        result['score'] = avg
        if avg >= 0.6:
            result['overall'] = 'Favorable'
            result['ovarian_response'] = 'Good'
            result['description'] = 'Your genetics suggest good ovarian reserve and response markers.'
        elif avg <= 0.4:
            result['overall'] = 'May benefit from early planning'
            result['ovarian_response'] = 'May be lower'
            result['description'] = 'Consider fertility assessment if planning pregnancy.'
        else:
            result['overall'] = 'Normal'
            result['description'] = 'Your female fertility genetics are typical.'

    return result


def analyze_menopause(dna_data: dict) -> dict:
    """Analyze menopause timing genetics"""
    result = {
        'timing': 'Average',
        'score': 0.5,
        'markers_found': [],
        'description': ''
    }

    scores = []
    for rsid, marker_data in MENOPAUSE_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            matched_key, data = get_genotype_match(genotype, marker_data['genotypes'])
            if data:
                scores.append(data.get('score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid, 'gene': marker_data['gene'],
                    'genotype': genotype, 'phenotype': data['phenotype']
                })

    if scores:
        avg = sum(scores) / len(scores)
        result['score'] = avg
        if avg >= 0.6:
            result['timing'] = 'Later than average'
            result['description'] = 'Your genetics suggest menopause may occur later than average.'
        elif avg <= 0.4:
            result['timing'] = 'Earlier than average'
            result['description'] = 'Your genetics suggest menopause may occur earlier. Consider fertility timeline planning.'
        else:
            result['timing'] = 'Average'
            result['description'] = 'Your menopause timing genetics are typical (average ~51 years).'

    return result


def analyze_twins(dna_data: dict) -> dict:
    """Analyze twin probability genetics"""
    result = {
        'probability': 'Normal',
        'odds_multiplier': '1x',
        'score': 0.5,
        'markers_found': [],
        'description': ''
    }

    scores = []
    for rsid, marker_data in TWIN_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            matched_key, data = get_genotype_match(genotype, marker_data['genotypes'])
            if data:
                scores.append(data.get('score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid, 'gene': marker_data['gene'],
                    'genotype': genotype, 'twin_odds': data.get('twin_odds', '1x')
                })

    if scores:
        avg = sum(scores) / len(scores)
        result['score'] = avg
        if avg >= 0.6:
            result['probability'] = 'Increased'
            result['odds_multiplier'] = '~1.3-1.5x baseline'
            result['description'] = 'You have genetic variants associated with higher fraternal twin probability.'
        else:
            result['probability'] = 'Normal'
            result['odds_multiplier'] = '~1x baseline'
            result['description'] = 'Your twin probability genetics are typical.'

    return result


def analyze_endometriosis(dna_data: dict) -> dict:
    """Analyze endometriosis risk genetics"""
    result = {
        'risk_level': 'Unknown',
        'risk_score': 0.5,
        'markers_found': [],
        'risk_variants_found': 0,
        'description': 'No genetic markers for this condition were found in your DNA file.'
    }

    scores = []
    for rsid, marker_data in ENDOMETRIOSIS_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            matched_key, data = get_genotype_match(genotype, marker_data['genotypes'])
            if data:
                scores.append(data.get('risk_score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid, 'gene': marker_data['gene'],
                    'genotype': genotype, 'phenotype': data['phenotype']
                })

    result['risk_variants_found'] = len(result['markers_found'])

    if scores:
        avg = sum(scores) / len(scores)
        result['risk_score'] = avg
        if avg >= 0.6:
            result['risk_level'] = 'Elevated'
            result['description'] = 'You have genetic variants associated with higher endometriosis risk.'
        elif avg <= 0.4:
            result['risk_level'] = 'Lower'
            result['description'] = 'You have lower genetic risk for endometriosis.'
        else:
            result['risk_level'] = 'Average'
            result['description'] = 'Your endometriosis risk genetics are typical.'

    return result


def analyze_pcos(dna_data: dict) -> dict:
    """Analyze PCOS risk genetics"""
    result = {
        'risk_level': 'Unknown',
        'risk_score': 0.5,
        'markers_found': [],
        'risk_variants_found': 0,
        'description': 'No genetic markers for this condition were found in your DNA file.'
    }

    scores = []
    for rsid, marker_data in PCOS_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            matched_key, data = get_genotype_match(genotype, marker_data['genotypes'])
            if data:
                scores.append(data.get('risk_score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid, 'gene': marker_data['gene'],
                    'genotype': genotype, 'phenotype': data['phenotype']
                })

    result['risk_variants_found'] = len(result['markers_found'])

    if scores:
        avg = sum(scores) / len(scores)
        result['risk_score'] = avg
        if avg >= 0.6:
            result['risk_level'] = 'Elevated'
            result['description'] = 'You have genetic variants associated with higher PCOS risk.'
        elif avg <= 0.4:
            result['risk_level'] = 'Lower'
            result['description'] = 'You have lower genetic risk for PCOS.'
        else:
            result['risk_level'] = 'Average'
            result['description'] = 'Your PCOS risk genetics are typical.'

    return result


def analyze_testosterone(dna_data: dict) -> dict:
    """Analyze testosterone genetics"""
    result = {
        'level_tendency': 'Average',
        'score': 0.5,
        'markers_found': [],
        'description': ''
    }

    scores = []
    for rsid, marker_data in TESTOSTERONE_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            matched_key, data = get_genotype_match(genotype, marker_data['genotypes'])
            if data:
                scores.append(data.get('score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid, 'gene': marker_data['gene'],
                    'genotype': genotype, 'phenotype': data['phenotype']
                })

    if scores:
        avg = sum(scores) / len(scores)
        result['score'] = avg
        if avg >= 0.6:
            result['level_tendency'] = 'Higher'
            result['description'] = 'Your genetics suggest higher free testosterone levels.'
        elif avg <= 0.4:
            result['level_tendency'] = 'Lower'
            result['description'] = 'Your genetics suggest lower free testosterone levels.'
        else:
            result['level_tendency'] = 'Average'
            result['description'] = 'Your testosterone genetics are typical.'

    return result


def analyze_estrogen(dna_data: dict) -> dict:
    """Analyze estrogen metabolism genetics"""
    result = {
        'metabolism': 'Normal',
        'score': 0.5,
        'markers_found': [],
        'description': ''
    }

    scores = []
    for rsid, marker_data in ESTROGEN_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            matched_key, data = get_genotype_match(genotype, marker_data['genotypes'])
            if data:
                scores.append(data.get('score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid, 'gene': marker_data['gene'],
                    'genotype': genotype, 'metabolism': data.get('metabolism', '')
                })

    if scores:
        avg = sum(scores) / len(scores)
        result['score'] = avg
        if avg >= 0.6:
            result['metabolism'] = 'Faster'
            result['description'] = 'You metabolize estrogen more quickly.'
        elif avg <= 0.4:
            result['metabolism'] = 'Slower'
            result['description'] = 'You metabolize estrogen more slowly - may have longer estrogen exposure.'
        else:
            result['metabolism'] = 'Normal'
            result['description'] = 'Your estrogen metabolism is typical.'

    return result


def analyze_pregnancy_risks(dna_data: dict) -> dict:
    """Analyze pregnancy complication risks"""
    result = {
        'clotting_risk': 'Normal',
        'ntd_risk': 'Normal',
        'factor_v_leiden': False,
        'prothrombin_mutation': False,
        'markers_found': [],
        'description': ''
    }

    for rsid, marker_data in PREGNANCY_COMPLICATIONS_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            matched_key, data = get_genotype_match(genotype, marker_data['genotypes'])
            if data:
                result['markers_found'].append({
                    'rsid': rsid, 'gene': marker_data['gene'],
                    'genotype': genotype, 'phenotype': data['phenotype'],
                    'risk': data.get('risk', '')
                })

                # Check for specific mutations
                if marker_data['gene'] == 'F5' and data.get('risk_score', 0) >= 0.5:
                    result['factor_v_leiden'] = True
                    result['clotting_risk'] = 'Elevated'
                if marker_data['gene'] == 'F2' and data.get('risk_score', 0) >= 0.5:
                    result['prothrombin_mutation'] = True
                    result['clotting_risk'] = 'Elevated'
                if marker_data['gene'] == 'MTHFR' and data.get('risk_score', 0) >= 0.5:
                    result['ntd_risk'] = 'Elevated without folate'

    if result['factor_v_leiden'] or result['prothrombin_mutation']:
        result['description'] = 'Important: Clotting risk variants detected. Discuss with doctor before/during pregnancy.'
    elif result['ntd_risk'] != 'Normal':
        result['description'] = 'MTHFR variant detected - ensure adequate folate/methylfolate before and during pregnancy.'
    else:
        result['description'] = 'No major pregnancy risk variants detected.'

    return result


def generate_reproduction_summary(results: dict) -> dict:
    """Generate reproduction summary"""
    summary = {
        'key_findings': [],
        'important_alerts': []
    }

    # Check for important findings
    preg = results.get('pregnancy_risks', {})
    if preg.get('factor_v_leiden'):
        summary['important_alerts'].append('Factor V Leiden mutation - discuss with healthcare provider')
    if preg.get('prothrombin_mutation'):
        summary['important_alerts'].append('Prothrombin mutation - discuss with healthcare provider')

    # Female findings
    female = results.get('female_fertility', {})
    if female.get('score', 0.5) <= 0.4:
        summary['key_findings'].append('Lower ovarian response genetics')

    menopause = results.get('menopause_timing', {})
    if menopause.get('timing') == 'Earlier than average':
        summary['key_findings'].append('Earlier menopause tendency')

    pcos = results.get('pcos_risk', {})
    if pcos.get('risk_level') == 'Elevated':
        summary['key_findings'].append('Elevated PCOS risk')

    endo = results.get('endometriosis_risk', {})
    if endo.get('risk_level') == 'Elevated':
        summary['key_findings'].append('Elevated endometriosis risk')

    twins = results.get('twin_probability', {})
    if twins.get('probability') == 'Increased':
        summary['key_findings'].append('Increased fraternal twin probability')

    return summary


def generate_reproduction_recommendations(results: dict) -> List[str]:
    """Generate reproduction recommendations"""
    recommendations = []

    preg = results.get('pregnancy_risks', {})
    if preg.get('factor_v_leiden') or preg.get('prothrombin_mutation'):
        recommendations.append('Consult a hematologist before pregnancy about blood clot prevention.')

    if preg.get('ntd_risk') != 'Normal':
        recommendations.append('Take methylfolate (active folate) before and during pregnancy.')

    female = results.get('female_fertility', {})
    if female.get('score', 0.5) <= 0.4:
        recommendations.append('Consider early fertility assessment if planning pregnancy.')

    menopause = results.get('menopause_timing', {})
    if menopause.get('timing') == 'Earlier than average':
        recommendations.append('Consider fertility timeline planning - menopause may occur earlier.')

    pcos = results.get('pcos_risk', {})
    if pcos.get('risk_level') == 'Elevated':
        recommendations.append('Monitor for PCOS symptoms and maintain healthy weight.')

    male = results.get('male_fertility', {})
    if male.get('score', 0.5) <= 0.4:
        recommendations.append('Consider semen analysis if trying to conceive.')

    recommendations.append('Maintain a healthy lifestyle to optimize reproductive health.')

    return recommendations
