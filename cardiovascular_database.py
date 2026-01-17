"""
Cardiovascular Genetics Database
Real SNPs for heart disease, stroke, blood pressure, cholesterol, and related conditions
Sources: CARDIoGRAM, GWAS Catalog, ClinVar
"""

from typing import Dict, Any, List

# =============================================================================
# CORONARY ARTERY DISEASE (CAD) RISK
# =============================================================================

CAD_GENETICS = {
    "rs10455872": {
        "gene": "LPA",
        "chromosome": "6",
        "function": "Lipoprotein(a) levels",
        "clinical_significance": "strong_risk_factor",
        "effect": {
            "AA": {"risk": "lower", "lpa_level": "normal", "description": "Normal Lp(a) levels"},
            "AG": {"risk": "elevated", "lpa_level": "elevated", "description": "Elevated Lp(a) - CAD risk increased 1.5x"},
            "GG": {"risk": "high", "lpa_level": "high", "description": "High Lp(a) - CAD risk increased 2-3x"}
        },
        "population_frequency": {"A": 0.93, "G": 0.07}
    },
    "rs1333049": {
        "gene": "9p21",
        "chromosome": "9",
        "function": "CDKN2A/B locus - cell cycle regulation",
        "clinical_significance": "risk_factor",
        "effect": {
            "GG": {"risk": "lower", "description": "Lower CAD risk"},
            "GC": {"risk": "moderate", "description": "Moderate risk (1.2x)"},
            "CC": {"risk": "elevated", "description": "Elevated risk (1.5x)"}
        },
        "population_frequency": {"G": 0.50, "C": 0.50}
    },
    "rs4977574": {
        "gene": "9p21",
        "chromosome": "9",
        "function": "9p21 CAD risk locus",
        "clinical_significance": "risk_factor",
        "effect": {
            "AA": {"risk": "lower", "description": "Lower CAD risk"},
            "AG": {"risk": "moderate", "description": "Intermediate risk"},
            "GG": {"risk": "elevated", "description": "Elevated CAD risk (1.3x)"}
        },
        "population_frequency": {"A": 0.45, "G": 0.55}
    },
    "rs599839": {
        "gene": "SORT1",
        "chromosome": "1",
        "function": "Sortilin 1 - LDL metabolism",
        "clinical_significance": "risk_factor",
        "effect": {
            "AA": {"risk": "lower", "description": "Lower LDL, lower CAD risk"},
            "AG": {"risk": "moderate", "description": "Intermediate"},
            "GG": {"risk": "elevated", "description": "Higher LDL tendency"}
        },
        "population_frequency": {"A": 0.22, "G": 0.78}
    },
    "rs646776": {
        "gene": "CELSR2",
        "chromosome": "1",
        "function": "Cadherin - LDL regulation",
        "clinical_significance": "risk_factor",
        "effect": {
            "TT": {"risk": "elevated", "description": "Higher LDL cholesterol"},
            "TC": {"risk": "moderate", "description": "Intermediate"},
            "CC": {"risk": "lower", "description": "Lower LDL cholesterol"}
        },
        "population_frequency": {"T": 0.78, "C": 0.22}
    }
}

# =============================================================================
# LDL CHOLESTEROL GENETICS
# =============================================================================

LDL_GENETICS = {
    "rs515135": {
        "gene": "APOB",
        "chromosome": "2",
        "function": "Apolipoprotein B",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"ldl_effect": "lower", "description": "Lower LDL cholesterol"},
            "CT": {"ldl_effect": "average", "description": "Average LDL"},
            "TT": {"ldl_effect": "higher", "description": "Higher LDL cholesterol"}
        },
        "population_frequency": {"C": 0.18, "T": 0.82}
    },
    "rs2228671": {
        "gene": "LDLR",
        "chromosome": "19",
        "function": "LDL receptor",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"ldl_effect": "higher", "description": "Higher LDL - reduced receptor function"},
            "CT": {"ldl_effect": "average", "description": "Average LDL"},
            "TT": {"ldl_effect": "lower", "description": "Lower LDL - better receptor function"}
        },
        "population_frequency": {"C": 0.88, "T": 0.12}
    },
    "rs629301": {
        "gene": "SORT1",
        "chromosome": "1",
        "function": "LDL clearance",
        "clinical_significance": "risk_factor",
        "effect": {
            "GG": {"ldl_effect": "higher", "description": "Higher LDL levels"},
            "GT": {"ldl_effect": "average", "description": "Average LDL"},
            "TT": {"ldl_effect": "lower", "description": "Lower LDL levels"}
        },
        "population_frequency": {"G": 0.78, "T": 0.22}
    }
}

