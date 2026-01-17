"""
Pharmacogenomics Database - Detailed Drug Metabolism Genetics
Real SNPs from PharmGKB, CPIC guidelines, and clinical pharmacogenomics research
50+ medications with genetic dosing recommendations
"""

from typing import Dict, Any, List

# =============================================================================
# CYP2D6 METABOLISM (Codeine, Tramadol, SSRIs, Beta-blockers, etc.)
# =============================================================================

CYP2D6_GENETICS = {
    "rs3892097": {
        "gene": "CYP2D6",
        "chromosome": "22",
        "variant": "*4",
        "variant_name": "Splice defect",
        "function": "CYP2D6*4 - most common non-functional allele",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GA": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "AA": {"activity": "none", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["codeine", "tramadol", "oxycodone", "hydrocodone", "tamoxifen",
                          "fluoxetine", "paroxetine", "venlafaxine", "metoprolol", "carvedilol"]
    },
    "rs5030655": {
        "gene": "CYP2D6",
        "chromosome": "22",
        "variant": "*6",
        "variant_name": "T1707del",
        "function": "CYP2D6*6 - frameshift deletion",
        "effect": {
            "AA": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "AT": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "TT": {"activity": "none", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["codeine", "tramadol", "tamoxifen", "SSRIs", "beta-blockers"]
    },
    "rs16947": {
        "gene": "CYP2D6",
        "chromosome": "22",
        "variant": "*2",
        "variant_name": "R296C",
        "function": "CYP2D6*2 - fully functional variant",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CT": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "TT": {"activity": "normal", "phenotype": "Normal Metabolizer"}
        },
        "affected_drugs": ["codeine", "tramadol", "tamoxifen"]
    },
    "rs1065852": {
        "gene": "CYP2D6",
        "chromosome": "22",
        "variant": "*10",
        "variant_name": "P34S",
        "function": "CYP2D6*10 - reduced function (common in Asians)",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CT": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "TT": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"}
        },
        "affected_drugs": ["codeine", "tamoxifen", "risperidone", "haloperidol"]
    },
    "rs28371706": {
        "gene": "CYP2D6",
        "chromosome": "22",
        "variant": "*17",
        "variant_name": "T107I",
        "function": "CYP2D6*17 - reduced function (common in Africans)",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CT": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "TT": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"}
        },
        "affected_drugs": ["codeine", "tamoxifen", "risperidone", "SSRIs"]
    },
    "rs28371725": {
        "gene": "CYP2D6",
        "chromosome": "22",
        "variant": "*41",
        "variant_name": "Splice defect",
        "function": "CYP2D6*41 - decreased function",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CT": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "TT": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"}
        },
        "affected_drugs": ["codeine", "tamoxifen", "tramadol", "antidepressants"]
    },
    "rs5030656": {
        "gene": "CYP2D6",
        "chromosome": "22",
        "variant": "*9",
        "variant_name": "K281del",
        "function": "CYP2D6*9 - decreased function",
        "effect": {
            "AA": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "AT": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "TT": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"}
        },
        "affected_drugs": ["codeine", "tramadol", "tamoxifen"]
    },
    "rs5030862": {
        "gene": "CYP2D6",
        "chromosome": "22",
        "variant": "*3",
        "variant_name": "A259fs",
        "function": "CYP2D6*3 - non-functional frameshift",
        "effect": {
            "AA": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "AG": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "GG": {"activity": "none", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["codeine", "tramadol", "tamoxifen", "SSRIs"]
    },
    "rs28371703": {
        "gene": "CYP2D6",
        "chromosome": "22",
        "variant": "*7",
        "variant_name": "H324P",
        "function": "CYP2D6*7 - non-functional",
        "effect": {
            "AA": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "AC": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "CC": {"activity": "none", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["codeine", "tramadol", "tamoxifen"]
    },
    "rs5030867": {
        "gene": "CYP2D6",
        "chromosome": "22",
        "variant": "*8",
        "variant_name": "G169X",
        "function": "CYP2D6*8 - stop codon, non-functional",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GT": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "TT": {"activity": "none", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["codeine", "tramadol", "tamoxifen"]
    },
    "rs5030865": {
        "gene": "CYP2D6",
        "chromosome": "22",
        "variant": "*11",
        "variant_name": "Splice",
        "function": "CYP2D6*11 - non-functional splice variant",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GC": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "CC": {"activity": "none", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["codeine", "tramadol"]
    },
    "rs1135840": {
        "gene": "CYP2D6",
        "chromosome": "22",
        "variant": "*2/*35",
        "variant_name": "S486T",
        "function": "CYP2D6 - functional variant marker",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"}
        },
        "affected_drugs": ["codeine", "tramadol", "tamoxifen"]
    },
    "rs28371704": {
        "gene": "CYP2D6",
        "chromosome": "22",
        "variant": "*12",
        "variant_name": "G212E",
        "function": "CYP2D6*12 - non-functional",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GA": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "AA": {"activity": "none", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["codeine", "tramadol"]
    },
    "rs72549353": {
        "gene": "CYP2D6",
        "chromosome": "22",
        "variant": "*14",
        "variant_name": "P34S+G169R",
        "function": "CYP2D6*14 - non-functional",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GA": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "AA": {"activity": "none", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["codeine", "tamoxifen"]
    },
    "rs59421388": {
        "gene": "CYP2D6",
        "chromosome": "22",
        "variant": "*29",
        "variant_name": "V136I",
        "function": "CYP2D6*29 - decreased function (African)",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GA": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "AA": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"}
        },
        "affected_drugs": ["codeine", "tramadol", "tamoxifen"]
    },
    "rs769258": {
        "gene": "CYP2D6",
        "chromosome": "22",
        "variant": "*35",
        "variant_name": "V11M",
        "function": "CYP2D6*35 - normal function variant",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GA": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "AA": {"activity": "normal", "phenotype": "Normal Metabolizer"}
        },
        "affected_drugs": ["codeine", "tramadol"]
    },
    "rs1080985": {
        "gene": "CYP2D6",
        "chromosome": "22",
        "variant": "*2A",
        "variant_name": "-1584C>G",
        "function": "CYP2D6*2A promoter - gene duplication marker",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CG": {"activity": "increased", "phenotype": "May indicate gene duplication"},
            "GG": {"activity": "increased", "phenotype": "Possible Ultrarapid Metabolizer"}
        },
        "affected_drugs": ["codeine", "tramadol", "tamoxifen"]
    }
}

# =============================================================================
# CYP2C19 METABOLISM (Clopidogrel, PPIs, SSRIs, etc.)
# =============================================================================

