#!/usr/bin/env python3
"""
Sleep & Circadian Genetics Database
Comprehensive database for sleep-related genetic analysis

Features:
1. Chronotype (morning lark vs night owl) - CLOCK, PER, CRY genes
2. Sleep duration need - ADORA2A, ADA, DRD2
3. Sleep quality - CLOCK, PER3, NPAS2
4. Insomnia susceptibility - MEIS1, BTBD9
5. Deep sleep percentage - SWS-related genes
6. REM sleep patterns - cholinergic genes
7. Sleep latency - adenosine receptors
8. Wake time preference - clock genes
9. Shift work tolerance - melatonin genes
10. Delayed sleep phase syndrome - PER2, CRY1

Data sources:
- GWAS Catalog (sleep-related studies)
- UK Biobank chronotype GWAS
- dbSNP (NCBI)
- Published circadian rhythm research
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
# CHRONOTYPE GENETICS (Morning vs Evening Person)
# =============================================================================

CHRONOTYPE_GENETICS = {
    'name': 'Chronotype',
    'description': 'Morning lark vs night owl preference',
    'markers': {
        # CLOCK gene - circadian locomotor output cycles kaput
        'rs1801260': {
            'gene': 'CLOCK',
            'name': 'CLOCK 3111T>C',
            'chromosome': '4',
            'position': 56286673,
            'genotypes': {
                'TT': {
                    'phenotype': 'Morning person (lark)',
                    'score': 0.8,
                    'description': 'Early chronotype, prefer morning activities',
                    'optimal_bedtime': '9:30-10:30 PM',
                    'optimal_wake': '5:30-6:30 AM'
                },
                'TC': {
                    'phenotype': 'Intermediate chronotype',
                    'score': 0.5,
                    'description': 'Moderate flexibility in sleep timing',
                    'optimal_bedtime': '10:30-11:30 PM',
                    'optimal_wake': '6:30-7:30 AM'
                },
                'CC': {
                    'phenotype': 'Evening person (owl)',
                    'score': 0.2,
                    'description': 'Late chronotype, prefer evening activities',
                    'optimal_bedtime': '11:30 PM-12:30 AM',
                    'optimal_wake': '7:30-8:30 AM'
                }
            },
            'population_frequency': {'T': 0.72, 'C': 0.28},
            'pmid': '9620769'
        },
        # PER2 gene - period circadian regulator 2
        'rs35333999': {
            'gene': 'PER2',
            'name': 'PER2 Ser662Gly',
            'chromosome': '2',
            'position': 238288027,
            'genotypes': {
                'GG': {
                    'phenotype': 'Advanced sleep phase',
                    'score': 0.9,
                    'description': 'Tendency toward early sleep times',
                    'effect': 'Early to bed, early to rise'
                },
                'GA': {
                    'phenotype': 'Normal phase',
                    'score': 0.5,
                    'description': 'Typical circadian timing',
                    'effect': 'Standard sleep-wake cycle'
                },
                'AA': {
                    'phenotype': 'Normal/delayed phase',
                    'score': 0.3,
                    'description': 'May trend toward later sleep',
                    'effect': 'Possible delayed preference'
                }
            },
            'population_frequency': {'G': 0.03, 'A': 0.97},
            'pmid': '11232563'
        },
        # PER3 VNTR proxy - affects sleep timing
        'rs228697': {
            'gene': 'PER3',
            'name': 'PER3 VNTR proxy',
            'chromosome': '1',
            'position': 7827019,
            'genotypes': {
                'CC': {
                    'phenotype': 'Strong morning preference',
                    'score': 0.85,
                    'description': 'Associated with 5-repeat VNTR allele'
                },
                'CG': {
                    'phenotype': 'Moderate chronotype',
                    'score': 0.5,
                    'description': 'Mixed chronotype tendency'
                },
                'GG': {
                    'phenotype': 'Evening preference',
                    'score': 0.2,
                    'description': 'Associated with 4-repeat VNTR allele'
                }
            },
            'population_frequency': {'C': 0.55, 'G': 0.45},
            'pmid': '17517622'
        },
        # CRY1 - cryptochrome 1
        'rs8192440': {
            'gene': 'CRY1',
            'name': 'CRY1 variant',
            'chromosome': '12',
            'position': 107421067,
            'genotypes': {
                'AA': {
                    'phenotype': 'Earlier chronotype',
                    'score': 0.7,
                    'description': 'Shorter circadian period'
                },
                'AG': {
                    'phenotype': 'Normal chronotype',
                    'score': 0.5,
                    'description': 'Typical circadian period'
                },
                'GG': {
                    'phenotype': 'Later chronotype',
                    'score': 0.3,
                    'description': 'Longer circadian period tendency'
                }
            },
            'population_frequency': {'A': 0.65, 'G': 0.35},
            'pmid': '28903088'
        },
        # NPAS2 - neuronal PAS domain protein 2
        'rs2305160': {
            'gene': 'NPAS2',
            'name': 'NPAS2 variant',
            'variant_name': 'Ala394Thr',
            'chromosome': '2',
            'position': 101442578,
            'genotypes': {
                'GG': {
                    'phenotype': 'Morning tendency',
                    'score': 0.7,
                    'description': 'Enhanced morning alertness'
                },
                'GA': {
                    'phenotype': 'Neutral chronotype',
                    'score': 0.5,
                    'description': 'Balanced circadian regulation'
                },
                'AA': {
                    'phenotype': 'Evening tendency',
                    'score': 0.3,
                    'description': 'Evening peak performance'
                }
            },
            'population_frequency': {'G': 0.58, 'A': 0.42},
            'pmid': '15687257'
        },
        # PER1 - Period 1
        'rs2735611': {
            'gene': 'PER1',
            'name': 'PER1 circadian variant',
            'variant_name': 'T2434C',
            'chromosome': '17',
            'position': 8043790,
            'genotypes': {
                'TT': {
                    'phenotype': 'Morning preference',
                    'score': 0.7,
                    'description': 'Earlier wake time tendency'
                },
                'TC': {
                    'phenotype': 'Intermediate',
                    'score': 0.5,
                    'description': 'Average chronotype'
                },
                'CC': {
                    'phenotype': 'Evening preference',
                    'score': 0.3,
                    'description': 'Later sleep tendency'
                }
            },
            'population_frequency': {'T': 0.60, 'C': 0.40},
            'pmid': '12397357'
        },
        # CRY2 - Cryptochrome 2
        'rs2292912': {
            'gene': 'CRY2',
            'name': 'CRY2 circadian',
            'variant_name': 'Intronic G/C',
            'chromosome': '11',
            'position': 45869297,
            'genotypes': {
                'GG': {
                    'phenotype': 'Earlier chronotype',
                    'score': 0.65,
                    'description': 'Morning alertness'
                },
                'GC': {
                    'phenotype': 'Intermediate',
                    'score': 0.5,
                    'description': 'Balanced timing'
                },
                'CC': {
                    'phenotype': 'Later chronotype',
                    'score': 0.35,
                    'description': 'Evening preference'
                }
            },
            'population_frequency': {'G': 0.55, 'C': 0.45},
            'pmid': '23804579'
        },
        # ARNTL/BMAL1 - Core clock gene
        'rs7107287': {
            'gene': 'ARNTL/BMAL1',
            'name': 'BMAL1 circadian',
            'variant_name': 'Intronic A/G',
            'chromosome': '11',
            'position': 13399604,
            'genotypes': {
                'AA': {
                    'phenotype': 'Strong morning type',
                    'score': 0.75,
                    'description': 'Enhanced morning function'
                },
                'AG': {
                    'phenotype': 'Intermediate',
                    'score': 0.5,
                    'description': 'Average chronotype'
                },
                'GG': {
                    'phenotype': 'Evening type',
                    'score': 0.3,
                    'description': 'Later peak performance'
                }
            },
            'population_frequency': {'A': 0.58, 'G': 0.42},
            'pmid': '19114110'
        },
        # TIMELESS
        'rs774045': {
            'gene': 'TIMELESS',
            'name': 'TIMELESS circadian',
            'variant_name': 'Intronic C/T',
            'chromosome': '12',
            'position': 56478519,
            'genotypes': {
                'CC': {
                    'phenotype': 'Morning tendency',
                    'score': 0.65,
                    'description': 'Earlier circadian phase'
                },
                'CT': {
                    'phenotype': 'Intermediate',
                    'score': 0.5,
                    'description': 'Average phase'
                },
                'TT': {
                    'phenotype': 'Evening tendency',
                    'score': 0.35,
                    'description': 'Later circadian phase'
                }
            },
            'population_frequency': {'C': 0.52, 'T': 0.48},
            'pmid': '20937127'
        },
        # RGS16 - Regulator of G-protein signaling
        'rs10157197': {
            'gene': 'RGS16',
            'name': 'RGS16 chronotype',
            'variant_name': 'Intronic T/C',
            'chromosome': '1',
            'position': 182546000,
            'genotypes': {
                'TT': {
                    'phenotype': 'Morning chronotype',
                    'score': 0.7,
                    'description': 'Associated with morningness'
                },
                'TC': {
                    'phenotype': 'Intermediate',
                    'score': 0.5,
                    'description': 'Balanced chronotype'
                },
                'CC': {
                    'phenotype': 'Evening chronotype',
                    'score': 0.3,
                    'description': 'Associated with eveningness'
                }
            },
            'population_frequency': {'T': 0.60, 'C': 0.40},
            'pmid': '29388134'
        },
        # AHR - Aryl hydrocarbon receptor
        'rs1476080': {
            'gene': 'AHR',
            'name': 'AHR chronotype',
            'variant_name': 'Intronic G/A',
            'chromosome': '7',
            'position': 17306715,
            'genotypes': {
                'GG': {
                    'phenotype': 'Morning tendency',
                    'score': 0.65,
                    'description': 'Earlier wake preference'
                },
                'GA': {
                    'phenotype': 'Intermediate',
                    'score': 0.5,
                    'description': 'Average chronotype'
                },
                'AA': {
                    'phenotype': 'Evening tendency',
                    'score': 0.35,
                    'description': 'Later wake preference'
                }
            },
            'population_frequency': {'G': 0.55, 'A': 0.45},
            'pmid': '29388134'
        },
        # FBXL3 - F-box and leucine-rich repeat protein
        'rs9565309': {
            'gene': 'FBXL3',
            'name': 'FBXL3 circadian',
            'variant_name': 'Intronic A/G',
            'chromosome': '13',
            'position': 77606810,
            'genotypes': {
                'AA': {
                    'phenotype': 'Shorter circadian period',
                    'score': 0.7,
                    'description': 'Morning preference'
                },
                'AG': {
                    'phenotype': 'Normal period',
                    'score': 0.5,
                    'description': 'Average timing'
                },
                'GG': {
                    'phenotype': 'Longer circadian period',
                    'score': 0.35,
                    'description': 'Evening preference'
                }
            },
            'population_frequency': {'A': 0.55, 'G': 0.45},
            'pmid': '28903088'
        }
    }
}

# =============================================================================
# SLEEP DURATION NEED GENETICS
# =============================================================================

SLEEP_DURATION_GENETICS = {
    'name': 'Sleep Duration Need',
    'description': 'Genetic factors affecting how much sleep you need',
    'markers': {
        # ADORA2A - adenosine A2a receptor
        'rs5751876': {
            'gene': 'ADORA2A',
            'name': 'ADORA2A 1976T>C',
            'chromosome': '22',
            'position': 24440070,
            'genotypes': {
                'TT': {
                    'phenotype': 'Normal sleep need',
                    'hours_needed': '7-8 hours',
                    'caffeine_sensitivity': 'Normal',
                    'score': 0.5
                },
                'TC': {
                    'phenotype': 'Slightly increased need',
                    'hours_needed': '7.5-8.5 hours',
                    'caffeine_sensitivity': 'Increased',
                    'score': 0.6
                },
                'CC': {
                    'phenotype': 'Increased sleep need',
                    'hours_needed': '8-9 hours',
                    'caffeine_sensitivity': 'High',
                    'score': 0.7
                }
            },
            'population_frequency': {'T': 0.52, 'C': 0.48},
            'pmid': '15700718'
        },
        # ADA - adenosine deaminase
        'rs73598374': {
            'gene': 'ADA',
            'name': 'ADA G22A',
            'chromosome': '20',
            'position': 44619526,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal deep sleep',
                    'hours_needed': '7-8 hours',
                    'slow_wave_sleep': 'Normal',
                    'score': 0.5
                },
                'GA': {
                    'phenotype': 'Enhanced deep sleep',
                    'hours_needed': '6.5-7.5 hours',
                    'slow_wave_sleep': 'Increased',
                    'score': 0.4
                },
                'AA': {
                    'phenotype': 'Efficient sleeper',
                    'hours_needed': '6-7 hours',
                    'slow_wave_sleep': 'High',
                    'score': 0.3
                }
            },
            'population_frequency': {'G': 0.93, 'A': 0.07},
            'pmid': '15700718'
        },
        # DEC2/BHLHE41 - short sleeper gene
        'rs121912617': {
            'gene': 'DEC2',
            'name': 'DEC2 P384R (short sleeper)',
            'chromosome': '12',
            'position': 26219755,
            'genotypes': {
                'CC': {
                    'phenotype': 'Normal sleep need',
                    'hours_needed': '7-8 hours',
                    'short_sleeper': False,
                    'score': 0.5
                },
                'CG': {
                    'phenotype': 'Reduced sleep need',
                    'hours_needed': '5-6 hours',
                    'short_sleeper': True,
                    'score': 0.2,
                    'description': 'Natural short sleeper mutation'
                },
                'GG': {
                    'phenotype': 'Very short sleep need',
                    'hours_needed': '4-5 hours',
                    'short_sleeper': True,
                    'score': 0.1,
                    'description': 'Rare - functions well on minimal sleep'
                }
            },
            'population_frequency': {'C': 0.9999, 'G': 0.0001},
            'pmid': '19679812'
        },
        # ADRB1 - another short sleeper gene
        'rs1805225': {
            'gene': 'ADRB1',
            'name': 'ADRB1 A187V',
            'variant_name': 'A187V',
            'chromosome': '10',
            'position': 114044017,
            'genotypes': {
                'CC': {
                    'phenotype': 'Normal sleep need',
                    'hours_needed': '7-8 hours',
                    'score': 0.5
                },
                'CT': {
                    'phenotype': 'Slightly reduced need',
                    'hours_needed': '6-7 hours',
                    'score': 0.35
                },
                'TT': {
                    'phenotype': 'Short sleep tolerance',
                    'hours_needed': '5-6 hours',
                    'score': 0.2
                }
            },
            'population_frequency': {'C': 0.95, 'T': 0.05},
            'pmid': '31473062'
        },
        # PAX8 - Sleep duration GWAS hit
        'rs1823125': {
            'gene': 'PAX8',
            'name': 'PAX8 sleep duration',
            'variant_name': 'Intergenic G/A',
            'chromosome': '2',
            'position': 113828037,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal sleep need',
                    'hours_needed': '7-8 hours',
                    'score': 0.5
                },
                'GA': {
                    'phenotype': 'Slightly longer need',
                    'hours_needed': '7.5-8.5 hours',
                    'score': 0.6
                },
                'AA': {
                    'phenotype': 'Increased sleep need',
                    'hours_needed': '8-9 hours',
                    'score': 0.7
                }
            },
            'population_frequency': {'G': 0.55, 'A': 0.45},
            'pmid': '27494321'
        },
        # NPSR1 - Neuropeptide S receptor
        'rs324981': {
            'gene': 'NPSR1',
            'name': 'NPSR1 sleep efficiency',
            'variant_name': 'Asn107Ile',
            'chromosome': '7',
            'position': 34875647,
            'genotypes': {
                'AA': {
                    'phenotype': 'Efficient sleeper',
                    'hours_needed': '6.5-7.5 hours',
                    'score': 0.4
                },
                'AT': {
                    'phenotype': 'Intermediate',
                    'hours_needed': '7-8 hours',
                    'score': 0.5
                },
                'TT': {
                    'phenotype': 'Needs more sleep',
                    'hours_needed': '7.5-8.5 hours',
                    'score': 0.6
                }
            },
            'population_frequency': {'A': 0.45, 'T': 0.55},
            'pmid': '20833647'
        },
        # ABCC9 - ATP-binding cassette
        'rs11046205': {
            'gene': 'ABCC9',
            'name': 'ABCC9 sleep duration',
            'variant_name': 'Intronic A/G',
            'chromosome': '12',
            'position': 21975277,
            'genotypes': {
                'AA': {
                    'phenotype': 'Shorter sleep need',
                    'hours_needed': '6.5-7.5 hours',
                    'score': 0.4
                },
                'AG': {
                    'phenotype': 'Normal sleep need',
                    'hours_needed': '7-8 hours',
                    'score': 0.5
                },
                'GG': {
                    'phenotype': 'Longer sleep need',
                    'hours_needed': '8-9 hours',
                    'score': 0.65
                }
            },
            'population_frequency': {'A': 0.60, 'G': 0.40},
            'pmid': '23286790'
        },
        # CLOCK 257T>G
        'rs3749474': {
            'gene': 'CLOCK',
            'name': 'CLOCK sleep duration',
            'variant_name': '257T>G',
            'chromosome': '4',
            'position': 56288145,
            'genotypes': {
                'TT': {
                    'phenotype': 'Normal sleep duration',
                    'hours_needed': '7-8 hours',
                    'score': 0.5
                },
                'TG': {
                    'phenotype': 'Slightly longer need',
                    'hours_needed': '7.5-8.5 hours',
                    'score': 0.55
                },
                'GG': {
                    'phenotype': 'Longer sleep need',
                    'hours_needed': '8+ hours',
                    'score': 0.65
                }
            },
            'population_frequency': {'T': 0.62, 'G': 0.38},
            'pmid': '18997308'
        },
        # GRM3 - Glutamate receptor
        'rs2299225': {
            'gene': 'GRM3',
            'name': 'GRM3 sleep regulation',
            'variant_name': 'Intronic C/T',
            'chromosome': '7',
            'position': 86647632,
            'genotypes': {
                'CC': {
                    'phenotype': 'Efficient sleep',
                    'hours_needed': '6.5-7.5 hours',
                    'score': 0.45
                },
                'CT': {
                    'phenotype': 'Normal need',
                    'hours_needed': '7-8 hours',
                    'score': 0.5
                },
                'TT': {
                    'phenotype': 'Higher sleep need',
                    'hours_needed': '8+ hours',
                    'score': 0.6
                }
            },
            'population_frequency': {'C': 0.55, 'T': 0.45},
            'pmid': '27494321'
        },
        # ATP2B4
        'rs7803505': {
            'gene': 'ATP2B4',
            'name': 'ATP2B4 sleep duration',
            'variant_name': 'Intronic A/G',
            'chromosome': '1',
            'position': 203653597,
            'genotypes': {
                'AA': {
                    'phenotype': 'Normal sleep need',
                    'hours_needed': '7-8 hours',
                    'score': 0.5
                },
                'AG': {
                    'phenotype': 'Slightly longer need',
                    'hours_needed': '7.5-8.5 hours',
                    'score': 0.55
                },
                'GG': {
                    'phenotype': 'Higher sleep need',
                    'hours_needed': '8+ hours',
                    'score': 0.6
                }
            },
            'population_frequency': {'A': 0.58, 'G': 0.42},
            'pmid': '27494321'
        }
    }
}

# =============================================================================
# SLEEP QUALITY GENETICS
# =============================================================================

SLEEP_QUALITY_GENETICS = {
    'name': 'Sleep Quality',
    'description': 'Genetic factors affecting sleep quality and efficiency',
    'markers': {
        # PER3 5/5 VNTR proxy
        'rs228729': {
            'gene': 'PER3',
            'name': 'PER3 sleep quality',
            'chromosome': '1',
            'position': 7843585,
            'genotypes': {
                'AA': {
                    'phenotype': 'Better sleep quality',
                    'quality_score': 0.8,
                    'sleep_efficiency': 'High',
                    'description': 'More consolidated sleep'
                },
                'AG': {
                    'phenotype': 'Normal sleep quality',
                    'quality_score': 0.6,
                    'sleep_efficiency': 'Normal',
                    'description': 'Typical sleep patterns'
                },
                'GG': {
                    'phenotype': 'Variable sleep quality',
                    'quality_score': 0.4,
                    'sleep_efficiency': 'May be reduced',
                    'description': 'More susceptible to disruption'
                }
            },
            'population_frequency': {'A': 0.45, 'G': 0.55},
            'pmid': '19142067'
        },
        # COMT - affects sleep under stress
        'rs4680': {
            'gene': 'COMT',
            'name': 'COMT Val158Met',
            'chromosome': '22',
            'position': 19963748,
            'genotypes': {
                'GG': {
                    'phenotype': 'Val/Val - stress-resilient sleep',
                    'quality_score': 0.7,
                    'stress_impact': 'Low',
                    'description': 'Sleep less affected by stress'
                },
                'GA': {
                    'phenotype': 'Val/Met - intermediate',
                    'quality_score': 0.5,
                    'stress_impact': 'Moderate',
                    'description': 'Moderate stress impact on sleep'
                },
                'AA': {
                    'phenotype': 'Met/Met - stress-sensitive sleep',
                    'quality_score': 0.3,
                    'stress_impact': 'High',
                    'description': 'Sleep more affected by stress'
                }
            },
            'population_frequency': {'G': 0.50, 'A': 0.50},
            'pmid': '17293723'
        },
        # BDNF - brain-derived neurotrophic factor
        'rs6265': {
            'gene': 'BDNF',
            'name': 'BDNF Val66Met',
            'variant_name': 'Val66Met',
            'chromosome': '11',
            'position': 27658369,
            'genotypes': {
                'GG': {
                    'phenotype': 'Val/Val - good sleep architecture',
                    'quality_score': 0.7,
                    'rem_quality': 'Normal',
                    'description': 'Normal sleep-dependent memory consolidation'
                },
                'GA': {
                    'phenotype': 'Val/Met - intermediate',
                    'quality_score': 0.5,
                    'rem_quality': 'May vary',
                    'description': 'Somewhat variable sleep quality'
                },
                'AA': {
                    'phenotype': 'Met/Met - variable sleep',
                    'quality_score': 0.4,
                    'rem_quality': 'May be altered',
                    'description': 'Possible sleep quality variations'
                }
            },
            'population_frequency': {'G': 0.80, 'A': 0.20},
            'pmid': '14976057'
        },
        # ADA - sleep quality/efficiency
        'rs73598374': {
            'gene': 'ADA',
            'name': 'ADA sleep quality',
            'variant_name': 'G22A',
            'chromosome': '20',
            'position': 44619526,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal sleep quality',
                    'quality_score': 0.5,
                    'sleep_efficiency': 'Normal'
                },
                'GA': {
                    'phenotype': 'Enhanced sleep quality',
                    'quality_score': 0.7,
                    'sleep_efficiency': 'High'
                },
                'AA': {
                    'phenotype': 'Excellent sleep efficiency',
                    'quality_score': 0.85,
                    'sleep_efficiency': 'Very high'
                }
            },
            'population_frequency': {'G': 0.93, 'A': 0.07},
            'pmid': '15700718'
        },
        # GABA-A receptor
        'rs4263535': {
            'gene': 'GABRA2',
            'name': 'GABA-A receptor alpha 2',
            'variant_name': 'Intronic T/C',
            'chromosome': '4',
            'position': 46254432,
            'genotypes': {
                'TT': {
                    'phenotype': 'Better sleep quality',
                    'quality_score': 0.7,
                    'description': 'Enhanced GABAergic sleep'
                },
                'TC': {
                    'phenotype': 'Intermediate quality',
                    'quality_score': 0.5,
                    'description': 'Normal GABA signaling'
                },
                'CC': {
                    'phenotype': 'Variable sleep quality',
                    'quality_score': 0.35,
                    'description': 'May have lighter sleep'
                }
            },
            'population_frequency': {'T': 0.55, 'C': 0.45},
            'pmid': '17507597'
        },
        # Adenosine receptor
        'rs2298383': {
            'gene': 'ADORA2A',
            'name': 'ADORA2A sleep quality',
            'variant_name': 'Intronic C/T',
            'chromosome': '22',
            'position': 24442404,
            'genotypes': {
                'CC': {
                    'phenotype': 'Better sleep quality',
                    'quality_score': 0.65,
                    'description': 'Good adenosine signaling'
                },
                'CT': {
                    'phenotype': 'Normal quality',
                    'quality_score': 0.5,
                    'description': 'Typical sleep patterns'
                },
                'TT': {
                    'phenotype': 'Variable quality',
                    'quality_score': 0.4,
                    'description': 'Sleep more affected by adenosine'
                }
            },
            'population_frequency': {'C': 0.52, 'T': 0.48},
            'pmid': '20009010'
        },
        # DRD2 - dopamine receptor
        'rs6277': {
            'gene': 'DRD2',
            'name': 'DRD2 sleep quality',
            'variant_name': 'C957T',
            'chromosome': '11',
            'position': 113283684,
            'genotypes': {
                'CC': {
                    'phenotype': 'Better sleep quality',
                    'quality_score': 0.65,
                    'description': 'Lower reward interference with sleep'
                },
                'CT': {
                    'phenotype': 'Normal quality',
                    'quality_score': 0.5,
                    'description': 'Typical dopamine influence'
                },
                'TT': {
                    'phenotype': 'Variable quality',
                    'quality_score': 0.4,
                    'description': 'Higher dopamine may affect sleep'
                }
            },
            'population_frequency': {'C': 0.55, 'T': 0.45},
            'pmid': '22367966'
        },
        # HTR1A - serotonin 1A
        'rs6295': {
            'gene': 'HTR1A',
            'name': 'HTR1A sleep quality',
            'variant_name': '-1019 C/G',
            'chromosome': '5',
            'position': 63258018,
            'genotypes': {
                'CC': {
                    'phenotype': 'Better sleep quality',
                    'quality_score': 0.7,
                    'description': 'Good serotonin regulation of sleep'
                },
                'CG': {
                    'phenotype': 'Intermediate',
                    'quality_score': 0.5,
                    'description': 'Average serotonin effect'
                },
                'GG': {
                    'phenotype': 'Variable quality',
                    'quality_score': 0.35,
                    'description': 'Sleep may be more variable'
                }
            },
            'population_frequency': {'C': 0.55, 'G': 0.45},
            'pmid': '19758331'
        },
        # IL6 - inflammation affecting sleep
        'rs1800795': {
            'gene': 'IL6',
            'name': 'IL-6 sleep inflammation',
            'variant_name': '-174 G/C',
            'chromosome': '7',
            'position': 22727026,
            'genotypes': {
                'GG': {
                    'phenotype': 'Better sleep quality',
                    'quality_score': 0.65,
                    'description': 'Lower inflammatory impact on sleep'
                },
                'GC': {
                    'phenotype': 'Normal quality',
                    'quality_score': 0.5,
                    'description': 'Moderate inflammation effect'
                },
                'CC': {
                    'phenotype': 'Sleep may be affected',
                    'quality_score': 0.4,
                    'description': 'Higher inflammation may impact sleep'
                }
            },
            'population_frequency': {'G': 0.60, 'C': 0.40},
            'pmid': '17101927'
        },
        # TNF-alpha
        'rs1800629': {
            'gene': 'TNF',
            'name': 'TNF-alpha sleep quality',
            'variant_name': '-308 G/A',
            'chromosome': '6',
            'position': 31575254,
            'genotypes': {
                'GG': {
                    'phenotype': 'Better sleep quality',
                    'quality_score': 0.65,
                    'description': 'Lower cytokine disruption'
                },
                'GA': {
                    'phenotype': 'Intermediate',
                    'quality_score': 0.5,
                    'description': 'Moderate immune impact'
                },
                'AA': {
                    'phenotype': 'Variable sleep quality',
                    'quality_score': 0.35,
                    'description': 'Higher cytokines may affect sleep'
                }
            },
            'population_frequency': {'G': 0.85, 'A': 0.15},
            'pmid': '14559724'
        }
    }
}

# =============================================================================
# INSOMNIA SUSCEPTIBILITY
# =============================================================================

INSOMNIA_GENETICS = {
    'name': 'Insomnia Susceptibility',
    'description': 'Genetic factors affecting insomnia risk',
    'markers': {
        # MEIS1 - restless legs/insomnia
        'rs2300478': {
            'gene': 'MEIS1',
            'name': 'MEIS1 insomnia variant',
            'chromosome': '2',
            'position': 66691049,
            'genotypes': {
                'GG': {
                    'phenotype': 'Lower insomnia risk',
                    'risk_score': 0.3,
                    'description': 'Reduced susceptibility to insomnia'
                },
                'GT': {
                    'phenotype': 'Moderate insomnia risk',
                    'risk_score': 0.5,
                    'description': 'Average insomnia susceptibility'
                },
                'TT': {
                    'phenotype': 'Higher insomnia risk',
                    'risk_score': 0.7,
                    'description': 'Increased insomnia susceptibility'
                }
            },
            'population_frequency': {'G': 0.62, 'T': 0.38},
            'pmid': '29083403'
        },
        # BTBD9 - restless legs/PLM
        'rs3923809': {
            'gene': 'BTBD9',
            'name': 'BTBD9 variant',
            'chromosome': '6',
            'position': 38602890,
            'genotypes': {
                'GG': {
                    'phenotype': 'Higher RLS/PLM risk',
                    'risk_score': 0.7,
                    'description': 'Increased risk of leg movements during sleep',
                    'plm_risk': 'Elevated'
                },
                'GA': {
                    'phenotype': 'Moderate RLS/PLM risk',
                    'risk_score': 0.5,
                    'description': 'Average risk',
                    'plm_risk': 'Normal'
                },
                'AA': {
                    'phenotype': 'Lower RLS/PLM risk',
                    'risk_score': 0.3,
                    'description': 'Reduced risk of leg movements',
                    'plm_risk': 'Low'
                }
            },
            'population_frequency': {'G': 0.25, 'A': 0.75},
            'pmid': '17634447'
        },
        # HTR2A - serotonin receptor
        'rs6313': {
            'gene': 'HTR2A',
            'name': 'HTR2A T102C',
            'chromosome': '13',
            'position': 46897343,
            'genotypes': {
                'CC': {
                    'phenotype': 'Higher insomnia susceptibility',
                    'risk_score': 0.65,
                    'description': 'Altered serotonin signaling affecting sleep'
                },
                'CT': {
                    'phenotype': 'Moderate risk',
                    'risk_score': 0.5,
                    'description': 'Average insomnia risk'
                },
                'TT': {
                    'phenotype': 'Lower insomnia risk',
                    'risk_score': 0.35,
                    'description': 'Better sleep initiation'
                }
            },
            'population_frequency': {'C': 0.42, 'T': 0.58},
            'pmid': '15944144'
        },
        # SLC6A4 - serotonin transporter (5-HTTLPR proxy)
        'rs25531': {
            'gene': 'SLC6A4',
            'name': '5-HTTLPR functional variant',
            'variant_name': 'rs25531 A/G',
            'chromosome': '17',
            'position': 30237328,
            'genotypes': {
                'AA': {
                    'phenotype': 'LA/LA - lower insomnia risk',
                    'risk_score': 0.35,
                    'description': 'Efficient serotonin transport, better sleep'
                },
                'AG': {
                    'phenotype': 'LA/S - moderate risk',
                    'risk_score': 0.5,
                    'description': 'Intermediate serotonin function'
                },
                'GG': {
                    'phenotype': 'S/S - higher stress-related insomnia',
                    'risk_score': 0.7,
                    'description': 'Higher susceptibility to stress-induced sleep problems'
                }
            },
            'population_frequency': {'A': 0.55, 'G': 0.45},
            'pmid': '17568774'
        },
        # FKBP5 - stress and insomnia
        'rs1360780': {
            'gene': 'FKBP5',
            'name': 'FKBP5 stress-insomnia',
            'variant_name': 'Intronic C/T',
            'chromosome': '6',
            'position': 35639794,
            'genotypes': {
                'CC': {
                    'phenotype': 'Lower stress-related insomnia',
                    'risk_score': 0.35,
                    'description': 'Better HPA axis regulation'
                },
                'CT': {
                    'phenotype': 'Moderate risk',
                    'risk_score': 0.5,
                    'description': 'Average stress impact'
                },
                'TT': {
                    'phenotype': 'Higher stress-insomnia',
                    'risk_score': 0.7,
                    'description': 'Stress may significantly impact sleep'
                }
            },
            'population_frequency': {'C': 0.70, 'T': 0.30},
            'pmid': '24608230'
        },
        # GABBR1 - GABA-B receptor
        'rs29230': {
            'gene': 'GABBR1',
            'name': 'GABA-B receptor insomnia',
            'variant_name': 'A/G',
            'chromosome': '6',
            'position': 29553534,
            'genotypes': {
                'AA': {
                    'phenotype': 'Lower insomnia risk',
                    'risk_score': 0.35,
                    'description': 'Good GABAergic sleep promotion'
                },
                'AG': {
                    'phenotype': 'Moderate risk',
                    'risk_score': 0.5,
                    'description': 'Average GABA function'
                },
                'GG': {
                    'phenotype': 'Higher insomnia risk',
                    'risk_score': 0.65,
                    'description': 'May have sleep initiation difficulty'
                }
            },
            'population_frequency': {'A': 0.55, 'G': 0.45},
            'pmid': '20133923'
        },
        # CRHR1 - cortisol/stress
        'rs110402': {
            'gene': 'CRHR1',
            'name': 'CRHR1 stress-insomnia',
            'variant_name': 'Intronic G/A',
            'chromosome': '17',
            'position': 45798367,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal insomnia risk',
                    'risk_score': 0.5,
                    'description': 'Typical stress response'
                },
                'GA': {
                    'phenotype': 'Potentially protective',
                    'risk_score': 0.4,
                    'description': 'May have stress buffering'
                },
                'AA': {
                    'phenotype': 'Protective against stress-insomnia',
                    'risk_score': 0.3,
                    'description': 'Better stress resilience'
                }
            },
            'population_frequency': {'G': 0.60, 'A': 0.40},
            'pmid': '16697422'
        },
        # NPSR1 - neuropeptide S receptor
        'rs324981': {
            'gene': 'NPSR1',
            'name': 'NPSR1 anxiety-insomnia',
            'variant_name': 'Asn107Ile',
            'chromosome': '7',
            'position': 34875647,
            'genotypes': {
                'AA': {
                    'phenotype': 'Lower anxiety-related insomnia',
                    'risk_score': 0.35,
                    'description': 'Better anxiety regulation'
                },
                'AT': {
                    'phenotype': 'Moderate risk',
                    'risk_score': 0.5,
                    'description': 'Average anxiety impact'
                },
                'TT': {
                    'phenotype': 'Higher anxiety-related insomnia',
                    'risk_score': 0.65,
                    'description': 'Anxiety may affect sleep more'
                }
            },
            'population_frequency': {'A': 0.45, 'T': 0.55},
            'pmid': '20833647'
        },
        # CLOCK insomnia
        'rs1801260': {
            'gene': 'CLOCK',
            'name': 'CLOCK insomnia variant',
            'variant_name': '3111T>C',
            'chromosome': '4',
            'position': 56286673,
            'genotypes': {
                'TT': {
                    'phenotype': 'Lower evening insomnia',
                    'risk_score': 0.4,
                    'description': 'Morning type, falls asleep earlier'
                },
                'TC': {
                    'phenotype': 'Moderate risk',
                    'risk_score': 0.5,
                    'description': 'Average sleep timing'
                },
                'CC': {
                    'phenotype': 'Higher evening insomnia',
                    'risk_score': 0.65,
                    'description': 'Night owl, may have trouble sleeping early'
                }
            },
            'population_frequency': {'T': 0.72, 'C': 0.28},
            'pmid': '9620769'
        },
        # MAP2K5 - insomnia GWAS hit
        'rs3784215': {
            'gene': 'MAP2K5',
            'name': 'MAP2K5 insomnia',
            'variant_name': 'Intronic A/G',
            'chromosome': '15',
            'position': 67985887,
            'genotypes': {
                'AA': {
                    'phenotype': 'Lower insomnia risk',
                    'risk_score': 0.35,
                    'description': 'Reduced insomnia susceptibility'
                },
                'AG': {
                    'phenotype': 'Moderate risk',
                    'risk_score': 0.5,
                    'description': 'Average risk'
                },
                'GG': {
                    'phenotype': 'Higher insomnia risk',
                    'risk_score': 0.65,
                    'description': 'Increased susceptibility'
                }
            },
            'population_frequency': {'A': 0.58, 'G': 0.42},
            'pmid': '29083403'
        },
        # CACNA1C - calcium channel
        'rs1006737': {
            'gene': 'CACNA1C',
            'name': 'CACNA1C insomnia',
            'variant_name': 'Intronic A/G',
            'chromosome': '12',
            'position': 2345295,
            'genotypes': {
                'GG': {
                    'phenotype': 'Lower insomnia risk',
                    'risk_score': 0.4,
                    'description': 'Better sleep stability'
                },
                'GA': {
                    'phenotype': 'Moderate risk',
                    'risk_score': 0.5,
                    'description': 'Average sleep regulation'
                },
                'AA': {
                    'phenotype': 'Higher insomnia tendency',
                    'risk_score': 0.65,
                    'description': 'May have more sleep variability'
                }
            },
            'population_frequency': {'G': 0.65, 'A': 0.35},
            'pmid': '23644508'
        }
    }
}

# =============================================================================
# DEEP SLEEP (SLOW-WAVE SLEEP) GENETICS
# =============================================================================

DEEP_SLEEP_GENETICS = {
    'name': 'Deep Sleep (Slow-Wave Sleep)',
    'description': 'Genetic factors affecting deep sleep amount and quality',
    'markers': {
        # ADORA2A - adenosine receptor affects SWS
        'rs5751862': {
            'gene': 'ADORA2A',
            'name': 'ADORA2A SWS variant',
            'chromosome': '22',
            'position': 24426661,
            'genotypes': {
                'AA': {
                    'phenotype': 'Enhanced deep sleep',
                    'sws_percentage': 'Above average (25-30%)',
                    'score': 0.8,
                    'description': 'More time in restorative deep sleep'
                },
                'AG': {
                    'phenotype': 'Normal deep sleep',
                    'sws_percentage': 'Average (20-25%)',
                    'score': 0.5,
                    'description': 'Typical slow-wave sleep amounts'
                },
                'GG': {
                    'phenotype': 'Reduced deep sleep',
                    'sws_percentage': 'Below average (15-20%)',
                    'score': 0.3,
                    'description': 'May have less deep sleep'
                }
            },
            'population_frequency': {'A': 0.58, 'G': 0.42},
            'pmid': '22580231'
        },
        # TNF-alpha - affects SWS
        'rs1800629': {
            'gene': 'TNF',
            'name': 'TNF-308G>A',
            'chromosome': '6',
            'position': 31543031,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal deep sleep',
                    'sws_quality': 'Standard',
                    'score': 0.5
                },
                'GA': {
                    'phenotype': 'Variable deep sleep',
                    'sws_quality': 'May fluctuate',
                    'score': 0.4
                },
                'AA': {
                    'phenotype': 'Reduced deep sleep efficiency',
                    'sws_quality': 'May be fragmented',
                    'score': 0.3
                }
            },
            'population_frequency': {'G': 0.85, 'A': 0.15},
            'pmid': '11525693'
        },
        # IL6 - interleukin 6
        'rs1800795': {
            'gene': 'IL6',
            'name': 'IL6 -174G>C',
            'chromosome': '7',
            'position': 22766645,
            'genotypes': {
                'GG': {
                    'phenotype': 'Good deep sleep recovery',
                    'sws_rebound': 'Strong',
                    'score': 0.7
                },
                'GC': {
                    'phenotype': 'Normal deep sleep',
                    'sws_rebound': 'Normal',
                    'score': 0.5
                },
                'CC': {
                    'phenotype': 'Slower sleep recovery',
                    'sws_rebound': 'May be slower',
                    'score': 0.4
                }
            },
            'population_frequency': {'G': 0.55, 'C': 0.45},
            'pmid': '11567596'
        }
    }
}

# =============================================================================
# REM SLEEP GENETICS
# =============================================================================

REM_SLEEP_GENETICS = {
    'name': 'REM Sleep',
    'description': 'Genetic factors affecting REM sleep patterns',
    'markers': {
        # CHRM3 - cholinergic receptor
        'rs7156974': {
            'gene': 'CHRM3',
            'name': 'CHRM3 REM variant',
            'chromosome': '1',
            'position': 239586871,
            'genotypes': {
                'AA': {
                    'phenotype': 'Enhanced REM sleep',
                    'rem_percentage': 'Above average (25-30%)',
                    'dreaming': 'Vivid dreams common',
                    'score': 0.7
                },
                'AG': {
                    'phenotype': 'Normal REM sleep',
                    'rem_percentage': 'Average (20-25%)',
                    'dreaming': 'Normal dreaming',
                    'score': 0.5
                },
                'GG': {
                    'phenotype': 'Variable REM sleep',
                    'rem_percentage': 'Variable (15-25%)',
                    'dreaming': 'Variable dream recall',
                    'score': 0.4
                }
            },
            'population_frequency': {'A': 0.55, 'G': 0.45},
            'pmid': '24531648'
        },
        # FABP7 - REM sleep and memory
        'rs7411299': {
            'gene': 'FABP7',
            'name': 'FABP7 variant',
            'chromosome': '6',
            'position': 122878567,
            'genotypes': {
                'CC': {
                    'phenotype': 'Enhanced REM quality',
                    'memory_consolidation': 'Efficient',
                    'score': 0.7
                },
                'CT': {
                    'phenotype': 'Normal REM',
                    'memory_consolidation': 'Normal',
                    'score': 0.5
                },
                'TT': {
                    'phenotype': 'Variable REM quality',
                    'memory_consolidation': 'May vary',
                    'score': 0.4
                }
            },
            'population_frequency': {'C': 0.70, 'T': 0.30},
            'pmid': '28011641'
        },
        # CHAT - choline acetyltransferase
        'rs1880676': {
            'gene': 'CHAT',
            'name': 'CHAT REM regulation',
            'chromosome': '10',
            'position': 49615282,
            'genotypes': {
                'GG': {
                    'phenotype': 'Enhanced REM',
                    'dreaming': 'Vivid dreams',
                    'score': 0.7
                },
                'GA': {
                    'phenotype': 'Normal REM',
                    'dreaming': 'Typical dreams',
                    'score': 0.5
                },
                'AA': {
                    'phenotype': 'Variable REM',
                    'dreaming': 'Less dream recall',
                    'score': 0.35
                }
            },
            'population_frequency': {'G': 0.55, 'A': 0.45}
        },
        # SLC5A7 - high affinity choline transporter
        'rs1013940': {
            'gene': 'SLC5A7',
            'name': 'Choline transporter REM',
            'chromosome': '2',
            'position': 108266987,
            'genotypes': {
                'CC': {
                    'phenotype': 'Better REM architecture',
                    'score': 0.65
                },
                'CT': {
                    'phenotype': 'Normal REM',
                    'score': 0.5
                },
                'TT': {
                    'phenotype': 'Variable REM',
                    'score': 0.4
                }
            },
            'population_frequency': {'C': 0.60, 'T': 0.40}
        },
        # ACHE - acetylcholinesterase
        'rs2571598': {
            'gene': 'ACHE',
            'name': 'Acetylcholinesterase REM',
            'chromosome': '7',
            'position': 100486735,
            'genotypes': {
                'AA': {
                    'phenotype': 'More REM sleep',
                    'score': 0.7
                },
                'AG': {
                    'phenotype': 'Normal REM',
                    'score': 0.5
                },
                'GG': {
                    'phenotype': 'Variable REM amount',
                    'score': 0.4
                }
            },
            'population_frequency': {'A': 0.55, 'G': 0.45}
        },
        # CHRM2 - muscarinic receptor
        'rs324650': {
            'gene': 'CHRM2',
            'name': 'CHRM2 REM dreams',
            'chromosome': '7',
            'position': 136559710,
            'genotypes': {
                'TT': {
                    'phenotype': 'Vivid dreaming',
                    'rem_intensity': 'High',
                    'score': 0.7
                },
                'TC': {
                    'phenotype': 'Normal dreaming',
                    'rem_intensity': 'Moderate',
                    'score': 0.5
                },
                'CC': {
                    'phenotype': 'Less dream recall',
                    'rem_intensity': 'Low',
                    'score': 0.35
                }
            },
            'population_frequency': {'T': 0.52, 'C': 0.48}
        },
        # BDNF - memory consolidation during REM
        'rs6265': {
            'gene': 'BDNF',
            'name': 'BDNF REM memory',
            'chromosome': '11',
            'position': 27658369,
            'genotypes': {
                'CC': {
                    'phenotype': 'Val/Val - good REM memory',
                    'memory_effect': 'Enhanced',
                    'score': 0.7
                },
                'CT': {
                    'phenotype': 'Val/Met - intermediate',
                    'memory_effect': 'Normal',
                    'score': 0.5
                },
                'TT': {
                    'phenotype': 'Met/Met - variable REM memory',
                    'memory_effect': 'May vary',
                    'score': 0.4
                }
            },
            'population_frequency': {'C': 0.80, 'T': 0.20}
        },
        # DRD2 - dopamine and REM
        'rs1800497': {
            'gene': 'DRD2',
            'name': 'DRD2 Taq1A REM',
            'chromosome': '11',
            'position': 113400106,
            'genotypes': {
                'CC': {
                    'phenotype': 'Normal REM regulation',
                    'score': 0.55
                },
                'CT': {
                    'phenotype': 'Variable REM',
                    'score': 0.5
                },
                'TT': {
                    'phenotype': 'More REM variability',
                    'score': 0.4
                }
            },
            'population_frequency': {'C': 0.72, 'T': 0.28}
        },
        # HTR2A - serotonin receptor REM
        'rs6313': {
            'gene': 'HTR2A',
            'name': 'HTR2A REM suppression',
            'chromosome': '13',
            'position': 46897343,
            'genotypes': {
                'TT': {
                    'phenotype': 'More REM time',
                    'score': 0.65
                },
                'CT': {
                    'phenotype': 'Normal REM',
                    'score': 0.5
                },
                'CC': {
                    'phenotype': 'Possibly less REM',
                    'score': 0.4
                }
            },
            'population_frequency': {'T': 0.58, 'C': 0.42}
        },
        # COMT - dream content
        'rs4680': {
            'gene': 'COMT',
            'name': 'COMT dream intensity',
            'chromosome': '22',
            'position': 19963748,
            'genotypes': {
                'AA': {
                    'phenotype': 'Met/Met - vivid dreams',
                    'dream_intensity': 'High',
                    'score': 0.7
                },
                'GA': {
                    'phenotype': 'Val/Met - normal dreams',
                    'dream_intensity': 'Moderate',
                    'score': 0.5
                },
                'GG': {
                    'phenotype': 'Val/Val - less vivid',
                    'dream_intensity': 'Lower',
                    'score': 0.4
                }
            },
            'population_frequency': {'A': 0.50, 'G': 0.50}
        },
        # SLC6A3 - dopamine transporter REM
        'rs27072': {
            'gene': 'SLC6A3',
            'name': 'DAT1 REM regulation',
            'chromosome': '5',
            'position': 1393350,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal REM',
                    'score': 0.55
                },
                'GA': {
                    'phenotype': 'Variable REM',
                    'score': 0.5
                },
                'AA': {
                    'phenotype': 'More REM variability',
                    'score': 0.4
                }
            },
            'population_frequency': {'G': 0.58, 'A': 0.42}
        }
    }
}

# =============================================================================
# SLEEP LATENCY (TIME TO FALL ASLEEP)
# =============================================================================

SLEEP_LATENCY_GENETICS = {
    'name': 'Sleep Latency',
    'description': 'Genetic factors affecting how quickly you fall asleep',
    'markers': {
        # GABRA2 - GABA receptor
        'rs279858': {
            'gene': 'GABRA2',
            'name': 'GABRA2 variant',
            'chromosome': '4',
            'position': 46261178,
            'genotypes': {
                'AA': {
                    'phenotype': 'Fast sleep onset',
                    'latency_minutes': '5-10 minutes',
                    'score': 0.8,
                    'description': 'Falls asleep quickly'
                },
                'AG': {
                    'phenotype': 'Normal sleep onset',
                    'latency_minutes': '10-20 minutes',
                    'score': 0.5,
                    'description': 'Average time to fall asleep'
                },
                'GG': {
                    'phenotype': 'Slower sleep onset',
                    'latency_minutes': '20-30+ minutes',
                    'score': 0.3,
                    'description': 'May take longer to fall asleep'
                }
            },
            'population_frequency': {'A': 0.52, 'G': 0.48},
            'pmid': '15564908'
        },
        # GRIA3 - glutamate receptor
        'rs4825476': {
            'gene': 'GRIA3',
            'name': 'GRIA3 variant',
            'chromosome': 'X',
            'position': 122441758,
            'genotypes': {
                'CC': {
                    'phenotype': 'Quick sleep initiation',
                    'effect': 'Enhanced sleep pressure',
                    'score': 0.7
                },
                'CT': {
                    'phenotype': 'Normal initiation',
                    'effect': 'Balanced',
                    'score': 0.5
                },
                'TT': {
                    'phenotype': 'Slower initiation',
                    'effect': 'May need longer wind-down',
                    'score': 0.35
                }
            },
            'population_frequency': {'C': 0.45, 'T': 0.55},
            'pmid': '17634447'
        },
        # ADORA2A - adenosine sleep latency
        'rs5751876': {
            'gene': 'ADORA2A',
            'name': 'ADORA2A sleep initiation',
            'chromosome': '22',
            'position': 24440070,
            'genotypes': {
                'TT': {
                    'phenotype': 'Quick sleep onset',
                    'latency_minutes': '5-15 minutes',
                    'score': 0.7
                },
                'TC': {
                    'phenotype': 'Normal onset',
                    'latency_minutes': '15-25 minutes',
                    'score': 0.5
                },
                'CC': {
                    'phenotype': 'Slower onset',
                    'latency_minutes': '25-40 minutes',
                    'score': 0.35
                }
            },
            'population_frequency': {'T': 0.52, 'C': 0.48}
        },
        # GABRB3 - GABA-B receptor beta 3
        'rs4906902': {
            'gene': 'GABRB3',
            'name': 'GABA-B3 sleep onset',
            'chromosome': '15',
            'position': 27010286,
            'genotypes': {
                'GG': {
                    'phenotype': 'Fast sleep onset',
                    'score': 0.7
                },
                'GA': {
                    'phenotype': 'Normal onset',
                    'score': 0.5
                },
                'AA': {
                    'phenotype': 'Slower onset',
                    'score': 0.35
                }
            },
            'population_frequency': {'G': 0.55, 'A': 0.45}
        },
        # GABRG2 - GABA-A gamma 2
        'rs211014': {
            'gene': 'GABRG2',
            'name': 'GABA-A gamma 2 latency',
            'chromosome': '5',
            'position': 162084507,
            'genotypes': {
                'CC': {
                    'phenotype': 'Better sleep initiation',
                    'score': 0.65
                },
                'CT': {
                    'phenotype': 'Normal initiation',
                    'score': 0.5
                },
                'TT': {
                    'phenotype': 'May take longer',
                    'score': 0.4
                }
            },
            'population_frequency': {'C': 0.58, 'G': 0.42}
        },
        # HTR1A - serotonin 1A sleep onset
        'rs6295': {
            'gene': 'HTR1A',
            'name': 'HTR1A sleep latency',
            'chromosome': '5',
            'position': 63258018,
            'genotypes': {
                'CC': {
                    'phenotype': 'Quick sleep onset',
                    'score': 0.65
                },
                'CG': {
                    'phenotype': 'Normal onset',
                    'score': 0.5
                },
                'GG': {
                    'phenotype': 'May take longer',
                    'score': 0.35
                }
            },
            'population_frequency': {'C': 0.55, 'G': 0.45}
        },
        # BDNF sleep latency
        'rs6265': {
            'gene': 'BDNF',
            'name': 'BDNF sleep initiation',
            'chromosome': '11',
            'position': 27658369,
            'genotypes': {
                'CC': {
                    'phenotype': 'Val/Val - normal onset',
                    'score': 0.55
                },
                'CT': {
                    'phenotype': 'Val/Met - may vary',
                    'score': 0.5
                },
                'TT': {
                    'phenotype': 'Met/Met - may take longer',
                    'score': 0.4
                }
            },
            'population_frequency': {'C': 0.80, 'T': 0.20}
        },
        # COMT sleep latency
        'rs4680': {
            'gene': 'COMT',
            'name': 'COMT sleep onset',
            'chromosome': '22',
            'position': 19963748,
            'genotypes': {
                'GG': {
                    'phenotype': 'Val/Val - quick onset',
                    'score': 0.65
                },
                'GA': {
                    'phenotype': 'Val/Met - normal onset',
                    'score': 0.5
                },
                'AA': {
                    'phenotype': 'Met/Met - may ruminate',
                    'score': 0.4
                }
            },
            'population_frequency': {'G': 0.50, 'A': 0.50}
        },
        # MEIS1 sleep latency
        'rs2300478': {
            'gene': 'MEIS1',
            'name': 'MEIS1 sleep onset',
            'chromosome': '2',
            'position': 66691049,
            'genotypes': {
                'GG': {
                    'phenotype': 'Quick sleep onset',
                    'score': 0.65
                },
                'GT': {
                    'phenotype': 'Normal onset',
                    'score': 0.5
                },
                'TT': {
                    'phenotype': 'May have restlessness',
                    'score': 0.35
                }
            },
            'population_frequency': {'G': 0.62, 'T': 0.38}
        },
        # SLC6A4 sleep latency
        'rs25531': {
            'gene': 'SLC6A4',
            'name': '5-HTTLPR sleep onset',
            'chromosome': '17',
            'position': 30237328,
            'genotypes': {
                'AA': {
                    'phenotype': 'LA/LA - quick onset',
                    'score': 0.65
                },
                'AG': {
                    'phenotype': 'LA/S - normal onset',
                    'score': 0.5
                },
                'GG': {
                    'phenotype': 'S/S - anxiety may delay',
                    'score': 0.35
                }
            },
            'population_frequency': {'A': 0.55, 'G': 0.45}
        }
    }
}

# =============================================================================
# SHIFT WORK TOLERANCE
# =============================================================================

SHIFT_WORK_GENETICS = {
    'name': 'Shift Work Tolerance',
    'description': 'Genetic factors affecting adaptation to irregular schedules',
    'markers': {
        # PER2 - circadian flexibility
        'rs2304672': {
            'gene': 'PER2',
            'name': 'PER2 shift work variant',
            'chromosome': '2',
            'position': 238286940,
            'genotypes': {
                'CC': {
                    'phenotype': 'Poor shift work tolerance',
                    'adaptation': 'Slow to adjust',
                    'score': 0.3,
                    'recommendation': 'Avoid rotating shifts if possible'
                },
                'CG': {
                    'phenotype': 'Moderate tolerance',
                    'adaptation': 'Can adapt with effort',
                    'score': 0.5,
                    'recommendation': 'Allow extra time for schedule changes'
                },
                'GG': {
                    'phenotype': 'Good shift work tolerance',
                    'adaptation': 'Adapts relatively well',
                    'score': 0.7,
                    'recommendation': 'Better equipped for variable schedules'
                }
            },
            'population_frequency': {'C': 0.60, 'G': 0.40},
            'pmid': '17634447'
        },
        # CLOCK flexibility
        'rs11932595': {
            'gene': 'CLOCK',
            'name': 'CLOCK flexibility variant',
            'chromosome': '4',
            'position': 56305756,
            'genotypes': {
                'TT': {
                    'phenotype': 'Flexible circadian rhythm',
                    'jet_lag_recovery': 'Faster',
                    'score': 0.7
                },
                'TC': {
                    'phenotype': 'Moderately flexible',
                    'jet_lag_recovery': 'Average',
                    'score': 0.5
                },
                'CC': {
                    'phenotype': 'Rigid circadian rhythm',
                    'jet_lag_recovery': 'Slower',
                    'score': 0.3
                }
            },
            'population_frequency': {'T': 0.45, 'C': 0.55},
            'pmid': '28903088'
        },
        # Melatonin receptor MTNR1B
        'rs10830963': {
            'gene': 'MTNR1B',
            'name': 'Melatonin receptor variant',
            'chromosome': '11',
            'position': 92708710,
            'genotypes': {
                'CC': {
                    'phenotype': 'Normal melatonin response',
                    'light_sensitivity': 'Standard',
                    'score': 0.6
                },
                'CG': {
                    'phenotype': 'Altered melatonin timing',
                    'light_sensitivity': 'May need more light exposure',
                    'score': 0.4
                },
                'GG': {
                    'phenotype': 'Delayed melatonin release',
                    'light_sensitivity': 'More sensitive to evening light',
                    'score': 0.3
                }
            },
            'population_frequency': {'C': 0.72, 'G': 0.28},
            'pmid': '28903088'
        }
    }
}

# =============================================================================
# DELAYED SLEEP PHASE SYNDROME (DSPS)
# =============================================================================

DSPS_GENETICS = {
    'name': 'Delayed Sleep Phase Syndrome',
    'description': 'Genetic susceptibility to delayed sleep-wake timing',
    'markers': {
        # CRY1 - major DSPS gene
        'rs184039278': {
            'gene': 'CRY1',
            'name': 'CRY1 c.1657+3A>C (DSPS mutation)',
            'chromosome': '12',
            'position': 107461080,
            'genotypes': {
                'AA': {
                    'phenotype': 'Normal sleep timing',
                    'dsps_risk': 'Low',
                    'score': 0.2,
                    'description': 'No DSPS mutation'
                },
                'AC': {
                    'phenotype': 'DSPS carrier',
                    'dsps_risk': 'High',
                    'score': 0.8,
                    'description': 'Delayed Sleep Phase Syndrome mutation carrier'
                },
                'CC': {
                    'phenotype': 'DSPS mutation',
                    'dsps_risk': 'Very high',
                    'score': 0.95,
                    'description': 'Homozygous for DSPS mutation'
                }
            },
            'population_frequency': {'A': 0.995, 'C': 0.005},
            'pmid': '28385956'
        },
        # PER3 VNTR
        'rs57875989': {
            'gene': 'PER3',
            'name': 'PER3 VNTR length',
            'chromosome': '1',
            'position': 7844941,
            'genotypes': {
                'DD': {
                    'phenotype': '4-repeat/4-repeat (delayed tendency)',
                    'dsps_risk': 'Elevated',
                    'score': 0.6,
                    'description': 'Associated with evening preference'
                },
                'DI': {
                    'phenotype': '4-repeat/5-repeat (intermediate)',
                    'dsps_risk': 'Moderate',
                    'score': 0.4,
                    'description': 'Mixed chronotype'
                },
                'II': {
                    'phenotype': '5-repeat/5-repeat (morning tendency)',
                    'dsps_risk': 'Low',
                    'score': 0.2,
                    'description': 'Associated with morning preference'
                }
            },
            'population_frequency': {'D': 0.55, 'I': 0.45},
            'pmid': '17517622'
        }
    }
}

# =============================================================================
# CAFFEINE AND SLEEP GENETICS
# =============================================================================

CAFFEINE_SLEEP_GENETICS = {
    'name': 'Caffeine & Sleep Interaction',
    'description': 'How caffeine affects your sleep based on genetics',
    'markers': {
        # CYP1A2 - caffeine metabolism
        'rs762551': {
            'gene': 'CYP1A2',
            'name': 'CYP1A2*1F',
            'chromosome': '15',
            'position': 74749576,
            'genotypes': {
                'AA': {
                    'phenotype': 'Fast caffeine metabolizer',
                    'caffeine_clearance': 'Rapid',
                    'evening_cutoff': '6-8 PM OK',
                    'score': 0.8,
                    'description': 'Can drink coffee later without sleep disruption'
                },
                'AC': {
                    'phenotype': 'Moderate metabolizer',
                    'caffeine_clearance': 'Average',
                    'evening_cutoff': '2-4 PM recommended',
                    'score': 0.5,
                    'description': 'Should limit late afternoon caffeine'
                },
                'CC': {
                    'phenotype': 'Slow caffeine metabolizer',
                    'caffeine_clearance': 'Slow',
                    'evening_cutoff': 'Noon or earlier',
                    'score': 0.2,
                    'description': 'Caffeine stays in system longer, avoid afternoon coffee'
                }
            },
            'population_frequency': {'A': 0.55, 'C': 0.45},
            'pmid': '16522833'
        },
        # AHR - aryl hydrocarbon receptor
        'rs4410790': {
            'gene': 'AHR',
            'name': 'AHR variant',
            'chromosome': '7',
            'position': 17282645,
            'genotypes': {
                'TT': {
                    'phenotype': 'Lower caffeine sensitivity',
                    'effect': 'Less sleep disruption from caffeine',
                    'score': 0.7
                },
                'TC': {
                    'phenotype': 'Normal caffeine response',
                    'effect': 'Standard sleep impact',
                    'score': 0.5
                },
                'CC': {
                    'phenotype': 'Higher caffeine sensitivity',
                    'effect': 'More sleep disruption from caffeine',
                    'score': 0.3
                }
            },
            'population_frequency': {'T': 0.52, 'C': 0.48},
            'pmid': '23836330'
        }
    }
}


# =============================================================================
# COMPLETE SLEEP GENETICS DATABASE
# =============================================================================

SLEEP_GENETICS_DATABASE = {
    'chronotype': CHRONOTYPE_GENETICS,
    'sleep_duration': SLEEP_DURATION_GENETICS,
    'sleep_quality': SLEEP_QUALITY_GENETICS,
    'insomnia': INSOMNIA_GENETICS,
    'deep_sleep': DEEP_SLEEP_GENETICS,
    'rem_sleep': REM_SLEEP_GENETICS,
    'sleep_latency': SLEEP_LATENCY_GENETICS,
    'shift_work': SHIFT_WORK_GENETICS,
    'dsps': DSPS_GENETICS,
    'caffeine_sleep': CAFFEINE_SLEEP_GENETICS
}


# =============================================================================
# ANALYSIS FUNCTIONS
# =============================================================================

def analyze_sleep_genetics(dna_data: dict) -> dict:
    """
    Comprehensive sleep genetics analysis

    Args:
        dna_data: Dictionary of rsid -> genotype

    Returns:
        Dictionary with all sleep-related trait analysis
    """
    results = {
        'chronotype': analyze_chronotype(dna_data),
        'sleep_duration': analyze_sleep_duration(dna_data),
        'sleep_quality': analyze_sleep_quality(dna_data),
        'insomnia_risk': analyze_insomnia_risk(dna_data),
        'deep_sleep': analyze_deep_sleep(dna_data),
        'rem_sleep': analyze_rem_sleep(dna_data),
        'sleep_latency': analyze_sleep_latency(dna_data),
        'shift_work_tolerance': analyze_shift_work(dna_data),
        'dsps_risk': analyze_dsps(dna_data),
        'caffeine_sleep': analyze_caffeine_sleep(dna_data)
    }

    # Calculate overall sleep profile
    results['overall_profile'] = calculate_sleep_profile(results)
    results['recommendations'] = generate_sleep_recommendations(results)

    return results


def analyze_chronotype(dna_data: dict) -> dict:
    """Analyze chronotype (morning lark vs night owl)"""
    result = {
        'phenotype': 'Intermediate',
        'score': 0.5,
        'markers_found': [],
        'optimal_bedtime': '10:30-11:30 PM',
        'optimal_wake': '6:30-7:30 AM',
        'description': 'Balanced chronotype'
    }

    scores = []

    for rsid, marker_data in CHRONOTYPE_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                scores.append(data.get('score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype'],
                    'description': data.get('description', '')
                })

    if scores:
        avg_score = sum(scores) / len(scores)
        result['score'] = avg_score

        if avg_score >= 0.7:
            result['phenotype'] = 'Strong morning person (lark)'
            result['optimal_bedtime'] = '9:00-10:00 PM'
            result['optimal_wake'] = '5:00-6:00 AM'
            result['description'] = 'You are genetically predisposed to be a morning person. Peak alertness is likely in the early morning hours.'
        elif avg_score >= 0.55:
            result['phenotype'] = 'Moderate morning preference'
            result['optimal_bedtime'] = '10:00-11:00 PM'
            result['optimal_wake'] = '6:00-7:00 AM'
            result['description'] = 'You have a mild morning preference. You likely feel best with a somewhat earlier schedule.'
        elif avg_score >= 0.45:
            result['phenotype'] = 'Intermediate chronotype'
            result['optimal_bedtime'] = '10:30-11:30 PM'
            result['optimal_wake'] = '6:30-7:30 AM'
            result['description'] = 'You have a balanced chronotype with flexibility in your schedule.'
        elif avg_score >= 0.35:
            result['phenotype'] = 'Moderate evening preference'
            result['optimal_bedtime'] = '11:30 PM-12:30 AM'
            result['optimal_wake'] = '7:30-8:30 AM'
            result['description'] = 'You have a mild evening preference. Peak performance may be later in the day.'
        else:
            result['phenotype'] = 'Strong evening person (owl)'
            result['optimal_bedtime'] = '12:00-1:00 AM'
            result['optimal_wake'] = '8:00-9:00 AM'
            result['description'] = 'You are genetically predisposed to be a night owl. Peak alertness is likely in the evening.'

    return result


def analyze_sleep_duration(dna_data: dict) -> dict:
    """Analyze sleep duration needs"""
    result = {
        'hours_needed': '7-8 hours',
        'phenotype': 'Normal sleep need',
        'short_sleeper_variant': False,
        'markers_found': [],
        'score': 0.5
    }

    scores = []

    for rsid, marker_data in SLEEP_DURATION_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                scores.append(data.get('score', 0.5))

                if data.get('short_sleeper', False):
                    result['short_sleeper_variant'] = True

                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype'],
                    'hours_needed': data.get('hours_needed', 'Unknown')
                })

    if scores:
        avg_score = sum(scores) / len(scores)
        result['score'] = avg_score

        if result['short_sleeper_variant']:
            result['phenotype'] = 'Natural short sleeper'
            result['hours_needed'] = '5-6 hours'
            result['description'] = 'You carry a rare variant associated with needing less sleep.'
        elif avg_score <= 0.35:
            result['phenotype'] = 'Lower sleep need'
            result['hours_needed'] = '6-7 hours'
            result['description'] = 'You may function well on slightly less sleep than average.'
        elif avg_score >= 0.65:
            result['phenotype'] = 'Higher sleep need'
            result['hours_needed'] = '8-9 hours'
            result['description'] = 'You may need more sleep than average to feel fully rested.'
        else:
            result['phenotype'] = 'Normal sleep need'
            result['hours_needed'] = '7-8 hours'
            result['description'] = 'You likely need a typical amount of sleep (7-8 hours).'

    return result


def analyze_sleep_quality(dna_data: dict) -> dict:
    """Analyze sleep quality genetics"""
    result = {
        'quality_score': 0.5,
        'phenotype': 'Normal sleep quality',
        'stress_impact': 'Moderate',
        'markers_found': []
    }

    scores = []

    for rsid, marker_data in SLEEP_QUALITY_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                score = data.get('quality_score', 0.5)
                scores.append(score)
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype'],
                    'stress_impact': data.get('stress_impact', 'Unknown')
                })

    if scores:
        avg_score = sum(scores) / len(scores)
        result['quality_score'] = avg_score

        if avg_score >= 0.65:
            result['phenotype'] = 'Good genetic sleep quality'
            result['description'] = 'Your genetics support good sleep quality and resilience to disruption.'
        elif avg_score >= 0.45:
            result['phenotype'] = 'Normal sleep quality'
            result['description'] = 'Your sleep quality genetics are average.'
        else:
            result['phenotype'] = 'Variable sleep quality'
            result['description'] = 'Your genetics may make sleep quality more susceptible to external factors.'

    return result


def analyze_insomnia_risk(dna_data: dict) -> dict:
    """Analyze insomnia susceptibility"""
    result = {
        'risk_score': 0.5,
        'risk_level': 'Average',
        'markers_found': [],
        'rls_plm_risk': 'Normal'
    }

    scores = []

    for rsid, marker_data in INSOMNIA_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                scores.append(data.get('risk_score', 0.5))

                if 'plm_risk' in data:
                    result['rls_plm_risk'] = data['plm_risk']

                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype'],
                    'description': data.get('description', '')
                })

    if scores:
        avg_score = sum(scores) / len(scores)
        result['risk_score'] = avg_score

        if avg_score >= 0.6:
            result['risk_level'] = 'Elevated'
            result['description'] = 'You may be more susceptible to insomnia. Good sleep hygiene is especially important.'
        elif avg_score <= 0.4:
            result['risk_level'] = 'Lower'
            result['description'] = 'Your genetics suggest lower susceptibility to insomnia.'
        else:
            result['risk_level'] = 'Average'
            result['description'] = 'Your insomnia risk is about average.'

    return result


def analyze_deep_sleep(dna_data: dict) -> dict:
    """Analyze deep sleep (slow-wave sleep) genetics"""
    result = {
        'score': 0.5,
        'percentage': 'Average (20-25%)',
        'phenotype': 'Normal deep sleep',
        'markers_found': []
    }

    scores = []

    for rsid, marker_data in DEEP_SLEEP_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                scores.append(data.get('score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype'],
                    'sws_percentage': data.get('sws_percentage', 'Unknown')
                })

    if scores:
        avg_score = sum(scores) / len(scores)
        result['score'] = avg_score

        if avg_score >= 0.65:
            result['phenotype'] = 'Enhanced deep sleep'
            result['percentage'] = 'Above average (25-30%)'
            result['description'] = 'Your genetics support good amounts of restorative deep sleep.'
        elif avg_score <= 0.4:
            result['phenotype'] = 'Reduced deep sleep tendency'
            result['percentage'] = 'Below average (15-20%)'
            result['description'] = 'You may get less deep sleep. Optimize sleep environment and avoid alcohol before bed.'
        else:
            result['phenotype'] = 'Normal deep sleep'
            result['percentage'] = 'Average (20-25%)'
            result['description'] = 'Your deep sleep genetics are typical.'

    return result


def analyze_rem_sleep(dna_data: dict) -> dict:
    """Analyze REM sleep genetics"""
    result = {
        'score': 0.5,
        'percentage': 'Average (20-25%)',
        'phenotype': 'Normal REM sleep',
        'dreaming': 'Normal',
        'markers_found': []
    }

    scores = []

    for rsid, marker_data in REM_SLEEP_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                scores.append(data.get('score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype'],
                    'dreaming': data.get('dreaming', 'Unknown')
                })

    if scores:
        avg_score = sum(scores) / len(scores)
        result['score'] = avg_score

        if avg_score >= 0.6:
            result['phenotype'] = 'Enhanced REM sleep'
            result['percentage'] = 'Above average (25-30%)'
            result['dreaming'] = 'Vivid dreams likely'
            result['description'] = 'You may have more REM sleep and vivid dreams.'
        elif avg_score <= 0.4:
            result['phenotype'] = 'Variable REM sleep'
            result['percentage'] = 'May vary'
            result['dreaming'] = 'Variable dream recall'
            result['description'] = 'Your REM sleep may be more variable.'
        else:
            result['phenotype'] = 'Normal REM sleep'
            result['percentage'] = 'Average (20-25%)'
            result['description'] = 'Your REM sleep genetics are typical.'

    return result


def analyze_sleep_latency(dna_data: dict) -> dict:
    """Analyze sleep latency (time to fall asleep)"""
    result = {
        'score': 0.5,
        'latency_minutes': '10-20 minutes',
        'phenotype': 'Normal sleep onset',
        'markers_found': []
    }

    scores = []

    for rsid, marker_data in SLEEP_LATENCY_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                scores.append(data.get('score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype'],
                    'latency': data.get('latency_minutes', 'Unknown')
                })

    if scores:
        avg_score = sum(scores) / len(scores)
        result['score'] = avg_score

        if avg_score >= 0.65:
            result['phenotype'] = 'Fast sleep onset'
            result['latency_minutes'] = '5-10 minutes'
            result['description'] = 'You likely fall asleep quickly once in bed.'
        elif avg_score <= 0.4:
            result['phenotype'] = 'Slower sleep onset'
            result['latency_minutes'] = '20-30+ minutes'
            result['description'] = 'You may take longer to fall asleep. Consider relaxation techniques.'
        else:
            result['phenotype'] = 'Normal sleep onset'
            result['latency_minutes'] = '10-20 minutes'
            result['description'] = 'Your time to fall asleep is typical.'

    return result


def analyze_shift_work(dna_data: dict) -> dict:
    """Analyze shift work tolerance"""
    result = {
        'score': 0.5,
        'tolerance': 'Moderate',
        'jet_lag_recovery': 'Average',
        'markers_found': []
    }

    scores = []

    for rsid, marker_data in SHIFT_WORK_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                scores.append(data.get('score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype'],
                    'adaptation': data.get('adaptation', 'Unknown')
                })

    if scores:
        avg_score = sum(scores) / len(scores)
        result['score'] = avg_score

        if avg_score >= 0.6:
            result['tolerance'] = 'Good'
            result['jet_lag_recovery'] = 'Faster'
            result['description'] = 'Your circadian system is relatively flexible. You may adapt to schedule changes more easily.'
        elif avg_score <= 0.4:
            result['tolerance'] = 'Poor'
            result['jet_lag_recovery'] = 'Slower'
            result['description'] = 'Your circadian rhythm may be more rigid. Avoid shift work if possible; allow extra recovery time after time zone changes.'
        else:
            result['tolerance'] = 'Moderate'
            result['jet_lag_recovery'] = 'Average'
            result['description'] = 'You have average tolerance for schedule changes.'

    return result


def analyze_dsps(dna_data: dict) -> dict:
    """Analyze Delayed Sleep Phase Syndrome risk"""
    result = {
        'risk_score': 0.2,
        'risk_level': 'Low',
        'dsps_mutation': False,
        'markers_found': []
    }

    scores = []

    for rsid, marker_data in DSPS_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                scores.append(data.get('score', 0.2))

                if data.get('dsps_risk') in ['High', 'Very high']:
                    result['dsps_mutation'] = True

                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype'],
                    'dsps_risk': data.get('dsps_risk', 'Unknown')
                })

    if scores:
        max_score = max(scores)  # DSPS is often dominant
        result['risk_score'] = max_score

        if max_score >= 0.7:
            result['risk_level'] = 'High'
            result['description'] = 'You carry variants associated with Delayed Sleep Phase Syndrome. Consider light therapy and melatonin timing.'
        elif max_score >= 0.5:
            result['risk_level'] = 'Moderate'
            result['description'] = 'You have some genetic tendency toward delayed sleep timing.'
        else:
            result['risk_level'] = 'Low'
            result['description'] = 'You have low genetic risk for DSPS.'

    return result


def analyze_caffeine_sleep(dna_data: dict) -> dict:
    """Analyze caffeine's effect on sleep"""
    result = {
        'metabolism': 'Average',
        'evening_cutoff': '2-4 PM',
        'sensitivity': 'Normal',
        'markers_found': []
    }

    for rsid, marker_data in CAFFEINE_SLEEP_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype'],
                    'clearance': data.get('caffeine_clearance', 'Unknown')
                })

                # CYP1A2 is the main caffeine metabolism gene
                if marker_data['gene'] == 'CYP1A2':
                    result['metabolism'] = data.get('caffeine_clearance', 'Average')
                    result['evening_cutoff'] = data.get('evening_cutoff', '2-4 PM')

                    if 'Fast' in data['phenotype']:
                        result['sensitivity'] = 'Low'
                        result['description'] = 'You metabolize caffeine quickly. Evening coffee is less likely to disrupt your sleep.'
                    elif 'Slow' in data['phenotype']:
                        result['sensitivity'] = 'High'
                        result['description'] = 'You metabolize caffeine slowly. Avoid caffeine after noon to protect your sleep.'
                    else:
                        result['sensitivity'] = 'Normal'
                        result['description'] = 'You have normal caffeine metabolism. Limit caffeine to morning/early afternoon.'

    return result