# =============================================================================
# HDL CHOLESTEROL GENETICS
# =============================================================================

HDL_GENETICS = {
    "rs1800775": {
        "gene": "CETP",
        "chromosome": "16",
        "function": "Cholesteryl ester transfer protein",
        "clinical_significance": "protective_factor",
        "effect": {
            "AA": {"hdl_effect": "higher", "description": "Higher HDL - reduced CETP activity"},
            "AC": {"hdl_effect": "average", "description": "Average HDL"},
            "CC": {"hdl_effect": "lower", "description": "Lower HDL - normal CETP activity"}
        },
        "population_frequency": {"A": 0.32, "C": 0.68}
    },
    "rs1532085": {
        "gene": "LIPC",
        "chromosome": "15",
        "function": "Hepatic lipase",
        "clinical_significance": "hdl_modifier",
        "effect": {
            "AA": {"hdl_effect": "higher", "description": "Higher HDL cholesterol"},
            "AG": {"hdl_effect": "average", "description": "Average HDL"},
            "GG": {"hdl_effect": "lower", "description": "Lower HDL cholesterol"}
        },
        "population_frequency": {"A": 0.40, "G": 0.60}
    },
    "rs3764261": {
        "gene": "CETP",
        "chromosome": "16",
        "function": "CETP expression",
        "clinical_significance": "hdl_modifier",
        "effect": {
            "AA": {"hdl_effect": "higher", "description": "Higher HDL - cardioprotective"},
            "AC": {"hdl_effect": "average", "description": "Average HDL"},
            "CC": {"hdl_effect": "lower", "description": "Lower HDL levels"}
        },
        "population_frequency": {"A": 0.32, "C": 0.68}
    }
}

# =============================================================================
# TRIGLYCERIDE GENETICS
# =============================================================================

TRIGLYCERIDE_GENETICS = {
    "rs662799": {
        "gene": "APOA5",
        "chromosome": "11",
        "function": "Apolipoprotein A5",
        "clinical_significance": "risk_factor",
        "effect": {
            "AA": {"tg_effect": "lower", "description": "Lower triglycerides"},
            "AG": {"tg_effect": "average", "description": "Average triglycerides"},
            "GG": {"tg_effect": "higher", "description": "Higher triglycerides (30-40% increase)"}
        },
        "population_frequency": {"A": 0.92, "G": 0.08}
    },
    "rs28927680": {
        "gene": "APOA5",
        "chromosome": "11",
        "function": "Triglyceride metabolism",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"tg_effect": "lower", "description": "Lower triglycerides"},
            "CT": {"tg_effect": "average", "description": "Average triglycerides"},
            "TT": {"tg_effect": "higher", "description": "Higher triglycerides"}
        },
        "population_frequency": {"C": 0.90, "T": 0.10}
    },
    "rs964184": {
        "gene": "ZNF259/APOA5",
        "chromosome": "11",
        "function": "Triglyceride regulation cluster",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"tg_effect": "lower", "description": "Lower triglycerides"},
            "CG": {"tg_effect": "average", "description": "Average triglycerides"},
            "GG": {"tg_effect": "higher", "description": "Higher triglycerides"}
        },
        "population_frequency": {"C": 0.85, "G": 0.15}
    }
}

# =============================================================================
# BLOOD PRESSURE / HYPERTENSION GENETICS
# =============================================================================

