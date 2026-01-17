#!/usr/bin/env python3
"""
Sports & Injury Genetics Database
Comprehensive database for athletic performance and injury risk genetics

Features:
1. Muscle fiber composition (ACTN3 power vs endurance)
2. VO2 max potential (ACE, PPARGC1A)
3. ACL injury susceptibility
4. Tendon/ligament injury risk (COL5A1)
5. Achilles tendinopathy risk
6. Muscle cramping susceptibility
7. Recovery speed from exercise
8. Exercise-induced fatigue
9. Blood pressure response to exercise
10. Lactate clearance

Data sources:
- GWAS Catalog (sports genetics studies)
- dbSNP (NCBI)
- Sports medicine research publications
- Olympic athlete genetic studies
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
# MUSCLE FIBER COMPOSITION (ACTN3)
# =============================================================================

MUSCLE_FIBER_GENETICS = {
    'name': 'Muscle Fiber Composition',
    'description': 'Fast-twitch vs slow-twitch muscle fiber genetics',
    'markers': {
        # ACTN3 R577X - the "speed gene"
        'rs1815739': {
            'gene': 'ACTN3',
            'name': 'ACTN3 R577X (Speed Gene)',
            'chromosome': '11',
            'position': 66328095,
            'genotypes': {
                'CC': {
                    'phenotype': 'Power/Sprint advantage',
                    'fiber_type': 'Fast-twitch dominant',
                    'sports_type': 'Power sports',
                    'score': 0.9,
                    'description': 'Full alpha-actinin-3 expression - sprint/power advantage',
                    'optimal_sports': ['Sprinting', 'Weightlifting', 'Football', 'Basketball']
                },
                'CT': {
                    'phenotype': 'Mixed fiber type',
                    'fiber_type': 'Balanced',
                    'sports_type': 'All-around athlete',
                    'score': 0.5,
                    'description': 'Mixed muscle fiber composition - versatile athlete',
                    'optimal_sports': ['Soccer', 'Tennis', 'Swimming', 'Mixed sports']
                },
                'TT': {
                    'phenotype': 'Endurance advantage',
                    'fiber_type': 'Slow-twitch dominant',
                    'sports_type': 'Endurance sports',
                    'score': 0.2,
                    'description': 'No alpha-actinin-3 - enhanced endurance capacity',
                    'optimal_sports': ['Marathon', 'Cycling', 'Triathlon', 'Cross-country skiing']
                }
            },
            'population_frequency': {'C': 0.57, 'T': 0.43},
            'pmid': '12879365',
            'note': 'Found in nearly all Olympic sprinters (CC genotype)'
        },
        # ACTN2 - related to ACTN3
        'rs4253778': {
            'gene': 'PPARA',
            'name': 'PPARA intron 7',
            'chromosome': '22',
            'position': 46439925,
            'genotypes': {
                'GG': {
                    'phenotype': 'Endurance orientation',
                    'fiber_type': 'Favors endurance',
                    'score': 0.3
                },
                'GC': {
                    'phenotype': 'Mixed',
                    'fiber_type': 'Balanced',
                    'score': 0.5
                },
                'CC': {
                    'phenotype': 'Power orientation',
                    'fiber_type': 'Favors power',
                    'score': 0.7
                }
            },
            'population_frequency': {'G': 0.65, 'C': 0.35},
            'pmid': '18043716'
        }
    }
}

# =============================================================================
# VO2 MAX POTENTIAL
# =============================================================================

VO2MAX_GENETICS = {
    'name': 'VO2 Max Potential',
    'description': 'Genetic factors affecting aerobic capacity',
    'markers': {
        # ACE I/D polymorphism
        'rs4340': {
            'gene': 'ACE',
            'name': 'ACE I/D polymorphism',
            'chromosome': '17',
            'position': 63488529,
            'genotypes': {
                'II': {
                    'phenotype': 'Endurance genotype',
                    'vo2max_potential': 'Higher ceiling',
                    'score': 0.8,
                    'description': 'Associated with higher VO2max trainability',
                    'effect': 'Lower ACE activity, better endurance adaptation'
                },
                'ID': {
                    'phenotype': 'Intermediate',
                    'vo2max_potential': 'Average',
                    'score': 0.5,
                    'description': 'Mixed endurance potential',
                    'effect': 'Balanced ACE activity'
                },
                'DD': {
                    'phenotype': 'Power genotype',
                    'vo2max_potential': 'Lower ceiling',
                    'score': 0.3,
                    'description': 'Better suited for power/strength',
                    'effect': 'Higher ACE activity, strength advantage'
                }
            },
            'population_frequency': {'I': 0.47, 'D': 0.53},
            'pmid': '10694420'
        },
        # PPARGC1A - mitochondrial biogenesis
        'rs8192678': {
            'gene': 'PPARGC1A',
            'name': 'PPARGC1A Gly482Ser',
            'chromosome': '4',
            'position': 23815662,
            'genotypes': {
                'GG': {
                    'phenotype': 'Enhanced mitochondrial function',
                    'vo2max_potential': 'Higher',
                    'score': 0.75,
                    'description': 'Better mitochondrial biogenesis'
                },
                'GA': {
                    'phenotype': 'Normal mitochondrial function',
                    'vo2max_potential': 'Average',
                    'score': 0.5,
                    'description': 'Standard response'
                },
                'AA': {
                    'phenotype': 'Reduced mitochondrial efficiency',
                    'vo2max_potential': 'Lower',
                    'score': 0.3,
                    'description': 'May need more training for same gains'
                }
            },
            'population_frequency': {'G': 0.65, 'A': 0.35},
            'pmid': '15930152'
        },
        # NRF2 - nuclear respiratory factor
        'rs12594956': {
            'gene': 'NRF1',
            'name': 'NRF1 endurance variant',
            'chromosome': '7',
            'position': 129570167,
            'genotypes': {
                'AA': {
                    'phenotype': 'Higher VO2max response',
                    'score': 0.7
                },
                'AC': {
                    'phenotype': 'Average VO2max response',
                    'score': 0.5
                },
                'CC': {
                    'phenotype': 'Lower VO2max response',
                    'score': 0.35
                }
            },
            'population_frequency': {'A': 0.55, 'C': 0.45},
            'pmid': '21925322'
        }
    }
}

# =============================================================================
# ACL INJURY SUSCEPTIBILITY
# =============================================================================

ACL_INJURY_GENETICS = {
    'name': 'ACL Injury Risk',
    'description': 'Genetic susceptibility to ACL tears',
    'markers': {
        # COL1A1 - collagen type I
        'rs1800012': {
            'gene': 'COL1A1',
            'name': 'COL1A1 Sp1',
            'chromosome': '17',
            'position': 50200388,
            'genotypes': {
                'GG': {
                    'phenotype': 'Lower ACL injury risk',
                    'risk_score': 0.3,
                    'description': 'Standard collagen structure'
                },
                'GT': {
                    'phenotype': 'Average ACL risk',
                    'risk_score': 0.5,
                    'description': 'Intermediate risk'
                },
                'TT': {
                    'phenotype': 'Higher ACL injury risk',
                    'risk_score': 0.75,
                    'description': 'Altered collagen may affect ligament strength'
                }
            },
            'population_frequency': {'G': 0.83, 'T': 0.17},
            'pmid': '20233398'
        },
        # COL5A1 - collagen type V
        'rs12722': {
            'gene': 'COL5A1',
            'name': 'COL5A1 BstUI',
            'chromosome': '9',
            'position': 134857927,
            'genotypes': {
                'CC': {
                    'phenotype': 'Lower ligament injury risk',
                    'risk_score': 0.3,
                    'description': 'Protective variant'
                },
                'CT': {
                    'phenotype': 'Average ligament injury risk',
                    'risk_score': 0.5,
                    'description': 'Intermediate'
                },
                'TT': {
                    'phenotype': 'Higher ligament injury risk',
                    'risk_score': 0.7,
                    'description': 'May have weaker connective tissue'
                }
            },
            'population_frequency': {'C': 0.62, 'T': 0.38},
            'pmid': '18508203'
        },
        # GDF5 - growth differentiation factor
        'rs143383': {
            'gene': 'GDF5',
            'name': 'GDF5 +104T/C',
            'chromosome': '20',
            'position': 34022649,
            'genotypes': {
                'TT': {
                    'phenotype': 'Lower ACL risk',
                    'risk_score': 0.35,
                    'description': 'Better joint/ligament development'
                },
                'TC': {
                    'phenotype': 'Average ACL risk',
                    'risk_score': 0.5,
                    'description': 'Intermediate'
                },
                'CC': {
                    'phenotype': 'Higher ACL risk',
                    'risk_score': 0.65,
                    'description': 'Associated with joint problems'
                }
            },
            'population_frequency': {'T': 0.55, 'C': 0.45},
            'pmid': '22406632'
        }
    }
}

# =============================================================================
# TENDON INJURY GENETICS
# =============================================================================

TENDON_INJURY_GENETICS = {
    'name': 'Tendon Injury Risk',
    'description': 'Genetic susceptibility to tendon injuries',
    'markers': {
        # COL5A1 - major tendon gene
        'rs71746744': {
            'gene': 'COL5A1',
            'name': 'COL5A1 3\'-UTR',
            'chromosome': '9',
            'position': 134831604,
            'genotypes': {
                'DD': {
                    'phenotype': 'Lower tendon injury risk',
                    'risk_score': 0.3,
                    'description': 'Protective for tendons'
                },
                'DI': {
                    'phenotype': 'Average tendon risk',
                    'risk_score': 0.5,
                    'description': 'Intermediate'
                },
                'II': {
                    'phenotype': 'Higher tendon injury risk',
                    'risk_score': 0.7,
                    'description': 'More susceptible to tendinopathy'
                }
            },
            'population_frequency': {'D': 0.55, 'I': 0.45},
            'pmid': '20595636'
        },
        # TNC - tenascin C
        'rs13321': {
            'gene': 'TNC',
            'name': 'TNC tendon variant',
            'chromosome': '9',
            'position': 114795893,
            'genotypes': {
                'AA': {
                    'phenotype': 'Lower Achilles risk',
                    'risk_score': 0.35,
                    'description': 'Protective for Achilles tendon'
                },
                'AG': {
                    'phenotype': 'Average Achilles risk',
                    'risk_score': 0.5,
                    'description': 'Intermediate'
                },
                'GG': {
                    'phenotype': 'Higher Achilles risk',
                    'risk_score': 0.7,
                    'description': 'Increased Achilles tendinopathy risk'
                }
            },
            'population_frequency': {'A': 0.70, 'G': 0.30},
            'pmid': '19247379'
        },
        # MMP3 - matrix metalloproteinase
        'rs679620': {
            'gene': 'MMP3',
            'name': 'MMP3 tendon variant',
            'chromosome': '11',
            'position': 102720529,
            'genotypes': {
                'AA': {
                    'phenotype': 'Better tendon repair',
                    'risk_score': 0.35
                },
                'AG': {
                    'phenotype': 'Average repair',
                    'risk_score': 0.5
                },
                'GG': {
                    'phenotype': 'Slower tendon repair',
                    'risk_score': 0.65
                }
            },
            'population_frequency': {'A': 0.45, 'G': 0.55},
            'pmid': '17449995'
        }
    }
}

# =============================================================================
# MUSCLE CRAMPING SUSCEPTIBILITY
# =============================================================================

MUSCLE_CRAMP_GENETICS = {
    'name': 'Muscle Cramping',
    'description': 'Susceptibility to exercise-associated muscle cramps',
    'markers': {
        # COL5A1 also affects cramping
        'rs3196378': {
            'gene': 'COL5A1',
            'name': 'COL5A1 cramp variant',
            'chromosome': '9',
            'position': 134838403,
            'genotypes': {
                'CC': {
                    'phenotype': 'Lower cramping tendency',
                    'risk_score': 0.3,
                    'description': 'Less prone to muscle cramps'
                },
                'CA': {
                    'phenotype': 'Average cramping',
                    'risk_score': 0.5,
                    'description': 'Normal cramping tendency'
                },
                'AA': {
                    'phenotype': 'Higher cramping tendency',
                    'risk_score': 0.7,
                    'description': 'More prone to exercise cramps'
                }
            },
            'population_frequency': {'C': 0.60, 'A': 0.40},
            'pmid': '23143560'
        },
        # Sodium channel gene
        'rs1805124': {
            'gene': 'SCN4A',
            'name': 'SCN4A cramp variant',
            'chromosome': '17',
            'position': 63967680,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal muscle excitability',
                    'risk_score': 0.4,
                    'description': 'Standard sodium channel function'
                },
                'GA': {
                    'phenotype': 'Slightly increased cramps',
                    'risk_score': 0.55,
                    'description': 'May have more cramps'
                },
                'AA': {
                    'phenotype': 'Increased cramping',
                    'risk_score': 0.7,
                    'description': 'Higher muscle excitability'
                }
            },
            'population_frequency': {'G': 0.65, 'A': 0.35},
            'pmid': '17567786'
        }
    }
}

# =============================================================================
# RECOVERY SPEED GENETICS
# =============================================================================

RECOVERY_GENETICS = {
    'name': 'Recovery Speed',
    'description': 'Genetic factors affecting exercise recovery',
    'markers': {
        # IL6 - inflammation
        'rs1800795': {
            'gene': 'IL6',
            'name': 'IL6 -174G>C',
            'chromosome': '7',
            'position': 22766645,
            'genotypes': {
                'GG': {
                    'phenotype': 'Faster recovery',
                    'recovery_score': 0.75,
                    'description': 'Lower inflammatory response, quicker recovery'
                },
                'GC': {
                    'phenotype': 'Normal recovery',
                    'recovery_score': 0.5,
                    'description': 'Average recovery speed'
                },
                'CC': {
                    'phenotype': 'Slower recovery',
                    'recovery_score': 0.3,
                    'description': 'Higher inflammatory response, needs more rest'
                }
            },
            'population_frequency': {'G': 0.55, 'C': 0.45},
            'pmid': '14678764'
        },
        # TNF-alpha - inflammation
        'rs1800629': {
            'gene': 'TNF',
            'name': 'TNF-alpha -308',
            'chromosome': '6',
            'position': 31543031,
            'genotypes': {
                'GG': {
                    'phenotype': 'Normal inflammation',
                    'recovery_score': 0.6,
                    'description': 'Standard recovery'
                },
                'GA': {
                    'phenotype': 'Moderate inflammation',
                    'recovery_score': 0.45,
                    'description': 'Slightly slower recovery'
                },
                'AA': {
                    'phenotype': 'Higher inflammation',
                    'recovery_score': 0.3,
                    'description': 'More muscle soreness, slower recovery'
                }
            },
            'population_frequency': {'G': 0.85, 'A': 0.15},
            'pmid': '18202571'
        },
        # CRP - C-reactive protein
        'rs1205': {
            'gene': 'CRP',
            'name': 'CRP inflammation variant',
            'chromosome': '1',
            'position': 159682233,
            'genotypes': {
                'CC': {
                    'phenotype': 'Lower baseline inflammation',
                    'recovery_score': 0.7,
                    'description': 'Generally faster recovery'
                },
                'CT': {
                    'phenotype': 'Average inflammation',
                    'recovery_score': 0.5,
                    'description': 'Normal recovery'
                },
                'TT': {
                    'phenotype': 'Higher baseline inflammation',
                    'recovery_score': 0.35,
                    'description': 'May need more recovery time'
                }
            },
            'population_frequency': {'C': 0.65, 'T': 0.35},
            'pmid': '16522833'
        }
    }
}

# =============================================================================
# EXERCISE FATIGUE RESISTANCE
# =============================================================================

FATIGUE_GENETICS = {
    'name': 'Fatigue Resistance',
    'description': 'Genetic factors affecting exercise fatigue',
    'markers': {
        # AMPD1 - AMP deaminase
        'rs17602729': {
            'gene': 'AMPD1',
            'name': 'AMPD1 C34T',
            'chromosome': '1',
            'position': 115226994,
            'genotypes': {
                'CC': {
                    'phenotype': 'Normal fatigue resistance',
                    'fatigue_score': 0.6,
                    'description': 'Standard exercise tolerance'
                },
                'CT': {
                    'phenotype': 'Reduced fatigue resistance',
                    'fatigue_score': 0.4,
                    'description': 'May fatigue faster during intense exercise'
                },
                'TT': {
                    'phenotype': 'Low fatigue resistance',
                    'fatigue_score': 0.2,
                    'description': 'Significantly faster fatigue - AMPD deficiency'
                }
            },
            'population_frequency': {'C': 0.88, 'T': 0.12},
            'pmid': '11524437'
        },
        # MCT1 - lactate transport
        'rs1049434': {
            'gene': 'MCT1',
            'name': 'MCT1 A1470T',
            'chromosome': '1',
            'position': 113457160,
            'genotypes': {
                'AA': {
                    'phenotype': 'Better lactate clearance',
                    'fatigue_score': 0.7,
                    'description': 'More efficient lactate transport'
                },
                'AT': {
                    'phenotype': 'Normal lactate clearance',
                    'fatigue_score': 0.5,
                    'description': 'Average lactate handling'
                },
                'TT': {
                    'phenotype': 'Reduced lactate clearance',
                    'fatigue_score': 0.3,
                    'description': 'Lactate builds up faster during exercise'
                }
            },
            'population_frequency': {'A': 0.60, 'T': 0.40},
            'pmid': '24566706'
        }
    }
}

# =============================================================================
# BLOOD PRESSURE RESPONSE TO EXERCISE
# =============================================================================

BP_EXERCISE_GENETICS = {
    'name': 'Blood Pressure Response',
    'description': 'How blood pressure responds to exercise',
    'markers': {
        # AGT - angiotensinogen
        'rs699': {
            'gene': 'AGT',
            'name': 'AGT M235T',
            'chromosome': '1',
            'position': 230845794,
            'genotypes': {
                'CC': {
                    'phenotype': 'Normal BP response',
                    'risk_score': 0.4,
                    'description': 'Standard blood pressure during exercise'
                },
                'CT': {
                    'phenotype': 'Slightly elevated BP response',
                    'risk_score': 0.55,
                    'description': 'Moderate increase with exercise'
                },
                'TT': {
                    'phenotype': 'Higher BP response',
                    'risk_score': 0.7,
                    'description': 'Greater blood pressure increase with exercise'
                }
            },
            'population_frequency': {'C': 0.58, 'T': 0.42},
            'pmid': '12093783'
        },
        # NOS3 - nitric oxide synthase
        'rs1799983': {
            'gene': 'NOS3',
            'name': 'NOS3 Glu298Asp',
            'chromosome': '7',
            'position': 150696111,
            'genotypes': {
                'GG': {
                    'phenotype': 'Better vasodilation',
                    'risk_score': 0.35,
                    'description': 'Efficient nitric oxide production'
                },
                'GT': {
                    'phenotype': 'Normal vasodilation',
                    'risk_score': 0.5,
                    'description': 'Standard response'
                },
                'TT': {
                    'phenotype': 'Reduced vasodilation',
                    'risk_score': 0.65,
                    'description': 'Less efficient blood flow regulation'
                }
            },
            'population_frequency': {'G': 0.65, 'T': 0.35},
            'pmid': '15466653'
        }
    }
}

# =============================================================================
# LACTATE CLEARANCE
# =============================================================================

LACTATE_GENETICS = {
    'name': 'Lactate Clearance',
    'description': 'Genetic factors affecting lactate metabolism',
    'markers': {
        # MCT1 - monocarboxylate transporter
        'rs1049434': {
            'gene': 'MCT1',
            'name': 'MCT1 lactate transporter',
            'chromosome': '1',
            'position': 113457160,
            'genotypes': {
                'AA': {
                    'phenotype': 'Fast lactate clearance',
                    'clearance_score': 0.8,
                    'description': 'Efficient lactate removal - can sustain high intensity'
                },
                'AT': {
                    'phenotype': 'Normal lactate clearance',
                    'clearance_score': 0.5,
                    'description': 'Average lactate metabolism'
                },
                'TT': {
                    'phenotype': 'Slow lactate clearance',
                    'clearance_score': 0.25,
                    'description': 'Lactate accumulates faster - "the burn" hits sooner'
                }
            },
            'population_frequency': {'A': 0.60, 'T': 0.40},
            'pmid': '24566706'
        },
        # LDHA - lactate dehydrogenase
        'rs1049891': {
            'gene': 'LDHA',
            'name': 'LDHA efficiency variant',
            'chromosome': '11',
            'position': 18411266,
            'genotypes': {
                'CC': {
                    'phenotype': 'Efficient lactate conversion',
                    'clearance_score': 0.7,
                    'description': 'Good lactate-to-pyruvate conversion'
                },
                'CT': {
                    'phenotype': 'Normal efficiency',
                    'clearance_score': 0.5,
                    'description': 'Standard'
                },
                'TT': {
                    'phenotype': 'Less efficient',
                    'clearance_score': 0.35,
                    'description': 'May fatigue faster at high intensity'
                }
            },
            'population_frequency': {'C': 0.55, 'T': 0.45},
            'pmid': '18839068'
        }
    }
}


# =============================================================================
# COMPLETE SPORTS GENETICS DATABASE
# =============================================================================

SPORTS_GENETICS_DATABASE = {
    'muscle_fiber': MUSCLE_FIBER_GENETICS,
    'vo2max': VO2MAX_GENETICS,
    'acl_injury': ACL_INJURY_GENETICS,
    'tendon_injury': TENDON_INJURY_GENETICS,
    'muscle_cramp': MUSCLE_CRAMP_GENETICS,
    'recovery': RECOVERY_GENETICS,
    'fatigue': FATIGUE_GENETICS,
    'bp_exercise': BP_EXERCISE_GENETICS,
    'lactate': LACTATE_GENETICS
}


# =============================================================================
# ANALYSIS FUNCTIONS
# =============================================================================

def analyze_sports_genetics(dna_data: dict) -> dict:
    """
    Comprehensive sports genetics analysis

    Args:
        dna_data: Dictionary of rsid -> genotype

    Returns:
        Dictionary with all sports/injury trait analysis
    """
    results = {
        'muscle_fiber': analyze_muscle_fiber(dna_data),
        'vo2max': analyze_vo2max(dna_data),
        'acl_injury': analyze_acl_risk(dna_data),
        'tendon_injury': analyze_tendon_risk(dna_data),
        'muscle_cramp': analyze_cramp_risk(dna_data),
        'recovery': analyze_recovery(dna_data),
        'fatigue': analyze_fatigue(dna_data),
        'bp_response': analyze_bp_response(dna_data),
        'lactate': analyze_lactate(dna_data)
    }

    # Calculate overall athletic profile
    results['athletic_profile'] = calculate_athletic_profile(results)
    results['recommendations'] = generate_sports_recommendations(results)

    return results


def analyze_muscle_fiber(dna_data: dict) -> dict:
    """Analyze muscle fiber composition genetics"""
    result = {
        'type': 'Mixed',
        'power_score': 0.5,
        'endurance_score': 0.5,
        'actn3_status': 'Unknown',
        'optimal_sports': [],
        'markers_found': [],
        'description': ''
    }

    for rsid, marker_data in MUSCLE_FIBER_GENETICS['markers'].items():
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
                    'fiber_type': data.get('fiber_type', '')
                })

                # ACTN3 is the primary marker
                if marker_data['gene'] == 'ACTN3':
                    result['actn3_status'] = data['phenotype']
                    result['type'] = data.get('fiber_type', 'Mixed')
                    result['optimal_sports'] = data.get('optimal_sports', [])

                    if data.get('score', 0.5) >= 0.7:
                        result['power_score'] = 0.85
                        result['endurance_score'] = 0.35
                        result['description'] = 'You have the "sprinter gene" - optimized for power and speed activities.'
                    elif data.get('score', 0.5) <= 0.3:
                        result['power_score'] = 0.35
                        result['endurance_score'] = 0.85
                        result['description'] = 'You have enhanced endurance genetics - optimized for aerobic activities.'
                    else:
                        result['power_score'] = 0.5
                        result['endurance_score'] = 0.5
                        result['description'] = 'You have versatile muscle genetics - suited for varied sports.'

    return result


def analyze_vo2max(dna_data: dict) -> dict:
    """Analyze VO2 max potential genetics"""
    result = {
        'potential': 'Average',
        'score': 0.5,
        'trainability': 'Normal',
        'markers_found': [],
        'description': ''
    }

    scores = []

    for rsid, marker_data in VO2MAX_GENETICS['markers'].items():
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
                    'phenotype': data['phenotype']
                })

    if scores:
        avg_score = sum(scores) / len(scores)
        result['score'] = avg_score

        if avg_score >= 0.65:
            result['potential'] = 'High'
            result['trainability'] = 'High responder'
            result['description'] = 'You have excellent VO2 max genetics - high aerobic potential with training.'
        elif avg_score <= 0.4:
            result['potential'] = 'Lower'
            result['trainability'] = 'May need more training'
            result['description'] = 'You may need to work harder to improve aerobic capacity.'
        else:
            result['potential'] = 'Average'
            result['trainability'] = 'Normal responder'
            result['description'] = 'You have typical VO2 max genetics.'

    return result


def analyze_acl_risk(dna_data: dict) -> dict:
    """Analyze ACL injury risk genetics"""
    result = {
        'risk_level': 'Average',
        'risk_score': 0.5,
        'markers_found': [],
        'description': ''
    }

    scores = []

    for rsid, marker_data in ACL_INJURY_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                scores.append(data.get('risk_score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })

    if scores:
        avg_score = sum(scores) / len(scores)
        result['risk_score'] = avg_score

        if avg_score >= 0.6:
            result['risk_level'] = 'Elevated'
            result['description'] = 'You may have higher ACL injury susceptibility. Focus on preventive exercises.'
        elif avg_score <= 0.4:
            result['risk_level'] = 'Lower'
            result['description'] = 'You have lower genetic risk for ACL injuries.'
        else:
            result['risk_level'] = 'Average'
            result['description'] = 'Your ACL injury risk is about average.'

    return result


def analyze_tendon_risk(dna_data: dict) -> dict:
    """Analyze tendon injury risk genetics"""
    result = {
        'risk_level': 'Average',
        'risk_score': 0.5,
        'achilles_risk': 'Average',
        'markers_found': [],
        'description': ''
    }

    scores = []

    for rsid, marker_data in TENDON_INJURY_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                scores.append(data.get('risk_score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })

    if scores:
        avg_score = sum(scores) / len(scores)
        result['risk_score'] = avg_score

        if avg_score >= 0.6:
            result['risk_level'] = 'Elevated'
            result['achilles_risk'] = 'Higher'
            result['description'] = 'You may be more prone to tendon injuries. Warm up thoroughly and progress gradually.'
        elif avg_score <= 0.4:
            result['risk_level'] = 'Lower'
            result['achilles_risk'] = 'Lower'
            result['description'] = 'You have lower genetic risk for tendon injuries.'
        else:
            result['risk_level'] = 'Average'
            result['achilles_risk'] = 'Average'
            result['description'] = 'Your tendon injury risk is about average.'

    return result


def analyze_cramp_risk(dna_data: dict) -> dict:
    """Analyze muscle cramping genetics"""
    result = {
        'risk_level': 'Average',
        'risk_score': 0.5,
        'markers_found': [],
        'description': ''
    }

    scores = []

    for rsid, marker_data in MUSCLE_CRAMP_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                scores.append(data.get('risk_score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })

    if scores:
        avg_score = sum(scores) / len(scores)
        result['risk_score'] = avg_score

        if avg_score >= 0.6:
            result['risk_level'] = 'Higher'
            result['description'] = 'You may be more prone to exercise-related muscle cramps. Stay hydrated and ensure adequate electrolytes.'
        elif avg_score <= 0.4:
            result['risk_level'] = 'Lower'
            result['description'] = 'You are less prone to muscle cramps.'
        else:
            result['risk_level'] = 'Average'
            result['description'] = 'Your cramping tendency is average.'

    return result


def analyze_recovery(dna_data: dict) -> dict:
    """Analyze exercise recovery genetics"""
    result = {
        'speed': 'Normal',
        'score': 0.5,
        'inflammation_tendency': 'Normal',
        'markers_found': [],
        'description': ''
    }

    scores = []

    for rsid, marker_data in RECOVERY_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                scores.append(data.get('recovery_score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })

    if scores:
        avg_score = sum(scores) / len(scores)
        result['score'] = avg_score

        if avg_score >= 0.6:
            result['speed'] = 'Fast'
            result['inflammation_tendency'] = 'Lower'
            result['description'] = 'You recover faster from exercise. Can handle higher training frequency.'
        elif avg_score <= 0.4:
            result['speed'] = 'Slower'
            result['inflammation_tendency'] = 'Higher'
            result['description'] = 'You may need more recovery time between intense workouts.'
        else:
            result['speed'] = 'Normal'
            result['inflammation_tendency'] = 'Normal'
            result['description'] = 'Your recovery speed is typical.'

    return result


def analyze_fatigue(dna_data: dict) -> dict:
    """Analyze exercise fatigue genetics"""
    result = {
        'resistance': 'Normal',
        'score': 0.5,
        'markers_found': [],
        'description': ''
    }

    scores = []

    for rsid, marker_data in FATIGUE_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                scores.append(data.get('fatigue_score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })

    if scores:
        avg_score = sum(scores) / len(scores)
        result['score'] = avg_score

        if avg_score >= 0.6:
            result['resistance'] = 'High'
            result['description'] = 'You have good fatigue resistance - can maintain intensity longer.'
        elif avg_score <= 0.35:
            result['resistance'] = 'Lower'
            result['description'] = 'You may fatigue faster during intense exercise. Focus on pacing.'
        else:
            result['resistance'] = 'Normal'
            result['description'] = 'Your fatigue resistance is typical.'

    return result


def analyze_bp_response(dna_data: dict) -> dict:
    """Analyze blood pressure response to exercise"""
    result = {
        'response': 'Normal',
        'risk_score': 0.5,
        'markers_found': [],
        'description': ''
    }

    scores = []

    for rsid, marker_data in BP_EXERCISE_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                scores.append(data.get('risk_score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })

    if scores:
        avg_score = sum(scores) / len(scores)
        result['risk_score'] = avg_score

        if avg_score >= 0.6:
            result['response'] = 'Elevated'
            result['description'] = 'You may have a greater blood pressure increase with exercise. Consider monitoring.'
        elif avg_score <= 0.4:
            result['response'] = 'Lower'
            result['description'] = 'You have good blood pressure regulation during exercise.'
        else:
            result['response'] = 'Normal'
            result['description'] = 'Your blood pressure response to exercise is typical.'

    return result


def analyze_lactate(dna_data: dict) -> dict:
    """Analyze lactate clearance genetics"""
    result = {
        'clearance': 'Normal',
        'score': 0.5,
        'markers_found': [],
        'description': ''
    }

    scores = []

    for rsid, marker_data in LACTATE_GENETICS['markers'].items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            genotypes = marker_data['genotypes']

            _key = get_genotype_key(genotype, genotypes)
            if _key:

                data = genotypes[_key]
                scores.append(data.get('clearance_score', 0.5))
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })

    if scores:
        avg_score = sum(scores) / len(scores)
        result['score'] = avg_score

        if avg_score >= 0.65:
            result['clearance'] = 'Fast'
            result['description'] = 'You clear lactate efficiently - can sustain high intensity exercise longer.'
        elif avg_score <= 0.35:
            result['clearance'] = 'Slow'
            result['description'] = 'Lactate accumulates faster during exercise - "the burn" hits sooner.'
        else:
            result['clearance'] = 'Normal'
            result['description'] = 'Your lactate clearance is typical.'

    return result


def calculate_athletic_profile(results: dict) -> dict:
    """Calculate overall athletic profile"""
    profile = {
        'type': 'All-Rounder',
        'power_score': 0.5,
        'endurance_score': 0.5,
        'injury_resilience': 0.5,
        'strengths': [],
        'challenges': [],
        'recommended_sports': []
    }

    # Get muscle fiber type
    fiber = results.get('muscle_fiber', {})
    profile['power_score'] = fiber.get('power_score', 0.5)
    profile['endurance_score'] = fiber.get('endurance_score', 0.5)

    if profile['power_score'] >= 0.7:
        profile['type'] = 'Power Athlete'
        profile['strengths'].append('Power/sprint genetics')
        profile['recommended_sports'] = ['Sprinting', 'Weightlifting', 'Football', 'Basketball', 'Jumping sports']
    elif profile['endurance_score'] >= 0.7:
        profile['type'] = 'Endurance Athlete'
        profile['strengths'].append('Endurance genetics')
        profile['recommended_sports'] = ['Marathon', 'Triathlon', 'Cycling', 'Swimming', 'Cross-country']
    else:
        profile['type'] = 'All-Rounder'
        profile['strengths'].append('Versatile muscle genetics')
        profile['recommended_sports'] = ['Soccer', 'Tennis', 'Swimming', 'CrossFit', 'Team sports']

    # VO2 max
    vo2 = results.get('vo2max', {})
    if vo2.get('score', 0.5) >= 0.65:
        profile['strengths'].append('High VO2 max potential')
    elif vo2.get('score', 0.5) <= 0.35:
        profile['challenges'].append('Lower VO2 max ceiling')

    # Injury risks
    injury_scores = []
    acl = results.get('acl_injury', {})
    if acl.get('risk_score', 0.5) >= 0.6:
        profile['challenges'].append('Higher ACL injury risk')
        injury_scores.append(0.3)
    else:
        injury_scores.append(0.7)

    tendon = results.get('tendon_injury', {})
    if tendon.get('risk_score', 0.5) >= 0.6:
        profile['challenges'].append('Higher tendon injury risk')
        injury_scores.append(0.3)
    else:
        injury_scores.append(0.7)

    if injury_scores:
        profile['injury_resilience'] = sum(injury_scores) / len(injury_scores)

    # Recovery
    recovery = results.get('recovery', {})
    if recovery.get('score', 0.5) >= 0.6:
        profile['strengths'].append('Fast recovery genetics')
    elif recovery.get('score', 0.5) <= 0.4:
        profile['challenges'].append('Slower recovery')

    # Lactate
    lactate = results.get('lactate', {})
    if lactate.get('score', 0.5) >= 0.65:
        profile['strengths'].append('Efficient lactate clearance')
    elif lactate.get('score', 0.5) <= 0.35:
        profile['challenges'].append('Lactate accumulates faster')

    return profile


def generate_sports_recommendations(results: dict) -> List[str]:
    """Generate personalized sports/training recommendations"""
    recommendations = []

    # Muscle fiber
    fiber = results.get('muscle_fiber', {})
    if fiber.get('power_score', 0.5) >= 0.7:
        recommendations.append('Focus on power and explosive training - you\'re genetically suited for it.')
    elif fiber.get('endurance_score', 0.5) >= 0.7:
        recommendations.append('Prioritize endurance training - your genetics favor aerobic activities.')

    # VO2 max
    vo2 = results.get('vo2max', {})
    if vo2.get('score', 0.5) <= 0.4:
        recommendations.append('Include consistent aerobic training to maximize your VO2 max potential.')

    # Injury prevention
    acl = results.get('acl_injury', {})
    if acl.get('risk_score', 0.5) >= 0.6:
        recommendations.append('Do ACL prevention exercises: Nordic curls, single-leg stability, and proper landing mechanics.')

    tendon = results.get('tendon_injury', {})
    if tendon.get('risk_score', 0.5) >= 0.6:
        recommendations.append('Progress training gradually and include eccentric exercises for tendon health.')

    # Cramping
    cramp = results.get('muscle_cramp', {})
    if cramp.get('risk_score', 0.5) >= 0.6:
        recommendations.append('Stay well hydrated and ensure adequate sodium, potassium, and magnesium intake.')

    # Recovery
    recovery = results.get('recovery', {})
    if recovery.get('score', 0.5) <= 0.4:
        recommendations.append('Allow extra recovery time between intense sessions. Prioritize sleep and nutrition.')

    # Blood pressure
    bp = results.get('bp_response', {})
    if bp.get('risk_score', 0.5) >= 0.6:
        recommendations.append('Consider monitoring blood pressure during exercise, especially with heavy lifting.')

    # General
    recommendations.append('Warm up thoroughly and cool down properly to prevent injuries.')

    return recommendations
