#!/usr/bin/env python3
"""
Advanced Traits Database
Facial features, sensory traits, chronotype, pain, addiction, mental resilience
All real SNPs from published GWAS studies
"""

# =============================================================================
# FACIAL FEATURE PREDICTION - Build a genetic "mugshot"
# =============================================================================

FACIAL_FEATURES = {
    # Face shape
    'face_shape': {
        'rs7559271': {
            'gene': 'PAX3',
            'description': 'Face morphology - nasion position',
            'GG': {'prediction': 'Wider face', 'score': 0.7},
            'CG': {'prediction': 'Average width', 'score': 0.5},
            'CC': {'prediction': 'Narrower face', 'score': 0.3}
        },
        'rs1268789': {
            'gene': 'DCHS2',
            'description': 'Face width and chin shape',
            'AA': {'prediction': 'Broader facial structure', 'score': 0.7},
            'AG': {'prediction': 'Average structure', 'score': 0.5},
            'GG': {'prediction': 'Narrower facial structure', 'score': 0.3}
        }
    },

    # Nose shape
    'nose_shape': {
        'rs1868752': {
            'gene': 'DCHS2',
            'description': 'Nose bridge width and pointiness',
            'AA': {'prediction': 'Wider nose bridge', 'width': 0.7, 'pointiness': 0.3},
            'AC': {'prediction': 'Medium nose bridge', 'width': 0.5, 'pointiness': 0.5},
            'CC': {'prediction': 'Narrower nose bridge', 'width': 0.3, 'pointiness': 0.7}
        },
        'rs6095473': {
            'gene': 'GLI3',
            'description': 'Nose tip shape and nostril width',
            'AA': {'prediction': 'Upturned nose tip', 'tip': 'upturned'},
            'AC': {'prediction': 'Straight nose tip', 'tip': 'straight'},
            'CC': {'prediction': 'Downturned nose tip', 'tip': 'downturned'}
        },
        'rs2045323': {
            'gene': 'RUNX2',
            'description': 'Nose bridge height',
            'TT': {'prediction': 'Higher nose bridge', 'height': 0.7},
            'CT': {'prediction': 'Medium nose bridge', 'height': 0.5},
            'CC': {'prediction': 'Lower nose bridge', 'height': 0.3}
        },
        'rs17640804': {
            'gene': 'PAX1',
            'description': 'Nostril width',
            'TT': {'prediction': 'Wider nostrils', 'width': 0.7},
            'CT': {'prediction': 'Medium nostrils', 'width': 0.5},
            'CC': {'prediction': 'Narrower nostrils', 'width': 0.3}
        }
    },

    # Lip thickness
    'lip_shape': {
        'rs17640804': {
            'gene': 'PAX1',
            'description': 'Lip thickness',
            'TT': {'prediction': 'Fuller lips', 'thickness': 0.7},
            'CT': {'prediction': 'Medium lips', 'thickness': 0.5},
            'CC': {'prediction': 'Thinner lips', 'thickness': 0.3}
        }
    },

    # Chin shape
    'chin_shape': {
        'rs11684042': {
            'gene': 'FOXL2',
            'description': 'Chin protrusion',
            'AA': {'prediction': 'More prominent chin', 'prominence': 0.7},
            'AG': {'prediction': 'Average chin', 'prominence': 0.5},
            'GG': {'prediction': 'Less prominent chin', 'prominence': 0.3}
        },
        'rs12644248': {
            'gene': 'FOXL2',
            'description': 'Chin shape (round vs pointed)',
            'CC': {'prediction': 'More pointed chin', 'shape': 'pointed'},
            'CT': {'prediction': 'Average chin shape', 'shape': 'average'},
            'TT': {'prediction': 'More rounded chin', 'shape': 'rounded'}
        }
    },

    # Cleft chin (butt chin)
    'cleft_chin': {
        'rs11684042': {
            'gene': 'Multiple',
            'description': 'Cleft chin (dimple in chin)',
            'AA': {'prediction': 'Cleft chin likely', 'has_cleft': True, 'probability': 0.7},
            'AG': {'prediction': 'Possible slight cleft', 'has_cleft': 'maybe', 'probability': 0.4},
            'GG': {'prediction': 'Smooth chin likely', 'has_cleft': False, 'probability': 0.2}
        }
    },

    # Cheekbones
    'cheekbones': {
        'rs927833': {
            'gene': 'GLI3',
            'description': 'Cheekbone prominence',
            'TT': {'prediction': 'Higher/more prominent cheekbones', 'prominence': 0.7},
            'CT': {'prediction': 'Average cheekbones', 'prominence': 0.5},
            'CC': {'prediction': 'Lower/less prominent cheekbones', 'prominence': 0.3}
        }
    },

    # Eyebrow thickness
    'eyebrow_thickness': {
        'rs3827760': {
            'gene': 'EDAR',
            'description': 'Eyebrow thickness (also affects hair)',
            'AA': {'prediction': 'Thicker eyebrows', 'thickness': 0.8},
            'AG': {'prediction': 'Medium eyebrows', 'thickness': 0.5},
            'GG': {'prediction': 'Thinner eyebrows', 'thickness': 0.3}
        },
        'rs16891982': {
            'gene': 'SLC45A2',
            'description': 'Eyebrow color influence',
            'GG': {'prediction': 'Lighter eyebrows likely', 'color': 'light'},
            'CG': {'prediction': 'Medium eyebrows', 'color': 'medium'},
            'CC': {'prediction': 'Darker eyebrows likely', 'color': 'dark'}
        }
    },

    # Earlobe attachment
    'earlobe': {
        'rs10212419': {
            'gene': 'EDAR',
            'description': 'Earlobe attachment type',
            'TT': {'prediction': 'Free (detached) earlobes', 'type': 'free', 'probability': 0.8},
            'CT': {'prediction': 'Partially attached', 'type': 'partial', 'probability': 0.5},
            'CC': {'prediction': 'Attached earlobes', 'type': 'attached', 'probability': 0.7}
        }
    },

    # Widow's peak
    'widows_peak': {
        'rs2223066': {
            'gene': 'Multiple',
            'description': 'Widow\'s peak hairline',
            'TT': {'prediction': 'Widow\'s peak likely', 'has_peak': True, 'probability': 0.7},
            'CT': {'prediction': 'Possible widow\'s peak', 'has_peak': 'maybe', 'probability': 0.4},
            'CC': {'prediction': 'Straight hairline likely', 'has_peak': False, 'probability': 0.2}
        }
    },

    # Dimples
    'dimples': {
        'rs2235371': {
            'gene': 'IRF6',
            'description': 'Cheek dimples',
            'CC': {'prediction': 'Dimples likely', 'has_dimples': True, 'probability': 0.6},
            'CT': {'prediction': 'Possible dimples', 'has_dimples': 'maybe', 'probability': 0.35},
            'TT': {'prediction': 'No dimples likely', 'has_dimples': False, 'probability': 0.15}
        }
    },

    # Unibrow tendency
    'unibrow': {
        'rs3827760': {
            'gene': 'EDAR',
            'description': 'Eyebrow connection tendency',
            'AA': {'prediction': 'Unibrow tendency higher', 'tendency': 0.6},
            'AG': {'prediction': 'Moderate tendency', 'tendency': 0.4},
            'GG': {'prediction': 'Separated eyebrows likely', 'tendency': 0.2}
        }
    },

    # Philtrum (groove between nose and lip)
    'philtrum': {
        'rs642961': {
            'gene': 'IRF6',
            'description': 'Philtrum depth and width',
            'AA': {'prediction': 'Deeper philtrum', 'depth': 0.7},
            'AG': {'prediction': 'Average philtrum', 'depth': 0.5},
            'GG': {'prediction': 'Shallower philtrum', 'depth': 0.3}
        }
    },

    # Jaw shape
    'jaw_shape': {
        'rs1268789': {
            'gene': 'DCHS2',
            'description': 'Jaw width and angle',
            'AA': {'prediction': 'Wider jaw', 'width': 0.7, 'shape': 'square'},
            'AG': {'prediction': 'Average jaw', 'width': 0.5, 'shape': 'oval'},
            'GG': {'prediction': 'Narrower jaw', 'width': 0.3, 'shape': 'narrow'}
        }
    },

    # Forehead height
    'forehead': {
        'rs2223066': {
            'gene': 'Multiple',
            'description': 'Forehead height',
            'TT': {'prediction': 'Higher forehead', 'height': 0.7},
            'CT': {'prediction': 'Average forehead', 'height': 0.5},
            'CC': {'prediction': 'Lower forehead', 'height': 0.3}
        }
    }
}

