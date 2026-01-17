"""
Longevity Genetics Database
Real SNPs from scientific literature for lifespan, aging, and longevity genetics
Sources: GWAS Catalog, dbSNP, ClinVar, Published longevity studies
"""

from typing import Dict, Any, List

# =============================================================================
# TELOMERE LENGTH GENETICS
# =============================================================================

TELOMERE_GENETICS = {
    "rs2736100": {
        "gene": "TERT",
        "chromosome": "5",
        "function": "Telomerase reverse transcriptase - maintains telomere length",
        "risk_allele": "C",
        "protective_allele": "A",
        "effect": {
            "CC": {"telomere_effect": "longer", "longevity_impact": "positive", "description": "Associated with longer telomeres"},
            "AC": {"telomere_effect": "average", "longevity_impact": "neutral", "description": "Intermediate telomere length"},
            "AA": {"telomere_effect": "shorter", "longevity_impact": "negative", "description": "Associated with shorter telomeres"}
        },
        "population_frequency": {"C": 0.49, "A": 0.51}
    },
    "rs10936599": {
        "gene": "TERC",
        "chromosome": "3",
        "function": "Telomerase RNA component",
        "risk_allele": "T",
        "protective_allele": "C",
        "effect": {
            "CC": {"telomere_effect": "longer", "longevity_impact": "positive", "description": "Enhanced telomere maintenance"},
            "CT": {"telomere_effect": "average", "longevity_impact": "neutral", "description": "Typical telomere function"},
            "TT": {"telomere_effect": "shorter", "longevity_impact": "negative", "description": "Reduced telomere maintenance"}
        },
        "population_frequency": {"C": 0.75, "T": 0.25}
    },
    "rs7726159": {
        "gene": "TERT",
        "chromosome": "5",
        "function": "Telomerase activity regulation",
        "risk_allele": "A",
        "protective_allele": "C",
        "effect": {
            "CC": {"telomere_effect": "longer", "longevity_impact": "positive", "description": "Optimal telomerase function"},
            "AC": {"telomere_effect": "average", "longevity_impact": "neutral", "description": "Normal telomerase activity"},
            "AA": {"telomere_effect": "shorter", "longevity_impact": "negative", "description": "Reduced telomerase activity"}
        },
        "population_frequency": {"C": 0.68, "A": 0.32}
    },
    "rs3772190": {
        "gene": "NAF1",
        "chromosome": "4",
        "function": "Nuclear assembly factor 1 - telomerase biogenesis",
        "risk_allele": "T",
        "protective_allele": "C",
        "effect": {
            "CC": {"telomere_effect": "longer", "longevity_impact": "positive", "description": "Better telomerase assembly"},
            "CT": {"telomere_effect": "average", "longevity_impact": "neutral", "description": "Normal assembly"},
            "TT": {"telomere_effect": "shorter", "longevity_impact": "negative", "description": "Impaired assembly"}
        },
        "population_frequency": {"C": 0.82, "T": 0.18}
    },
    "rs11125529": {
        "gene": "ACYP2",
        "chromosome": "2",
        "function": "Acylphosphatase 2 - telomere length regulation",
        "risk_allele": "A",
        "protective_allele": "C",
        "effect": {
            "CC": {"telomere_effect": "longer", "longevity_impact": "positive", "description": "Favorable telomere regulation"},
            "AC": {"telomere_effect": "average", "longevity_impact": "neutral", "description": "Typical regulation"},
            "AA": {"telomere_effect": "shorter", "longevity_impact": "negative", "description": "Accelerated shortening"}
        },
        "population_frequency": {"C": 0.88, "A": 0.12}
    }
}

# =============================================================================
# SIRTUIN PATHWAY GENETICS (SIRT1-7)
# =============================================================================

