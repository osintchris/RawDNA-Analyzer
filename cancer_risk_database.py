"""
Cancer Risk Genetics Database
Real SNPs from clinical genetics, ClinVar, and cancer genomics studies
Note: These are risk factors, not diagnoses. Consult genetic counselor for actionable variants.
"""

from typing import Dict, Any, List

# =============================================================================
# BREAST CANCER RISK (Including BRCA1/2 common variants)
# =============================================================================

BREAST_CANCER_GENETICS = {
    "rs1799950": {
        "gene": "BRCA1",
        "chromosome": "17",
        "function": "BRCA1 Q356R variant",
        "clinical_significance": "likely_benign",
        "effect": {
            "GG": {"risk": "population", "description": "Common variant - population risk"},
            "GA": {"risk": "population", "description": "Common variant"},
            "AA": {"risk": "population", "description": "Common variant"}
        },
        "population_frequency": {"G": 0.92, "A": 0.08}
    },
    "rs1799966": {
        "gene": "BRCA1",
        "chromosome": "17",
        "function": "BRCA1 P871L polymorphism",
        "clinical_significance": "benign",
        "effect": {
            "TT": {"risk": "population", "description": "Common polymorphism"},
            "TC": {"risk": "population", "description": "Common polymorphism"},
            "CC": {"risk": "population", "description": "Common polymorphism"}
        },
        "population_frequency": {"T": 0.70, "C": 0.30}
    },
    "rs144848": {
        "gene": "BRCA2",
        "chromosome": "13",
        "function": "BRCA2 N372H variant",
        "clinical_significance": "benign",
        "effect": {
            "AA": {"risk": "population", "description": "Common variant"},
            "AC": {"risk": "population", "description": "Common variant"},
            "CC": {"risk": "population", "description": "Common variant"}
        },
        "population_frequency": {"A": 0.75, "C": 0.25}
    },
    "rs2981582": {
        "gene": "FGFR2",
        "chromosome": "10",
        "function": "Fibroblast growth factor receptor 2",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower breast cancer risk"},
            "CT": {"risk": "moderate", "description": "Intermediate risk (1.1x)"},
            "TT": {"risk": "elevated", "description": "Elevated risk (1.25x)"}
        },
        "population_frequency": {"C": 0.60, "T": 0.40}
    },
    "rs3803662": {
        "gene": "TOX3/TNRC9",
        "chromosome": "16",
        "function": "Breast cancer susceptibility locus",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower risk"},
            "CT": {"risk": "moderate", "description": "Moderate risk (1.15x)"},
            "TT": {"risk": "elevated", "description": "Elevated risk (1.3x)"}
        },
        "population_frequency": {"C": 0.72, "T": 0.28}
    },
    "rs13387042": {
        "gene": "2q35",
        "chromosome": "2",
        "function": "Breast cancer susceptibility locus",
        "clinical_significance": "risk_factor",
        "effect": {
            "GG": {"risk": "lower", "description": "Lower risk"},
            "GA": {"risk": "moderate", "description": "Moderate risk"},
            "AA": {"risk": "elevated", "description": "Elevated risk (1.2x)"}
        },
        "population_frequency": {"G": 0.50, "A": 0.50}
    },
    "rs1219648": {
        "gene": "FGFR2",
        "chromosome": "10",
        "function": "FGFR2 intronic variant",
        "clinical_significance": "risk_factor",
        "effect": {
            "AA": {"risk": "lower", "description": "Lower risk"},
            "AG": {"risk": "moderate", "description": "Moderate risk"},
            "GG": {"risk": "elevated", "description": "Elevated risk (1.2x)"}
        },
        "population_frequency": {"A": 0.60, "G": 0.40}
    }
}

# =============================================================================
# COLORECTAL CANCER RISK (Including Lynch syndrome markers)
# =============================================================================