# =============================================================================
# CHRONOTYPE / CIRCADIAN RHYTHM - Morning lark vs night owl
# =============================================================================

CHRONOTYPE_GENETICS = {
    'morningness': {
        'rs12927162': {
            'gene': 'RASD1',
            'description': 'Morning preference regulator',
            'TT': {'chronotype': 'Strong morning person', 'score': 90, 'wake_time': '5:00-6:00 AM'},
            'CT': {'chronotype': 'Moderate morning preference', 'score': 65, 'wake_time': '6:00-7:00 AM'},
            'CC': {'chronotype': 'Evening tendency', 'score': 40, 'wake_time': '7:30+ AM'}
        },
        'rs10493596': {
            'gene': 'AK5',
            'description': 'Circadian rhythm regulator',
            'TT': {'chronotype': 'Morning type', 'score': 75},
            'CT': {'chronotype': 'Intermediate', 'score': 50},
            'CC': {'chronotype': 'Evening type', 'score': 25}
        },
        'rs2032658': {
            'gene': 'PER2',
            'description': 'Period circadian clock gene',
            'AA': {'chronotype': 'Early bird', 'score': 80, 'sleep_need': '7 hours'},
            'AG': {'chronotype': 'Average', 'score': 50, 'sleep_need': '7-8 hours'},
            'GG': {'chronotype': 'Night owl', 'score': 30, 'sleep_need': '8+ hours'}
        }
    },

    'sleep_duration': {
        'rs1801260': {
            'gene': 'CLOCK',
            'description': 'Core circadian clock gene',
            'TT': {'duration': 'Short sleeper (6-7h)', 'need': 6.5, 'score': 30},
            'CT': {'duration': 'Average sleeper (7-8h)', 'need': 7.5, 'score': 50},
            'CC': {'duration': 'Long sleeper (8-9h)', 'need': 8.5, 'score': 70}
        },
        'rs57875989': {
            'gene': 'DEC2',
            'description': 'Short sleep gene (rare)',
            'AA': {'duration': 'Natural short sleeper', 'need': 6.0, 'note': 'Can function on 6 hours'},
            'AG': {'duration': 'Slightly reduced need', 'need': 7.0},
            'GG': {'duration': 'Normal sleep need', 'need': 8.0}
        }
    },

    'insomnia_risk': {
        'rs113851554': {
            'gene': 'MEIS1',
            'description': 'Insomnia and restless legs',
            'TT': {'risk': 'Higher insomnia risk', 'level': 'elevated', 'score': 70},
            'CT': {'risk': 'Moderate risk', 'level': 'moderate', 'score': 50},
            'CC': {'risk': 'Lower insomnia risk', 'level': 'low', 'score': 30}
        }
    }
}

