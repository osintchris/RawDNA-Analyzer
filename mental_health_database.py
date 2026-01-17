"""
Mental Health Genetics Database
Real SNPs from GWAS studies for psychiatric and mental health conditions
Sources: Psychiatric Genomics Consortium, GWAS Catalog, Nature Genetics
"""

from typing import Dict, Any, List

# =============================================================================
# DEPRESSION GENETICS
# =============================================================================

DEPRESSION_GENETICS = {
    "rs1545843": {
        "gene": "OLFM4",
        "chromosome": "13",
        "function": "Olfactomedin 4 - neural development",
        "risk_allele": "A",
        "effect": {
            "GG": {"risk": "lower", "description": "Lower depression risk"},
            "GA": {"risk": "average", "description": "Average risk"},
            "AA": {"risk": "elevated", "description": "Slightly elevated risk"}
        },
        "population_frequency": {"G": 0.65, "A": 0.35}
    },
    "rs2522833": {
        "gene": "PCLO",
        "chromosome": "7",
        "function": "Piccolo - synaptic function",
        "risk_allele": "T",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower risk"},
            "CT": {"risk": "average", "description": "Average risk"},
            "TT": {"risk": "elevated", "description": "Elevated risk"}
        },
        "population_frequency": {"C": 0.72, "T": 0.28}
    },
    "rs4713916": {
        "gene": "FKBP5",
        "chromosome": "6",
        "function": "FK506 binding protein - stress response",
        "risk_allele": "A",
        "effect": {
            "GG": {"risk": "lower", "description": "Normal stress response"},
            "GA": {"risk": "moderate", "description": "Moderate stress vulnerability"},
            "AA": {"risk": "elevated", "description": "Increased stress sensitivity"}
        },
        "population_frequency": {"G": 0.70, "A": 0.30}
    },
    "rs6265": {
        "gene": "BDNF",
        "chromosome": "11",
        "function": "Brain-derived neurotrophic factor Val66Met",
        "risk_allele": "A",
        "effect": {
            "GG": {"risk": "lower", "description": "Val/Val - normal BDNF secretion"},
            "GA": {"risk": "moderate", "description": "Val/Met - reduced activity-dependent secretion"},
            "AA": {"risk": "elevated", "description": "Met/Met - impaired BDNF secretion"}
        },
        "population_frequency": {"G": 0.80, "A": 0.20}
    },
    "rs10994336": {
        "gene": "ANK3",
        "chromosome": "10",
        "function": "Ankyrin 3 - neuronal signaling",
        "risk_allele": "T",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower risk"},
            "CT": {"risk": "moderate", "description": "Moderate risk"},
            "TT": {"risk": "elevated", "description": "Elevated risk"}
        },
        "population_frequency": {"C": 0.92, "T": 0.08}
    },
    "rs1006737": {
        "gene": "CACNA1C",
        "chromosome": "12",
        "function": "Calcium channel - neuronal signaling",
        "risk_allele": "A",
        "effect": {
            "GG": {"risk": "lower", "description": "Lower risk"},
            "GA": {"risk": "moderate", "description": "Moderate risk"},
            "AA": {"risk": "elevated", "description": "Elevated risk"}
        },
        "population_frequency": {"G": 0.67, "A": 0.33}
    },
    "rs7044150": {
        "gene": "SIRT1",
        "chromosome": "10",
        "function": "Sirtuin 1 - mood regulation",
        "risk_allele": "T",
        "effect": {
            "CC": {"risk": "lower", "description": "Normal serotonin signaling"},
            "CT": {"risk": "moderate", "description": "Slightly altered signaling"},
            "TT": {"risk": "elevated", "description": "May affect mood regulation"}
        },
        "population_frequency": {"C": 0.75, "T": 0.25}
    }
}

# =============================================================================
# ANXIETY GENETICS
# =============================================================================

