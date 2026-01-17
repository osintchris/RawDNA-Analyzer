"""
Skin & Dermatology Genetics Database
Real SNPs for skin aging, wrinkles, UV sensitivity, skin conditions
Sources: GWAS Catalog, dermatology genetics studies, dbSNP
"""

from typing import Dict, Any, List

# =============================================================================
# SKIN AGING & WRINKLES GENETICS
# =============================================================================

SKIN_AGING_GENETICS = {
    "rs1800012": {
        "gene": "COL1A1",
        "chromosome": "17",
        "function": "Collagen type I alpha 1 - skin structure",
        "effect": {
            "GG": {"aging": "normal", "description": "Normal collagen production"},
            "GT": {"aging": "faster", "description": "Reduced collagen - may age faster"},
            "TT": {"aging": "faster", "description": "Significantly reduced collagen"}
        },
        "population_frequency": {"G": 0.83, "T": 0.17}
    },
    "rs1800255": {
        "gene": "COL3A1",
        "chromosome": "2",
        "function": "Collagen type III - skin elasticity",
        "effect": {
            "GG": {"aging": "normal", "description": "Normal skin elasticity"},
            "GA": {"aging": "moderate", "description": "Slightly reduced elasticity"},
            "AA": {"aging": "faster", "description": "Reduced skin elasticity"}
        },
        "population_frequency": {"G": 0.70, "A": 0.30}
    },
    "rs2228570": {
        "gene": "VDR",
        "chromosome": "12",
        "function": "Vitamin D receptor - skin health",
        "effect": {
            "CC": {"aging": "slower", "description": "Better vitamin D utilization for skin"},
            "CT": {"aging": "normal", "description": "Normal vitamin D response"},
            "TT": {"aging": "faster", "description": "Reduced vitamin D skin benefits"}
        },
        "population_frequency": {"C": 0.60, "T": 0.40}
    },
    "rs11568820": {
        "gene": "VDR",
        "chromosome": "12",
        "function": "VDR Cdx2 variant",
        "effect": {
            "GG": {"aging": "slower", "description": "Enhanced skin protection"},
            "GA": {"aging": "normal", "description": "Normal skin aging"},
            "AA": {"aging": "faster", "description": "May benefit from vitamin D"}
        },
        "population_frequency": {"G": 0.80, "A": 0.20}
    },
    "rs4880": {
        "gene": "SOD2",
        "chromosome": "6",
        "function": "Superoxide dismutase 2 - antioxidant",
        "effect": {
            "TT": {"aging": "slower", "description": "Better antioxidant protection"},
            "CT": {"aging": "normal", "description": "Normal antioxidant function"},
            "CC": {"aging": "faster", "description": "Reduced antioxidant capacity - more oxidative damage"}
        },
        "population_frequency": {"T": 0.50, "C": 0.50}
    },
    "rs1050450": {
        "gene": "GPX1",
        "chromosome": "3",
        "function": "Glutathione peroxidase - antioxidant",
        "effect": {
            "CC": {"aging": "slower", "description": "Better glutathione activity"},
            "CT": {"aging": "normal", "description": "Normal antioxidant function"},
            "TT": {"aging": "faster", "description": "Reduced antioxidant protection"}
        },
        "population_frequency": {"C": 0.70, "T": 0.30}
    },
    "rs1801131": {
        "gene": "MTHFR",
        "chromosome": "1",
        "function": "Methylation - affects skin cell renewal",
        "effect": {
            "AA": {"aging": "normal", "description": "Normal methylation"},
            "AC": {"aging": "normal", "description": "Slightly reduced methylation"},
            "CC": {"aging": "faster", "description": "Reduced methylation - may affect skin renewal"}
        },
        "population_frequency": {"A": 0.70, "C": 0.30}
    }
}

# =============================================================================
# UV SENSITIVITY & SUN DAMAGE
# =============================================================================