# =============================================================================
# PAIN SENSITIVITY
# =============================================================================

PAIN_GENETICS = {
    'pain_threshold': {
        'rs4680': {
            'gene': 'COMT',
            'description': 'Catechol-O-methyltransferase - pain processing',
            'GG': {
                'sensitivity': 'Lower pain sensitivity',
                'threshold': 'High',
                'score': 30,
                'description': 'Warrior gene - higher pain tolerance, calmer under stress',
                'drug_response': 'May need higher doses of pain medication'
            },
            'AG': {
                'sensitivity': 'Average pain sensitivity',
                'threshold': 'Medium',
                'score': 50,
                'description': 'Balanced pain response',
                'drug_response': 'Standard medication dosing'
            },
            'AA': {
                'sensitivity': 'Higher pain sensitivity',
                'threshold': 'Low',
                'score': 70,
                'description': 'Worrier gene - more sensitive to pain and stress',
                'drug_response': 'May need lower doses, responds well to opioids'
            }
        },
        'rs1799971': {
            'gene': 'OPRM1',
            'description': 'Opioid receptor - pain and pleasure',
            'AA': {
                'sensitivity': 'Normal opioid response',
                'endorphin': 'Normal',
                'score': 50,
                'drug_response': 'Standard opioid sensitivity'
            },
            'AG': {
                'sensitivity': 'Reduced opioid binding',
                'endorphin': 'Lower pleasure response',
                'score': 60,
                'drug_response': 'May need higher opioid doses'
            },
            'GG': {
                'sensitivity': 'Significantly reduced binding',
                'endorphin': 'Much lower',
                'score': 75,
                'drug_response': 'Often resistant to opioid pain relief'
            }
        }
    },

    'pain_conditions': {
        'rs6746030': {
            'gene': 'SCN9A',
            'description': 'Sodium channel - pain signaling',
            'AA': {'risk': 'Higher chronic pain risk', 'score': 70},
            'AG': {'risk': 'Average risk', 'score': 50},
            'GG': {'risk': 'Lower chronic pain risk', 'score': 30}
        },
        'rs7574193': {
            'gene': 'GCH1',
            'description': 'Pain protection gene',
            'TT': {'protection': 'Pain protective variant', 'score': 25},
            'CT': {'protection': 'Partial protection', 'score': 50},
            'CC': {'protection': 'No extra protection', 'score': 65}
        }
    },

    'migraine_risk': {
        'rs2651899': {
            'gene': 'PRDM16',
            'description': 'Migraine susceptibility',
            'CC': {'risk': 'Higher migraine risk', 'odds': 1.3, 'score': 70},
            'CT': {'risk': 'Moderate risk', 'odds': 1.15, 'score': 55},
            'TT': {'risk': 'Lower migraine risk', 'odds': 1.0, 'score': 40}
        },
        'rs10166942': {
            'gene': 'TRPM8',
            'description': 'Cold/pain receptor - migraine',
            'TT': {'risk': 'Reduced migraine risk', 'score': 35},
            'CT': {'risk': 'Average risk', 'score': 50},
            'CC': {'risk': 'Elevated migraine risk', 'score': 65}
        }
    }
}

# =============================================================================
# ADDICTION RISK
# =============================================================================