ANXIETY_GENETICS = {
    "rs6295": {
        "gene": "HTR1A",
        "chromosome": "5",
        "function": "Serotonin 1A receptor",
        "risk_allele": "G",
        "effect": {
            "CC": {"risk": "lower", "description": "Higher receptor expression - better anxiety resilience"},
            "CG": {"risk": "moderate", "description": "Intermediate expression"},
            "GG": {"risk": "elevated", "description": "Lower receptor expression - anxiety vulnerability"}
        },
        "population_frequency": {"C": 0.55, "G": 0.45}
    },
    "rs4680": {
        "gene": "COMT",
        "chromosome": "22",
        "function": "Catechol-O-methyltransferase Val158Met",
        "risk_allele": "A",
        "effect": {
            "GG": {"risk": "lower", "description": "Val/Val - fast dopamine clearance, stress resilient"},
            "GA": {"risk": "moderate", "description": "Val/Met - intermediate"},
            "AA": {"risk": "elevated", "description": "Met/Met - slow clearance, higher anxiety sensitivity"}
        },
        "population_frequency": {"G": 0.50, "A": 0.50}
    },
    "rs25531": {
        "gene": "SLC6A4",
        "chromosome": "17",
        "function": "Serotonin transporter 5-HTTLPR",
        "risk_allele": "G",
        "effect": {
            "AA": {"risk": "lower", "description": "LA/LA - higher serotonin transport, resilience"},
            "AG": {"risk": "moderate", "description": "LA/S or LA/LG - intermediate"},
            "GG": {"risk": "elevated", "description": "S/S or LG/LG - anxiety vulnerability"}
        },
        "population_frequency": {"A": 0.55, "G": 0.45}
    },
    "rs3800373": {
        "gene": "FKBP5",
        "chromosome": "6",
        "function": "Stress hormone regulation",
        "risk_allele": "A",
        "effect": {
            "CC": {"risk": "lower", "description": "Normal HPA axis function"},
            "CA": {"risk": "moderate", "description": "Slight stress sensitivity"},
            "AA": {"risk": "elevated", "description": "Increased stress hormone response"}
        },
        "population_frequency": {"C": 0.68, "A": 0.32}
    },
    "rs10482672": {
        "gene": "NPSR1",
        "chromosome": "7",
        "function": "Neuropeptide S receptor - arousal/anxiety",
        "risk_allele": "T",
        "effect": {
            "CC": {"risk": "lower", "description": "Normal arousal regulation"},
            "CT": {"risk": "moderate", "description": "Intermediate"},
            "TT": {"risk": "elevated", "description": "Increased panic sensitivity"}
        },
        "population_frequency": {"C": 0.75, "T": 0.25}
    },
    "rs2267735": {
        "gene": "CRHR1",
        "chromosome": "17",
        "function": "Corticotropin releasing hormone receptor",
        "risk_allele": "G",
        "effect": {
            "CC": {"risk": "lower", "description": "Normal stress response"},
            "CG": {"risk": "moderate", "description": "Slightly elevated stress response"},
            "GG": {"risk": "elevated", "description": "Enhanced stress reactivity"}
        },
        "population_frequency": {"C": 0.60, "G": 0.40}
    }
}

# =============================================================================
# ADHD GENETICS
# =============================================================================