CYP2C19_GENETICS = {
    "rs4244285": {
        "gene": "CYP2C19",
        "chromosome": "10",
        "variant": "*2",
        "variant_name": "Splice defect",
        "function": "CYP2C19*2 - loss of function",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GA": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "AA": {"activity": "none", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["clopidogrel", "omeprazole", "esomeprazole", "pantoprazole",
                          "citalopram", "escitalopram", "sertraline", "voriconazole"]
    },
    "rs4986893": {
        "gene": "CYP2C19",
        "chromosome": "10",
        "variant": "*3",
        "variant_name": "W212X",
        "function": "CYP2C19*3 - loss of function",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GA": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "AA": {"activity": "none", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["clopidogrel", "PPIs", "citalopram"]
    },
    "rs12248560": {
        "gene": "CYP2C19",
        "chromosome": "10",
        "variant": "*17",
        "variant_name": "-806C>T",
        "function": "CYP2C19*17 - ultrarapid metabolizer",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CT": {"activity": "increased", "phenotype": "Rapid Metabolizer"},
            "TT": {"activity": "very_increased", "phenotype": "Ultrarapid Metabolizer"}
        },
        "affected_drugs": ["clopidogrel", "citalopram", "escitalopram", "sertraline", "voriconazole"]
    },
    "rs28399504": {
        "gene": "CYP2C19",
        "chromosome": "10",
        "variant": "*4",
        "variant_name": "A1>G",
        "function": "CYP2C19*4 - loss of function (start codon)",
        "effect": {
            "AA": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "AG": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "GG": {"activity": "none", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["clopidogrel", "PPIs", "voriconazole"]
    },
    "rs56337013": {
        "gene": "CYP2C19",
        "chromosome": "10",
        "variant": "*5",
        "variant_name": "R433W",
        "function": "CYP2C19*5 - no function",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CT": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "TT": {"activity": "none", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["clopidogrel", "PPIs", "antidepressants"]
    },
    "rs72552267": {
        "gene": "CYP2C19",
        "chromosome": "10",
        "variant": "*6",
        "variant_name": "R132Q",
        "function": "CYP2C19*6 - no function",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GA": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "AA": {"activity": "none", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["clopidogrel", "PPIs"]
    },
    "rs72558186": {
        "gene": "CYP2C19",
        "chromosome": "10",
        "variant": "*8",
        "variant_name": "W120R",
        "function": "CYP2C19*8 - no function",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GA": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "AA": {"activity": "none", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["clopidogrel", "PPIs"]
    }
}

# =============================================================================
# CYP2C9 METABOLISM (Warfarin, NSAIDs, Sulfonylureas)
# =============================================================================

CYP2C9_GENETICS = {
    "rs1799853": {
        "gene": "CYP2C9",
        "chromosome": "10",
        "variant": "*2",
        "variant_name": "R144C",
        "function": "CYP2C9*2 - reduced function",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CT": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "TT": {"activity": "poor", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["warfarin", "phenytoin", "celecoxib", "flurbiprofen",
                          "glimepiride", "glipizide", "tolbutamide"]
    },
    "rs1057910": {
        "gene": "CYP2C9",
        "chromosome": "10",
        "variant": "*3",
        "variant_name": "I359L",
        "function": "CYP2C9*3 - reduced function (greater impact than *2)",
        "effect": {
            "AA": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "AC": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "CC": {"activity": "poor", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["warfarin", "phenytoin", "NSAIDs", "sulfonylureas"]
    },
    "rs28371686": {
        "gene": "CYP2C9",
        "chromosome": "10",
        "variant": "*5",
        "variant_name": "D360E",
        "function": "CYP2C9*5 - reduced function",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CG": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "GG": {"activity": "poor", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["warfarin", "phenytoin", "NSAIDs"]
    },
    "rs9332131": {
        "gene": "CYP2C9",
        "chromosome": "10",
        "variant": "*6",
        "variant_name": "818delA",
        "function": "CYP2C9*6 - no function (frameshift)",
        "effect": {
            "AA": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "AT": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "TT": {"activity": "none", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["warfarin", "phenytoin"]
    },
    "rs7900194": {
        "gene": "CYP2C9",
        "chromosome": "10",
        "variant": "*8",
        "variant_name": "R150H",
        "function": "CYP2C9*8 - decreased function (common in African Americans)",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GA": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "AA": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"}
        },
        "affected_drugs": ["warfarin", "phenytoin", "losartan"]
    },
    "rs28371685": {
        "gene": "CYP2C9",
        "chromosome": "10",
        "variant": "*11",
        "variant_name": "R335W",
        "function": "CYP2C9*11 - reduced function",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CT": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "TT": {"activity": "poor", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["warfarin", "phenytoin"]
    }
}

# =============================================================================
# WARFARIN SENSITIVITY (VKORC1)
# =============================================================================

VKORC1_GENETICS = {
    "rs9923231": {
        "gene": "VKORC1",
        "chromosome": "16",
        "variant_name": "-1639G>A",
        "function": "Vitamin K epoxide reductase - warfarin target",
        "effect": {
            "GG": {"sensitivity": "normal", "dose_adjustment": "Standard dose", "description": "Normal warfarin sensitivity"},
            "GA": {"sensitivity": "intermediate", "dose_adjustment": "20-40% dose reduction", "description": "Intermediate sensitivity"},
            "AA": {"sensitivity": "high", "dose_adjustment": "40-60% dose reduction", "description": "High sensitivity - low dose needed"}
        },
        "affected_drugs": ["warfarin", "acenocoumarol", "phenprocoumon"]
    },
    "rs8050894": {
        "gene": "VKORC1",
        "chromosome": "16",
        "variant_name": "1173C>T",
        "function": "VKORC1 additional variant - warfarin sensitivity",
        "effect": {
            "CC": {"sensitivity": "normal", "dose_adjustment": "Standard dose"},
            "CG": {"sensitivity": "intermediate", "dose_adjustment": "Moderate reduction"},
            "GG": {"sensitivity": "high", "dose_adjustment": "Significant reduction needed"}
        },
        "affected_drugs": ["warfarin", "acenocoumarol"]
    },
    "rs2359612": {
        "gene": "VKORC1",
        "chromosome": "16",
        "variant_name": "2255C>T",
        "function": "VKORC1 haplotype variant",
        "effect": {
            "CC": {"sensitivity": "normal", "dose_adjustment": "Standard dose"},
            "CT": {"sensitivity": "intermediate", "dose_adjustment": "Moderate reduction"},
            "TT": {"sensitivity": "high", "dose_adjustment": "Significant reduction"}
        },
        "affected_drugs": ["warfarin"]
    }
}

# =============================================================================
# UGT1A1 (Irinotecan, Atazanavir)
# =============================================================================

UGT1A1_GENETICS = {
    "rs8175347": {
        "gene": "UGT1A1",
        "chromosome": "2",
        "variant_name": "*28 (TA)7",
        "function": "UDP-glucuronosyltransferase - irinotecan metabolism",
        "effect": {
            "(TA)6/(TA)6": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "(TA)6/(TA)7": {"activity": "intermediate", "phenotype": "Intermediate Metabolizer"},
            "(TA)7/(TA)7": {"activity": "poor", "phenotype": "Poor Metabolizer - HIGH toxicity risk"}
        },
        "affected_drugs": ["irinotecan", "atazanavir", "belinostat"]
    },
    "rs4148323": {
        "gene": "UGT1A1",
        "chromosome": "2",
        "variant_name": "*6 (G71R)",
        "function": "UGT1A1*6 - common in Asians",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GA": {"activity": "intermediate", "phenotype": "Intermediate Metabolizer"},
            "AA": {"activity": "poor", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["irinotecan", "atazanavir"]
    }
}

# =============================================================================
# NUDT15 (Thiopurines - especially important in Asians)
# =============================================================================

NUDT15_GENETICS = {
    "rs116855232": {
        "gene": "NUDT15",
        "chromosome": "13",
        "variant_name": "R139C",
        "function": "NUDT15 - thiopurine metabolism (critical in Asians)",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CT": {"activity": "intermediate", "phenotype": "Intermediate Metabolizer - dose reduction"},
            "TT": {"activity": "poor", "phenotype": "Poor Metabolizer - SEVERE toxicity risk"}
        },
        "affected_drugs": ["azathioprine", "mercaptopurine", "thioguanine"]
    },
    "rs746071566": {
        "gene": "NUDT15",
        "chromosome": "13",
        "variant_name": "R139H",
        "function": "NUDT15*3 - loss of function",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GA": {"activity": "intermediate", "phenotype": "Intermediate Metabolizer"},
            "AA": {"activity": "poor", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["azathioprine", "mercaptopurine"]
    },
    "rs186364861": {
        "gene": "NUDT15",
        "chromosome": "13",
        "variant_name": "V18I",
        "function": "NUDT15*4 - intermediate function",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GA": {"activity": "intermediate", "phenotype": "Intermediate Metabolizer"},
            "AA": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"}
        },
        "affected_drugs": ["azathioprine", "mercaptopurine"]
    }
}

# =============================================================================
# CYP2B6 METABOLISM (Efavirenz, Methadone, Bupropion, Ketamine)
# =============================================================================

CYP2B6_GENETICS = {
    "rs3745274": {
        "gene": "CYP2B6",
        "chromosome": "19",
        "variant": "*9",
        "variant_name": "Q172H",
        "function": "CYP2B6*9 - decreased function",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GT": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "TT": {"activity": "poor", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["efavirenz", "nevirapine", "methadone", "bupropion", "ketamine", "cyclophosphamide"]
    },
    "rs28399499": {
        "gene": "CYP2B6",
        "chromosome": "19",
        "variant": "*18",
        "variant_name": "I328T",
        "function": "CYP2B6*18 - decreased function (African)",
        "effect": {
            "TT": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "TC": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "CC": {"activity": "poor", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["efavirenz", "nevirapine", "methadone"]
    },
    "rs3211371": {
        "gene": "CYP2B6",
        "chromosome": "19",
        "variant": "*5",
        "variant_name": "R487C",
        "function": "CYP2B6*5 - reduced expression",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CT": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "TT": {"activity": "poor", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["efavirenz", "bupropion", "methadone"]
    },
    "rs2279343": {
        "gene": "CYP2B6",
        "chromosome": "19",
        "variant": "*4",
        "variant_name": "K262R",
        "function": "CYP2B6*4 - increased activity",
        "effect": {
            "AA": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "AG": {"activity": "increased", "phenotype": "Rapid Metabolizer"},
            "GG": {"activity": "increased", "phenotype": "Rapid Metabolizer"}
        },
        "affected_drugs": ["efavirenz", "bupropion", "cyclophosphamide"]
    },
    "rs8192709": {
        "gene": "CYP2B6",
        "chromosome": "19",
        "variant": "*2",
        "variant_name": "R22C",
        "function": "CYP2B6*2 - normal to slightly reduced",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CT": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "TT": {"activity": "decreased", "phenotype": "Slightly Reduced"}
        },
        "affected_drugs": ["efavirenz", "bupropion"]
    },
    "rs4803419": {
        "gene": "CYP2B6",
        "chromosome": "19",
        "variant": "*22",
        "variant_name": "-82T>C",
        "function": "CYP2B6*22 - reduced expression",
        "effect": {
            "TT": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "TC": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "CC": {"activity": "poor", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["efavirenz", "nevirapine"]
    },
    "rs34223104": {
        "gene": "CYP2B6",
        "chromosome": "19",
        "variant": "*6",
        "variant_name": "Q172H+K262R",
        "function": "CYP2B6*6 - most common reduced function haplotype",
        "effect": {
            "TT": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "TC": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "CC": {"activity": "poor", "phenotype": "Poor Metabolizer - HIGH efavirenz levels"}
        },
        "affected_drugs": ["efavirenz", "nevirapine", "methadone", "bupropion"]
    }
}

# =============================================================================
# NAT2 METABOLISM (Isoniazid, Sulfonamides, Caffeine, Hydralazine)
# =============================================================================

NAT2_GENETICS = {
    "rs1801280": {
        "gene": "NAT2",
        "chromosome": "8",
        "variant": "*5",
        "variant_name": "I114T",
        "function": "NAT2*5 - slow acetylator",
        "effect": {
            "TT": {"activity": "normal", "phenotype": "Rapid Acetylator"},
            "TC": {"activity": "intermediate", "phenotype": "Intermediate Acetylator"},
            "CC": {"activity": "slow", "phenotype": "Slow Acetylator"}
        },
        "affected_drugs": ["isoniazid", "hydralazine", "procainamide", "sulfonamides", "caffeine"]
    },
    "rs1799930": {
        "gene": "NAT2",
        "chromosome": "8",
        "variant": "*6",
        "variant_name": "R197Q",
        "function": "NAT2*6 - slow acetylator",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Rapid Acetylator"},
            "GA": {"activity": "intermediate", "phenotype": "Intermediate Acetylator"},
            "AA": {"activity": "slow", "phenotype": "Slow Acetylator"}
        },
        "affected_drugs": ["isoniazid", "hydralazine", "procainamide", "sulfonamides"]
    },
    "rs1799931": {
        "gene": "NAT2",
        "chromosome": "8",
        "variant": "*7",
        "variant_name": "G286E",
        "function": "NAT2*7 - slow acetylator",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Rapid Acetylator"},
            "GA": {"activity": "intermediate", "phenotype": "Intermediate Acetylator"},
            "AA": {"activity": "slow", "phenotype": "Slow Acetylator"}
        },
        "affected_drugs": ["isoniazid", "hydralazine", "sulfonamides"]
    },
    "rs1801279": {
        "gene": "NAT2",
        "chromosome": "8",
        "variant": "*14",
        "variant_name": "R64Q",
        "function": "NAT2*14 - slow acetylator",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Rapid Acetylator"},
            "GA": {"activity": "intermediate", "phenotype": "Intermediate Acetylator"},
            "AA": {"activity": "slow", "phenotype": "Slow Acetylator"}
        },
        "affected_drugs": ["isoniazid", "hydralazine"]
    },
    "rs1208": {
        "gene": "NAT2",
        "chromosome": "8",
        "variant": "*4/*12/*13",
        "variant_name": "K268R",
        "function": "NAT2 - rapid acetylator marker",
        "effect": {
            "AA": {"activity": "rapid", "phenotype": "Rapid Acetylator"},
            "AG": {"activity": "rapid", "phenotype": "Rapid Acetylator"},
            "GG": {"activity": "varies", "phenotype": "Depends on other variants"}
        },
        "affected_drugs": ["isoniazid", "caffeine"]
    },
    "rs1041983": {
        "gene": "NAT2",
        "chromosome": "8",
        "variant": "C282T",
        "variant_name": "Y94Y",
        "function": "NAT2 synonymous - haplotype marker",
        "effect": {
            "CC": {"activity": "rapid", "phenotype": "Rapid Acetylator"},
            "CT": {"activity": "varies", "phenotype": "Intermediate possible"},
            "TT": {"activity": "varies", "phenotype": "Check other variants"}
        },
        "affected_drugs": ["isoniazid", "sulfonamides"]
    },
    "rs1495741": {
        "gene": "NAT2",
        "chromosome": "8",
        "variant": "Tag SNP",
        "variant_name": "Intergenic",
        "function": "NAT2 acetylator status tag SNP",
        "effect": {
            "AA": {"activity": "slow", "phenotype": "Slow Acetylator"},
            "AG": {"activity": "intermediate", "phenotype": "Intermediate Acetylator"},
            "GG": {"activity": "rapid", "phenotype": "Rapid Acetylator"}
        },
        "affected_drugs": ["isoniazid", "hydralazine", "sulfonamides", "caffeine"]
    }
}

# =============================================================================
# CYP2E1 METABOLISM (Acetaminophen, Alcohol, Anesthetics)
# =============================================================================

CYP2E1_GENETICS = {
    "rs2031920": {
        "gene": "CYP2E1",
        "chromosome": "10",
        "variant": "*5",
        "variant_name": "-1293G>C",
        "function": "CYP2E1*5 - altered expression",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "GC": {"activity": "increased", "phenotype": "Increased Activity"},
            "CC": {"activity": "increased", "phenotype": "Increased Activity - higher acetaminophen toxicity risk"}
        },
        "affected_drugs": ["acetaminophen", "alcohol", "isoflurane", "sevoflurane", "halothane"]
    },
    "rs6413432": {
        "gene": "CYP2E1",
        "chromosome": "10",
        "variant": "*6",
        "variant_name": "DraI",
        "function": "CYP2E1*6 - altered metabolism",
        "effect": {
            "TT": {"activity": "normal", "phenotype": "Normal"},
            "TA": {"activity": "variable", "phenotype": "Variable"},
            "AA": {"activity": "altered", "phenotype": "Altered metabolism"}
        },
        "affected_drugs": ["acetaminophen", "alcohol", "anesthetics"]
    },
    "rs3813867": {
        "gene": "CYP2E1",
        "chromosome": "10",
        "variant": "*5B",
        "variant_name": "-1053C>T",
        "function": "CYP2E1*5B - promoter variant",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal"},
            "GC": {"activity": "altered", "phenotype": "Altered expression"},
            "CC": {"activity": "altered", "phenotype": "Altered expression"}
        },
        "affected_drugs": ["acetaminophen", "chlorzoxazone"]
    }
}

