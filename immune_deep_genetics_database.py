"""
Immune System Deep Dive Genetics Database
Real SNP data for comprehensive immune system genetic analysis

Features:
1. HLA Type Analysis (autoimmune/transplant)
2. Cytokine Response Genetics (IL-6, TNF-alpha)
3. Inflammatory Response
4. Allergy Susceptibility
5. Celiac Disease Risk
6. Lupus (SLE) Genetic Risk
7. Multiple Sclerosis Risk
8. Rheumatoid Arthritis Risk
9. Psoriasis Risk
10. IBD/Crohn's Disease Risk
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
# HLA TYPE MARKERS
# =============================================================================

HLA_GENETICS = {
    # HLA-B27 - strongly associated with ankylosing spondylitis
    "rs4349859": {
        "gene": "HLA-B27 tag",
        "chromosome": "6",
        "function": "Tags HLA-B*27 haplotype",
        "risk_allele": "A",
        "effect": {
            "AA": {"hla_b27_likely": True, "ankylosing_spondylitis_risk": "Very High", "risk_multiplier": 40.0},
            "AG": {"hla_b27_likely": True, "ankylosing_spondylitis_risk": "High", "risk_multiplier": 15.0},
            "GG": {"hla_b27_likely": False, "ankylosing_spondylitis_risk": "Normal", "risk_multiplier": 1.0}
        },
        "population_frequency": {"EUR": 0.08, "AFR": 0.02, "EAS": 0.04}
    },
    # HLA-DQ2 - celiac disease, type 1 diabetes
    "rs2187668": {
        "gene": "HLA-DQ2.5 tag",
        "chromosome": "6",
        "function": "Tags HLA-DQ2.5 (DQA1*05:01-DQB1*02:01)",
        "risk_allele": "A",
        "effect": {
            "AA": {"hla_dq2_positive": True, "celiac_risk": "Very High", "t1d_risk": "Elevated"},
            "AG": {"hla_dq2_positive": "Possible", "celiac_risk": "Moderate", "t1d_risk": "Slightly Elevated"},
            "GG": {"hla_dq2_positive": False, "celiac_risk": "Low", "t1d_risk": "Normal"}
        },
        "population_frequency": {"EUR": 0.20, "AFR": 0.10, "EAS": 0.05}
    },
    # HLA-DQ8 - celiac, T1D
    "rs7454108": {
        "gene": "HLA-DQ8 tag",
        "chromosome": "6",
        "function": "Tags HLA-DQ8 (DQA1*03-DQB1*03:02)",
        "risk_allele": "C",
        "effect": {
            "CC": {"hla_dq8_positive": True, "celiac_risk": "High", "t1d_risk": "High"},
            "CT": {"hla_dq8_positive": "Possible", "celiac_risk": "Moderate", "t1d_risk": "Moderate"},
            "TT": {"hla_dq8_positive": False, "celiac_risk": "Lower", "t1d_risk": "Lower"}
        },
        "population_frequency": {"EUR": 0.15, "AFR": 0.08, "EAS": 0.12}
    },
    # HLA-DRB1 shared epitope - rheumatoid arthritis
    "rs6910071": {
        "gene": "HLA-DRB1 region",
        "chromosome": "6",
        "function": "Associated with shared epitope for RA",
        "risk_allele": "A",
        "effect": {
            "AA": {"ra_risk": "High", "shared_epitope_likely": True},
            "AG": {"ra_risk": "Moderate", "shared_epitope_likely": "Possible"},
            "GG": {"ra_risk": "Normal", "shared_epitope_likely": False}
        },
        "population_frequency": {"EUR": 0.25, "AFR": 0.15, "EAS": 0.20}
    }
}

# =============================================================================
# CYTOKINE RESPONSE GENETICS
# =============================================================================

CYTOKINE_GENETICS = {
    # IL-6 promoter - inflammation levels
    "rs1800795": {
        "gene": "IL6",
        "chromosome": "7",
        "function": "IL-6 promoter polymorphism (-174G/C)",
        "common_name": "IL-6 -174 G/C",
        "risk_allele": "C",
        "effect": {
            "GG": {"il6_production": "Higher", "inflammation_tendency": "Higher", "response": "Pro-inflammatory"},
            "GC": {"il6_production": "Moderate", "inflammation_tendency": "Moderate", "response": "Intermediate"},
            "CC": {"il6_production": "Lower", "inflammation_tendency": "Lower", "response": "Anti-inflammatory tendency"}
        },
        "population_frequency": {"EUR": 0.40, "AFR": 0.05, "EAS": 0.02}
    },
    # TNF-alpha promoter - inflammation
    "rs1800629": {
        "gene": "TNF",
        "chromosome": "6",
        "function": "TNF-alpha promoter polymorphism (-308G/A)",
        "common_name": "TNF-alpha -308",
        "risk_allele": "A",
        "effect": {
            "AA": {"tnf_production": "Very High", "inflammation_tendency": "Very High", "autoimmune_risk": "Elevated"},
            "GA": {"tnf_production": "High", "inflammation_tendency": "High", "autoimmune_risk": "Moderately Elevated"},
            "GG": {"tnf_production": "Normal", "inflammation_tendency": "Normal", "autoimmune_risk": "Normal"}
        },
        "population_frequency": {"EUR": 0.17, "AFR": 0.12, "EAS": 0.05}
    },
    # IL-1beta
    "rs16944": {
        "gene": "IL1B",
        "chromosome": "2",
        "function": "IL-1beta promoter (-511)",
        "risk_allele": "A",
        "effect": {
            "AA": {"il1b_production": "Higher", "fever_response": "Strong"},
            "AG": {"il1b_production": "Moderate", "fever_response": "Normal"},
            "GG": {"il1b_production": "Normal", "fever_response": "Normal"}
        },
        "population_frequency": {"EUR": 0.33, "AFR": 0.45, "EAS": 0.50}
    },
    # IL-10 - anti-inflammatory
    "rs1800896": {
        "gene": "IL10",
        "chromosome": "1",
        "function": "IL-10 promoter (-1082)",
        "allele_effect": "A",
        "effect": {
            "AA": {"il10_production": "Low", "anti_inflammatory": "Reduced", "autoimmune_risk": "Higher"},
            "AG": {"il10_production": "Moderate", "anti_inflammatory": "Moderate", "autoimmune_risk": "Normal"},
            "GG": {"il10_production": "High", "anti_inflammatory": "Strong", "autoimmune_risk": "Lower"}
        },
        "population_frequency": {"EUR": 0.48, "AFR": 0.35, "EAS": 0.25}
    },
    # Interferon gamma
    "rs2430561": {
        "gene": "IFNG",
        "chromosome": "12",
        "function": "IFN-gamma +874 A/T",
        "risk_allele": "T",
        "effect": {
            "TT": {"ifng_production": "High", "th1_response": "Strong", "pathogen_clearance": "Enhanced"},
            "TA": {"ifng_production": "Moderate", "th1_response": "Normal", "pathogen_clearance": "Normal"},
            "AA": {"ifng_production": "Low", "th1_response": "Reduced", "pathogen_clearance": "May be reduced"}
        },
        "population_frequency": {"EUR": 0.45, "AFR": 0.55, "EAS": 0.40}
    }
}

# =============================================================================
# INFLAMMATORY RESPONSE GENETICS
# =============================================================================

INFLAMMATORY_GENETICS = {
    # CRP - baseline inflammation marker
    "rs3093077": {
        "gene": "CRP",
        "chromosome": "1",
        "function": "Affects baseline CRP levels",
        "risk_allele": "T",
        "effect": {
            "TT": {"baseline_crp": "Elevated", "cardiovascular_inflammation": "Higher"},
            "GT": {"baseline_crp": "Moderately Elevated", "cardiovascular_inflammation": "Moderate"},
            "GG": {"baseline_crp": "Normal", "cardiovascular_inflammation": "Normal"}
        },
        "population_frequency": {"EUR": 0.08, "AFR": 0.15, "EAS": 0.25}
    },
    "rs1205": {
        "gene": "CRP",
        "chromosome": "1",
        "function": "CRP levels regulation",
        "effect": {
            "CC": {"crp_level": "Lower", "inflammation_baseline": "Reduced"},
            "CT": {"crp_level": "Normal", "inflammation_baseline": "Normal"},
            "TT": {"crp_level": "Higher", "inflammation_baseline": "Elevated"}
        },
        "population_frequency": {"EUR": 0.32, "AFR": 0.15, "EAS": 0.08}
    },
    # NF-kB pathway
    "rs28362491": {
        "gene": "NFKB1",
        "chromosome": "4",
        "function": "NF-kB1 promoter deletion",
        "effect": {
            "DD": {"nfkb_activity": "Higher", "inflammatory_genes": "Upregulated"},
            "ID": {"nfkb_activity": "Moderate", "inflammatory_genes": "Normal"},
            "II": {"nfkb_activity": "Normal", "inflammatory_genes": "Normal"}
        },
        "population_frequency": {"EUR": 0.38, "AFR": 0.42, "EAS": 0.45}
    },
    # COX-2 inflammation
    "rs20417": {
        "gene": "PTGS2",
        "chromosome": "1",
        "function": "COX-2 expression",
        "effect": {
            "CC": {"cox2_expression": "Higher", "prostaglandin": "Elevated"},
            "CG": {"cox2_expression": "Normal", "prostaglandin": "Normal"},
            "GG": {"cox2_expression": "Lower", "prostaglandin": "Reduced"}
        },
        "population_frequency": {"EUR": 0.15, "AFR": 0.30, "EAS": 0.05}
    }
}

# =============================================================================
# ALLERGY SUSCEPTIBILITY GENETICS
# =============================================================================

ALLERGY_GENETICS = {
    # IgE levels - total allergy susceptibility
    "rs2251746": {
        "gene": "FCER1A",
        "chromosome": "1",
        "function": "High-affinity IgE receptor alpha",
        "risk_allele": "C",
        "effect": {
            "CC": {"ige_levels": "High", "allergy_susceptibility": "High", "atopy_risk": "Elevated"},
            "CT": {"ige_levels": "Moderate", "allergy_susceptibility": "Moderate", "atopy_risk": "Normal"},
            "TT": {"ige_levels": "Normal", "allergy_susceptibility": "Normal", "atopy_risk": "Normal"}
        },
        "population_frequency": {"EUR": 0.25, "AFR": 0.20, "EAS": 0.30}
    },
    # IL-4 receptor - Th2 response
    "rs1805010": {
        "gene": "IL4R",
        "chromosome": "16",
        "function": "IL-4 receptor alpha (I50V)",
        "risk_allele": "A",
        "effect": {
            "AA": {"il4_response": "Enhanced", "th2_bias": "Strong", "allergy_risk": "Higher"},
            "AG": {"il4_response": "Normal", "th2_bias": "Moderate", "allergy_risk": "Normal"},
            "GG": {"il4_response": "Normal", "th2_bias": "Normal", "allergy_risk": "Lower"}
        },
        "population_frequency": {"EUR": 0.45, "AFR": 0.60, "EAS": 0.30}
    },
    # FLG - skin barrier, eczema, allergies
    "rs61816761": {
        "gene": "FLG",
        "chromosome": "1",
        "function": "Filaggrin R501X loss-of-function",
        "risk_allele": "A",
        "effect": {
            "AA": {"skin_barrier": "Severely Impaired", "eczema_risk": "Very High", "food_allergy_risk": "High"},
            "GA": {"skin_barrier": "Impaired", "eczema_risk": "High", "food_allergy_risk": "Elevated"},
            "GG": {"skin_barrier": "Normal", "eczema_risk": "Normal", "food_allergy_risk": "Normal"}
        },
        "population_frequency": {"EUR": 0.04, "AFR": 0.01, "EAS": 0.01}
    },
    # Histamine metabolism
    "rs1050891": {
        "gene": "HNMT",
        "chromosome": "2",
        "function": "Histamine N-methyltransferase",
        "effect": {
            "CC": {"histamine_clearance": "Normal", "histamine_sensitivity": "Normal"},
            "CT": {"histamine_clearance": "Reduced", "histamine_sensitivity": "Increased"},
            "TT": {"histamine_clearance": "Low", "histamine_sensitivity": "High"}
        },
        "population_frequency": {"EUR": 0.12, "AFR": 0.08, "EAS": 0.15}
    }
}

# =============================================================================
# CELIAC DISEASE GENETICS
# =============================================================================

CELIAC_GENETICS = {
    # Primary HLA markers covered in HLA_GENETICS
    # Additional non-HLA risk markers
    "rs2816316": {
        "gene": "RGS1",
        "chromosome": "1",
        "function": "Regulator of G-protein signaling",
        "risk_allele": "C",
        "effect": {
            "CC": {"celiac_risk_modifier": "Increased"},
            "CT": {"celiac_risk_modifier": "Slightly Increased"},
            "TT": {"celiac_risk_modifier": "Normal"}
        },
        "population_frequency": {"EUR": 0.18, "AFR": 0.10, "EAS": 0.08}
    },
    "rs13151961": {
        "gene": "IL2/IL21",
        "chromosome": "4",
        "function": "Interleukin 2/21 region",
        "risk_allele": "A",
        "effect": {
            "AA": {"celiac_immune_component": "Higher Risk"},
            "AG": {"celiac_immune_component": "Moderate Risk"},
            "GG": {"celiac_immune_component": "Normal"}
        },
        "population_frequency": {"EUR": 0.25, "AFR": 0.15, "EAS": 0.20}
    },
    "rs17810546": {
        "gene": "IL12A",
        "chromosome": "3",
        "function": "IL-12 subunit alpha",
        "risk_allele": "G",
        "effect": {
            "GG": {"th1_response": "Altered", "celiac_modifier": "Risk Increased"},
            "AG": {"th1_response": "Slightly Altered", "celiac_modifier": "Slight Risk"},
            "AA": {"th1_response": "Normal", "celiac_modifier": "Normal"}
        },
        "population_frequency": {"EUR": 0.08, "AFR": 0.05, "EAS": 0.03}
    }
}

# =============================================================================
# LUPUS (SLE) GENETICS
# =============================================================================

LUPUS_GENETICS = {
    # STAT4 - major SLE risk gene
    "rs7574865": {
        "gene": "STAT4",
        "chromosome": "2",
        "function": "Signal transducer and activator",
        "risk_allele": "T",
        "odds_ratio": 1.55,
        "effect": {
            "TT": {"sle_risk": "High", "risk_score": 2},
            "GT": {"sle_risk": "Moderately Increased", "risk_score": 1},
            "GG": {"sle_risk": "Normal", "risk_score": 0}
        },
        "population_frequency": {"EUR": 0.23, "AFR": 0.35, "EAS": 0.40}
    },
    # IRF5 - interferon regulatory factor
    "rs2004640": {
        "gene": "IRF5",
        "chromosome": "7",
        "function": "Interferon regulatory factor 5",
        "risk_allele": "T",
        "odds_ratio": 1.50,
        "effect": {
            "TT": {"sle_risk": "Elevated", "interferon_signature": "High"},
            "GT": {"sle_risk": "Moderate", "interferon_signature": "Moderate"},
            "GG": {"sle_risk": "Normal", "interferon_signature": "Normal"}
        },
        "population_frequency": {"EUR": 0.45, "AFR": 0.50, "EAS": 0.35}
    },
    # PTPN22 - also RA risk
    "rs2476601": {
        "gene": "PTPN22",
        "chromosome": "1",
        "function": "Protein tyrosine phosphatase (R620W)",
        "risk_allele": "A",
        "odds_ratio": 1.60,
        "effect": {
            "AA": {"autoimmune_risk": "Very High", "sle_risk": "High", "ra_risk": "High"},
            "GA": {"autoimmune_risk": "Elevated", "sle_risk": "Moderate", "ra_risk": "Moderate"},
            "GG": {"autoimmune_risk": "Normal", "sle_risk": "Normal", "ra_risk": "Normal"}
        },
        "population_frequency": {"EUR": 0.10, "AFR": 0.02, "EAS": 0.01}
    },
    # ITGAM - complement receptor
    "rs1143679": {
        "gene": "ITGAM",
        "chromosome": "16",
        "function": "Complement receptor 3 alpha (R77H)",
        "risk_allele": "A",
        "effect": {
            "AA": {"complement_function": "Altered", "sle_risk": "High"},
            "GA": {"complement_function": "Slightly Altered", "sle_risk": "Moderate"},
            "GG": {"complement_function": "Normal", "sle_risk": "Normal"}
        },
        "population_frequency": {"EUR": 0.12, "AFR": 0.35, "EAS": 0.20}
    }
}

# =============================================================================
# MULTIPLE SCLEROSIS GENETICS
# =============================================================================

MS_GENETICS = {
    # HLA-DRB1*15:01 - strongest MS risk
    "rs3135388": {
        "gene": "HLA-DRB1*15:01 tag",
        "chromosome": "6",
        "function": "Tags HLA-DRB1*15:01 haplotype",
        "risk_allele": "A",
        "odds_ratio": 3.10,
        "effect": {
            "AA": {"ms_risk": "Very High", "hla_drb1_1501": True},
            "GA": {"ms_risk": "High", "hla_drb1_1501": "Likely"},
            "GG": {"ms_risk": "Normal", "hla_drb1_1501": False}
        },
        "population_frequency": {"EUR": 0.17, "AFR": 0.08, "EAS": 0.05}
    },
    # IL7R
    "rs6897932": {
        "gene": "IL7R",
        "chromosome": "5",
        "function": "Interleukin-7 receptor alpha",
        "risk_allele": "C",
        "effect": {
            "CC": {"il7r_function": "Altered", "ms_modifier": "Risk Increased"},
            "CT": {"il7r_function": "Normal", "ms_modifier": "Slight Risk"},
            "TT": {"il7r_function": "Normal", "ms_modifier": "Normal"}
        },
        "population_frequency": {"EUR": 0.75, "AFR": 0.85, "EAS": 0.90}
    },
    # IL2RA - CD25
    "rs2104286": {
        "gene": "IL2RA",
        "chromosome": "10",
        "function": "IL-2 receptor alpha (CD25)",
        "risk_allele": "A",
        "effect": {
            "AA": {"treg_function": "Possibly Altered", "ms_risk": "Elevated"},
            "AG": {"treg_function": "Normal", "ms_risk": "Slightly Elevated"},
            "GG": {"treg_function": "Normal", "ms_risk": "Normal"}
        },
        "population_frequency": {"EUR": 0.25, "AFR": 0.20, "EAS": 0.15}
    },
    # CD58
    "rs2300747": {
        "gene": "CD58",
        "chromosome": "1",
        "function": "Lymphocyte function antigen 3",
        "effect": {
            "AA": {"cd58_expression": "Lower", "ms_risk": "Elevated"},
            "AG": {"cd58_expression": "Normal", "ms_risk": "Normal"},
            "GG": {"cd58_expression": "Normal", "ms_risk": "Normal"}
        },
        "population_frequency": {"EUR": 0.20, "AFR": 0.15, "EAS": 0.10}
    }
}

# =============================================================================
# RHEUMATOID ARTHRITIS GENETICS
# =============================================================================

RA_GENETICS = {
    # PTPN22 - covered in LUPUS_GENETICS
    # TRAF1/C5
    "rs3761847": {
        "gene": "TRAF1/C5",
        "chromosome": "9",
        "function": "TNF receptor-associated factor 1",
        "risk_allele": "G",
        "effect": {
            "GG": {"ra_risk": "Elevated", "complement_activation": "Increased"},
            "AG": {"ra_risk": "Moderate", "complement_activation": "Normal"},
            "AA": {"ra_risk": "Normal", "complement_activation": "Normal"}
        },
        "population_frequency": {"EUR": 0.42, "AFR": 0.30, "EAS": 0.25}
    },
    # CCR6
    "rs3093024": {
        "gene": "CCR6",
        "chromosome": "6",
        "function": "C-C chemokine receptor type 6",
        "risk_allele": "A",
        "effect": {
            "AA": {"th17_migration": "Enhanced", "ra_risk": "Elevated"},
            "GA": {"th17_migration": "Normal", "ra_risk": "Slightly Elevated"},
            "GG": {"th17_migration": "Normal", "ra_risk": "Normal"}
        },
        "population_frequency": {"EUR": 0.52, "AFR": 0.60, "EAS": 0.45}
    },
    # CTLA4
    "rs3087243": {
        "gene": "CTLA4",
        "chromosome": "2",
        "function": "Cytotoxic T-lymphocyte antigen 4",
        "risk_allele": "G",
        "effect": {
            "GG": {"t_cell_regulation": "Altered", "autoimmune_risk": "Elevated"},
            "AG": {"t_cell_regulation": "Normal", "autoimmune_risk": "Slightly Elevated"},
            "AA": {"t_cell_regulation": "Normal", "autoimmune_risk": "Normal"}
        },
        "population_frequency": {"EUR": 0.45, "AFR": 0.55, "EAS": 0.65}
    }
}

# =============================================================================
# PSORIASIS GENETICS
# =============================================================================

PSORIASIS_GENETICS = {
    # HLA-C*06:02 - major psoriasis risk
    "rs10484554": {
        "gene": "HLA-C*06:02 tag",
        "chromosome": "6",
        "function": "Tags HLA-C*06:02 psoriasis haplotype",
        "risk_allele": "T",
        "odds_ratio": 4.0,
        "effect": {
            "TT": {"psoriasis_risk": "Very High", "hla_c0602": True, "early_onset_risk": "High"},
            "CT": {"psoriasis_risk": "High", "hla_c0602": "Likely", "early_onset_risk": "Elevated"},
            "CC": {"psoriasis_risk": "Normal", "hla_c0602": False, "early_onset_risk": "Normal"}
        },
        "population_frequency": {"EUR": 0.10, "AFR": 0.05, "EAS": 0.03}
    },
    # IL12B
    "rs3212227": {
        "gene": "IL12B",
        "chromosome": "5",
        "function": "Interleukin-12 subunit beta",
        "risk_allele": "A",
        "effect": {
            "AA": {"il12_production": "Higher", "psoriasis_modifier": "Risk Increased"},
            "AC": {"il12_production": "Normal", "psoriasis_modifier": "Slight Risk"},
            "CC": {"il12_production": "Normal", "psoriasis_modifier": "Normal"}
        },
        "population_frequency": {"EUR": 0.22, "AFR": 0.45, "EAS": 0.55}
    },
    # IL23R - protective variant
    "rs11209026": {
        "gene": "IL23R",
        "chromosome": "1",
        "function": "Interleukin-23 receptor (R381Q)",
        "protective_allele": "A",
        "effect": {
            "AA": {"psoriasis_risk": "Reduced", "il23_signaling": "Reduced", "ibd_protection": True},
            "GA": {"psoriasis_risk": "Slightly Reduced", "il23_signaling": "Slightly Reduced"},
            "GG": {"psoriasis_risk": "Normal", "il23_signaling": "Normal", "ibd_protection": False}
        },
        "population_frequency": {"EUR": 0.07, "AFR": 0.02, "EAS": 0.01}
    },
    # TNFAIP3 (A20)
    "rs610604": {
        "gene": "TNFAIP3",
        "chromosome": "6",
        "function": "TNF-induced protein 3 (A20)",
        "risk_allele": "G",
        "effect": {
            "GG": {"nfkb_regulation": "Impaired", "psoriasis_risk": "Elevated"},
            "GT": {"nfkb_regulation": "Normal", "psoriasis_risk": "Slightly Elevated"},
            "TT": {"nfkb_regulation": "Normal", "psoriasis_risk": "Normal"}
        },
        "population_frequency": {"EUR": 0.30, "AFR": 0.25, "EAS": 0.20}
    }
}

# =============================================================================
# IBD / CROHN'S DISEASE GENETICS
# =============================================================================

IBD_GENETICS = {
    # NOD2 - major Crohn's gene
    "rs2066844": {
        "gene": "NOD2",
        "chromosome": "16",
        "function": "NOD2 R702W variant",
        "risk_allele": "T",
        "odds_ratio": 2.4,
        "effect": {
            "TT": {"crohn_risk": "High", "nod2_function": "Impaired", "bacterial_sensing": "Reduced"},
            "CT": {"crohn_risk": "Elevated", "nod2_function": "Partially Impaired", "bacterial_sensing": "Reduced"},
            "CC": {"crohn_risk": "Normal", "nod2_function": "Normal", "bacterial_sensing": "Normal"}
        },
        "population_frequency": {"EUR": 0.05, "AFR": 0.01, "EAS": 0.001}
    },
    "rs2066845": {
        "gene": "NOD2",
        "chromosome": "16",
        "function": "NOD2 G908R variant",
        "risk_allele": "C",
        "odds_ratio": 2.8,
        "effect": {
            "CC": {"crohn_risk": "High", "nod2_function": "Impaired"},
            "GC": {"crohn_risk": "Elevated", "nod2_function": "Reduced"},
            "GG": {"crohn_risk": "Normal", "nod2_function": "Normal"}
        },
        "population_frequency": {"EUR": 0.02, "AFR": 0.001, "EAS": 0.001}
    },
    "rs2066847": {
        "gene": "NOD2",
        "chromosome": "16",
        "function": "NOD2 1007fs frameshift",
        "risk_allele": "C",
        "odds_ratio": 4.1,
        "effect": {
            "insC": {"crohn_risk": "Very High", "nod2_function": "Lost"},
            "het": {"crohn_risk": "High", "nod2_function": "Impaired"},
            "wt": {"crohn_risk": "Normal", "nod2_function": "Normal"}
        },
        "population_frequency": {"EUR": 0.03, "AFR": 0.001, "EAS": 0.001}
    },
    # ATG16L1 - autophagy
    "rs2241880": {
        "gene": "ATG16L1",
        "chromosome": "2",
        "function": "Autophagy-related 16-like 1 (T300A)",
        "risk_allele": "G",
        "effect": {
            "GG": {"autophagy": "Impaired", "crohn_risk": "Elevated", "pathogen_clearance": "Reduced"},
            "AG": {"autophagy": "Slightly Impaired", "crohn_risk": "Slightly Elevated"},
            "AA": {"autophagy": "Normal", "crohn_risk": "Normal", "pathogen_clearance": "Normal"}
        },
        "population_frequency": {"EUR": 0.55, "AFR": 0.40, "EAS": 0.80}
    },
    # IL23R protective (same as psoriasis)
    # IRGM - autophagy
    "rs13361189": {
        "gene": "IRGM",
        "chromosome": "5",
        "function": "Immunity-related GTPase M",
        "risk_allele": "C",
        "effect": {
            "CC": {"autophagy": "Impaired", "crohn_risk": "Elevated"},
            "CT": {"autophagy": "Slightly Impaired", "crohn_risk": "Moderate"},
            "TT": {"autophagy": "Normal", "crohn_risk": "Normal"}
        },
        "population_frequency": {"EUR": 0.10, "AFR": 0.05, "EAS": 0.02}
    }
}


# =============================================================================
# MAIN ANALYSIS FUNCTION
# =============================================================================

def analyze_immune_deep_genetics(dna_data: dict) -> Dict[str, Any]:
    """
    Perform comprehensive immune system genetic analysis.

    Args:
        dna_data: Dictionary of rsid -> genotype

    Returns:
        Dictionary containing all immune deep dive analysis results
    """
    results = {
        "hla_analysis": analyze_hla_types(dna_data),
        "cytokine_response": analyze_cytokine_genetics(dna_data),
        "inflammatory_markers": analyze_inflammatory_genetics(dna_data),
        "allergy_susceptibility": analyze_allergy_genetics(dna_data),
        "celiac_risk": analyze_celiac_genetics(dna_data),
        "lupus_risk": analyze_lupus_genetics(dna_data),
        "ms_risk": analyze_ms_genetics(dna_data),
        "ra_risk": analyze_ra_genetics(dna_data),
        "psoriasis_risk": analyze_psoriasis_genetics(dna_data),
        "ibd_risk": analyze_ibd_genetics(dna_data),
        "summary": {}
    }

    # Generate overall summary
    results["summary"] = generate_immune_summary(results)

    return results


def analyze_hla_types(dna_data: dict) -> Dict[str, Any]:
    """Analyze HLA type markers"""
    result = {
        "snps_analyzed": [],
        "hla_b27_status": "Unknown",
        "hla_dq2_status": "Unknown",
        "hla_dq8_status": "Unknown",
        "autoimmune_hla_risk": "Unknown",
        "findings": []
    }

    for rsid, info in HLA_GENETICS.items():
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

                # HLA-B27
                if "hla_b27_likely" in effect:
                    if effect["hla_b27_likely"] == True:
                        result["hla_b27_status"] = "Positive (likely)"
                        result["findings"].append(f"HLA-B27 positive - 40x increased ankylosing spondylitis risk")
                    elif effect["hla_b27_likely"] == False:
                        result["hla_b27_status"] = "Negative (likely)"

                # HLA-DQ2
                if "hla_dq2_positive" in effect:
                    if effect["hla_dq2_positive"] == True:
                        result["hla_dq2_status"] = "Positive"
                        result["findings"].append("HLA-DQ2 positive - celiac disease susceptibility")
                    elif effect["hla_dq2_positive"] == "Possible":
                        result["hla_dq2_status"] = "Possibly Positive"
                    else:
                        result["hla_dq2_status"] = "Negative"

                # HLA-DQ8
                if "hla_dq8_positive" in effect:
                    if effect["hla_dq8_positive"] == True:
                        result["hla_dq8_status"] = "Positive"
                        result["findings"].append("HLA-DQ8 positive - celiac and T1D risk")
                    elif effect["hla_dq8_positive"] == "Possible":
                        result["hla_dq8_status"] = "Possibly Positive"
                    else:
                        result["hla_dq8_status"] = "Negative"

    # Determine overall HLA autoimmune risk
    high_risk = any("High" in f or "Very High" in f for f in result["findings"])
    result["autoimmune_hla_risk"] = "Elevated" if high_risk else "Normal" if result["snps_analyzed"] else "Unknown"

    return result


def analyze_cytokine_genetics(dna_data: dict) -> Dict[str, Any]:
    """Analyze cytokine response genetics"""
    result = {
        "snps_analyzed": [],
        "il6_response": "Unknown",
        "tnf_response": "Unknown",
        "il10_level": "Unknown",
        "ifng_response": "Unknown",
        "overall_inflammatory_tendency": "Unknown",
        "findings": []
    }

    inflammatory_score = 0
    snps_found = 0

    for rsid, info in CYTOKINE_GENETICS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            effects = info.get("effect", {})
            snps_found += 1

            result["snps_analyzed"].append({
                "rsid": rsid,
                "gene": info.get("gene", ""),
                "genotype": genotype,
                "common_name": info.get("common_name", "")
            })

            _key = get_genotype_key(genotype, effects)
            if _key:

                effect = effects[_key]

                # IL-6
                if info.get("gene") == "IL6":
                    result["il6_response"] = effect.get("il6_production", "Unknown")
                    if "Higher" in effect.get("il6_production", ""):
                        inflammatory_score += 2
                        result["findings"].append("Higher IL-6 production - pro-inflammatory tendency")
                    elif "Moderate" in effect.get("il6_production", ""):
                        inflammatory_score += 1

                # TNF-alpha
                if info.get("gene") == "TNF":
                    result["tnf_response"] = effect.get("tnf_production", "Unknown")
                    if "Very High" in effect.get("tnf_production", ""):
                        inflammatory_score += 3
                        result["findings"].append("High TNF-alpha production - strong inflammatory response")
                    elif "High" in effect.get("tnf_production", ""):
                        inflammatory_score += 2

                # IL-10 (anti-inflammatory)
                if info.get("gene") == "IL10":
                    result["il10_level"] = effect.get("il10_production", "Unknown")
                    if "Low" in effect.get("il10_production", ""):
                        inflammatory_score += 1
                        result["findings"].append("Lower IL-10 - reduced anti-inflammatory capacity")
                    elif "High" in effect.get("il10_production", ""):
                        inflammatory_score -= 1

                # IFN-gamma
                if info.get("gene") == "IFNG":
                    result["ifng_response"] = effect.get("ifng_production", "Unknown")

    # Determine overall tendency
    if snps_found > 0:
        if inflammatory_score >= 4:
            result["overall_inflammatory_tendency"] = "High"
        elif inflammatory_score >= 2:
            result["overall_inflammatory_tendency"] = "Moderately Elevated"
        elif inflammatory_score <= -1:
            result["overall_inflammatory_tendency"] = "Lower than average"
        else:
            result["overall_inflammatory_tendency"] = "Normal"

    return result


def analyze_inflammatory_genetics(dna_data: dict) -> Dict[str, Any]:
    """Analyze baseline inflammatory markers"""
    result = {
        "snps_analyzed": [],
        "baseline_crp": "Unknown",
        "nfkb_activity": "Unknown",
        "findings": []
    }

    for rsid, info in INFLAMMATORY_GENETICS.items():
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

                if info.get("gene") == "CRP":
                    if "Elevated" in str(effect.get("baseline_crp", "")):
                        result["baseline_crp"] = "Elevated"
                        result["findings"].append("Genetic tendency for elevated baseline CRP levels")
                    elif "Lower" in str(effect.get("crp_level", "")):
                        result["baseline_crp"] = "Lower"

                if info.get("gene") == "NFKB1":
                    result["nfkb_activity"] = effect.get("nfkb_activity", "Unknown")

    if not result["baseline_crp"] or result["baseline_crp"] == "Unknown":
        result["baseline_crp"] = "Normal" if result["snps_analyzed"] else "Unknown"

    return result


def analyze_allergy_genetics(dna_data: dict) -> Dict[str, Any]:
    """Analyze allergy susceptibility genetics"""
    result = {
        "snps_analyzed": [],
        "ige_tendency": "Unknown",
        "skin_barrier": "Unknown",
        "histamine_sensitivity": "Unknown",
        "overall_allergy_risk": "Unknown",
        "risk_score": 0,
        "findings": []
    }

    risk_count = 0
    snps_found = 0

    for rsid, info in ALLERGY_GENETICS.items():
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

                # IgE levels
                if "ige_levels" in effect:
                    if effect["ige_levels"] == "High":
                        result["ige_tendency"] = "High"
                        risk_count += 2
                        result["findings"].append("High IgE tendency - increased allergy susceptibility")
                    elif effect["ige_levels"] == "Moderate":
                        result["ige_tendency"] = "Moderate"
                        risk_count += 1

                # Skin barrier
                if "skin_barrier" in effect:
                    result["skin_barrier"] = effect["skin_barrier"]
                    if "Impaired" in effect["skin_barrier"]:
                        risk_count += 2
                        result["findings"].append("Impaired skin barrier (FLG) - eczema and food allergy risk")

                # Histamine
                if "histamine_sensitivity" in effect:
                    result["histamine_sensitivity"] = effect["histamine_sensitivity"]
                    if effect["histamine_sensitivity"] == "High":
                        risk_count += 1
                        result["findings"].append("High histamine sensitivity - may react strongly to histamine")

    result["risk_score"] = risk_count

    if snps_found > 0:
        if risk_count >= 4:
            result["overall_allergy_risk"] = "High"
        elif risk_count >= 2:
            result["overall_allergy_risk"] = "Elevated"
        else:
            result["overall_allergy_risk"] = "Normal"

    return result


def analyze_celiac_genetics(dna_data: dict) -> Dict[str, Any]:
    """Analyze celiac disease genetic risk"""
    result = {
        "snps_analyzed": [],
        "hla_risk": "Unknown",
        "non_hla_modifiers": [],
        "overall_risk": "Unknown",
        "can_develop_celiac": True,
        "findings": []
    }

    hla_positive = False
    risk_modifiers = 0

    # Check HLA markers
    for rsid, info in HLA_GENETICS.items():
        if rsid in dna_data and ("DQ2" in info.get("gene", "") or "DQ8" in info.get("gene", "")):
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
                if effect.get("hla_dq2_positive") == True or effect.get("hla_dq8_positive") == True:
                    hla_positive = True
                    result["hla_risk"] = "Positive"
                    result["findings"].append(f"HLA-DQ2/DQ8 positive - can develop celiac disease")

    # Check non-HLA modifiers
    for rsid, info in CELIAC_GENETICS.items():
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
                if "Increased" in str(effect.get("celiac_risk_modifier", "")):
                    risk_modifiers += 1
                    result["non_hla_modifiers"].append(info.get("gene", rsid))

    if not hla_positive and result["snps_analyzed"]:
        result["hla_risk"] = "Negative"
        result["can_develop_celiac"] = False
        result["findings"].append("HLA-DQ2/DQ8 negative - very unlikely to develop celiac disease")
        result["overall_risk"] = "Very Low"
    elif hla_positive:
        if risk_modifiers >= 2:
            result["overall_risk"] = "High"
        elif risk_modifiers >= 1:
            result["overall_risk"] = "Moderate"
        else:
            result["overall_risk"] = "Possible (HLA positive)"

    return result


def analyze_lupus_genetics(dna_data: dict) -> Dict[str, Any]:
    """Analyze systemic lupus erythematosus (SLE) genetic risk"""
    result = {
        "snps_analyzed": [],
        "risk_variants_found": 0,
        "risk_score": 0,
        "risk_level": "Unknown",
        "key_genes": [],
        "findings": []
    }

    for rsid, info in LUPUS_GENETICS.items():
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
                risk_score = effect.get("risk_score", 0)
                result["risk_score"] += risk_score

                if effect.get("sle_risk") in ["High", "Elevated"]:
                    result["risk_variants_found"] += 1
                    result["key_genes"].append(info.get("gene", ""))
                    result["findings"].append(f"{info.get('gene', rsid)}: {effect.get('sle_risk')} SLE risk")

    if result["snps_analyzed"]:
        if result["risk_score"] >= 4:
            result["risk_level"] = "High"
        elif result["risk_score"] >= 2:
            result["risk_level"] = "Elevated"
        else:
            result["risk_level"] = "Normal"

    return result


def analyze_ms_genetics(dna_data: dict) -> Dict[str, Any]:
    """Analyze multiple sclerosis genetic risk"""
    result = {
        "snps_analyzed": [],
        "hla_drb1_1501": "Unknown",
        "risk_variants_found": 0,
        "risk_level": "Unknown",
        "findings": []
    }

    risk_count = 0

    for rsid, info in MS_GENETICS.items():
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

                # HLA-DRB1*15:01
                if "hla_drb1_1501" in effect:
                    if effect["hla_drb1_1501"] == True:
                        result["hla_drb1_1501"] = "Positive"
                        risk_count += 3
                        result["findings"].append("HLA-DRB1*15:01 positive - major MS risk factor (3x)")
                    elif effect["hla_drb1_1501"] == "Likely":
                        result["hla_drb1_1501"] = "Likely Positive"
                        risk_count += 2
                    else:
                        result["hla_drb1_1501"] = "Negative"

                if effect.get("ms_risk") in ["Elevated", "High", "Very High"]:
                    result["risk_variants_found"] += 1
                    risk_count += 1

    if result["snps_analyzed"]:
        if risk_count >= 4:
            result["risk_level"] = "High"
        elif risk_count >= 2:
            result["risk_level"] = "Elevated"
        else:
            result["risk_level"] = "Normal"

    return result


def analyze_ra_genetics(dna_data: dict) -> Dict[str, Any]:
    """Analyze rheumatoid arthritis genetic risk"""
    result = {
        "snps_analyzed": [],
        "shared_epitope": "Unknown",
        "risk_variants_found": 0,
        "risk_level": "Unknown",
        "findings": []
    }

    risk_count = 0

    # Check HLA shared epitope
    for rsid, info in HLA_GENETICS.items():
        if rsid in dna_data and "DRB1" in info.get("gene", ""):
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
                if effect.get("shared_epitope_likely") == True:
                    result["shared_epitope"] = "Likely Present"
                    risk_count += 2
                    result["findings"].append("HLA shared epitope likely - increased RA risk")

    # Check other RA genes
    for rsid, info in RA_GENETICS.items():
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
                if effect.get("ra_risk") == "Elevated":
                    result["risk_variants_found"] += 1
                    risk_count += 1

    # Also check PTPN22 from lupus genetics
    if "rs2476601" in dna_data:
        genotype = dna_data["rs2476601"]
        if genotype in ["AA", "GA"]:
            risk_count += 1
            result["findings"].append("PTPN22 risk variant - increased autoimmune/RA risk")

    if result["snps_analyzed"]:
        if risk_count >= 4:
            result["risk_level"] = "High"
        elif risk_count >= 2:
            result["risk_level"] = "Elevated"
        else:
            result["risk_level"] = "Normal"

    return result


def analyze_psoriasis_genetics(dna_data: dict) -> Dict[str, Any]:
    """Analyze psoriasis genetic risk"""
    result = {
        "snps_analyzed": [],
        "hla_c0602": "Unknown",
        "risk_variants_found": 0,
        "protective_variants": 0,
        "risk_level": "Unknown",
        "early_onset_risk": "Unknown",
        "findings": []
    }

    risk_score = 0

    for rsid, info in PSORIASIS_GENETICS.items():
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

                # HLA-C*06:02
                if "hla_c0602" in effect:
                    if effect["hla_c0602"] == True:
                        result["hla_c0602"] = "Positive"
                        risk_score += 3
                        result["findings"].append("HLA-C*06:02 positive - major psoriasis risk (4x)")
                    elif effect["hla_c0602"] == "Likely":
                        result["hla_c0602"] = "Likely Positive"
                        risk_score += 2
                    else:
                        result["hla_c0602"] = "Negative"

                result["early_onset_risk"] = effect.get("early_onset_risk", result["early_onset_risk"])

                # Protective IL23R variant
                if info.get("gene") == "IL23R" and effect.get("psoriasis_risk") == "Reduced":
                    result["protective_variants"] += 1
                    risk_score -= 1
                    result["findings"].append("IL23R protective variant - reduced psoriasis and IBD risk")

                if "Risk Increased" in str(effect.get("psoriasis_modifier", "")):
                    result["risk_variants_found"] += 1
                    risk_score += 1

    if result["snps_analyzed"]:
        if risk_score >= 4:
            result["risk_level"] = "High"
        elif risk_score >= 2:
            result["risk_level"] = "Elevated"
        elif risk_score <= 0:
            result["risk_level"] = "Lower than average"
        else:
            result["risk_level"] = "Normal"

    return result


def analyze_ibd_genetics(dna_data: dict) -> Dict[str, Any]:
    """Analyze IBD/Crohn's disease genetic risk"""
    result = {
        "snps_analyzed": [],
        "nod2_status": "Normal",
        "nod2_variants": 0,
        "autophagy_genes": [],
        "risk_variants_found": 0,
        "risk_level": "Unknown",
        "crohn_vs_uc": "Unknown",
        "findings": []
    }

    risk_score = 0
    nod2_count = 0

    for rsid, info in IBD_GENETICS.items():
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

                # NOD2 variants
                if info.get("gene") == "NOD2":
                    if effect.get("crohn_risk") in ["High", "Very High", "Elevated"]:
                        nod2_count += 1
                        risk_score += 2
                        result["findings"].append(f"NOD2 variant ({info.get('function', rsid)}) - Crohn's risk")

                # Autophagy genes
                if info.get("gene") in ["ATG16L1", "IRGM"]:
                    if "Impaired" in str(effect.get("autophagy", "")):
                        result["autophagy_genes"].append(info.get("gene"))
                        risk_score += 1
                        result["findings"].append(f"{info.get('gene')} - impaired autophagy, Crohn's risk")

    result["nod2_variants"] = nod2_count
    if nod2_count >= 2:
        result["nod2_status"] = "Compound Heterozygote - High Risk"
        result["crohn_vs_uc"] = "Crohn's Disease more likely"
    elif nod2_count == 1:
        result["nod2_status"] = "Single Variant - Elevated Risk"
        result["crohn_vs_uc"] = "Crohn's Disease more likely"

    result["risk_variants_found"] = nod2_count + len(result["autophagy_genes"])

    if result["snps_analyzed"]:
        if risk_score >= 5:
            result["risk_level"] = "High"
        elif risk_score >= 3:
            result["risk_level"] = "Elevated"
        elif risk_score >= 1:
            result["risk_level"] = "Slightly Elevated"
        else:
            result["risk_level"] = "Normal"

    return result