UV_SENSITIVITY_GENETICS = {
    "rs1805007": {
        "gene": "MC1R",
        "chromosome": "16",
        "function": "Melanocortin 1 receptor - R151C red hair variant",
        "effect": {
            "CC": {"uv_sensitivity": "normal", "burn_risk": "normal", "description": "Normal UV response"},
            "CT": {"uv_sensitivity": "high", "burn_risk": "elevated", "description": "Red hair carrier - burns easily"},
            "TT": {"uv_sensitivity": "very_high", "burn_risk": "high", "description": "Very fair skin - high burn risk"}
        },
        "population_frequency": {"C": 0.92, "T": 0.08}
    },
    "rs1805008": {
        "gene": "MC1R",
        "chromosome": "16",
        "function": "MC1R R160W variant",
        "effect": {
            "CC": {"uv_sensitivity": "normal", "burn_risk": "normal", "description": "Normal pigmentation"},
            "CT": {"uv_sensitivity": "high", "burn_risk": "elevated", "description": "Fair skin variant"},
            "TT": {"uv_sensitivity": "very_high", "burn_risk": "high", "description": "Very fair - burns easily"}
        },
        "population_frequency": {"C": 0.90, "T": 0.10}
    },
    "rs1805009": {
        "gene": "MC1R",
        "chromosome": "16",
        "function": "MC1R D294H variant",
        "effect": {
            "GG": {"uv_sensitivity": "normal", "burn_risk": "normal", "description": "Normal UV protection"},
            "GC": {"uv_sensitivity": "high", "burn_risk": "elevated", "description": "Increased sun sensitivity"},
            "CC": {"uv_sensitivity": "very_high", "burn_risk": "high", "description": "Very sun sensitive"}
        },
        "population_frequency": {"G": 0.98, "C": 0.02}
    },
    "rs12913832": {
        "gene": "HERC2/OCA2",
        "chromosome": "15",
        "function": "Eye/skin pigmentation",
        "effect": {
            "AA": {"uv_sensitivity": "high", "description": "Blue eyes - less melanin protection"},
            "AG": {"uv_sensitivity": "moderate", "description": "Green/hazel - moderate protection"},
            "GG": {"uv_sensitivity": "low", "description": "Brown eyes - better UV protection"}
        },
        "population_frequency": {"A": 0.35, "G": 0.65}
    },
    "rs16891982": {
        "gene": "SLC45A2",
        "chromosome": "5",
        "function": "Skin pigmentation - MATP",
        "effect": {
            "CC": {"uv_sensitivity": "high", "description": "Light skin - higher UV sensitivity"},
            "CG": {"uv_sensitivity": "moderate", "description": "Intermediate pigmentation"},
            "GG": {"uv_sensitivity": "low", "description": "Darker skin - better UV protection"}
        },
        "population_frequency": {"C": 0.95, "G": 0.05}
    },
    "rs1426654": {
        "gene": "SLC24A5",
        "chromosome": "15",
        "function": "Skin pigmentation",
        "effect": {
            "AA": {"uv_sensitivity": "high", "description": "European light skin variant"},
            "AG": {"uv_sensitivity": "moderate", "description": "Intermediate"},
            "GG": {"uv_sensitivity": "low", "description": "Ancestral - more melanin"}
        },
        "population_frequency": {"A": 0.98, "G": 0.02}
    }
}

# =============================================================================
# ECZEMA / ATOPIC DERMATITIS
# =============================================================================