COLORECTAL_CANCER_GENETICS = {
    "rs6983267": {
        "gene": "8q24",
        "chromosome": "8",
        "function": "Colorectal cancer susceptibility locus",
        "clinical_significance": "risk_factor",
        "effect": {
            "TT": {"risk": "lower", "description": "Lower colorectal cancer risk"},
            "TG": {"risk": "moderate", "description": "Moderate risk (1.2x)"},
            "GG": {"risk": "elevated", "description": "Elevated risk (1.4x)"}
        },
        "population_frequency": {"T": 0.50, "G": 0.50}
    },
    "rs4939827": {
        "gene": "SMAD7",
        "chromosome": "18",
        "function": "TGF-beta signaling",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "elevated", "description": "Elevated risk"},
            "CT": {"risk": "moderate", "description": "Moderate risk"},
            "TT": {"risk": "lower", "description": "Lower risk"}
        },
        "population_frequency": {"C": 0.52, "T": 0.48}
    },
    "rs10795668": {
        "gene": "10p14",
        "chromosome": "10",
        "function": "Colorectal cancer susceptibility",
        "clinical_significance": "risk_factor",
        "effect": {
            "AA": {"risk": "lower", "description": "Lower risk"},
            "AG": {"risk": "moderate", "description": "Moderate risk"},
            "GG": {"risk": "elevated", "description": "Elevated risk"}
        },
        "population_frequency": {"A": 0.65, "G": 0.35}
    },
    "rs3802842": {
        "gene": "11q23",
        "chromosome": "11",
        "function": "Colorectal cancer locus",
        "clinical_significance": "risk_factor",
        "effect": {
            "AA": {"risk": "lower", "description": "Lower risk"},
            "AC": {"risk": "moderate", "description": "Moderate risk"},
            "CC": {"risk": "elevated", "description": "Elevated risk (1.15x)"}
        },
        "population_frequency": {"A": 0.70, "C": 0.30}
    }
}

# =============================================================================
# PROSTATE CANCER RISK
# =============================================================================

PROSTATE_CANCER_GENETICS = {
    "rs1447295": {
        "gene": "8q24",
        "chromosome": "8",
        "function": "Prostate cancer susceptibility",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower prostate cancer risk"},
            "CA": {"risk": "moderate", "description": "Moderate risk (1.4x)"},
            "AA": {"risk": "elevated", "description": "Elevated risk (1.8x)"}
        },
        "population_frequency": {"C": 0.85, "A": 0.15}
    },
    "rs16901979": {
        "gene": "8q24",
        "chromosome": "8",
        "function": "Prostate cancer region 2",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower risk"},
            "CA": {"risk": "moderate", "description": "Moderate risk"},
            "AA": {"risk": "elevated", "description": "Elevated risk"}
        },
        "population_frequency": {"C": 0.92, "A": 0.08}
    },
    "rs4430796": {
        "gene": "HNF1B",
        "chromosome": "17",
        "function": "Hepatocyte nuclear factor 1B",
        "clinical_significance": "risk_factor",
        "effect": {
            "GG": {"risk": "elevated", "description": "Elevated risk"},
            "GA": {"risk": "moderate", "description": "Moderate risk"},
            "AA": {"risk": "lower", "description": "Lower risk"}
        },
        "population_frequency": {"G": 0.48, "A": 0.52}
    },
    "rs10993994": {
        "gene": "MSMB",
        "chromosome": "10",
        "function": "Microseminoprotein beta",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower risk"},
            "CT": {"risk": "moderate", "description": "Moderate risk (1.2x)"},
            "TT": {"risk": "elevated", "description": "Elevated risk (1.5x)"}
        },
        "population_frequency": {"C": 0.60, "T": 0.40}
    },
    "rs2735839": {
        "gene": "KLK3",
        "chromosome": "19",
        "function": "Prostate specific antigen gene",
        "clinical_significance": "risk_factor",
        "effect": {
            "GG": {"risk": "lower", "description": "Lower risk, higher PSA"},
            "GA": {"risk": "moderate", "description": "Moderate risk"},
            "AA": {"risk": "elevated", "description": "Elevated risk, lower PSA"}
        },
        "population_frequency": {"G": 0.85, "A": 0.15}
    }
}

# =============================================================================
# LUNG CANCER RISK
# =============================================================================

