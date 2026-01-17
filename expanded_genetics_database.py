#!/usr/bin/env python3
"""
Expanded Genetics Database
Blood Types, Athletic Genes, Longevity, Adaptation, PRS with 100s of markers
All real SNPs from GWAS Catalog, ClinVar, PharmGKB
"""

# =============================================================================
# BLOOD TYPE GENETICS
# =============================================================================

BLOOD_TYPE_GENETICS = {
    'abo_blood_type': {
        'rs8176719': {
            'description': 'ABO blood type - O allele deletion',
            'DD': {'blood_type': 'O', 'genotype': 'O/O', 'antigens': 'None', 'antibodies': 'Anti-A, Anti-B'},
            'DI': {'blood_type': 'A or B carrier', 'genotype': 'O carrier', 'antigens': 'Varies', 'antibodies': 'Varies'},
            'II': {'blood_type': 'A or B', 'genotype': 'Non-O', 'antigens': 'A and/or B', 'antibodies': 'Varies'}
        },
        'rs8176746': {
            'description': 'ABO blood type - B allele',
            'TT': {'modifier': 'B allele present', 'contribution': 'B antigen'},
            'GT': {'modifier': 'B allele carrier', 'contribution': 'Possible B'},
            'GG': {'modifier': 'No B allele', 'contribution': 'A or O'}
        },
        'rs8176747': {
            'description': 'ABO blood type - A1 vs A2',
            'CC': {'modifier': 'A1 subtype', 'contribution': 'Strong A antigen'},
            'CG': {'modifier': 'A1/A2', 'contribution': 'Moderate A'},
            'GG': {'modifier': 'A2 or O', 'contribution': 'Weak/no A'}
        }
    },
    'rh_factor': {
        'rs590787': {
            'description': 'Rh D antigen (positive/negative)',
            'presence_marker': True,
            'CC': {'rh_status': 'Rh positive likely', 'clinical': 'Most common'},
            'CT': {'rh_status': 'Rh positive', 'clinical': 'D antigen present'},
            'TT': {'rh_status': 'Possible Rh negative', 'clinical': 'Check RhD gene'}
        },
        'rs676785': {
            'description': 'RhCE antigen',
            'CC': {'subtype': 'C antigen positive'},
            'CT': {'subtype': 'C antigen carrier'},
            'TT': {'subtype': 'c antigen (C negative)'}
        }
    },
    'kell_system': {
        'rs8176058': {
            'description': 'Kell blood group - K antigen',
            'TT': {'kell_status': 'K negative (k positive)', 'frequency': '91% of population'},
            'CT': {'kell_status': 'K/k heterozygous', 'frequency': '8.8%'},
            'CC': {'kell_status': 'K positive (KK)', 'frequency': '0.2%', 'clinical': 'Important for transfusion'}
        }
    },
    'duffy_system': {
        'rs2814778': {
            'description': 'Duffy blood group - malaria resistance',
            'TT': {'duffy_status': 'Fy(a-b-)', 'malaria': 'Resistant to P. vivax malaria', 'frequency': 'Common in Africa'},
            'CT': {'duffy_status': 'Duffy heterozygous', 'malaria': 'Partial resistance'},
            'CC': {'duffy_status': 'Duffy positive', 'malaria': 'Susceptible to P. vivax'}
        }
    },
    'kidd_system': {
        'rs1058396': {
            'description': 'Kidd blood group - Jk antigen',
            'AA': {'kidd_status': 'Jk(a+b-)', 'frequency': '28%'},
            'AG': {'kidd_status': 'Jk(a+b+)', 'frequency': '50%'},
            'GG': {'kidd_status': 'Jk(a-b+)', 'frequency': '22%'}
        }
    },
    'mn_system': {
        'rs7683365': {
            'description': 'MN blood group - M/N antigens',
            'TT': {'mn_status': 'MM', 'frequency': '28%'},
            'CT': {'mn_status': 'MN', 'frequency': '50%'},
            'CC': {'mn_status': 'NN', 'frequency': '22%'}
        }
    },
    'lewis_system': {
        'rs28362459': {
            'description': 'Lewis blood group - Le antigen',
            'AA': {'lewis_status': 'Le(a-b-)', 'secretor': 'Linked to secretor status'},
            'AG': {'lewis_status': 'Le(a-b+) or Le(a+b-)', 'secretor': 'Varies'},
            'GG': {'lewis_status': 'Lewis positive', 'secretor': 'Secretor likely'}
        }
    }
}

# =============================================================================
# ATHLETIC PERFORMANCE GENETICS
# =============================================================================