# =============================================================================
# CYP3A4/CYP3A5 METABOLISM (Statins, Immunosuppressants, many drugs)
# =============================================================================

CYP3A_GENETICS = {
    "rs776746": {
        "gene": "CYP3A5",
        "chromosome": "7",
        "variant": "*3",
        "variant_name": "Splice variant",
        "function": "CYP3A5*3 - splicing defect causing non-expression",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "CYP3A5 Expressor"},
            "CT": {"activity": "decreased", "phenotype": "Intermediate Expressor"},
            "TT": {"activity": "none", "phenotype": "Non-Expressor"}
        },
        "affected_drugs": ["tacrolimus", "cyclosporine", "sirolimus", "atorvastatin",
                          "simvastatin", "midazolam", "fentanyl"]
    },
    "rs35599367": {
        "gene": "CYP3A4",
        "chromosome": "7",
        "variant": "*22",
        "variant_name": "Intronic",
        "function": "CYP3A4*22 - reduced expression",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CT": {"activity": "decreased", "phenotype": "Intermediate Metabolizer"},
            "TT": {"activity": "poor", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["statins", "tacrolimus", "cyclosporine", "midazolam"]
    },
    "rs10264272": {
        "gene": "CYP3A5",
        "chromosome": "7",
        "variant": "*6",
        "variant_name": "Splice",
        "function": "CYP3A5*6 - non-expression (African populations)",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "CYP3A5 Expressor"},
            "CT": {"activity": "none", "phenotype": "Non-Expressor"},
            "TT": {"activity": "none", "phenotype": "Non-Expressor"}
        },
        "affected_drugs": ["tacrolimus", "cyclosporine"]
    },
    "rs4646437": {
        "gene": "CYP3A4",
        "chromosome": "7",
        "variant": "*1B",
        "variant_name": "-392G>A",
        "function": "CYP3A4*1B - promoter variant",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal"},
            "GA": {"activity": "variable", "phenotype": "Variable expression"},
            "AA": {"activity": "variable", "phenotype": "Variable expression"}
        },
        "affected_drugs": ["statins", "tacrolimus", "midazolam"]
    }
}

# =============================================================================
# STATIN MYOPATHY RISK (SLCO1B1)
# =============================================================================

SLCO1B1_GENETICS = {
    "rs4149056": {
        "gene": "SLCO1B1",
        "chromosome": "12",
        "variant": "*5",
        "variant_name": "V174A",
        "function": "SLCO1B1 - hepatic transporter for statins",
        "effect": {
            "TT": {"myopathy_risk": "normal", "recommendation": "Standard statin dosing"},
            "TC": {"myopathy_risk": "increased_2x", "recommendation": "Consider lower dose or alternative statin"},
            "CC": {"myopathy_risk": "increased_17x", "recommendation": "Avoid simvastatin >20mg, consider alternative"}
        },
        "affected_drugs": ["simvastatin", "atorvastatin", "pravastatin", "rosuvastatin", "pitavastatin"]
    },
    "rs2306283": {
        "gene": "SLCO1B1",
        "chromosome": "12",
        "variant": "*1b",
        "variant_name": "N130D",
        "function": "SLCO1B1*1b - common variant affecting statin transport",
        "effect": {
            "AA": {"myopathy_risk": "normal", "recommendation": "Standard statin dosing"},
            "AG": {"myopathy_risk": "slightly_increased", "recommendation": "Standard dosing, monitor"},
            "GG": {"myopathy_risk": "increased_1.5x", "recommendation": "May affect some drug levels, monitor"}
        },
        "affected_drugs": ["statins", "methotrexate", "rifampin"]
    },
    "rs4149015": {
        "gene": "SLCO1B1",
        "chromosome": "12",
        "variant": "*15/*17",
        "variant_name": "-11187G>A",
        "function": "SLCO1B1 promoter - affects expression and statin transport",
        "effect": {
            "GG": {"myopathy_risk": "normal", "recommendation": "Standard statin dosing"},
            "GA": {"myopathy_risk": "slightly_increased", "recommendation": "Monitor drug response"},
            "AA": {"myopathy_risk": "increased_2x", "recommendation": "Consider lower dose or alternative"}
        },
        "affected_drugs": ["statins", "methotrexate"]
    }
}

# =============================================================================
# THIOPURINE TOXICITY (TPMT)
# =============================================================================

TPMT_GENETICS = {
    "rs1800460": {
        "gene": "TPMT",
        "chromosome": "6",
        "variant": "*3A/*3C",
        "variant_name": "A154T",
        "function": "Thiopurine methyltransferase",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CT": {"activity": "intermediate", "phenotype": "Intermediate Metabolizer"},
            "TT": {"activity": "deficient", "phenotype": "Poor Metabolizer - HIGH TOXICITY RISK"}
        },
        "affected_drugs": ["azathioprine", "mercaptopurine", "thioguanine"]
    },
    "rs1142345": {
        "gene": "TPMT",
        "chromosome": "6",
        "variant": "*3A",
        "variant_name": "Y240C",
        "function": "TPMT enzyme activity",
        "effect": {
            "AA": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "AG": {"activity": "intermediate", "phenotype": "Intermediate Metabolizer"},
            "GG": {"activity": "deficient", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["azathioprine", "mercaptopurine"]
    },
    "rs1800462": {
        "gene": "TPMT",
        "chromosome": "6",
        "variant": "*2",
        "variant_name": "A80P",
        "function": "TPMT*2 - non-functional",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CG": {"activity": "intermediate", "phenotype": "Intermediate Metabolizer"},
            "GG": {"activity": "deficient", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["azathioprine", "mercaptopurine", "thioguanine"]
    },
    "rs1800584": {
        "gene": "TPMT",
        "chromosome": "6",
        "variant": "*3D",
        "variant_name": "E98G",
        "function": "TPMT*3D - rare non-functional",
        "effect": {
            "AA": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "AG": {"activity": "intermediate", "phenotype": "Intermediate Metabolizer"},
            "GG": {"activity": "deficient", "phenotype": "Poor Metabolizer"}
        },
        "affected_drugs": ["azathioprine", "mercaptopurine"]
    }
}

# =============================================================================
# FLUOROPYRIMIDINE TOXICITY (DPYD)
# =============================================================================

DPYD_GENETICS = {
    "rs3918290": {
        "gene": "DPYD",
        "chromosome": "1",
        "variant": "*2A",
        "variant_name": "IVS14+1G>A",
        "function": "Dihydropyrimidine dehydrogenase - 5-FU metabolism",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CT": {"activity": "intermediate", "phenotype": "Intermediate - 50% dose reduction"},
            "TT": {"activity": "deficient", "phenotype": "DPYD Deficient - AVOID 5-FU"}
        },
        "affected_drugs": ["5-fluorouracil", "capecitabine", "tegafur"]
    },
    "rs55886062": {
        "gene": "DPYD",
        "chromosome": "1",
        "variant": "*13",
        "variant_name": "I560S",
        "function": "DPYD enzyme activity",
        "effect": {
            "AA": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "AT": {"activity": "intermediate", "phenotype": "Intermediate Metabolizer"},
            "TT": {"activity": "deficient", "phenotype": "DPYD Deficient"}
        },
        "affected_drugs": ["5-fluorouracil", "capecitabine"]
    },
    "rs67376798": {
        "gene": "DPYD",
        "chromosome": "1",
        "variant": "D949V",
        "variant_name": "D949V",
        "function": "DPYD - decreased function",
        "effect": {
            "TT": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "TA": {"activity": "intermediate", "phenotype": "Intermediate - dose reduction"},
            "AA": {"activity": "deficient", "phenotype": "DPYD Deficient"}
        },
        "affected_drugs": ["5-fluorouracil", "capecitabine"]
    },
    "rs75017182": {
        "gene": "DPYD",
        "chromosome": "1",
        "variant": "HapB3",
        "variant_name": "c.1129-5923C>G",
        "function": "DPYD HapB3 - decreased expression",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CG": {"activity": "intermediate", "phenotype": "Intermediate Metabolizer"},
            "GG": {"activity": "intermediate", "phenotype": "Intermediate Metabolizer"}
        },
        "affected_drugs": ["5-fluorouracil", "capecitabine"]
    }
}