BLOOD_PRESSURE_GENETICS = {
    "rs5186": {
        "gene": "AGTR1",
        "chromosome": "3",
        "function": "Angiotensin II receptor type 1",
        "clinical_significance": "risk_factor",
        "effect": {
            "AA": {"bp_effect": "lower", "description": "Lower blood pressure tendency"},
            "AC": {"bp_effect": "average", "description": "Average blood pressure"},
            "CC": {"bp_effect": "higher", "description": "Higher blood pressure tendency"}
        },
        "population_frequency": {"A": 0.70, "C": 0.30}
    },
    "rs699": {
        "gene": "AGT",
        "chromosome": "1",
        "function": "Angiotensinogen M235T",
        "clinical_significance": "risk_factor",
        "effect": {
            "AA": {"bp_effect": "lower", "description": "Met235 - lower angiotensinogen"},
            "AG": {"bp_effect": "average", "description": "Intermediate"},
            "GG": {"bp_effect": "higher", "description": "Thr235 - higher angiotensinogen, HTN risk"}
        },
        "population_frequency": {"A": 0.58, "G": 0.42}
    },
    "rs4340": {
        "gene": "ACE",
        "chromosome": "17",
        "function": "Angiotensin converting enzyme I/D",
        "clinical_significance": "risk_factor",
        "effect": {
            "II": {"bp_effect": "lower", "description": "Insertion - lower ACE activity"},
            "ID": {"bp_effect": "average", "description": "Intermediate ACE activity"},
            "DD": {"bp_effect": "higher", "description": "Deletion - higher ACE, HTN risk"}
        },
        "population_frequency": {"I": 0.45, "D": 0.55}
    },
    "rs1801253": {
        "gene": "ADRB1",
        "chromosome": "10",
        "function": "Beta-1 adrenergic receptor Arg389Gly",
        "clinical_significance": "drug_response",
        "effect": {
            "CC": {"bp_effect": "normal", "beta_blocker": "better_response", "description": "Arg389 - better beta-blocker response"},
            "CG": {"bp_effect": "normal", "beta_blocker": "moderate_response", "description": "Intermediate response"},
            "GG": {"bp_effect": "normal", "beta_blocker": "reduced_response", "description": "Gly389 - may need higher doses"}
        },
        "population_frequency": {"C": 0.72, "G": 0.28}
    },
    "rs1799998": {
        "gene": "CYP11B2",
        "chromosome": "8",
        "function": "Aldosterone synthase",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"bp_effect": "higher", "description": "Higher aldosterone - salt sensitive HTN"},
            "CT": {"bp_effect": "average", "description": "Intermediate"},
            "TT": {"bp_effect": "lower", "description": "Lower aldosterone"}
        },
        "population_frequency": {"C": 0.45, "T": 0.55}
    }
}

# =============================================================================
# STROKE RISK GENETICS
# =============================================================================

STROKE_GENETICS = {
    "rs1333049": {
        "gene": "9p21",
        "chromosome": "9",
        "function": "Cardiovascular disease locus",
        "clinical_significance": "risk_factor",
        "effect": {
            "GG": {"risk": "lower", "description": "Lower stroke risk"},
            "GC": {"risk": "moderate", "description": "Moderate risk"},
            "CC": {"risk": "elevated", "description": "Elevated stroke and CAD risk"}
        },
        "population_frequency": {"G": 0.50, "C": 0.50}
    },
    "rs11984041": {
        "gene": "HDAC9",
        "chromosome": "7",
        "function": "Histone deacetylase 9 - large vessel stroke",
        "clinical_significance": "risk_factor",
        "effect": {
            "TT": {"risk": "lower", "description": "Lower large vessel stroke risk"},
            "TA": {"risk": "moderate", "description": "Intermediate risk"},
            "AA": {"risk": "elevated", "description": "Elevated large vessel stroke risk"}
        },
        "population_frequency": {"T": 0.90, "A": 0.10}
    },
    "rs12425791": {
        "gene": "NINJ2",
        "chromosome": "12",
        "function": "Ninjurin 2 - ischemic stroke",
        "clinical_significance": "risk_factor",
        "effect": {
            "AA": {"risk": "lower", "description": "Lower ischemic stroke risk"},
            "AG": {"risk": "moderate", "description": "Intermediate risk"},
            "GG": {"risk": "elevated", "description": "Elevated ischemic stroke risk"}
        },
        "population_frequency": {"A": 0.82, "G": 0.18}
    }
}