ADHD_GENETICS = {
    "rs27072": {
        "gene": "DAT1/SLC6A3",
        "chromosome": "5",
        "function": "Dopamine transporter",
        "risk_allele": "T",
        "effect": {
            "CC": {"risk": "lower", "description": "Typical dopamine transport"},
            "CT": {"risk": "moderate", "description": "Slightly altered transport"},
            "TT": {"risk": "elevated", "description": "Altered dopamine signaling"}
        },
        "population_frequency": {"C": 0.72, "T": 0.28}
    },
    "rs1800544": {
        "gene": "ADRA2A",
        "chromosome": "10",
        "function": "Alpha-2A adrenergic receptor",
        "risk_allele": "G",
        "effect": {
            "CC": {"risk": "lower", "description": "Normal attention regulation"},
            "CG": {"risk": "moderate", "description": "Intermediate"},
            "GG": {"risk": "elevated", "description": "May affect attention/impulsivity"}
        },
        "population_frequency": {"C": 0.75, "G": 0.25}
    },
    "rs1801260": {
        "gene": "CLOCK",
        "chromosome": "4",
        "function": "Circadian rhythm - attention/alertness",
        "risk_allele": "C",
        "effect": {
            "TT": {"risk": "lower", "description": "Typical circadian function"},
            "TC": {"risk": "moderate", "description": "Slightly altered rhythm"},
            "CC": {"risk": "elevated", "description": "May affect alertness patterns"}
        },
        "population_frequency": {"T": 0.70, "C": 0.30}
    },
    "rs6277": {
        "gene": "DRD2",
        "chromosome": "11",
        "function": "Dopamine D2 receptor",
        "risk_allele": "T",
        "effect": {
            "CC": {"risk": "lower", "description": "Normal D2 receptor function"},
            "CT": {"risk": "moderate", "description": "Slightly altered signaling"},
            "TT": {"risk": "elevated", "description": "Reduced D2 binding"}
        },
        "population_frequency": {"C": 0.58, "T": 0.42}
    },
    "rs1800955": {
        "gene": "DRD4",
        "chromosome": "11",
        "function": "Dopamine D4 receptor",
        "risk_allele": "T",
        "effect": {
            "CC": {"risk": "lower", "description": "Normal novelty seeking"},
            "CT": {"risk": "moderate", "description": "Intermediate"},
            "TT": {"risk": "elevated", "description": "Higher novelty seeking"}
        },
        "population_frequency": {"C": 0.60, "T": 0.40}
    },
    "rs5569": {
        "gene": "SLC6A2",
        "chromosome": "16",
        "function": "Norepinephrine transporter",
        "risk_allele": "G",
        "effect": {
            "AA": {"risk": "lower", "description": "Normal norepinephrine function"},
            "AG": {"risk": "moderate", "description": "Slightly altered transport"},
            "GG": {"risk": "elevated", "description": "May affect attention regulation"}
        },
        "population_frequency": {"A": 0.65, "G": 0.35}
    }
}

# =============================================================================
# BIPOLAR DISORDER GENETICS
# =============================================================================

BIPOLAR_GENETICS = {
    "rs10994336": {
        "gene": "ANK3",
        "chromosome": "10",
        "function": "Ankyrin 3 - neuronal function",
        "risk_allele": "T",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower bipolar risk"},
            "CT": {"risk": "moderate", "description": "Intermediate risk"},
            "TT": {"risk": "elevated", "description": "Elevated risk"}
        },
        "population_frequency": {"C": 0.92, "T": 0.08}
    },
    "rs1006737": {
        "gene": "CACNA1C",
        "chromosome": "12",
        "function": "L-type calcium channel",
        "risk_allele": "A",
        "effect": {
            "GG": {"risk": "lower", "description": "Lower risk"},
            "GA": {"risk": "moderate", "description": "Moderate risk"},
            "AA": {"risk": "elevated", "description": "Elevated risk for mood disorders"}
        },
        "population_frequency": {"G": 0.67, "A": 0.33}
    },
    "rs4765913": {
        "gene": "CACNA1C",
        "chromosome": "12",
        "function": "Calcium signaling",
        "risk_allele": "T",
        "effect": {
            "CC": {"risk": "lower", "description": "Typical signaling"},
            "CT": {"risk": "moderate", "description": "Intermediate"},
            "TT": {"risk": "elevated", "description": "Altered calcium signaling"}
        },
        "population_frequency": {"C": 0.78, "T": 0.22}
    },
    "rs420259": {
        "gene": "PALB2",
        "chromosome": "16",
        "function": "DNA repair - neural health",
        "risk_allele": "A",
        "effect": {
            "GG": {"risk": "lower", "description": "Lower risk"},
            "GA": {"risk": "moderate", "description": "Intermediate"},
            "AA": {"risk": "elevated", "description": "Slightly elevated risk"}
        },
        "population_frequency": {"G": 0.72, "A": 0.28}
    },
    "rs2251219": {
        "gene": "DGKH",
        "chromosome": "13",
        "function": "Diacylglycerol kinase - cell signaling",
        "risk_allele": "T",
        "effect": {
            "CC": {"risk": "lower", "description": "Normal signaling"},
            "CT": {"risk": "moderate", "description": "Intermediate"},
            "TT": {"risk": "elevated", "description": "Altered cell signaling"}
        },
        "population_frequency": {"C": 0.65, "T": 0.35}
    }
}

# =============================================================================
# SCHIZOPHRENIA GENETICS
# =============================================================================