SIRTUIN_GENETICS = {
    "rs7895833": {
        "gene": "SIRT1",
        "chromosome": "10",
        "function": "NAD-dependent deacetylase - caloric restriction pathway",
        "risk_allele": "G",
        "protective_allele": "A",
        "effect": {
            "AA": {"sirtuin_activity": "high", "longevity_impact": "positive", "description": "Enhanced SIRT1 activity, mimics caloric restriction"},
            "AG": {"sirtuin_activity": "moderate", "longevity_impact": "neutral", "description": "Normal SIRT1 function"},
            "GG": {"sirtuin_activity": "low", "longevity_impact": "negative", "description": "Reduced SIRT1 activity"}
        },
        "population_frequency": {"A": 0.45, "G": 0.55}
    },
    "rs3758391": {
        "gene": "SIRT1",
        "chromosome": "10",
        "function": "SIRT1 expression regulation",
        "risk_allele": "C",
        "protective_allele": "T",
        "effect": {
            "TT": {"sirtuin_activity": "high", "longevity_impact": "positive", "description": "Higher SIRT1 expression"},
            "CT": {"sirtuin_activity": "moderate", "longevity_impact": "neutral", "description": "Average expression"},
            "CC": {"sirtuin_activity": "low", "longevity_impact": "negative", "description": "Lower expression"}
        },
        "population_frequency": {"T": 0.72, "C": 0.28}
    },
    "rs2273773": {
        "gene": "SIRT1",
        "chromosome": "10",
        "function": "SIRT1 protein stability",
        "risk_allele": "T",
        "protective_allele": "C",
        "effect": {
            "CC": {"sirtuin_activity": "high", "longevity_impact": "positive", "description": "Stable SIRT1 protein"},
            "CT": {"sirtuin_activity": "moderate", "longevity_impact": "neutral", "description": "Normal stability"},
            "TT": {"sirtuin_activity": "low", "longevity_impact": "negative", "description": "Reduced stability"}
        },
        "population_frequency": {"C": 0.68, "T": 0.32}
    },
    "rs28365964": {
        "gene": "SIRT3",
        "chromosome": "11",
        "function": "Mitochondrial sirtuin - oxidative stress protection",
        "risk_allele": "G",
        "protective_allele": "A",
        "effect": {
            "AA": {"sirtuin_activity": "high", "longevity_impact": "positive", "description": "Enhanced mitochondrial protection"},
            "AG": {"sirtuin_activity": "moderate", "longevity_impact": "neutral", "description": "Normal protection"},
            "GG": {"sirtuin_activity": "low", "longevity_impact": "negative", "description": "Reduced mitochondrial protection"}
        },
        "population_frequency": {"A": 0.58, "G": 0.42}
    },
    "rs11246020": {
        "gene": "SIRT3",
        "chromosome": "11",
        "function": "SIRT3 Val208Ile variant",
        "risk_allele": "A",
        "protective_allele": "G",
        "effect": {
            "GG": {"sirtuin_activity": "high", "longevity_impact": "positive", "description": "Optimal SIRT3 function"},
            "AG": {"sirtuin_activity": "moderate", "longevity_impact": "neutral", "description": "Intermediate function"},
            "AA": {"sirtuin_activity": "low", "longevity_impact": "negative", "description": "Reduced deacetylase activity"}
        },
        "population_frequency": {"G": 0.85, "A": 0.15}
    },
    "rs10823108": {
        "gene": "SIRT6",
        "chromosome": "19",
        "function": "DNA repair and glucose metabolism sirtuin",
        "risk_allele": "T",
        "protective_allele": "C",
        "effect": {
            "CC": {"sirtuin_activity": "high", "longevity_impact": "positive", "description": "Enhanced DNA repair"},
            "CT": {"sirtuin_activity": "moderate", "longevity_impact": "neutral", "description": "Normal repair"},
            "TT": {"sirtuin_activity": "low", "longevity_impact": "negative", "description": "Impaired DNA repair"}
        },
        "population_frequency": {"C": 0.75, "T": 0.25}
    }
}

# =============================================================================
# FOXO PATHWAY GENETICS
# =============================================================================

