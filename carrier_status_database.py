#!/usr/bin/env python3
"""
Comprehensive Carrier Status Database
Real SNP data for genetic disease carrier screening
Sources: ClinVar, dbSNP, OMIM, gnomAD, ACMG recommendations
"""


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
# CYSTIC FIBROSIS (CFTR Gene)
# =============================================================================

CYSTIC_FIBROSIS = {
    'condition': 'Cystic Fibrosis',
    'gene': 'CFTR',
    'chromosome': '7',
    'inheritance': 'Autosomal Recessive',
    'description': 'Affects lungs, pancreas, and other organs. Most common life-threatening genetic disease in Caucasians.',
    'carrier_frequency': {
        'European': '1 in 25',
        'Hispanic': '1 in 46',
        'African': '1 in 65',
        'East_Asian': '1 in 90'
    },
    'markers': {
        'rs113993960': {  # F508del - most common CF mutation
            'gene': 'CFTR',
            'name': 'F508del (deltaF508)',
            'clinical_significance': 'Pathogenic',
            'frequency_in_CF': '70%',
            'alleles': {
                'CTT': {'status': 'Normal', 'description': 'No F508del mutation'},
                'DEL': {'status': 'Carrier', 'description': 'Carries F508del mutation - most common CF variant'}
            }
        },
        'rs75039782': {  # G542X
            'gene': 'CFTR',
            'name': 'G542X',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'GG': {'status': 'Normal', 'description': 'No G542X mutation'},
                'GA': {'status': 'Carrier', 'description': 'Carries G542X mutation'},
                'AA': {'status': 'Affected', 'description': 'Homozygous G542X'}
            }
        },
        'rs78655421': {  # G551D
            'gene': 'CFTR',
            'name': 'G551D',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'GG': {'status': 'Normal', 'description': 'No G551D mutation'},
                'GA': {'status': 'Carrier', 'description': 'Carries G551D mutation - responsive to ivacaftor'},
                'AA': {'status': 'Affected', 'description': 'Homozygous G551D'}
            }
        },
        'rs121908745': {  # W1282X
            'gene': 'CFTR',
            'name': 'W1282X',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'GG': {'status': 'Normal', 'description': 'No W1282X mutation'},
                'GA': {'status': 'Carrier', 'description': 'Carries W1282X mutation'},
                'AA': {'status': 'Affected', 'description': 'Homozygous W1282X'}
            }
        },
        'rs121909011': {  # N1303K
            'gene': 'CFTR',
            'name': 'N1303K',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'CC': {'status': 'Normal', 'description': 'No N1303K mutation'},
                'CG': {'status': 'Carrier', 'description': 'Carries N1303K mutation'},
                'GG': {'status': 'Affected', 'description': 'Homozygous N1303K'}
            }
        }
    },
    'implications': {
        'Carrier': [
            'No symptoms expected',
            '50% chance of passing mutation to each child',
            'If partner is also carrier: 25% chance of affected child',
            'Consider genetic counseling before family planning'
        ],
        'Affected': [
            'Consult with CF specialist immediately',
            'Lung function monitoring essential',
            'Pancreatic enzyme supplementation often needed',
            'Life expectancy has improved significantly with modern treatments'
        ]
    }
}

# =============================================================================
# SICKLE CELL DISEASE (HBB Gene)
# =============================================================================