def generate_immune_summary(results: Dict[str, Any]) -> Dict[str, Any]:
    """Generate overall immune system summary"""
    summary = {
        "autoimmune_risk_level": "Unknown",
        "highest_risk_conditions": [],
        "inflammatory_profile": "Unknown",
        "key_findings": [],
        "recommendations": []
    }

    # Collect risk levels
    risk_conditions = []

    conditions = [
        ("Celiac Disease", results.get("celiac_risk", {}).get("overall_risk", "Unknown")),
        ("Lupus (SLE)", results.get("lupus_risk", {}).get("risk_level", "Unknown")),
        ("Multiple Sclerosis", results.get("ms_risk", {}).get("risk_level", "Unknown")),
        ("Rheumatoid Arthritis", results.get("ra_risk", {}).get("risk_level", "Unknown")),
        ("Psoriasis", results.get("psoriasis_risk", {}).get("risk_level", "Unknown")),
        ("Crohn's/IBD", results.get("ibd_risk", {}).get("risk_level", "Unknown"))
    ]

    for condition, risk in conditions:
        if risk in ["High", "Very High", "Elevated"]:
            risk_conditions.append({"condition": condition, "risk": risk})

    summary["highest_risk_conditions"] = sorted(
        risk_conditions,
        key=lambda x: 2 if x["risk"] in ["High", "Very High"] else 1,
        reverse=True
    )[:3]

    # Inflammatory profile
    cytokine = results.get("cytokine_response", {})
    summary["inflammatory_profile"] = cytokine.get("overall_inflammatory_tendency", "Unknown")

    # Overall autoimmune risk
    if len(risk_conditions) >= 3:
        summary["autoimmune_risk_level"] = "High"
    elif len(risk_conditions) >= 1:
        summary["autoimmune_risk_level"] = "Elevated"
    else:
        summary["autoimmune_risk_level"] = "Normal"

    # Compile key findings
    for key in ["hla_analysis", "cytokine_response", "allergy_susceptibility",
                "celiac_risk", "lupus_risk", "ms_risk", "ibd_risk"]:
        findings = results.get(key, {}).get("findings", [])
        summary["key_findings"].extend(findings[:2])

    # Generate recommendations
    if summary["autoimmune_risk_level"] in ["High", "Elevated"]:
        summary["recommendations"].append("Consider discussing autoimmune risk factors with a rheumatologist")

    if results.get("celiac_risk", {}).get("can_develop_celiac") == True:
        summary["recommendations"].append("Monitor for celiac symptoms; consider testing if digestive issues arise")

    if results.get("allergy_susceptibility", {}).get("overall_allergy_risk") in ["High", "Elevated"]:
        summary["recommendations"].append("May benefit from allergy testing and management strategies")

    if summary["inflammatory_profile"] in ["High", "Moderately Elevated"]:
        summary["recommendations"].append("Anti-inflammatory diet and lifestyle may be beneficial")

    return summary