LUNG_CANCER_GENETICS = {
    "rs2736100": {
        "gene": "TERT",
        "chromosome": "5",
        "function": "Telomerase reverse transcriptase",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "elevated", "description": "Elevated lung cancer risk"},
            "AC": {"risk": "moderate", "description": "Moderate risk"},
            "AA": {"risk": "lower", "description": "Lower risk"}
        },
        "population_frequency": {"C": 0.50, "A": 0.50}
    },
    "rs8034191": {
        "gene": "CHRNA3/5",
        "chromosome": "15",
        "function": "Nicotinic acetylcholine receptor",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower risk"},
            "CT": {"risk": "moderate", "description": "Moderate risk"},
            "TT": {"risk": "elevated", "description": "Elevated risk (1.3x) - affects nicotine dependence too"}
        },
        "population_frequency": {"C": 0.65, "T": 0.35}
    },
    "rs1051730": {
        "gene": "CHRNA3",
        "chromosome": "15",
        "function": "Nicotinic receptor subunit",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower risk"},
            "CT": {"risk": "moderate", "description": "Moderate risk"},
            "TT": {"risk": "elevated", "description": "Elevated lung cancer risk"}
        },
        "population_frequency": {"C": 0.65, "T": 0.35}
    },
    "rs401681": {
        "gene": "CLPTM1L",
        "chromosome": "5",
        "function": "Cleft lip/palate transmembrane 1-like",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "elevated", "description": "Elevated risk"},
            "CT": {"risk": "moderate", "description": "Moderate risk"},
            "TT": {"risk": "lower", "description": "Lower risk"}
        },
        "population_frequency": {"C": 0.45, "T": 0.55}
    }
}

# =============================================================================
# MELANOMA/SKIN CANCER RISK
# =============================================================================

MELANOMA_GENETICS = {
    "rs910873": {
        "gene": "PIGU/MC1R",
        "chromosome": "20",
        "function": "Melanin production pathway",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower melanoma risk"},
            "CT": {"risk": "moderate", "description": "Moderate risk"},
            "TT": {"risk": "elevated", "description": "Elevated risk"}
        },
        "population_frequency": {"C": 0.88, "T": 0.12}
    },
    "rs1805007": {
        "gene": "MC1R",
        "chromosome": "16",
        "function": "Melanocortin 1 receptor - red hair variant",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "lower", "description": "Typical pigmentation"},
            "CT": {"risk": "elevated", "description": "Red hair variant carrier - elevated melanoma risk"},
            "TT": {"risk": "high", "description": "Red hair/fair skin - high melanoma risk (2-4x)"}
        },
        "population_frequency": {"C": 0.92, "T": 0.08}
    },
    "rs1805008": {
        "gene": "MC1R",
        "chromosome": "16",
        "function": "MC1R R160W variant",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "lower", "description": "Normal pigmentation"},
            "CT": {"risk": "elevated", "description": "Carrier - elevated risk"},
            "TT": {"risk": "high", "description": "High melanoma risk"}
        },
        "population_frequency": {"C": 0.90, "T": 0.10}
    },
    "rs12913832": {
        "gene": "HERC2/OCA2",
        "chromosome": "15",
        "function": "Eye color - UV sensitivity",
        "clinical_significance": "risk_factor",
        "effect": {
            "AA": {"risk": "elevated", "description": "Blue eyes - higher UV sensitivity/melanoma risk"},
            "AG": {"risk": "moderate", "description": "Green/hazel eyes - moderate risk"},
            "GG": {"risk": "lower", "description": "Brown eyes - lower melanoma risk"}
        },
        "population_frequency": {"A": 0.35, "G": 0.65}
    }
}

# =============================================================================
# THYROID CANCER RISK
# =============================================================================

THYROID_CANCER_GENETICS = {
    "rs966423": {
        "gene": "DIRC3",
        "chromosome": "2",
        "function": "Thyroid cancer susceptibility",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower thyroid cancer risk"},
            "CT": {"risk": "moderate", "description": "Moderate risk"},
            "TT": {"risk": "elevated", "description": "Elevated risk (1.3x)"}
        },
        "population_frequency": {"C": 0.60, "T": 0.40}
    },
    "rs965513": {
        "gene": "FOXE1",
        "chromosome": "9",
        "function": "Forkhead box E1",
        "clinical_significance": "risk_factor",
        "effect": {
            "GG": {"risk": "lower", "description": "Lower risk"},
            "GA": {"risk": "moderate", "description": "Moderate risk (1.4x)"},
            "AA": {"risk": "elevated", "description": "Elevated risk (1.8x)"}
        },
        "population_frequency": {"G": 0.65, "A": 0.35}
    },
    "rs944289": {
        "gene": "NKX2-1",
        "chromosome": "14",
        "function": "Thyroid transcription factor",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower risk"},
            "CT": {"risk": "moderate", "description": "Moderate risk"},
            "TT": {"risk": "elevated", "description": "Elevated risk"}
        },
        "population_frequency": {"C": 0.55, "T": 0.45}
    }
}