ECZEMA_GENETICS = {
    "rs2282634": {
        "gene": "FLG",
        "chromosome": "1",
        "function": "Filaggrin - skin barrier",
        "effect": {
            "CC": {"risk": "lower", "description": "Normal skin barrier"},
            "CT": {"risk": "elevated", "description": "Carrier - increased eczema risk"},
            "TT": {"risk": "high", "description": "Filaggrin deficiency - high eczema risk"}
        },
        "population_frequency": {"C": 0.95, "T": 0.05}
    },
    "rs61816761": {
        "gene": "FLG",
        "chromosome": "1",
        "function": "Filaggrin R501X mutation",
        "effect": {
            "GG": {"risk": "lower", "description": "Normal filaggrin"},
            "GA": {"risk": "elevated", "description": "Carrier - eczema susceptibility"},
            "AA": {"risk": "high", "description": "Loss of function - high eczema risk"}
        },
        "population_frequency": {"G": 0.96, "A": 0.04}
    },
    "rs2066844": {
        "gene": "NOD2",
        "chromosome": "16",
        "function": "Innate immunity - skin inflammation",
        "effect": {
            "CC": {"risk": "lower", "description": "Normal immune response"},
            "CT": {"risk": "moderate", "description": "Slightly increased inflammation"},
            "TT": {"risk": "elevated", "description": "Increased inflammatory response"}
        },
        "population_frequency": {"C": 0.95, "T": 0.05}
    },
    "rs1800925": {
        "gene": "IL13",
        "chromosome": "5",
        "function": "Interleukin 13 - allergic inflammation",
        "effect": {
            "CC": {"risk": "lower", "description": "Normal IL-13"},
            "CT": {"risk": "moderate", "description": "Slightly elevated IL-13"},
            "TT": {"risk": "elevated", "description": "Higher IL-13 - atopic tendency"}
        },
        "population_frequency": {"C": 0.75, "T": 0.25}
    },
    "rs20541": {
        "gene": "IL13",
        "chromosome": "5",
        "function": "IL-13 R130Q variant",
        "effect": {
            "GG": {"risk": "lower", "description": "Normal function"},
            "GA": {"risk": "moderate", "description": "Intermediate"},
            "AA": {"risk": "elevated", "description": "Increased atopic disease risk"}
        },
        "population_frequency": {"G": 0.75, "A": 0.25}
    }
}

# =============================================================================
# PSORIASIS GENETICS
# =============================================================================

PSORIASIS_GENETICS = {
    "rs10484554": {
        "gene": "HLA-C",
        "chromosome": "6",
        "function": "HLA-C*06:02 - strongest psoriasis risk",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower psoriasis risk"},
            "CT": {"risk": "elevated", "description": "Elevated risk (3x)"},
            "TT": {"risk": "high", "description": "High psoriasis risk (9x)"}
        },
        "population_frequency": {"C": 0.85, "T": 0.15}
    },
    "rs12191877": {
        "gene": "HLA-C",
        "chromosome": "6",
        "function": "HLA region psoriasis locus",
        "effect": {
            "TT": {"risk": "lower", "description": "Lower risk"},
            "TC": {"risk": "moderate", "description": "Moderate risk"},
            "CC": {"risk": "elevated", "description": "Elevated risk"}
        },
        "population_frequency": {"T": 0.70, "C": 0.30}
    },
    "rs27524": {
        "gene": "ERAP1",
        "chromosome": "5",
        "function": "Endoplasmic reticulum aminopeptidase",
        "effect": {
            "GG": {"risk": "lower", "description": "Lower risk"},
            "GA": {"risk": "moderate", "description": "Intermediate"},
            "AA": {"risk": "elevated", "description": "Elevated psoriasis risk"}
        },
        "population_frequency": {"G": 0.65, "A": 0.35}
    },
    "rs2201841": {
        "gene": "IL23R",
        "chromosome": "1",
        "function": "IL-23 receptor - inflammation",
        "effect": {
            "CC": {"risk": "elevated", "description": "Higher psoriasis risk"},
            "CT": {"risk": "moderate", "description": "Intermediate"},
            "TT": {"risk": "lower", "description": "Protective variant"}
        },
        "population_frequency": {"C": 0.92, "T": 0.08}
    }
}

# =============================================================================
# ROSACEA GENETICS
# =============================================================================

ROSACEA_GENETICS = {
    "rs763035": {
        "gene": "HLA-DRA",
        "chromosome": "6",
        "function": "HLA class II - rosacea risk",
        "effect": {
            "AA": {"risk": "lower", "description": "Lower rosacea risk"},
            "AG": {"risk": "moderate", "description": "Moderate risk"},
            "GG": {"risk": "elevated", "description": "Elevated rosacea risk"}
        },
        "population_frequency": {"A": 0.55, "G": 0.45}
    },
    "rs3733631": {
        "gene": "BTNL2",
        "chromosome": "6",
        "function": "Butyrophilin-like 2 - immune regulation",
        "effect": {
            "GG": {"risk": "lower", "description": "Lower risk"},
            "GA": {"risk": "moderate", "description": "Intermediate"},
            "AA": {"risk": "elevated", "description": "Elevated rosacea susceptibility"}
        },
        "population_frequency": {"G": 0.72, "A": 0.28}
    },
    "rs1805007": {
        "gene": "MC1R",
        "chromosome": "16",
        "function": "Red hair/fair skin - rosacea link",
        "effect": {
            "CC": {"risk": "lower", "description": "Normal pigmentation"},
            "CT": {"risk": "elevated", "description": "Fair skin - rosacea prone"},
            "TT": {"risk": "high", "description": "Very fair - high rosacea risk"}
        },
        "population_frequency": {"C": 0.92, "T": 0.08}
    }
}

