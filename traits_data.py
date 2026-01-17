"""
Physical and Health Traits Data
Contains marker definitions for trait predictions
"""

# Physical Trait Markers
PHYSICAL_TRAIT_MARKERS = {
    'eye_color': {
        'weights': {
            'rs12913832': 0.6,  # HERC2 - strongest predictor
            'rs1800407': 0.25,  # OCA2
            'rs1393350': 0.15   # TYR
        },
        'genotypes': {
            'rs12913832': {
                'GG': {'blue': 0.90, 'green': 0.05, 'brown': 0.05},
                'AG': {'blue': 0.60, 'green': 0.25, 'brown': 0.15},
                'AA': {'blue': 0.05, 'green': 0.15, 'brown': 0.80}
            },
            'rs1800407': {
                'TT': {'blue': 0.70, 'green': 0.20, 'brown': 0.10},
                'CT': {'blue': 0.40, 'green': 0.30, 'brown': 0.30},
                'CC': {'blue': 0.15, 'green': 0.25, 'brown': 0.60}
            },
            'rs1393350': {
                'GG': {'blue': 0.50, 'green': 0.30, 'brown': 0.20},
                'AG': {'blue': 0.30, 'green': 0.35, 'brown': 0.35},
                'AA': {'blue': 0.10, 'green': 0.20, 'brown': 0.70}
            }
        }
    },

    'hair_color': {
        'weights': {
            'rs1805007': 0.4,   # MC1R - major red hair gene
            'rs1805008': 0.3,   # MC1R variant
            'rs16891982': 0.2,  # SLC45A2
            'rs1426654': 0.1    # SLC24A5
        },
        'genotypes': {
            'rs1805007': {
                'TT': {'red': 0.90, 'blonde': 0.05, 'brown': 0.03, 'black': 0.02},
                'CT': {'red': 0.20, 'blonde': 0.30, 'brown': 0.40, 'black': 0.10},
                'CC': {'red': 0.02, 'blonde': 0.15, 'brown': 0.50, 'black': 0.33}
            },
            'rs1805008': {
                'TT': {'red': 0.85, 'blonde': 0.10, 'brown': 0.05, 'black': 0.00},
                'CT': {'red': 0.15, 'blonde': 0.35, 'brown': 0.40, 'black': 0.10},
                'CC': {'red': 0.01, 'blonde': 0.20, 'brown': 0.49, 'black': 0.30}
            },
            'rs16891982': {
                'GG': {'red': 0.05, 'blonde': 0.50, 'brown': 0.35, 'black': 0.10},
                'CG': {'red': 0.03, 'blonde': 0.30, 'brown': 0.50, 'black': 0.17},
                'CC': {'red': 0.01, 'blonde': 0.10, 'brown': 0.40, 'black': 0.49}
            },
            'rs1426654': {
                'GG': {'red': 0.02, 'blonde': 0.40, 'brown': 0.45, 'black': 0.13},
                'AG': {'red': 0.02, 'blonde': 0.25, 'brown': 0.55, 'black': 0.18},
                'AA': {'red': 0.01, 'blonde': 0.05, 'brown': 0.45, 'black': 0.49}
            }
        }
    },

    'hair_texture': {
        'weights': {
            'rs3827760': 0.7,   # EDAR - major predictor
            'rs260690': 0.3    # WNT10A
        },
        'genotypes': {
            'rs3827760': {
                'GG': {'straight_thick': 0.80, 'straight': 0.10, 'wavy': 0.08, 'curly': 0.02},
                'AG': {'straight_thick': 0.40, 'straight': 0.20, 'wavy': 0.30, 'curly': 0.10},
                'AA': {'straight_thick': 0.10, 'straight': 0.15, 'wavy': 0.30, 'curly': 0.45}
            },
            'rs260690': {
                'TT': {'straight_thick': 0.30, 'straight': 0.40, 'wavy': 0.25, 'curly': 0.05},
                'CT': {'straight_thick': 0.20, 'straight': 0.25, 'wavy': 0.40, 'curly': 0.15},
                'CC': {'straight_thick': 0.10, 'straight': 0.10, 'wavy': 0.35, 'curly': 0.45}
            }
        }
    },

    'skin_pigmentation': {
        'weights': {
            'rs1426654': 0.5,   # SLC24A5 - major European lightening
            'rs16891982': 0.3,  # SLC45A2
            'rs1805007': 0.2    # MC1R
        },
        'genotypes': {
            'rs1426654': {
                'GG': {'very_light': 0.80, 'light': 0.15, 'medium': 0.04, 'dark': 0.01},
                'AG': {'very_light': 0.40, 'light': 0.40, 'medium': 0.15, 'dark': 0.05},
                'AA': {'very_light': 0.05, 'light': 0.15, 'medium': 0.40, 'dark': 0.40}
            },
            'rs16891982': {
                'GG': {'very_light': 0.70, 'light': 0.25, 'medium': 0.04, 'dark': 0.01},
                'CG': {'very_light': 0.35, 'light': 0.45, 'medium': 0.15, 'dark': 0.05},
                'CC': {'very_light': 0.10, 'light': 0.25, 'medium': 0.40, 'dark': 0.25}
            },
            'rs1805007': {
                'TT': {'very_light': 0.95, 'light': 0.05, 'medium': 0.00, 'dark': 0.00},
                'CT': {'very_light': 0.60, 'light': 0.30, 'medium': 0.08, 'dark': 0.02},
                'CC': {'very_light': 0.30, 'light': 0.35, 'medium': 0.25, 'dark': 0.10}
            }
        }
    },

    'freckles': {
        'weights': {
            'rs1805007': 0.6,   # MC1R
            'rs1805008': 0.4    # MC1R variant
        },
        'genotypes': {
            'rs1805007': {
                'TT': {'many_freckles': 0.90, 'some_freckles': 0.08, 'no_freckles': 0.02},
                'CT': {'many_freckles': 0.40, 'some_freckles': 0.35, 'no_freckles': 0.25},
                'CC': {'many_freckles': 0.10, 'some_freckles': 0.25, 'no_freckles': 0.65}
            },
            'rs1805008': {
                'TT': {'many_freckles': 0.85, 'some_freckles': 0.10, 'no_freckles': 0.05},
                'CT': {'many_freckles': 0.35, 'some_freckles': 0.40, 'no_freckles': 0.25},
                'CC': {'many_freckles': 0.08, 'some_freckles': 0.27, 'no_freckles': 0.65}
            }
        }
    }
}