FOXO_GENETICS = {
    "rs2802292": {
        "gene": "FOXO3",
        "chromosome": "6",
        "function": "Forkhead box O3 - longevity transcription factor",
        "risk_allele": "T",
        "protective_allele": "G",
        "effect": {
            "GG": {"foxo_activity": "high", "longevity_impact": "strongly_positive", "description": "Longevity variant - found in centenarians"},
            "GT": {"foxo_activity": "moderate", "longevity_impact": "positive", "description": "Partial longevity benefit"},
            "TT": {"foxo_activity": "low", "longevity_impact": "neutral", "description": "Common variant"}
        },
        "population_frequency": {"G": 0.25, "T": 0.75},
        "centenarian_frequency": 0.40
    },
    "rs13217795": {
        "gene": "FOXO3",
        "chromosome": "6",
        "function": "FOXO3 regulatory variant",
        "risk_allele": "C",
        "protective_allele": "T",
        "effect": {
            "TT": {"foxo_activity": "high", "longevity_impact": "positive", "description": "Enhanced FOXO3 signaling"},
            "CT": {"foxo_activity": "moderate", "longevity_impact": "neutral", "description": "Normal signaling"},
            "CC": {"foxo_activity": "low", "longevity_impact": "negative", "description": "Reduced signaling"}
        },
        "population_frequency": {"T": 0.30, "C": 0.70}
    },
    "rs2764264": {
        "gene": "FOXO3",
        "chromosome": "6",
        "function": "FOXO3 stress response",
        "risk_allele": "C",
        "protective_allele": "T",
        "effect": {
            "TT": {"foxo_activity": "high", "longevity_impact": "positive", "description": "Better stress response"},
            "CT": {"foxo_activity": "moderate", "longevity_impact": "neutral", "description": "Normal response"},
            "CC": {"foxo_activity": "low", "longevity_impact": "negative", "description": "Reduced stress response"}
        },
        "population_frequency": {"T": 0.28, "C": 0.72}
    },
    "rs4946936": {
        "gene": "FOXO1",
        "chromosome": "13",
        "function": "FOXO1 metabolic regulation",
        "risk_allele": "T",
        "protective_allele": "C",
        "effect": {
            "CC": {"foxo_activity": "high", "longevity_impact": "positive", "description": "Optimal metabolic regulation"},
            "CT": {"foxo_activity": "moderate", "longevity_impact": "neutral", "description": "Normal metabolism"},
            "TT": {"foxo_activity": "low", "longevity_impact": "negative", "description": "Suboptimal regulation"}
        },
        "population_frequency": {"C": 0.62, "T": 0.38}
    }
}

# =============================================================================
# IGF-1/GROWTH HORMONE PATHWAY
# =============================================================================

IGF1_PATHWAY_GENETICS = {
    "rs2229765": {
        "gene": "IGF1R",
        "chromosome": "15",
        "function": "IGF-1 receptor - growth hormone signaling",
        "risk_allele": "G",
        "protective_allele": "A",
        "effect": {
            "AA": {"igf_activity": "reduced", "longevity_impact": "positive", "description": "Lower IGF-1 signaling - associated with longevity"},
            "AG": {"igf_activity": "moderate", "longevity_impact": "neutral", "description": "Normal signaling"},
            "GG": {"igf_activity": "high", "longevity_impact": "negative", "description": "Higher IGF-1 signaling - faster aging"}
        },
        "population_frequency": {"A": 0.35, "G": 0.65}
    },
    "rs6214": {
        "gene": "IGF1",
        "chromosome": "12",
        "function": "IGF-1 production",
        "risk_allele": "A",
        "protective_allele": "G",
        "effect": {
            "GG": {"igf_activity": "lower", "longevity_impact": "positive", "description": "Lower IGF-1 levels - longevity benefit"},
            "AG": {"igf_activity": "moderate", "longevity_impact": "neutral", "description": "Normal IGF-1 levels"},
            "AA": {"igf_activity": "higher", "longevity_impact": "negative", "description": "Higher IGF-1 levels"}
        },
        "population_frequency": {"G": 0.42, "A": 0.58}
    },
    "rs35767": {
        "gene": "IGF1",
        "chromosome": "12",
        "function": "IGF-1 expression regulation",
        "risk_allele": "A",
        "protective_allele": "G",
        "effect": {
            "GG": {"igf_activity": "lower", "longevity_impact": "positive", "description": "Reduced IGF-1 expression"},
            "AG": {"igf_activity": "moderate", "longevity_impact": "neutral", "description": "Normal expression"},
            "AA": {"igf_activity": "higher", "longevity_impact": "negative", "description": "Higher expression"}
        },
        "population_frequency": {"G": 0.48, "A": 0.52}
    },
    "rs10735380": {
        "gene": "GH1",
        "chromosome": "17",
        "function": "Growth hormone secretion",
        "risk_allele": "A",
        "protective_allele": "G",
        "effect": {
            "GG": {"igf_activity": "lower", "longevity_impact": "positive", "description": "Moderate GH secretion"},
            "AG": {"igf_activity": "moderate", "longevity_impact": "neutral", "description": "Normal GH secretion"},
            "AA": {"igf_activity": "higher", "longevity_impact": "neutral", "description": "Higher GH secretion"}
        },
        "population_frequency": {"G": 0.55, "A": 0.45}
    }
}

# =============================================================================
# AUTOPHAGY GENETICS
# =============================================================================