# =============================================================================
# ACNE GENETICS
# =============================================================================

ACNE_GENETICS = {
    "rs4133274": {
        "gene": "DDB2",
        "chromosome": "11",
        "function": "DNA damage binding - skin repair",
        "effect": {
            "TT": {"risk": "lower", "description": "Lower acne risk"},
            "TC": {"risk": "moderate", "description": "Moderate risk"},
            "CC": {"risk": "elevated", "description": "Elevated acne susceptibility"}
        },
        "population_frequency": {"T": 0.65, "C": 0.35}
    },
    "rs1159268": {
        "gene": "FST",
        "chromosome": "5",
        "function": "Follistatin - sebum production",
        "effect": {
            "CC": {"risk": "lower", "description": "Normal sebum"},
            "CT": {"risk": "moderate", "description": "Slightly oily"},
            "TT": {"risk": "elevated", "description": "Oilier skin - acne prone"}
        },
        "population_frequency": {"C": 0.60, "T": 0.40}
    },
    "rs7531806": {
        "gene": "OVOL1",
        "chromosome": "11",
        "function": "Skin cell differentiation",
        "effect": {
            "AA": {"risk": "lower", "description": "Normal skin turnover"},
            "AG": {"risk": "moderate", "description": "Intermediate"},
            "GG": {"risk": "elevated", "description": "May have acne tendency"}
        },
        "population_frequency": {"A": 0.55, "G": 0.45}
    }
}

# =============================================================================
# SKIN ELASTICITY & CELLULITE
# =============================================================================

SKIN_ELASTICITY_GENETICS = {
    "rs1800012": {
        "gene": "COL1A1",
        "chromosome": "17",
        "function": "Collagen production",
        "effect": {
            "GG": {"elasticity": "good", "cellulite_risk": "lower", "description": "Good collagen production"},
            "GT": {"elasticity": "moderate", "cellulite_risk": "moderate", "description": "Moderate collagen"},
            "TT": {"elasticity": "reduced", "cellulite_risk": "higher", "description": "Reduced collagen - cellulite prone"}
        },
        "population_frequency": {"G": 0.83, "T": 0.17}
    },
    "rs1799750": {
        "gene": "MMP1",
        "chromosome": "11",
        "function": "Matrix metalloproteinase 1 - collagen breakdown",
        "effect": {
            "1G/1G": {"elasticity": "good", "description": "Normal collagen breakdown"},
            "1G/2G": {"elasticity": "moderate", "description": "Moderate breakdown"},
            "2G/2G": {"elasticity": "reduced", "description": "Faster collagen breakdown - aging"}
        },
        "population_frequency": {"1G": 0.50, "2G": 0.50}
    },
    "rs1800629": {
        "gene": "TNF",
        "chromosome": "6",
        "function": "TNF-alpha - skin inflammation/damage",
        "effect": {
            "GG": {"elasticity": "good", "description": "Lower inflammation"},
            "GA": {"elasticity": "moderate", "description": "Moderate inflammation"},
            "AA": {"elasticity": "reduced", "description": "Higher inflammation - accelerated aging"}
        },
        "population_frequency": {"G": 0.85, "A": 0.15}
    }
}

# =============================================================================
# STRETCH MARKS SUSCEPTIBILITY
# =============================================================================