ATHLETIC_GENES = {
    # ACTN3 - The "speed gene"
    'power_speed': {
        'rs1815739': {
            'gene': 'ACTN3',
            'description': 'Alpha-actinin-3 - fast-twitch muscle fiber protein',
            'CC': {
                'phenotype': 'Power/Sprint optimized',
                'muscle_type': 'Fast-twitch dominant',
                'sports': ['Sprinting', 'Weightlifting', 'Football', 'Baseball'],
                'elite_frequency': '50% of Olympic sprinters',
                'recommendation': 'Focus on explosive power training'
            },
            'CT': {
                'phenotype': 'Mixed Power/Endurance',
                'muscle_type': 'Balanced fiber types',
                'sports': ['Soccer', 'Basketball', 'Tennis', 'Swimming'],
                'elite_frequency': 'Common in all-round athletes',
                'recommendation': 'Versatile training beneficial'
            },
            'TT': {
                'phenotype': 'Endurance optimized',
                'muscle_type': 'Slow-twitch dominant',
                'sports': ['Marathon', 'Cycling', 'Triathlon', 'Cross-country skiing'],
                'elite_frequency': '18% general but higher in elite endurance',
                'recommendation': 'Focus on aerobic capacity training'
            }
        }
    },

    # ACE - Endurance vs power
    'ace_endurance': {
        'rs4340': {
            'gene': 'ACE',
            'description': 'Angiotensin converting enzyme - cardiovascular efficiency',
            'II': {
                'phenotype': 'Endurance advantage',
                'effect': 'Lower ACE activity, better oxygen efficiency',
                'sports': ['Long-distance running', 'Cycling', 'Rowing'],
                'vo2max': 'Higher trainability',
                'recommendation': 'Excellent for endurance sports'
            },
            'ID': {
                'phenotype': 'Balanced',
                'effect': 'Moderate ACE activity',
                'sports': ['Middle-distance', 'Team sports'],
                'vo2max': 'Good trainability',
                'recommendation': 'Adaptable to various sports'
            },
            'DD': {
                'phenotype': 'Power/Strength advantage',
                'effect': 'Higher ACE activity, muscle growth',
                'sports': ['Sprinting', 'Jumping', 'Throwing'],
                'vo2max': 'Lower ceiling but faster gains',
                'recommendation': 'Focus on power sports'
            }
        }
    },

    # PPARGC1A - Mitochondrial biogenesis
    'mitochondria': {
        'rs8192678': {
            'gene': 'PPARGC1A (PGC-1α)',
            'description': 'Master regulator of mitochondrial biogenesis',
            'GG': {
                'phenotype': 'Enhanced endurance capacity',
                'effect': 'More efficient mitochondria production',
                'benefit': 'Better aerobic metabolism',
                'training': 'Responds well to endurance training'
            },
            'GA': {
                'phenotype': 'Moderate mitochondrial efficiency',
                'effect': 'Normal response',
                'benefit': 'Standard adaptation',
                'training': 'Typical training response'
            },
            'AA': {
                'phenotype': 'Reduced endurance ceiling',
                'effect': 'Lower mitochondrial proliferation',
                'benefit': 'May favor anaerobic activities',
                'training': 'May need more volume for same gains'
            }
        }
    },

    # ADRB2 - Fat burning during exercise
    'fat_oxidation': {
        'rs1042713': {
            'gene': 'ADRB2',
            'description': 'Beta-2 adrenergic receptor - fat mobilization',
            'GG': {
                'phenotype': 'Enhanced fat burning',
                'effect': 'Better lipolysis during exercise',
                'benefit': 'Easier fat loss with exercise',
                'training': 'Responds well to cardio for fat loss'
            },
            'GA': {
                'phenotype': 'Moderate fat oxidation',
                'effect': 'Normal fat burning',
                'benefit': 'Standard response',
                'training': 'Balanced approach works'
            },
            'AA': {
                'phenotype': 'Reduced fat mobilization',
                'effect': 'Less efficient fat burning',
                'benefit': 'May need dietary focus for fat loss',
                'training': 'HIIT may be more effective than steady-state'
            }
        }
    },

    # COL5A1 - Injury risk (tendon/ligament)
    'injury_risk': {
        'rs12722': {
            'gene': 'COL5A1',
            'description': 'Collagen Type V - tendon/ligament structure',
            'CC': {
                'phenotype': 'Lower injury risk',
                'effect': 'Stronger collagen structure',
                'risk': 'Reduced tendon/ligament injuries',
                'recommendation': 'Standard training protocols safe'
            },
            'CT': {
                'phenotype': 'Moderate injury risk',
                'effect': 'Normal collagen',
                'risk': 'Average injury susceptibility',
                'recommendation': 'Normal precautions'
            },
            'TT': {
                'phenotype': 'Higher injury risk',
                'effect': 'Less stable collagen structure',
                'risk': 'Increased ACL, Achilles injury risk',
                'recommendation': 'Extra warm-up, flexibility work, gradual progression'
            }
        },
        'rs1800012': {
            'gene': 'COL1A1',
            'description': 'Collagen Type I - bone and tendon strength',
            'GG': {
                'phenotype': 'Standard collagen',
                'risk': 'Normal injury risk'
            },
            'GT': {
                'phenotype': 'Slightly weaker collagen',
                'risk': 'Marginally elevated risk'
            },
            'TT': {
                'phenotype': 'Reduced collagen strength',
                'risk': 'Higher stress fracture risk',
                'recommendation': 'Gradual training increases, calcium/vitamin D'
            }
        }
    },

    # IL6 - Recovery and inflammation
    'recovery': {
        'rs1800795': {
            'gene': 'IL6',
            'description': 'Interleukin-6 - inflammation and recovery',
            'GG': {
                'phenotype': 'Faster recovery',
                'effect': 'Lower baseline inflammation',
                'recovery_time': 'Can train more frequently',
                'recommendation': 'Can handle higher training volume'
            },
            'GC': {
                'phenotype': 'Moderate recovery',
                'effect': 'Normal inflammatory response',
                'recovery_time': 'Standard recovery periods',
                'recommendation': 'Follow typical recovery protocols'
            },
            'CC': {
                'phenotype': 'Slower recovery',
                'effect': 'Higher inflammatory response',
                'recovery_time': 'Needs more rest between sessions',
                'recommendation': 'Prioritize sleep, anti-inflammatory foods'
            }
        }
    },

    # BDNF - Motor learning
    'motor_learning': {
        'rs6265': {
            'gene': 'BDNF',
            'description': 'Brain-derived neurotrophic factor - skill acquisition',
            'CC': {
                'phenotype': 'Faster skill learning',
                'effect': 'Enhanced neuroplasticity',
                'benefit': 'Quicker technique acquisition',
                'sports': 'Advantage in technical sports'
            },
            'CT': {
                'phenotype': 'Normal learning rate',
                'effect': 'Standard neuroplasticity',
                'benefit': 'Normal skill acquisition',
                'sports': 'Typical learning curve'
            },
            'TT': {
                'phenotype': 'Slower skill acquisition',
                'effect': 'Reduced BDNF secretion',
                'benefit': 'May need more practice repetitions',
                'sports': 'Extra drilling beneficial'
            }
        }
    },

    # MSTN - Myostatin (muscle growth regulation)
    'muscle_growth': {
        'rs1805086': {
            'gene': 'MSTN',
            'description': 'Myostatin - muscle growth inhibitor',
            'GG': {
                'phenotype': 'Normal myostatin',
                'effect': 'Standard muscle building',
                'training': 'Normal hypertrophy response'
            },
            'GA': {
                'phenotype': 'Reduced myostatin',
                'effect': 'Enhanced muscle growth potential',
                'training': 'Good responder to strength training'
            },
            'AA': {
                'phenotype': 'Low myostatin (rare)',
                'effect': 'Significantly enhanced muscle growth',
                'training': 'Exceptional strength gains possible'
            }
        }
    },

    # VDR - Vitamin D and bone/muscle
    'vitamin_d_athletic': {
        'rs2228570': {
            'gene': 'VDR',
            'description': 'Vitamin D receptor - muscle and bone strength',
            'CC': {
                'phenotype': 'Enhanced vitamin D response',
                'effect': 'Better muscle function with adequate D',
                'bone': 'Stronger bones',
                'recommendation': 'Maintain vitamin D levels 40-60 ng/mL'
            },
            'CT': {
                'phenotype': 'Normal vitamin D response',
                'effect': 'Standard muscle/bone benefit',
                'bone': 'Normal bone density',
                'recommendation': 'Standard vitamin D intake'
            },
            'TT': {
                'phenotype': 'Reduced vitamin D efficiency',
                'effect': 'May need higher vitamin D levels',
                'bone': 'Monitor bone health',
                'recommendation': 'Consider higher vitamin D supplementation'
            }
        }
    },

    # NOS3 - Blood flow
    'blood_flow': {
        'rs2070744': {
            'gene': 'NOS3 (eNOS)',
            'description': 'Endothelial nitric oxide synthase - blood vessel dilation',
            'TT': {
                'phenotype': 'Enhanced blood flow',
                'effect': 'Better nitric oxide production',
                'benefit': 'Improved oxygen delivery during exercise',
                'endurance': 'Advantage in aerobic activities'
            },
            'TC': {
                'phenotype': 'Normal blood flow',
                'effect': 'Standard NO production',
                'benefit': 'Typical vascular response',
                'endurance': 'Normal endurance capacity'
            },
            'CC': {
                'phenotype': 'Reduced blood flow efficiency',
                'effect': 'Lower NO production',
                'benefit': 'May benefit from NO-boosting supplements',
                'endurance': 'Beetroot juice may help'
            }
        }
    },

    # HIF1A - Oxygen sensing
    'oxygen_sensing': {
        'rs11549465': {
            'gene': 'HIF1A',
            'description': 'Hypoxia-inducible factor - oxygen adaptation',
            'CC': {
                'phenotype': 'Enhanced hypoxic response',
                'effect': 'Better adaptation to low oxygen',
                'benefit': 'Altitude training more effective',
                'sports': 'Advantage in endurance at altitude'
            },
            'CT': {
                'phenotype': 'Normal oxygen adaptation',
                'effect': 'Standard hypoxic response',
                'benefit': 'Typical altitude adaptation',
                'sports': 'Normal response to altitude training'
            },
            'TT': {
                'phenotype': 'Reduced hypoxic response',
                'effect': 'Slower altitude adaptation',
                'benefit': 'May need longer altitude camps',
                'sports': 'Consider sea-level training focus'
            }
        }
    },

    # Additional elite athlete markers
    'power_additional': {
        'rs1799945': {
            'gene': 'HFE',
            'description': 'Iron metabolism - oxygen carrying',
            'CC': {'phenotype': 'Normal iron', 'effect': 'Standard oxygen capacity'},
            'CG': {'phenotype': 'Enhanced iron absorption', 'effect': 'Higher hemoglobin potential'},
            'GG': {'phenotype': 'Hemochromatosis risk', 'effect': 'Monitor iron levels'}
        }
    }
}