def calculate_sleep_profile(results: dict) -> dict:
    """Calculate overall sleep profile"""
    profile = {
        'type': 'Balanced',
        'strengths': [],
        'challenges': [],
        'optimal_schedule': {},
        'description': ''
    }

    # Determine chronotype
    chrono = results.get('chronotype', {})
    if chrono.get('score', 0.5) >= 0.65:
        profile['type'] = 'Morning-oriented'
        profile['strengths'].append('Natural early riser')
        profile['optimal_schedule'] = {
            'bedtime': chrono.get('optimal_bedtime', '10:00 PM'),
            'wake_time': chrono.get('optimal_wake', '6:00 AM'),
            'peak_hours': '8 AM - 12 PM'
        }
    elif chrono.get('score', 0.5) <= 0.35:
        profile['type'] = 'Evening-oriented'
        profile['strengths'].append('Natural night owl')
        profile['optimal_schedule'] = {
            'bedtime': chrono.get('optimal_bedtime', '12:00 AM'),
            'wake_time': chrono.get('optimal_wake', '8:00 AM'),
            'peak_hours': '4 PM - 10 PM'
        }
    else:
        profile['type'] = 'Balanced'
        profile['strengths'].append('Flexible schedule adaptation')
        profile['optimal_schedule'] = {
            'bedtime': '10:30-11:30 PM',
            'wake_time': '6:30-7:30 AM',
            'peak_hours': 'Variable'
        }

    # Check sleep duration
    duration = results.get('sleep_duration', {})
    if duration.get('short_sleeper_variant'):
        profile['strengths'].append('Natural short sleeper genetics')

    # Check quality factors
    quality = results.get('sleep_quality', {})
    if quality.get('quality_score', 0.5) >= 0.6:
        profile['strengths'].append('Good sleep quality genetics')
    elif quality.get('quality_score', 0.5) <= 0.4:
        profile['challenges'].append('Sleep quality may need extra attention')

    # Check insomnia risk
    insomnia = results.get('insomnia_risk', {})
    if insomnia.get('risk_level') == 'Elevated':
        profile['challenges'].append('Higher insomnia susceptibility')

    # Check deep sleep
    deep = results.get('deep_sleep', {})
    if deep.get('score', 0.5) >= 0.6:
        profile['strengths'].append('Good deep sleep genetics')
    elif deep.get('score', 0.5) <= 0.4:
        profile['challenges'].append('May need to optimize for deep sleep')

    # Check shift work tolerance
    shift = results.get('shift_work_tolerance', {})
    if shift.get('tolerance') == 'Poor':
        profile['challenges'].append('Low shift work/jet lag tolerance')
    elif shift.get('tolerance') == 'Good':
        profile['strengths'].append('Good schedule flexibility')

    # Check DSPS
    dsps = results.get('dsps_risk', {})
    if dsps.get('risk_level') == 'High':
        profile['challenges'].append('DSPS mutation detected')

    # Check caffeine sensitivity
    caffeine = results.get('caffeine_sleep', {})
    if caffeine.get('sensitivity') == 'High':
        profile['challenges'].append('Caffeine disrupts sleep easily')
    elif caffeine.get('sensitivity') == 'Low':
        profile['strengths'].append('Low caffeine sleep disruption')

    # Generate description
    if len(profile['strengths']) > len(profile['challenges']):
        profile['description'] = 'Your genetics support good sleep overall.'
    elif len(profile['challenges']) > len(profile['strengths']):
        profile['description'] = 'Your genetics suggest paying extra attention to sleep hygiene.'
    else:
        profile['description'] = 'You have a balanced sleep genetic profile.'

    return profile