SICKLE_CELL_DISEASE = {
    'condition': 'Sickle Cell Disease',
    'gene': 'HBB',
    'chromosome': '11',
    'inheritance': 'Autosomal Recessive',
    'description': 'Red blood cells become sickle-shaped, causing anemia, pain, and organ damage.',
    'carrier_frequency': {
        'African': '1 in 12',
        'Hispanic': '1 in 36',
        'Middle_Eastern': '1 in 25',
        'Mediterranean': '1 in 30',
        'European': '< 1 in 200'
    },
    'markers': {
        'rs334': {  # HbS mutation - primary sickle cell variant
            'gene': 'HBB',
            'name': 'HbS (Glu6Val)',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'TT': {'status': 'Normal', 'description': 'Normal hemoglobin (HbA/HbA)'},
                'AT': {'status': 'Carrier (Sickle Cell Trait)', 'description': 'Carrier - confers malaria resistance'},
                'TA': {'status': 'Carrier (Sickle Cell Trait)', 'description': 'Carrier - confers malaria resistance'},
                'AA': {'status': 'Affected (Sickle Cell Disease)', 'description': 'Has sickle cell disease (HbS/HbS)'}
            }
        },
        'rs33930165': {  # HbC mutation
            'gene': 'HBB',
            'name': 'HbC (Glu6Lys)',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'GG': {'status': 'Normal', 'description': 'No HbC mutation'},
                'GA': {'status': 'Carrier (HbC Trait)', 'description': 'HbC carrier'},
                'AA': {'status': 'Affected (HbCC)', 'description': 'HbC disease'}
            }
        },
        'rs33950507': {  # HbE mutation - common in Southeast Asia
            'gene': 'HBB',
            'name': 'HbE (Glu26Lys)',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'GG': {'status': 'Normal', 'description': 'No HbE mutation'},
                'GA': {'status': 'Carrier (HbE Trait)', 'description': 'HbE carrier - common in Southeast Asia'},
                'AA': {'status': 'Affected (HbEE)', 'description': 'HbE disease - usually mild'}
            }
        }
    },
    'implications': {
        'Carrier (Sickle Cell Trait)': [
            'Generally healthy with no symptoms',
            'Provides protection against malaria',
            'Rare risk of complications at extreme altitude or dehydration',
            'Important to know for family planning',
            '50% chance of passing trait to each child'
        ],
        'Affected': [
            'Requires specialized hematology care',
            'Pain crises may require hospitalization',
            'Increased infection risk - vaccinations critical',
            'Hydroxyurea may reduce complications',
            'Bone marrow transplant can be curative'
        ]
    }
}

# =============================================================================
# TAY-SACHS DISEASE (HEXA Gene)
# =============================================================================

TAY_SACHS_DISEASE = {
    'condition': 'Tay-Sachs Disease',
    'gene': 'HEXA',
    'chromosome': '15',
    'inheritance': 'Autosomal Recessive',
    'description': 'Fatal neurological disorder causing progressive destruction of nerve cells.',
    'carrier_frequency': {
        'Ashkenazi_Jewish': '1 in 30',
        'French_Canadian': '1 in 30',
        'Cajun': '1 in 30',
        'European': '1 in 300',
        'Global': '1 in 250'
    },
    'markers': {
        'rs28940868': {  # 1278insTATC - Ashkenazi founder mutation
            'gene': 'HEXA',
            'name': '1278insTATC',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'normal': {'status': 'Normal', 'description': 'No mutation'},
                'insertion': {'status': 'Carrier', 'description': 'Carries 1278insTATC - common Ashkenazi mutation'}
            }
        },
        'rs121907952': {  # IVS12+1G>C
            'gene': 'HEXA',
            'name': 'IVS12+1G>C',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'GG': {'status': 'Normal', 'description': 'No IVS12 mutation'},
                'GC': {'status': 'Carrier', 'description': 'Carries IVS12+1G>C mutation'},
                'CC': {'status': 'Affected', 'description': 'Homozygous IVS12+1G>C'}
            }
        },
        'rs121907951': {  # G269S - late-onset variant
            'gene': 'HEXA',
            'name': 'G269S',
            'clinical_significance': 'Pathogenic (late-onset)',
            'alleles': {
                'GG': {'status': 'Normal', 'description': 'No G269S mutation'},
                'GA': {'status': 'Carrier', 'description': 'Carries G269S - associated with late-onset form'},
                'AA': {'status': 'Affected', 'description': 'Homozygous G269S - late-onset Tay-Sachs'}
            }
        }
    },
    'implications': {
        'Carrier': [
            'No symptoms - completely healthy',
            'Important for Ashkenazi Jewish individuals to know carrier status',
            'Standard screening recommended before pregnancy',
            'If both partners are carriers: consider IVF with PGT'
        ],
        'Affected': [
            'Infantile form: symptoms begin at 6 months',
            'Progressive neurological decline',
            'No cure currently available',
            'Supportive care and palliative care options'
        ]
    }
}

# =============================================================================
# BETA THALASSEMIA (HBB Gene)
# =============================================================================