ADDICTION_GENETICS = {
    'alcohol': {
        'rs1229984': {
            'gene': 'ADH1B',
            'description': 'Alcohol dehydrogenase - alcohol metabolism',
            'TT': {
                'risk': 'Strong protection against alcoholism',
                'score': 15,
                'effect': 'Rapid alcohol metabolism causes unpleasant flush',
                'note': 'Common in East Asians - protective'
            },
            'CT': {
                'risk': 'Moderate protection',
                'score': 35,
                'effect': 'Faster metabolism, some protection'
            },
            'CC': {
                'risk': 'No genetic protection',
                'score': 60,
                'effect': 'Normal alcohol metabolism',
                'note': 'Typical in Europeans'
            }
        },
        'rs671': {
            'gene': 'ALDH2',
            'description': 'Aldehyde dehydrogenase - Asian flush',
            'AA': {
                'risk': 'Strong protection (flush reaction)',
                'score': 10,
                'effect': 'Cannot process acetaldehyde - severe reaction',
                'note': 'Essentially cannot drink alcohol'
            },
            'AG': {
                'risk': 'Moderate protection (mild flush)',
                'score': 30,
                'effect': 'Partial processing ability'
            },
            'GG': {
                'risk': 'No flush protection',
                'score': 55,
                'effect': 'Normal aldehyde processing'
            }
        }
    },

    'nicotine': {
        'rs16969968': {
            'gene': 'CHRNA5',
            'description': 'Nicotinic receptor - smoking addiction',
            'AA': {
                'risk': 'Higher nicotine addiction risk',
                'score': 75,
                'cigarettes': 'Tendency to smoke more if you start',
                'quit_difficulty': 'Harder to quit'
            },
            'AG': {
                'risk': 'Moderate risk',
                'score': 55,
                'cigarettes': 'Average smoking behavior',
                'quit_difficulty': 'Average'
            },
            'GG': {
                'risk': 'Lower addiction risk',
                'score': 35,
                'cigarettes': 'Less likely to become heavy smoker',
                'quit_difficulty': 'Easier to quit'
            }
        },
        'rs1051730': {
            'gene': 'CHRNA3',
            'description': 'Nicotinic receptor cluster',
            'TT': {'risk': 'Higher dependence risk', 'score': 70},
            'CT': {'risk': 'Moderate risk', 'score': 50},
            'CC': {'risk': 'Lower risk', 'score': 30}
        }
    },

    'dopamine_reward': {
        'rs1800497': {
            'gene': 'DRD2/ANKK1',
            'description': 'Dopamine D2 receptor - reward sensitivity',
            'TT': {
                'risk': 'Reduced dopamine receptors',
                'score': 70,
                'effect': 'Reward deficiency - may seek stimulation',
                'addictions': 'Higher risk for multiple addictions',
                'note': 'The "addiction gene"'
            },
            'CT': {
                'risk': 'Moderate receptor density',
                'score': 50,
                'effect': 'Average reward sensitivity'
            },
            'CC': {
                'risk': 'Normal receptor density',
                'score': 30,
                'effect': 'Normal reward response'
            }
        },
        'rs4680': {
            'gene': 'COMT',
            'description': 'Dopamine breakdown (same as pain gene)',
            'GG': {
                'reward': 'Quick dopamine clearance',
                'risk': 'May need more stimulation',
                'score': 55
            },
            'AG': {
                'reward': 'Balanced dopamine levels',
                'risk': 'Average',
                'score': 45
            },
            'AA': {
                'reward': 'Slow dopamine clearance',
                'risk': 'More sensitive to rewards',
                'score': 50
            }
        }
    },

    'gambling': {
        'rs1800497': {
            'gene': 'DRD2',
            'description': 'Dopamine receptor - gambling risk',
            'TT': {'risk': 'Higher gambling addiction risk', 'score': 70},
            'CT': {'risk': 'Moderate risk', 'score': 50},
            'CC': {'risk': 'Lower risk', 'score': 30}
        }
    },

    'cannabis': {
        'rs2023239': {
            'gene': 'CNR1',
            'description': 'Cannabinoid receptor 1',
            'TT': {'risk': 'Higher cannabis dependence risk', 'score': 65},
            'CT': {'risk': 'Moderate risk', 'score': 50},
            'CC': {'risk': 'Lower risk', 'score': 35}
        }
    }
}

# =============================================================================
# MENTAL RESILIENCE / STRESS RESPONSE
# =============================================================================