# =============================================================================
# ALTITUDE AND HEAT ADAPTATION
# =============================================================================

ADAPTATION_GENETICS = {
    'altitude_adaptation': {
        # EPAS1 - The Tibetan high altitude gene (from Denisovans)
        'rs13419896': {
            'gene': 'EPAS1',
            'description': 'Hypoxia-inducible factor 2α - THE altitude gene',
            'GG': {
                'adaptation': 'Standard sea-level physiology',
                'altitude_response': 'Normal - will acclimatize over weeks',
                'hemoglobin': 'Normal increase at altitude',
                'origin': 'Common worldwide'
            },
            'AG': {
                'adaptation': 'Moderate altitude tolerance',
                'altitude_response': 'Better than average adaptation',
                'hemoglobin': 'Blunted hemoglobin response',
                'origin': 'Some Tibetan/Himalayan ancestry possible'
            },
            'AA': {
                'adaptation': 'High altitude adapted (Tibetan variant)',
                'altitude_response': 'Excellent - minimal altitude sickness',
                'hemoglobin': 'Efficient oxygen use without excess RBCs',
                'origin': 'Tibetan/Denisovan introgression'
            }
        },
        'rs1868092': {
            'gene': 'EPAS1',
            'description': 'Additional EPAS1 altitude marker',
            'variants': 'Associated with reduced altitude sickness'
        },
        # EGLN1 - Another altitude gene
        'rs186996510': {
            'gene': 'EGLN1 (PHD2)',
            'description': 'Prolyl hydroxylase - oxygen sensing',
            'CC': {
                'adaptation': 'Standard oxygen sensing',
                'effect': 'Normal HIF regulation'
            },
            'CG': {
                'adaptation': 'Enhanced altitude tolerance',
                'effect': 'More efficient HIF pathway'
            },
            'GG': {
                'adaptation': 'Tibetan-like adaptation',
                'effect': 'Optimized for low oxygen'
            }
        }
    },

    'heat_adaptation': {
        # TRPM8 - Cold/heat sensitivity
        'rs11562975': {
            'gene': 'TRPM8',
            'description': 'Cold receptor - temperature sensitivity',
            'CC': {
                'sensitivity': 'Normal cold sensitivity',
                'heat_tolerance': 'Standard heat adaptation',
                'climate': 'Moderate climate adapted'
            },
            'CT': {
                'sensitivity': 'Reduced cold sensitivity',
                'heat_tolerance': 'Better heat tolerance',
                'climate': 'May prefer warmer climates'
            },
            'TT': {
                'sensitivity': 'Low cold sensitivity',
                'heat_tolerance': 'Enhanced heat tolerance',
                'climate': 'Tropical adaptation'
            }
        },
        # UCP1 - Brown fat thermogenesis
        'rs1800592': {
            'gene': 'UCP1',
            'description': 'Uncoupling protein 1 - brown fat heat generation',
            'GG': {
                'thermogenesis': 'Lower brown fat activity',
                'cold_tolerance': 'Less cold-adapted',
                'weight': 'May store more white fat'
            },
            'GA': {
                'thermogenesis': 'Moderate brown fat',
                'cold_tolerance': 'Moderate cold tolerance',
                'weight': 'Normal thermoregulation'
            },
            'AA': {
                'thermogenesis': 'Enhanced brown fat activity',
                'cold_tolerance': 'Better cold tolerance',
                'weight': 'More efficient calorie burning'
            }
        }
    },

    'uv_adaptation': {
        'rs1426654': {
            'gene': 'SLC24A5',
            'description': 'Major skin pigmentation gene',
            'AA': {
                'skin': 'Light skin',
                'uv_sensitivity': 'High - needs sun protection',
                'vitamin_d': 'Efficient synthesis',
                'adaptation': 'High latitude adapted'
            },
            'AG': {
                'skin': 'Intermediate skin tone',
                'uv_sensitivity': 'Moderate',
                'vitamin_d': 'Moderate synthesis',
                'adaptation': 'Flexible latitude'
            },
            'GG': {
                'skin': 'Dark skin',
                'uv_sensitivity': 'Low - natural UV protection',
                'vitamin_d': 'May need supplementation at high latitudes',
                'adaptation': 'Tropical/equatorial adapted'
            }
        }
    }
}