BETA_THALASSEMIA = {
    'condition': 'Beta Thalassemia',
    'gene': 'HBB',
    'chromosome': '11',
    'inheritance': 'Autosomal Recessive',
    'description': 'Reduced production of beta-globin causes anemia. Severity varies from mild to transfusion-dependent.',
    'carrier_frequency': {
        'Mediterranean': '1 in 7',
        'Middle_Eastern': '1 in 10',
        'South_Asian': '1 in 20',
        'Southeast_Asian': '1 in 20',
        'African': '1 in 75',
        'European': '1 in 100'
    },
    'markers': {
        'rs11549407': {  # IVS1-110G>A - common Mediterranean mutation
            'gene': 'HBB',
            'name': 'IVS1-110 G>A',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'GG': {'status': 'Normal', 'description': 'No IVS1-110 mutation'},
                'GA': {'status': 'Carrier (Thalassemia Minor)', 'description': 'Carries IVS1-110 mutation'},
                'AA': {'status': 'Affected (Thalassemia Major)', 'description': 'Homozygous - requires transfusions'}
            }
        },
        'rs35004220': {  # Codon 39 C>T - Mediterranean founder
            'gene': 'HBB',
            'name': 'Codon 39 (C>T)',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'CC': {'status': 'Normal', 'description': 'No Codon 39 mutation'},
                'CT': {'status': 'Carrier', 'description': 'Carries Codon 39 mutation - common in Mediterranean'},
                'TT': {'status': 'Affected', 'description': 'Homozygous Codon 39'}
            }
        },
        'rs63750783': {  # IVS1-5 G>C - Asian variant
            'gene': 'HBB',
            'name': 'IVS1-5 G>C',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'GG': {'status': 'Normal', 'description': 'No IVS1-5 mutation'},
                'GC': {'status': 'Carrier', 'description': 'Carries IVS1-5 mutation - common in Asia'},
                'CC': {'status': 'Affected', 'description': 'Homozygous IVS1-5'}
            }
        }
    },
    'implications': {
        'Carrier (Thalassemia Minor)': [
            'Usually mild or no anemia',
            'May be mistaken for iron deficiency - iron supplements not helpful',
            'MCV typically low (microcytic)',
            'Important to identify before pregnancy',
            'No treatment usually needed'
        ],
        'Affected (Thalassemia Major)': [
            'Requires regular blood transfusions',
            'Iron chelation therapy essential',
            'Bone marrow transplant can be curative',
            'Gene therapy becoming available',
            'Lifelong monitoring required'
        ]
    }
}

# =============================================================================
# SPINAL MUSCULAR ATROPHY (SMN1 Gene)
# =============================================================================

SPINAL_MUSCULAR_ATROPHY = {
    'condition': 'Spinal Muscular Atrophy (SMA)',
    'gene': 'SMN1',
    'chromosome': '5',
    'inheritance': 'Autosomal Recessive',
    'description': 'Progressive muscle weakness and atrophy due to motor neuron loss. Leading genetic cause of infant death.',
    'carrier_frequency': {
        'European': '1 in 50',
        'African': '1 in 66',
        'Asian': '1 in 59',
        'Hispanic': '1 in 68',
        'Global': '1 in 54'
    },
    'markers': {
        'rs121909192': {  # SMN1 exon 7 deletion marker
            'gene': 'SMN1',
            'name': 'SMN1 copy number (exon 7)',
            'clinical_significance': 'Pathogenic',
            'note': 'SMA is typically caused by deletion of SMN1. Most carriers have 1 copy instead of 2.',
            'alleles': {
                '2_copies': {'status': 'Normal', 'description': '2 copies of SMN1 - normal'},
                '1_copy': {'status': 'Carrier', 'description': '1 copy of SMN1 - carrier'},
                '0_copies': {'status': 'Affected', 'description': '0 copies of SMN1 - affected with SMA'}
            }
        },
        'rs143838139': {  # SMN1 exon 8 marker
            'gene': 'SMN1',
            'name': 'c.815A>G (p.Tyr272Cys)',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'AA': {'status': 'Normal', 'description': 'No point mutation'},
                'AG': {'status': 'Carrier', 'description': 'Carries SMN1 point mutation'},
                'GG': {'status': 'Affected', 'description': 'Homozygous mutation'}
            }
        }
    },
    'implications': {
        'Carrier': [
            'No symptoms',
            'Carrier screening recommended for all couples',
            'ACMG recommends carrier screening regardless of ethnicity',
            'If both partners are carriers: consider PGT',
            'New treatments (Zolgensma, Spinraza) available for affected children'
        ],
        'Affected': [
            'Types range from severe (Type 1) to mild (Type 4)',
            'Gene therapy (Zolgensma) can be curative if given early',
            'Spinraza (nusinersen) effective at all ages',
            'Risdiplam (oral) also available',
            'Early diagnosis critical for best outcomes'
        ]
    }
}