# Health Trait Markers
HEALTH_TRAIT_MARKERS = {
    # Metabolism & Diet
    'Lactose Tolerance': {
        'rs4988235': {
            'AA': {'result': 'Lactose intolerant', 'confidence': 'High'},
            'AG': {'result': 'Some lactose tolerance', 'confidence': 'Medium'},
            'GG': {'result': 'Lactose tolerant', 'confidence': 'High'}
        }
    },

    'Caffeine Metabolism': {
        'rs762551': {
            'AA': {'result': 'Fast caffeine metabolizer', 'confidence': 'High'},
            'AC': {'result': 'Average caffeine metabolism', 'confidence': 'Medium'},
            'CC': {'result': 'Slow caffeine metabolizer', 'confidence': 'High'}
        }
    },

    'Alcohol Flush Reaction': {
        'rs671': {
            'GG': {'result': 'Normal alcohol metabolism', 'confidence': 'High'},
            'AG': {'result': 'Moderate alcohol flush', 'confidence': 'High'},
            'AA': {'result': 'Strong alcohol flush reaction', 'confidence': 'High'}
        }
    },

    'Bitter Taste Perception': {
        'rs713598': {
            'CC': {'result': 'Can taste bitter (PTC/PROP)', 'confidence': 'High'},
            'CG': {'result': 'Moderate bitter taste sensitivity', 'confidence': 'Medium'},
            'GG': {'result': 'Cannot taste bitter compounds', 'confidence': 'High'}
        }
    },

    # Athletic Performance
    'Muscle Type': {
        'rs1815739': {
            'CC': {'result': 'Power/Sprint muscle type', 'confidence': 'High'},
            'CT': {'result': 'Mixed muscle type', 'confidence': 'Medium'},
            'TT': {'result': 'Endurance muscle type', 'confidence': 'High'}
        }
    },

    # Cardiovascular
    'Heart Disease Risk': {
        'rs11591147': {
            'GG': {'result': 'Average risk', 'confidence': 'Medium'},
            'GT': {'result': 'Reduced risk (~15%)', 'confidence': 'High'},
            'TT': {'result': 'Significantly reduced risk (~28%)', 'confidence': 'High'}
        }
    },

    'Blood Pressure Sensitivity': {
        'rs4961': {
            'CC': {'result': 'Salt-sensitive blood pressure', 'confidence': 'Medium'},
            'CT': {'result': 'Moderate salt sensitivity', 'confidence': 'Medium'},
            'TT': {'result': 'Low salt sensitivity', 'confidence': 'Medium'}
        }
    },

    # Diabetes
    'Type 2 Diabetes Risk': {
        'rs7903146': {
            'CC': {'result': 'Lower diabetes risk', 'confidence': 'High'},
            'CT': {'result': 'Increased risk (~45%)', 'confidence': 'High'},
            'TT': {'result': 'Higher risk (~80%)', 'confidence': 'High'}
        }
    },

    # Brain Health
    'Alzheimer Disease Risk': {
        'rs429358': {
            'CC': {'result': 'Lower AD risk', 'confidence': 'High'},
            'CT': {'result': 'Average AD risk', 'confidence': 'High'},
            'TT': {'result': 'Increased AD risk (APOE4)', 'confidence': 'High'}
        }
    },

    # Blood Clotting
    'Factor V Leiden': {
        'rs6025': {
            'GG': {'result': 'Normal clotting factor', 'confidence': 'High'},
            'AG': {'result': 'Increased clotting risk (3-8x)', 'confidence': 'High'},
            'AA': {'result': 'High clotting risk (50-80x)', 'confidence': 'High'}
        }
    },

    # Folate Metabolism
    'MTHFR Mutation': {
        'rs1801133': {
            'CC': {'result': 'Normal folate metabolism', 'confidence': 'High'},
            'CT': {'result': 'Reduced folate efficiency (~35%)', 'confidence': 'High'},
            'TT': {'result': 'Significantly reduced (~70%)', 'confidence': 'High'}
        }
    },

    # Iron Metabolism
    'Hemochromatosis Risk': {
        'rs1800562': {
            'GG': {'result': 'Normal iron metabolism', 'confidence': 'High'},
            'AG': {'result': 'Iron overload carrier', 'confidence': 'High'},
            'AA': {'result': 'Hemochromatosis risk (~90%)', 'confidence': 'High'}
        }
    },

    # Eye Health
    'Macular Degeneration Risk': {
        'rs1061170': {
            'CC': {'result': 'Lower AMD risk', 'confidence': 'High'},
            'CT': {'result': 'Moderate AMD risk (2.5x)', 'confidence': 'High'},
            'TT': {'result': 'Higher AMD risk (5.5x)', 'confidence': 'High'}
        }
    },

    # Respiratory
    'Asthma Risk': {
        'rs7216389': {
            'CC': {'result': 'Lower asthma risk', 'confidence': 'Medium'},
            'CT': {'result': 'Moderate asthma risk', 'confidence': 'Medium'},
            'TT': {'result': 'Higher asthma risk', 'confidence': 'High'}
        }
    },

    # Sleep
    'Chronotype': {
        'rs9565309': {
            'AA': {'result': 'Morning person tendency', 'confidence': 'Low'},
            'AT': {'result': 'Flexible sleep pattern', 'confidence': 'Low'},
            'TT': {'result': 'Night owl tendency', 'confidence': 'Low'}
        }
    },

    # Vitamin D
    'Vitamin D Levels': {
        'rs12794714': {
            'AA': {'result': 'Normal vitamin D levels', 'confidence': 'Medium'},
            'AG': {'result': 'Slightly lower vitamin D', 'confidence': 'Low'},
            'GG': {'result': 'Lower vitamin D tendency', 'confidence': 'Medium'}
        }
    },

    # Earwax Type
    'Earwax Type': {
        'rs17822931': {
            'CC': {'result': 'Wet earwax', 'confidence': 'High'},
            'CT': {'result': 'Wet earwax', 'confidence': 'High'},
            'TT': {'result': 'Dry earwax', 'confidence': 'High'}
        }
    },

    # Asparagus Smell
    'Asparagus Odor Detection': {
        'rs4481887': {
            'AA': {'result': 'Can smell asparagus metabolites', 'confidence': 'High'},
            'AG': {'result': 'Moderate detection ability', 'confidence': 'Medium'},
            'GG': {'result': 'Cannot smell asparagus metabolites', 'confidence': 'High'}
        }
    }
}