SCHIZOPHRENIA_GENETICS = {
    "rs1625579": {
        "gene": "MIR137",
        "chromosome": "1",
        "function": "MicroRNA-137 - brain development",
        "risk_allele": "T",
        "effect": {
            "GG": {"risk": "lower", "description": "Lower risk"},
            "GT": {"risk": "moderate", "description": "Intermediate risk"},
            "TT": {"risk": "elevated", "description": "Elevated risk"}
        },
        "population_frequency": {"G": 0.80, "T": 0.20}
    },
    "rs1344706": {
        "gene": "ZNF804A",
        "chromosome": "2",
        "function": "Zinc finger protein - gene regulation",
        "risk_allele": "T",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower risk"},
            "CT": {"risk": "moderate", "description": "Intermediate"},
            "TT": {"risk": "elevated", "description": "Slightly elevated risk"}
        },
        "population_frequency": {"C": 0.60, "T": 0.40}
    },
    "rs6932590": {
        "gene": "Intergenic",
        "chromosome": "6",
        "function": "MHC region - immune/neural",
        "risk_allele": "T",
        "effect": {
            "CC": {"risk": "lower", "description": "Lower risk"},
            "CT": {"risk": "moderate", "description": "Intermediate"},
            "TT": {"risk": "elevated", "description": "Elevated risk"}
        },
        "population_frequency": {"C": 0.75, "T": 0.25}
    },
    "rs2021722": {
        "gene": "TRIM26",
        "chromosome": "6",
        "function": "Tripartite motif protein",
        "risk_allele": "C",
        "effect": {
            "TT": {"risk": "lower", "description": "Lower risk"},
            "TC": {"risk": "moderate", "description": "Intermediate"},
            "CC": {"risk": "elevated", "description": "Elevated risk"}
        },
        "population_frequency": {"T": 0.70, "C": 0.30}
    },
    "rs12966547": {
        "gene": "TCF4",
        "chromosome": "18",
        "function": "Transcription factor 4 - neural development",
        "risk_allele": "A",
        "effect": {
            "GG": {"risk": "lower", "description": "Lower risk"},
            "GA": {"risk": "moderate", "description": "Intermediate"},
            "AA": {"risk": "elevated", "description": "Elevated risk"}
        },
        "population_frequency": {"G": 0.72, "A": 0.28}
    }
}

# =============================================================================
# PTSD GENETICS
# =============================================================================

PTSD_GENETICS = {
    "rs4713916": {
        "gene": "FKBP5",
        "chromosome": "6",
        "function": "Glucocorticoid receptor sensitivity",
        "risk_allele": "A",
        "effect": {
            "GG": {"risk": "lower", "description": "Normal HPA axis regulation"},
            "GA": {"risk": "moderate", "description": "Intermediate sensitivity"},
            "AA": {"risk": "elevated", "description": "Enhanced stress response vulnerability"}
        },
        "population_frequency": {"G": 0.70, "A": 0.30}
    },
    "rs9296158": {
        "gene": "FKBP5",
        "chromosome": "6",
        "function": "Stress hormone binding",
        "risk_allele": "T",
        "effect": {
            "CC": {"risk": "lower", "description": "Normal stress recovery"},
            "CT": {"risk": "moderate", "description": "Intermediate"},
            "TT": {"risk": "elevated", "description": "Prolonged stress response"}
        },
        "population_frequency": {"C": 0.65, "T": 0.35}
    },
    "rs6265": {
        "gene": "BDNF",
        "chromosome": "11",
        "function": "Brain-derived neurotrophic factor",
        "risk_allele": "A",
        "effect": {
            "GG": {"risk": "lower", "description": "Normal fear extinction"},
            "GA": {"risk": "moderate", "description": "Slightly impaired extinction"},
            "AA": {"risk": "elevated", "description": "Impaired fear extinction learning"}
        },
        "population_frequency": {"G": 0.80, "A": 0.20}
    },
    "rs110402": {
        "gene": "CRHR1",
        "chromosome": "17",
        "function": "CRH receptor - stress response",
        "risk_allele": "G",
        "effect": {
            "AA": {"risk": "lower", "description": "Normal stress response"},
            "AG": {"risk": "moderate", "description": "Intermediate"},
            "GG": {"risk": "elevated", "description": "Enhanced stress reactivity"}
        },
        "population_frequency": {"A": 0.55, "G": 0.45}
    }
}

