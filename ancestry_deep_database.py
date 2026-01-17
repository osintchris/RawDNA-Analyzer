"""
Deep Ancestry Genetics Database
Detailed regional ancestry markers and ancient migration patterns
Sources: 1000 Genomes, Human Origins, GWAS ancestry-informative markers
"""

from typing import Dict, Any, List

# =============================================================================
# EUROPEAN SUB-REGIONAL MARKERS
# =============================================================================

EUROPEAN_REGIONAL_MARKERS = {
    # Northern European markers
    "rs16891982": {
        "gene": "SLC45A2",
        "region": "Northern European",
        "populations": ["Scandinavian", "British", "German"],
        "effect": {
            "GG": {"ancestry": "Southern/Non-European", "frequency": 0.02},
            "CG": {"ancestry": "Mixed European", "frequency": 0.15},
            "CC": {"ancestry": "Northern European", "frequency": 0.98}
        }
    },
    "rs12913832": {
        "gene": "HERC2/OCA2",
        "region": "Northern European",
        "populations": ["Nordic", "Baltic", "British Isles"],
        "effect": {
            "AA": {"ancestry": "Northern European (blue eyes)", "frequency": 0.75},
            "AG": {"ancestry": "Mixed European", "frequency": 0.50},
            "GG": {"ancestry": "Southern/Non-European", "frequency": 0.10}
        }
    },
    "rs1426654": {
        "gene": "SLC24A5",
        "region": "European",
        "populations": ["All European"],
        "effect": {
            "AA": {"ancestry": "European", "frequency": 0.99},
            "AG": {"ancestry": "Mixed", "frequency": 0.50},
            "GG": {"ancestry": "African/Asian", "frequency": 0.01}
        }
    },
    # Mediterranean markers
    "rs1800407": {
        "gene": "OCA2",
        "region": "Mediterranean",
        "populations": ["Italian", "Greek", "Iberian"],
        "effect": {
            "CC": {"ancestry": "Northern European", "frequency": 0.85},
            "CT": {"ancestry": "Mediterranean/Mixed", "frequency": 0.40},
            "TT": {"ancestry": "Mediterranean", "frequency": 0.15}
        }
    },
    # Eastern European markers
    "rs4988235": {
        "gene": "LCT",
        "region": "Northern/Eastern European",
        "populations": ["Slavic", "Scandinavian", "British"],
        "effect": {
            "TT": {"ancestry": "Northern European (lactase persistent)", "frequency": 0.80},
            "CT": {"ancestry": "Mixed European", "frequency": 0.50},
            "CC": {"ancestry": "Southern European/Non-European", "frequency": 0.15}
        }
    }
}

# =============================================================================
# AFRICAN REGIONAL MARKERS
# =============================================================================

AFRICAN_REGIONAL_MARKERS = {
    "rs2814778": {
        "gene": "DARC/Duffy",
        "region": "Sub-Saharan African",
        "populations": ["West African", "Central African", "East African"],
        "effect": {
            "CC": {"ancestry": "Sub-Saharan African (Duffy null)", "frequency": 0.99},
            "CT": {"ancestry": "Mixed African/Non-African", "frequency": 0.50},
            "TT": {"ancestry": "Non-African", "frequency": 0.99}
        }
    },
    "rs1800401": {
        "gene": "OCA2",
        "region": "African",
        "populations": ["West African", "East African"],
        "effect": {
            "CC": {"ancestry": "Non-African", "frequency": 0.95},
            "CT": {"ancestry": "Mixed", "frequency": 0.50},
            "TT": {"ancestry": "African", "frequency": 0.30}
        }
    },
    "rs7495174": {
        "gene": "OCA2",
        "region": "African",
        "populations": ["African populations"],
        "effect": {
            "AA": {"ancestry": "African ancestry", "frequency": 0.85},
            "AG": {"ancestry": "Mixed", "frequency": 0.50},
            "GG": {"ancestry": "Non-African", "frequency": 0.90}
        }
    }
}

# =============================================================================
# EAST ASIAN REGIONAL MARKERS
# =============================================================================

EAST_ASIAN_REGIONAL_MARKERS = {
    "rs3827760": {
        "gene": "EDAR",
        "region": "East Asian",
        "populations": ["Han Chinese", "Japanese", "Korean", "Native American"],
        "effect": {
            "CC": {"ancestry": "Non-Asian", "frequency": 0.01},
            "CT": {"ancestry": "Mixed Asian", "frequency": 0.30},
            "TT": {"ancestry": "East Asian/Native American", "frequency": 0.95}
        }
    },
    "rs671": {
        "gene": "ALDH2",
        "region": "East Asian",
        "populations": ["Han Chinese", "Japanese", "Korean"],
        "effect": {
            "GG": {"ancestry": "Non-Asian or mixed", "frequency": 0.99},
            "GA": {"ancestry": "East Asian (flush reaction)", "frequency": 0.35},
            "AA": {"ancestry": "East Asian (strong flush)", "frequency": 0.05}
        }
    },
    "rs1229984": {
        "gene": "ADH1B",
        "region": "East Asian",
        "populations": ["East Asian populations"],
        "effect": {
            "CC": {"ancestry": "European/African", "frequency": 0.95},
            "CT": {"ancestry": "Mixed", "frequency": 0.30},
            "TT": {"ancestry": "East Asian", "frequency": 0.70}
        }
    }
}