# =============================================================================
# ATRIAL FIBRILLATION GENETICS
# =============================================================================

AFIB_GENETICS = {
    "rs2200733": {
        "gene": "4q25",
        "chromosome": "4",
        "function": "PITX2 locus - atrial development",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower atrial fibrillation risk"},
            "CT": {"risk": "moderate", "description": "Moderate risk (1.4x)"},
            "TT": {"risk": "elevated", "description": "Elevated AFib risk (1.9x)"}
        },
        "population_frequency": {"C": 0.85, "T": 0.15}
    },
    "rs10033464": {
        "gene": "4q25",
        "chromosome": "4",
        "function": "PITX2 regulatory region",
        "clinical_significance": "risk_factor",
        "effect": {
            "GG": {"risk": "lower", "description": "Lower AFib risk"},
            "GT": {"risk": "moderate", "description": "Moderate risk"},
            "TT": {"risk": "elevated", "description": "Elevated AFib risk"}
        },
        "population_frequency": {"G": 0.88, "T": 0.12}
    },
    "rs7193343": {
        "gene": "ZFHX3",
        "chromosome": "16",
        "function": "Zinc finger homeobox 3",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower AFib risk"},
            "CT": {"risk": "moderate", "description": "Intermediate"},
            "TT": {"risk": "elevated", "description": "Elevated AFib risk"}
        },
        "population_frequency": {"C": 0.80, "T": 0.20}
    }
}

# =============================================================================
# CLOTTING / THROMBOSIS GENETICS
# =============================================================================

CLOTTING_GENETICS = {
    "rs6025": {
        "gene": "F5",
        "chromosome": "1",
        "function": "Factor V Leiden",
        "clinical_significance": "pathogenic",
        "effect": {
            "CC": {"risk": "normal", "description": "Normal - no Factor V Leiden"},
            "CT": {"risk": "elevated", "description": "Heterozygous FVL - 5-10x VTE risk"},
            "TT": {"risk": "high", "description": "Homozygous FVL - 50-80x VTE risk"}
        },
        "population_frequency": {"C": 0.97, "T": 0.03}
    },
    "rs1799963": {
        "gene": "F2",
        "chromosome": "11",
        "function": "Prothrombin G20210A",
        "clinical_significance": "pathogenic",
        "effect": {
            "GG": {"risk": "normal", "description": "Normal prothrombin"},
            "GA": {"risk": "elevated", "description": "Heterozygous - 3x VTE risk"},
            "AA": {"risk": "high", "description": "Homozygous - significantly elevated VTE risk"}
        },
        "population_frequency": {"G": 0.98, "A": 0.02}
    },
    "rs8176719": {
        "gene": "ABO",
        "chromosome": "9",
        "function": "ABO blood type - VTE risk",
        "clinical_significance": "risk_factor",
        "effect": {
            "del": {"risk": "lower", "description": "Blood type O - lower VTE risk"},
            "ins": {"risk": "elevated", "description": "Non-O blood type - 1.5x VTE risk"}
        },
        "population_frequency": {"del": 0.35, "ins": 0.65}
    }
}

# =============================================================================
# MAIN ANALYSIS FUNCTION
# =============================================================================


def get_effect_with_complement(genotype, effect_dict):
    """Get effect trying original, reverse, and complement orientations."""
    if not genotype or not effect_dict:
        return None
    # Try original
    if genotype in effect_dict:
        return effect_dict[genotype]
    # Try reverse
    rev = genotype[::-1]
    if rev in effect_dict:
        return effect_dict[rev]
    # Try complement (A<->T, G<->C)
    comp_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    comp = ''.join(comp_map.get(b, b) for b in genotype.upper())
    if comp in effect_dict:
        return effect_dict[comp]
    # Try reverse complement
    rev_comp = comp[::-1]
    if rev_comp in effect_dict:
        return effect_dict[rev_comp]
    return None