# =============================================================================
# ADDICTION VULNERABILITY
# =============================================================================

ADDICTION_GENETICS = {
    "rs1799971": {
        "gene": "OPRM1",
        "chromosome": "6",
        "function": "Mu opioid receptor",
        "risk_allele": "G",
        "effect": {
            "AA": {"risk": "lower", "description": "Normal opioid response"},
            "AG": {"risk": "moderate", "description": "Altered reward response"},
            "GG": {"risk": "elevated", "description": "May have reduced reward from natural activities"}
        },
        "population_frequency": {"A": 0.85, "G": 0.15}
    },
    "rs1800497": {
        "gene": "DRD2/ANKK1",
        "chromosome": "11",
        "function": "Dopamine D2 receptor - Taq1A",
        "risk_allele": "T",
        "effect": {
            "CC": {"risk": "lower", "description": "Normal D2 receptor density"},
            "CT": {"risk": "moderate", "description": "Slightly reduced density"},
            "TT": {"risk": "elevated", "description": "Reduced D2 density - addiction vulnerability"}
        },
        "population_frequency": {"C": 0.70, "T": 0.30}
    },
    "rs1229984": {
        "gene": "ADH1B",
        "chromosome": "4",
        "function": "Alcohol dehydrogenase",
        "risk_allele": "C",
        "effect": {
            "TT": {"risk": "lower", "description": "Fast alcohol metabolism - protective"},
            "CT": {"risk": "moderate", "description": "Intermediate metabolism"},
            "CC": {"risk": "elevated", "description": "Slow metabolism - increased alcoholism risk"}
        },
        "population_frequency": {"T": 0.30, "C": 0.70}
    },
    "rs16969968": {
        "gene": "CHRNA5",
        "chromosome": "15",
        "function": "Nicotinic receptor alpha 5",
        "risk_allele": "A",
        "effect": {
            "GG": {"risk": "lower", "description": "Lower nicotine dependence risk"},
            "GA": {"risk": "moderate", "description": "Intermediate risk"},
            "AA": {"risk": "elevated", "description": "Higher nicotine dependence risk"}
        },
        "population_frequency": {"G": 0.65, "A": 0.35}
    },
    "rs4680": {
        "gene": "COMT",
        "chromosome": "22",
        "function": "Dopamine metabolism",
        "risk_allele": "A",
        "effect": {
            "GG": {"risk": "lower", "description": "Fast dopamine clearance - stimulant tolerance"},
            "GA": {"risk": "moderate", "description": "Intermediate metabolism"},
            "AA": {"risk": "elevated", "description": "Slow clearance - may seek stimulation"}
        },
        "population_frequency": {"G": 0.50, "A": 0.50}
    }
}

# =============================================================================
# COGNITIVE FUNCTION GENETICS
# =============================================================================

