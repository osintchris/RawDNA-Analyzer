"""
Nutrition & Metabolism Genetics Database
Real SNP data for personalized nutrition and metabolic analysis

Features:
1. Vitamin A metabolism (BCMO1)
2. Vitamin B12 metabolism (FUT2, TCN2)
3. Vitamin C requirements (SLC23A1)
4. Vitamin E metabolism (TTPA)
5. Omega-3 fatty acid metabolism (FADS1/FADS2)
6. Saturated fat metabolism
7. Carbohydrate metabolism / Glycemic response
8. Protein requirements and metabolism
9. Sodium sensitivity (ACE, AGT)
10. Alcohol metabolism (ADH1B, ALDH2)
"""

from typing import Dict, Any, List, Optional


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
# VITAMIN A METABOLISM (Beta-carotene conversion)
# =============================================================================

VITAMIN_A_GENETICS = {
    # BCMO1 - Beta-carotene monooxygenase 1
    "rs7501331": {
        "gene": "BCMO1",
        "chromosome": "16",
        "function": "Beta-carotene to vitamin A conversion efficiency",
        "risk_allele": "T",
        "effect": {
            "CC": {"conversion_efficiency": "Normal (100%)", "recommendation": "Can rely on plant beta-carotene"},
            "CT": {"conversion_efficiency": "Reduced (~57%)", "recommendation": "May need more beta-carotene or preformed vitamin A"},
            "TT": {"conversion_efficiency": "Poor (~32%)", "recommendation": "Should prioritize preformed vitamin A (retinol)"}
        },
        "population_frequency": {"EUR": 0.42, "AFR": 0.24, "EAS": 0.33}
    },
    "rs12934922": {
        "gene": "BCMO1",
        "chromosome": "16",
        "function": "Beta-carotene conversion (secondary variant)",
        "risk_allele": "T",
        "effect": {
            "AA": {"conversion_efficiency": "Normal", "status": "Good converter"},
            "AT": {"conversion_efficiency": "Reduced", "status": "Moderate converter"},
            "TT": {"conversion_efficiency": "Poor", "status": "Poor converter"}
        },
        "population_frequency": {"EUR": 0.45, "AFR": 0.38, "EAS": 0.40}
    }
}

# =============================================================================
# VITAMIN B12 METABOLISM
# =============================================================================