# =============================================================================
# SOUTH ASIAN REGIONAL MARKERS
# =============================================================================

SOUTH_ASIAN_REGIONAL_MARKERS = {
    "rs1042602": {
        "gene": "TYR",
        "region": "South Asian",
        "populations": ["Indian", "Pakistani", "Bangladeshi"],
        "effect": {
            "CC": {"ancestry": "European", "frequency": 0.70},
            "CA": {"ancestry": "South Asian/Mixed", "frequency": 0.45},
            "AA": {"ancestry": "South Asian/African", "frequency": 0.25}
        }
    },
    "rs12203592": {
        "gene": "IRF4",
        "region": "European/South Asian",
        "populations": ["European", "South Asian"],
        "effect": {
            "CC": {"ancestry": "Non-European", "frequency": 0.80},
            "CT": {"ancestry": "European/Mixed", "frequency": 0.40},
            "TT": {"ancestry": "Northern European", "frequency": 0.15}
        }
    }
}

# =============================================================================
# NATIVE AMERICAN MARKERS
# =============================================================================

NATIVE_AMERICAN_MARKERS = {
    "rs3827760": {
        "gene": "EDAR",
        "region": "Native American/East Asian",
        "populations": ["Native American", "Mestizo"],
        "effect": {
            "TT": {"ancestry": "Native American/East Asian", "frequency": 0.95},
            "CT": {"ancestry": "Mixed ancestry", "frequency": 0.50},
            "CC": {"ancestry": "European/African", "frequency": 0.01}
        }
    },
    "rs1426654": {
        "gene": "SLC24A5",
        "region": "Native American ancestry indicator",
        "populations": ["Native American"],
        "effect": {
            "GG": {"ancestry": "Native American (ancestral)", "frequency": 0.60},
            "AG": {"ancestry": "Mixed/Mestizo", "frequency": 0.40},
            "AA": {"ancestry": "European ancestry", "frequency": 0.99}
        }
    }
}

# =============================================================================
# MIDDLE EASTERN/NORTH AFRICAN MARKERS
# =============================================================================

MENA_MARKERS = {
    "rs1426654": {
        "gene": "SLC24A5",
        "region": "Middle Eastern/North African",
        "populations": ["Arab", "Berber", "Persian", "Turkish"],
        "effect": {
            "AA": {"ancestry": "Western Eurasian", "frequency": 0.85},
            "AG": {"ancestry": "Mixed", "frequency": 0.50},
            "GG": {"ancestry": "Sub-Saharan African", "frequency": 0.01}
        }
    },
    "rs16891982": {
        "gene": "SLC45A2",
        "region": "MENA pigmentation",
        "populations": ["Middle Eastern", "North African"],
        "effect": {
            "CC": {"ancestry": "Lighter skin MENA", "frequency": 0.70},
            "CG": {"ancestry": "Mixed", "frequency": 0.40},
            "GG": {"ancestry": "Darker skin MENA/African", "frequency": 0.10}
        }
    }
}

# =============================================================================
# ANCIENT MIGRATION MARKERS
# =============================================================================