AUTOPHAGY_GENETICS = {
    "rs2245214": {
        "gene": "ATG16L1",
        "chromosome": "2",
        "function": "Autophagy-related 16-like 1",
        "risk_allele": "C",
        "protective_allele": "G",
        "effect": {
            "GG": {"autophagy": "normal", "longevity_impact": "positive", "description": "Normal autophagy function"},
            "CG": {"autophagy": "reduced", "longevity_impact": "neutral", "description": "Slightly reduced autophagy"},
            "CC": {"autophagy": "impaired", "longevity_impact": "negative", "description": "Impaired autophagy"}
        },
        "population_frequency": {"G": 0.55, "C": 0.45}
    },
    "rs6861": {
        "gene": "BECN1",
        "chromosome": "17",
        "function": "Beclin-1 - autophagy initiation",
        "risk_allele": "A",
        "protective_allele": "G",
        "effect": {
            "GG": {"autophagy": "enhanced", "longevity_impact": "positive", "description": "Enhanced autophagy initiation"},
            "AG": {"autophagy": "normal", "longevity_impact": "neutral", "description": "Normal initiation"},
            "AA": {"autophagy": "reduced", "longevity_impact": "negative", "description": "Reduced autophagy"}
        },
        "population_frequency": {"G": 0.62, "A": 0.38}
    },
    "rs510432": {
        "gene": "ATG5",
        "chromosome": "6",
        "function": "Autophagy protein 5",
        "risk_allele": "T",
        "protective_allele": "C",
        "effect": {
            "CC": {"autophagy": "normal", "longevity_impact": "positive", "description": "Normal autophagy"},
            "CT": {"autophagy": "normal", "longevity_impact": "neutral", "description": "Normal function"},
            "TT": {"autophagy": "reduced", "longevity_impact": "negative", "description": "Reduced autophagy capacity"}
        },
        "population_frequency": {"C": 0.70, "T": 0.30}
    },
    "rs12201458": {
        "gene": "ULK1",
        "chromosome": "12",
        "function": "UNC-51-like kinase 1 - autophagy regulation",
        "risk_allele": "A",
        "protective_allele": "G",
        "effect": {
            "GG": {"autophagy": "enhanced", "longevity_impact": "positive", "description": "Enhanced autophagy regulation"},
            "AG": {"autophagy": "normal", "longevity_impact": "neutral", "description": "Normal regulation"},
            "AA": {"autophagy": "reduced", "longevity_impact": "negative", "description": "Impaired regulation"}
        },
        "population_frequency": {"G": 0.78, "A": 0.22}
    }
}

# =============================================================================
# MITOCHONDRIAL FUNCTION GENETICS
# =============================================================================

MITOCHONDRIAL_GENETICS = {
    "rs11006132": {
        "gene": "PPARGC1A",
        "chromosome": "4",
        "function": "PGC-1alpha - mitochondrial biogenesis master regulator",
        "risk_allele": "T",
        "protective_allele": "C",
        "effect": {
            "CC": {"mito_function": "enhanced", "longevity_impact": "positive", "description": "Enhanced mitochondrial biogenesis"},
            "CT": {"mito_function": "normal", "longevity_impact": "neutral", "description": "Normal biogenesis"},
            "TT": {"mito_function": "reduced", "longevity_impact": "negative", "description": "Reduced biogenesis capacity"}
        },
        "population_frequency": {"C": 0.65, "T": 0.35}
    },
    "rs8192678": {
        "gene": "PPARGC1A",
        "chromosome": "4",
        "function": "PGC-1alpha Gly482Ser variant",
        "risk_allele": "A",
        "protective_allele": "G",
        "effect": {
            "GG": {"mito_function": "optimal", "longevity_impact": "positive", "description": "Gly482 - optimal mitochondrial function"},
            "AG": {"mito_function": "normal", "longevity_impact": "neutral", "description": "Heterozygous - normal function"},
            "AA": {"mito_function": "reduced", "longevity_impact": "negative", "description": "Ser482 - reduced efficiency"}
        },
        "population_frequency": {"G": 0.58, "A": 0.42}
    },
    "rs4253778": {
        "gene": "PPARA",
        "chromosome": "22",
        "function": "Peroxisome proliferator-activated receptor alpha",
        "risk_allele": "C",
        "protective_allele": "G",
        "effect": {
            "GG": {"mito_function": "enhanced", "longevity_impact": "positive", "description": "Better fatty acid oxidation"},
            "CG": {"mito_function": "normal", "longevity_impact": "neutral", "description": "Normal oxidation"},
            "CC": {"mito_function": "reduced", "longevity_impact": "negative", "description": "Reduced fat metabolism"}
        },
        "population_frequency": {"G": 0.82, "C": 0.18}
    },
    "rs1800849": {
        "gene": "UCP3",
        "chromosome": "11",
        "function": "Uncoupling protein 3 - mitochondrial efficiency",
        "risk_allele": "T",
        "protective_allele": "C",
        "effect": {
            "CC": {"mito_function": "efficient", "longevity_impact": "positive", "description": "Efficient mitochondria"},
            "CT": {"mito_function": "normal", "longevity_impact": "neutral", "description": "Normal efficiency"},
            "TT": {"mito_function": "less_efficient", "longevity_impact": "neutral", "description": "Higher heat generation"}
        },
        "population_frequency": {"C": 0.72, "T": 0.28}
    },
    "rs10521108": {
        "gene": "TFAM",
        "chromosome": "10",
        "function": "Mitochondrial transcription factor A",
        "risk_allele": "A",
        "protective_allele": "G",
        "effect": {
            "GG": {"mito_function": "optimal", "longevity_impact": "positive", "description": "Optimal mtDNA transcription"},
            "AG": {"mito_function": "normal", "longevity_impact": "neutral", "description": "Normal transcription"},
            "AA": {"mito_function": "reduced", "longevity_impact": "negative", "description": "Reduced mtDNA maintenance"}
        },
        "population_frequency": {"G": 0.85, "A": 0.15}
    }
}