COGNITIVE_GENETICS = {
    "rs4680": {
        "gene": "COMT",
        "chromosome": "22",
        "function": "Prefrontal cortex function",
        "effect": {
            "GG": {"cognitive": "warrior", "description": "Val/Val - better stress performance, lower baseline cognition"},
            "GA": {"cognitive": "balanced", "description": "Val/Met - balanced profile"},
            "AA": {"cognitive": "worrier", "description": "Met/Met - higher baseline cognition, stress vulnerable"}
        },
        "population_frequency": {"G": 0.50, "A": 0.50}
    },
    "rs6265": {
        "gene": "BDNF",
        "chromosome": "11",
        "function": "Memory and learning",
        "effect": {
            "GG": {"cognitive": "optimal", "description": "Better memory formation"},
            "GA": {"cognitive": "typical", "description": "Normal memory function"},
            "AA": {"cognitive": "reduced", "description": "May have reduced memory consolidation"}
        },
        "population_frequency": {"G": 0.80, "A": 0.20}
    },
    "rs9536314": {
        "gene": "KLOTHO",
        "chromosome": "13",
        "function": "Cognitive longevity",
        "effect": {
            "TT": {"cognitive": "enhanced", "description": "KL-VS variant - enhanced cognition"},
            "GT": {"cognitive": "enhanced", "description": "KL-VS heterozygote - cognitive benefit"},
            "GG": {"cognitive": "normal", "description": "Normal cognitive aging"}
        },
        "population_frequency": {"G": 0.84, "T": 0.16}
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


def analyze_mental_health_genetics(dna_data: Dict[str, str]) -> Dict[str, Any]:
    """
    Analyze DNA data for mental health-related genetic markers

    Args:
        dna_data: Dictionary mapping rsIDs to genotypes

    Returns:
        Dictionary containing mental health genetics analysis
    """
    results = {}

    # Analyze depression risk
    depression_results = []
    depression_score = 0
    for rsid, snp_info in DEPRESSION_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                depression_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect["risk"],
                    "description": effect["description"]
                })
                if effect["risk"] == "elevated":
                    depression_score += 1
                elif effect["risk"] == "lower":
                    depression_score -= 1

    results["depression"] = {
        "risk_level": get_risk_level(depression_score, len(depression_results)),
        "risk_score": depression_score,
        "variants_analyzed": len(depression_results),
        "key_findings": [r for r in depression_results if r["risk"] in ["elevated", "lower"]][:3],
        "snps_analyzed": depression_results
    }

    # Analyze anxiety risk
    anxiety_results = []
    anxiety_score = 0
    for rsid, snp_info in ANXIETY_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                anxiety_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect["risk"],
                    "description": effect["description"]
                })
                if effect["risk"] == "elevated":
                    anxiety_score += 1
                elif effect["risk"] == "lower":
                    anxiety_score -= 1

    results["anxiety"] = {
        "risk_level": get_risk_level(anxiety_score, len(anxiety_results)),
        "risk_score": anxiety_score,
        "variants_analyzed": len(anxiety_results),
        "key_findings": [r for r in anxiety_results if r["risk"] in ["elevated", "lower"]][:3],
        "snps_analyzed": anxiety_results
    }

    # Analyze ADHD risk
    adhd_results = []
    adhd_score = 0
    for rsid, snp_info in ADHD_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                adhd_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect["risk"],
                    "description": effect["description"]
                })
                if effect["risk"] == "elevated":
                    adhd_score += 1
                elif effect["risk"] == "lower":
                    adhd_score -= 1

    results["adhd"] = {
        "risk_level": get_risk_level(adhd_score, len(adhd_results)),
        "risk_score": adhd_score,
        "variants_analyzed": len(adhd_results),
        "key_findings": [r for r in adhd_results if r["risk"] in ["elevated", "lower"]][:3],
        "snps_analyzed": adhd_results
    }

    # Analyze bipolar risk
    bipolar_results = []
    bipolar_score = 0
    for rsid, snp_info in BIPOLAR_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                bipolar_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect["risk"],
                    "description": effect["description"]
                })
                if effect["risk"] == "elevated":
                    bipolar_score += 1
                elif effect["risk"] == "lower":
                    bipolar_score -= 1

    results["bipolar"] = {
        "risk_level": get_risk_level(bipolar_score, len(bipolar_results)),
        "risk_score": bipolar_score,
        "variants_analyzed": len(bipolar_results),
        "snps_analyzed": bipolar_results
    }

    # Analyze schizophrenia risk
    schizophrenia_results = []
    schizophrenia_score = 0
    for rsid, snp_info in SCHIZOPHRENIA_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                schizophrenia_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect["risk"],
                    "description": effect["description"]
                })
                if effect["risk"] == "elevated":
                    schizophrenia_score += 1
                elif effect["risk"] == "lower":
                    schizophrenia_score -= 1

    results["schizophrenia"] = {
        "risk_level": get_risk_level(schizophrenia_score, len(schizophrenia_results)),
        "risk_score": schizophrenia_score,
        "variants_analyzed": len(schizophrenia_results),
        "snps_analyzed": schizophrenia_results
    }

    # Analyze PTSD vulnerability
    ptsd_results = []
    ptsd_score = 0
    for rsid, snp_info in PTSD_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                ptsd_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect["risk"],
                    "description": effect["description"]
                })
                if effect["risk"] == "elevated":
                    ptsd_score += 1
                elif effect["risk"] == "lower":
                    ptsd_score -= 1

    results["ptsd_vulnerability"] = {
        "risk_level": get_risk_level(ptsd_score, len(ptsd_results)),
        "risk_score": ptsd_score,
        "variants_analyzed": len(ptsd_results),
        "snps_analyzed": ptsd_results
    }

    # Analyze addiction vulnerability
    addiction_results = []
    addiction_score = 0
    for rsid, snp_info in ADDICTION_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                addiction_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect["risk"],
                    "description": effect["description"]
                })
                if effect["risk"] == "elevated":
                    addiction_score += 1
                elif effect["risk"] == "lower":
                    addiction_score -= 1

    results["addiction_vulnerability"] = {
        "risk_level": get_risk_level(addiction_score, len(addiction_results)),
        "risk_score": addiction_score,
        "variants_analyzed": len(addiction_results),
        "snps_analyzed": addiction_results
    }

    # Analyze cognitive profile
    cognitive_results = []
    cognitive_profile = {}
    for rsid, snp_info in COGNITIVE_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                cognitive_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "cognitive": effect.get("cognitive", "normal"),
                    "description": effect["description"]
                })
                if snp_info["gene"] == "COMT":
                    cognitive_profile["stress_cognition"] = effect["cognitive"]
                elif snp_info["gene"] == "BDNF":
                    cognitive_profile["memory"] = effect["cognitive"]
                elif snp_info["gene"] == "KLOTHO":
                    cognitive_profile["cognitive_aging"] = effect["cognitive"]

    results["cognitive_profile"] = {
        "profile": cognitive_profile,
        "variants_analyzed": len(cognitive_results),
        "snps_analyzed": cognitive_results
    }

    # Overall mental health resilience
    total_risk = (depression_score + anxiety_score + adhd_score +
                  bipolar_score + schizophrenia_score + ptsd_score + addiction_score)
    total_variants = sum([
        len(depression_results), len(anxiety_results), len(adhd_results),
        len(bipolar_results), len(schizophrenia_results), len(ptsd_results),
        len(addiction_results)
    ])

    if total_variants > 0:
        if total_risk <= -5:
            resilience = "High mental health resilience"
        elif total_risk <= 0:
            resilience = "Average mental health profile"
        elif total_risk <= 5:
            resilience = "Some vulnerability factors present"
        else:
            resilience = "Multiple vulnerability factors - preventive care recommended"
    else:
        resilience = "Insufficient data"

    results["overall"] = {
        "resilience": resilience,
        "total_risk_score": total_risk,
        "variants_analyzed": total_variants,
        "recommendations": get_mental_health_recommendations(results)
    }

    return results