MIGRATION_MARKERS = {
    # Indo-European expansion markers
    "rs4988235": {
        "migration": "Neolithic Farmer Expansion",
        "description": "Lactase persistence spread with farming",
        "origin": "Anatolia/Near East",
        "time_period": "8,000-5,000 years ago",
        "effect": {
            "TT": {"ancestry": "Descended from lactase-persistent farmers", "migration": "Farmer ancestry"},
            "CT": {"ancestry": "Mixed farmer/hunter-gatherer", "migration": "Partial farmer ancestry"},
            "CC": {"ancestry": "Non-farmer ancestry", "migration": "Hunter-gatherer ancestry"}
        }
    },
    # Steppe ancestry
    "rs1800012": {
        "migration": "Bronze Age Steppe Migration",
        "description": "Indo-European expansion from Pontic Steppe",
        "origin": "Ukraine/Russia steppes",
        "time_period": "5,000-3,000 years ago",
        "effect": {
            "GG": {"ancestry": "Common in steppe-descended populations", "migration": "Yamnaya-related"},
            "GT": {"ancestry": "Mixed ancestry", "migration": "Partial steppe"},
            "TT": {"ancestry": "Less steppe ancestry", "migration": "Non-steppe"}
        }
    },
    # Out of Africa
    "rs2814778": {
        "migration": "Out of Africa",
        "description": "Duffy null provides malaria protection",
        "origin": "Sub-Saharan Africa",
        "time_period": "70,000+ years ago",
        "effect": {
            "CC": {"ancestry": "African origin - malaria protection", "migration": "Remained in Africa"},
            "CT": {"ancestry": "Mixed African/Non-African", "migration": "Recent admixture"},
            "TT": {"ancestry": "Non-African - susceptible to P. vivax", "migration": "Out of Africa lineage"}
        }
    },
    # Pacific Islander markers
    "rs3827760": {
        "migration": "Austronesian Expansion",
        "description": "EDAR variant spread with East Asian/Pacific migration",
        "origin": "Taiwan/Southeast Asia",
        "time_period": "5,000-1,000 years ago",
        "effect": {
            "TT": {"ancestry": "East Asian/Pacific ancestry", "migration": "Austronesian expansion"},
            "CT": {"ancestry": "Mixed", "migration": "Contact with East Asian populations"},
            "CC": {"ancestry": "European/African", "migration": "Non-Austronesian"}
        }
    }
}

# =============================================================================
# JEWISH ANCESTRY MARKERS
# =============================================================================

JEWISH_ANCESTRY_MARKERS = {
    "rs12913832": {
        "population": "Ashkenazi Jewish",
        "description": "Eye color - Ashkenazi intermediate frequency",
        "effect": {
            "AA": {"ancestry": "Possible Ashkenazi (blue eyes ~25%)", "frequency": 0.25},
            "AG": {"ancestry": "Mixed", "frequency": 0.40},
            "GG": {"ancestry": "Southern Mediterranean/MENA", "frequency": 0.35}
        }
    },
    "rs4988235": {
        "population": "Jewish populations",
        "description": "Lactase persistence in Jewish populations",
        "effect": {
            "TT": {"ancestry": "Lactase persistent", "frequency": 0.60},
            "CT": {"ancestry": "Heterozygous", "frequency": 0.30},
            "CC": {"ancestry": "Lactase non-persistent", "frequency": 0.10}
        }
    }
}

# =============================================================================
# FINNISH/ISOLATED POPULATION MARKERS
# =============================================================================