# =============================================================================
# PHENYLKETONURIA (PAH Gene)
# =============================================================================

PHENYLKETONURIA = {
    'condition': 'Phenylketonuria (PKU)',
    'gene': 'PAH',
    'chromosome': '12',
    'inheritance': 'Autosomal Recessive',
    'description': 'Inability to metabolize phenylalanine. Untreated causes intellectual disability. Treatable with diet.',
    'carrier_frequency': {
        'European': '1 in 50',
        'Turkish': '1 in 26',
        'Irish': '1 in 30',
        'Asian': '1 in 100',
        'African': '1 in 200'
    },
    'markers': {
        'rs5030858': {  # R408W - most common mutation in Europeans
            'gene': 'PAH',
            'name': 'R408W',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'CC': {'status': 'Normal', 'description': 'No R408W mutation'},
                'CT': {'status': 'Carrier', 'description': 'Carries R408W - most common PKU mutation in Europeans'},
                'TT': {'status': 'Affected', 'description': 'Homozygous R408W - classic PKU'}
            }
        },
        'rs5030857': {  # IVS12+1G>A
            'gene': 'PAH',
            'name': 'IVS12+1G>A',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'GG': {'status': 'Normal', 'description': 'No IVS12 mutation'},
                'GA': {'status': 'Carrier', 'description': 'Carries IVS12 mutation'},
                'AA': {'status': 'Affected', 'description': 'Homozygous IVS12'}
            }
        },
        'rs62508188': {  # R261Q - mild variant
            'gene': 'PAH',
            'name': 'R261Q',
            'clinical_significance': 'Pathogenic (mild)',
            'alleles': {
                'GG': {'status': 'Normal', 'description': 'No R261Q mutation'},
                'GA': {'status': 'Carrier', 'description': 'Carries R261Q - associated with milder PKU'},
                'AA': {'status': 'Affected (mild)', 'description': 'Homozygous R261Q - mild PKU'}
            }
        }
    },
    'implications': {
        'Carrier': [
            'No dietary restrictions needed',
            'No symptoms',
            'Important to know for family planning'
        ],
        'Affected': [
            'Newborn screening detects PKU at birth',
            'Strict low-phenylalanine diet from infancy',
            'Normal development possible with early treatment',
            'Kuvan (sapropterin) helps some patients',
            'Lifelong dietary management recommended',
            'Maternal PKU: strict control essential during pregnancy'
        ]
    }
}

# =============================================================================
# GAUCHER DISEASE (GBA Gene)
# =============================================================================

GAUCHER_DISEASE = {
    'condition': 'Gaucher Disease',
    'gene': 'GBA',
    'chromosome': '1',
    'inheritance': 'Autosomal Recessive',
    'description': 'Lysosomal storage disorder causing enlarged spleen/liver, bone problems. Type 1 is treatable.',
    'carrier_frequency': {
        'Ashkenazi_Jewish': '1 in 15',
        'European': '1 in 100',
        'Global': '1 in 100'
    },
    'markers': {
        'rs76763715': {  # N370S - most common, type 1
            'gene': 'GBA',
            'name': 'N370S (N409S)',
            'clinical_significance': 'Pathogenic',
            'note': 'N370S causes Type 1 (non-neuronopathic) - the treatable form',
            'alleles': {
                'AA': {'status': 'Normal', 'description': 'No N370S mutation'},
                'AG': {'status': 'Carrier', 'description': 'Carries N370S - Type 1 Gaucher if homozygous'},
                'GG': {'status': 'Affected (Type 1)', 'description': 'Homozygous N370S - Type 1 Gaucher'}
            }
        },
        'rs421016': {  # 84GG insertion
            'gene': 'GBA',
            'name': '84GG (c.84dupG)',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'normal': {'status': 'Normal', 'description': 'No 84GG insertion'},
                'insertion': {'status': 'Carrier', 'description': 'Carries 84GG insertion'}
            }
        },
        'rs80356769': {  # L444P - severe, types 2/3
            'gene': 'GBA',
            'name': 'L444P (L483P)',
            'clinical_significance': 'Pathogenic',
            'note': 'L444P associated with neuronopathic forms and Parkinson risk',
            'alleles': {
                'CC': {'status': 'Normal', 'description': 'No L444P mutation'},
                'CT': {'status': 'Carrier', 'description': 'Carries L444P - increased Parkinson risk'},
                'TT': {'status': 'Affected', 'description': 'Homozygous L444P - likely neuronopathic'}
            }
        }
    },
    'implications': {
        'Carrier': [
            'No Gaucher disease symptoms',
            'GBA mutations increase Parkinson disease risk ~5x',
            'Screening recommended for Ashkenazi Jewish couples',
            'Does NOT mean Parkinson is inevitable'
        ],
        'Affected': [
            'Type 1: Enlarged spleen/liver, bone disease, treatable',
            'Types 2/3: Neurological involvement, more severe',
            'Enzyme replacement therapy (ERT) very effective for Type 1',
            'Substrate reduction therapy also available',
            'Early treatment prevents complications'
        ]
    }
}