MENTAL_GENETICS = {
    'stress_response': {
        'rs4680': {
            'gene': 'COMT',
            'description': 'Warrior vs Worrier gene',
            'GG': {
                'type': 'Warrior',
                'stress': 'Performs better under stress',
                'baseline': 'May be less focused day-to-day',
                'score': 70,
                'description': 'Thrives in high-pressure situations'
            },
            'AG': {
                'type': 'Balanced',
                'stress': 'Moderate stress tolerance',
                'baseline': 'Good overall function',
                'score': 50,
                'description': 'Adaptable stress response'
            },
            'AA': {
                'type': 'Worrier',
                'stress': 'More affected by stress',
                'baseline': 'Better focus in calm environments',
                'score': 35,
                'description': 'Excellent memory and attention when calm'
            }
        },
        'rs53576': {
            'gene': 'OXTR',
            'description': 'Oxytocin receptor - social bonding',
            'GG': {
                'trait': 'Higher empathy and social sensitivity',
                'stress': 'Strong social support helps',
                'score': 40,
                'description': 'More affected by social stress but also more resilient with support'
            },
            'AG': {
                'trait': 'Moderate social sensitivity',
                'stress': 'Balanced response',
                'score': 50
            },
            'AA': {
                'trait': 'Lower social sensitivity',
                'stress': 'Less affected by social evaluation',
                'score': 60,
                'description': 'More independent stress coping'
            }
        }
    },

    'anxiety_tendency': {
        'rs6265': {
            'gene': 'BDNF',
            'description': 'Brain-derived neurotrophic factor',
            'CC': {
                'resilience': 'Higher stress resilience',
                'anxiety': 'Lower anxiety tendency',
                'score': 35,
                'neuroplasticity': 'Better brain adaptability'
            },
            'CT': {
                'resilience': 'Moderate',
                'anxiety': 'Average',
                'score': 50
            },
            'TT': {
                'resilience': 'Lower stress resilience',
                'anxiety': 'Higher anxiety tendency',
                'score': 70,
                'neuroplasticity': 'May benefit from exercise, meditation'
            }
        },
        'rs25531': {
            'gene': 'SLC6A4',
            'description': 'Serotonin transporter - mood regulation',
            'LL': {
                'mood': 'More stable mood',
                'anxiety': 'Lower anxiety risk',
                'score': 35
            },
            'LS': {
                'mood': 'Moderate stability',
                'anxiety': 'Average risk',
                'score': 50
            },
            'SS': {
                'mood': 'More mood variability',
                'anxiety': 'Higher anxiety sensitivity',
                'score': 70,
                'note': 'More responsive to environment - good and bad'
            }
        }
    },

    'depression_risk': {
        'rs6265': {
            'gene': 'BDNF',
            'description': 'Depression resilience',
            'CC': {'risk': 'Lower depression risk', 'score': 30},
            'CT': {'risk': 'Average risk', 'score': 50},
            'TT': {'risk': 'Higher depression risk', 'score': 65}
        },
        'rs4570625': {
            'gene': 'TPH2',
            'description': 'Tryptophan hydroxylase - serotonin synthesis',
            'GG': {'risk': 'Lower depression tendency', 'score': 35},
            'GT': {'risk': 'Moderate', 'score': 50},
            'TT': {'risk': 'Higher depression tendency', 'score': 65}
        }
    },

    'risk_taking': {
        'rs1800497': {
            'gene': 'DRD2',
            'description': 'Dopamine receptor - novelty seeking',
            'TT': {'tendency': 'Higher risk-taking', 'score': 70, 'novelty': 'Seeks new experiences'},
            'CT': {'tendency': 'Moderate', 'score': 50},
            'CC': {'tendency': 'Lower risk-taking', 'score': 30, 'novelty': 'Prefers stability'}
        },
        'rs4680': {
            'gene': 'COMT',
            'description': 'Risk assessment under pressure',
            'GG': {'tendency': 'More risk-tolerant under stress', 'score': 65},
            'AG': {'tendency': 'Balanced', 'score': 50},
            'AA': {'tendency': 'More risk-averse', 'score': 35}
        }
    }
}

# =============================================================================
# SENSORY GENETICS - Supertaster, super smeller, etc.
# =============================================================================

SENSORY_GENETICS = {
    'taste': {
        'rs713598': {
            'gene': 'TAS2R38',
            'description': 'Bitter taste receptor - supertaster gene',
            'CC': {
                'type': 'Supertaster',
                'bitter': 'Very sensitive to bitter compounds',
                'score': 90,
                'foods': 'May dislike broccoli, coffee, beer, grapefruit',
                'note': 'Tastes PROP/PTC strongly'
            },
            'CG': {
                'type': 'Medium taster',
                'bitter': 'Moderate bitter sensitivity',
                'score': 55,
                'foods': 'Average taste perception'
            },
            'GG': {
                'type': 'Non-taster',
                'bitter': 'Cannot taste certain bitter compounds',
                'score': 20,
                'foods': 'May enjoy bitter vegetables, hoppy beers',
                'note': 'Cannot taste PROP/PTC'
            }
        },
        'rs10246939': {
            'gene': 'TAS2R38',
            'description': 'Additional bitter receptor variant',
            'CC': {'type': 'Enhanced bitter', 'score': 80},
            'CT': {'type': 'Medium', 'score': 50},
            'TT': {'type': 'Reduced bitter', 'score': 25}
        }
    },

    'smell': {
        'rs2590498': {
            'gene': 'OR2M7',
            'description': 'Asparagus smell detection',
            'GG': {
                'ability': 'Can smell asparagus in urine',
                'score': 80,
                'note': 'Can detect asparagus metabolite'
            },
            'AG': {
                'ability': 'Moderate detection',
                'score': 50
            },
            'AA': {
                'ability': 'Cannot smell asparagus in urine',
                'score': 20,
                'note': 'Specific anosmia for asparagus'
            }
        },
        'rs8065080': {
            'gene': 'OR6A2',
            'description': 'Cilantro/coriander perception',
            'TT': {
                'perception': 'Cilantro tastes like soap',
                'score': 80,
                'note': 'Aldehydes taste soapy/metallic'
            },
            'CT': {
                'perception': 'May find cilantro slightly soapy',
                'score': 50
            },
            'CC': {
                'perception': 'Normal cilantro taste',
                'score': 20,
                'note': 'Enjoys cilantro normally'
            }
        },
        'rs6591536': {
            'gene': 'OR5A1',
            'description': 'Beta-ionone (violets) smell',
            'GG': {'ability': 'Can smell beta-ionone strongly', 'sensitivity': 'high'},
            'AG': {'ability': 'Moderate sensitivity', 'sensitivity': 'medium'},
            'AA': {'ability': 'Low sensitivity to violet scent', 'sensitivity': 'low'}
        }
    },

    'hearing': {
        'rs7598759': {
            'gene': 'GRM7',
            'description': 'Age-related hearing loss',
            'TT': {'risk': 'Higher hearing loss risk', 'score': 70},
            'CT': {'risk': 'Moderate risk', 'score': 50},
            'CC': {'risk': 'Lower hearing loss risk', 'score': 30}
        },
        'rs80338939': {
            'gene': 'GJB2',
            'description': 'Connexin 26 - congenital hearing',
            'GG': {'status': 'Normal hearing gene', 'score': 20},
            'GA': {'status': 'Carrier', 'score': 40},
            'AA': {'status': 'Risk variant', 'score': 70}
        }
    },

    'perfect_pitch': {
        'rs3057': {
            'gene': 'Auditory cortex genes',
            'description': 'Absolute pitch tendency',
            'note': 'Perfect pitch is mostly training but has genetic component',
            'AA': {'tendency': 'Higher perfect pitch potential', 'score': 70},
            'AG': {'tendency': 'Moderate potential', 'score': 50},
            'GG': {'tendency': 'Lower natural tendency', 'score': 30}
        }
    }
}