STRETCH_MARKS_GENETICS = {
    "rs1800012": {
        "gene": "COL1A1",
        "chromosome": "17",
        "function": "Collagen type I",
        "effect": {
            "GG": {"risk": "lower", "description": "Better collagen - less stretch marks"},
            "GT": {"risk": "moderate", "description": "Moderate susceptibility"},
            "TT": {"risk": "higher", "description": "Weaker collagen - stretch mark prone"}
        },
        "population_frequency": {"G": 0.83, "T": 0.17}
    },
    "rs1800255": {
        "gene": "COL3A1",
        "chromosome": "2",
        "function": "Collagen type III",
        "effect": {
            "GG": {"risk": "lower", "description": "Good elastin/collagen"},
            "GA": {"risk": "moderate", "description": "Moderate"},
            "AA": {"risk": "higher", "description": "Stretch mark susceptible"}
        },
        "population_frequency": {"G": 0.70, "A": 0.30}
    },
    "rs1799750": {
        "gene": "MMP1",
        "chromosome": "11",
        "function": "Collagen degradation enzyme",
        "effect": {
            "GG": {"risk": "lower", "description": "Normal collagen maintenance"},
            "GT": {"risk": "moderate", "description": "Intermediate"},
            "TT": {"risk": "higher", "description": "Faster collagen breakdown"}
        },
        "population_frequency": {"G": 0.50, "T": 0.50}
    }
}

# =============================================================================
# VITAMIN D SKIN SYNTHESIS
# =============================================================================