# =============================================================================
# HEMOCHROMATOSIS (HFE Gene)
# =============================================================================

HEMOCHROMATOSIS = {
    'condition': 'Hereditary Hemochromatosis',
    'gene': 'HFE',
    'chromosome': '6',
    'inheritance': 'Autosomal Recessive',
    'description': 'Excess iron absorption leads to organ damage. Most common genetic disorder in people of European descent.',
    'carrier_frequency': {
        'European': '1 in 8',
        'Irish': '1 in 5',
        'Northern_European': '1 in 6',
        'Mediterranean': '1 in 20',
        'Asian': 'Very rare',
        'African': 'Very rare'
    },
    'markers': {
        'rs1800562': {  # C282Y - primary mutation
            'gene': 'HFE',
            'name': 'C282Y',
            'clinical_significance': 'Pathogenic',
            'note': 'C282Y homozygosity causes most clinical hemochromatosis',
            'alleles': {
                'GG': {'status': 'Normal', 'description': 'No C282Y mutation'},
                'GA': {'status': 'Carrier', 'description': 'Heterozygous C282Y - usually no iron overload'},
                'AA': {'status': 'At Risk', 'description': 'Homozygous C282Y - high risk of iron overload'}
            }
        },
        'rs1799945': {  # H63D - common variant
            'gene': 'HFE',
            'name': 'H63D',
            'clinical_significance': 'Risk factor',
            'note': 'H63D alone rarely causes disease, but compound het (C282Y/H63D) can',
            'alleles': {
                'CC': {'status': 'Normal', 'description': 'No H63D mutation'},
                'CG': {'status': 'Carrier', 'description': 'Heterozygous H63D - minor risk factor'},
                'GG': {'status': 'Homozygous H63D', 'description': 'H63D/H63D - mild risk only'}
            }
        },
        'rs1800730': {  # S65C - rare variant
            'gene': 'HFE',
            'name': 'S65C',
            'clinical_significance': 'Uncertain significance',
            'alleles': {
                'AA': {'status': 'Normal', 'description': 'No S65C mutation'},
                'AT': {'status': 'Carrier', 'description': 'Heterozygous S65C - minimal significance'},
                'TT': {'status': 'Homozygous', 'description': 'S65C/S65C - significance unclear'}
            }
        }
    },
    'implications': {
        'Carrier': [
            'Usually no iron overload',
            'Monitor ferritin levels periodically',
            'Compound heterozygotes (C282Y/H63D) should monitor iron'
        ],
        'At Risk (C282Y/C282Y)': [
            'Monitor serum ferritin and transferrin saturation annually',
            'Penetrance is variable - not all develop symptoms',
            'Men at higher risk than women (menstruation is protective)',
            'Avoid iron supplements and vitamin C with meals',
            'Therapeutic phlebotomy if iron levels elevated',
            'Early detection prevents cirrhosis and cardiomyopathy'
        ]
    }
}

# =============================================================================
# G6PD DEFICIENCY (G6PD Gene)
# =============================================================================