# =============================================================================
# CELLULAR SENESCENCE GENETICS
# =============================================================================

SENESCENCE_GENETICS = {
    "rs1042522": {
        "gene": "TP53",
        "chromosome": "17",
        "function": "Tumor protein p53 - cellular senescence regulator",
        "risk_allele": "C",
        "protective_allele": "G",
        "effect": {
            "GG": {"senescence": "balanced", "longevity_impact": "positive", "description": "Arg72 - balanced apoptosis/senescence"},
            "CG": {"senescence": "normal", "longevity_impact": "neutral", "description": "Heterozygous - normal function"},
            "CC": {"senescence": "enhanced", "longevity_impact": "neutral", "description": "Pro72 - enhanced apoptosis"}
        },
        "population_frequency": {"G": 0.60, "C": 0.40}
    },
    "rs2279744": {
        "gene": "MDM2",
        "chromosome": "12",
        "function": "MDM2 proto-oncogene - p53 regulator",
        "risk_allele": "G",
        "protective_allele": "T",
        "effect": {
            "TT": {"senescence": "normal", "longevity_impact": "neutral", "description": "Normal p53 regulation"},
            "TG": {"senescence": "reduced", "longevity_impact": "neutral", "description": "Slightly reduced p53 activity"},
            "GG": {"senescence": "reduced", "longevity_impact": "variable", "description": "SNP309 - reduced p53"}
        },
        "population_frequency": {"T": 0.60, "G": 0.40}
    },
    "rs2811712": {
        "gene": "CDKN2A",
        "chromosome": "9",
        "function": "p16INK4a - senescence marker",
        "risk_allele": "C",
        "protective_allele": "T",
        "effect": {
            "TT": {"senescence": "normal", "longevity_impact": "positive", "description": "Normal p16 expression"},
            "CT": {"senescence": "normal", "longevity_impact": "neutral", "description": "Normal function"},
            "CC": {"senescence": "elevated", "longevity_impact": "negative", "description": "Elevated senescence"}
        },
        "population_frequency": {"T": 0.75, "C": 0.25}
    }
}

# =============================================================================
# INFLAMMATION & AGING (INFLAMMAGING)
# =============================================================================

INFLAMMAGING_GENETICS = {
    "rs1800795": {
        "gene": "IL6",
        "chromosome": "7",
        "function": "Interleukin-6 - inflammatory cytokine",
        "risk_allele": "G",
        "protective_allele": "C",
        "effect": {
            "CC": {"inflammation": "low", "longevity_impact": "positive", "description": "Lower IL-6 production - reduced inflammation"},
            "CG": {"inflammation": "moderate", "longevity_impact": "neutral", "description": "Moderate IL-6"},
            "GG": {"inflammation": "high", "longevity_impact": "negative", "description": "Higher IL-6 - increased inflammation"}
        },
        "population_frequency": {"C": 0.40, "G": 0.60}
    },
    "rs1800896": {
        "gene": "IL10",
        "chromosome": "1",
        "function": "Interleukin-10 - anti-inflammatory cytokine",
        "risk_allele": "A",
        "protective_allele": "G",
        "effect": {
            "GG": {"inflammation": "low", "longevity_impact": "positive", "description": "Higher IL-10 - better inflammation control"},
            "AG": {"inflammation": "moderate", "longevity_impact": "neutral", "description": "Moderate IL-10"},
            "AA": {"inflammation": "high", "longevity_impact": "negative", "description": "Lower IL-10 - less inflammation control"}
        },
        "population_frequency": {"G": 0.50, "A": 0.50}
    },
    "rs1800629": {
        "gene": "TNF",
        "chromosome": "6",
        "function": "Tumor necrosis factor alpha",
        "risk_allele": "A",
        "protective_allele": "G",
        "effect": {
            "GG": {"inflammation": "low", "longevity_impact": "positive", "description": "Lower TNF-alpha production"},
            "AG": {"inflammation": "moderate", "longevity_impact": "neutral", "description": "Moderate TNF-alpha"},
            "AA": {"inflammation": "high", "longevity_impact": "negative", "description": "Higher TNF-alpha - increased inflammation"}
        },
        "population_frequency": {"G": 0.85, "A": 0.15}
    }
}