# =============================================================================
# PANCREATIC CANCER RISK
# =============================================================================

PANCREATIC_CANCER_GENETICS = {
    "rs505922": {
        "gene": "ABO",
        "chromosome": "9",
        "function": "ABO blood group",
        "clinical_significance": "risk_factor",
        "effect": {
            "CC": {"risk": "lower", "description": "Blood type O - lower pancreatic cancer risk"},
            "CT": {"risk": "moderate", "description": "Intermediate risk"},
            "TT": {"risk": "elevated", "description": "Non-O blood type - elevated risk (1.3x)"}
        },
        "population_frequency": {"C": 0.35, "T": 0.65}
    },
    "rs3790844": {
        "gene": "NR5A2",
        "chromosome": "1",
        "function": "Nuclear receptor subfamily 5",
        "clinical_significance": "risk_factor",
        "effect": {
            "TT": {"risk": "lower", "description": "Lower risk"},
            "TC": {"risk": "moderate", "description": "Moderate risk"},
            "CC": {"risk": "elevated", "description": "Elevated risk"}
        },
        "population_frequency": {"T": 0.75, "C": 0.25}
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


def analyze_cancer_risk_genetics(dna_data: Dict[str, str]) -> Dict[str, Any]:
    """
    Analyze DNA data for cancer risk genetic markers

    Args:
        dna_data: Dictionary mapping rsIDs to genotypes

    Returns:
        Dictionary containing cancer risk analysis
    """
    results = {}

    # Analyze breast cancer
    breast_results = []
    breast_score = 0
    for rsid, snp_info in BREAST_CANCER_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                breast_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect["risk"],
                    "description": effect["description"]
                })
                if effect["risk"] == "elevated":
                    breast_score += 1
                elif effect["risk"] == "lower":
                    breast_score -= 1

    results["breast_cancer"] = {
        "risk_level": get_cancer_risk_level(breast_score, len(breast_results)),
        "risk_score": breast_score,
        "variants_analyzed": len(breast_results),
        "snps_analyzed": breast_results,
        "note": "Common variants only - does not include rare BRCA1/2 pathogenic variants"
    }

    # Analyze colorectal cancer
    colorectal_results = []
    colorectal_score = 0
    for rsid, snp_info in COLORECTAL_CANCER_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                colorectal_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect["risk"],
                    "description": effect["description"]
                })
                if effect["risk"] == "elevated":
                    colorectal_score += 1
                elif effect["risk"] == "lower":
                    colorectal_score -= 1

    results["colorectal_cancer"] = {
        "risk_level": get_cancer_risk_level(colorectal_score, len(colorectal_results)),
        "risk_score": colorectal_score,
        "variants_analyzed": len(colorectal_results),
        "snps_analyzed": colorectal_results,
        "screening_recommendation": "Regular colonoscopy screening recommended especially if elevated risk"
    }

    # Analyze prostate cancer
    prostate_results = []
    prostate_score = 0
    for rsid, snp_info in PROSTATE_CANCER_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                prostate_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect["risk"],
                    "description": effect["description"]
                })
                if effect["risk"] == "elevated":
                    prostate_score += 1
                elif effect["risk"] == "lower":
                    prostate_score -= 1

    results["prostate_cancer"] = {
        "risk_level": get_cancer_risk_level(prostate_score, len(prostate_results)),
        "risk_score": prostate_score,
        "variants_analyzed": len(prostate_results),
        "snps_analyzed": prostate_results,
        "note": "Relevant for males - discuss PSA screening with doctor"
    }

    # Analyze lung cancer
    lung_results = []
    lung_score = 0
    for rsid, snp_info in LUNG_CANCER_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                lung_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect["risk"],
                    "description": effect["description"]
                })
                if effect["risk"] == "elevated":
                    lung_score += 1
                elif effect["risk"] == "lower":
                    lung_score -= 1

    results["lung_cancer"] = {
        "risk_level": get_cancer_risk_level(lung_score, len(lung_results)),
        "risk_score": lung_score,
        "variants_analyzed": len(lung_results),
        "snps_analyzed": lung_results,
        "note": "Smoking is the strongest risk factor - these variants may also affect nicotine dependence"
    }

    # Analyze melanoma
    melanoma_results = []
    melanoma_score = 0
    for rsid, snp_info in MELANOMA_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                melanoma_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect["risk"],
                    "description": effect["description"]
                })
                if effect["risk"] in ["elevated", "high"]:
                    melanoma_score += 1
                elif effect["risk"] == "lower":
                    melanoma_score -= 1

    results["melanoma"] = {
        "risk_level": get_cancer_risk_level(melanoma_score, len(melanoma_results)),
        "risk_score": melanoma_score,
        "variants_analyzed": len(melanoma_results),
        "snps_analyzed": melanoma_results,
        "recommendation": "Sun protection and regular skin checks especially if elevated risk"
    }

    # Analyze thyroid cancer
    thyroid_results = []
    thyroid_score = 0
    for rsid, snp_info in THYROID_CANCER_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                thyroid_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect["risk"],
                    "description": effect["description"]
                })
                if effect["risk"] == "elevated":
                    thyroid_score += 1
                elif effect["risk"] == "lower":
                    thyroid_score -= 1

    results["thyroid_cancer"] = {
        "risk_level": get_cancer_risk_level(thyroid_score, len(thyroid_results)),
        "risk_score": thyroid_score,
        "variants_analyzed": len(thyroid_results),
        "snps_analyzed": thyroid_results
    }

    # Analyze pancreatic cancer
    pancreatic_results = []
    pancreatic_score = 0
    for rsid, snp_info in PANCREATIC_CANCER_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                pancreatic_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect["risk"],
                    "description": effect["description"]
                })
                if effect["risk"] == "elevated":
                    pancreatic_score += 1
                elif effect["risk"] == "lower":
                    pancreatic_score -= 1

    results["pancreatic_cancer"] = {
        "risk_level": get_cancer_risk_level(pancreatic_score, len(pancreatic_results)),
        "risk_score": pancreatic_score,
        "variants_analyzed": len(pancreatic_results),
        "snps_analyzed": pancreatic_results
    }

    # Overall summary
    total_variants = sum([
        len(breast_results), len(colorectal_results), len(prostate_results),
        len(lung_results), len(melanoma_results), len(thyroid_results),
        len(pancreatic_results)
    ])

    elevated_cancers = []
    for cancer_type in ["breast_cancer", "colorectal_cancer", "prostate_cancer",
                       "lung_cancer", "melanoma", "thyroid_cancer", "pancreatic_cancer"]:
        if results.get(cancer_type, {}).get("risk_score", 0) > 1:
            elevated_cancers.append(cancer_type.replace("_", " ").title())

    results["overall"] = {
        "total_variants_analyzed": total_variants,
        "elevated_risk_cancers": elevated_cancers,
        "recommendations": get_cancer_recommendations(results)
    }

    return results


def get_cancer_risk_level(score: int, variants: int) -> str:
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


def get_cancer_recommendations(results: Dict[str, Any]) -> List[str]:
    """Generate cancer screening recommendations"""
    recommendations = []

    if results.get("breast_cancer", {}).get("risk_score", 0) > 1:
        recommendations.append("Discuss breast cancer screening schedule with your doctor")

    if results.get("colorectal_cancer", {}).get("risk_score", 0) > 1:
        recommendations.append("Consider earlier or more frequent colonoscopy screening")

    if results.get("melanoma", {}).get("risk_score", 0) > 1:
        recommendations.append("Use sun protection and get regular skin examinations")

    if results.get("lung_cancer", {}).get("risk_score", 0) > 1:
        recommendations.append("If you smoke, consider lung cancer screening (low-dose CT)")

    recommendations.append("These are common genetic variants - consult genetic counselor for comprehensive testing")

    return recommendations