G6PD_DEFICIENCY = {
    'condition': 'G6PD Deficiency',
    'gene': 'G6PD',
    'chromosome': 'X',
    'inheritance': 'X-Linked Recessive',
    'description': 'Red blood cells break down when exposed to certain triggers (fava beans, medications). Most common enzyme deficiency worldwide.',
    'carrier_frequency': {
        'African': '1 in 5 males affected',
        'Mediterranean': '1 in 10 males affected',
        'Middle_Eastern': '1 in 10 males affected',
        'Southeast_Asian': '1 in 14 males affected',
        'European': '< 1 in 100'
    },
    'markers': {
        'rs1050828': {  # G6PD A- (202A)
            'gene': 'G6PD',
            'name': 'G6PD A- (Val68Met)',
            'clinical_significance': 'Pathogenic',
            'note': 'Common in African populations, milder phenotype',
            'alleles': {
                'CC': {'status': 'Normal', 'description': 'No A- variant'},
                'CT': {'status': 'Carrier (female) / Affected (male)', 'description': 'Carries A- variant'},
                'TT': {'status': 'Affected', 'description': 'A- variant - avoid triggers'}
            }
        },
        'rs1050829': {  # G6PD A (376G)
            'gene': 'G6PD',
            'name': 'G6PD A (Asn126Asp)',
            'clinical_significance': 'Benign (usually)',
            'note': 'G6PD A alone is usually not pathogenic - becomes A- with Val68Met',
            'alleles': {
                'AA': {'status': 'Normal', 'description': 'No A variant'},
                'AG': {'status': 'Variant', 'description': 'G6PD A variant'},
                'GG': {'status': 'Variant', 'description': 'G6PD A homozygous'}
            }
        },
        'rs5030868': {  # G6PD Mediterranean (563T)
            'gene': 'G6PD',
            'name': 'G6PD Mediterranean (Ser188Phe)',
            'clinical_significance': 'Pathogenic',
            'note': 'Severe form, common in Mediterranean populations',
            'alleles': {
                'CC': {'status': 'Normal', 'description': 'No Mediterranean variant'},
                'CT': {'status': 'Carrier (female) / Affected (male)', 'description': 'G6PD Mediterranean - severe form'},
                'TT': {'status': 'Affected', 'description': 'Mediterranean variant - strict avoidance needed'}
            }
        }
    },
    'triggers_to_avoid': [
        'Fava beans (favism)',
        'Primaquine (antimalarial)',
        'Dapsone',
        'Nitrofurantoin',
        'Methylene blue',
        'Sulfonamides',
        'Mothballs (naphthalene)',
        'High-dose aspirin',
        'Quinidine'
    ],
    'implications': {
        'Carrier (Female)': [
            'Usually mild or no symptoms due to X-inactivation',
            'May have some hemolysis with severe triggers',
            'Can pass to sons (50% affected) and daughters (50% carriers)'
        ],
        'Affected': [
            'Avoid known trigger medications and foods',
            'Carry medical ID card listing condition',
            'Inform all healthcare providers',
            'Hemolysis episodes usually self-limiting',
            'Blood transfusion rarely needed',
            'Provides protection against malaria'
        ]
    }
}

# =============================================================================
# FAMILIAL MEDITERRANEAN FEVER (MEFV Gene)
# =============================================================================

FAMILIAL_MEDITERRANEAN_FEVER = {
    'condition': 'Familial Mediterranean Fever (FMF)',
    'gene': 'MEFV',
    'chromosome': '16',
    'inheritance': 'Autosomal Recessive (usually)',
    'description': 'Periodic fever and inflammation episodes. Most common in Mediterranean populations. Treatable with colchicine.',
    'carrier_frequency': {
        'Armenian': '1 in 5',
        'Turkish': '1 in 5',
        'Sephardic_Jewish': '1 in 5',
        'Arab': '1 in 5',
        'Ashkenazi_Jewish': '1 in 5',
        'European': '1 in 200'
    },
    'markers': {
        'rs61752717': {  # M694V - most common, severe
            'gene': 'MEFV',
            'name': 'M694V',
            'clinical_significance': 'Pathogenic',
            'note': 'Most common mutation, associated with severe disease and amyloidosis risk',
            'alleles': {
                'AA': {'status': 'Normal', 'description': 'No M694V mutation'},
                'AG': {'status': 'Carrier', 'description': 'Carries M694V - monitor for symptoms'},
                'GG': {'status': 'Affected', 'description': 'Homozygous M694V - likely symptomatic'}
            }
        },
        'rs28940579': {  # M680I
            'gene': 'MEFV',
            'name': 'M680I',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'GG': {'status': 'Normal', 'description': 'No M680I mutation'},
                'GA': {'status': 'Carrier', 'description': 'Carries M680I mutation'},
                'AA': {'status': 'Affected', 'description': 'Homozygous M680I'}
            }
        },
        'rs3743930': {  # E148Q - common, mild
            'gene': 'MEFV',
            'name': 'E148Q',
            'clinical_significance': 'Uncertain significance / low penetrance',
            'note': 'Very common variant, may modify disease but rarely causes FMF alone',
            'alleles': {
                'GG': {'status': 'Normal', 'description': 'No E148Q variant'},
                'GC': {'status': 'Variant carrier', 'description': 'E148Q - significance unclear'},
                'CC': {'status': 'Homozygous variant', 'description': 'E148Q/E148Q - may have mild symptoms'}
            }
        },
        'rs28940578': {  # V726A
            'gene': 'MEFV',
            'name': 'V726A',
            'clinical_significance': 'Pathogenic',
            'alleles': {
                'TT': {'status': 'Normal', 'description': 'No V726A mutation'},
                'TC': {'status': 'Carrier', 'description': 'Carries V726A mutation'},
                'CC': {'status': 'Affected', 'description': 'Homozygous V726A'}
            }
        }
    },
    'implications': {
        'Carrier': [
            'Some carriers have mild symptoms (pseudodominant)',
            'More common in Mediterranean populations',
            'Monitor for recurrent fevers with abdominal pain'
        ],
        'Affected': [
            'Colchicine is highly effective - prevents attacks and amyloidosis',
            'Take colchicine daily, not just during attacks',
            'IL-1 blockers (Anakinra, Canakinumab) for colchicine-resistant cases',
            'Monitor for AA amyloidosis with urine protein',
            'Most patients lead normal lives with treatment'
        ]
    }
}