ISOLATED_POPULATION_MARKERS = {
    "rs1800562": {
        "gene": "HFE",
        "population": "Celtic/Nordic",
        "description": "Hemochromatosis - high in Celtic populations",
        "effect": {
            "GG": {"ancestry": "Non-Celtic", "frequency": 0.90},
            "GA": {"ancestry": "Celtic/Nordic carrier", "frequency": 0.10},
            "AA": {"ancestry": "Celtic ancestry", "frequency": 0.005}
        }
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


def analyze_deep_ancestry(dna_data: Dict[str, str]) -> Dict[str, Any]:
    """
    Analyze DNA data for detailed regional ancestry

    Args:
        dna_data: Dictionary mapping rsIDs to genotypes

    Returns:
        Dictionary containing deep ancestry analysis
    """
    results = {}

    # Analyze European regional markers
    european_results = []
    european_score = {"northern": 0, "southern": 0, "eastern": 0}
    for rsid, snp_info in EUROPEAN_REGIONAL_MARKERS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                european_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "region": snp_info["region"],
                    "ancestry": effect["ancestry"]
                })
                if "Northern" in effect["ancestry"]:
                    european_score["northern"] += 1
                if "Mediterranean" in effect["ancestry"] or "Southern" in effect["ancestry"]:
                    european_score["southern"] += 1

    results["european_regional"] = {
        "northern_european_score": european_score["northern"],
        "southern_european_score": european_score["southern"],
        "likely_region": get_european_region(european_score),
        "variants_analyzed": len(european_results),
        "snps_analyzed": european_results
    }

    # Analyze African regional markers
    african_results = []
    african_score = 0
    has_duffy_null = False
    for rsid, snp_info in AFRICAN_REGIONAL_MARKERS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                african_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "region": snp_info["region"],
                    "ancestry": effect["ancestry"]
                })
                if "African" in effect["ancestry"] and "Non" not in effect["ancestry"]:
                    african_score += 1
                    if "Duffy null" in effect["ancestry"]:
                        has_duffy_null = True

    results["african_regional"] = {
        "african_ancestry_score": african_score,
        "has_duffy_null": has_duffy_null,
        "duffy_null_note": "Duffy null provides malaria resistance" if has_duffy_null else None,
        "variants_analyzed": len(african_results),
        "snps_analyzed": african_results
    }

    # Analyze East Asian regional markers
    east_asian_results = []
    east_asian_score = 0
    has_asian_flush = False
    for rsid, snp_info in EAST_ASIAN_REGIONAL_MARKERS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                east_asian_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "region": snp_info["region"],
                    "ancestry": effect["ancestry"]
                })
                if "East Asian" in effect["ancestry"] and "Non" not in effect["ancestry"]:
                    east_asian_score += 1
                    if "flush" in effect["ancestry"]:
                        has_asian_flush = True

    results["east_asian_regional"] = {
        "east_asian_ancestry_score": east_asian_score,
        "has_asian_flush": has_asian_flush,
        "edar_variant": any("EDAR" in r.get("gene", "") for r in east_asian_results),
        "variants_analyzed": len(east_asian_results),
        "snps_analyzed": east_asian_results
    }

    # Analyze South Asian markers
    south_asian_results = []
    south_asian_score = 0
    for rsid, snp_info in SOUTH_ASIAN_REGIONAL_MARKERS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                south_asian_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "ancestry": effect["ancestry"]
                })
                if "South Asian" in effect["ancestry"]:
                    south_asian_score += 1

    results["south_asian_regional"] = {
        "south_asian_ancestry_score": south_asian_score,
        "variants_analyzed": len(south_asian_results),
        "snps_analyzed": south_asian_results
    }

    # Analyze Native American markers
    native_american_results = []
    native_american_score = 0
    for rsid, snp_info in NATIVE_AMERICAN_MARKERS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                native_american_results.append({
                    "rsid": rsid,
                    "gene": snp_info["gene"],
                    "genotype": genotype,
                    "ancestry": effect["ancestry"]
                })
                if "Native American" in effect["ancestry"]:
                    native_american_score += 1

    results["native_american_regional"] = {
        "native_american_ancestry_score": native_american_score,
        "variants_analyzed": len(native_american_results),
        "snps_analyzed": native_american_results
    }

    # Analyze migration patterns
    migration_results = []
    migrations_detected = []
    for rsid, snp_info in MIGRATION_MARKERS.items():
        genotype = dna_data.get(rsid)
        if genotype:
            effect = get_effect_with_complement(genotype, snp_info["effect"])
            if effect:
                migration_results.append({
                    "rsid": rsid,
                    "migration": snp_info["migration"],
                    "genotype": genotype,
                    "description": snp_info["description"],
                    "origin": snp_info["origin"],
                    "time_period": snp_info["time_period"],
                    "ancestry": effect["ancestry"],
                    "migration_type": effect.get("migration", "")
                })
                if effect.get("migration") and "Non" not in effect.get("migration", ""):
                    migrations_detected.append({
                        "name": snp_info["migration"],
                        "origin": snp_info["origin"],
                        "time_period": snp_info["time_period"]
                    })

    results["migration_patterns"] = {
        "migrations_detected": migrations_detected,
        "variants_analyzed": len(migration_results),
        "snps_analyzed": migration_results
    }

    # Determine primary ancestry
    ancestry_scores = {
        "European": european_score["northern"] + european_score["southern"],
        "African": african_score,
        "East Asian": east_asian_score,
        "South Asian": south_asian_score,
        "Native American": native_american_score
    }

    primary_ancestry = max(ancestry_scores, key=ancestry_scores.get) if any(ancestry_scores.values()) else "Mixed/Unknown"

    # Overall summary
    total_variants = sum([
        len(european_results), len(african_results), len(east_asian_results),
        len(south_asian_results), len(native_american_results), len(migration_results)
    ])

    results["overall"] = {
        "primary_ancestry_signal": primary_ancestry,
        "ancestry_scores": ancestry_scores,
        "total_variants_analyzed": total_variants,
        "ancestry_summary": get_ancestry_summary(ancestry_scores, migrations_detected)
    }

    return results


def get_european_region(scores: Dict[str, int]) -> str:
    """Determine likely European region"""
    if scores["northern"] > scores["southern"]:
        return "Northern European (Scandinavian/British/Germanic)"
    elif scores["southern"] > scores["northern"]:
        return "Southern European (Mediterranean)"
    elif scores["northern"] > 0 or scores["southern"] > 0:
        return "Central European (Mixed North/South)"
    else:
        return "Insufficient data"


def get_ancestry_summary(scores: Dict[str, int], migrations: List[Dict]) -> str:
    """Generate ancestry summary text"""
    summary_parts = []

    # Find significant ancestries
    for ancestry, score in scores.items():
        if score >= 2:
            summary_parts.append(f"Strong {ancestry} ancestry signal")
        elif score == 1:
            summary_parts.append(f"Some {ancestry} ancestry markers")

    # Add migration info
    if migrations:
        migration_names = [m["name"] for m in migrations]
        summary_parts.append(f"Migration patterns: {', '.join(migration_names)}")

    if summary_parts:
        return " | ".join(summary_parts)
    else:
        return "Mixed or insufficient ancestry markers to determine primary ancestry"