# =============================================================================
# OPIOID SENSITIVITY (OPRM1)
# =============================================================================

OPRM1_GENETICS = {
    "rs1799971": {
        "gene": "OPRM1",
        "chromosome": "6",
        "variant_name": "A118G",
        "function": "Mu opioid receptor",
        "effect": {
            "AA": {"sensitivity": "normal", "description": "Normal opioid response"},
            "AG": {"sensitivity": "reduced", "description": "May require higher doses for pain relief"},
            "GG": {"sensitivity": "reduced", "description": "Reduced opioid binding - may need dose adjustment"}
        },
        "affected_drugs": ["morphine", "fentanyl", "oxycodone", "hydrocodone", "methadone", "buprenorphine"]
    },
    "rs2075572": {
        "gene": "OPRM1",
        "chromosome": "6",
        "variant_name": "Intronic",
        "function": "OPRM1 intronic - affects expression",
        "effect": {
            "CC": {"sensitivity": "normal", "description": "Normal response"},
            "CG": {"sensitivity": "variable", "description": "Variable response"},
            "GG": {"sensitivity": "altered", "description": "May affect opioid requirements"}
        },
        "affected_drugs": ["morphine", "fentanyl", "oxycodone"]
    },
    "rs563649": {
        "gene": "OPRM1",
        "chromosome": "6",
        "variant_name": "Intronic",
        "function": "OPRM1 - influences pain sensitivity",
        "effect": {
            "GG": {"sensitivity": "normal", "description": "Normal pain response"},
            "GA": {"sensitivity": "variable", "description": "Variable pain sensitivity"},
            "AA": {"sensitivity": "altered", "description": "Altered pain perception"}
        },
        "affected_drugs": ["opioids", "analgesics"]
    }
}

# =============================================================================
# ANTIDEPRESSANT RESPONSE (SLC6A4 - Serotonin transporter)
# =============================================================================

SSRI_GENETICS = {
    "rs25531": {
        "gene": "SLC6A4",
        "chromosome": "17",
        "variant_name": "5-HTTLPR LA/LG",
        "function": "Serotonin transporter - SSRI target",
        "effect": {
            "AA": {"response": "better", "description": "LA allele - better SSRI response predicted"},
            "AG": {"response": "intermediate", "description": "Intermediate SSRI response"},
            "GG": {"response": "reduced", "description": "LG/S allele - may have reduced SSRI response"}
        },
        "affected_drugs": ["sertraline", "fluoxetine", "paroxetine", "citalopram", "escitalopram"]
    },
    "rs6295": {
        "gene": "HTR1A",
        "chromosome": "5",
        "variant_name": "-1019C>G",
        "function": "Serotonin 1A receptor",
        "effect": {
            "CC": {"response": "better", "description": "Better antidepressant response"},
            "CG": {"response": "intermediate", "description": "Intermediate response"},
            "GG": {"response": "reduced", "description": "May have reduced response to SSRIs"}
        },
        "affected_drugs": ["SSRIs", "buspirone", "vilazodone"]
    },
    "rs6313": {
        "gene": "HTR2A",
        "chromosome": "13",
        "variant_name": "T102C",
        "function": "Serotonin 2A receptor - antidepressant response",
        "effect": {
            "CC": {"response": "better", "description": "Better SSRI response"},
            "CT": {"response": "intermediate", "description": "Intermediate response"},
            "TT": {"response": "variable", "description": "Variable response to SSRIs"}
        },
        "affected_drugs": ["SSRIs", "atypical antipsychotics"]
    },
    "rs7997012": {
        "gene": "HTR2A",
        "chromosome": "13",
        "variant_name": "Intronic",
        "function": "HTR2A - antidepressant treatment response",
        "effect": {
            "AA": {"response": "better", "description": "Better treatment response"},
            "AG": {"response": "intermediate", "description": "Intermediate"},
            "GG": {"response": "variable", "description": "Variable response"}
        },
        "affected_drugs": ["SSRIs", "SNRIs"]
    },
    "rs4680": {
        "gene": "COMT",
        "chromosome": "22",
        "variant_name": "V158M",
        "function": "Catechol-O-methyltransferase - affects dopamine",
        "effect": {
            "GG": {"phenotype": "Val/Val (Warrior)", "description": "Faster dopamine breakdown"},
            "AG": {"phenotype": "Val/Met", "description": "Intermediate"},
            "AA": {"phenotype": "Met/Met (Worrier)", "description": "Slower dopamine breakdown"}
        },
        "affected_drugs": ["SSRIs", "SNRIs", "antipsychotics", "ADHD medications"]
    }
}

# =============================================================================
# METHOTREXATE TOXICITY (MTHFR)
# =============================================================================

MTHFR_GENETICS = {
    "rs1801133": {
        "gene": "MTHFR",
        "chromosome": "1",
        "variant": "C677T",
        "variant_name": "A222V",
        "function": "Methylenetetrahydrofolate reductase",
        "effect": {
            "CC": {"activity": "normal", "folate_status": "normal"},
            "CT": {"activity": "reduced_35%", "folate_status": "may need supplementation"},
            "TT": {"activity": "reduced_70%", "folate_status": "folate supplementation recommended"}
        },
        "affected_drugs": ["methotrexate", "pemetrexed", "folic acid", "L-methylfolate"]
    },
    "rs1801131": {
        "gene": "MTHFR",
        "chromosome": "1",
        "variant": "A1298C",
        "variant_name": "E429A",
        "function": "MTHFR enzyme activity",
        "effect": {
            "AA": {"activity": "normal", "folate_status": "normal"},
            "AC": {"activity": "reduced_20%", "folate_status": "mild reduction"},
            "CC": {"activity": "reduced_40%", "folate_status": "may need supplementation"}
        },
        "affected_drugs": ["methotrexate", "folate metabolism"]
    }
}

# =============================================================================
# ABCB1 (P-GLYCOPROTEIN) - Drug efflux
# =============================================================================

ABCB1_GENETICS = {
    "rs1045642": {
        "gene": "ABCB1",
        "chromosome": "7",
        "variant": "C3435T",
        "variant_name": "I1145I",
        "function": "P-glycoprotein - drug efflux transporter",
        "effect": {
            "CC": {"expression": "high", "drug_levels": "lower tissue levels"},
            "CT": {"expression": "intermediate", "drug_levels": "intermediate"},
            "TT": {"expression": "low", "drug_levels": "higher tissue levels"}
        },
        "affected_drugs": ["digoxin", "fexofenadine", "loperamide", "cyclosporine",
                          "tacrolimus", "chemotherapy agents"]
    },
    "rs1128503": {
        "gene": "ABCB1",
        "chromosome": "7",
        "variant": "C1236T",
        "variant_name": "G412G",
        "function": "P-glycoprotein expression",
        "effect": {
            "CC": {"expression": "high", "drug_levels": "standard"},
            "CT": {"expression": "intermediate", "drug_levels": "intermediate"},
            "TT": {"expression": "reduced", "drug_levels": "may be elevated"}
        },
        "affected_drugs": ["digoxin", "immunosuppressants", "antiretrovirals"]
    },
    "rs2032582": {
        "gene": "ABCB1",
        "chromosome": "7",
        "variant": "G2677T/A",
        "variant_name": "S893A/T",
        "function": "P-glycoprotein - major functional variant",
        "effect": {
            "GG": {"expression": "high", "drug_levels": "standard efflux"},
            "GT": {"expression": "intermediate", "drug_levels": "intermediate"},
            "TT": {"expression": "low", "drug_levels": "elevated tissue levels"}
        },
        "affected_drugs": ["digoxin", "tacrolimus", "cyclosporine", "fexofenadine"]
    }
}

# =============================================================================
# CARBAMAZEPINE HYPERSENSITIVITY (HLA-B)
# =============================================================================

HLA_DRUG_GENETICS = {
    "rs2395029": {
        "gene": "HLA-B*5701",
        "chromosome": "6",
        "variant_name": "HLA-B*57:01 tag",
        "function": "HLA class I - immune response",
        "effect": {
            "TT": {"risk": "low", "recommendation": "Standard abacavir use"},
            "CT": {"risk": "high", "recommendation": "AVOID abacavir - hypersensitivity risk"},
            "CC": {"risk": "high", "recommendation": "AVOID abacavir"}
        },
        "affected_drugs": ["abacavir"]
    },
    "rs3909184": {
        "gene": "HLA-B*1502",
        "chromosome": "6",
        "variant_name": "HLA-B*15:02 tag",
        "function": "HLA class I - carbamazepine reaction",
        "effect": {
            "AA": {"risk": "low", "recommendation": "Standard use in non-Asian populations"},
            "AG": {"risk": "high", "recommendation": "Screen before carbamazepine in Asians"},
            "GG": {"risk": "very_high", "recommendation": "AVOID carbamazepine - SJS/TEN risk"}
        },
        "affected_drugs": ["carbamazepine", "oxcarbazepine", "phenytoin"]
    },
    "rs1061235": {
        "gene": "HLA-A*3101",
        "chromosome": "6",
        "variant_name": "HLA-A*31:01 tag",
        "function": "HLA-A*31:01 - carbamazepine hypersensitivity (Europeans)",
        "effect": {
            "TT": {"risk": "low", "recommendation": "Standard carbamazepine dosing"},
            "CT": {"risk": "intermediate", "recommendation": "Monitor closely"},
            "CC": {"risk": "high", "recommendation": "Consider alternative to carbamazepine"}
        },
        "affected_drugs": ["carbamazepine", "oxcarbazepine"]
    },
    "rs2395029": {
        "gene": "HLA-B*5801",
        "chromosome": "6",
        "variant_name": "HLA-B*58:01 proxy",
        "function": "HLA-B*58:01 - allopurinol hypersensitivity",
        "effect": {
            "GG": {"risk": "low", "recommendation": "Standard allopurinol use"},
            "AG": {"risk": "high", "recommendation": "Caution with allopurinol"},
            "AA": {"risk": "very_high", "recommendation": "AVOID allopurinol - SJS risk"}
        },
        "affected_drugs": ["allopurinol"]
    }
}