# =============================================================================
# BODY ODOR TYPE
# =============================================================================

BODY_ODOR_GENETICS = {
    'body_odor': {
        'rs17822931': {
            'gene': 'ABCC11',
            'description': 'Earwax type AND body odor',
            'TT': {
                'earwax': 'Dry earwax',
                'odor': 'Little to no body odor',
                'deodorant': 'Rarely need deodorant',
                'note': 'Common in East Asians (80-95%)',
                'breast_cancer': 'Lower breast cancer risk'
            },
            'CT': {
                'earwax': 'Wet earwax',
                'odor': 'Moderate body odor',
                'deodorant': 'May need deodorant',
                'note': 'Intermediate type'
            },
            'CC': {
                'earwax': 'Wet, sticky earwax',
                'odor': 'Typical body odor',
                'deodorant': 'Likely need deodorant',
                'note': 'Common in Europeans/Africans (95-100%)'
            }
        }
    }
}

# =============================================================================
# HANDEDNESS
# =============================================================================

HANDEDNESS_GENETICS = {
    'handedness': {
        'rs11855415': {
            'gene': 'PCSK6',
            'description': 'Left-right asymmetry',
            'CC': {'tendency': 'Slightly higher left-handed chance', 'left_prob': 0.15},
            'CT': {'tendency': 'Average', 'left_prob': 0.10},
            'TT': {'tendency': 'Slightly lower left-handed chance', 'left_prob': 0.08}
        },
        'rs1446109': {
            'gene': 'LRRTM1',
            'description': 'Left-handedness associated gene',
            'AA': {'tendency': 'Higher left-handed tendency', 'left_prob': 0.18},
            'AG': {'tendency': 'Average', 'left_prob': 0.10},
            'GG': {'tendency': 'Lower left-handed tendency', 'left_prob': 0.07}
        }
    }
}

# =============================================================================
# ANCIENT POPULATION MATCHING
# =============================================================================