def analyze_cardiovascular_genetics(dna_data: Dict[str, str]) -> Dict[str, Any]:
    """
    Analyze DNA data for cardiovascular genetic markers

    Args:
        dna_data: Dictionary mapping rsIDs to genotypes

    Returns:
        Dictionary containing cardiovascular genetics analysis
    """
    results = {}

    # Analyze CAD risk
    cad_results = []
    cad_score = 0
    has_lpa_risk = False
    for rsid, snp_info in CAD_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                cad_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect.get("risk", "unknown"),
                    "description": effect["description"]
                })
                if effect.get("risk") in ["elevated", "high"]:
                    cad_score += 1
                    if snp_info["gene"] == "LPA":
                        has_lpa_risk = True
                elif effect.get("risk") == "lower":
                    cad_score -= 1

    results["coronary_artery_disease"] = {
        "risk_level": get_cv_risk_level(cad_score, len(cad_results)),
        "risk_score": cad_score,
        "has_lpa_risk": has_lpa_risk,
        "variants_analyzed": len(cad_results),
        "snps_analyzed": cad_results,
        "note": "Lipoprotein(a) is a strong independent risk factor - discuss with doctor if elevated"
    }

    # Analyze LDL cholesterol
    ldl_results = []
    ldl_score = 0
    for rsid, snp_info in LDL_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                ldl_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "ldl_effect": effect["ldl_effect"],
                    "description": effect["description"]
                })
                if effect["ldl_effect"] == "higher":
                    ldl_score += 1
                elif effect["ldl_effect"] == "lower":
                    ldl_score -= 1

    results["ldl_cholesterol"] = {
        "tendency": "Higher LDL tendency" if ldl_score > 0 else ("Lower LDL tendency" if ldl_score < 0 else "Average LDL tendency"),
        "score": ldl_score,
        "variants_analyzed": len(ldl_results),
        "snps_analyzed": ldl_results
    }

    # Analyze HDL cholesterol
    hdl_results = []
    hdl_score = 0
    for rsid, snp_info in HDL_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                hdl_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "hdl_effect": effect["hdl_effect"],
                    "description": effect["description"]
                })
                if effect["hdl_effect"] == "higher":
                    hdl_score += 1
                elif effect["hdl_effect"] == "lower":
                    hdl_score -= 1

    results["hdl_cholesterol"] = {
        "tendency": "Higher HDL tendency (protective)" if hdl_score > 0 else ("Lower HDL tendency" if hdl_score < 0 else "Average HDL tendency"),
        "score": hdl_score,
        "variants_analyzed": len(hdl_results),
        "snps_analyzed": hdl_results
    }

    # Analyze triglycerides
    tg_results = []
    tg_score = 0
    for rsid, snp_info in TRIGLYCERIDE_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                tg_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "tg_effect": effect["tg_effect"],
                    "description": effect["description"]
                })
                if effect["tg_effect"] == "higher":
                    tg_score += 1
                elif effect["tg_effect"] == "lower":
                    tg_score -= 1

    results["triglycerides"] = {
        "tendency": "Higher triglyceride tendency" if tg_score > 0 else ("Lower triglyceride tendency" if tg_score < 0 else "Average triglyceride tendency"),
        "score": tg_score,
        "variants_analyzed": len(tg_results),
        "snps_analyzed": tg_results
    }

    # Analyze blood pressure
    bp_results = []
    bp_score = 0
    beta_blocker_response = "normal"
    for rsid, snp_info in BLOOD_PRESSURE_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                bp_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "bp_effect": effect.get("bp_effect", "normal"),
                    "description": effect["description"]
                })
                if effect.get("bp_effect") == "higher":
                    bp_score += 1
                elif effect.get("bp_effect") == "lower":
                    bp_score -= 1
                if effect.get("beta_blocker"):
                    beta_blocker_response = effect["beta_blocker"]

    results["blood_pressure"] = {
        "tendency": "Higher BP tendency" if bp_score > 0 else ("Lower BP tendency" if bp_score < 0 else "Average BP tendency"),
        "score": bp_score,
        "beta_blocker_response": beta_blocker_response,
        "variants_analyzed": len(bp_results),
        "snps_analyzed": bp_results
    }

    # Analyze stroke risk
    stroke_results = []
    stroke_score = 0
    for rsid, snp_info in STROKE_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                stroke_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect["risk"],
                    "description": effect["description"]
                })
                if effect["risk"] == "elevated":
                    stroke_score += 1
                elif effect["risk"] == "lower":
                    stroke_score -= 1

    results["stroke"] = {
        "risk_level": get_cv_risk_level(stroke_score, len(stroke_results)),
        "risk_score": stroke_score,
        "variants_analyzed": len(stroke_results),
        "snps_analyzed": stroke_results
    }

    # Analyze AFib risk
    afib_results = []
    afib_score = 0
    for rsid, snp_info in AFIB_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                afib_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect["risk"],
                    "description": effect["description"]
                })
                if effect["risk"] == "elevated":
                    afib_score += 1
                elif effect["risk"] == "lower":
                    afib_score -= 1

    results["atrial_fibrillation"] = {
        "risk_level": get_cv_risk_level(afib_score, len(afib_results)),
        "risk_score": afib_score,
        "variants_analyzed": len(afib_results),
        "snps_analyzed": afib_results
    }

    # Analyze clotting risk
    clotting_results = []
    has_fvl = False
    has_prothrombin = False
    for rsid, snp_info in CLOTTING_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                clotting_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect.get("risk", "normal"),
                    "description": effect["description"]
                })
                if snp_info["gene"] == "F5" and effect.get("risk") in ["elevated", "high"]:
                    has_fvl = True
                if snp_info["gene"] == "F2" and effect.get("risk") in ["elevated", "high"]:
                    has_prothrombin = True

    clotting_risk = "Normal"
    if has_fvl or has_prothrombin:
        clotting_risk = "Elevated - thrombophilia variant detected"

    results["clotting_risk"] = {
        "risk_level": clotting_risk,
        "has_factor_v_leiden": has_fvl,
        "has_prothrombin_mutation": has_prothrombin,
        "variants_analyzed": len(clotting_results),
        "snps_analyzed": clotting_results,
        "note": "Factor V Leiden and Prothrombin mutations increase VTE risk - important for surgery/pregnancy"
    }

    # Overall summary
    total_variants = sum([
        len(cad_results), len(ldl_results), len(hdl_results), len(tg_results),
        len(bp_results), len(stroke_results), len(afib_results), len(clotting_results)
    ])

    results["overall"] = {
        "total_variants_analyzed": total_variants,
        "recommendations": get_cv_recommendations(results)
    }

    return results