# =============================================================================
# CAFFEINE METABOLISM (CYP1A2)
# =============================================================================

CYP1A2_GENETICS = {
    "rs762551": {
        "gene": "CYP1A2",
        "chromosome": "15",
        "variant": "*1F",
        "variant_name": "-163C>A",
        "function": "CYP1A2 - caffeine and drug metabolism",
        "effect": {
            "AA": {"activity": "rapid", "phenotype": "Rapid Caffeine Metabolizer"},
            "AC": {"activity": "intermediate", "phenotype": "Intermediate Metabolizer"},
            "CC": {"activity": "slow", "phenotype": "Slow Caffeine Metabolizer"}
        },
        "affected_drugs": ["caffeine", "theophylline", "clozapine", "olanzapine", "melatonin"]
    },
    "rs2069514": {
        "gene": "CYP1A2",
        "chromosome": "15",
        "variant": "*1C",
        "variant_name": "-3860G>A",
        "function": "CYP1A2*1C - reduced inducibility",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal inducibility"},
            "GA": {"activity": "reduced", "phenotype": "Reduced inducibility"},
            "AA": {"activity": "reduced", "phenotype": "Reduced inducibility"}
        },
        "affected_drugs": ["caffeine", "theophylline", "clozapine"]
    },
    "rs12720461": {
        "gene": "CYP1A2",
        "chromosome": "15",
        "variant": "*1K",
        "variant_name": "-729C>T",
        "function": "CYP1A2*1K - reduced activity",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Metabolizer"},
            "CT": {"activity": "reduced", "phenotype": "Reduced Activity"},
            "TT": {"activity": "reduced", "phenotype": "Reduced Activity"}
        },
        "affected_drugs": ["caffeine", "clozapine", "olanzapine"]
    }
}

# =============================================================================
# ALCOHOL METABOLISM (ADH1B, ALDH2)
# =============================================================================

# =============================================================================
# BETA-BLOCKER RESPONSE (ADRB1, ADRB2)
# =============================================================================

ADRB_GENETICS = {
    "rs1801252": {
        "gene": "ADRB1",
        "chromosome": "10",
        "variant_name": "S49G",
        "function": "Beta-1 receptor - cardiovascular drug response",
        "effect": {
            "AA": {"response": "enhanced", "phenotype": "Enhanced beta-blocker response"},
            "AG": {"response": "normal", "phenotype": "Normal response"},
            "GG": {"response": "reduced", "phenotype": "May need higher doses"}
        },
        "affected_drugs": ["metoprolol", "atenolol", "bisoprolol", "carvedilol", "nebivolol"]
    },
    "rs1801253": {
        "gene": "ADRB1",
        "chromosome": "10",
        "variant_name": "R389G",
        "function": "Beta-1 receptor - major functional variant",
        "effect": {
            "CC": {"response": "enhanced", "phenotype": "Arg389 - Enhanced beta-blocker response"},
            "CG": {"response": "intermediate", "phenotype": "Intermediate response"},
            "GG": {"response": "reduced", "phenotype": "Gly389 - Reduced response"}
        },
        "affected_drugs": ["metoprolol", "atenolol", "carvedilol", "bucindolol"]
    },
    "rs1042713": {
        "gene": "ADRB2",
        "chromosome": "5",
        "variant_name": "R16G",
        "function": "Beta-2 receptor - bronchodilator and cardiac response",
        "effect": {
            "AA": {"response": "variable", "phenotype": "Arg16 - variable bronchodilator response"},
            "AG": {"response": "intermediate", "phenotype": "Intermediate"},
            "GG": {"response": "enhanced", "phenotype": "Gly16 - better initial bronchodilator response"}
        },
        "affected_drugs": ["albuterol", "salmeterol", "formoterol", "carvedilol"]
    },
    "rs1042714": {
        "gene": "ADRB2",
        "chromosome": "5",
        "variant_name": "Q27E",
        "function": "Beta-2 receptor - affects receptor function",
        "effect": {
            "CC": {"response": "normal", "phenotype": "Gln27 - normal"},
            "CG": {"response": "intermediate", "phenotype": "Intermediate"},
            "GG": {"response": "altered", "phenotype": "Glu27 - altered response"}
        },
        "affected_drugs": ["albuterol", "salmeterol", "beta-blockers"]
    },
    "rs1800888": {
        "gene": "ADRB2",
        "chromosome": "5",
        "variant_name": "T164I",
        "function": "Beta-2 receptor - rare but significant variant",
        "effect": {
            "CC": {"response": "normal", "phenotype": "Normal Thr164"},
            "CT": {"response": "reduced", "phenotype": "Reduced receptor function"},
            "TT": {"response": "poor", "phenotype": "Significantly reduced function"}
        },
        "affected_drugs": ["albuterol", "salmeterol", "formoterol"]
    }
}

# =============================================================================
# GLUTATHIONE S-TRANSFERASES (Chemotherapy, Detoxification)
# =============================================================================

GST_GENETICS = {
    "rs1695": {
        "gene": "GSTP1",
        "chromosome": "11",
        "variant_name": "I105V",
        "function": "GSTP1*B - chemotherapy detoxification",
        "effect": {
            "AA": {"activity": "normal", "phenotype": "Normal - Ile105"},
            "AG": {"activity": "reduced", "phenotype": "Intermediate detoxification"},
            "GG": {"activity": "reduced", "phenotype": "Val105 - reduced detoxification, altered chemo response"}
        },
        "affected_drugs": ["cyclophosphamide", "cisplatin", "carboplatin", "oxaliplatin", "doxorubicin"]
    },
    "rs1138272": {
        "gene": "GSTP1",
        "chromosome": "11",
        "variant_name": "A114V",
        "function": "GSTP1*C - additional variant",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal Ala114"},
            "CT": {"activity": "reduced", "phenotype": "Intermediate"},
            "TT": {"activity": "reduced", "phenotype": "Val114 - reduced activity"}
        },
        "affected_drugs": ["platinum chemotherapy", "cyclophosphamide"]
    },
    "rs1799735": {
        "gene": "GSTM3",
        "chromosome": "1",
        "variant_name": "Intron 6",
        "function": "GSTM3 - detoxification enzyme",
        "effect": {
            "AA": {"activity": "normal", "phenotype": "Normal"},
            "AB": {"activity": "variable", "phenotype": "Variable"},
            "BB": {"activity": "altered", "phenotype": "Altered detoxification"}
        },
        "affected_drugs": ["chemotherapy agents", "carcinogens"]
    },
    "rs4986938": {
        "gene": "GSTT1",
        "chromosome": "22",
        "variant_name": "Deletion proxy",
        "function": "GSTT1 null - gene deletion",
        "effect": {
            "present": {"activity": "normal", "phenotype": "GSTT1 present - normal detox"},
            "null": {"activity": "none", "phenotype": "GSTT1 null - reduced detoxification"}
        },
        "affected_drugs": ["chemotherapy", "industrial chemicals"]
    },
    "rs366631": {
        "gene": "GSTM1",
        "chromosome": "1",
        "variant_name": "Deletion proxy",
        "function": "GSTM1 null - gene deletion",
        "effect": {
            "present": {"activity": "normal", "phenotype": "GSTM1 present"},
            "null": {"activity": "none", "phenotype": "GSTM1 null - 50% of population"}
        },
        "affected_drugs": ["chemotherapy", "acetaminophen", "carcinogens"]
    }
}

# =============================================================================
# ANTICOAGULANT RESPONSE (F2, F5, additional)
# =============================================================================

COAGULATION_GENETICS = {
    "rs1799963": {
        "gene": "F2",
        "chromosome": "11",
        "variant_name": "G20210A",
        "function": "Prothrombin mutation - clotting risk",
        "effect": {
            "GG": {"risk": "normal", "phenotype": "Normal prothrombin"},
            "GA": {"risk": "increased", "phenotype": "Prothrombin mutation carrier - increased clot risk"},
            "AA": {"risk": "high", "phenotype": "Homozygous - high clot risk"}
        },
        "affected_drugs": ["warfarin", "heparin", "DOACs", "oral contraceptives"]
    },
    "rs6025": {
        "gene": "F5",
        "chromosome": "1",
        "variant_name": "R506Q (Leiden)",
        "function": "Factor V Leiden - most common thrombophilia",
        "effect": {
            "GG": {"risk": "normal", "phenotype": "Normal Factor V"},
            "GA": {"risk": "increased_5x", "phenotype": "FVL heterozygous - 5x clot risk"},
            "AA": {"risk": "increased_50x", "phenotype": "FVL homozygous - 50x clot risk"}
        },
        "affected_drugs": ["warfarin", "heparin", "oral contraceptives", "HRT"]
    },
    "rs2289252": {
        "gene": "F11",
        "chromosome": "4",
        "variant_name": "Intron 13",
        "function": "Factor XI levels - bleeding/clotting",
        "effect": {
            "TT": {"risk": "low", "phenotype": "Lower F11 levels"},
            "TC": {"risk": "normal", "phenotype": "Normal"},
            "CC": {"risk": "elevated", "phenotype": "Higher F11 - increased clot risk"}
        },
        "affected_drugs": ["anticoagulants"]
    },
    "rs1799889": {
        "gene": "SERPINE1",
        "chromosome": "7",
        "variant_name": "4G/5G",
        "function": "PAI-1 - plasminogen activator inhibitor",
        "effect": {
            "5G5G": {"risk": "low", "phenotype": "Lower PAI-1 - better clot breakdown"},
            "4G5G": {"risk": "intermediate", "phenotype": "Intermediate"},
            "4G4G": {"risk": "elevated", "phenotype": "Higher PAI-1 - increased thrombosis risk"}
        },
        "affected_drugs": ["anticoagulants", "thrombolytics"]
    }
}

# =============================================================================
# ANTIPSYCHOTIC RESPONSE (DRD2, DRD3, HTR2C)
# =============================================================================