# =============================================================================
# ALPHA-1 ANTITRYPSIN DEFICIENCY (SERPINA1 Gene)
# =============================================================================

ALPHA1_ANTITRYPSIN = {
    'condition': 'Alpha-1 Antitrypsin Deficiency',
    'gene': 'SERPINA1',
    'chromosome': '14',
    'inheritance': 'Autosomal Codominant',
    'description': 'Causes lung disease (COPD/emphysema) and liver disease. Especially harmful in smokers.',
    'carrier_frequency': {
        'European': '1 in 25 (for Z allele)',
        'Scandinavian': '1 in 20',
        'Irish': '1 in 20',
        'Asian': 'Very rare',
        'African': 'Very rare'
    },
    'markers': {
        'rs28929474': {  # Z allele (E342K)
            'gene': 'SERPINA1',
            'name': 'Pi*Z (E342K)',
            'clinical_significance': 'Pathogenic',
            'note': 'Z/Z causes severe deficiency, M/Z carriers have some risk',
            'alleles': {
                'CC': {'status': 'Normal (MM)', 'description': 'No Z allele - normal AAT levels'},
                'CT': {'status': 'Carrier (MZ)', 'description': 'One Z allele - mildly reduced AAT, avoid smoking'},
                'TT': {'status': 'Affected (ZZ)', 'description': 'Homozygous Z - severely reduced AAT'}
            }
        },
        'rs17580': {  # S allele (E264V)
            'gene': 'SERPINA1',
            'name': 'Pi*S (E264V)',
            'clinical_significance': 'Risk factor',
            'note': 'S allele is milder, but S/Z compound hets have moderate deficiency',
            'alleles': {
                'AA': {'status': 'Normal (MM)', 'description': 'No S allele'},
                'AT': {'status': 'Carrier (MS)', 'description': 'One S allele - usually normal AAT levels'},
                'TT': {'status': 'Homozygous (SS)', 'description': 'Mild-moderate reduction in AAT'}
            }
        }
    },
    'implications': {
        'Carrier (MZ)': [
            'Mildly reduced AAT levels',
            'Do NOT smoke - even MZ carriers have increased COPD risk if smoking',
            'Avoid occupational dust and chemical exposure',
            'Generally good prognosis with healthy lifestyle'
        ],
        'Affected (ZZ)': [
            'High risk of emphysema/COPD, especially if smoking',
            'Can develop liver disease (cirrhosis)',
            'Absolutely avoid smoking and secondhand smoke',
            'AAT augmentation therapy available (IV infusions)',
            'Lung transplant for end-stage disease',
            'Screen family members'
        ]
    }
}

# =============================================================================
# COMPREHENSIVE CARRIER STATUS DATABASE
# =============================================================================

CARRIER_STATUS_DATABASE = {
    'cystic_fibrosis': CYSTIC_FIBROSIS,
    'sickle_cell_disease': SICKLE_CELL_DISEASE,
    'tay_sachs': TAY_SACHS_DISEASE,
    'beta_thalassemia': BETA_THALASSEMIA,
    'spinal_muscular_atrophy': SPINAL_MUSCULAR_ATROPHY,
    'phenylketonuria': PHENYLKETONURIA,
    'gaucher_disease': GAUCHER_DISEASE,
    'hemochromatosis': HEMOCHROMATOSIS,
    'g6pd_deficiency': G6PD_DEFICIENCY,
    'familial_mediterranean_fever': FAMILIAL_MEDITERRANEAN_FEVER,
    'alpha1_antitrypsin': ALPHA1_ANTITRYPSIN
}