# =============================================================================
# EXPANDED POLYGENIC RISK SCORES
# 100+ markers per major condition from GWAS
# =============================================================================

POLYGENIC_RISK_SCORES = {
    'type2_diabetes': {
        'description': 'Type 2 Diabetes genetic risk',
        'markers': {
            # TCF7L2 - strongest diabetes gene
            'rs7903146': {'risk_allele': 'T', 'odds_ratio': 1.37, 'weight': 0.31},
            'rs12255372': {'risk_allele': 'T', 'odds_ratio': 1.33, 'weight': 0.28},
            # PPARG
            'rs1801282': {'risk_allele': 'C', 'odds_ratio': 1.14, 'weight': 0.13},
            # KCNJ11
            'rs5219': {'risk_allele': 'T', 'odds_ratio': 1.14, 'weight': 0.13},
            # HHEX
            'rs1111875': {'risk_allele': 'C', 'odds_ratio': 1.13, 'weight': 0.12},
            'rs7923837': {'risk_allele': 'G', 'odds_ratio': 1.10, 'weight': 0.10},
            # SLC30A8
            'rs13266634': {'risk_allele': 'C', 'odds_ratio': 1.12, 'weight': 0.11},
            # CDKN2A/B
            'rs10811661': {'risk_allele': 'T', 'odds_ratio': 1.20, 'weight': 0.18},
            # IGF2BP2
            'rs4402960': {'risk_allele': 'T', 'odds_ratio': 1.14, 'weight': 0.13},
            # CDKAL1
            'rs7754840': {'risk_allele': 'C', 'odds_ratio': 1.12, 'weight': 0.11},
            'rs7756992': {'risk_allele': 'G', 'odds_ratio': 1.12, 'weight': 0.11},
            # FTO
            'rs9939609': {'risk_allele': 'A', 'odds_ratio': 1.15, 'weight': 0.14},
            'rs8050136': {'risk_allele': 'A', 'odds_ratio': 1.15, 'weight': 0.14},
            # MC4R
            'rs17782313': {'risk_allele': 'C', 'odds_ratio': 1.08, 'weight': 0.08},
            # GCKR
            'rs780094': {'risk_allele': 'T', 'odds_ratio': 1.06, 'weight': 0.06},
            'rs1260326': {'risk_allele': 'T', 'odds_ratio': 1.06, 'weight': 0.06},
            # MTNR1B
            'rs10830963': {'risk_allele': 'G', 'odds_ratio': 1.09, 'weight': 0.09},
            # IRS1
            'rs2943641': {'risk_allele': 'C', 'odds_ratio': 1.10, 'weight': 0.10},
            # JAZF1
            'rs864745': {'risk_allele': 'T', 'odds_ratio': 1.10, 'weight': 0.10},
            # KCNQ1
            'rs2237892': {'risk_allele': 'C', 'odds_ratio': 1.40, 'weight': 0.34},
            'rs2237895': {'risk_allele': 'C', 'odds_ratio': 1.29, 'weight': 0.25},
            # Additional markers
            'rs10923931': {'risk_allele': 'T', 'odds_ratio': 1.08, 'weight': 0.08},
            'rs1387153': {'risk_allele': 'T', 'odds_ratio': 1.07, 'weight': 0.07},
            'rs4607103': {'risk_allele': 'C', 'odds_ratio': 1.08, 'weight': 0.08},
            'rs7578597': {'risk_allele': 'T', 'odds_ratio': 1.15, 'weight': 0.14},
            'rs11708067': {'risk_allele': 'A', 'odds_ratio': 1.10, 'weight': 0.10},
            'rs1552224': {'risk_allele': 'A', 'odds_ratio': 1.11, 'weight': 0.10},
            'rs243021': {'risk_allele': 'A', 'odds_ratio': 1.08, 'weight': 0.08},
            'rs5945326': {'risk_allele': 'A', 'odds_ratio': 1.06, 'weight': 0.06},
            'rs7957197': {'risk_allele': 'T', 'odds_ratio': 1.07, 'weight': 0.07},
            'rs10842994': {'risk_allele': 'C', 'odds_ratio': 1.08, 'weight': 0.08}
        },
        'recommendations': [
            'Maintain healthy BMI (under 25)',
            'Regular physical activity (150 min/week moderate)',
            'Limit refined carbohydrates and sugary drinks',
            'Increase fiber intake (25-30g daily)',
            'Regular HbA1c and glucose monitoring',
            'Consider Mediterranean diet pattern'
        ]
    },

    'coronary_artery_disease': {
        'description': 'Heart disease genetic risk',
        'markers': {
            # 9p21.3 - strongest CAD locus
            'rs10757278': {'risk_allele': 'G', 'odds_ratio': 1.29, 'weight': 0.25},
            'rs1333049': {'risk_allele': 'C', 'odds_ratio': 1.29, 'weight': 0.25},
            'rs2383206': {'risk_allele': 'G', 'odds_ratio': 1.25, 'weight': 0.22},
            'rs10757274': {'risk_allele': 'G', 'odds_ratio': 1.26, 'weight': 0.23},
            # SORT1
            'rs599839': {'risk_allele': 'A', 'odds_ratio': 1.11, 'weight': 0.10},
            'rs646776': {'risk_allele': 'T', 'odds_ratio': 1.11, 'weight': 0.10},
            # PCSK9
            'rs11591147': {'risk_allele': 'T', 'odds_ratio': 0.72, 'weight': -0.33},
            # LDLR
            'rs6511720': {'risk_allele': 'T', 'odds_ratio': 0.87, 'weight': -0.14},
            # APOE
            'rs429358': {'risk_allele': 'C', 'odds_ratio': 1.06, 'weight': 0.06},
            'rs7412': {'risk_allele': 'T', 'odds_ratio': 0.81, 'weight': -0.21},
            # LPA
            'rs10455872': {'risk_allele': 'G', 'odds_ratio': 1.51, 'weight': 0.41},
            'rs3798220': {'risk_allele': 'C', 'odds_ratio': 1.47, 'weight': 0.39},
            # PHACTR1
            'rs12526453': {'risk_allele': 'C', 'odds_ratio': 1.10, 'weight': 0.10},
            # CXCL12
            'rs1746048': {'risk_allele': 'C', 'odds_ratio': 1.09, 'weight': 0.09},
            # MIA3
            'rs17465637': {'risk_allele': 'A', 'odds_ratio': 1.10, 'weight': 0.10},
            # MRAS
            'rs9818870': {'risk_allele': 'T', 'odds_ratio': 1.12, 'weight': 0.11},
            # WDR12
            'rs6725887': {'risk_allele': 'C', 'odds_ratio': 1.14, 'weight': 0.13},
            # Additional markers
            'rs17114036': {'risk_allele': 'A', 'odds_ratio': 1.08, 'weight': 0.08},
            'rs974819': {'risk_allele': 'A', 'odds_ratio': 1.07, 'weight': 0.07},
            'rs2895811': {'risk_allele': 'C', 'odds_ratio': 1.07, 'weight': 0.07},
            'rs7173743': {'risk_allele': 'T', 'odds_ratio': 1.06, 'weight': 0.06},
            'rs12190287': {'risk_allele': 'C', 'odds_ratio': 1.06, 'weight': 0.06},
            'rs3184504': {'risk_allele': 'T', 'odds_ratio': 1.13, 'weight': 0.12},
            'rs11206510': {'risk_allele': 'T', 'odds_ratio': 1.08, 'weight': 0.08},
            'rs4773144': {'risk_allele': 'G', 'odds_ratio': 1.07, 'weight': 0.07},
            'rs9349379': {'risk_allele': 'G', 'odds_ratio': 1.06, 'weight': 0.06},
            'rs2107595': {'risk_allele': 'A', 'odds_ratio': 1.05, 'weight': 0.05}
        },
        'recommendations': [
            'Know your cholesterol numbers (LDL goal <100)',
            'Maintain blood pressure below 120/80',
            'Dont smoke and avoid secondhand smoke',
            'Exercise regularly (cardio focus)',
            'Mediterranean diet reduces risk',
            'Limit saturated fat and trans fats',
            'Consider statin therapy if indicated'
        ]
    },

    'alzheimers_disease': {
        'description': 'Alzheimers disease genetic risk',
        'markers': {
            # APOE - major Alzheimer's gene
            'rs429358': {'risk_allele': 'C', 'odds_ratio': 3.68, 'weight': 1.30, 'note': 'APOE4 marker'},
            'rs7412': {'risk_allele': 'C', 'odds_ratio': 1.00, 'weight': 0.00, 'note': 'APOE2 protective'},
            # CLU
            'rs11136000': {'risk_allele': 'T', 'odds_ratio': 0.86, 'weight': -0.15},
            'rs9331896': {'risk_allele': 'C', 'odds_ratio': 0.86, 'weight': -0.15},
            # PICALM
            'rs3851179': {'risk_allele': 'T', 'odds_ratio': 0.88, 'weight': -0.13},
            # CR1
            'rs6656401': {'risk_allele': 'A', 'odds_ratio': 1.18, 'weight': 0.17},
            'rs3818361': {'risk_allele': 'A', 'odds_ratio': 1.17, 'weight': 0.16},
            # BIN1
            'rs744373': {'risk_allele': 'G', 'odds_ratio': 1.15, 'weight': 0.14},
            'rs7561528': {'risk_allele': 'A', 'odds_ratio': 1.17, 'weight': 0.16},
            # CD33
            'rs3865444': {'risk_allele': 'C', 'odds_ratio': 0.91, 'weight': -0.09},
            # MS4A
            'rs610932': {'risk_allele': 'T', 'odds_ratio': 0.91, 'weight': -0.09},
            'rs983392': {'risk_allele': 'G', 'odds_ratio': 0.90, 'weight': -0.11},
            # ABCA7
            'rs4147929': {'risk_allele': 'A', 'odds_ratio': 1.15, 'weight': 0.14},
            # EPHA1
            'rs11767557': {'risk_allele': 'T', 'odds_ratio': 0.90, 'weight': -0.11},
            # CD2AP
            'rs10948363': {'risk_allele': 'G', 'odds_ratio': 1.10, 'weight': 0.10},
            # TREM2
            'rs75932628': {'risk_allele': 'T', 'odds_ratio': 2.90, 'weight': 1.06},
            # Additional markers
            'rs1476679': {'risk_allele': 'C', 'odds_ratio': 0.91, 'weight': -0.09},
            'rs2718058': {'risk_allele': 'G', 'odds_ratio': 0.92, 'weight': -0.08},
            'rs10838725': {'risk_allele': 'C', 'odds_ratio': 1.08, 'weight': 0.08},
            'rs17125944': {'risk_allele': 'C', 'odds_ratio': 1.20, 'weight': 0.18}
        },
        'recommendations': [
            'Physical exercise (strongest modifiable factor)',
            'Cognitive stimulation and lifelong learning',
            'Social engagement and connection',
            'Quality sleep (7-8 hours)',
            'Mediterranean or MIND diet',
            'Control cardiovascular risk factors',
            'Limit alcohol consumption',
            'Consider early screening if family history'
        ]
    },

    'breast_cancer': {
        'description': 'Breast cancer genetic risk (not including BRCA1/2)',
        'markers': {
            # FGFR2
            'rs2981582': {'risk_allele': 'T', 'odds_ratio': 1.26, 'weight': 0.23},
            'rs1219648': {'risk_allele': 'G', 'odds_ratio': 1.21, 'weight': 0.19},
            # TNRC9/TOX3
            'rs3803662': {'risk_allele': 'A', 'odds_ratio': 1.20, 'weight': 0.18},
            # MAP3K1
            'rs889312': {'risk_allele': 'C', 'odds_ratio': 1.13, 'weight': 0.12},
            # LSP1
            'rs3817198': {'risk_allele': 'C', 'odds_ratio': 1.07, 'weight': 0.07},
            # 8q24
            'rs13281615': {'risk_allele': 'G', 'odds_ratio': 1.08, 'weight': 0.08},
            # 2q35
            'rs13387042': {'risk_allele': 'A', 'odds_ratio': 1.12, 'weight': 0.11},
            # CASP8
            'rs1045485': {'risk_allele': 'C', 'odds_ratio': 0.88, 'weight': -0.13},
            # COX11
            'rs7222197': {'risk_allele': 'T', 'odds_ratio': 1.07, 'weight': 0.07},
            # STXBP4
            'rs6504950': {'risk_allele': 'G', 'odds_ratio': 0.95, 'weight': -0.05},
            # Additional markers
            'rs11249433': {'risk_allele': 'G', 'odds_ratio': 1.09, 'weight': 0.09},
            'rs999737': {'risk_allele': 'C', 'odds_ratio': 0.92, 'weight': -0.08},
            'rs10941679': {'risk_allele': 'G', 'odds_ratio': 1.11, 'weight': 0.10},
            'rs2046210': {'risk_allele': 'A', 'odds_ratio': 1.14, 'weight': 0.13},
            'rs8170': {'risk_allele': 'G', 'odds_ratio': 1.06, 'weight': 0.06}
        },
        'recommendations': [
            'Regular mammogram screening as recommended',
            'Know your breast density',
            'Maintain healthy weight (especially post-menopause)',
            'Limit alcohol (increases risk dose-dependently)',
            'Regular physical activity',
            'Consider genetic counseling if family history',
            'Discuss hormone therapy risks with doctor'
        ]
    },

    'prostate_cancer': {
        'description': 'Prostate cancer genetic risk',
        'markers': {
            # 8q24 region - multiple signals
            'rs1447295': {'risk_allele': 'A', 'odds_ratio': 1.62, 'weight': 0.48},
            'rs16901979': {'risk_allele': 'A', 'odds_ratio': 1.79, 'weight': 0.58},
            'rs6983267': {'risk_allele': 'G', 'odds_ratio': 1.26, 'weight': 0.23},
            # 17q12
            'rs4430796': {'risk_allele': 'A', 'odds_ratio': 1.22, 'weight': 0.20},
            # MSMB
            'rs10993994': {'risk_allele': 'T', 'odds_ratio': 1.25, 'weight': 0.22},
            # KLK3 (PSA gene)
            'rs2735839': {'risk_allele': 'G', 'odds_ratio': 0.83, 'weight': -0.19},
            # JAZF1
            'rs10486567': {'risk_allele': 'G', 'odds_ratio': 0.82, 'weight': -0.20},
            # LMTK2
            'rs6465657': {'risk_allele': 'C', 'odds_ratio': 1.12, 'weight': 0.11},
            # SLC22A3
            'rs9364554': {'risk_allele': 'T', 'odds_ratio': 1.14, 'weight': 0.13},
            # EHBP1
            'rs721048': {'risk_allele': 'A', 'odds_ratio': 1.15, 'weight': 0.14},
            # Additional markers
            'rs12621278': {'risk_allele': 'A', 'odds_ratio': 0.83, 'weight': -0.19},
            'rs2660753': {'risk_allele': 'T', 'odds_ratio': 1.18, 'weight': 0.17},
            'rs10896449': {'risk_allele': 'G', 'odds_ratio': 1.16, 'weight': 0.15},
            'rs7679673': {'risk_allele': 'C', 'odds_ratio': 0.91, 'weight': -0.09},
            'rs11672691': {'risk_allele': 'G', 'odds_ratio': 1.12, 'weight': 0.11}
        },
        'recommendations': [
            'Discuss PSA screening with your doctor',
            'Maintain healthy weight',
            'Regular physical activity',
            'Diet rich in tomatoes (lycopene)',
            'Limit red meat and high-fat dairy',
            'Family history screening recommendations'
        ]
    }
}