VITAMIN_D_SKIN_GENETICS = {
    "rs2228570": {
        "gene": "VDR",
        "chromosome": "12",
        "function": "Vitamin D receptor FokI",
        "effect": {
            "CC": {"synthesis": "efficient", "description": "Efficient vitamin D utilization"},
            "CT": {"synthesis": "normal", "description": "Normal vitamin D response"},
            "TT": {"synthesis": "reduced", "description": "May need more sun/supplementation"}
        },
        "population_frequency": {"C": 0.60, "T": 0.40}
    },
    "rs1544410": {
        "gene": "VDR",
        "chromosome": "12",
        "function": "VDR BsmI variant",
        "effect": {
            "CC": {"synthesis": "efficient", "description": "Better vitamin D metabolism"},
            "CT": {"synthesis": "normal", "description": "Normal metabolism"},
            "TT": {"synthesis": "reduced", "description": "Lower vitamin D efficiency"}
        },
        "population_frequency": {"C": 0.55, "T": 0.45}
    },
    "rs10741657": {
        "gene": "CYP2R1",
        "chromosome": "11",
        "function": "Vitamin D 25-hydroxylase",
        "effect": {
            "GG": {"synthesis": "efficient", "description": "Efficient conversion"},
            "GA": {"synthesis": "normal", "description": "Normal conversion"},
            "AA": {"synthesis": "reduced", "description": "Reduced vitamin D activation"}
        },
        "population_frequency": {"G": 0.70, "A": 0.30}
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


def analyze_skin_dermatology(dna_data: Dict[str, str]) -> Dict[str, Any]:
    """
    Analyze DNA data for skin and dermatology genetics

    Args:
        dna_data: Dictionary mapping rsIDs to genotypes

    Returns:
        Dictionary containing skin genetics analysis
    """
    results = {}

    # Analyze skin aging
    aging_results = []
    aging_score = 0
    for rsid, snp_info in SKIN_AGING_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                aging_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "aging": effect.get("aging", "normal"),
                    "description": effect["description"]
                })
                if effect.get("aging") == "slower":
                    aging_score += 1
                elif effect.get("aging") == "faster":
                    aging_score -= 1

    results["skin_aging"] = {
        "tendency": "Slower aging genetics" if aging_score > 1 else ("Faster aging genetics" if aging_score < -1 else "Average aging genetics"),
        "score": aging_score,
        "variants_analyzed": len(aging_results),
        "snps_analyzed": aging_results,
        "recommendations": get_aging_recommendations(aging_score)
    }

    # Analyze UV sensitivity
    uv_results = []
    uv_score = 0
    has_mc1r_variant = False
    for rsid, snp_info in UV_SENSITIVITY_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                uv_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "sensitivity": effect.get("uv_sensitivity", "normal"),
                    "description": effect["description"]
                })
                if effect.get("uv_sensitivity") in ["high", "very_high"]:
                    uv_score += 1
                    if "MC1R" in snp_info["gene"]:
                        has_mc1r_variant = True
                elif effect.get("uv_sensitivity") == "low":
                    uv_score -= 1

    results["uv_sensitivity"] = {
        "level": "High UV sensitivity" if uv_score > 1 else ("Low UV sensitivity" if uv_score < -1 else "Moderate UV sensitivity"),
        "score": uv_score,
        "has_mc1r_variant": has_mc1r_variant,
        "burn_easily": uv_score > 0,
        "variants_analyzed": len(uv_results),
        "snps_analyzed": uv_results,
        "recommendation": "High SPF sunscreen essential" if uv_score > 0 else "Normal sun protection recommended"
    }

    # Analyze eczema risk
    eczema_results = []
    eczema_score = 0
    has_filaggrin = False
    for rsid, snp_info in ECZEMA_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                eczema_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect.get("risk", "lower"),
                    "description": effect["description"]
                })
                if effect.get("risk") in ["elevated", "high"]:
                    eczema_score += 1
                    if "FLG" in snp_info["gene"]:
                        has_filaggrin = True
                elif effect.get("risk") == "lower":
                    eczema_score -= 1

    results["eczema_risk"] = {
        "risk_level": get_risk_level(eczema_score, len(eczema_results)),
        "score": eczema_score,
        "has_filaggrin_variant": has_filaggrin,
        "variants_analyzed": len(eczema_results),
        "snps_analyzed": eczema_results
    }

    # Analyze psoriasis risk
    psoriasis_results = []
    psoriasis_score = 0
    for rsid, snp_info in PSORIASIS_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                psoriasis_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect.get("risk", "lower"),
                    "description": effect["description"]
                })
                if effect.get("risk") in ["elevated", "high"]:
                    psoriasis_score += 1
                elif effect.get("risk") == "lower":
                    psoriasis_score -= 1

    results["psoriasis_risk"] = {
        "risk_level": get_risk_level(psoriasis_score, len(psoriasis_results)),
        "score": psoriasis_score,
        "variants_analyzed": len(psoriasis_results),
        "snps_analyzed": psoriasis_results
    }

    # Analyze rosacea risk
    rosacea_results = []
    rosacea_score = 0
    for rsid, snp_info in ROSACEA_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                rosacea_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect.get("risk", "lower"),
                    "description": effect["description"]
                })
                if effect.get("risk") in ["elevated", "high"]:
                    rosacea_score += 1
                elif effect.get("risk") == "lower":
                    rosacea_score -= 1

    results["rosacea_risk"] = {
        "risk_level": get_risk_level(rosacea_score, len(rosacea_results)),
        "score": rosacea_score,
        "variants_analyzed": len(rosacea_results),
        "snps_analyzed": rosacea_results
    }

    # Analyze acne
    acne_results = []
    acne_score = 0
    for rsid, snp_info in ACNE_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                acne_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect.get("risk", "lower"),
                    "description": effect["description"]
                })
                if effect.get("risk") == "elevated":
                    acne_score += 1
                elif effect.get("risk") == "lower":
                    acne_score -= 1

    results["acne_tendency"] = {
        "tendency": "Acne prone" if acne_score > 0 else ("Less prone" if acne_score < 0 else "Average"),
        "score": acne_score,
        "variants_analyzed": len(acne_results),
        "snps_analyzed": acne_results
    }

    # Analyze skin elasticity
    elasticity_results = []
    elasticity_score = 0
    for rsid, snp_info in SKIN_ELASTICITY_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                elasticity_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "elasticity": effect.get("elasticity", "moderate"),
                    "description": effect["description"]
                })
                if effect.get("elasticity") == "good":
                    elasticity_score += 1
                elif effect.get("elasticity") == "reduced":
                    elasticity_score -= 1

    results["skin_elasticity"] = {
        "level": "Good elasticity" if elasticity_score > 0 else ("Reduced elasticity" if elasticity_score < 0 else "Average elasticity"),
        "score": elasticity_score,
        "cellulite_prone": elasticity_score < 0,
        "variants_analyzed": len(elasticity_results),
        "snps_analyzed": elasticity_results
    }

    # Analyze stretch marks
    stretchmark_results = []
    stretchmark_score = 0
    for rsid, snp_info in STRETCH_MARKS_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                stretchmark_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect.get("risk", "moderate"),
                    "description": effect["description"]
                })
                if effect.get("risk") == "higher":
                    stretchmark_score += 1
                elif effect.get("risk") == "lower":
                    stretchmark_score -= 1

    results["stretch_marks"] = {
        "susceptibility": "Higher susceptibility" if stretchmark_score > 0 else ("Lower susceptibility" if stretchmark_score < 0 else "Average"),
        "score": stretchmark_score,
        "variants_analyzed": len(stretchmark_results),
        "snps_analyzed": stretchmark_results
    }

    # Analyze vitamin D skin synthesis
    vitd_results = []
    vitd_score = 0
    for rsid, snp_info in VITAMIN_D_SKIN_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                vitd_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "synthesis": effect.get("synthesis", "normal"),
                    "description": effect["description"]
                })
                if effect.get("synthesis") == "efficient":
                    vitd_score += 1
                elif effect.get("synthesis") == "reduced":
                    vitd_score -= 1

    results["vitamin_d_synthesis"] = {
        "efficiency": "Efficient" if vitd_score > 0 else ("Reduced" if vitd_score < 0 else "Normal"),
        "score": vitd_score,
        "may_need_supplementation": vitd_score < 0,
        "variants_analyzed": len(vitd_results),
        "snps_analyzed": vitd_results
    }

    # Overall summary
    total_variants = sum([
        len(aging_results), len(uv_results), len(eczema_results),
        len(psoriasis_results), len(rosacea_results), len(acne_results),
        len(elasticity_results), len(stretchmark_results), len(vitd_results)
    ])

    results["overall"] = {
        "total_variants_analyzed": total_variants,
        "skin_type_summary": get_skin_type_summary(results),
        "recommendations": get_skin_recommendations(results)
    }

    return results