# =============================================================================
# ANALYSIS FUNCTIONS
# =============================================================================

def analyze_carrier_status(dna_data: dict) -> dict:
    """
    Comprehensive carrier status analysis

    Args:
        dna_data: Dictionary of {rsid: genotype}

    Returns:
        Dictionary with carrier status for all conditions
    """
    results = {
        'carriers_found': [],
        'conditions_clear': [],
        'conditions_analyzed': [],
        'high_risk_conditions': [],
        'markers_tested': 0,
        'recommendations': []
    }

    for condition_id, condition_data in CARRIER_STATUS_DATABASE.items():
        condition_name = condition_data['condition']
        gene = condition_data['gene']
        inheritance = condition_data['inheritance']

        condition_result = {
            'condition': condition_name,
            'gene': gene,
            'inheritance': inheritance,
            'status': 'Unknown',
            'variants_found': [],
            'description': condition_data['description']
        }

        markers_checked = 0
        carrier_variants = []
        affected_variants = []

        for rsid, marker_info in condition_data['markers'].items():
            if rsid in dna_data:
                markers_checked += 1
                results['markers_tested'] += 1
                genotype = dna_data[rsid]

                alleles = marker_info.get('alleles', {})
                _key = get_genotype_key(genotype, alleles)
                if _key:
                    variant_status = alleles[_key]
                    status = variant_status.get('status', 'Unknown')

                    variant_info = {
                        'rsid': rsid,
                        'name': marker_info.get('name', rsid),
                        'genotype': genotype,
                        'status': status,
                        'description': variant_status.get('description', '')
                    }

                    if 'Carrier' in status:
                        carrier_variants.append(variant_info)
                    elif 'Affected' in status or 'At Risk' in status:
                        affected_variants.append(variant_info)

                    condition_result['variants_found'].append(variant_info)

        # Determine overall status
        if affected_variants:
            condition_result['status'] = 'At Risk / Affected'
            condition_result['implications'] = condition_data.get('implications', {}).get('Affected', [])
            results['high_risk_conditions'].append({
                **condition_result,
                'carrier_frequency': condition_data.get('carrier_frequency', {})
            })
        elif carrier_variants:
            condition_result['status'] = 'Carrier'
            carrier_key = next((k for k in condition_data.get('implications', {}).keys() if 'Carrier' in k), 'Carrier')
            condition_result['implications'] = condition_data.get('implications', {}).get(carrier_key, [])
            results['carriers_found'].append({
                **condition_result,
                'carrier_frequency': condition_data.get('carrier_frequency', {})
            })
        elif markers_checked > 0:
            condition_result['status'] = 'Clear (no variants detected)'
            results['conditions_clear'].append(condition_result)

        if markers_checked > 0:
            results['conditions_analyzed'].append({
                'condition': condition_name,
                'markers_tested': markers_checked,
                'status': condition_result['status']
            })

    # Generate recommendations
    if results['high_risk_conditions']:
        results['recommendations'].append('IMPORTANT: Consult a genetic counselor about high-risk conditions')

    if results['carriers_found']:
        results['recommendations'].append('Consider partner testing for carrier conditions before pregnancy')
        results['recommendations'].append('Genetic counseling recommended for family planning')

    # Summary stats
    results['summary'] = {
        'total_conditions_tested': len(results['conditions_analyzed']),
        'carriers_detected': len(results['carriers_found']),
        'high_risk_detected': len(results['high_risk_conditions']),
        'clear_conditions': len(results['conditions_clear'])
    }

    return results


def get_condition_info(condition_id: str) -> dict:
    """Get detailed information about a specific condition"""
    return CARRIER_STATUS_DATABASE.get(condition_id, {})


def get_all_tested_markers() -> list:
    """Get list of all markers tested in carrier screening"""
    markers = []
    for condition_id, condition_data in CARRIER_STATUS_DATABASE.items():
        for rsid, marker_info in condition_data['markers'].items():
            markers.append({
                'rsid': rsid,
                'gene': condition_data['gene'],
                'condition': condition_data['condition'],
                'name': marker_info.get('name', rsid),
                'clinical_significance': marker_info.get('clinical_significance', '')
            })
    return markers