def get_cv_risk_level(score: int, variants: int) -> str:
    """Convert risk score to risk level"""
    if variants == 0:
        return "Insufficient data"
    if score <= -2:
        return "Below Average Risk"
    elif score <= 0:
        return "Average Population Risk"
    elif score <= 2:
        return "Slightly Elevated Risk"
    else:
        return "Elevated Risk"


def get_cv_recommendations(results: Dict[str, Any]) -> List[str]:
    """Generate cardiovascular recommendations"""
    recommendations = []

    if results.get("coronary_artery_disease", {}).get("has_lpa_risk"):
        recommendations.append("Consider Lp(a) blood test - you have genetic variants for elevated Lp(a)")

    if results.get("ldl_cholesterol", {}).get("score", 0) > 0:
        recommendations.append("Monitor LDL cholesterol regularly - genetic tendency for higher levels")

    if results.get("hdl_cholesterol", {}).get("score", 0) < 0:
        recommendations.append("Exercise and healthy fats can help raise HDL levels")

    if results.get("blood_pressure", {}).get("score", 0) > 0:
        recommendations.append("Monitor blood pressure regularly - genetic hypertension tendency")

    if results.get("clotting_risk", {}).get("has_factor_v_leiden"):
        recommendations.append("Factor V Leiden detected - discuss with doctor before surgery, pregnancy, or hormone therapy")

    if results.get("clotting_risk", {}).get("has_prothrombin_mutation"):
        recommendations.append("Prothrombin mutation detected - increased VTE risk, discuss with hematologist")

    if results.get("atrial_fibrillation", {}).get("risk_score", 0) > 1:
        recommendations.append("Elevated AFib genetic risk - monitor heart rhythm, limit alcohol/caffeine")

    if not recommendations:
        recommendations.append("Maintain heart-healthy lifestyle: exercise, healthy diet, no smoking")

    return recommendations