def generate_sleep_recommendations(results: dict) -> List[str]:
    """Generate personalized sleep recommendations"""
    recommendations = []

    # Chronotype recommendations
    chrono = results.get('chronotype', {})
    if chrono.get('score', 0.5) >= 0.65:
        recommendations.append('As a morning person, schedule important tasks for early in the day when you are most alert.')
    elif chrono.get('score', 0.5) <= 0.35:
        recommendations.append('As an evening person, try to schedule demanding tasks for late afternoon/evening when possible.')

    # Sleep duration
    duration = results.get('sleep_duration', {})
    hours = duration.get('hours_needed', '7-8 hours')
    recommendations.append(f'Aim for {hours} of sleep based on your genetics.')

    # Sleep quality
    quality = results.get('sleep_quality', {})
    if quality.get('quality_score', 0.5) <= 0.45:
        recommendations.append('Prioritize sleep hygiene: dark room, cool temperature, consistent schedule.')

    # Insomnia
    insomnia = results.get('insomnia_risk', {})
    if insomnia.get('risk_level') == 'Elevated':
        recommendations.append('Consider cognitive behavioral therapy for insomnia (CBT-I) if you experience sleep difficulties.')

    # Deep sleep
    deep = results.get('deep_sleep', {})
    if deep.get('score', 0.5) <= 0.45:
        recommendations.append('To maximize deep sleep: avoid alcohol before bed, exercise regularly (but not late), keep bedroom cool.')

    # Sleep latency
    latency = results.get('sleep_latency', {})
    if latency.get('score', 0.5) <= 0.4:
        recommendations.append('Try relaxation techniques before bed: meditation, progressive muscle relaxation, or reading.')

    # Shift work
    shift = results.get('shift_work_tolerance', {})
    if shift.get('tolerance') == 'Poor':
        recommendations.append('Avoid shift work or rotating schedules if possible. Allow extra recovery time after time zone travel.')

    # DSPS
    dsps = results.get('dsps_risk', {})
    if dsps.get('risk_level') == 'High':
        recommendations.append('Consider bright light therapy in the morning and blue light blocking glasses in the evening.')
        recommendations.append('Talk to a sleep specialist about melatonin timing for DSPS management.')

    # Caffeine
    caffeine = results.get('caffeine_sleep', {})
    cutoff = caffeine.get('evening_cutoff', '2-4 PM')
    if caffeine.get('sensitivity') == 'High':
        recommendations.append(f'Stop caffeine consumption by {cutoff} to protect your sleep.')

    return recommendations