ANTIPSYCHOTIC_GENETICS = {
    "rs1800497": {
        "gene": "DRD2/ANKK1",
        "chromosome": "11",
        "variant_name": "Taq1A",
        "function": "Dopamine D2 receptor - antipsychotic response",
        "effect": {
            "CC": {"response": "normal", "phenotype": "A2/A2 - normal D2 density"},
            "CT": {"response": "variable", "phenotype": "A1/A2 - reduced D2 density"},
            "TT": {"response": "reduced", "phenotype": "A1/A1 - lowest D2 density, variable response"}
        },
        "affected_drugs": ["haloperidol", "risperidone", "olanzapine", "aripiprazole", "clozapine"]
    },
    "rs6280": {
        "gene": "DRD3",
        "chromosome": "3",
        "variant_name": "S9G",
        "function": "Dopamine D3 receptor",
        "effect": {
            "CC": {"response": "normal", "phenotype": "Ser9 - normal"},
            "CT": {"response": "variable", "phenotype": "Heterozygous"},
            "TT": {"response": "altered", "phenotype": "Gly9 - altered response, tardive dyskinesia risk"}
        },
        "affected_drugs": ["antipsychotics", "pramipexole", "ropinirole"]
    },
    "rs3813929": {
        "gene": "HTR2C",
        "chromosome": "X",
        "variant_name": "-759C>T",
        "function": "Serotonin 2C receptor - weight gain prediction",
        "effect": {
            "CC": {"risk": "high", "phenotype": "Higher weight gain risk with antipsychotics"},
            "CT": {"risk": "intermediate", "phenotype": "Intermediate risk"},
            "TT": {"risk": "low", "phenotype": "Lower weight gain risk"}
        },
        "affected_drugs": ["olanzapine", "clozapine", "quetiapine", "risperidone"]
    },
    "rs518147": {
        "gene": "HTR2C",
        "chromosome": "X",
        "variant_name": "Intron",
        "function": "HTR2C - metabolic side effects",
        "effect": {
            "CC": {"risk": "lower", "phenotype": "Lower metabolic risk"},
            "CT": {"risk": "intermediate", "phenotype": "Intermediate"},
            "TT": {"risk": "higher", "phenotype": "Higher metabolic syndrome risk"}
        },
        "affected_drugs": ["atypical antipsychotics"]
    },
    "rs1414334": {
        "gene": "HTR2C",
        "chromosome": "X",
        "variant_name": "Intron",
        "function": "HTR2C - antipsychotic-induced weight gain",
        "effect": {
            "CC": {"risk": "high", "phenotype": "High weight gain susceptibility"},
            "CG": {"risk": "intermediate", "phenotype": "Intermediate"},
            "GG": {"risk": "lower", "phenotype": "Lower risk"}
        },
        "affected_drugs": ["olanzapine", "clozapine"]
    }
}

# =============================================================================
# PAIN RESPONSE (Additional markers)
# =============================================================================

PAIN_GENETICS = {
    "rs4680": {
        "gene": "COMT",
        "chromosome": "22",
        "variant_name": "V158M",
        "function": "Catechol-O-methyltransferase - pain sensitivity",
        "effect": {
            "GG": {"sensitivity": "lower", "phenotype": "Val/Val - lower pain sensitivity, faster dopamine clearance"},
            "AG": {"sensitivity": "intermediate", "phenotype": "Val/Met - intermediate"},
            "AA": {"sensitivity": "higher", "phenotype": "Met/Met - higher pain sensitivity, may need more opioids"}
        },
        "affected_drugs": ["opioids", "NSAIDs", "antidepressants for pain"]
    },
    "rs4818": {
        "gene": "COMT",
        "chromosome": "22",
        "variant_name": "L136L",
        "function": "COMT haplotype marker",
        "effect": {
            "CC": {"sensitivity": "varies", "phenotype": "Part of pain haplotype"},
            "CG": {"sensitivity": "intermediate", "phenotype": "Intermediate"},
            "GG": {"sensitivity": "varies", "phenotype": "Part of pain haplotype"}
        },
        "affected_drugs": ["opioids", "pain medications"]
    },
    "rs6269": {
        "gene": "COMT",
        "chromosome": "22",
        "variant_name": "Synonymous",
        "function": "COMT haplotype - pain processing",
        "effect": {
            "AA": {"sensitivity": "higher", "phenotype": "High pain sensitivity haplotype"},
            "AG": {"sensitivity": "intermediate", "phenotype": "Intermediate"},
            "GG": {"sensitivity": "lower", "phenotype": "Low pain sensitivity"}
        },
        "affected_drugs": ["opioids", "analgesics"]
    },
    "rs16944": {
        "gene": "IL1B",
        "chromosome": "2",
        "variant_name": "-511C>T",
        "function": "IL-1beta - inflammatory pain",
        "effect": {
            "CC": {"inflammation": "lower", "phenotype": "Lower IL-1B expression"},
            "CT": {"inflammation": "intermediate", "phenotype": "Intermediate"},
            "TT": {"inflammation": "higher", "phenotype": "Higher inflammation - may affect chronic pain"}
        },
        "affected_drugs": ["NSAIDs", "IL-1 inhibitors", "opioids"]
    },
    "rs1800795": {
        "gene": "IL6",
        "chromosome": "7",
        "variant_name": "-174G>C",
        "function": "IL-6 - inflammatory pain response",
        "effect": {
            "GG": {"inflammation": "higher", "phenotype": "Higher IL-6 - increased inflammation"},
            "GC": {"inflammation": "intermediate", "phenotype": "Intermediate"},
            "CC": {"inflammation": "lower", "phenotype": "Lower IL-6 - less inflammatory pain"}
        },
        "affected_drugs": ["NSAIDs", "corticosteroids", "IL-6 inhibitors"]
    },
    "rs1799971": {
        "gene": "OPRM1",
        "chromosome": "6",
        "variant_name": "A118G",
        "function": "Mu-opioid receptor - opioid response",
        "effect": {
            "AA": {"response": "normal", "phenotype": "Normal opioid response"},
            "AG": {"response": "reduced", "phenotype": "May need higher opioid doses"},
            "GG": {"response": "significantly_reduced", "phenotype": "Reduced opioid efficacy"}
        },
        "affected_drugs": ["morphine", "fentanyl", "oxycodone", "codeine"]
    },
    "rs1045642": {
        "gene": "ABCB1",
        "chromosome": "7",
        "variant_name": "C3435T",
        "function": "P-glycoprotein - opioid brain penetration",
        "effect": {
            "CC": {"penetration": "lower", "phenotype": "Less opioid in brain - may need higher dose"},
            "CT": {"penetration": "intermediate", "phenotype": "Intermediate"},
            "TT": {"penetration": "higher", "phenotype": "More opioid effect - may need lower dose"}
        },
        "affected_drugs": ["morphine", "fentanyl", "methadone", "loperamide"]
    },
    "rs4633": {
        "gene": "COMT",
        "chromosome": "22",
        "variant_name": "His62His",
        "function": "COMT haplotype - pain sensitivity",
        "effect": {
            "TT": {"sensitivity": "higher", "phenotype": "Higher pain sensitivity"},
            "TC": {"sensitivity": "intermediate", "phenotype": "Intermediate"},
            "CC": {"sensitivity": "lower", "phenotype": "Lower pain sensitivity"}
        },
        "affected_drugs": ["opioids", "analgesics"]
    },
    "rs2952768": {
        "gene": "GCH1",
        "chromosome": "14",
        "variant_name": "Intronic",
        "function": "BH4 synthesis - pain modulation",
        "effect": {
            "CC": {"protection": "protective", "phenotype": "Lower chronic pain risk"},
            "CT": {"protection": "intermediate", "phenotype": "Intermediate"},
            "TT": {"protection": "none", "phenotype": "Normal pain sensitivity"}
        },
        "affected_drugs": ["chronic pain medications"]
    },
    "rs7209436": {
        "gene": "GCH1",
        "chromosome": "14",
        "variant_name": "Intronic",
        "function": "Pain protective haplotype",
        "effect": {
            "CC": {"protection": "protective", "phenotype": "Protective against chronic pain"},
            "CT": {"protection": "intermediate", "phenotype": "Intermediate"},
            "TT": {"protection": "none", "phenotype": "Normal pain processing"}
        },
        "affected_drugs": ["analgesics", "neuropathic pain drugs"]
    },
    "rs4141964": {
        "gene": "KCNS1",
        "chromosome": "20",
        "variant_name": "Intronic",
        "function": "Potassium channel - neuropathic pain",
        "effect": {
            "AA": {"sensitivity": "higher", "phenotype": "Higher neuropathic pain risk"},
            "AG": {"sensitivity": "intermediate", "phenotype": "Intermediate"},
            "GG": {"sensitivity": "lower", "phenotype": "Lower neuropathic pain risk"}
        },
        "affected_drugs": ["gabapentin", "pregabalin", "carbamazepine"]
    },
    "rs6746030": {
        "gene": "SCN9A",
        "chromosome": "2",
        "variant_name": "R1150W",
        "function": "Nav1.7 sodium channel - pain perception",
        "effect": {
            "GG": {"sensitivity": "normal", "phenotype": "Normal pain perception"},
            "GA": {"sensitivity": "reduced", "phenotype": "Reduced pain sensitivity"},
            "AA": {"sensitivity": "very_reduced", "phenotype": "Significantly reduced pain"}
        },
        "affected_drugs": ["local anesthetics", "sodium channel blockers"]
    },
    "rs12994338": {
        "gene": "SCN9A",
        "chromosome": "2",
        "variant_name": "Intronic",
        "function": "Nav1.7 expression - pain threshold",
        "effect": {
            "TT": {"sensitivity": "higher", "phenotype": "Higher pain sensitivity"},
            "TC": {"sensitivity": "intermediate", "phenotype": "Intermediate"},
            "CC": {"sensitivity": "lower", "phenotype": "Lower pain sensitivity"}
        },
        "affected_drugs": ["analgesics", "local anesthetics"]
    },
    "rs2234922": {
        "gene": "EPHX1",
        "chromosome": "1",
        "variant_name": "H139R",
        "function": "Epoxide hydrolase - drug metabolism in pain",
        "effect": {
            "AA": {"activity": "normal", "phenotype": "Normal metabolism"},
            "AG": {"activity": "intermediate", "phenotype": "Intermediate"},
            "GG": {"activity": "fast", "phenotype": "Faster drug metabolism"}
        },
        "affected_drugs": ["phenytoin", "carbamazepine", "valproate"]
    },
    "rs1800587": {
        "gene": "IL1A",
        "chromosome": "2",
        "variant_name": "-889C>T",
        "function": "IL-1 alpha - inflammatory pain",
        "effect": {
            "CC": {"inflammation": "lower", "phenotype": "Lower IL-1A"},
            "CT": {"inflammation": "intermediate", "phenotype": "Intermediate"},
            "TT": {"inflammation": "higher", "phenotype": "Higher inflammatory response"}
        },
        "affected_drugs": ["NSAIDs", "IL-1 antagonists"]
    },
    "rs1800629": {
        "gene": "TNF",
        "chromosome": "6",
        "variant_name": "-308G>A",
        "function": "TNF-alpha - inflammatory pain",
        "effect": {
            "GG": {"inflammation": "normal", "phenotype": "Normal TNF levels"},
            "GA": {"inflammation": "higher", "phenotype": "Higher TNF - more inflammation"},
            "AA": {"inflammation": "high", "phenotype": "High TNF - chronic pain risk"}
        },
        "affected_drugs": ["TNF inhibitors", "NSAIDs", "steroids"]
    }
}