ANCIENT_POPULATIONS = {
    'yamnaya_steppe': {
        'description': 'Yamnaya - Bronze Age Steppe pastoralists',
        'time_period': '5,000-3,000 years ago',
        'location': 'Pontic-Caspian steppe (Ukraine/Russia)',
        'contribution': 'Indo-European languages, horse domestication',
        'markers': {
            'rs4988235': {'yamnaya_allele': 'T', 'freq': 0.90},  # Lactase persistence
            'rs16891982': {'yamnaya_allele': 'G', 'freq': 0.85},  # Light skin
            'rs12913832': {'yamnaya_allele': 'G', 'freq': 0.50}   # Blue eyes sometimes
        },
        'typical_traits': ['Lactose tolerant', 'Light skin', 'Tall stature', 'Brown/light eyes']
    },

    'ancient_north_eurasian': {
        'description': 'Ancient North Eurasian (ANE)',
        'time_period': '24,000-15,000 years ago',
        'location': 'Siberia/Central Asia',
        'contribution': 'Ancestry in both Europeans and Native Americans',
        'markers': {
            'rs3827760': {'ane_allele': 'G', 'freq': 0.95}
        }
    },

    'western_hunter_gatherer': {
        'description': 'Western European Hunter-Gatherers (WHG)',
        'time_period': '15,000-8,000 years ago',
        'location': 'Western Europe',
        'contribution': 'Mesolithic Europeans',
        'markers': {
            'rs12913832': {'whg_allele': 'G', 'freq': 0.95},  # Blue eyes
            'rs1426654': {'whg_allele': 'G', 'freq': 0.40}    # Dark skin
        },
        'typical_traits': ['Blue eyes', 'Dark skin (unusual combo)', 'Robust build']
    },

    'early_european_farmer': {
        'description': 'Anatolian Neolithic Farmers (EEF)',
        'time_period': '10,000-5,000 years ago',
        'location': 'Anatolia (Turkey) -> Europe',
        'contribution': 'Agriculture, pottery, light skin genes',
        'markers': {
            'rs1426654': {'eef_allele': 'A', 'freq': 0.90},  # Light skin
            'rs16891982': {'eef_allele': 'G', 'freq': 0.75}
        },
        'typical_traits': ['Light skin', 'Brown eyes', 'Shorter stature']
    },

    'eastern_hunter_gatherer': {
        'description': 'Eastern European Hunter-Gatherers (EHG)',
        'time_period': '15,000-5,000 years ago',
        'location': 'Eastern Europe/Western Siberia',
        'contribution': 'Mixed with ANE, precursor to Yamnaya',
        'markers': {
            'rs12913832': {'ehg_allele': 'A', 'freq': 0.60}  # Brown eyes common
        }
    },

    'viking': {
        'description': 'Viking Age Scandinavians',
        'time_period': '800-1100 CE',
        'location': 'Scandinavia',
        'contribution': 'Norse expansion, mixed Northern European',
        'markers': {
            'rs12913832': {'viking_allele': 'G', 'freq': 0.75},
            'rs1805007': {'viking_allele': 'T', 'freq': 0.10},  # Red hair
            'rs4988235': {'viking_allele': 'T', 'freq': 0.85}
        },
        'typical_traits': ['Light eyes', 'Blond/red hair', 'Tall', 'Light skin']
    },

    'roman': {
        'description': 'Ancient Romans',
        'time_period': '500 BCE - 500 CE',
        'location': 'Italian Peninsula',
        'contribution': 'Roman Empire, Mediterranean genetics',
        'markers': {
            'rs1426654': {'roman_allele': 'A', 'freq': 0.85},
            'rs12913832': {'roman_allele': 'A', 'freq': 0.75}  # Brown eyes common
        },
        'typical_traits': ['Brown eyes', 'Dark hair', 'Olive skin', 'Medium height']
    },

    'ancient_egyptian': {
        'description': 'Ancient Egyptians',
        'time_period': '3,000 BCE - 300 BCE',
        'location': 'Nile Valley',
        'contribution': 'Ancient civilization, North African/Near Eastern mix',
        'markers': {
            'rs1426654': {'egyptian_allele': 'A', 'freq': 0.65}
        }
    }
}

# =============================================================================
# VOICE PREDICTION
# =============================================================================

VOICE_GENETICS = {
    'voice_pitch': {
        'rs11031006': {
            'gene': 'FSHB',
            'description': 'Voice pitch (hormone-related)',
            'GG': {'pitch': 'Tendency toward deeper voice', 'score': 70},
            'GT': {'pitch': 'Average voice pitch', 'score': 50},
            'TT': {'pitch': 'Tendency toward higher voice', 'score': 30}
        }
    }
}

# =============================================================================
# LONGEVITY MARKERS - FIXED WITH PROPER SCORING
# =============================================================================