def get_risk_level(score: int, variants: int) -> str:
    """Convert risk score to risk level"""
    if variants == 0:
        return "Insufficient data"
    if score <= -2:
        return "Below Average Risk"
    elif score <= 0:
        return "Average Risk"
    elif score <= 2:
        return "Slightly Elevated Risk"
    else:
        return "Elevated Risk"


def get_mental_health_recommendations(results: Dict[str, Any]) -> List[str]:
    """Generate personalized mental health recommendations"""
    recommendations = []

    if results.get("depression", {}).get("risk_score", 0) > 1:
        recommendations.append("Regular exercise and social connection are protective for mood")

    if results.get("anxiety", {}).get("risk_score", 0) > 1:
        recommendations.append("Stress management techniques (meditation, deep breathing) may be especially beneficial")

    if results.get("adhd", {}).get("risk_score", 0) > 1:
        recommendations.append("Structured routines and regular sleep schedule support attention")

    if results.get("ptsd_vulnerability", {}).get("risk_score", 0) > 1:
        recommendations.append("Early intervention after trauma exposure is particularly important")

    if results.get("addiction_vulnerability", {}).get("risk_score", 0) > 1:
        recommendations.append("Be aware of substance use patterns - genetic predisposition present")

    cognitive = results.get("cognitive_profile", {}).get("profile", {})
    if cognitive.get("stress_cognition") == "worrier":
        recommendations.append("You may perform best in calm environments - plan for stress management")
    elif cognitive.get("stress_cognition") == "warrior":
        recommendations.append("You may handle stress well but benefit from cognitive challenges")

    if not recommendations:
        recommendations.append("Maintain healthy lifestyle habits for optimal mental health")

    return recommendations