# =============================================================================
# KLOTHO & ANTI-AGING GENETICS
# =============================================================================

KLOTHO_GENETICS = {
    "rs9536314": {
        "gene": "KL",
        "chromosome": "13",
        "function": "Klotho - anti-aging hormone",
        "risk_allele": "G",
        "protective_allele": "T",
        "effect": {
            "TT": {"klotho_level": "higher", "longevity_impact": "positive", "description": "KL-VS variant - higher klotho, better cognition"},
            "GT": {"klotho_level": "elevated", "longevity_impact": "positive", "description": "Heterozygous - cognitive benefit"},
            "GG": {"klotho_level": "normal", "longevity_impact": "neutral", "description": "Normal klotho levels"}
        },
        "population_frequency": {"T": 0.16, "G": 0.84}
    },
    "rs9527025": {
        "gene": "KL",
        "chromosome": "13",
        "function": "Klotho expression",
        "risk_allele": "C",
        "protective_allele": "G",
        "effect": {
            "GG": {"klotho_level": "higher", "longevity_impact": "positive", "description": "Elevated klotho expression"},
            "CG": {"klotho_level": "moderate", "longevity_impact": "neutral", "description": "Normal expression"},
            "CC": {"klotho_level": "lower", "longevity_impact": "negative", "description": "Reduced klotho"}
        },
        "population_frequency": {"G": 0.18, "C": 0.82}
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


def analyze_longevity_genetics(dna_data: Dict[str, str]) -> Dict[str, Any]:
    """
    Analyze DNA data for longevity-related genetic markers

    Args:
        dna_data: Dictionary mapping rsIDs to genotypes

    Returns:
        Dictionary containing longevity analysis results
    """
    results = {}

    # Analyze telomere genetics
    telomere_results = []
    telomere_score = 0
    for rsid, snp_info in TELOMERE_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                telomere_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "telomere_effect": effect["telomere_effect"],
                    "description": effect["description"]
                })
                if effect["longevity_impact"] == "positive":
                    telomere_score += 1
                elif effect["longevity_impact"] == "negative":
                    telomere_score -= 1

    if telomere_results:
        if telomere_score >= 2:
            telomere_assessment = "Favorable - genetic variants support longer telomere maintenance"
        elif telomere_score <= -2:
            telomere_assessment = "Less favorable - may benefit from telomere-protective lifestyle"
        else:
            telomere_assessment = "Average telomere genetics"
    else:
        telomere_assessment = "Insufficient data"

    results["telomere_length"] = {
        "score": telomere_score,
        "assessment": telomere_assessment,
        "variants_analyzed": len(telomere_results),
        "snps_analyzed": telomere_results
    }

    # Analyze sirtuin pathway
    sirtuin_results = []
    sirtuin_score = 0
    for rsid, snp_info in SIRTUIN_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                sirtuin_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "activity": effect["sirtuin_activity"],
                    "description": effect["description"]
                })
                if effect["longevity_impact"] == "positive":
                    sirtuin_score += 1
                elif effect["longevity_impact"] == "negative":
                    sirtuin_score -= 1

    if sirtuin_results:
        if sirtuin_score >= 3:
            sirtuin_assessment = "Enhanced - sirtuin pathway favors longevity (caloric restriction mimetic effect)"
        elif sirtuin_score <= -2:
            sirtuin_assessment = "Reduced - may benefit from sirtuin activators (resveratrol, NAD+ precursors)"
        else:
            sirtuin_assessment = "Normal sirtuin activity"
    else:
        sirtuin_assessment = "Insufficient data"

    results["sirtuin_pathway"] = {
        "score": sirtuin_score,
        "assessment": sirtuin_assessment,
        "variants_analyzed": len(sirtuin_results),
        "snps_analyzed": sirtuin_results
    }

    # Analyze FOXO pathway
    foxo_results = []
    foxo_score = 0
    has_longevity_variant = False
    for rsid, snp_info in FOXO_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                foxo_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "activity": effect["foxo_activity"],
                    "description": effect["description"]
                })
                if effect["longevity_impact"] == "strongly_positive":
                    foxo_score += 2
                    has_longevity_variant = True
                elif effect["longevity_impact"] == "positive":
                    foxo_score += 1
                elif effect["longevity_impact"] == "negative":
                    foxo_score -= 1

    if foxo_results:
        if has_longevity_variant:
            foxo_assessment = "Exceptional - carries FOXO3 longevity variant found in centenarians"
        elif foxo_score >= 2:
            foxo_assessment = "Favorable FOXO signaling for longevity"
        elif foxo_score <= -1:
            foxo_assessment = "Typical FOXO variants"
        else:
            foxo_assessment = "Normal FOXO function"
    else:
        foxo_assessment = "Insufficient data"

    results["foxo_pathway"] = {
        "score": foxo_score,
        "assessment": foxo_assessment,
        "has_centenarian_variant": has_longevity_variant,
        "variants_analyzed": len(foxo_results),
        "snps_analyzed": foxo_results
    }

    # Analyze IGF-1 pathway
    igf_results = []
    igf_score = 0
    for rsid, snp_info in IGF1_PATHWAY_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                igf_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "igf_level": effect["igf_activity"],
                    "description": effect["description"]
                })
                if effect["longevity_impact"] == "positive":
                    igf_score += 1
                elif effect["longevity_impact"] == "negative":
                    igf_score -= 1

    if igf_results:
        if igf_score >= 2:
            igf_assessment = "Favorable - lower IGF-1 signaling associated with longevity"
        elif igf_score <= -2:
            igf_assessment = "Higher IGF-1 - good for muscle but may accelerate aging"
        else:
            igf_assessment = "Normal IGF-1 pathway"
    else:
        igf_assessment = "Insufficient data"

    results["igf1_pathway"] = {
        "score": igf_score,
        "assessment": igf_assessment,
        "variants_analyzed": len(igf_results),
        "snps_analyzed": igf_results
    }

    # Analyze autophagy
    autophagy_results = []
    autophagy_score = 0
    for rsid, snp_info in AUTOPHAGY_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                autophagy_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "autophagy_level": effect["autophagy"],
                    "description": effect["description"]
                })
                if effect["longevity_impact"] == "positive":
                    autophagy_score += 1
                elif effect["longevity_impact"] == "negative":
                    autophagy_score -= 1

    if autophagy_results:
        if autophagy_score >= 2:
            autophagy_assessment = "Enhanced autophagy - efficient cellular cleanup"
        elif autophagy_score <= -2:
            autophagy_assessment = "Reduced autophagy - may benefit from fasting/exercise"
        else:
            autophagy_assessment = "Normal autophagy function"
    else:
        autophagy_assessment = "Insufficient data"

    results["autophagy"] = {
        "score": autophagy_score,
        "assessment": autophagy_assessment,
        "variants_analyzed": len(autophagy_results),
        "snps_analyzed": autophagy_results
    }

    # Analyze mitochondrial function
    mito_results = []
    mito_score = 0
    for rsid, snp_info in MITOCHONDRIAL_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                mito_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "function": effect["mito_function"],
                    "description": effect["description"]
                })
                if effect["longevity_impact"] == "positive":
                    mito_score += 1
                elif effect["longevity_impact"] == "negative":
                    mito_score -= 1

    if mito_results:
        if mito_score >= 2:
            mito_assessment = "Optimal mitochondrial genetics - efficient energy production"
        elif mito_score <= -2:
            mito_assessment = "May benefit from CoQ10, PQQ, and mitochondrial support"
        else:
            mito_assessment = "Normal mitochondrial function"
    else:
        mito_assessment = "Insufficient data"

    results["mitochondrial_function"] = {
        "score": mito_score,
        "assessment": mito_assessment,
        "variants_analyzed": len(mito_results),
        "snps_analyzed": mito_results
    }

    # Analyze inflammaging
    inflammation_results = []
    inflammation_score = 0
    for rsid, snp_info in INFLAMMAGING_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                inflammation_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "inflammation_level": effect["inflammation"],
                    "description": effect["description"]
                })
                if effect["longevity_impact"] == "positive":
                    inflammation_score += 1
                elif effect["longevity_impact"] == "negative":
                    inflammation_score -= 1

    if inflammation_results:
        if inflammation_score >= 2:
            inflammation_assessment = "Low inflammatory genetics - favorable for aging"
        elif inflammation_score <= -2:
            inflammation_assessment = "Pro-inflammatory variants - anti-inflammatory lifestyle recommended"
        else:
            inflammation_assessment = "Normal inflammatory response"
    else:
        inflammation_assessment = "Insufficient data"

    results["inflammaging"] = {
        "score": inflammation_score,
        "assessment": inflammation_assessment,
        "variants_analyzed": len(inflammation_results),
        "snps_analyzed": inflammation_results
    }

    # Analyze Klotho
    klotho_results = []
    klotho_score = 0
    has_klvs = False
    for rsid, snp_info in KLOTHO_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                klotho_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "klotho_level": effect["klotho_level"],
                    "description": effect["description"]
                })
                if effect["longevity_impact"] == "positive":
                    klotho_score += 1
                    if rsid == "rs9536314" and effect["klotho_level"] in ["higher", "elevated"]:
                        has_klvs = True
                elif effect["longevity_impact"] == "negative":
                    klotho_score -= 1

    if klotho_results:
        if has_klvs:
            klotho_assessment = "Carries KL-VS variant - associated with cognitive longevity and higher klotho"
        elif klotho_score >= 1:
            klotho_assessment = "Favorable klotho genetics"
        else:
            klotho_assessment = "Normal klotho levels"
    else:
        klotho_assessment = "Insufficient data"

    results["klotho"] = {
        "score": klotho_score,
        "assessment": klotho_assessment,
        "has_klvs_variant": has_klvs,
        "variants_analyzed": len(klotho_results),
        "snps_analyzed": klotho_results
    }

    # Calculate overall longevity score
    total_positive = sum([
        results["telomere_length"]["score"],
        results["sirtuin_pathway"]["score"],
        results["foxo_pathway"]["score"],
        results["igf1_pathway"]["score"],
        results["autophagy"]["score"],
        results["mitochondrial_function"]["score"],
        results["inflammaging"]["score"],
        results["klotho"]["score"]
    ])

    total_variants = sum([
        results["telomere_length"]["variants_analyzed"],
        results["sirtuin_pathway"]["variants_analyzed"],
        results["foxo_pathway"]["variants_analyzed"],
        results["igf1_pathway"]["variants_analyzed"],
        results["autophagy"]["variants_analyzed"],
        results["mitochondrial_function"]["variants_analyzed"],
        results["inflammaging"]["variants_analyzed"],
        results["klotho"]["variants_analyzed"]
    ])

    if total_variants > 0:
        if total_positive >= 10:
            overall = "Exceptional longevity genetics"
            percentile = 95
        elif total_positive >= 5:
            overall = "Favorable longevity genetics"
            percentile = 75
        elif total_positive >= 0:
            overall = "Average longevity genetics"
            percentile = 50
        elif total_positive >= -5:
            overall = "Below average - lifestyle interventions important"
            percentile = 30
        else:
            overall = "May benefit significantly from longevity-focused lifestyle"
            percentile = 15
    else:
        overall = "Insufficient data"
        percentile = None

    results["overall"] = {
        "total_score": total_positive,
        "assessment": overall,
        "percentile": percentile,
        "variants_analyzed": total_variants,
        "recommendations": get_longevity_recommendations(results)
    }

    return results