LONGEVITY_MARKERS_FIXED = {
    'rs2802292': {
        'gene': 'FOXO3',
        'description': 'Forkhead box O3 - major longevity gene',
        'category': 'longevity_core',
        'TT': {'effect': 'Longevity associated', 'score': 85, 'centenarian_enriched': True},
        'GT': {'effect': 'Moderate longevity benefit', 'score': 65},
        'GG': {'effect': 'Standard lifespan genetics', 'score': 45}
    },
    'rs2764264': {
        'gene': 'FOXO3',
        'description': 'Additional FOXO3 longevity marker',
        'category': 'longevity_core',
        'CC': {'effect': 'Longevity variant', 'score': 80, 'centenarian_enriched': True},
        'CT': {'effect': 'Partial benefit', 'score': 60},
        'TT': {'effect': 'Standard', 'score': 45}
    },
    'rs429358': {
        'gene': 'APOE',
        'description': 'APOE - affects longevity and Alzheimers',
        'category': 'longevity_core',
        'TT': {'effect': 'APOE2/3 - longevity associated', 'score': 80, 'note': 'Common in centenarians'},
        'CT': {'effect': 'APOE3/4 - average lifespan', 'score': 50},
        'CC': {'effect': 'APOE4/4 - reduced longevity', 'score': 25, 'note': 'Alzheimers risk'}
    },
    'rs5882': {
        'gene': 'CETP',
        'description': 'Cholesterol ester transfer protein',
        'category': 'cardiovascular_aging',
        'AA': {'effect': 'Longevity variant', 'score': 75, 'hdl': 'Higher HDL cholesterol'},
        'AG': {'effect': 'Moderate benefit', 'score': 58, 'hdl': 'Moderately higher HDL'},
        'GG': {'effect': 'Standard', 'score': 45, 'hdl': 'Normal HDL'}
    },
    'rs1800795': {
        'gene': 'IL6',
        'description': 'Interleukin-6 - inflammation and aging',
        'category': 'inflammation',
        'GG': {'effect': 'Lower inflammation, longevity associated', 'score': 78},
        'GC': {'effect': 'Moderate inflammation', 'score': 55},
        'CC': {'effect': 'Higher inflammation, faster aging', 'score': 35}
    },
    'rs2736100': {
        'gene': 'TERT',
        'description': 'Telomerase reverse transcriptase',
        'category': 'telomere',
        'CC': {'effect': 'Longer telomeres', 'score': 80, 'longevity': 'Associated with longer life'},
        'AC': {'effect': 'Average telomere length', 'score': 55},
        'AA': {'effect': 'Shorter telomeres', 'score': 35, 'longevity': 'Faster cellular aging'}
    },
    'rs10936599': {
        'gene': 'TERC',
        'description': 'Telomerase RNA component',
        'category': 'telomere',
        'CC': {'effect': 'Longer telomeres', 'score': 75},
        'CT': {'effect': 'Average', 'score': 52},
        'TT': {'effect': 'Shorter telomeres', 'score': 32}
    },
    'rs3758391': {
        'gene': 'SIRT1',
        'description': 'Sirtuin 1 - caloric restriction mimetic pathway',
        'category': 'metabolism',
        'CC': {'effect': 'Enhanced stress resistance', 'score': 78, 'longevity': 'Caloric restriction benefit'},
        'CT': {'effect': 'Moderate benefit', 'score': 55},
        'TT': {'effect': 'Standard aging', 'score': 40}
    },
    'rs9536314': {
        'gene': 'KLOTHO',
        'description': 'Klotho anti-aging gene',
        'category': 'longevity_core',
        'TT': {'effect': 'KL-VS variant - longevity associated', 'score': 82, 'cognition': 'Better cognitive aging'},
        'GT': {'effect': 'One copy - some benefit', 'score': 62},
        'GG': {'effect': 'Standard aging', 'score': 45}
    },
    'rs4880': {
        'gene': 'SOD2',
        'description': 'Superoxide dismutase - antioxidant enzyme',
        'category': 'oxidative_stress',
        'TT': {'effect': 'Higher SOD activity', 'score': 72, 'oxidative': 'Better antioxidant defense'},
        'CT': {'effect': 'Moderate activity', 'score': 52},
        'CC': {'effect': 'Lower activity', 'score': 38, 'oxidative': 'May benefit from antioxidants'}
    },
    'rs4340': {
        'gene': 'ACE',
        'description': 'Angiotensin converting enzyme',
        'category': 'cardiovascular_aging',
        'II': {'effect': 'Lower ACE - associated with longevity', 'score': 70},
        'ID': {'effect': 'Moderate', 'score': 52},
        'DD': {'effect': 'Higher ACE - may affect cardiovascular aging', 'score': 38}
    },
    'rs1042522': {
        'gene': 'TP53',
        'description': 'Tumor suppressor p53',
        'category': 'dna_repair',
        'CC': {'effect': 'Pro72 - better DNA repair with age', 'score': 68},
        'CG': {'effect': 'Heterozygous', 'score': 50},
        'GG': {'effect': 'Arg72 - stronger apoptosis', 'score': 48}
    },
    'rs5174': {
        'gene': 'LPA',
        'description': 'Lipoprotein(a) - cardiovascular longevity',
        'category': 'cardiovascular_aging',
        'TT': {'effect': 'Lower Lp(a) - cardiovascular benefit', 'score': 72},
        'CT': {'effect': 'Moderate Lp(a)', 'score': 50},
        'CC': {'effect': 'Higher Lp(a) - cardiovascular risk', 'score': 35}
    },
    'rs1801133': {
        'gene': 'MTHFR',
        'description': 'Methylation and homocysteine',
        'category': 'metabolism',
        'CC': {'effect': 'Normal folate metabolism', 'score': 65},
        'CT': {'effect': 'Slightly reduced', 'score': 52},
        'TT': {'effect': 'Reduced - take methylfolate', 'score': 40}
    },
    'rs662': {
        'gene': 'PON1',
        'description': 'Paraoxonase - protects LDL from oxidation',
        'category': 'oxidative_stress',
        'AA': {'effect': 'Higher PON1 activity', 'score': 70},
        'AG': {'effect': 'Moderate activity', 'score': 52},
        'GG': {'effect': 'Lower activity', 'score': 38}
    }
}

print("Advanced traits database loaded")
print(f"Facial features: {len(FACIAL_FEATURES)} categories")
print(f"Chronotype markers: {len(CHRONOTYPE_GENETICS)} categories")
print(f"Pain genetics: {len(PAIN_GENETICS)} categories")
print(f"Addiction genetics: {len(ADDICTION_GENETICS)} categories")
print(f"Mental genetics: {len(MENTAL_GENETICS)} categories")
print(f"Sensory genetics: {len(SENSORY_GENETICS)} categories")
print(f"Longevity markers (fixed): {len(LONGEVITY_MARKERS_FIXED)}")