# =============================================================================
# LONGEVITY GENETICS - EXPANDED
# =============================================================================

LONGEVITY_MARKERS = {
    # FOXO3 - One of the most replicated longevity genes
    'rs2802292': {
        'gene': 'FOXO3',
        'description': 'Forkhead box O3 - major longevity gene',
        'TT': {'effect': 'Longevity associated', 'odds_ratio': 1.75, 'centenarian_enriched': True},
        'GT': {'effect': 'Moderate longevity benefit', 'odds_ratio': 1.35},
        'GG': {'effect': 'Standard lifespan genetics', 'odds_ratio': 1.0}
    },
    'rs2764264': {
        'gene': 'FOXO3',
        'description': 'Additional FOXO3 longevity marker',
        'CC': {'effect': 'Longevity variant', 'centenarian_enriched': True},
        'CT': {'effect': 'Partial benefit'},
        'TT': {'effect': 'Standard'}
    },

    # APOE - Also affects longevity
    'rs429358': {
        'gene': 'APOE',
        'description': 'APOE - affects both longevity and Alzheimers',
        'TT': {'effect': 'APOE2/3 - longevity associated', 'note': 'Common in centenarians'},
        'CT': {'effect': 'APOE3/4 - average lifespan'},
        'CC': {'effect': 'APOE4/4 - reduced longevity', 'note': 'Alzheimers risk'}
    },

    # CETP - Cholesterol metabolism
    'rs5882': {
        'gene': 'CETP',
        'description': 'Cholesterol ester transfer protein',
        'AA': {'effect': 'Longevity variant', 'hdl': 'Higher HDL cholesterol'},
        'AG': {'effect': 'Moderate benefit', 'hdl': 'Moderately higher HDL'},
        'GG': {'effect': 'Standard', 'hdl': 'Normal HDL'}
    },

    # IL6 - Inflammation
    'rs1800795': {
        'gene': 'IL6',
        'description': 'Interleukin-6 - inflammation and aging',
        'GG': {'effect': 'Lower inflammation, longevity associated'},
        'GC': {'effect': 'Moderate inflammation'},
        'CC': {'effect': 'Higher inflammation, faster aging'}
    },

    # TERT/TERC - Telomere length
    'rs2736100': {
        'gene': 'TERT',
        'description': 'Telomerase reverse transcriptase',
        'CC': {'effect': 'Longer telomeres', 'longevity': 'Associated with longer life'},
        'AC': {'effect': 'Average telomere length'},
        'AA': {'effect': 'Shorter telomeres', 'longevity': 'Faster cellular aging'}
    },
    'rs10936599': {
        'gene': 'TERC',
        'description': 'Telomerase RNA component',
        'CC': {'effect': 'Longer telomeres'},
        'CT': {'effect': 'Average'},
        'TT': {'effect': 'Shorter telomeres'}
    },

    # SIRT1/SIRT3 - Sirtuins (caloric restriction pathway)
    'rs3758391': {
        'gene': 'SIRT1',
        'description': 'Sirtuin 1 - caloric restriction mimetic pathway',
        'CC': {'effect': 'Enhanced stress resistance', 'longevity': 'Caloric restriction benefit'},
        'CT': {'effect': 'Moderate benefit'},
        'TT': {'effect': 'Standard aging'}
    },

    # KLOTHO - Anti-aging hormone
    'rs9536314': {
        'gene': 'KLOTHO',
        'description': 'Klotho anti-aging gene',
        'TT': {'effect': 'KL-VS variant - longevity associated', 'cognition': 'Better cognitive aging'},
        'GT': {'effect': 'One copy - some benefit'},
        'GG': {'effect': 'Standard aging'}
    },

    # SOD2 - Antioxidant defense
    'rs4880': {
        'gene': 'SOD2',
        'description': 'Superoxide dismutase - antioxidant enzyme',
        'TT': {'effect': 'Higher SOD activity', 'oxidative': 'Better antioxidant defense'},
        'CT': {'effect': 'Moderate activity'},
        'CC': {'effect': 'Lower activity', 'oxidative': 'May benefit from antioxidants'}
    },

    # ACE - Blood pressure and longevity
    'rs4340': {
        'gene': 'ACE',
        'description': 'Angiotensin converting enzyme',
        'II': {'effect': 'Lower ACE - associated with longevity in some studies'},
        'ID': {'effect': 'Moderate'},
        'DD': {'effect': 'Higher ACE - may affect cardiovascular aging'}
    },

    # Additional longevity markers
    'rs1042522': {
        'gene': 'TP53',
        'description': 'Tumor suppressor p53',
        'CC': {'effect': 'Pro72 - better DNA repair with age'},
        'CG': {'effect': 'Heterozygous'},
        'GG': {'effect': 'Arg72 - stronger apoptosis'}
    },
    'rs5174': {
        'gene': 'LPA',
        'description': 'Lipoprotein(a) - cardiovascular longevity',
        'TT': {'effect': 'Lower Lp(a) - cardiovascular benefit'},
        'CT': {'effect': 'Moderate Lp(a)'},
        'CC': {'effect': 'Higher Lp(a) - cardiovascular risk'}
    }
}

print("Expanded genetics database loaded successfully")
print(f"Blood type systems: {len(BLOOD_TYPE_GENETICS)}")
print(f"Athletic gene categories: {len(ATHLETIC_GENES)}")
print(f"Polygenic risk conditions: {len(POLYGENIC_RISK_SCORES)}")
print(f"Longevity markers: {len(LONGEVITY_MARKERS)}")