def get_longevity_recommendations(results: Dict[str, Any]) -> List[str]:
    """Generate personalized longevity recommendations based on genetic results"""
    recommendations = []

    if results.get("telomere_length", {}).get("score", 0) < 0:
        recommendations.append("Consider telomere-protective activities: meditation, omega-3s, adequate sleep")

    if results.get("sirtuin_pathway", {}).get("score", 0) < 0:
        recommendations.append("May benefit from NAD+ precursors (NMN/NR) and resveratrol for sirtuin activation")

    if results.get("autophagy", {}).get("score", 0) < 0:
        recommendations.append("Intermittent fasting and exercise can enhance autophagy")

    if results.get("mitochondrial_function", {}).get("score", 0) < 0:
        recommendations.append("Consider CoQ10, PQQ, and mitochondrial support supplements")

    if results.get("inflammaging", {}).get("score", 0) < 0:
        recommendations.append("Anti-inflammatory diet (omega-3s, turmeric, green vegetables) recommended")

    if results.get("foxo_pathway", {}).get("has_centenarian_variant"):
        recommendations.append("Carry rare FOXO3 longevity variant - maintain healthy lifestyle to maximize benefit")

    if results.get("klotho", {}).get("has_klvs_variant"):
        recommendations.append("KL-VS variant carrier - cognitive activities help maintain klotho benefits")

    if not recommendations:
        recommendations.append("Maintain balanced lifestyle with regular exercise, healthy diet, and adequate sleep")

    return recommendations