# =============================================================================
# ALCOHOL METABOLISM (ADH1B, ALDH2)
# =============================================================================

ALCOHOL_GENETICS = {
    "rs1229984": {
        "gene": "ADH1B",
        "chromosome": "4",
        "variant_name": "H48R",
        "function": "Alcohol dehydrogenase - ethanol metabolism",
        "effect": {
            "CC": {"activity": "slow", "phenotype": "Slow alcohol metabolism"},
            "CT": {"activity": "fast", "phenotype": "Fast alcohol metabolism"},
            "TT": {"activity": "very_fast", "phenotype": "Very fast metabolism - protective against alcoholism"}
        },
        "affected_drugs": ["alcohol/ethanol"]
    },
    "rs671": {
        "gene": "ALDH2",
        "chromosome": "12",
        "variant_name": "E504K",
        "function": "Aldehyde dehydrogenase - acetaldehyde metabolism",
        "effect": {
            "GG": {"activity": "normal", "phenotype": "Normal - no flush reaction"},
            "GA": {"activity": "reduced", "phenotype": "Asian flush - reduced tolerance"},
            "AA": {"activity": "deficient", "phenotype": "Severe flush reaction - avoid alcohol"}
        },
        "affected_drugs": ["alcohol/ethanol", "nitroglycerin"]
    },
    "rs2066702": {
        "gene": "ADH1B",
        "chromosome": "4",
        "variant_name": "R370C",
        "function": "ADH1B*3 - rapid metabolism (African populations)",
        "effect": {
            "CC": {"activity": "normal", "phenotype": "Normal metabolism"},
            "CT": {"activity": "fast", "phenotype": "Fast metabolism"},
            "TT": {"activity": "very_fast", "phenotype": "Very fast metabolism - African variant"}
        },
        "affected_drugs": ["alcohol/ethanol"]
    },
    "rs1693482": {
        "gene": "ADH1C",
        "chromosome": "4",
        "variant_name": "I350V",
        "function": "ADH1C*1 vs *2 - affects alcohol metabolism rate",
        "effect": {
            "CC": {"activity": "fast", "phenotype": "*1/*1 Fast metabolizer"},
            "CT": {"activity": "intermediate", "phenotype": "*1/*2 Intermediate"},
            "TT": {"activity": "slow", "phenotype": "*2/*2 Slower metabolism"}
        },
        "affected_drugs": ["alcohol/ethanol"]
    }
}

# =============================================================================
# DRUG RECOMMENDATIONS DATABASE
# =============================================================================

DRUG_RECOMMENDATIONS = {
    "codeine": {
        "gene": "CYP2D6",
        "normal_metabolizer": "Standard dosing",
        "intermediate_metabolizer": "Consider 25-50% dose reduction or alternative",
        "poor_metabolizer": "AVOID - no analgesic effect, use alternative opioid",
        "ultrarapid_metabolizer": "AVOID - risk of toxicity, use alternative"
    },
    "clopidogrel": {
        "gene": "CYP2C19",
        "normal_metabolizer": "Standard 75mg daily",
        "intermediate_metabolizer": "Consider alternative (prasugrel, ticagrelor)",
        "poor_metabolizer": "Use alternative antiplatelet (prasugrel, ticagrelor)",
        "ultrarapid_metabolizer": "Standard dosing effective"
    },
    "warfarin": {
        "genes": ["CYP2C9", "VKORC1"],
        "dosing_algorithm": "Use FDA-approved warfarin dosing calculator",
        "poor_metabolizer": "Start with lower dose, more frequent INR monitoring",
        "high_sensitivity": "Reduce initial dose by 25-50%"
    },
    "simvastatin": {
        "gene": "SLCO1B1",
        "normal": "Standard dosing up to 80mg",
        "intermediate": "Limit to 20mg or use alternative statin",
        "high_risk": "AVOID simvastatin, use pravastatin or rosuvastatin"
    },
    "tacrolimus": {
        "gene": "CYP3A5",
        "expressor": "May require higher doses",
        "non_expressor": "Standard dosing, therapeutic drug monitoring"
    },
    "azathioprine": {
        "gene": "TPMT",
        "normal": "Standard dosing",
        "intermediate": "Start with 30-70% dose reduction",
        "poor": "AVOID or use 10% of standard dose with close monitoring"
    },
    "5-fluorouracil": {
        "gene": "DPYD",
        "normal": "Standard dosing",
        "intermediate": "50% dose reduction",
        "deficient": "AVOID - life-threatening toxicity risk"
    },
    "abacavir": {
        "gene": "HLA-B*5701",
        "negative": "Standard use",
        "positive": "CONTRAINDICATED - hypersensitivity risk"
    },
    "carbamazepine": {
        "gene": "HLA-B*1502",
        "negative": "Standard use",
        "positive": "AVOID - SJS/TEN risk (screen Asians before use)"
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


def analyze_pharmacogenomics(dna_data: Dict[str, str]) -> Dict[str, Any]:
    """
    Analyze DNA data for pharmacogenomics markers

    Args:
        dna_data: Dictionary mapping rsIDs to genotypes

    Returns:
        Dictionary containing pharmacogenomics analysis results
    """
    results = {}

    # Analyze CYP2D6
    cyp2d6_results = []
    cyp2d6_phenotype = "Normal Metabolizer"
    for rsid, snp_info in CYP2D6_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                cyp2d6_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "variant": snp_info.get("variant", ""),
                    "genotype": genotype,
                    "phenotype": effect["phenotype"]
                })
                if effect["activity"] in ["none", "decreased"]:
                    if "Poor" in effect["phenotype"]:
                        cyp2d6_phenotype = "Poor Metabolizer"
                    elif cyp2d6_phenotype != "Poor Metabolizer":
                        cyp2d6_phenotype = "Intermediate Metabolizer"

    results["cyp2d6"] = {
        "phenotype": cyp2d6_phenotype,
        "affected_drugs": ["codeine", "tramadol", "oxycodone", "tamoxifen", "fluoxetine",
                         "paroxetine", "metoprolol", "carvedilol"],
        "recommendation": get_cyp2d6_recommendation(cyp2d6_phenotype),
        "variants_analyzed": len(cyp2d6_results),
        "snps_analyzed": cyp2d6_results
    }

    # Analyze CYP2C19
    cyp2c19_results = []
    cyp2c19_phenotype = "Normal Metabolizer"
    for rsid, snp_info in CYP2C19_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                cyp2c19_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "variant": snp_info.get("variant", ""),
                    "genotype": genotype,
                    "phenotype": effect["phenotype"]
                })
                if "Poor" in effect["phenotype"]:
                    cyp2c19_phenotype = "Poor Metabolizer"
                elif "Ultrarapid" in effect["phenotype"]:
                    cyp2c19_phenotype = "Ultrarapid Metabolizer"
                elif "Rapid" in effect["phenotype"] and cyp2c19_phenotype == "Normal Metabolizer":
                    cyp2c19_phenotype = "Rapid Metabolizer"
                elif "Intermediate" in effect["phenotype"] and cyp2c19_phenotype == "Normal Metabolizer":
                    cyp2c19_phenotype = "Intermediate Metabolizer"

    results["cyp2c19"] = {
        "phenotype": cyp2c19_phenotype,
        "affected_drugs": ["clopidogrel", "omeprazole", "pantoprazole", "citalopram",
                         "escitalopram", "sertraline", "voriconazole"],
        "recommendation": get_cyp2c19_recommendation(cyp2c19_phenotype),
        "variants_analyzed": len(cyp2c19_results),
        "snps_analyzed": cyp2c19_results
    }

    # Analyze CYP2C9
    cyp2c9_results = []
    cyp2c9_phenotype = "Normal Metabolizer"
    for rsid, snp_info in CYP2C9_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                cyp2c9_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "variant": snp_info.get("variant", ""),
                    "genotype": genotype,
                    "activity": effect["activity"]
                })
                if effect["activity"] in ["poor", "decreased"]:
                    cyp2c9_phenotype = "Poor Metabolizer" if effect["activity"] == "poor" else "Intermediate Metabolizer"

    results["cyp2c9"] = {
        "phenotype": cyp2c9_phenotype,
        "affected_drugs": ["warfarin", "phenytoin", "celecoxib", "glimepiride", "glipizide"],
        "recommendation": get_cyp2c9_recommendation(cyp2c9_phenotype),
        "variants_analyzed": len(cyp2c9_results),
        "snps_analyzed": cyp2c9_results
    }

    # Analyze VKORC1 for warfarin
    vkorc1_results = []
    warfarin_sensitivity = "Normal"
    for rsid, snp_info in VKORC1_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                vkorc1_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "sensitivity": effect["sensitivity"],
                    "dose_adjustment": effect["dose_adjustment"]
                })
                warfarin_sensitivity = effect["sensitivity"]

    results["vkorc1_warfarin"] = {
        "sensitivity": warfarin_sensitivity,
        "dose_adjustment": get_warfarin_dose_adjustment(warfarin_sensitivity),
        "variants_analyzed": len(vkorc1_results),
        "snps_analyzed": vkorc1_results
    }

    # Analyze SLCO1B1 for statin myopathy
    slco1b1_results = []
    statin_myopathy_risk = "Normal"
    for rsid, snp_info in SLCO1B1_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                slco1b1_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "risk": effect["myopathy_risk"],
                    "recommendation": effect["recommendation"]
                })
                if "17x" in effect["myopathy_risk"]:
                    statin_myopathy_risk = "High"
                elif "2x" in effect["myopathy_risk"]:
                    statin_myopathy_risk = "Intermediate"

    results["slco1b1_statins"] = {
        "myopathy_risk": statin_myopathy_risk,
        "affected_drugs": ["simvastatin", "atorvastatin", "pravastatin", "rosuvastatin"],
        "recommendation": get_statin_recommendation(statin_myopathy_risk),
        "variants_analyzed": len(slco1b1_results),
        "snps_analyzed": slco1b1_results
    }

    # Analyze TPMT
    tpmt_results = []
    tpmt_status = "Normal"
    for rsid, snp_info in TPMT_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                tpmt_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "activity": effect["activity"]
                })
                if effect["activity"] == "deficient":
                    tpmt_status = "Deficient"
                elif effect["activity"] == "intermediate" and tpmt_status != "Deficient":
                    tpmt_status = "Intermediate"

    results["tpmt_thiopurines"] = {
        "status": tpmt_status,
        "affected_drugs": ["azathioprine", "mercaptopurine", "thioguanine"],
        "recommendation": get_tpmt_recommendation(tpmt_status),
        "variants_analyzed": len(tpmt_results),
        "snps_analyzed": tpmt_results
    }

    # Analyze DPYD
    dpyd_results = []
    dpyd_status = "Normal"
    for rsid, snp_info in DPYD_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                dpyd_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "activity": effect["activity"]
                })
                if effect["activity"] == "deficient":
                    dpyd_status = "Deficient"
                elif effect["activity"] == "intermediate" and dpyd_status != "Deficient":
                    dpyd_status = "Intermediate"

    results["dpyd_fluoropyrimidines"] = {
        "status": dpyd_status,
        "affected_drugs": ["5-fluorouracil", "capecitabine"],
        "recommendation": get_dpyd_recommendation(dpyd_status),
        "variants_analyzed": len(dpyd_results),
        "snps_analyzed": dpyd_results
    }

    # Analyze opioid response
    opioid_results = []
    opioid_response = "Normal"
    for rsid, snp_info in OPRM1_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                opioid_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "sensitivity": effect["sensitivity"]
                })
                if effect["sensitivity"] == "reduced":
                    opioid_response = "Reduced"

    results["oprm1_opioids"] = {
        "response": opioid_response,
        "affected_drugs": ["morphine", "fentanyl", "oxycodone", "hydrocodone"],
        "recommendation": "May require dose adjustment" if opioid_response == "Reduced" else "Standard dosing",
        "variants_analyzed": len(opioid_results),
        "snps_analyzed": opioid_results
    }

    # Analyze caffeine metabolism
    caffeine_results = []
    caffeine_metabolism = "Normal"
    for rsid, snp_info in CYP1A2_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                caffeine_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "phenotype": effect["phenotype"]
                })
                caffeine_metabolism = effect["phenotype"]

    results["cyp1a2_caffeine"] = {
        "metabolism": caffeine_metabolism,
        "affected_drugs": ["caffeine", "theophylline", "clozapine"],
        "recommendation": get_caffeine_recommendation(caffeine_metabolism),
        "variants_analyzed": len(caffeine_results),
        "snps_analyzed": caffeine_results
    }

    # Analyze MTHFR
    mthfr_results = []
    mthfr_status = "Normal"
    for rsid, snp_info in MTHFR_GENETICS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                mthfr_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "variant": snp_info.get("variant", ""),
                    "genotype": genotype,
                    "activity": effect["activity"]
                })
                if "70%" in str(effect["activity"]):
                    mthfr_status = "Significantly Reduced"
                elif "35%" in str(effect["activity"]) or "40%" in str(effect["activity"]):
                    if mthfr_status != "Significantly Reduced":
                        mthfr_status = "Moderately Reduced"

    results["mthfr_folate"] = {
        "status": mthfr_status,
        "affected_drugs": ["methotrexate", "folate supplements"],
        "recommendation": get_mthfr_recommendation(mthfr_status),
        "variants_analyzed": len(mthfr_results),
        "snps_analyzed": mthfr_results
    }

    # Count total actionable findings
    actionable_count = 0
    if cyp2d6_phenotype != "Normal Metabolizer":
        actionable_count += 1
    if cyp2c19_phenotype != "Normal Metabolizer":
        actionable_count += 1
    if cyp2c9_phenotype != "Normal Metabolizer":
        actionable_count += 1
    if warfarin_sensitivity != "Normal":
        actionable_count += 1
    if statin_myopathy_risk != "Normal":
        actionable_count += 1
    if tpmt_status != "Normal":
        actionable_count += 1
    if dpyd_status != "Normal":
        actionable_count += 1

    results["summary"] = {
        "total_genes_analyzed": 10,
        "actionable_findings": actionable_count,
        "drugs_with_guidance": get_all_drug_guidance(results)
    }

    return results