VITAMIN_B12_GENETICS = {
    # FUT2 - Secretor status affects B12 absorption
    "rs601338": {
        "gene": "FUT2",
        "chromosome": "19",
        "function": "Secretor status - affects B12 absorption and gut microbiome",
        "common_name": "Secretor Status (FUT2)",
        "effect": {
            "GG": {"secretor_status": "Secretor", "b12_absorption": "Normal", "b12_risk": "Lower"},
            "GA": {"secretor_status": "Secretor", "b12_absorption": "Normal", "b12_risk": "Lower"},
            "AA": {"secretor_status": "Non-Secretor", "b12_absorption": "May be reduced", "b12_risk": "Higher deficiency risk"}
        },
        "population_frequency": {"EUR": 0.45, "AFR": 0.35, "EAS": 0.10}
    },
    # TCN2 - Transcobalamin II (B12 transport)
    "rs1801198": {
        "gene": "TCN2",
        "chromosome": "22",
        "function": "Vitamin B12 cellular transport (C776G)",
        "effect": {
            "CC": {"b12_transport": "Normal", "cellular_uptake": "Efficient"},
            "CG": {"b12_transport": "Slightly Reduced", "cellular_uptake": "Moderately Efficient"},
            "GG": {"b12_transport": "Reduced", "cellular_uptake": "Less Efficient - may need higher B12"}
        },
        "population_frequency": {"EUR": 0.45, "AFR": 0.40, "EAS": 0.35}
    },
    # MTHFR - Affects B12 utilization
    "rs1801133": {
        "gene": "MTHFR",
        "chromosome": "1",
        "function": "MTHFR C677T - affects folate/B12 metabolism",
        "common_name": "MTHFR C677T",
        "risk_allele": "T",
        "effect": {
            "CC": {"mthfr_activity": "Normal (100%)", "folate_need": "Normal", "homocysteine": "Normal"},
            "CT": {"mthfr_activity": "Reduced (~65%)", "folate_need": "Slightly Increased", "homocysteine": "May be elevated"},
            "TT": {"mthfr_activity": "Low (~30%)", "folate_need": "Increased", "homocysteine": "Elevated risk"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.10, "EAS": 0.40}
    },
    "rs1801131": {
        "gene": "MTHFR",
        "chromosome": "1",
        "function": "MTHFR A1298C - secondary variant",
        "effect": {
            "AA": {"mthfr_a1298c": "Normal", "activity": "100%"},
            "AC": {"mthfr_a1298c": "Heterozygous", "activity": "~80%"},
            "CC": {"mthfr_a1298c": "Homozygous", "activity": "~60%"}
        },
        "population_frequency": {"EUR": 0.32, "AFR": 0.15, "EAS": 0.20}
    }
}

# =============================================================================
# VITAMIN C METABOLISM
# =============================================================================

VITAMIN_C_GENETICS = {
    # SLC23A1 - Vitamin C transporter
    "rs33972313": {
        "gene": "SLC23A1",
        "chromosome": "5",
        "function": "Vitamin C transporter SVCT1",
        "effect": {
            "CC": {"vit_c_transport": "Normal", "plasma_levels": "Normal"},
            "CT": {"vit_c_transport": "Reduced", "plasma_levels": "May be lower"},
            "TT": {"vit_c_transport": "Significantly Reduced", "plasma_levels": "Likely lower"}
        },
        "population_frequency": {"EUR": 0.02, "AFR": 0.01, "EAS": 0.01}
    },
    # GSTT1/GSTM1 - Antioxidant need
    "rs1695": {
        "gene": "GSTP1",
        "chromosome": "11",
        "function": "Glutathione S-transferase - antioxidant enzyme",
        "effect": {
            "AA": {"antioxidant_activity": "Normal", "oxidative_stress": "Normal protection"},
            "AG": {"antioxidant_activity": "Reduced", "oxidative_stress": "Slightly increased need"},
            "GG": {"antioxidant_activity": "Low", "oxidative_stress": "Higher antioxidant needs"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.42, "EAS": 0.25}
    }
}

# =============================================================================
# VITAMIN E METABOLISM
# =============================================================================

VITAMIN_E_GENETICS = {
    # TTPA - Alpha-tocopherol transfer protein
    "rs6994076": {
        "gene": "TTPA",
        "chromosome": "8",
        "function": "Vitamin E transport and retention",
        "effect": {
            "TT": {"vit_e_status": "Normal retention", "recommendation": "Standard intake"},
            "TC": {"vit_e_status": "Reduced retention", "recommendation": "May benefit from higher intake"},
            "CC": {"vit_e_status": "Low retention", "recommendation": "Higher vitamin E intake recommended"}
        },
        "population_frequency": {"EUR": 0.30, "AFR": 0.25, "EAS": 0.28}
    },
    # CYP4F2 - Vitamin E metabolism
    "rs2108622": {
        "gene": "CYP4F2",
        "chromosome": "19",
        "function": "Vitamin E catabolism (also affects warfarin)",
        "effect": {
            "CC": {"vit_e_metabolism": "Normal", "levels": "Normal turnover"},
            "CT": {"vit_e_metabolism": "Reduced catabolism", "levels": "Slightly higher retention"},
            "TT": {"vit_e_metabolism": "Slow catabolism", "levels": "Higher retention - may need less"}
        },
        "population_frequency": {"EUR": 0.25, "AFR": 0.10, "EAS": 0.30}
    }
}

# =============================================================================
# OMEGA-3 FATTY ACID METABOLISM
# =============================================================================

OMEGA3_GENETICS = {
    # FADS1 - Fatty acid desaturase 1
    "rs174546": {
        "gene": "FADS1",
        "chromosome": "11",
        "function": "Conversion of ALA to EPA/DHA",
        "effect": {
            "CC": {"conversion": "High", "recommendation": "Can convert plant omega-3s efficiently"},
            "CT": {"conversion": "Moderate", "recommendation": "Some conversion ability"},
            "TT": {"conversion": "Low", "recommendation": "Should prioritize fish/algae DHA+EPA directly"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.85, "EAS": 0.55}
    },
    # FADS2 - Fatty acid desaturase 2
    "rs1535": {
        "gene": "FADS2",
        "chromosome": "11",
        "function": "Delta-6 desaturase - first step in omega-3 conversion",
        "effect": {
            "AA": {"d6d_activity": "High", "ala_conversion": "Efficient"},
            "AG": {"d6d_activity": "Moderate", "ala_conversion": "Moderate"},
            "GG": {"d6d_activity": "Low", "ala_conversion": "Poor - need preformed EPA/DHA"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.80, "EAS": 0.50}
    },
    # ELOVL2 - Elongase
    "rs3734398": {
        "gene": "ELOVL2",
        "chromosome": "6",
        "function": "Elongation of EPA to DHA",
        "effect": {
            "CC": {"dha_synthesis": "Efficient", "recommendation": "Good EPA to DHA conversion"},
            "CT": {"dha_synthesis": "Moderate", "recommendation": "Moderate conversion"},
            "TT": {"dha_synthesis": "Less Efficient", "recommendation": "May benefit from direct DHA"}
        },
        "population_frequency": {"EUR": 0.45, "AFR": 0.50, "EAS": 0.55}
    }
}

# =============================================================================
# SATURATED FAT METABOLISM
# =============================================================================

SATURATED_FAT_GENETICS = {
    # APOA2 - Affects response to saturated fat
    "rs5082": {
        "gene": "APOA2",
        "chromosome": "1",
        "function": "Saturated fat and weight/metabolic response",
        "risk_allele": "C",
        "effect": {
            "TT": {"sat_fat_response": "Normal", "weight_risk": "Normal with high sat fat"},
            "TC": {"sat_fat_response": "Slightly Sensitive", "weight_risk": "Moderate risk with high sat fat"},
            "CC": {"sat_fat_response": "Highly Sensitive", "weight_risk": "High obesity risk with sat fat intake"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.25, "EAS": 0.15}
    },
    # APOE - Lipid metabolism
    "rs429358": {
        "gene": "APOE",
        "chromosome": "19",
        "function": "APOE isoform (part 1 of 2) - affects cholesterol response",
        "effect": {
            "TT": {"apoe_partial": "E2/E3", "cholesterol_response": "Lower"},
            "TC": {"apoe_partial": "E3/E4", "cholesterol_response": "Variable"},
            "CC": {"apoe_partial": "E4/E4", "cholesterol_response": "Higher - limit saturated fat"}
        },
        "population_frequency": {"EUR": 0.15, "AFR": 0.25, "EAS": 0.10}
    },
    "rs7412": {
        "gene": "APOE",
        "chromosome": "19",
        "function": "APOE isoform (part 2 of 2)",
        "effect": {
            "CC": {"apoe_partial2": "E3/E4", "status": "Common"},
            "CT": {"apoe_partial2": "E2 carrier", "status": "Protective"},
            "TT": {"apoe_partial2": "E2/E2", "status": "Rare - may affect lipids"}
        },
        "population_frequency": {"EUR": 0.08, "AFR": 0.10, "EAS": 0.05}
    }
}

# =============================================================================
# CARBOHYDRATE METABOLISM
# =============================================================================

CARBOHYDRATE_GENETICS = {
    # AMY1 copy number affects starch digestion (proxy SNP)
    "rs4244372": {
        "gene": "AMY1 region",
        "chromosome": "1",
        "function": "Associated with amylase copy number",
        "effect": {
            "TT": {"amylase_activity": "Higher", "starch_digestion": "Efficient"},
            "TC": {"amylase_activity": "Moderate", "starch_digestion": "Normal"},
            "CC": {"amylase_activity": "Lower", "starch_digestion": "May digest starch slower"}
        },
        "population_frequency": {"EUR": 0.45, "AFR": 0.50, "EAS": 0.55}
    },
    # TCF7L2 - Glucose metabolism and T2D risk
    "rs7903146": {
        "gene": "TCF7L2",
        "chromosome": "10",
        "function": "Strongest genetic risk for type 2 diabetes",
        "risk_allele": "T",
        "effect": {
            "CC": {"t2d_risk": "Normal", "insulin_response": "Normal", "carb_tolerance": "Good"},
            "CT": {"t2d_risk": "Increased (1.4x)", "insulin_response": "Slightly Reduced", "carb_tolerance": "Monitor intake"},
            "TT": {"t2d_risk": "High (2x)", "insulin_response": "Reduced", "carb_tolerance": "Limit refined carbs"}
        },
        "population_frequency": {"EUR": 0.30, "AFR": 0.25, "EAS": 0.05}
    },
    # IRS1 - Insulin signaling
    "rs2943641": {
        "gene": "IRS1",
        "chromosome": "2",
        "function": "Insulin receptor substrate 1",
        "effect": {
            "CC": {"insulin_sensitivity": "Normal", "carb_response": "Normal"},
            "CT": {"insulin_sensitivity": "Slightly Reduced", "carb_response": "Monitor response"},
            "TT": {"insulin_sensitivity": "Reduced", "carb_response": "May benefit from lower carbs"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.20, "EAS": 0.15}
    },
    # SLC2A2 (GLUT2) - Glucose sensing
    "rs5400": {
        "gene": "SLC2A2",
        "chromosome": "3",
        "function": "Glucose transporter 2 - sugar preference",
        "effect": {
            "CC": {"sugar_sensing": "Normal", "sugar_preference": "Normal"},
            "CT": {"sugar_sensing": "Altered", "sugar_preference": "May prefer sweets more"},
            "TT": {"sugar_sensing": "Reduced", "sugar_preference": "Stronger sweet preference"}
        },
        "population_frequency": {"EUR": 0.12, "AFR": 0.08, "EAS": 0.05}
    }
}

# =============================================================================
# PROTEIN METABOLISM
# =============================================================================

PROTEIN_GENETICS = {
    # FTO - Satiety and protein preference
    "rs9939609": {
        "gene": "FTO",
        "chromosome": "16",
        "function": "Fat mass and obesity associated - affects satiety",
        "risk_allele": "A",
        "effect": {
            "TT": {"satiety": "Normal", "protein_benefit": "Standard", "weight_risk": "Normal"},
            "TA": {"satiety": "Slightly Reduced", "protein_benefit": "Moderate - helps satiety", "weight_risk": "Moderate"},
            "AA": {"satiety": "Reduced", "protein_benefit": "High - protein helps control appetite", "weight_risk": "Elevated"}
        },
        "population_frequency": {"EUR": 0.40, "AFR": 0.50, "EAS": 0.15}
    },
    # PPARG - Fat/protein metabolism
    "rs1801282": {
        "gene": "PPARG",
        "chromosome": "3",
        "function": "PPAR-gamma Pro12Ala - metabolic efficiency",
        "effect": {
            "CC": {"metabolic_type": "Normal", "protein_need": "Standard"},
            "CG": {"metabolic_type": "More Efficient", "protein_need": "May process nutrients better"},
            "GG": {"metabolic_type": "Highly Efficient", "protein_need": "Very efficient metabolism"}
        },
        "population_frequency": {"EUR": 0.12, "AFR": 0.03, "EAS": 0.04}
    }
}

# =============================================================================
# SODIUM SENSITIVITY
# =============================================================================

SODIUM_GENETICS = {
    # ACE - Angiotensin converting enzyme
    "rs4343": {
        "gene": "ACE",
        "chromosome": "17",
        "function": "ACE activity - blood pressure salt response",
        "effect": {
            "AA": {"ace_activity": "Lower", "salt_sensitivity": "Lower", "bp_response": "Less sensitive to salt"},
            "AG": {"ace_activity": "Moderate", "salt_sensitivity": "Moderate", "bp_response": "Normal sensitivity"},
            "GG": {"ace_activity": "Higher", "salt_sensitivity": "Higher", "bp_response": "More sensitive - limit sodium"}
        },
        "population_frequency": {"EUR": 0.50, "AFR": 0.35, "EAS": 0.40}
    },
    # AGT - Angiotensinogen
    "rs699": {
        "gene": "AGT",
        "chromosome": "1",
        "function": "Angiotensinogen M235T",
        "risk_allele": "T",
        "effect": {
            "CC": {"agt_level": "Lower", "salt_sensitivity": "Lower", "hypertension_risk": "Lower"},
            "CT": {"agt_level": "Moderate", "salt_sensitivity": "Moderate", "hypertension_risk": "Average"},
            "TT": {"agt_level": "Higher", "salt_sensitivity": "Higher", "hypertension_risk": "Elevated - watch sodium"}
        },
        "population_frequency": {"EUR": 0.42, "AFR": 0.85, "EAS": 0.75}
    },
    # ADD1 - Alpha-adducin
    "rs4961": {
        "gene": "ADD1",
        "chromosome": "4",
        "function": "Alpha-adducin Gly460Trp - renal sodium handling",
        "effect": {
            "GG": {"sodium_reabsorption": "Normal", "salt_sensitivity": "Normal"},
            "GT": {"sodium_reabsorption": "Increased", "salt_sensitivity": "Moderate"},
            "TT": {"sodium_reabsorption": "High", "salt_sensitivity": "High - salt-sensitive hypertension risk"}
        },
        "population_frequency": {"EUR": 0.20, "AFR": 0.10, "EAS": 0.50}
    }
}

# =============================================================================
# VITAMIN D METABOLISM
# =============================================================================

VITAMIN_D_GENETICS = {
    # GC (VDBP) - Vitamin D binding protein
    "rs2282679": {
        "gene": "GC",
        "chromosome": "4",
        "variant_name": "Intronic",
        "function": "Vitamin D binding protein - major determinant of D levels",
        "effect": {
            "TT": {"vit_d_status": "Higher levels likely", "transport": "Efficient"},
            "GT": {"vit_d_status": "Normal levels", "transport": "Normal"},
            "GG": {"vit_d_status": "Lower levels likely", "transport": "Reduced", "recommendation": "May need higher vitamin D intake"}
        },
        "population_frequency": {"EUR": 0.28, "AFR": 0.08, "EAS": 0.03}
    },
    "rs7041": {
        "gene": "GC",
        "chromosome": "4",
        "variant_name": "D416E",
        "function": "Vitamin D binding protein isoform",
        "effect": {
            "GG": {"gc_type": "Gc1f-1f", "d_levels": "Higher"},
            "GT": {"gc_type": "Gc1f-1s/2", "d_levels": "Moderate"},
            "TT": {"gc_type": "Gc1s/2", "d_levels": "Lower tendency"}
        },
        "population_frequency": {"EUR": 0.42, "AFR": 0.86, "EAS": 0.25}
    },
    # CYP2R1 - 25-hydroxylase (converts D to 25-OH-D)
    "rs10741657": {
        "gene": "CYP2R1",
        "chromosome": "11",
        "variant_name": "Upstream",
        "function": "Vitamin D 25-hydroxylation (liver activation)",
        "effect": {
            "GG": {"hydroxylation": "Normal", "conversion": "Efficient"},
            "GA": {"hydroxylation": "Slightly reduced", "conversion": "Moderate"},
            "AA": {"hydroxylation": "Reduced", "conversion": "May need higher D3 intake"}
        },
        "population_frequency": {"EUR": 0.40, "AFR": 0.15, "EAS": 0.55}
    },
    # VDR - Vitamin D receptor
    "rs1544410": {
        "gene": "VDR",
        "chromosome": "12",
        "variant_name": "BsmI",
        "function": "Vitamin D receptor - affects D action in cells",
        "effect": {
            "CC": {"vdr_activity": "Normal", "d_response": "Good response"},
            "CT": {"vdr_activity": "Slightly altered", "d_response": "Normal"},
            "TT": {"vdr_activity": "Altered", "d_response": "May need higher levels"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.10, "EAS": 0.06}
    },
    "rs2228570": {
        "gene": "VDR",
        "chromosome": "12",
        "variant_name": "FokI",
        "function": "VDR start codon variant - affects receptor function",
        "effect": {
            "CC": {"vdr_function": "Full-length VDR", "activity": "Slightly reduced"},
            "CT": {"vdr_function": "Mixed", "activity": "Normal"},
            "TT": {"vdr_function": "Shorter VDR", "activity": "More active"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.30, "EAS": 0.45}
    },
    "rs731236": {
        "gene": "VDR",
        "chromosome": "12",
        "variant_name": "TaqI",
        "function": "VDR TaqI polymorphism",
        "effect": {
            "TT": {"vdr_variant": "TaqI T", "bone_density": "May affect"},
            "TC": {"vdr_variant": "Heterozygous", "bone_density": "Normal"},
            "CC": {"vdr_variant": "TaqI C", "bone_density": "Normal"}
        },
        "population_frequency": {"EUR": 0.40, "AFR": 0.25, "EAS": 0.08}
    },
    # DHCR7 - Skin vitamin D synthesis
    "rs12785878": {
        "gene": "DHCR7",
        "chromosome": "11",
        "variant_name": "Intronic",
        "function": "7-dehydrocholesterol reductase - skin D synthesis",
        "effect": {
            "TT": {"skin_synthesis": "Normal", "sun_response": "Good"},
            "GT": {"skin_synthesis": "Slightly reduced", "sun_response": "Normal"},
            "GG": {"skin_synthesis": "Reduced", "sun_response": "May make less D from sun"}
        },
        "population_frequency": {"EUR": 0.25, "AFR": 0.02, "EAS": 0.05}
    }
}

# =============================================================================
# IRON METABOLISM
# =============================================================================

IRON_GENETICS = {
    # HFE - Hereditary hemochromatosis
    "rs1800562": {
        "gene": "HFE",
        "chromosome": "6",
        "variant_name": "C282Y",
        "function": "HFE C282Y - hereditary hemochromatosis major mutation",
        "effect": {
            "GG": {"hfe_status": "Normal", "iron_absorption": "Normal", "hemochromatosis_risk": "No"},
            "GA": {"hfe_status": "Carrier", "iron_absorption": "Slightly increased", "hemochromatosis_risk": "Carrier only"},
            "AA": {"hfe_status": "Homozygous", "iron_absorption": "Significantly increased", "hemochromatosis_risk": "High - monitor ferritin"}
        },
        "population_frequency": {"EUR": 0.06, "AFR": 0.001, "EAS": 0.001}
    },
    "rs1799945": {
        "gene": "HFE",
        "chromosome": "6",
        "variant_name": "H63D",
        "function": "HFE H63D - minor hemochromatosis variant",
        "effect": {
            "CC": {"hfe_h63d": "Normal", "iron_status": "Normal"},
            "CG": {"hfe_h63d": "Carrier", "iron_status": "May have slightly higher iron"},
            "GG": {"hfe_h63d": "Homozygous", "iron_status": "May have elevated iron"}
        },
        "population_frequency": {"EUR": 0.15, "AFR": 0.02, "EAS": 0.02}
    },
    # TMPRSS6 - Iron deficiency susceptibility
    "rs855791": {
        "gene": "TMPRSS6",
        "chromosome": "22",
        "variant_name": "A736V",
        "function": "Matriptase-2 - affects hepcidin and iron absorption",
        "effect": {
            "CC": {"iron_absorption": "Higher", "anemia_risk": "Lower"},
            "CT": {"iron_absorption": "Normal", "anemia_risk": "Normal"},
            "TT": {"iron_absorption": "Lower", "anemia_risk": "Higher - may need more iron"}
        },
        "population_frequency": {"EUR": 0.45, "AFR": 0.20, "EAS": 0.60}
    },
    # TF - Transferrin
    "rs3811647": {
        "gene": "TF",
        "chromosome": "3",
        "variant_name": "Intronic",
        "function": "Transferrin - iron transport protein",
        "effect": {
            "GG": {"transferrin": "Normal", "iron_transport": "Efficient"},
            "GA": {"transferrin": "Slightly altered", "iron_transport": "Normal"},
            "AA": {"transferrin": "Lower levels", "iron_transport": "May be less efficient"}
        },
        "population_frequency": {"EUR": 0.35, "AFR": 0.25, "EAS": 0.45}
    },
    # TFR2 - Transferrin receptor 2
    "rs7385804": {
        "gene": "TFR2",
        "chromosome": "7",
        "variant_name": "Intronic",
        "function": "Transferrin receptor - cellular iron uptake",
        "effect": {
            "AA": {"tfr2_function": "Normal", "iron_uptake": "Normal"},
            "AC": {"tfr2_function": "Slightly altered", "iron_uptake": "Normal"},
            "CC": {"tfr2_function": "Variant", "iron_uptake": "May be altered"}
        },
        "population_frequency": {"EUR": 0.30, "AFR": 0.20, "EAS": 0.15}
    }
}

# =============================================================================
# ZINC METABOLISM
# =============================================================================

ZINC_GENETICS = {
    # SLC30A8 - Zinc transporter (also affects insulin)
    "rs13266634": {
        "gene": "SLC30A8",
        "chromosome": "8",
        "variant_name": "R325W",
        "function": "Zinc transporter in pancreatic cells",
        "effect": {
            "CC": {"zinc_transport": "Normal", "diabetes_risk": "Normal"},
            "CT": {"zinc_transport": "Slightly altered", "diabetes_risk": "Slightly reduced"},
            "TT": {"zinc_transport": "Altered", "diabetes_risk": "Reduced (protective)"}
        },
        "population_frequency": {"EUR": 0.30, "AFR": 0.05, "EAS": 0.40}
    },
    # SLC39A4 - ZIP4 zinc transporter
    "rs1871534": {
        "gene": "SLC39A4",
        "chromosome": "8",
        "variant_name": "Intronic",
        "function": "ZIP4 - intestinal zinc absorption",
        "effect": {
            "GG": {"zinc_absorption": "Normal", "status": "Efficient"},
            "GA": {"zinc_absorption": "Slightly reduced", "status": "Normal"},
            "AA": {"zinc_absorption": "Reduced", "status": "May need more zinc"}
        },
        "population_frequency": {"EUR": 0.15, "AFR": 0.10, "EAS": 0.08}
    },
    # CA6 - Gustin (zinc-dependent taste)
    "rs2274333": {
        "gene": "CA6",
        "chromosome": "1",
        "variant_name": "S90G",
        "function": "Gustin - zinc binding protein affecting taste",
        "effect": {
            "GG": {"gustin_function": "Normal", "zinc_taste": "Normal"},
            "AG": {"gustin_function": "Slightly reduced", "zinc_taste": "May be altered"},
            "AA": {"gustin_function": "Reduced", "zinc_taste": "May affect taste perception"}
        },
        "population_frequency": {"EUR": 0.30, "AFR": 0.25, "EAS": 0.35}
    }
}

# =============================================================================
# MAGNESIUM METABOLISM
# =============================================================================

MAGNESIUM_GENETICS = {
    # TRPM6 - Magnesium channel
    "rs2274924": {
        "gene": "TRPM6",
        "chromosome": "9",
        "variant_name": "V1393I",
        "function": "Primary magnesium absorption channel",
        "effect": {
            "CC": {"mg_absorption": "Normal", "status": "Efficient"},
            "CT": {"mg_absorption": "Slightly reduced", "status": "Normal"},
            "TT": {"mg_absorption": "Reduced", "status": "May need more magnesium"}
        },
        "population_frequency": {"EUR": 0.20, "AFR": 0.15, "EAS": 0.25}
    },
    # TRPM7 - Magnesium homeostasis
    "rs8042919": {
        "gene": "TRPM7",
        "chromosome": "15",
        "variant_name": "T1482I",
        "function": "Magnesium homeostasis and cellular transport",
        "effect": {
            "CC": {"mg_homeostasis": "Normal", "cellular_mg": "Normal"},
            "CT": {"mg_homeostasis": "Slightly altered", "cellular_mg": "Normal"},
            "TT": {"mg_homeostasis": "Altered", "cellular_mg": "May be lower"}
        },
        "population_frequency": {"EUR": 0.15, "AFR": 0.10, "EAS": 0.20}
    },
    # CNNM2 - Magnesium reabsorption
    "rs7914558": {
        "gene": "CNNM2",
        "chromosome": "10",
        "variant_name": "Intronic",
        "function": "Renal magnesium reabsorption",
        "effect": {
            "GG": {"mg_reabsorption": "Normal", "kidney_mg": "Efficient"},
            "AG": {"mg_reabsorption": "Slightly reduced", "kidney_mg": "Normal"},
            "AA": {"mg_reabsorption": "Reduced", "kidney_mg": "May lose more Mg in urine"}
        },
        "population_frequency": {"EUR": 0.45, "AFR": 0.30, "EAS": 0.55}
    },
    # ATP2B1 - Calcium/Magnesium ATPase
    "rs2681472": {
        "gene": "ATP2B1",
        "chromosome": "12",
        "variant_name": "Intronic",
        "function": "Calcium/Magnesium pump - affects blood pressure",
        "effect": {
            "AA": {"pump_activity": "Normal", "bp_effect": "Normal"},
            "AG": {"pump_activity": "Slightly altered", "bp_effect": "May affect BP"},
            "GG": {"pump_activity": "Altered", "bp_effect": "May need more Mg for BP"}
        },
        "population_frequency": {"EUR": 0.20, "AFR": 0.35, "EAS": 0.15}
    }
}

# =============================================================================
# CALCIUM METABOLISM
# =============================================================================

CALCIUM_GENETICS = {
    # CASR - Calcium sensing receptor
    "rs1801725": {
        "gene": "CASR",
        "chromosome": "3",
        "variant_name": "A986S",
        "function": "Calcium sensing receptor - regulates PTH and calcium",
        "effect": {
            "GG": {"casr_function": "Normal", "calcium_sensing": "Normal"},
            "GT": {"casr_function": "Slightly altered", "calcium_sensing": "May have higher calcium"},
            "TT": {"casr_function": "Altered", "calcium_sensing": "Higher serum calcium tendency"}
        },
        "population_frequency": {"EUR": 0.15, "AFR": 0.05, "EAS": 0.03}
    },
    # CLDN14 - Claudin 14 (kidney calcium handling)
    "rs219780": {
        "gene": "CLDN14",
        "chromosome": "21",
        "variant_name": "Intronic",
        "function": "Kidney calcium reabsorption - kidney stone risk",
        "effect": {
            "CC": {"kidney_calcium": "Normal", "stone_risk": "Normal"},
            "CT": {"kidney_calcium": "Slightly altered", "stone_risk": "Slightly elevated"},
            "TT": {"kidney_calcium": "Higher excretion", "stone_risk": "Elevated kidney stone risk"}
        },
        "population_frequency": {"EUR": 0.25, "AFR": 0.15, "EAS": 0.10}
    },
    # DGKD - Kidney stone susceptibility
    "rs838717": {
        "gene": "DGKD",
        "chromosome": "2",
        "variant_name": "Intronic",
        "function": "Kidney stone formation risk",
        "effect": {
            "GG": {"stone_risk": "Normal", "calcium_handling": "Normal"},
            "GA": {"stone_risk": "Slightly elevated", "calcium_handling": "Normal"},
            "AA": {"stone_risk": "Elevated", "calcium_handling": "May need to monitor calcium"}
        },
        "population_frequency": {"EUR": 0.30, "AFR": 0.20, "EAS": 0.25}
    }
}

# =============================================================================
# SELENIUM METABOLISM
# =============================================================================

SELENIUM_GENETICS = {
    # GPX1 - Glutathione peroxidase (selenium enzyme)
    "rs1050450": {
        "gene": "GPX1",
        "chromosome": "3",
        "variant_name": "P198L",
        "function": "Selenium-dependent antioxidant enzyme",
        "effect": {
            "CC": {"gpx1_activity": "Normal", "selenium_use": "Efficient"},
            "CT": {"gpx1_activity": "Slightly reduced", "selenium_use": "Normal"},
            "TT": {"gpx1_activity": "Reduced", "selenium_use": "May need more selenium"}
        },
        "population_frequency": {"EUR": 0.30, "AFR": 0.45, "EAS": 0.10}
    },
    # SEPP1 - Selenoprotein P
    "rs3877899": {
        "gene": "SEPP1",
        "chromosome": "5",
        "variant_name": "A234T",
        "function": "Selenium transport protein",
        "effect": {
            "GG": {"sepp1_function": "Normal", "selenium_transport": "Efficient"},
            "GA": {"sepp1_function": "Slightly reduced", "selenium_transport": "Normal"},
            "AA": {"sepp1_function": "Reduced", "selenium_transport": "May have lower selenium"}
        },
        "population_frequency": {"EUR": 0.15, "AFR": 0.25, "EAS": 0.05}
    },
    # SEP15/SELENOF
    "rs5845": {
        "gene": "SELENOF",
        "chromosome": "1",
        "variant_name": "1125G/A",
        "function": "Selenoprotein F - antioxidant",
        "effect": {
            "GG": {"selenof_function": "Normal", "antioxidant": "Normal"},
            "GA": {"selenof_function": "Slightly altered", "antioxidant": "Normal"},
            "AA": {"selenof_function": "Altered", "antioxidant": "May need more selenium"}
        },
        "population_frequency": {"EUR": 0.25, "AFR": 0.35, "EAS": 0.15}
    }
}

# =============================================================================
# LACTOSE TOLERANCE
# =============================================================================

LACTOSE_GENETICS = {
    # MCM6/LCT - Lactase persistence
    "rs4988235": {
        "gene": "MCM6/LCT",
        "chromosome": "2",
        "variant_name": "-13910C/T",
        "function": "Lactase persistence - ability to digest milk as adult",
        "effect": {
            "TT": {"lactase_persistence": "Yes", "lactose_tolerance": "Tolerant", "milk_digestion": "Can digest lactose"},
            "CT": {"lactase_persistence": "Partial", "lactose_tolerance": "Likely tolerant", "milk_digestion": "Usually can digest"},
            "CC": {"lactase_persistence": "No", "lactose_tolerance": "Intolerant", "milk_digestion": "Cannot digest lactose well"}
        },
        "population_frequency": {"EUR": 0.75, "AFR": 0.15, "EAS": 0.01}
    },
    # Secondary lactase persistence variant (African)
    "rs145946881": {
        "gene": "MCM6/LCT",
        "chromosome": "2",
        "variant_name": "-14010G/C",
        "function": "African lactase persistence variant",
        "effect": {
            "GG": {"lactase_african": "Non-persistent", "tolerance": "May be intolerant"},
            "GC": {"lactase_african": "Persistent", "tolerance": "Likely tolerant"},
            "CC": {"lactase_african": "Persistent", "tolerance": "Tolerant"}
        },
        "population_frequency": {"EUR": 0.001, "AFR": 0.20, "EAS": 0.001}
    }
}

# =============================================================================
# GLUTEN SENSITIVITY (Celiac HLA markers)
# =============================================================================

GLUTEN_GENETICS = {
    # HLA-DQ2.5 proxy
    "rs2187668": {
        "gene": "HLA-DQA1",
        "chromosome": "6",
        "variant_name": "DQ2.5 proxy",
        "function": "HLA-DQ2.5 celiac disease susceptibility",
        "effect": {
            "CC": {"hla_dq2": "Non-carrier", "celiac_risk": "Lower", "gluten_sensitivity": "Lower risk"},
            "CT": {"hla_dq2": "Carrier", "celiac_risk": "Elevated", "gluten_sensitivity": "May be susceptible"},
            "TT": {"hla_dq2": "Homozygous", "celiac_risk": "High", "gluten_sensitivity": "High risk if exposed to gluten"}
        },
        "population_frequency": {"EUR": 0.25, "AFR": 0.05, "EAS": 0.02}
    },
    # HLA-DQ8 proxy
    "rs7454108": {
        "gene": "HLA-DQB1",
        "chromosome": "6",
        "variant_name": "DQ8 proxy",
        "function": "HLA-DQ8 celiac disease susceptibility",
        "effect": {
            "CC": {"hla_dq8": "Non-carrier", "celiac_risk": "Lower"},
            "CT": {"hla_dq8": "Carrier", "celiac_risk": "Elevated"},
            "TT": {"hla_dq8": "Homozygous", "celiac_risk": "High"}
        },
        "population_frequency": {"EUR": 0.15, "AFR": 0.05, "EAS": 0.05}
    }
}

# =============================================================================
# CHOLINE METABOLISM
# =============================================================================

CHOLINE_GENETICS = {
    # PEMT - Phosphatidylethanolamine N-methyltransferase
    "rs12325817": {
        "gene": "PEMT",
        "chromosome": "17",
        "variant_name": "G/C",
        "function": "Endogenous choline synthesis",
        "effect": {
            "GG": {"choline_synthesis": "Normal", "dietary_need": "Standard"},
            "GC": {"choline_synthesis": "Reduced", "dietary_need": "Slightly higher"},
            "CC": {"choline_synthesis": "Significantly reduced", "dietary_need": "Higher - need more dietary choline"}
        },
        "population_frequency": {"EUR": 0.45, "AFR": 0.30, "EAS": 0.50}
    },
    # CHDH - Choline dehydrogenase
    "rs12676": {
        "gene": "CHDH",
        "chromosome": "3",
        "variant_name": "G/T",
        "function": "Choline oxidation to betaine",
        "effect": {
            "GG": {"choline_oxidation": "Normal", "betaine_production": "Normal"},
            "GT": {"choline_oxidation": "Slightly reduced", "betaine_production": "Normal"},
            "TT": {"choline_oxidation": "Reduced", "betaine_production": "May be lower"}
        },
        "population_frequency": {"EUR": 0.20, "AFR": 0.15, "EAS": 0.10}
    }
}

# =============================================================================
# CAFFEINE METABOLISM
# =============================================================================

CAFFEINE_GENETICS = {
    # CYP1A2 - Primary caffeine metabolism
    "rs762551": {
        "gene": "CYP1A2",
        "chromosome": "15",
        "variant_name": "-163C/A",
        "function": "Primary caffeine metabolizing enzyme",
        "effect": {
            "AA": {"caffeine_metabolism": "Fast", "sensitivity": "Low", "recommendation": "Can tolerate higher caffeine"},
            "CA": {"caffeine_metabolism": "Moderate", "sensitivity": "Moderate", "recommendation": "Moderate caffeine intake"},
            "CC": {"caffeine_metabolism": "Slow", "sensitivity": "High", "recommendation": "Limit caffeine - stays in system longer"}
        },
        "population_frequency": {"EUR": 0.50, "AFR": 0.45, "EAS": 0.35}
    },
    # ADORA2A - Adenosine receptor (caffeine anxiety)
    "rs5751876": {
        "gene": "ADORA2A",
        "chromosome": "22",
        "variant_name": "1976T/C",
        "function": "Adenosine receptor - caffeine anxiety response",
        "effect": {
            "TT": {"anxiety_response": "Normal", "caffeine_anxiety": "Lower risk"},
            "TC": {"anxiety_response": "Moderate", "caffeine_anxiety": "Moderate risk"},
            "CC": {"anxiety_response": "Increased", "caffeine_anxiety": "Higher anxiety risk with caffeine"}
        },
        "population_frequency": {"EUR": 0.45, "AFR": 0.35, "EAS": 0.50}
    },
    # AHR - Aryl hydrocarbon receptor
    "rs4410790": {
        "gene": "AHR",
        "chromosome": "7",
        "variant_name": "Intronic",
        "function": "Caffeine metabolism regulator",
        "effect": {
            "TT": {"ahr_activity": "Normal", "caffeine_clearance": "Normal"},
            "TC": {"ahr_activity": "Slightly increased", "caffeine_clearance": "Slightly faster"},
            "CC": {"ahr_activity": "Increased", "caffeine_clearance": "Faster metabolism"}
        },
        "population_frequency": {"EUR": 0.40, "AFR": 0.30, "EAS": 0.45}
    }
}

# =============================================================================
# ALCOHOL METABOLISM
# =============================================================================

ALCOHOL_GENETICS = {
    # ADH1B - Alcohol dehydrogenase
    "rs1229984": {
        "gene": "ADH1B",
        "chromosome": "4",
        "function": "Alcohol to acetaldehyde conversion speed",
        "common_name": "ADH1B*2 (fast metabolizer)",
        "effect": {
            "CC": {"adh_activity": "Normal", "alcohol_to_acetaldehyde": "Normal speed", "flushing": "Unlikely"},
            "CT": {"adh_activity": "Fast", "alcohol_to_acetaldehyde": "Fast - acetaldehyde buildup", "flushing": "May occur"},
            "TT": {"adh_activity": "Very Fast", "alcohol_to_acetaldehyde": "Very Fast - rapid acetaldehyde", "flushing": "Likely (Asian flush)"}
        },
        "population_frequency": {"EUR": 0.03, "AFR": 0.02, "EAS": 0.70}
    },
    # ALDH2 - Acetaldehyde metabolism
    "rs671": {
        "gene": "ALDH2",
        "chromosome": "12",
        "function": "Acetaldehyde clearance (ALDH2*2)",
        "common_name": "ALDH2 deficiency (Asian flush)",
        "effect": {
            "GG": {"aldh2_activity": "Normal", "acetaldehyde_clearance": "Efficient", "alcohol_tolerance": "Normal"},
            "GA": {"aldh2_activity": "Reduced (~50%)", "acetaldehyde_clearance": "Slow - buildup", "alcohol_tolerance": "Reduced - flushing, nausea"},
            "AA": {"aldh2_activity": "Very Low (~5%)", "acetaldehyde_clearance": "Very Slow", "alcohol_tolerance": "Very Low - severe reaction"}
        },
        "population_frequency": {"EUR": 0.001, "AFR": 0.001, "EAS": 0.30}
    },
    # CYP2E1 - Additional alcohol metabolism
    "rs2031920": {
        "gene": "CYP2E1",
        "chromosome": "10",
        "function": "Microsomal alcohol oxidation",
        "effect": {
            "CC": {"cyp2e1_activity": "Normal", "metabolism": "Standard"},
            "CT": {"cyp2e1_activity": "Increased", "metabolism": "Faster - may reduce intoxication"},
            "TT": {"cyp2e1_activity": "High", "metabolism": "Rapid - but more toxic metabolites"}
        },
        "population_frequency": {"EUR": 0.02, "AFR": 0.05, "EAS": 0.25}
    }
}


# =============================================================================
# MAIN ANALYSIS FUNCTION
# =============================================================================

def analyze_nutrition_metabolism(dna_data: dict) -> Dict[str, Any]:
    """
    Perform comprehensive nutrition and metabolism genetic analysis.

    Args:
        dna_data: Dictionary of rsid -> genotype

    Returns:
        Dictionary containing all nutrition metabolism analysis results
    """
    results = {
        "vitamin_a_metabolism": analyze_vitamin_a(dna_data),
        "vitamin_b12_metabolism": analyze_vitamin_b12(dna_data),
        "vitamin_c_metabolism": analyze_vitamin_c(dna_data),
        "vitamin_e_metabolism": analyze_vitamin_e(dna_data),
        "omega3_metabolism": analyze_omega3(dna_data),
        "saturated_fat_response": analyze_saturated_fat(dna_data),
        "carbohydrate_metabolism": analyze_carbohydrate(dna_data),
        "protein_metabolism": analyze_protein(dna_data),
        "sodium_sensitivity": analyze_sodium(dna_data),
        "alcohol_metabolism": analyze_alcohol(dna_data),
        "summary": {}
    }

    # Generate overall summary
    results["summary"] = generate_nutrition_summary(results)

    return results


def analyze_vitamin_a(dna_data: dict) -> Dict[str, Any]:
    """Analyze vitamin A / beta-carotene metabolism"""
    result = {
        "snps_analyzed": [],
        "conversion_efficiency": "Unknown",
        "beta_carotene_converter": "Unknown",
        "recommendation": "",
        "findings": []
    }

    conversion_scores = []

    for rsid, info in VITAMIN_A_GENETICS.items():
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
                if "conversion_efficiency" in effect:
                    result["conversion_efficiency"] = effect["conversion_efficiency"]
                    if "Poor" in effect["conversion_efficiency"]:
                        conversion_scores.append(0)
                        result["findings"].append("Poor beta-carotene to vitamin A conversion")
                    elif "Reduced" in effect["conversion_efficiency"]:
                        conversion_scores.append(1)
                    else:
                        conversion_scores.append(2)

                if effect.get("recommendation"):
                    result["recommendation"] = effect["recommendation"]

    if conversion_scores:
        avg = sum(conversion_scores) / len(conversion_scores)
        if avg <= 0.5:
            result["beta_carotene_converter"] = "Poor Converter"
        elif avg <= 1.5:
            result["beta_carotene_converter"] = "Moderate Converter"
        else:
            result["beta_carotene_converter"] = "Good Converter"

    return result


def analyze_vitamin_b12(dna_data: dict) -> Dict[str, Any]:
    """Analyze vitamin B12 metabolism"""
    result = {
        "snps_analyzed": [],
        "secretor_status": "Unknown",
        "b12_transport": "Unknown",
        "mthfr_status": "Unknown",
        "overall_b12_need": "Normal",
        "findings": []
    }

    risk_count = 0

    for rsid, info in VITAMIN_B12_GENETICS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            effects = info.get("effect", {})

            result["snps_analyzed"].append({
                "rsid": rsid,
                "gene": info.get("gene", ""),
                "genotype": genotype,
                "common_name": info.get("common_name", "")
            })

            _key = get_genotype_key(genotype, effects)
            if _key:

                effect = effects[_key]

                # Secretor status
                if "secretor_status" in effect:
                    result["secretor_status"] = effect["secretor_status"]
                    if effect["secretor_status"] == "Non-Secretor":
                        risk_count += 1
                        result["findings"].append("Non-secretor - may have reduced B12 absorption")

                # Transport
                if "b12_transport" in effect:
                    result["b12_transport"] = effect["b12_transport"]
                    if "Reduced" in effect["b12_transport"]:
                        risk_count += 1

                # MTHFR
                if "mthfr_activity" in effect:
                    result["mthfr_status"] = effect["mthfr_activity"]
                    if "Low" in effect["mthfr_activity"]:
                        risk_count += 2
                        result["findings"].append("MTHFR C677T TT - reduced enzyme activity, needs active folate")
                    elif "Reduced" in effect["mthfr_activity"]:
                        risk_count += 1

    if risk_count >= 3:
        result["overall_b12_need"] = "Increased"
    elif risk_count >= 1:
        result["overall_b12_need"] = "Slightly Increased"

    return result


def analyze_vitamin_c(dna_data: dict) -> Dict[str, Any]:
    """Analyze vitamin C metabolism"""
    result = {
        "snps_analyzed": [],
        "vitamin_c_transport": "Unknown",
        "antioxidant_capacity": "Unknown",
        "findings": []
    }

    for rsid, info in VITAMIN_C_GENETICS.items():
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

                if "vit_c_transport" in effect:
                    result["vitamin_c_transport"] = effect["vit_c_transport"]
                    if "Reduced" in effect["vit_c_transport"]:
                        result["findings"].append("Reduced vitamin C transport - may need higher intake")

                if "antioxidant_activity" in effect:
                    result["antioxidant_capacity"] = effect["antioxidant_activity"]
                    if "Low" in effect["antioxidant_activity"]:
                        result["findings"].append("Lower antioxidant enzyme activity - increased antioxidant needs")

    return result


def analyze_vitamin_e(dna_data: dict) -> Dict[str, Any]:
    """Analyze vitamin E metabolism"""
    result = {
        "snps_analyzed": [],
        "vitamin_e_retention": "Unknown",
        "metabolism_rate": "Unknown",
        "findings": []
    }

    for rsid, info in VITAMIN_E_GENETICS.items():
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

                if "vit_e_status" in effect:
                    result["vitamin_e_retention"] = effect["vit_e_status"]
                    if "Low" in effect["vit_e_status"]:
                        result["findings"].append("Lower vitamin E retention - may benefit from higher intake")

                if "vit_e_metabolism" in effect:
                    result["metabolism_rate"] = effect["vit_e_metabolism"]

    return result


def analyze_omega3(dna_data: dict) -> Dict[str, Any]:
    """Analyze omega-3 fatty acid metabolism"""
    result = {
        "snps_analyzed": [],
        "ala_to_epa_conversion": "Unknown",
        "epa_to_dha_conversion": "Unknown",
        "overall_conversion_ability": "Unknown",
        "recommendation": "",
        "findings": []
    }

    conversion_score = 0
    snps_found = 0

    for rsid, info in OMEGA3_GENETICS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            effects = info.get("effect", {})
            snps_found += 1

            result["snps_analyzed"].append({
                "rsid": rsid,
                "gene": info.get("gene", ""),
                "genotype": genotype
            })

            _key = get_genotype_key(genotype, effects)
            if _key:

                effect = effects[_key]

                if info.get("gene") == "FADS1":
                    result["ala_to_epa_conversion"] = effect.get("conversion", "Unknown")
                    if effect.get("conversion") == "High":
                        conversion_score += 2
                    elif effect.get("conversion") == "Moderate":
                        conversion_score += 1
                    else:
                        result["findings"].append("Low omega-3 conversion - need preformed EPA/DHA")

                if info.get("gene") == "ELOVL2":
                    result["epa_to_dha_conversion"] = effect.get("dha_synthesis", "Unknown")

    if snps_found > 0:
        if conversion_score >= 3:
            result["overall_conversion_ability"] = "Good"
            result["recommendation"] = "Can convert plant omega-3s (ALA) efficiently"
        elif conversion_score >= 1:
            result["overall_conversion_ability"] = "Moderate"
            result["recommendation"] = "Some conversion ability - supplement with fish oil recommended"
        else:
            result["overall_conversion_ability"] = "Poor"
            result["recommendation"] = "Should get omega-3s directly from fish or algae oil (EPA/DHA)"

    return result


def analyze_saturated_fat(dna_data: dict) -> Dict[str, Any]:
    """Analyze saturated fat metabolism response"""
    result = {
        "snps_analyzed": [],
        "sat_fat_sensitivity": "Unknown",
        "apoe_status": "Unknown",
        "weight_risk_with_sat_fat": "Unknown",
        "recommendation": "",
        "findings": []
    }

    for rsid, info in SATURATED_FAT_GENETICS.items():
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

                if "sat_fat_response" in effect:
                    result["sat_fat_sensitivity"] = effect["sat_fat_response"]
                    if "Highly Sensitive" in effect["sat_fat_response"]:
                        result["findings"].append("APOA2 CC - weight gain risk with high saturated fat")
                        result["recommendation"] = "Limit saturated fat intake"

                if "apoe_partial" in effect:
                    result["apoe_status"] = effect["apoe_partial"]
                    if "E4" in effect["apoe_partial"]:
                        result["findings"].append("APOE4 carrier - cholesterol more responsive to sat fat")

                if "weight_risk" in effect:
                    result["weight_risk_with_sat_fat"] = effect["weight_risk"]

    return result


def analyze_carbohydrate(dna_data: dict) -> Dict[str, Any]:
    """Analyze carbohydrate metabolism"""
    result = {
        "snps_analyzed": [],
        "starch_digestion": "Unknown",
        "insulin_response": "Unknown",
        "t2d_genetic_risk": "Unknown",
        "sugar_preference": "Unknown",
        "recommendation": "",
        "findings": []
    }

    risk_score = 0

    for rsid, info in CARBOHYDRATE_GENETICS.items():
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

                if "starch_digestion" in effect:
                    result["starch_digestion"] = effect["starch_digestion"]

                if "t2d_risk" in effect:
                    result["t2d_genetic_risk"] = effect["t2d_risk"]
                    if "High" in effect["t2d_risk"]:
                        risk_score += 2
                        result["findings"].append("TCF7L2 TT - significantly elevated T2D genetic risk")
                    elif "Increased" in effect["t2d_risk"]:
                        risk_score += 1

                if "insulin_response" in effect:
                    result["insulin_response"] = effect["insulin_response"]
                    if "Reduced" in effect["insulin_response"]:
                        result["recommendation"] = "Consider lower glycemic index foods"

                if "sugar_preference" in effect:
                    result["sugar_preference"] = effect["sugar_preference"]
                    if "Stronger" in effect["sugar_preference"]:
                        result["findings"].append("Genetic tendency for stronger sweet preference")

    return result


def analyze_protein(dna_data: dict) -> Dict[str, Any]:
    """Analyze protein metabolism"""
    result = {
        "snps_analyzed": [],
        "satiety_response": "Unknown",
        "protein_benefit": "Unknown",
        "metabolic_efficiency": "Unknown",
        "findings": []
    }

    for rsid, info in PROTEIN_GENETICS.items():
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

                if "satiety" in effect:
                    result["satiety_response"] = effect["satiety"]
                    if "Reduced" in effect["satiety"]:
                        result["findings"].append("FTO risk variant - may experience reduced satiety")

                if "protein_benefit" in effect:
                    result["protein_benefit"] = effect["protein_benefit"]
                    if "High" in effect["protein_benefit"]:
                        result["findings"].append("Higher protein intake may help with appetite control")

                if "metabolic_type" in effect:
                    result["metabolic_efficiency"] = effect["metabolic_type"]

    return result


def analyze_sodium(dna_data: dict) -> Dict[str, Any]:
    """Analyze sodium sensitivity"""
    result = {
        "snps_analyzed": [],
        "salt_sensitivity": "Unknown",
        "blood_pressure_response": "Unknown",
        "hypertension_risk": "Unknown",
        "recommendation": "",
        "findings": []
    }

    sensitivity_score = 0
    snps_found = 0

    for rsid, info in SODIUM_GENETICS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            effects = info.get("effect", {})
            snps_found += 1

            result["snps_analyzed"].append({
                "rsid": rsid,
                "gene": info.get("gene", ""),
                "genotype": genotype
            })

            _key = get_genotype_key(genotype, effects)
            if _key:

                effect = effects[_key]

                if effect.get("salt_sensitivity") == "Higher":
                    sensitivity_score += 2
                elif effect.get("salt_sensitivity") == "Moderate":
                    sensitivity_score += 1

                if "hypertension_risk" in effect:
                    if "Elevated" in effect["hypertension_risk"]:
                        result["findings"].append(f"{info.get('gene', rsid)}: elevated hypertension risk")

    if snps_found > 0:
        if sensitivity_score >= 4:
            result["salt_sensitivity"] = "High"
            result["blood_pressure_response"] = "Very Sensitive"
            result["recommendation"] = "Strong recommendation to limit sodium intake"
        elif sensitivity_score >= 2:
            result["salt_sensitivity"] = "Moderate"
            result["blood_pressure_response"] = "Moderately Sensitive"
            result["recommendation"] = "Monitor sodium intake"
        else:
            result["salt_sensitivity"] = "Normal"
            result["blood_pressure_response"] = "Normal"
            result["recommendation"] = "Standard dietary sodium recommendations"

    return result


def analyze_alcohol(dna_data: dict) -> Dict[str, Any]:
    """Analyze alcohol metabolism"""
    result = {
        "snps_analyzed": [],
        "adh_activity": "Unknown",
        "aldh_activity": "Unknown",
        "alcohol_tolerance": "Unknown",
        "flushing_risk": "Unknown",
        "health_implications": [],
        "findings": []
    }

    for rsid, info in ALCOHOL_GENETICS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            effects = info.get("effect", {})

            result["snps_analyzed"].append({
                "rsid": rsid,
                "gene": info.get("gene", ""),
                "genotype": genotype,
                "common_name": info.get("common_name", "")
            })

            _key = get_genotype_key(genotype, effects)
            if _key:

                effect = effects[_key]

                # ADH1B
                if info.get("gene") == "ADH1B":
                    result["adh_activity"] = effect.get("adh_activity", "Unknown")
                    if effect.get("flushing") in ["May occur", "Likely (Asian flush)"]:
                        result["flushing_risk"] = effect["flushing"]
                        result["findings"].append("Fast alcohol metabolism - acetaldehyde buildup risk")

                # ALDH2
                if info.get("gene") == "ALDH2":
                    result["aldh_activity"] = effect.get("aldh2_activity", "Unknown")
                    result["alcohol_tolerance"] = effect.get("alcohol_tolerance", "Unknown")

                    if "Reduced" in effect.get("aldh2_activity", "") or "Very Low" in effect.get("aldh2_activity", ""):
                        result["flushing_risk"] = "High"
                        result["findings"].append("ALDH2 deficiency - flushing, nausea with alcohol")
                        result["health_implications"].append("Increased esophageal cancer risk with alcohol consumption")
                        result["health_implications"].append("Acetaldehyde is a carcinogen that accumulates")

    # Determine overall tolerance
    if result["aldh_activity"] == "Very Low (~5%)":
        result["alcohol_tolerance"] = "Very Low - should avoid alcohol"
    elif result["aldh_activity"] == "Reduced (~50%)":
        result["alcohol_tolerance"] = "Reduced - limit alcohol consumption"
    elif result["adh_activity"] in ["Fast", "Very Fast"] and result["aldh_activity"] == "Normal":
        result["alcohol_tolerance"] = "Moderate - fast processing but normal clearance"

    return result


def generate_nutrition_summary(results: Dict[str, Any]) -> Dict[str, Any]:
    """Generate overall nutrition summary"""
    summary = {
        "personalized_recommendations": [],
        "key_nutrient_needs": [],
        "dietary_sensitivities": [],
        "metabolism_profile": "",
        "key_findings": []
    }

    # Vitamin A
    vit_a = results.get("vitamin_a_metabolism", {})
    if vit_a.get("beta_carotene_converter") == "Poor Converter":
        summary["personalized_recommendations"].append("Prioritize preformed vitamin A (retinol) from animal sources")
        summary["key_nutrient_needs"].append("Vitamin A (retinol)")

    # B12/MTHFR
    b12 = results.get("vitamin_b12_metabolism", {})
    if b12.get("overall_b12_need") in ["Increased", "Slightly Increased"]:
        summary["key_nutrient_needs"].append("Vitamin B12")
    if "Low" in str(b12.get("mthfr_status", "")):
        summary["key_nutrient_needs"].append("Active Folate (Methylfolate)")
        summary["personalized_recommendations"].append("Consider methylated B vitamins (methylfolate, methylcobalamin)")

    # Omega-3
    omega3 = results.get("omega3_metabolism", {})
    if omega3.get("overall_conversion_ability") == "Poor":
        summary["personalized_recommendations"].append("Get omega-3s from fish or algae oil (EPA/DHA directly)")
        summary["key_nutrient_needs"].append("Preformed EPA/DHA")

    # Saturated fat
    sat_fat = results.get("saturated_fat_response", {})
    if "Highly Sensitive" in str(sat_fat.get("sat_fat_sensitivity", "")):
        summary["dietary_sensitivities"].append("Saturated Fat")
        summary["personalized_recommendations"].append("Limit saturated fat intake for weight management")

    # Carbs
    carbs = results.get("carbohydrate_metabolism", {})
    if "High" in str(carbs.get("t2d_genetic_risk", "")):
        summary["dietary_sensitivities"].append("Refined Carbohydrates")
        summary["personalized_recommendations"].append("Choose low-glycemic foods; monitor blood sugar")

    # Sodium
    sodium = results.get("sodium_sensitivity", {})
    if sodium.get("salt_sensitivity") == "High":
        summary["dietary_sensitivities"].append("Sodium/Salt")
        summary["personalized_recommendations"].append("Limit sodium intake to protect blood pressure")

    # Alcohol
    alcohol = results.get("alcohol_metabolism", {})
    if alcohol.get("alcohol_tolerance") in ["Very Low - should avoid alcohol", "Reduced - limit alcohol consumption"]:
        summary["dietary_sensitivities"].append("Alcohol")
        summary["personalized_recommendations"].append("Limit or avoid alcohol due to metabolism genetics")

    # Determine metabolism profile
    profiles = []
    if carbs.get("t2d_genetic_risk") in ["High (2x)", "Increased (1.4x)"]:
        profiles.append("Carb-sensitive")
    if sat_fat.get("sat_fat_sensitivity") == "Highly Sensitive":
        profiles.append("Fat-sensitive")
    if sodium.get("salt_sensitivity") == "High":
        profiles.append("Salt-sensitive")

    summary["metabolism_profile"] = ", ".join(profiles) if profiles else "Balanced"

    # Compile key findings
    for key in results:
        if key != "summary" and isinstance(results[key], dict):
            findings = results[key].get("findings", [])
            summary["key_findings"].extend(findings[:2])

    return summary