def get_risk_level(score: int, variants: int) -> str:
    """Convert risk score to risk level"""
    if variants == 0:
        return "Insufficient data"
    if score <= -1:
        return "Below Average Risk"
    elif score == 0:
        return "Average Risk"
    elif score == 1:
        return "Slightly Elevated Risk"
    else:
        return "Elevated Risk"


def get_aging_recommendations(score: int) -> List[str]:
    """Get anti-aging recommendations based on genetics"""
    if score < 0:
        return [
            "Focus on antioxidant skincare (Vitamin C, E)",
            "Consider retinoid products for collagen support",
            "Sunscreen is especially important for you",
            "Collagen supplements may be beneficial"
        ]
    else:
        return [
            "Maintain your natural skin health with regular moisturizing",
            "Continue sun protection habits"
        ]


def get_skin_type_summary(results: Dict[str, Any]) -> str:
    """Generate a skin type summary"""
    traits = []

    if results.get("uv_sensitivity", {}).get("score", 0) > 0:
        traits.append("sun-sensitive")
    if results.get("skin_aging", {}).get("score", 0) < 0:
        traits.append("aging-prone")
    if results.get("eczema_risk", {}).get("score", 0) > 0:
        traits.append("eczema-prone")
    if results.get("acne_tendency", {}).get("score", 0) > 0:
        traits.append("oily/acne-prone")
    if results.get("rosacea_risk", {}).get("score", 0) > 0:
        traits.append("rosacea-prone")

    if traits:
        return "Your skin type: " + ", ".join(traits)
    else:
        return "Your skin type: balanced/normal"


def get_skin_recommendations(results: Dict[str, Any]) -> List[str]:
    """Generate personalized skin recommendations"""
    recommendations = []

    if results.get("uv_sensitivity", {}).get("score", 0) > 0:
        recommendations.append("Use SPF 50+ sunscreen daily - you burn easily")

    if results.get("skin_aging", {}).get("score", 0) < 0:
        recommendations.append("Prioritize antioxidants and retinoids in skincare")

    if results.get("eczema_risk", {}).get("has_filaggrin_variant"):
        recommendations.append("Keep skin well moisturized - barrier function may be impaired")

    if results.get("rosacea_risk", {}).get("score", 0) > 0:
        recommendations.append("Avoid triggers: alcohol, spicy food, extreme temperatures")

    if results.get("acne_tendency", {}).get("score", 0) > 0:
        recommendations.append("Consider salicylic acid or benzoyl peroxide products")

    if results.get("vitamin_d_synthesis", {}).get("score", 0) < 0:
        recommendations.append("May benefit from vitamin D supplementation")

    if not recommendations:
        recommendations.append("Maintain regular skincare routine with sunscreen and moisturizer")

    return recommendations