def get_cyp2d6_recommendation(phenotype: str) -> str:
    """Get CYP2D6-based drug recommendations"""
    recs = {
        "Poor Metabolizer": "AVOID codeine/tramadol (no effect). Consider alternatives for SSRIs. Lower doses for beta-blockers.",
        "Intermediate Metabolizer": "Consider dose reductions for codeine, tramadol. Monitor for reduced efficacy.",
        "Normal Metabolizer": "Standard dosing for CYP2D6 substrates",
        "Ultrarapid Metabolizer": "AVOID codeine (toxicity risk). May need higher SSRI doses."
    }
    return recs.get(phenotype, "Standard dosing")


def get_cyp2c19_recommendation(phenotype: str) -> str:
    """Get CYP2C19-based drug recommendations"""
    recs = {
        "Poor Metabolizer": "Use prasugrel/ticagrelor instead of clopidogrel. PPIs may have prolonged effect.",
        "Intermediate Metabolizer": "Consider alternative to clopidogrel. Standard PPI dosing.",
        "Normal Metabolizer": "Standard dosing for CYP2C19 substrates",
        "Rapid Metabolizer": "Standard clopidogrel effective. May need higher SSRI doses.",
        "Ultrarapid Metabolizer": "Good clopidogrel response. Consider higher SSRI doses if poor response."
    }
    return recs.get(phenotype, "Standard dosing")


def get_cyp2c9_recommendation(phenotype: str) -> str:
    """Get CYP2C9-based drug recommendations"""
    recs = {
        "Poor Metabolizer": "Lower warfarin dose needed. Caution with NSAIDs. Sulfonylurea dose reduction.",
        "Intermediate Metabolizer": "Moderate warfarin dose reduction. Monitor with NSAIDs.",
        "Normal Metabolizer": "Standard dosing for CYP2C9 substrates"
    }
    return recs.get(phenotype, "Standard dosing")


def get_warfarin_dose_adjustment(sensitivity: str) -> str:
    """Get warfarin dose adjustment based on VKORC1"""
    adjustments = {
        "high": "40-60% dose reduction - start low",
        "intermediate": "20-40% dose reduction",
        "normal": "Standard dosing algorithm"
    }
    return adjustments.get(sensitivity, "Standard dosing")


def get_statin_recommendation(risk: str) -> str:
    """Get statin recommendations based on SLCO1B1"""
    recs = {
        "High": "Avoid simvastatin >20mg. Use pravastatin, rosuvastatin, or fluvastatin instead.",
        "Intermediate": "Limit simvastatin to 20mg. Consider alternative statin.",
        "Normal": "Standard statin dosing. Monitor for muscle symptoms."
    }
    return recs.get(risk, "Standard dosing")


def get_tpmt_recommendation(status: str) -> str:
    """Get thiopurine recommendations based on TPMT"""
    recs = {
        "Deficient": "AVOID or use 10% dose with frequent monitoring. Consider alternative immunosuppressant.",
        "Intermediate": "Start with 30-70% dose reduction. Monitor closely.",
        "Normal": "Standard dosing with routine monitoring."
    }
    return recs.get(status, "Standard dosing")


def get_dpyd_recommendation(status: str) -> str:
    """Get fluoropyrimidine recommendations based on DPYD"""
    recs = {
        "Deficient": "CONTRAINDICATED - life-threatening toxicity risk. Use alternative chemotherapy.",
        "Intermediate": "50% dose reduction required. Close monitoring essential.",
        "Normal": "Standard dosing with routine monitoring."
    }
    return recs.get(status, "Standard dosing")


def get_caffeine_recommendation(metabolism: str) -> str:
    """Get caffeine recommendations based on CYP1A2"""
    recs = {
        "Slow Caffeine Metabolizer": "Limit caffeine to <200mg/day. Avoid afternoon caffeine. Higher cardiovascular risk with excess caffeine.",
        "Intermediate Metabolizer": "Moderate caffeine intake recommended.",
        "Rapid Caffeine Metabolizer": "Can tolerate higher caffeine. May metabolize some medications faster."
    }
    return recs.get(metabolism, "Moderate caffeine intake")


def get_mthfr_recommendation(status: str) -> str:
    """Get folate/MTHFR recommendations"""
    recs = {
        "Significantly Reduced": "Consider methylfolate supplementation. May need methotrexate dose adjustment.",
        "Moderately Reduced": "Folate supplementation may be beneficial.",
        "Normal": "Standard folate requirements."
    }
    return recs.get(status, "Standard folate intake")


def get_all_drug_guidance(results: Dict[str, Any]) -> List[Dict[str, str]]:
    """Compile all drug guidance from results"""
    guidance = []

    if results.get("cyp2d6", {}).get("phenotype") != "Normal Metabolizer":
        guidance.append({
            "drug_class": "Opioids (codeine, tramadol)",
            "guidance": results["cyp2d6"]["recommendation"]
        })

    if results.get("cyp2c19", {}).get("phenotype") != "Normal Metabolizer":
        guidance.append({
            "drug_class": "Clopidogrel",
            "guidance": results["cyp2c19"]["recommendation"]
        })

    if results.get("slco1b1_statins", {}).get("myopathy_risk") != "Normal":
        guidance.append({
            "drug_class": "Statins",
            "guidance": results["slco1b1_statins"]["recommendation"]
        })

    if results.get("tpmt_thiopurines", {}).get("status") != "Normal":
        guidance.append({
            "drug_class": "Thiopurines (azathioprine)",
            "guidance": results["tpmt_thiopurines"]["recommendation"]
        })

    if results.get("dpyd_fluoropyrimidines", {}).get("status") != "Normal":
        guidance.append({
            "drug_class": "Fluoropyrimidines (5-FU)",
            "guidance": results["dpyd_fluoropyrimidines"]["recommendation"]
        })

    return guidance
