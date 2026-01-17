#!/usr/bin/env python3
"""
Comprehensive DNA Analysis Engine
Integrates all analysis modules for a complete DNA analysis experience
177 Reference Populations (AncestryDNA 2025 level)
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, field
import math

# Import the expanded reference populations (177 regions)
from reference_populations import REFERENCE_POPULATIONS

# Import REAL ancestry data from scientific databases (dbSNP, gnomAD, 1000 Genomes)
from real_ancestry_data import REAL_ANCESTRY_MARKERS, POPULATION_HIERARCHY, REGION_DISPLAY_NAMES

# Import EXPANDED trait databases with real SNPs and action recommendations
from expanded_traits import (
    PHYSICAL_TRAITS_EXPANDED,
    HEALTH_TRAITS_EXPANDED,
    PHARMACOGENOMICS_EXPANDED,
    CARRIER_STATUS,
    IMMUNITY_EXPANDED,
    NUTRITION_EXPANDED,
    FITNESS_EXPANDED
)

# Import Ancient DNA database (Neanderthal/Denisovan)
from ancient_dna_database import (
    NEANDERTHAL_SNPS,
    DENISOVAN_SNPS,
    NEANDERTHAL_TRAIT_CATEGORIES,
    HUMAN_MIGRATION_TIMELINE,
    MTDNA_MIGRATION_PATHS,
    YDNA_MIGRATION_PATHS
)

# Import expanded genetics (Blood types, Athletic, PRS, Longevity)
from expanded_genetics_database import (
    BLOOD_TYPE_GENETICS,
    ATHLETIC_GENES,
    ADAPTATION_GENETICS,
    POLYGENIC_RISK_SCORES,
    LONGEVITY_MARKERS
)

# Import advanced traits (Facial features, Chronotype, Pain, Addiction, Sensory, etc.)
from advanced_traits_database import (
    FACIAL_FEATURES,
    CHRONOTYPE_GENETICS,
    PAIN_GENETICS,
    ADDICTION_GENETICS,
    MENTAL_GENETICS,
    SENSORY_GENETICS,
    BODY_ODOR_GENETICS,
    HANDEDNESS_GENETICS,
    ANCIENT_POPULATIONS,
    VOICE_GENETICS,
    LONGEVITY_MARKERS_FIXED
)

# Import comprehensive sensory genetics database
from sensory_genetics_database import analyze_sensory_genetics

# Import comprehensive carrier status database
from carrier_status_database import analyze_carrier_status as analyze_carrier_status_comprehensive

# Import comprehensive behavioral genetics database
from behavioral_genetics_database import analyze_behavioral_genetics

# Import comprehensive sleep genetics database
from sleep_genetics_database import analyze_sleep_genetics

# Import expanded physical traits database
from physical_traits_expanded_database import analyze_physical_traits_expanded

# Import sports genetics database
from sports_genetics_database import analyze_sports_genetics

# Import reproduction genetics database
from reproduction_genetics_database import analyze_reproduction_genetics

# Import immune deep genetics database
from immune_deep_genetics_database import analyze_immune_deep_genetics

# Import nutrition metabolism database
from nutrition_metabolism_database import analyze_nutrition_metabolism

# Import ancient DNA history database
from ancient_dna_history_database import analyze_ancient_dna_history

# Import longevity genetics database
from longevity_genetics_database import analyze_longevity_genetics

# Import pharmacogenomics database
from pharmacogenomics_database import analyze_pharmacogenomics

# Import mental health genetics database
from mental_health_database import analyze_mental_health_genetics

# Import cancer risk genetics database
from cancer_risk_database import analyze_cancer_risk_genetics

# Import cardiovascular genetics database
from cardiovascular_database import analyze_cardiovascular_genetics

# Import skin dermatology genetics database
from skin_dermatology_database import analyze_skin_dermatology

# Import deep ancestry genetics database
from ancestry_deep_database import analyze_deep_ancestry

# =============================================================================
# DATA CLASSES FOR RESULTS
# =============================================================================

@dataclass
class AncestryResult:
    """Detailed ancestry result for a population"""
    population: str
    region: str
    country: str
    percentage: float
    confidence: float
    historical_context: str
    time_depth: Tuple[int, int]

@dataclass
class TraitResult:
    """Physical or health trait result"""
    trait_name: str
    prediction: str
    confidence: float
    genotype: str
    description: str
    category: str

@dataclass
class PharmacogeneticResult:
    """Drug metabolism result"""
    gene: str
    phenotype: str
    activity_score: float
    drug_recommendations: List[Dict]
    clinical_significance: str

@dataclass
class HaplogroupResult:
    """mtDNA or Y-DNA haplogroup result"""
    haplogroup: str
    confidence: float
    origin_region: str
    migration_path: str
    ancient_association: str

@dataclass
class HealthRiskResult:
    """Polygenic health risk result"""
    condition: str
    risk_level: str
    percentile: float
    markers_analyzed: int
    recommendations: List[str]

@dataclass
class CarrierResult:
    """Carrier status for recessive diseases"""
    condition: str
    status: str
    description: str
    inheritance: str
    population_frequency: str
    markers_found: int

@dataclass
class ComprehensiveResults:
    """Complete DNA analysis results"""
    ancestry: Dict[str, Any]
    physical_traits: Dict[str, TraitResult]
    health_traits: Dict[str, Any]
    pharmacogenomics: Dict[str, PharmacogeneticResult]
    haplogroups: Dict[str, HaplogroupResult]
    immunity: Dict[str, Any]
    longevity: Dict[str, Any]
    nutrition_fitness: Dict[str, Any]
    climate_adaptation: Dict[str, Any]
    polygenic_scores: Dict[str, HealthRiskResult]
    ancient_dna: Dict[str, Any]
    carrier_status: Dict[str, CarrierResult]
    blood_type: Dict[str, Any]
    athletic_genetics: Dict[str, Any]
    adaptation: Dict[str, Any]
    # New advanced traits
    facial_features: Dict[str, Any]
    chronotype: Dict[str, Any]
    pain_sensitivity: Dict[str, Any]
    addiction_risk: Dict[str, Any]
    mental_traits: Dict[str, Any]
    sensory_traits: Dict[str, Any]
    ancient_population_match: Dict[str, Any]
    personalized_plan: Dict[str, Any]
    summary: Dict[str, Any]
    # Behavioral & cognitive genetics
    behavioral_genetics: Dict[str, Any] = field(default_factory=dict)
    # Sleep & circadian genetics
    sleep_genetics: Dict[str, Any] = field(default_factory=dict)
    # Expanded physical traits
    physical_traits_expanded: Dict[str, Any] = field(default_factory=dict)
    # Sports & injury genetics
    sports_genetics: Dict[str, Any] = field(default_factory=dict)
    # Reproduction & fertility genetics
    reproduction_genetics: Dict[str, Any] = field(default_factory=dict)
    # Immune system deep dive
    immune_deep_genetics: Dict[str, Any] = field(default_factory=dict)
    # Nutrition & metabolism
    nutrition_metabolism: Dict[str, Any] = field(default_factory=dict)
    # Ancient DNA & history
    ancient_dna_history: Dict[str, Any] = field(default_factory=dict)
    # Longevity genetics
    longevity_genetics: Dict[str, Any] = field(default_factory=dict)
    # Pharmacogenomics - drug metabolism
    pharmacogenomics_detailed: Dict[str, Any] = field(default_factory=dict)
    # Mental health genetics
    mental_health_genetics: Dict[str, Any] = field(default_factory=dict)
    # Cancer risk genetics
    cancer_risk_genetics: Dict[str, Any] = field(default_factory=dict)
    # Cardiovascular genetics
    cardiovascular_genetics: Dict[str, Any] = field(default_factory=dict)
    # Skin & dermatology genetics
    skin_dermatology: Dict[str, Any] = field(default_factory=dict)
    # Deep ancestry genetics
    deep_ancestry: Dict[str, Any] = field(default_factory=dict)
    # Unique features
    unique_features: Dict[str, Any] = field(default_factory=dict)


# Note: REFERENCE_POPULATIONS (177 regions) imported from reference_populations.py




# =============================================================================
# PHYSICAL TRAITS DATABASE
# =============================================================================

PHYSICAL_TRAITS = {
    'eye_color': {
        'rs12913832': {
            'GG': {'prediction': 'Blue/Green', 'confidence': 0.85},
            'AG': {'prediction': 'Green/Hazel', 'confidence': 0.70},
            'AA': {'prediction': 'Brown', 'confidence': 0.80}
        },
        'rs1800407': {
            'TT': {'prediction': 'Blue (modifier)', 'confidence': 0.75},
            'CT': {'prediction': 'Green/Hazel (modifier)', 'confidence': 0.60},
            'CC': {'prediction': 'Brown likely', 'confidence': 0.50}
        }
    },
    'hair_color': {
        'rs1805007': {
            'TT': {'prediction': 'Red hair', 'confidence': 0.90},
            'CT': {'prediction': 'Red hair carrier', 'confidence': 0.70},
            'CC': {'prediction': 'Non-red hair', 'confidence': 0.85}
        },
        'rs12821256': {
            'TT': {'prediction': 'Blonde hair likely', 'confidence': 0.75},
            'CT': {'prediction': 'Light brown possible', 'confidence': 0.60},
            'CC': {'prediction': 'Dark hair likely', 'confidence': 0.70}
        }
    },
    'skin_pigmentation': {
        'rs1426654': {
            'AA': {'prediction': 'Light skin', 'confidence': 0.90},
            'AG': {'prediction': 'Intermediate skin', 'confidence': 0.75},
            'GG': {'prediction': 'Dark skin', 'confidence': 0.85}
        },
        'rs16891982': {
            'GG': {'prediction': 'Light skin', 'confidence': 0.85},
            'CG': {'prediction': 'Intermediate skin', 'confidence': 0.70},
            'CC': {'prediction': 'Dark skin', 'confidence': 0.80}
        }
    },
    'freckling': {
        'rs1805007': {
            'TT': {'prediction': 'Heavy freckling likely', 'confidence': 0.85},
            'CT': {'prediction': 'Moderate freckling', 'confidence': 0.65},
            'CC': {'prediction': 'Minimal freckling', 'confidence': 0.60}
        }
    },
    'hair_texture': {
        'rs3827760': {
            'AA': {'prediction': 'Thick, straight hair', 'confidence': 0.85},
            'AG': {'prediction': 'Medium thickness', 'confidence': 0.65},
            'GG': {'prediction': 'Normal thickness', 'confidence': 0.60}
        }
    },
    'male_pattern_baldness': {
        'rs2180439': {
            'TT': {'prediction': 'Higher baldness risk', 'confidence': 0.70},
            'CT': {'prediction': 'Moderate baldness risk', 'confidence': 0.55},
            'CC': {'prediction': 'Lower baldness risk', 'confidence': 0.60}
        }
    },
    'earwax_type': {
        'rs17822931': {
            'TT': {'prediction': 'Dry earwax', 'confidence': 0.95},
            'CT': {'prediction': 'Wet earwax', 'confidence': 0.85},
            'CC': {'prediction': 'Wet earwax', 'confidence': 0.95}
        }
    },
    'bitter_taste_perception': {
        'rs713598': {
            'CC': {'prediction': 'Supertaster (bitter sensitive)', 'confidence': 0.85},
            'CG': {'prediction': 'Medium taster', 'confidence': 0.70},
            'GG': {'prediction': 'Non-taster', 'confidence': 0.80}
        }
    },
    'cilantro_preference': {
        'rs72921001': {
            'AA': {'prediction': 'Cilantro tastes like soap', 'confidence': 0.70},
            'AC': {'prediction': 'May dislike cilantro', 'confidence': 0.55},
            'CC': {'prediction': 'Normal cilantro taste', 'confidence': 0.60}
        }
    }
}


# =============================================================================
# HEALTH TRAITS DATABASE
# =============================================================================

HEALTH_TRAITS = {
    'lactose_tolerance': {
        'rs4988235': {
            'TT': {'status': 'Lactose tolerant', 'description': 'Can digest lactose as adult'},
            'CT': {'status': 'Partially tolerant', 'description': 'Some lactose tolerance'},
            'CC': {'status': 'Lactose intolerant', 'description': 'Cannot digest lactose well'}
        }
    },
    'caffeine_metabolism': {
        'rs762551': {
            'AA': {'status': 'Fast metabolizer', 'description': 'Metabolizes caffeine quickly'},
            'AC': {'status': 'Normal metabolizer', 'description': 'Average caffeine metabolism'},
            'CC': {'status': 'Slow metabolizer', 'description': 'Caffeine stays longer in system'}
        }
    },
    'alcohol_flush': {
        'rs671': {
            'AA': {'status': 'Flush reaction', 'description': 'Cannot metabolize acetaldehyde'},
            'AG': {'status': 'Partial flush', 'description': 'Mild flush reaction possible'},
            'GG': {'status': 'No flush', 'description': 'Normal alcohol metabolism'}
        }
    },
    'muscle_fiber_type': {
        'rs1815739': {
            'CC': {'status': 'Power/Sprint athlete', 'description': 'Fast-twitch muscle fibers'},
            'CT': {'status': 'Mixed muscle type', 'description': 'Balanced fiber types'},
            'TT': {'status': 'Endurance athlete', 'description': 'Slow-twitch muscle fibers dominant'}
        }
    },
    'vitamin_d_levels': {
        'rs2282679': {
            'AA': {'status': 'Normal vitamin D', 'description': 'Normal vitamin D binding'},
            'AC': {'status': 'Slightly lower', 'description': 'May need more vitamin D'},
            'CC': {'status': 'Lower levels', 'description': 'Often has lower vitamin D levels'}
        }
    },
    'folate_metabolism': {
        'rs1801133': {
            'CC': {'status': 'Normal MTHFR', 'description': 'Normal folate metabolism'},
            'CT': {'status': 'Heterozygous MTHFR', 'description': 'Slightly reduced efficiency'},
            'TT': {'status': 'Homozygous MTHFR', 'description': 'Reduced folate conversion'}
        }
    },
    'type2_diabetes_risk': {
        'rs7903146': {
            'CC': {'status': 'Lower risk', 'description': 'Reduced T2D risk'},
            'CT': {'status': 'Average risk', 'description': 'Moderate T2D risk'},
            'TT': {'status': 'Higher risk', 'description': 'Increased T2D risk'}
        }
    },
    'clotting_factor_v': {
        'rs6025': {
            'GG': {'status': 'Normal clotting', 'description': 'No Factor V Leiden'},
            'AG': {'status': 'Carrier', 'description': 'Heterozygous Factor V Leiden'},
            'AA': {'status': 'Elevated risk', 'description': 'Homozygous Factor V Leiden'}
        }
    }
}


# =============================================================================
# PHARMACOGENOMICS DATABASE
# =============================================================================

PHARMACOGENOMICS = {
    'CYP2D6': {
        'description': 'Drug metabolism enzyme - processes many medications',
        'drugs': ['Codeine', 'Tramadol', 'Metoprolol', 'Antidepressants'],
        'markers': {
            'rs3892097': {
                'AA': {'phenotype': 'Normal Metabolizer', 'activity': 1.0},
                'AG': {'phenotype': 'Intermediate Metabolizer', 'activity': 0.5},
                'GG': {'phenotype': 'Poor Metabolizer', 'activity': 0.0}
            }
        }
    },
    'CYP2C19': {
        'description': 'Metabolizes PPIs, antidepressants, clopidogrel',
        'drugs': ['Clopidogrel', 'Omeprazole', 'Escitalopram'],
        'markers': {
            'rs4244285': {
                'GG': {'phenotype': 'Normal Metabolizer', 'activity': 1.0},
                'GA': {'phenotype': 'Intermediate Metabolizer', 'activity': 0.5},
                'AA': {'phenotype': 'Poor Metabolizer', 'activity': 0.0}
            },
            'rs12248560': {
                'CC': {'phenotype': 'Normal Metabolizer', 'activity': 1.0},
                'CT': {'phenotype': 'Rapid Metabolizer', 'activity': 1.5},
                'TT': {'phenotype': 'Ultra-rapid Metabolizer', 'activity': 2.0}
            }
        }
    },
    'VKORC1': {
        'description': 'Warfarin sensitivity',
        'drugs': ['Warfarin'],
        'markers': {
            'rs9923231': {
                'GG': {'phenotype': 'High Sensitivity', 'activity': 0.5},
                'GT': {'phenotype': 'Intermediate', 'activity': 0.75},
                'TT': {'phenotype': 'Normal Sensitivity', 'activity': 1.0}
            }
        }
    },
    'SLCO1B1': {
        'description': 'Statin transport - affects statin side effects',
        'drugs': ['Simvastatin', 'Atorvastatin'],
        'markers': {
            'rs4149056': {
                'TT': {'phenotype': 'Normal Function', 'activity': 1.0},
                'TC': {'phenotype': 'Decreased Function', 'activity': 0.6},
                'CC': {'phenotype': 'Poor Function', 'activity': 0.2}
            }
        }
    },
    'DPYD': {
        'description': 'Fluoropyrimidine metabolism - cancer drugs',
        'drugs': ['5-Fluorouracil', 'Capecitabine'],
        'markers': {
            'rs3918290': {
                'CC': {'phenotype': 'Normal Metabolizer', 'activity': 1.0},
                'CT': {'phenotype': 'Intermediate Metabolizer', 'activity': 0.5},
                'TT': {'phenotype': 'Poor Metabolizer', 'activity': 0.0}
            }
        }
    }
}


# =============================================================================
# HAPLOGROUP MARKERS
# =============================================================================

MTDNA_HAPLOGROUPS = {
    'H': {'markers': ['rs2032658', 'rs3928306'], 'origin': 'Europe', 'freq': 0.45},
    'U': {'markers': ['rs41323649'], 'origin': 'Western Eurasia', 'freq': 0.15},
    'K': {'markers': ['rs8896'], 'origin': 'Near East', 'freq': 0.10},
    'J': {'markers': ['rs2853499'], 'origin': 'Near East', 'freq': 0.12},
    'T': {'markers': ['rs41456348'], 'origin': 'Near East', 'freq': 0.08},
    'L': {'markers': ['rs2853515'], 'origin': 'Africa', 'freq': 0.05},
    'A': {'markers': ['rs3928305'], 'origin': 'East Asia/Americas', 'freq': 0.03},
    'B': {'markers': ['rs8896'], 'origin': 'East Asia/Oceania', 'freq': 0.03}
}

YDNA_HAPLOGROUPS = {
    'R1b': {'markers': ['rs9786184'], 'origin': 'Western Europe', 'freq': 0.50},
    'R1a': {'markers': ['rs17250535'], 'origin': 'Eastern Europe/South Asia', 'freq': 0.15},
    'I': {'markers': ['rs2032597'], 'origin': 'Northern Europe', 'freq': 0.20},
    'J': {'markers': ['rs9341296'], 'origin': 'Middle East', 'freq': 0.08},
    'E': {'markers': ['rs2032652'], 'origin': 'Africa', 'freq': 0.05},
    'G': {'markers': ['rs2032636'], 'origin': 'Caucasus', 'freq': 0.02},
    'N': {'markers': ['rs9341301'], 'origin': 'Northern Eurasia', 'freq': 0.03},
    'O': {'markers': ['rs2032595'], 'origin': 'East Asia', 'freq': 0.02}
}


# =============================================================================
# IMMUNITY AND PATHOGEN RESISTANCE
# =============================================================================

IMMUNITY_MARKERS = {
    'hiv_resistance': {
        'rs333': {
            'II': {'resistance': 'None', 'description': 'Normal CCR5 receptor'},
            'ID': {'resistance': 'Partial', 'description': 'Heterozygous CCR5-delta32'},
            'DD': {'resistance': 'Strong', 'description': 'Homozygous CCR5-delta32 (rare)'}
        }
    },
    'malaria_resistance': {
        'rs334': {
            'TT': {'resistance': 'None', 'sickle': 'Normal hemoglobin'},
            'AT': {'resistance': 'High', 'sickle': 'Carrier (trait) - malaria resistant'},
            'TA': {'resistance': 'High', 'sickle': 'Carrier (trait) - malaria resistant'},
            'AA': {'resistance': 'Very High', 'sickle': 'Sickle cell disease (requires medical care)'}
        }
    },
    'norovirus_resistance': {
        'rs601338': {
            'GG': {'resistance': 'High', 'description': 'Non-secretor - norovirus resistant'},
            'AG': {'resistance': 'Partial', 'description': 'Heterozygous secretor'},
            'AA': {'resistance': 'None', 'description': 'Secretor - susceptible'}
        }
    },
    'hla_b27': {
        'rs4349859': {
            'AA': {'status': 'HLA-B*27 Positive', 'autoimmune_risk': 'Elevated'},
            'AG': {'status': 'Heterozygous', 'autoimmune_risk': 'Moderate'},
            'GG': {'status': 'HLA-B*27 Negative', 'autoimmune_risk': 'Normal'}
        }
    }
}


# =============================================================================
# LONGEVITY AND AGING MARKERS (Now imported from expanded_genetics_database.py)
# See LONGEVITY_MARKERS import at top of file for expanded 15+ marker database
# =============================================================================


# =============================================================================
# NUTRITION AND FITNESS MARKERS
# =============================================================================

NUTRITION_MARKERS = {
    'vitamin_d_binding': {
        'rs2282679': {
            'AA': {'need': 'Normal', 'recommendation': 'Standard intake'},
            'AC': {'need': 'Slightly increased', 'recommendation': 'Higher intake may help'},
            'CC': {'need': 'Increased', 'recommendation': 'Consider supplementation'}
        }
    },
    'folate_requirement': {
        'rs1801133': {
            'CC': {'need': 'Normal', 'form': 'Any folate form'},
            'CT': {'need': 'Slightly increased', 'form': 'Methylfolate preferred'},
            'TT': {'need': 'Increased', 'form': 'Methylfolate required'}
        }
    },
    'iron_absorption': {
        'rs1800562': {
            'GG': {'absorption': 'Normal', 'risk': 'None'},
            'AG': {'absorption': 'Increased', 'risk': 'Monitor iron levels'},
            'AA': {'absorption': 'High', 'risk': 'Hemochromatosis risk'}
        }
    },
    'omega3_conversion': {
        'rs174546': {
            'CC': {'conversion': 'High', 'recommendation': 'Plant omega-3 may suffice'},
            'CT': {'conversion': 'Moderate', 'recommendation': 'Some fish oil beneficial'},
            'TT': {'conversion': 'Low', 'recommendation': 'Direct fish oil recommended'}
        }
    }
}

FITNESS_MARKERS = {
    'actn3': {
        'rs1815739': {
            'CC': {'type': 'Power/Sprint', 'focus': 'Explosive movements'},
            'CT': {'type': 'Mixed', 'focus': 'Balanced training'},
            'TT': {'type': 'Endurance', 'focus': 'Aerobic activities'}
        }
    },
    'ace': {
        'rs4340': {
            'II': {'type': 'Endurance', 'vo2max': 'Higher potential'},
            'ID': {'type': 'Mixed', 'vo2max': 'Average potential'},
            'DD': {'type': 'Power', 'vo2max': 'Power focus'}
        }
    },
    'injury_risk': {
        'rs1800012': {
            'GG': {'risk': 'Lower', 'collagen': 'Strong'},
            'GT': {'risk': 'Moderate', 'collagen': 'Normal'},
            'TT': {'risk': 'Higher', 'collagen': 'Monitor carefully'}
        }
    }
}


# =============================================================================
# CLIMATE ADAPTATION MARKERS
# =============================================================================

CLIMATE_MARKERS = {
    'altitude_adaptation': {
        'rs11689011': {
            'AA': {'adaptation': 'High altitude adapted', 'description': 'EPAS1 variant'},
            'AG': {'adaptation': 'Partial adaptation', 'description': 'Heterozygous'},
            'GG': {'adaptation': 'Not adapted', 'description': 'Normal oxygen processing'}
        }
    },
    'cold_tolerance': {
        'rs1800592': {
            'AA': {'tolerance': 'Enhanced', 'thermogenesis': 'High'},
            'AG': {'tolerance': 'Moderate', 'thermogenesis': 'Normal'},
            'GG': {'tolerance': 'Lower', 'thermogenesis': 'Reduced'}
        }
    },
    'uv_protection': {
        'rs1126809': {
            'GG': {'protection': 'High', 'melanin': 'Efficient production'},
            'AG': {'protection': 'Moderate', 'melanin': 'Normal production'},
            'AA': {'protection': 'Lower', 'melanin': 'Less efficient'}
        }
    }
}


# =============================================================================
# ANCIENT DNA CONNECTIONS
# =============================================================================

ANCIENT_DNA_COMPONENTS = {
    'western_hunter_gatherer': {
        'description': 'Mesolithic European hunter-gatherers',
        'time_period': '15,000 - 8,000 years ago',
        'markers': ['rs12913832', 'rs16891982'],
        'typical_percentage': {'European': 15, 'Other': 2}
    },
    'early_european_farmer': {
        'description': 'Neolithic Anatolian farmers',
        'time_period': '8,000 - 5,000 years ago',
        'markers': ['rs1426654', 'rs4988235'],
        'typical_percentage': {'European': 35, 'Middle_Eastern': 40, 'Other': 5}
    },
    'yamnaya_steppe': {
        'description': 'Bronze Age steppe pastoralists',
        'time_period': '5,000 - 3,000 years ago',
        'markers': ['rs4988235', 'rs16891982'],
        'typical_percentage': {'European': 35, 'South_Asian': 15, 'Other': 3}
    },
    'east_asian_ancient': {
        'description': 'Ancient East Asian populations',
        'time_period': '40,000+ years ago',
        'markers': ['rs3827760', 'rs671'],
        'typical_percentage': {'East_Asian': 95, 'Native_American': 70, 'Other': 2}
    },
    'african_ancient': {
        'description': 'Ancient African populations',
        'time_period': '200,000+ years ago',
        'markers': ['rs1426654', 'rs334'],
        'typical_percentage': {'African': 98, 'Other': 5}
    }
}


# =============================================================================
# MAIN ANALYSIS ENGINE CLASS
# =============================================================================

class ComprehensiveDNAAnalysisEngine:
    """Complete DNA analysis engine integrating all modules"""

    def __init__(self):
        self.snp_dict = {}
        self.results = None

    def load_dna_data(self, dna_df: pd.DataFrame):
        """Load DNA data into the engine"""
        self.snp_dict = {}
        for _, row in dna_df.iterrows():
            rsid = row.get('rsid', '')
            genotype = row.get('genotype', '')
            if rsid and genotype:
                self.snp_dict[rsid] = self._standardize_genotype(genotype)

    def _standardize_genotype(self, genotype: str) -> str:
        """Standardize genotype format (alphabetically sorted)"""
        if len(genotype) == 2:
            return ''.join(sorted(genotype))
        return genotype

    def run_full_analysis(self, dna_df: pd.DataFrame) -> ComprehensiveResults:
        """Run all analysis modules including unique features"""
        self.load_dna_data(dna_df)

        # Run standard analysis first
        ancestry = self.analyze_ancestry()
        haplogroups = self.analyze_haplogroups()

        # Run unique features analysis
        from unique_features_analysis import run_unique_features_analysis
        unique_features = run_unique_features_analysis(
            self.snp_dict,
            ancestry_results=ancestry,
            haplogroups=haplogroups,
            chronological_age=30  # Default age, could be user input
        )

        # Run all analysis modules and store for plan generation
        health_traits = self.analyze_health_traits()
        nutrition_fitness = self.analyze_nutrition_fitness()
        athletic_genetics = self.analyze_athletic_genes()
        pharmacogenomics = self.analyze_pharmacogenomics()
        polygenic_scores = self.analyze_polygenic_scores()
        carrier_status = self.analyze_carrier_status()
        longevity = self.analyze_longevity()
        immunity = self.analyze_immunity()
        mental_traits = self.analyze_mental_traits()
        chronotype = self.analyze_chronotype()
        cardiovascular = self.analyze_cardiovascular_genetics()
        cancer_risk = self.analyze_cancer_risk_genetics()
        nutrition_metabolism = self.analyze_nutrition_metabolism()

        # Generate personalized plan with all analysis data
        personalized_plan = self.generate_personalized_plan(
            health_traits=health_traits,
            nutrition_fitness=nutrition_fitness,
            athletic_genetics=athletic_genetics,
            pharmacogenomics=pharmacogenomics,
            polygenic_scores=polygenic_scores,
            carrier_status=carrier_status,
            longevity=longevity,
            immunity=immunity,
            mental_traits=mental_traits,
            chronotype=chronotype,
            cardiovascular=cardiovascular,
            cancer_risk=cancer_risk,
            nutrition_metabolism=nutrition_metabolism
        )

        return ComprehensiveResults(
            ancestry=ancestry,
            physical_traits=self.analyze_physical_traits(),
            health_traits=health_traits,
            pharmacogenomics=pharmacogenomics,
            haplogroups=haplogroups,
            immunity=immunity,
            longevity=longevity,
            nutrition_fitness=nutrition_fitness,
            climate_adaptation=self.analyze_climate_adaptation(),
            polygenic_scores=polygenic_scores,
            ancient_dna=self.analyze_ancient_dna(),
            carrier_status=carrier_status,
            blood_type=self.analyze_blood_type(),
            athletic_genetics=athletic_genetics,
            adaptation=self.analyze_adaptation(),
            # New advanced traits
            facial_features=self.analyze_facial_features(),
            chronotype=chronotype,
            pain_sensitivity=self.analyze_pain_sensitivity(),
            addiction_risk=self.analyze_addiction_risk(),
            mental_traits=mental_traits,
            sensory_traits=self.analyze_sensory_traits(),
            ancient_population_match=self.analyze_ancient_population_match(),
            personalized_plan=personalized_plan,
            summary=self.generate_summary(),
            # Behavioral & cognitive genetics
            behavioral_genetics=self.analyze_behavioral_genetics(),
            # Sleep & circadian genetics
            sleep_genetics=self.analyze_sleep_genetics(),
            # Expanded physical traits
            physical_traits_expanded=self.analyze_physical_traits_expanded(),
            # Sports & injury genetics
            sports_genetics=self.analyze_sports_genetics(),
            # Reproduction & fertility genetics
            reproduction_genetics=self.analyze_reproduction_genetics(),
            # Immune system deep dive
            immune_deep_genetics=self.analyze_immune_deep_genetics(),
            # Nutrition & metabolism
            nutrition_metabolism=self.analyze_nutrition_metabolism(),
            # Ancient DNA & history
            ancient_dna_history=self.analyze_ancient_dna_history(),
            # Longevity genetics
            longevity_genetics=self.analyze_longevity_genetics(),
            # Pharmacogenomics - detailed drug metabolism
            pharmacogenomics_detailed=self.analyze_pharmacogenomics_detailed(),
            # Mental health genetics
            mental_health_genetics=self.analyze_mental_health_genetics(),
            # Cancer risk genetics
            cancer_risk_genetics=self.analyze_cancer_risk_genetics(),
            # Cardiovascular genetics
            cardiovascular_genetics=self.analyze_cardiovascular_genetics(),
            # Skin & dermatology genetics
            skin_dermatology=self.analyze_skin_dermatology(),
            # Deep ancestry genetics
            deep_ancestry=self.analyze_deep_ancestry(),
            # Unique features
            unique_features=unique_features
        )

    # -------------------------------------------------------------------------
    # ANCESTRY ANALYSIS (Rewritten for accuracy)
    # -------------------------------------------------------------------------

    def analyze_ancestry(self) -> Dict:
        """
        Ancestry analysis - DISABLED
        To be redone from scratch with better data sources.
        """
        # Return empty ancestry results
        return {
            'composition': {},
            'regional_summary': {},
            'time_depths': {},
            'confidence': 0,
            'population_details': [],
            'markers_continental': 0,
            'markers_subpop': 0,
        }

    # -------------------------------------------------------------------------
    # PHYSICAL TRAITS ANALYSIS (EXPANDED - 25+ traits)
    # -------------------------------------------------------------------------

    def analyze_physical_traits(self) -> Dict[str, Any]:
        """Analyze physical appearance traits using expanded database"""
        results = {}

        for trait_name, markers in PHYSICAL_TRAITS_EXPANDED.items():
            trait_results = []
            best_confidence = 0
            best_prediction = None
            best_genotype = None
            population_avg = None

            for marker, genotypes in markers.items():
                if marker in self.snp_dict:
                    genotype = self.snp_dict[marker]
                    if genotype in genotypes:
                        data = genotypes[genotype]
                        trait_results.append({
                            'marker': marker,
                            'genotype': genotype,
                            'prediction': data['prediction'],
                            'confidence': data['confidence'],
                            'population_freq': data.get('population_freq', 'N/A')
                        })
                        if data['confidence'] > best_confidence:
                            best_confidence = data['confidence']
                            best_prediction = data['prediction']
                            best_genotype = genotype
                            population_avg = data.get('population_freq')

            if trait_results:
                results[trait_name] = {
                    'trait_name': trait_name.replace('_', ' ').title(),
                    'prediction': best_prediction,
                    'confidence': best_confidence,
                    'genotype': best_genotype,
                    'category': 'Physical Appearance',
                    'markers_analyzed': len(trait_results),
                    'all_markers': trait_results,
                    'population_comparison': f"{population_avg*100:.0f}% of population" if population_avg else None
                }

        return results

    # -------------------------------------------------------------------------
    # HEALTH TRAITS ANALYSIS (EXPANDED - 22+ conditions with actions)
    # -------------------------------------------------------------------------

    def analyze_health_traits(self) -> Dict[str, Any]:
        """Analyze health-related traits with action recommendations"""
        results = {}

        for trait_name, markers in HEALTH_TRAITS_EXPANDED.items():
            trait_findings = []
            primary_status = None
            primary_action = None

            for marker, genotypes in markers.items():
                if marker in self.snp_dict:
                    genotype = self.snp_dict[marker]
                    if genotype in genotypes:
                        data = genotypes[genotype]
                        finding = {
                            'marker': marker,
                            'genotype': genotype,
                            'status': data['status'],
                            'description': data['description'],
                            'action': data.get('action', 'Consult healthcare provider')
                        }
                        trait_findings.append(finding)

                        # Use first finding as primary
                        if primary_status is None:
                            primary_status = data['status']
                            primary_action = data.get('action', '')

            if trait_findings:
                results[trait_name] = {
                    'trait_name': trait_name.replace('_', ' ').title(),
                    'status': primary_status,
                    'action': primary_action,
                    'markers_analyzed': len(trait_findings),
                    'all_findings': trait_findings,
                    'category': 'Health'
                }

        return results

    # -------------------------------------------------------------------------
    # PHARMACOGENOMICS ANALYSIS (EXPANDED - 12 genes with detailed actions)
    # -------------------------------------------------------------------------

    def analyze_pharmacogenomics(self) -> Dict[str, Any]:
        """Analyze drug metabolism genetics with expanded gene database"""
        results = {
            'gene_results': {},
            'drug_recommendations': [],
            'high_priority_alerts': []
        }

        for gene, data in PHARMACOGENOMICS_EXPANDED.items():
            gene_result = {
                'gene': gene,
                'description': data['description'],
                'affected_drugs': data['drugs'],
                'variants': []
            }
            activity_scores = []
            actions = []

            for marker, genotypes in data['markers'].items():
                if marker in self.snp_dict:
                    genotype = self.snp_dict[marker]
                    if genotype in genotypes:
                        variant_data = genotypes[genotype]
                        gene_result['variants'].append({
                            'marker': marker,
                            'genotype': genotype,
                            'phenotype': variant_data['phenotype'],
                            'activity': variant_data['activity'],
                            'action': variant_data.get('action', '')
                        })
                        activity_scores.append(variant_data['activity'])
                        if variant_data.get('action'):
                            actions.append(variant_data['action'])

            if activity_scores:
                avg_activity = np.mean(activity_scores)
                gene_result['overall_activity'] = avg_activity
                gene_result['overall_phenotype'] = self._get_phenotype_from_activity(avg_activity)
                gene_result['primary_action'] = actions[0] if actions else 'Standard dosing'
                results['gene_results'][gene] = gene_result

                # High priority alerts for dangerous combinations
                if avg_activity == 0.0:
                    results['high_priority_alerts'].append({
                        'gene': gene,
                        'alert': f'AVOID or use alternatives',
                        'affected_drugs': data['drugs'],
                        'severity': 'HIGH'
                    })

                # Add recommendations for affected drugs
                if avg_activity < 0.5 or avg_activity > 1.5:
                    for drug in data['drugs']:
                        results['drug_recommendations'].append({
                            'drug': drug,
                            'gene': gene,
                            'phenotype': gene_result['overall_phenotype'],
                            'recommendation': actions[0] if actions else self._get_drug_recommendation(gene, avg_activity)
                        })

        return results

    def _get_phenotype_from_activity(self, activity: float) -> str:
        """Convert activity score to phenotype"""
        if activity >= 1.5:
            return 'Ultra-rapid Metabolizer'
        elif activity >= 1.2:
            return 'Rapid Metabolizer'
        elif activity >= 0.7:
            return 'Normal Metabolizer'
        elif activity >= 0.3:
            return 'Intermediate Metabolizer'
        else:
            return 'Poor Metabolizer'

    def _get_drug_recommendation(self, gene: str, activity: float) -> str:
        """Get drug recommendation based on activity"""
        if activity < 0.3:
            return 'Consider alternative medication or reduced dose'
        elif activity < 0.7:
            return 'May need dose adjustment - consult pharmacist'
        elif activity > 1.5:
            return 'May need higher dose for efficacy - consult physician'
        return 'Standard dosing likely appropriate'

    # -------------------------------------------------------------------------
    # HAPLOGROUP ANALYSIS
    # -------------------------------------------------------------------------

    def analyze_haplogroups(self) -> Dict[str, Any]:
        """Analyze maternal (mtDNA) and paternal (Y-DNA) lineages"""
        results = {
            'mtDNA': self._analyze_mtdna(),
            'Y_DNA': self._analyze_ydna()
        }
        return results

    def _analyze_mtdna(self) -> Dict:
        """Analyze mitochondrial DNA haplogroup"""
        best_match = None
        best_score = 0

        for haplogroup, data in MTDNA_HAPLOGROUPS.items():
            score = sum(1 for m in data['markers'] if m in self.snp_dict)
            if score > best_score:
                best_score = score
                best_match = haplogroup

        if best_match:
            data = MTDNA_HAPLOGROUPS[best_match]
            return {
                'haplogroup': best_match,
                'confidence': min(0.9, 0.5 + best_score * 0.2),
                'origin': data['origin'],
                'description': f"Maternal lineage from {data['origin']}",
                'population_frequency': data['freq']
            }
        return {'haplogroup': 'Unknown', 'confidence': 0.0}

    def _analyze_ydna(self) -> Dict:
        """Analyze Y-chromosome haplogroup"""
        best_match = None
        best_score = 0

        for haplogroup, data in YDNA_HAPLOGROUPS.items():
            score = sum(1 for m in data['markers'] if m in self.snp_dict)
            if score > best_score:
                best_score = score
                best_match = haplogroup

        if best_match:
            data = YDNA_HAPLOGROUPS[best_match]
            return {
                'haplogroup': best_match,
                'confidence': min(0.9, 0.5 + best_score * 0.2),
                'origin': data['origin'],
                'description': f"Paternal lineage from {data['origin']}",
                'population_frequency': data['freq']
            }
        return {'haplogroup': 'Unknown (or female sample)', 'confidence': 0.0}

    # -------------------------------------------------------------------------
    # IMMUNITY ANALYSIS (EXPANDED - 9 conditions with actions)
    # -------------------------------------------------------------------------

    def analyze_immunity(self) -> Dict[str, Any]:
        """Analyze immunity and pathogen resistance with expanded markers"""
        results = {
            'pathogen_resistance': [],
            'autoimmune_markers': [],
            'disease_susceptibility': [],
            'recommendations': []
        }

        for trait_name, markers in IMMUNITY_EXPANDED.items():
            for marker, genotypes in markers.items():
                if marker in self.snp_dict:
                    genotype = self.snp_dict[marker]
                    if genotype in genotypes:
                        data = genotypes[genotype]

                        # Pathogen resistance (HIV, malaria, norovirus, etc.)
                        if 'resistance' in data:
                            results['pathogen_resistance'].append({
                                'pathogen': trait_name.replace('_', ' ').title(),
                                'resistance': data['resistance'],
                                'description': data.get('description', data.get('sickle', '')),
                                'action': data.get('action', ''),
                                'marker': marker,
                                'genotype': genotype
                            })

                        # Disease risk/susceptibility (COVID, TB, etc.)
                        if 'risk' in data or 'susceptibility' in data:
                            results['disease_susceptibility'].append({
                                'condition': trait_name.replace('_', ' ').title(),
                                'risk': data.get('risk', data.get('susceptibility', '')),
                                'description': data.get('description', ''),
                                'action': data.get('action', ''),
                                'marker': marker,
                                'genotype': genotype
                            })

                        # Autoimmune markers (HLA-B27, lupus, celiac HLA)
                        if 'status' in data:
                            results['autoimmune_markers'].append({
                                'marker_name': trait_name.replace('_', ' ').title(),
                                'status': data['status'],
                                'risk': data.get('risk', data.get('autoimmune_risk', '')),
                                'action': data.get('action', ''),
                                'marker': marker,
                                'genotype': genotype
                            })

                        # Response markers (Hepatitis B clearance, etc.)
                        if 'response' in data:
                            results['pathogen_resistance'].append({
                                'pathogen': trait_name.replace('_', ' ').title(),
                                'resistance': data['response'],
                                'description': data.get('description', ''),
                                'action': data.get('action', ''),
                                'marker': marker,
                                'genotype': genotype
                            })

        return results

    # -------------------------------------------------------------------------
    # LONGEVITY ANALYSIS (Expanded - 15+ markers)
    # -------------------------------------------------------------------------

    def analyze_longevity(self) -> Dict[str, Any]:
        """Analyze longevity and aging genetics using expanded database"""
        results = {
            'aging_factors': [],
            'overall_score': 50,
            'longevity_variants': 0,
            'centenarian_variants': 0,
            'genes_analyzed': [],
            'recommendations': []
        }

        longevity_scores = []
        markers_found = 0

        for rsid, marker_data in LONGEVITY_MARKERS_FIXED.items():
            if rsid in self.snp_dict:
                genotype = self.snp_dict[rsid]
                markers_found += 1

                if genotype in marker_data:
                    data = marker_data[genotype]
                    gene = marker_data.get('gene', 'Unknown')
                    description = marker_data.get('description', '')

                    # Use score directly from LONGEVITY_MARKERS_FIXED
                    score = data.get('score', 50)
                    if not isinstance(score, (int, float)):
                        score = 50

                    longevity_scores.append(min(100, max(0, score)))

                    # Track centenarian-enriched variants
                    is_centenarian = data.get('centenarian_enriched', False)
                    if is_centenarian:
                        results['centenarian_variants'] += 1

                    # Check if it's a longevity-associated variant
                    effect = data.get('effect', '')
                    if 'longevity' in effect.lower() or score >= 60:
                        results['longevity_variants'] += 1

                    results['aging_factors'].append({
                        'gene': gene,
                        'rsid': rsid,
                        'genotype': genotype,
                        'effect': effect,
                        'description': description,
                        'score': round(score, 1),
                        'centenarian_enriched': is_centenarian,
                        'details': {k: v for k, v in data.items() if k not in ['effect', 'odds_ratio', 'centenarian_enriched']}
                    })

                    if gene not in results['genes_analyzed']:
                        results['genes_analyzed'].append(gene)

        if longevity_scores:
            results['overall_score'] = round(np.mean(longevity_scores), 1)
            results['markers_analyzed'] = markers_found
            results['total_markers'] = len(LONGEVITY_MARKERS_FIXED)

            if results['overall_score'] >= 70:
                results['category'] = 'Excellent longevity genetics'
                results['interpretation'] = 'You carry multiple variants associated with exceptional longevity'
            elif results['overall_score'] >= 60:
                results['category'] = 'Good longevity genetics'
                results['interpretation'] = 'You have favorable longevity genetics'
            elif results['overall_score'] >= 50:
                results['category'] = 'Average longevity genetics'
                results['interpretation'] = 'Your longevity genetics are typical'
            else:
                results['category'] = 'Focus on lifestyle factors'
                results['interpretation'] = 'Lifestyle factors are especially important for your longevity'

            results['recommendations'] = [
                'Exercise: 150+ min moderate or 75+ min vigorous weekly',
                'Diet: Mediterranean or MIND diet pattern - rich in vegetables, olive oil, fish',
                'Sleep: 7-9 hours quality sleep supports cellular repair and telomere maintenance',
                'Stress: Chronic stress shortens telomeres - meditation, social connection help',
                'Fasting: Intermittent fasting may activate SIRT1/FOXO3 longevity pathways',
                'Social: Strong social connections consistently associated with longevity',
                'Purpose: Having meaning/purpose in life associated with longer lifespan',
                'Supplements to consider: Vitamin D, Omega-3, NAD+ precursors (based on your genetics)'
            ]

            # Add gene-specific recommendations
            for factor in results['aging_factors']:
                if factor['gene'] == 'FOXO3' and factor['score'] < 50:
                    results['recommendations'].append('FOXO3: Caloric restriction and exercise activate this pathway')
                if factor['gene'] == 'SIRT1' and factor['score'] < 50:
                    results['recommendations'].append('SIRT1: Resveratrol and NAD+ precursors may help')
                if factor['gene'] == 'SOD2' and 'Lower' in str(factor.get('details', {})):
                    results['recommendations'].append('SOD2: Consider antioxidant supplementation (vitamin C, E)')

        return results

    # -------------------------------------------------------------------------
    # NUTRITION AND FITNESS ANALYSIS (EXPANDED - 11 nutrition, 7 fitness markers)
    # -------------------------------------------------------------------------

    def analyze_nutrition_fitness(self) -> Dict[str, Any]:
        """Analyze nutrition and fitness genetics with expanded markers"""
        results = {
            'nutrition': {},
            'fitness': {},
            'diet_recommendations': [],
            'exercise_recommendations': [],
            'supplement_recommendations': []
        }

        # Nutrition analysis with expanded markers
        for trait_name, markers in NUTRITION_EXPANDED.items():
            for marker, genotypes in markers.items():
                if marker in self.snp_dict:
                    genotype = self.snp_dict[marker]
                    if genotype in genotypes:
                        data = genotypes[genotype]
                        results['nutrition'][trait_name] = {
                            'trait_name': trait_name.replace('_', ' ').title(),
                            'need': data.get('need', data.get('sensitivity', data.get('absorption', data.get('conversion', data.get('response', 'Unknown'))))),
                            'recommendation': data.get('recommendation', data.get('action', '')),
                            'food_source': data.get('food', data.get('source', '')),
                            'dose': data.get('dose', data.get('target', '')),
                            'form': data.get('form', ''),
                            'marker': marker,
                            'genotype': genotype
                        }

                        # Generate supplement recommendations
                        if 'recommendation' in data and ('supplement' in data['recommendation'].lower() or 'IU' in str(data.get('dose', ''))):
                            results['supplement_recommendations'].append({
                                'nutrient': trait_name.replace('_', ' ').title(),
                                'recommendation': data['recommendation'],
                                'dose': data.get('dose', '')
                            })

        # Fitness analysis with expanded markers
        for trait_name, markers in FITNESS_EXPANDED.items():
            for marker, genotypes in markers.items():
                if marker in self.snp_dict:
                    genotype = self.snp_dict[marker]
                    if genotype in genotypes:
                        data = genotypes[genotype]
                        results['fitness'][trait_name] = {
                            'trait_name': trait_name.replace('_', ' ').title(),
                            'type': data.get('type', data.get('recovery', data.get('response', data.get('growth', data.get('potential', 'Unknown'))))),
                            'description': data.get('strength', data.get('vo2max', data.get('collagen', data.get('adaptation', data.get('fat_oxidation', data.get('myostatin', data.get('bp_effect', ''))))))),
                            'training_focus': data.get('training', data.get('rest', data.get('action', ''))),
                            'marker': marker,
                            'genotype': genotype
                        }

        # Generate exercise recommendations based on fitness markers
        if 'power_vs_endurance' in results['fitness']:
            muscle_type = results['fitness']['power_vs_endurance']['type']
            training = results['fitness']['power_vs_endurance'].get('training_focus', '')
            if muscle_type == 'Power/Sprint':
                results['exercise_recommendations'].append(f'Your genetics favor explosive power. {training}')
            elif muscle_type == 'Endurance':
                results['exercise_recommendations'].append(f'Your genetics favor endurance. {training}')
            else:
                results['exercise_recommendations'].append(f'Versatile genetics - balanced training beneficial. {training}')

        if 'injury_risk' in results['fitness']:
            risk = results['fitness']['injury_risk']['type']
            action = results['fitness']['injury_risk'].get('training_focus', '')
            if 'Higher' in str(risk):
                results['exercise_recommendations'].append(f'Increased injury risk detected. {action}')

        if 'recovery_speed' in results['fitness']:
            recovery = results['fitness']['recovery_speed']['type']
            rest_advice = results['fitness']['recovery_speed'].get('training_focus', '')
            results['exercise_recommendations'].append(f'{recovery} recovery: {rest_advice}')

        return results

    # -------------------------------------------------------------------------
    # CLIMATE ADAPTATION ANALYSIS
    # -------------------------------------------------------------------------

    def analyze_climate_adaptation(self) -> Dict[str, Any]:
        """Analyze climate adaptation genetics"""
        results = {
            'adaptations': [],
            'recommendations': []
        }

        for trait_name, markers in CLIMATE_MARKERS.items():
            for marker, genotypes in markers.items():
                if marker in self.snp_dict:
                    genotype = self.snp_dict[marker]
                    if genotype in genotypes:
                        data = genotypes[genotype]
                        results['adaptations'].append({
                            'trait': trait_name.replace('_', ' ').title(),
                            'adaptation': data.get('adaptation', data.get('tolerance', data.get('protection', 'Unknown'))),
                            'description': data.get('description', data.get('thermogenesis', data.get('melanin', ''))),
                            'marker': marker
                        })

        return results

    # -------------------------------------------------------------------------
    # POLYGENIC SCORES (100+ markers per condition)
    # -------------------------------------------------------------------------

    def analyze_polygenic_scores(self) -> Dict[str, Any]:
        """Calculate polygenic risk scores using 100s of markers per condition"""
        results = {}

        for condition_id, condition_data in POLYGENIC_RISK_SCORES.items():
            markers = condition_data['markers']
            score = 0.0
            markers_found = 0
            risk_alleles = 0
            marker_details = []

            for rsid, marker_info in markers.items():
                if rsid in self.snp_dict:
                    genotype = self.snp_dict[rsid]
                    markers_found += 1
                    risk_allele = marker_info['risk_allele']
                    weight = marker_info['weight']

                    # Count risk alleles
                    allele_count = genotype.count(risk_allele)
                    if allele_count > 0:
                        risk_alleles += allele_count
                        score += weight * allele_count

                        marker_details.append({
                            'rsid': rsid,
                            'genotype': genotype,
                            'risk_allele': risk_allele,
                            'copies': allele_count,
                            'odds_ratio': marker_info['odds_ratio']
                        })

            if markers_found >= 5:  # Need at least 5 markers for meaningful score
                # Calculate percentile (higher score = higher risk)
                # Normalize score to 0-100 range
                max_possible = sum(m['weight'] * 2 for m in markers.values())
                if max_possible > 0:
                    normalized_score = (score / max_possible) * 100
                else:
                    normalized_score = 50

                # Determine risk level
                if normalized_score >= 70:
                    risk_level = 'Significantly elevated'
                    percentile = min(95, 50 + normalized_score * 0.5)
                elif normalized_score >= 55:
                    risk_level = 'Moderately elevated'
                    percentile = 60 + (normalized_score - 55) * 2
                elif normalized_score >= 45:
                    risk_level = 'Average'
                    percentile = 40 + (normalized_score - 45) * 2
                elif normalized_score >= 30:
                    risk_level = 'Below average'
                    percentile = 20 + (normalized_score - 30) * 1.5
                else:
                    risk_level = 'Low'
                    percentile = max(5, normalized_score * 0.7)

                results[condition_id] = {
                    'condition': condition_data['description'],
                    'risk_level': risk_level,
                    'percentile': round(percentile, 0),
                    'score': round(score, 2),
                    'markers_analyzed': markers_found,
                    'total_markers': len(markers),
                    'risk_alleles_found': risk_alleles,
                    'top_risk_markers': sorted(marker_details, key=lambda x: x['odds_ratio'], reverse=True)[:5],
                    'recommendations': condition_data['recommendations']
                }

        return results

    # -------------------------------------------------------------------------
    # ANCIENT DNA ANALYSIS (Neanderthal & Denisovan)
    # -------------------------------------------------------------------------

    def analyze_ancient_dna(self) -> Dict[str, Any]:
        """Analyze Neanderthal and Denisovan ancestry with trait inheritance"""
        results = {
            'neanderthal': {
                'percentage': 0.0,
                'markers_found': 0,
                'markers_tested': len(NEANDERTHAL_SNPS),
                'inherited_traits': [],
                'trait_categories': {}
            },
            'denisovan': {
                'percentage': 0.0,
                'markers_found': 0,
                'markers_tested': len(DENISOVAN_SNPS),
                'inherited_traits': []
            },
            'timeline': HUMAN_MIGRATION_TIMELINE,
            'your_story': []
        }

        # Calculate Neanderthal percentage
        neanderthal_count = 0
        neanderthal_traits = []

        for rsid, snp_data in NEANDERTHAL_SNPS.items():
            if rsid in self.snp_dict:
                genotype = self.snp_dict[rsid]
                neanderthal_allele = snp_data['neanderthal_allele']

                # Check if user carries the Neanderthal allele
                if neanderthal_allele in genotype:
                    neanderthal_count += 1
                    copies = genotype.count(neanderthal_allele)
                    neanderthal_traits.append({
                        'rsid': rsid,
                        'gene': snp_data['gene'],
                        'trait': snp_data['trait'],
                        'function': snp_data['function'],
                        'copies': copies,
                        'genotype': genotype
                    })

        # Calculate both marker match rate and estimated actual ancestry
        if len(NEANDERTHAL_SNPS) > 0:
            marker_pct = (neanderthal_count / len(NEANDERTHAL_SNPS)) * 100
            results['neanderthal']['marker_match_rate'] = round(marker_pct, 1)
            results['neanderthal']['markers_found'] = neanderthal_count
            results['neanderthal']['inherited_traits'] = neanderthal_traits[:20]

            # Estimated actual ancestry (scientific range: 1-4% for non-Africans)
            if marker_pct >= 40:
                results['neanderthal']['percentage'] = 2.5  # Above average
            elif marker_pct >= 25:
                results['neanderthal']['percentage'] = 2.0  # Average
            else:
                results['neanderthal']['percentage'] = 1.5  # Below average

        # Categorize Neanderthal traits
        for category_id, category_data in NEANDERTHAL_TRAIT_CATEGORIES.items():
            category_traits = []
            for trait in neanderthal_traits:
                if trait['rsid'] in category_data['snps']:
                    category_traits.append(trait)

            if category_traits:
                results['neanderthal']['trait_categories'][category_id] = {
                    'name': category_data['name'],
                    'description': category_data['description'],
                    'traits_inherited': len(category_traits),
                    'total_markers': len(category_data['snps']),
                    'examples': category_traits[:3]
                }

        # Calculate Denisovan percentage
        denisovan_count = 0
        denisovan_traits = []

        for rsid, snp_data in DENISOVAN_SNPS.items():
            if rsid in self.snp_dict:
                genotype = self.snp_dict[rsid]
                denisovan_allele = snp_data['denisovan_allele']

                if denisovan_allele in genotype:
                    denisovan_count += 1
                    denisovan_traits.append({
                        'rsid': rsid,
                        'gene': snp_data['gene'],
                        'trait': snp_data['trait'],
                        'function': snp_data['function']
                    })

        # Calculate both marker match rate and estimated actual ancestry
        if len(DENISOVAN_SNPS) > 0:
            marker_pct = (denisovan_count / len(DENISOVAN_SNPS)) * 100
            results['denisovan']['marker_match_rate'] = round(marker_pct, 1)
            results['denisovan']['markers_found'] = denisovan_count
            results['denisovan']['inherited_traits'] = denisovan_traits

            # Estimated actual ancestry (most non-Oceanians: 0-1%, Oceanians: 3-6%)
            if marker_pct >= 50:
                results['denisovan']['percentage'] = 1.0  # Above average for non-Oceanians
            elif marker_pct >= 30:
                results['denisovan']['percentage'] = 0.5  # Some Denisovan
            else:
                results['denisovan']['percentage'] = 0.2  # Trace

        # Build SEPARATE maternal (mtDNA) and paternal (Y-DNA) journeys
        # Your mom and dad had different ancestral paths!

        # Maternal Journey (mtDNA - passed mother to all children)
        maternal_journey = []

        # Get mtDNA haplogroup path if available
        mtdna_hap = self.mtdna_haplogroup if hasattr(self, 'mtdna_haplogroup') else 'Unknown'

        maternal_journey.append({
            'period': '~200,000 years ago',
            'event': 'Mitochondrial Eve',
            'description': 'Your maternal line traces back to a single woman in Africa - the common ancestor of all living humans through maternal lines'
        })

        maternal_journey.append({
            'period': '~70,000 years ago',
            'event': 'Maternal ancestors left Africa',
            'description': 'Your mother\'s mother\'s mother (going back thousands of generations) left Africa'
        })

        # Add mtDNA haplogroup-specific migration
        for haplo, path_data in MTDNA_MIGRATION_PATHS.items():
            if mtdna_hap.startswith(haplo) or haplo in str(mtdna_hap):
                maternal_journey.append({
                    'period': path_data.get('time_period', 'Ancient'),
                    'event': f'Maternal haplogroup {haplo} formed',
                    'description': f"Your maternal line settled in {path_data.get('origin', 'Unknown')}. {path_data.get('migration', '')}"
                })
                break

        if results['neanderthal']['percentage'] > 0.5:
            maternal_journey.append({
                'period': '~60,000 years ago',
                'event': 'Neanderthal mixing (inherited by all children)',
                'description': 'Your maternal ancestors interbred with Neanderthals - this DNA passed to both sons and daughters'
            })

        results['maternal_journey'] = maternal_journey

        # Paternal Journey (Y-DNA - passed father to sons only)
        paternal_journey = []

        # Get Y-DNA haplogroup if available
        ydna_hap = self.ydna_haplogroup if hasattr(self, 'ydna_haplogroup') else 'Unknown'

        paternal_journey.append({
            'period': '~275,000 years ago',
            'event': 'Y-Chromosomal Adam',
            'description': 'Your paternal line traces back to a single man in Africa - the common ancestor of all living humans through paternal lines'
        })

        paternal_journey.append({
            'period': '~70,000 years ago',
            'event': 'Paternal ancestors left Africa',
            'description': 'Your father\'s father\'s father (going back thousands of generations) left Africa'
        })

        # Add Y-DNA haplogroup-specific migration
        for haplo, path_data in YDNA_MIGRATION_PATHS.items():
            if ydna_hap.startswith(haplo) or haplo in str(ydna_hap):
                paternal_journey.append({
                    'period': path_data.get('time_period', 'Ancient'),
                    'event': f'Paternal haplogroup {haplo} formed',
                    'description': f"Your paternal line settled in {path_data.get('origin', 'Unknown')}. {path_data.get('migration', '')}"
                })
                break

        if results['neanderthal']['percentage'] > 0.5:
            paternal_journey.append({
                'period': '~60,000 years ago',
                'event': 'Neanderthal mixing (inherited)',
                'description': 'Your paternal ancestors also interbred with Neanderthals'
            })

        results['paternal_journey'] = paternal_journey

        # Combined story (what you inherit from BOTH parents)
        your_story = []

        your_story.append({
            'period': '~70,000 years ago',
            'event': 'Both lineages left Africa',
            'description': 'Both your maternal and paternal ancestral lines migrated out of Africa, though they may have taken different routes'
        })

        if results['neanderthal']['percentage'] > 0.5:
            your_story.append({
                'period': '~60,000 years ago',
                'event': 'Neanderthal interbreeding',
                'description': f"Ancestors on one or both sides interbred with Neanderthals. "
                              f"You carry {results['neanderthal']['percentage']:.1f}% Neanderthal DNA "
                              f"({len(neanderthal_traits)} inherited traits)."
            })

        if results['denisovan']['percentage'] > 0.1:
            your_story.append({
                'period': '~50,000 years ago',
                'event': 'Denisovan interbreeding',
                'description': f"Some ancestors encountered Denisovans in Asia. "
                              f"You carry {results['denisovan']['percentage']:.1f}% Denisovan DNA."
            })

        your_story.append({
            'period': '~45,000 years ago',
            'event': 'Spread across continents',
            'description': 'Your ancestors spread across Europe and Asia, adapting to new environments'
        })

        your_story.append({
            'period': '~25,000 years ago',
            'event': 'Last Ice Age survival',
            'description': 'Your ancestors survived the Last Glacial Maximum in refugia'
        })

        your_story.append({
            'period': '~10,000 years ago',
            'event': 'Agricultural Revolution',
            'description': 'The shift to farming changed human genetics, diet, and society'
        })

        your_story.append({
            'period': 'Recent history',
            'event': 'Your parents meet',
            'description': 'Two separate lineages (maternal and paternal) that traveled different paths for tens of thousands of years finally merged to create YOU'
        })

        results['your_story'] = your_story

        return results

    # -------------------------------------------------------------------------
    # CARRIER STATUS ANALYSIS (11+ genetic conditions)
    # -------------------------------------------------------------------------

    def analyze_carrier_status(self) -> Dict[str, Any]:
        """
        Comprehensive carrier status analysis for genetic conditions including:
        - Cystic Fibrosis (CFTR)
        - Sickle Cell Disease (HBB)
        - Tay-Sachs Disease (HEXA)
        - Beta Thalassemia (HBB)
        - Spinal Muscular Atrophy (SMN1)
        - Phenylketonuria (PAH)
        - Gaucher Disease (GBA)
        - Hemochromatosis (HFE)
        - G6PD Deficiency (G6PD)
        - Familial Mediterranean Fever (MEFV)
        - Alpha-1 Antitrypsin Deficiency (SERPINA1)
        """
        # Use the comprehensive carrier status analysis module
        comprehensive_results = analyze_carrier_status_comprehensive(self.snp_dict)

        # Also run the legacy analysis for any conditions not in the new database
        legacy_results = self._analyze_carrier_status_legacy()

        # Merge results, preferring comprehensive data
        results = comprehensive_results.copy()

        # Add any legacy carriers not already found
        legacy_conditions = {c.get('condition', '') for c in results.get('carriers_found', [])}
        for carrier in legacy_results.get('carriers_found', []):
            if carrier.get('condition', '') not in legacy_conditions:
                results['carriers_found'].append(carrier)

        # Update summary
        results['summary'] = {
            'total_conditions_tested': len(results.get('conditions_analyzed', [])),
            'carriers_detected': len(results.get('carriers_found', [])),
            'high_risk_detected': len(results.get('high_risk_conditions', [])),
            'clear_conditions': len(results.get('conditions_clear', [])),
            'conditions_tested': len(results.get('conditions_analyzed', [])),
            'affected_detected': len(results.get('high_risk_conditions', []))
        }

        return results

    def _analyze_carrier_status_legacy(self) -> Dict[str, Any]:
        """Legacy carrier status analysis for backward compatibility"""
        results = {
            'conditions': {},
            'carriers_found': [],
            'affected_found': [],
            'summary': {}
        }

        for condition_name, condition_data in CARRIER_STATUS.items():
            condition_result = {
                'condition_name': condition_name.replace('_', ' ').title(),
                'description': condition_data['description'],
                'inheritance': condition_data['inheritance'],
                'population_frequency': condition_data['frequency'],
                'markers_tested': 0,
                'status': 'Not tested',
                'marker_results': []
            }

            worst_status = 'Normal'
            for marker, genotypes in condition_data['markers'].items():
                if marker in self.snp_dict:
                    genotype = self.snp_dict[marker]
                    condition_result['markers_tested'] += 1

                    if genotype in genotypes:
                        data = genotypes[genotype]
                        marker_result = {
                            'marker': marker,
                            'genotype': genotype,
                            'status': data['status'],
                            'description': data['description']
                        }
                        condition_result['marker_results'].append(marker_result)

                        if 'Affected' in data['status'] or 'At risk' in data['status'] or 'Deficient' in data['status'] or 'Major' in data['status']:
                            worst_status = data['status']
                            results['affected_found'].append({
                                'condition': condition_name.replace('_', ' ').title(),
                                'status': data['status'],
                                'description': data['description']
                            })
                        elif 'Carrier' in data['status'] or 'Trait' in data['status'] and worst_status == 'Normal':
                            worst_status = data['status']
                            results['carriers_found'].append({
                                'condition': condition_name.replace('_', ' ').title(),
                                'status': data['status'],
                                'description': data['description'],
                                'population_frequency': condition_data['frequency']
                            })

            if condition_result['markers_tested'] > 0:
                condition_result['status'] = worst_status
                results['conditions'][condition_name] = condition_result

        return results

    # -------------------------------------------------------------------------
    # BLOOD TYPE ANALYSIS (7 blood group systems)
    # -------------------------------------------------------------------------

    def analyze_blood_type(self) -> Dict[str, Any]:
        """Analyze blood type genetics across multiple blood group systems"""
        results = {
            'abo_type': None,
            'rh_factor': None,
            'full_type': None,
            'blood_systems': {},
            'transfusion_notes': [],
            'clinical_significance': []
        }

        # ABO Blood Type
        abo_result = {'o_likely': False, 'a_likely': False, 'b_likely': False}

        for system_name, markers in BLOOD_TYPE_GENETICS.items():
            system_results = {
                'system': system_name.replace('_', ' ').title(),
                'markers_found': [],
                'interpretation': ''
            }

            for rsid, marker_data in markers.items():
                if rsid in self.snp_dict:
                    genotype = self.snp_dict[rsid]
                    if genotype in marker_data:
                        data = marker_data[genotype]
                        system_results['markers_found'].append({
                            'rsid': rsid,
                            'genotype': genotype,
                            'description': marker_data.get('description', ''),
                            'result': data
                        })

                        # Determine ABO type
                        if system_name == 'abo_blood_type':
                            if rsid == 'rs8176719':
                                if 'blood_type' in data:
                                    if data['blood_type'] == 'O':
                                        abo_result['o_likely'] = True
                                    elif 'A' in data['blood_type']:
                                        abo_result['a_likely'] = True
                                    elif 'B' in data['blood_type']:
                                        abo_result['b_likely'] = True
                            elif rsid == 'rs8176746':
                                if data.get('modifier', '') == 'B allele present':
                                    abo_result['b_likely'] = True

                        # Determine Rh factor
                        if system_name == 'rh_factor':
                            if 'rh_status' in data:
                                results['rh_factor'] = data['rh_status']

                        # Duffy system - malaria resistance
                        if system_name == 'duffy_system':
                            if 'malaria' in data:
                                results['clinical_significance'].append({
                                    'system': 'Duffy',
                                    'finding': data['duffy_status'],
                                    'clinical': data['malaria']
                                })

                        # Kell system - transfusion importance
                        if system_name == 'kell_system':
                            if 'K positive' in str(data.get('kell_status', '')):
                                results['transfusion_notes'].append(
                                    'Kell positive (K+) - important for transfusion matching'
                                )

            if system_results['markers_found']:
                results['blood_systems'][system_name] = system_results

        # Determine final ABO type
        if abo_result['o_likely']:
            results['abo_type'] = 'O'
        elif abo_result['a_likely'] and abo_result['b_likely']:
            results['abo_type'] = 'AB'
        elif abo_result['a_likely']:
            results['abo_type'] = 'A'
        elif abo_result['b_likely']:
            results['abo_type'] = 'B'
        else:
            results['abo_type'] = 'Unable to determine'

        # Combine ABO and Rh
        if results['abo_type'] and results['abo_type'] != 'Unable to determine':
            rh = '+' if 'positive' in str(results['rh_factor']).lower() else '-' if 'negative' in str(results['rh_factor']).lower() else '?'
            results['full_type'] = f"{results['abo_type']}{rh}"

        # Add transfusion compatibility info
        abo = results['abo_type']
        if abo == 'O':
            results['transfusion_notes'].append('Universal donor (red blood cells)')
            results['transfusion_notes'].append('Can only receive type O blood')
        elif abo == 'AB':
            results['transfusion_notes'].append('Universal recipient')
            results['transfusion_notes'].append('Can donate to AB recipients only')
        elif abo == 'A':
            results['transfusion_notes'].append('Can donate to A and AB recipients')
            results['transfusion_notes'].append('Can receive from A and O donors')
        elif abo == 'B':
            results['transfusion_notes'].append('Can donate to B and AB recipients')
            results['transfusion_notes'].append('Can receive from B and O donors')

        return results

    # -------------------------------------------------------------------------
    # ATHLETIC GENETICS ANALYSIS (12 performance genes)
    # -------------------------------------------------------------------------

    def analyze_athletic_genes(self) -> Dict[str, Any]:
        """Analyze athletic performance genetics"""
        results = {
            'overall_profile': '',
            'power_score': 50,
            'endurance_score': 50,
            'genes_analyzed': [],
            'sport_recommendations': [],
            'training_recommendations': [],
            'injury_risk': {},
            'recovery_profile': {}
        }

        power_indicators = 0
        endurance_indicators = 0
        total_genes = 0

        for category, markers in ATHLETIC_GENES.items():
            for rsid, marker_data in markers.items():
                if rsid in self.snp_dict:
                    genotype = self.snp_dict[rsid]
                    total_genes += 1

                    if genotype in marker_data:
                        data = marker_data[genotype]
                        gene = marker_data.get('gene', category)
                        description = marker_data.get('description', '')

                        gene_result = {
                            'gene': gene,
                            'category': category.replace('_', ' ').title(),
                            'rsid': rsid,
                            'genotype': genotype,
                            'phenotype': data.get('phenotype', data.get('effect', '')),
                            'details': data
                        }
                        results['genes_analyzed'].append(gene_result)

                        # Score power vs endurance
                        phenotype = str(data.get('phenotype', '')).lower()
                        muscle_type = str(data.get('muscle_type', '')).lower()
                        effect = str(data.get('effect', '')).lower()

                        if 'power' in phenotype or 'sprint' in phenotype or 'fast-twitch' in muscle_type:
                            power_indicators += 1
                        if 'endurance' in phenotype or 'slow-twitch' in muscle_type or 'aerobic' in effect:
                            endurance_indicators += 1

                        # Track injury risk
                        if category == 'injury_risk':
                            risk = data.get('risk', data.get('phenotype', ''))
                            results['injury_risk'][gene] = {
                                'risk_level': risk,
                                'recommendation': data.get('recommendation', '')
                            }

                        # Track recovery
                        if category == 'recovery':
                            results['recovery_profile'] = {
                                'recovery_speed': data.get('phenotype', ''),
                                'recovery_time': data.get('recovery_time', ''),
                                'recommendation': data.get('recommendation', '')
                            }

                        # Get sport recommendations
                        if 'sports' in data:
                            for sport in data['sports']:
                                if sport not in results['sport_recommendations']:
                                    results['sport_recommendations'].append(sport)

                        # Get training recommendations
                        if data.get('recommendation'):
                            results['training_recommendations'].append(
                                f"{gene}: {data['recommendation']}"
                            )

        # Calculate overall profile
        if total_genes > 0:
            results['power_score'] = 50 + (power_indicators - endurance_indicators) * 10
            results['endurance_score'] = 50 + (endurance_indicators - power_indicators) * 10

            # Cap scores
            results['power_score'] = max(20, min(80, results['power_score']))
            results['endurance_score'] = max(20, min(80, results['endurance_score']))

            if results['power_score'] > 60:
                results['overall_profile'] = 'Power/Sprint Athlete'
                results['primary_sports'] = ['Sprinting', 'Weightlifting', 'Football', 'Baseball', 'Jumping events']
            elif results['endurance_score'] > 60:
                results['overall_profile'] = 'Endurance Athlete'
                results['primary_sports'] = ['Marathon', 'Cycling', 'Triathlon', 'Swimming', 'Cross-country']
            else:
                results['overall_profile'] = 'Versatile/Mixed Athlete'
                results['primary_sports'] = ['Soccer', 'Basketball', 'Tennis', 'MMA', 'Team sports']

        return results

    # -------------------------------------------------------------------------
    # ADAPTATION GENETICS (Altitude, Heat, UV)
    # -------------------------------------------------------------------------

    def analyze_adaptation(self) -> Dict[str, Any]:
        """Analyze environmental adaptation genetics"""
        results = {
            'altitude': {
                'adaptation_level': 'Not analyzed',
                'markers': [],
                'recommendations': []
            },
            'heat': {
                'adaptation_level': 'Not analyzed',
                'markers': [],
                'recommendations': []
            },
            'uv': {
                'adaptation_level': 'Not analyzed',
                'markers': [],
                'recommendations': []
            },
            'ancestral_environment': ''
        }

        altitude_score = 0
        heat_score = 0
        uv_score = 0

        for category, markers in ADAPTATION_GENETICS.items():
            for rsid, marker_data in markers.items():
                if rsid in self.snp_dict:
                    genotype = self.snp_dict[rsid]

                    if genotype in marker_data:
                        data = marker_data[genotype]
                        gene = marker_data.get('gene', '')
                        description = marker_data.get('description', '')

                        marker_result = {
                            'gene': gene,
                            'rsid': rsid,
                            'genotype': genotype,
                            'description': description,
                            'effect': data
                        }

                        if category == 'altitude_adaptation':
                            results['altitude']['markers'].append(marker_result)
                            adaptation = data.get('adaptation', '')
                            if 'High altitude' in adaptation or 'Tibetan' in adaptation:
                                altitude_score += 2
                            elif 'Moderate' in adaptation or 'Better' in adaptation:
                                altitude_score += 1

                            if 'Denisovan' in str(data.get('origin', '')):
                                results['altitude']['denisovan_origin'] = True

                        elif category == 'heat_adaptation':
                            results['heat']['markers'].append(marker_result)
                            sensitivity = data.get('sensitivity', '')
                            tolerance = data.get('heat_tolerance', data.get('cold_tolerance', ''))
                            if 'Enhanced heat' in tolerance or 'Low cold' in sensitivity:
                                heat_score += 1
                            elif 'cold' in tolerance.lower():
                                heat_score -= 1

                        elif category == 'uv_adaptation':
                            results['uv']['markers'].append(marker_result)
                            if 'Dark skin' in data.get('skin', ''):
                                uv_score += 2
                            elif 'Intermediate' in data.get('skin', ''):
                                uv_score += 1

        # Interpret altitude adaptation
        if altitude_score >= 2:
            results['altitude']['adaptation_level'] = 'High altitude adapted'
            results['altitude']['recommendations'] = [
                'You may have natural advantage at high altitude',
                'Less susceptible to acute mountain sickness',
                'May benefit from altitude training camps'
            ]
        elif altitude_score >= 1:
            results['altitude']['adaptation_level'] = 'Moderate altitude tolerance'
            results['altitude']['recommendations'] = [
                'Better than average altitude adaptation',
                'Standard acclimatization still recommended',
                'Altitude training can be beneficial'
            ]
        else:
            results['altitude']['adaptation_level'] = 'Standard (sea-level adapted)'
            results['altitude']['recommendations'] = [
                'Allow 2-3 days for altitude acclimatization above 8000ft',
                'Ascend gradually - no more than 1000ft/day above 10,000ft',
                'Stay hydrated and avoid alcohol at altitude',
                'Consider acetazolamide for rapid ascents'
            ]

        # Interpret heat adaptation
        if heat_score >= 1:
            results['heat']['adaptation_level'] = 'Heat adapted'
            results['heat']['recommendations'] = [
                'Natural heat tolerance advantage',
                'May perform better in hot conditions',
                'Still important to stay hydrated'
            ]
        elif heat_score <= -1:
            results['heat']['adaptation_level'] = 'Cold adapted'
            results['heat']['recommendations'] = [
                'Better cold tolerance through brown fat thermogenesis',
                'May need extra care in hot environments',
                'Ensure adequate hydration in heat'
            ]
        else:
            results['heat']['adaptation_level'] = 'Moderate climate adapted'
            results['heat']['recommendations'] = [
                'Balanced temperature adaptation',
                'Can acclimatize to both hot and cold over time'
            ]

        # Interpret UV adaptation
        if uv_score >= 2:
            results['uv']['adaptation_level'] = 'High UV protection (equatorial adapted)'
            results['uv']['recommendations'] = [
                'Natural protection against sun damage',
                'May need vitamin D supplementation at high latitudes',
                'Lower skin cancer risk'
            ]
        elif uv_score >= 1:
            results['uv']['adaptation_level'] = 'Moderate UV protection'
            results['uv']['recommendations'] = [
                'Moderate sun protection needed',
                'SPF 30+ recommended for extended sun exposure'
            ]
        else:
            results['uv']['adaptation_level'] = 'Low UV protection (high latitude adapted)'
            results['uv']['recommendations'] = [
                'High risk for sun damage - use SPF 50+',
                'Efficient vitamin D synthesis from sunlight',
                'Monitor for skin changes regularly',
                'Avoid tanning beds'
            ]

        # Determine ancestral environment
        if altitude_score >= 2:
            results['ancestral_environment'] = 'High altitude (Tibetan/Andean heritage likely)'
        elif uv_score >= 2:
            results['ancestral_environment'] = 'Equatorial/tropical regions'
        elif uv_score <= 0 and heat_score <= 0:
            results['ancestral_environment'] = 'Northern/high latitude regions'
        else:
            results['ancestral_environment'] = 'Temperate climate regions'

        return results

    # -------------------------------------------------------------------------
    # FACIAL FEATURE PREDICTION
    # -------------------------------------------------------------------------

    def analyze_facial_features(self) -> Dict[str, Any]:
        """Predict facial features from genetics - build a genetic mugshot"""
        results = {
            'features': {},
            'mugshot_description': '',
            'confidence': 0
        }

        features_found = 0
        total_features = 0

        for feature_name, markers in FACIAL_FEATURES.items():
            feature_result = {
                'name': feature_name.replace('_', ' ').title(),
                'prediction': '',
                'details': {},
                'markers_found': 0
            }

            for rsid, marker_data in markers.items():
                total_features += 1
                if rsid in self.snp_dict:
                    genotype = self.snp_dict[rsid]
                    if genotype in marker_data:
                        features_found += 1
                        data = marker_data[genotype]
                        feature_result['prediction'] = data.get('prediction', '')
                        feature_result['details'] = data
                        feature_result['markers_found'] += 1
                        feature_result['gene'] = marker_data.get('gene', '')
                        feature_result['genotype'] = genotype

            if feature_result['markers_found'] > 0:
                results['features'][feature_name] = feature_result

        # Generate mugshot description
        descriptions = []
        if 'face_shape' in results['features']:
            descriptions.append(results['features']['face_shape'].get('prediction', ''))
        if 'nose_shape' in results['features']:
            descriptions.append(results['features']['nose_shape'].get('prediction', ''))
        if 'chin_shape' in results['features']:
            descriptions.append(results['features']['chin_shape'].get('prediction', ''))
        if 'lip_shape' in results['features']:
            descriptions.append(results['features']['lip_shape'].get('prediction', ''))
        if 'eyebrow_thickness' in results['features']:
            descriptions.append(results['features']['eyebrow_thickness'].get('prediction', ''))

        results['mugshot_description'] = '. '.join([d for d in descriptions if d])
        results['confidence'] = (features_found / max(total_features, 1)) * 100

        return results

    # -------------------------------------------------------------------------
    # CHRONOTYPE / SLEEP GENETICS
    # -------------------------------------------------------------------------

    def analyze_chronotype(self) -> Dict[str, Any]:
        """Analyze circadian rhythm and sleep genetics"""
        results = {
            'chronotype': '',
            'morning_score': 50,
            'sleep_duration_need': 7.5,
            'insomnia_risk': 'Average',
            'ideal_wake_time': '7:00 AM',
            'ideal_sleep_time': '11:00 PM',
            'markers': [],
            'recommendations': []
        }

        morning_scores = []
        sleep_needs = []

        for category, markers in CHRONOTYPE_GENETICS.items():
            for rsid, marker_data in markers.items():
                if rsid in self.snp_dict:
                    genotype = self.snp_dict[rsid]
                    if genotype in marker_data:
                        data = marker_data[genotype]
                        results['markers'].append({
                            'gene': marker_data.get('gene', ''),
                            'rsid': rsid,
                            'genotype': genotype,
                            'effect': data
                        })

                        if 'score' in data:
                            if category == 'morningness':
                                morning_scores.append(data['score'])
                            if 'wake_time' in data:
                                results['ideal_wake_time'] = data['wake_time']

                        if 'need' in data:
                            sleep_needs.append(data['need'])

                        if category == 'insomnia_risk':
                            results['insomnia_risk'] = data.get('risk', 'Average')

        if morning_scores:
            avg_score = np.mean(morning_scores)
            results['morning_score'] = avg_score
            if avg_score >= 70:
                results['chronotype'] = 'Morning Lark'
                results['ideal_wake_time'] = '5:30-6:30 AM'
                results['ideal_sleep_time'] = '9:30-10:30 PM'
            elif avg_score >= 55:
                results['chronotype'] = 'Moderate Morning'
                results['ideal_wake_time'] = '6:30-7:30 AM'
                results['ideal_sleep_time'] = '10:30-11:30 PM'
            elif avg_score >= 45:
                results['chronotype'] = 'Intermediate'
                results['ideal_wake_time'] = '7:00-8:00 AM'
                results['ideal_sleep_time'] = '11:00 PM-12:00 AM'
            else:
                results['chronotype'] = 'Night Owl'
                results['ideal_wake_time'] = '8:00-10:00 AM'
                results['ideal_sleep_time'] = '12:00-2:00 AM'

        if sleep_needs:
            results['sleep_duration_need'] = np.mean(sleep_needs)

        # Recommendations
        if results['chronotype'] == 'Night Owl':
            results['recommendations'] = [
                'Avoid scheduling important tasks early morning',
                'Use bright light therapy in morning to shift rhythm',
                'Your cognitive peak is likely late morning/afternoon',
                'Avoid blue light 2 hours before bed'
            ]
        elif results['chronotype'] == 'Morning Lark':
            results['recommendations'] = [
                'Schedule demanding tasks in early morning',
                'Avoid caffeine after 2 PM',
                'Your cognitive peak is likely 9-11 AM',
                'Plan social events earlier in evening'
            ]

        return results

    # -------------------------------------------------------------------------
    # PAIN SENSITIVITY
    # -------------------------------------------------------------------------

    def analyze_pain_sensitivity(self) -> Dict[str, Any]:
        """Analyze pain perception genetics"""
        results = {
            'overall_sensitivity': 'Average',
            'pain_score': 50,
            'threshold': 'Medium',
            'markers': [],
            'migraine_risk': 'Average',
            'drug_response': {},
            'recommendations': []
        }

        pain_scores = []

        for category, markers in PAIN_GENETICS.items():
            for rsid, marker_data in markers.items():
                if rsid in self.snp_dict:
                    genotype = self.snp_dict[rsid]
                    if genotype in marker_data:
                        data = marker_data[genotype]
                        results['markers'].append({
                            'gene': marker_data.get('gene', ''),
                            'rsid': rsid,
                            'genotype': genotype,
                            'category': category,
                            'effect': data
                        })

                        if 'score' in data:
                            pain_scores.append(data['score'])

                        if 'drug_response' in data:
                            results['drug_response'][marker_data.get('gene', '')] = data['drug_response']

                        if category == 'migraine_risk':
                            results['migraine_risk'] = data.get('risk', 'Average')

        if pain_scores:
            avg = np.mean(pain_scores)
            results['pain_score'] = avg
            if avg >= 65:
                results['overall_sensitivity'] = 'High (more sensitive to pain)'
                results['threshold'] = 'Low'
                results['recommendations'] = [
                    'You may be more sensitive to pain - communicate with doctors',
                    'May respond well to lower doses of pain medication',
                    'Consider preventive approaches for chronic conditions',
                    'Mind-body techniques may be especially helpful'
                ]
            elif avg <= 40:
                results['overall_sensitivity'] = 'Low (higher pain tolerance)'
                results['threshold'] = 'High'
                results['recommendations'] = [
                    'Higher pain tolerance - dont ignore warning pain signals',
                    'May need higher doses of pain medication',
                    'Good candidate for endurance sports/activities'
                ]
            else:
                results['overall_sensitivity'] = 'Average'
                results['threshold'] = 'Medium'

        return results

    # -------------------------------------------------------------------------
    # ADDICTION RISK
    # -------------------------------------------------------------------------

    def analyze_addiction_risk(self) -> Dict[str, Any]:
        """Analyze addiction susceptibility genetics"""
        results = {
            'overall_risk': 'Average',
            'alcohol': {'risk': 'Unknown', 'score': 50, 'details': []},
            'nicotine': {'risk': 'Unknown', 'score': 50, 'details': []},
            'dopamine_reward': {'profile': 'Normal', 'score': 50, 'details': []},
            'gambling': {'risk': 'Unknown', 'score': 50, 'details': []},
            'cannabis': {'risk': 'Unknown', 'score': 50, 'details': []},
            'recommendations': []
        }

        for category, markers in ADDICTION_GENETICS.items():
            category_scores = []
            for rsid, marker_data in markers.items():
                if rsid in self.snp_dict:
                    genotype = self.snp_dict[rsid]
                    if genotype in marker_data:
                        data = marker_data[genotype]
                        if 'score' in data:
                            category_scores.append(data['score'])

                        if category in results:
                            if isinstance(results[category], dict):
                                results[category]['details'].append({
                                    'gene': marker_data.get('gene', ''),
                                    'genotype': genotype,
                                    'effect': data
                                })

            if category_scores and category in results:
                avg = np.mean(category_scores)
                results[category]['score'] = avg
                if avg >= 60:
                    results[category]['risk'] = 'Elevated'
                elif avg <= 35:
                    results[category]['risk'] = 'Lower'
                else:
                    results[category]['risk'] = 'Average'

        # Overall risk
        all_scores = []
        for cat in ['alcohol', 'nicotine', 'dopamine_reward', 'gambling', 'cannabis']:
            if cat in results and isinstance(results[cat], dict):
                all_scores.append(results[cat].get('score', 50))

        if all_scores:
            overall = np.mean(all_scores)
            if overall >= 60:
                results['overall_risk'] = 'Elevated genetic risk'
                results['recommendations'] = [
                    'Be cautious with addictive substances',
                    'Your genetics suggest higher susceptibility',
                    'Seek support early if you notice patterns',
                    'Healthy dopamine activities: exercise, social connection'
                ]
            elif overall <= 35:
                results['overall_risk'] = 'Lower genetic risk'
                results['recommendations'] = [
                    'Lower genetic predisposition but not immune',
                    'Environment and behavior still matter'
                ]

        return results

    # -------------------------------------------------------------------------
    # MENTAL TRAITS / STRESS RESPONSE
    # -------------------------------------------------------------------------

    def analyze_mental_traits(self) -> Dict[str, Any]:
        """Analyze mental resilience and stress genetics"""
        results = {
            'stress_type': '',  # Warrior vs Worrier
            'stress_score': 50,
            'anxiety_tendency': 'Average',
            'depression_risk': 'Average',
            'risk_taking': 'Average',
            'markers': [],
            'strengths': [],
            'recommendations': []
        }

        stress_scores = []
        anxiety_scores = []

        for category, markers in MENTAL_GENETICS.items():
            for rsid, marker_data in markers.items():
                if rsid in self.snp_dict:
                    genotype = self.snp_dict[rsid]
                    if genotype in marker_data:
                        data = marker_data[genotype]
                        results['markers'].append({
                            'gene': marker_data.get('gene', ''),
                            'rsid': rsid,
                            'genotype': genotype,
                            'category': category,
                            'effect': data
                        })

                        if 'type' in data:  # Warrior/Worrier
                            results['stress_type'] = data['type']

                        if 'score' in data:
                            if category == 'stress_response':
                                stress_scores.append(data['score'])
                            elif category == 'anxiety_tendency':
                                anxiety_scores.append(data['score'])

        if stress_scores:
            avg = np.mean(stress_scores)
            results['stress_score'] = avg
            if avg >= 60:
                results['stress_type'] = 'Warrior'
                results['strengths'] = [
                    'Performs well under pressure',
                    'Good in competitive/stressful situations',
                    'Less affected by stress hormones'
                ]
            elif avg <= 40:
                results['stress_type'] = 'Worrier'
                results['strengths'] = [
                    'Better focus in calm environments',
                    'Excellent memory and attention to detail',
                    'More thoughtful decision-making'
                ]

        if anxiety_scores:
            avg = np.mean(anxiety_scores)
            if avg >= 60:
                results['anxiety_tendency'] = 'Higher'
                results['recommendations'] = [
                    'Regular exercise is especially beneficial for your genetics',
                    'Meditation/mindfulness practices recommended',
                    'Prioritize sleep and stress management',
                    'Consider omega-3s and B vitamins'
                ]
            elif avg <= 40:
                results['anxiety_tendency'] = 'Lower'

        return results

    # -------------------------------------------------------------------------
    # SENSORY TRAITS (Comprehensive: Taste, Smell, Touch, Temperature, Vision)
    # -------------------------------------------------------------------------

    def analyze_sensory_traits(self) -> Dict[str, Any]:
        """
        Comprehensive sensory genetics analysis including:
        - Bitter taste (TAS2R38 supertaster status)
        - Sweet taste sensitivity (TAS1R2/TAS1R3)
        - Umami taste (TAS1R1)
        - Cilantro soap gene (OR6A2)
        - Asparagus smell detection (OR2M7)
        - Color vision / color blindness
        - Smell sensitivity (super-smellers)
        - Specific anosmias
        - Touch sensitivity (PIEZO2)
        - Temperature sensitivity (TRP channels)
        """
        # Use the comprehensive sensory genetics analysis module
        comprehensive_results = analyze_sensory_genetics(self.snp_dict)

        # Also include legacy body odor and handedness analysis for completeness
        legacy_results = {
            'body_odor': {
                'type': 'Unknown',
                'earwax': 'Unknown',
                'needs_deodorant': True
            },
            'handedness': {
                'left_handed_probability': 0.10
            },
            'hearing': {
                'loss_risk': 'Average',
                'details': []
            }
        }

        # Body odor from ABCC11 gene
        for rsid, marker_data in BODY_ODOR_GENETICS.get('body_odor', {}).items():
            if rsid in self.snp_dict:
                genotype = self.snp_dict[rsid]
                if genotype in marker_data:
                    data = marker_data[genotype]
                    legacy_results['body_odor']['earwax'] = data.get('earwax', 'Unknown')
                    legacy_results['body_odor']['type'] = data.get('odor', 'Unknown')
                    legacy_results['body_odor']['needs_deodorant'] = 'need' in data.get('deodorant', '').lower()

        # Handedness
        left_probs = []
        for rsid, marker_data in HANDEDNESS_GENETICS.get('handedness', {}).items():
            if rsid in self.snp_dict:
                genotype = self.snp_dict[rsid]
                if genotype in marker_data:
                    data = marker_data[genotype]
                    if 'left_prob' in data:
                        left_probs.append(data['left_prob'])

        if left_probs:
            legacy_results['handedness']['left_handed_probability'] = np.mean(left_probs)

        # Merge comprehensive results with legacy
        results = {
            **comprehensive_results,
            **legacy_results,
            # Also keep backward-compatible fields
            'taste': {
                'type': comprehensive_results.get('bitter_taste', {}).get('phenotype', 'Average taster'),
                'bitter_sensitivity': 'High' if comprehensive_results.get('bitter_taste', {}).get('taster_score', 0.5) > 0.7 else 'Normal',
                'sweet_sensitivity': comprehensive_results.get('sweet_taste', {}).get('phenotype', 'Normal'),
                'umami_sensitivity': comprehensive_results.get('umami_taste', {}).get('phenotype', 'Normal'),
                'details': comprehensive_results.get('bitter_taste', {}).get('markers_found', [])
            },
            'smell': {
                'cilantro_soap': comprehensive_results.get('cilantro', {}).get('tastes_soapy', False),
                'asparagus_detection': comprehensive_results.get('asparagus_smell', {}).get('phenotype', 'Unknown'),
                'overall_sensitivity': comprehensive_results.get('smell_sensitivity', {}).get('overall_sensitivity', 'Normal'),
                'details': comprehensive_results.get('smell_sensitivity', {}).get('markers_found', [])
            }
        }

        return results

    # -------------------------------------------------------------------------
    # BEHAVIORAL & COGNITIVE GENETICS
    # -------------------------------------------------------------------------

    def analyze_behavioral_genetics(self) -> Dict[str, Any]:
        """
        Comprehensive behavioral genetics analysis including:
        - Empathy levels (OXTR)
        - Novelty/risk seeking (DRD4, DRD2)
        - Warrior gene (MAOA)
        - Stress resilience (CRHR1, FKBP5)
        - Depression susceptibility (SLC6A4)
        - Social bonding (AVPR1A)
        - Memory & learning (KIBRA, BDNF, COMT)
        - Attention & impulsivity (DAT1, ADRA2A)
        """
        # Use the comprehensive behavioral genetics analysis module
        return analyze_behavioral_genetics(self.snp_dict)

    # -------------------------------------------------------------------------
    # SLEEP & CIRCADIAN GENETICS
    # -------------------------------------------------------------------------

    def analyze_sleep_genetics(self) -> Dict[str, Any]:
        """
        Comprehensive sleep genetics analysis including:
        - Chronotype (morning lark vs night owl)
        - Sleep duration need
        - Sleep quality
        - Insomnia susceptibility
        - Deep sleep (slow-wave sleep)
        - REM sleep patterns
        - Sleep latency
        - Shift work tolerance
        - Delayed sleep phase syndrome risk
        - Caffeine and sleep interaction
        """
        # Use the comprehensive sleep genetics analysis module
        return analyze_sleep_genetics(self.snp_dict)

    # -------------------------------------------------------------------------
    # EXPANDED PHYSICAL TRAITS
    # -------------------------------------------------------------------------

    def analyze_physical_traits_expanded(self) -> Dict[str, Any]:
        """
        Expanded physical traits analysis including:
        - Height prediction (polygenic)
        - Hair texture (curly, wavy, straight)
        - Hair loss / Male pattern baldness
        - Freckles
        - Dimples
        - Widow's peak
        - Cleft chin
        - Earlobe attachment
        - Tongue rolling ability
        - Finger length ratio (2D:4D)
        """
        # Use the comprehensive physical traits expanded analysis module
        return analyze_physical_traits_expanded(self.snp_dict)

    # -------------------------------------------------------------------------
    # SPORTS & INJURY GENETICS
    # -------------------------------------------------------------------------

    def analyze_sports_genetics(self) -> Dict[str, Any]:
        """
        Comprehensive sports genetics analysis including:
        - Muscle fiber composition (ACTN3 power vs endurance)
        - VO2 max potential
        - ACL injury susceptibility
        - Tendon injury risk
        - Muscle cramping susceptibility
        - Recovery speed
        - Exercise-induced fatigue
        - Blood pressure response to exercise
        - Lactate clearance
        """
        # Use the comprehensive sports genetics analysis module
        return analyze_sports_genetics(self.snp_dict)

    # -------------------------------------------------------------------------
    # REPRODUCTION & FERTILITY GENETICS
    # -------------------------------------------------------------------------

    def analyze_reproduction_genetics(self) -> Dict[str, Any]:
        """
        Comprehensive reproduction genetics analysis including:
        - Male fertility factors (sperm quality, motility)
        - Female fertility factors (ovarian reserve, egg quality)
        - Menopause timing prediction
        - Twin probability (fraternal twins)
        - Endometriosis risk
        - PCOS risk
        - Testosterone levels
        - Estrogen metabolism
        - Pregnancy complications (thrombosis risk)
        """
        # Use the comprehensive reproduction genetics analysis module
        return analyze_reproduction_genetics(self.snp_dict)

    # -------------------------------------------------------------------------
    # IMMUNE SYSTEM DEEP DIVE
    # -------------------------------------------------------------------------

    def analyze_immune_deep_genetics(self) -> Dict[str, Any]:
        """
        Comprehensive immune system genetics analysis including:
        - HLA type analysis (autoimmune, transplant compatibility)
        - Cytokine response genetics (IL-6, TNF-alpha, IL-10)
        - Inflammatory markers (CRP, NF-kB)
        - Allergy susceptibility (IgE, skin barrier)
        - Celiac disease risk
        - Lupus (SLE) risk
        - Multiple sclerosis risk
        - Rheumatoid arthritis risk
        - Psoriasis risk
        - IBD/Crohn's disease risk
        """
        # Use the comprehensive immune deep genetics analysis module
        return analyze_immune_deep_genetics(self.snp_dict)

    # -------------------------------------------------------------------------
    # NUTRITION & METABOLISM
    # -------------------------------------------------------------------------

    def analyze_nutrition_metabolism(self) -> Dict[str, Any]:
        """
        Comprehensive nutrition and metabolism genetics including:
        - Vitamin A metabolism (beta-carotene conversion)
        - Vitamin B12 metabolism (FUT2, TCN2, MTHFR)
        - Vitamin C requirements
        - Vitamin E metabolism
        - Omega-3 fatty acid metabolism (FADS1/FADS2)
        - Saturated fat response
        - Carbohydrate metabolism (glycemic response, T2D risk)
        - Protein metabolism and satiety
        - Sodium sensitivity
        - Alcohol metabolism (ADH1B, ALDH2)
        """
        # Use the comprehensive nutrition metabolism analysis module
        return analyze_nutrition_metabolism(self.snp_dict)

    # -------------------------------------------------------------------------
    # ANCIENT DNA & HISTORY
    # -------------------------------------------------------------------------

    def analyze_ancient_dna_history(self) -> Dict[str, Any]:
        """
        Comprehensive ancient DNA and historical genetics including:
        - Neanderthal ancestry markers
        - Denisovan ancestry markers
        - Ancient European Farmer ancestry
        - Hunter-Gatherer ancestry
        - Steppe/Yamnaya ancestry
        - Ancient pathogen resistance (plague, TB)
        - Lactase persistence historical context
        - Blue eye and light skin origins
        - Historical migration markers
        """
        # Use the comprehensive ancient DNA history analysis module
        return analyze_ancient_dna_history(self.snp_dict)

    # -------------------------------------------------------------------------
    # LONGEVITY GENETICS
    # -------------------------------------------------------------------------

    def analyze_longevity_genetics(self) -> Dict[str, Any]:
        """
        Comprehensive longevity and aging genetics including:
        - Telomere length genetics (TERT, TERC)
        - Sirtuin pathway (SIRT1, SIRT3, SIRT6)
        - FOXO longevity transcription factors
        - IGF-1/growth hormone pathway
        - Autophagy genetics
        - Mitochondrial function genes
        - Inflammaging markers
        - Klotho anti-aging hormone
        """
        return analyze_longevity_genetics(self.snp_dict)

    # -------------------------------------------------------------------------
    # PHARMACOGENOMICS - DETAILED DRUG METABOLISM
    # -------------------------------------------------------------------------

    def analyze_pharmacogenomics_detailed(self) -> Dict[str, Any]:
        """
        Comprehensive pharmacogenomics including:
        - CYP2D6 (codeine, tramadol, SSRIs, beta-blockers)
        - CYP2C19 (clopidogrel, PPIs, SSRIs)
        - CYP2C9 (warfarin, NSAIDs, sulfonylureas)
        - VKORC1 (warfarin sensitivity)
        - SLCO1B1 (statin myopathy)
        - TPMT (thiopurine toxicity)
        - DPYD (5-FU toxicity)
        - OPRM1 (opioid response)
        - CYP1A2 (caffeine metabolism)
        - MTHFR (folate metabolism)
        """
        return analyze_pharmacogenomics(self.snp_dict)

    # -------------------------------------------------------------------------
    # MENTAL HEALTH GENETICS
    # -------------------------------------------------------------------------

    def analyze_mental_health_genetics(self) -> Dict[str, Any]:
        """
        Comprehensive mental health genetics including:
        - Depression risk factors (BDNF, FKBP5, etc.)
        - Anxiety vulnerability (HTR1A, COMT, SLC6A4)
        - ADHD genetics (DAT1, DRD4, ADRA2A)
        - Bipolar disorder risk (ANK3, CACNA1C)
        - Schizophrenia risk factors
        - PTSD vulnerability (FKBP5, CRHR1)
        - Addiction vulnerability (OPRM1, DRD2)
        - Cognitive profile (COMT warrior/worrier)
        """
        return analyze_mental_health_genetics(self.snp_dict)

    # -------------------------------------------------------------------------
    # CANCER RISK GENETICS
    # -------------------------------------------------------------------------

    def analyze_cancer_risk_genetics(self) -> Dict[str, Any]:
        """
        Common cancer risk variants including:
        - Breast cancer (FGFR2, TOX3, common BRCA variants)
        - Colorectal cancer (8q24, SMAD7)
        - Prostate cancer (8q24, HNF1B, MSMB)
        - Lung cancer (TERT, CHRNA3/5)
        - Melanoma (MC1R, HERC2)
        - Thyroid cancer (FOXE1, NKX2-1)
        - Pancreatic cancer (ABO, NR5A2)
        Note: Does not include rare pathogenic BRCA1/2 mutations
        """
        return analyze_cancer_risk_genetics(self.snp_dict)

    # -------------------------------------------------------------------------
    # CARDIOVASCULAR GENETICS
    # -------------------------------------------------------------------------

    def analyze_cardiovascular_genetics(self) -> Dict[str, Any]:
        """
        Comprehensive cardiovascular genetics including:
        - Coronary artery disease risk (9p21, LPA, SORT1)
        - LDL cholesterol genetics (APOB, LDLR)
        - HDL cholesterol genetics (CETP, LIPC)
        - Triglyceride genetics (APOA5)
        - Blood pressure/hypertension (ACE, AGT, AGTR1)
        - Stroke risk factors
        - Atrial fibrillation risk (PITX2, ZFHX3)
        - Clotting/thrombosis (Factor V Leiden, Prothrombin)
        """
        return analyze_cardiovascular_genetics(self.snp_dict)

    # -------------------------------------------------------------------------
    # SKIN & DERMATOLOGY GENETICS
    # -------------------------------------------------------------------------

    def analyze_skin_dermatology(self) -> Dict[str, Any]:
        """
        Comprehensive skin & dermatology genetics including:
        - Skin aging genetics (MMP1, COL1A1, ELN)
        - UV sensitivity and sun damage (MC1R, TYR, OCA2)
        - Eczema/atopic dermatitis risk (FLG, IL4, IL13)
        - Psoriasis risk (HLA-C, IL12B, IL23R)
        - Rosacea risk (HLA-DRA, BTNL2)
        - Acne tendency (SELL, FST, OVOL1)
        - Skin elasticity and stretch marks
        - Vitamin D synthesis efficiency
        """
        return analyze_skin_dermatology(self.snp_dict)

    # -------------------------------------------------------------------------
    # DEEP ANCESTRY GENETICS
    # -------------------------------------------------------------------------

    def analyze_deep_ancestry(self) -> Dict[str, Any]:
        """
        Deep ancestry analysis including:
        - European regional markers (Northern, Mediterranean, Eastern)
        - African regional markers (Sub-Saharan, Duffy null)
        - East Asian markers (EDAR, alcohol flush)
        - South Asian markers
        - Native American markers (Beringian ancestry)
        - Middle Eastern/North African markers
        - Jewish ancestry markers (Ashkenazi, Sephardic)
        - Ancient migration patterns (Neolithic Farmer, Bronze Age Steppe)
        - Isolated population markers
        """
        return analyze_deep_ancestry(self.snp_dict)

    # -------------------------------------------------------------------------
    # ANCIENT POPULATION MATCHING
    # -------------------------------------------------------------------------

    def analyze_ancient_population_match(self) -> Dict[str, Any]:
        """Match to ancient populations (Vikings, Romans, etc.)"""
        results = {
            'matches': [],
            'best_match': '',
            'match_scores': {}
        }

        for pop_id, pop_data in ANCIENT_POPULATIONS.items():
            match_score = 0
            markers_found = 0
            markers_matched = 0

            markers = pop_data.get('markers', {})
            for rsid, marker_info in markers.items():
                if rsid in self.snp_dict:
                    markers_found += 1
                    genotype = self.snp_dict[rsid]
                    expected = marker_info.get(f'{pop_id}_allele', marker_info.get('yamnaya_allele', ''))
                    if expected and expected in genotype:
                        markers_matched += 1
                        match_score += marker_info.get('freq', 0.5)

            if markers_found > 0:
                score = (markers_matched / markers_found) * 100
                results['match_scores'][pop_id] = {
                    'name': pop_data['description'],
                    'score': round(score, 1),
                    'time_period': pop_data['time_period'],
                    'location': pop_data['location'],
                    'contribution': pop_data.get('contribution', ''),
                    'typical_traits': pop_data.get('typical_traits', [])
                }

        # Sort by score
        sorted_matches = sorted(
            results['match_scores'].items(),
            key=lambda x: x[1]['score'],
            reverse=True
        )

        for pop_id, data in sorted_matches[:5]:
            results['matches'].append({
                'population': pop_id,
                **data
            })

        if sorted_matches:
            results['best_match'] = sorted_matches[0][1]['name']

        return results

    # -------------------------------------------------------------------------
    # PERSONALIZED PLAN (Supplements, Diet, Exercise)
    # -------------------------------------------------------------------------

    def generate_personalized_plan(self, health_traits=None, nutrition_fitness=None,
                                      athletic_genetics=None, pharmacogenomics=None,
                                      polygenic_scores=None, carrier_status=None,
                                      longevity=None, immunity=None, mental_traits=None,
                                      chronotype=None, cardiovascular=None, cancer_risk=None,
                                      nutrition_metabolism=None) -> Dict[str, Any]:
        """Generate personalized supplement, diet, and exercise recommendations
        by aggregating data from ALL analysis modules"""
        results = {
            'supplements': [],
            'diet': {
                'type': 'Balanced',
                'recommendations': [],
                'foods_to_increase': [],
                'foods_to_limit': []
            },
            'exercise': {
                'type': 'Mixed',
                'recommendations': [],
                'optimal_activities': []
            },
            'lifestyle': [],
            'screening': [],
            'avoid': []
        }

        # Track supplements by name to avoid duplicates
        added_supplements = set()

        def add_supplement(name, reason, dose, priority):
            if name not in added_supplements:
                added_supplements.add(name)
                results['supplements'].append({
                    'supplement': name,
                    'reason': reason,
                    'dose': dose,
                    'priority': priority
                })

        # ========== SNP-BASED RECOMMENDATIONS (existing) ==========
        # Check MTHFR for methylfolate
        if 'rs1801133' in self.snp_dict:
            genotype = self.snp_dict['rs1801133']
            if genotype in ['TT', 'CT']:
                add_supplement('Methylfolate (L-5-MTHF)',
                    'MTHFR variant - reduced folate conversion',
                    '400-800 mcg daily',
                    'high' if genotype == 'TT' else 'medium')

        # Check VDR for vitamin D
        if 'rs2228570' in self.snp_dict:
            genotype = self.snp_dict['rs2228570']
            if genotype in ['TT', 'CT']:
                add_supplement('Vitamin D3',
                    'VDR variant - reduced vitamin D efficiency',
                    '2000-4000 IU daily',
                    'high' if genotype == 'TT' else 'medium')

        # Check SOD2 for antioxidants
        if 'rs4880' in self.snp_dict:
            genotype = self.snp_dict['rs4880']
            if genotype == 'CC':
                add_supplement('Antioxidants (Vitamin C, E, Selenium)',
                    'SOD2 variant - lower antioxidant enzyme activity',
                    'Vitamin C 500mg, Vitamin E 200IU, Selenium 100mcg',
                    'medium')

        # Check COMT for stress
        if 'rs4680' in self.snp_dict:
            genotype = self.snp_dict['rs4680']
            if genotype == 'AA':  # Worrier
                add_supplement('Magnesium Glycinate',
                    'COMT worrier variant - supports stress response',
                    '200-400 mg before bed',
                    'medium')
                results['lifestyle'].append('Practice stress-reduction: meditation, yoga, breathing exercises')

        # Check APOE for diet
        if 'rs429358' in self.snp_dict:
            genotype = self.snp_dict['rs429358']
            if genotype in ['CC', 'CT']:  # APOE4
                results['diet']['type'] = 'Mediterranean/Low Saturated Fat'
                results['diet']['recommendations'].append('APOE4 carrier: Limit saturated fat strictly')
                results['diet']['foods_to_limit'].extend(['Red meat', 'Full-fat dairy', 'Coconut oil'])
                results['diet']['foods_to_increase'].extend(['Fatty fish', 'Olive oil', 'Leafy greens'])
                add_supplement('Omega-3 (DHA)',
                    'APOE4 - DHA especially important for brain health',
                    '1000mg DHA daily',
                    'high')

        # Check FTO for weight management
        if 'rs9939609' in self.snp_dict:
            genotype = self.snp_dict['rs9939609']
            if genotype in ['AA', 'AT']:
                results['diet']['recommendations'].append('FTO variant: Higher obesity risk - portion control important')
                results['diet']['foods_to_limit'].extend(['Processed foods', 'Added sugars'])
                results['exercise']['recommendations'].append('FTO variant: Exercise is especially effective for weight management')

        # Check ACTN3 for exercise type
        if 'rs1815739' in self.snp_dict:
            genotype = self.snp_dict['rs1815739']
            if genotype == 'CC':
                results['exercise']['type'] = 'Power/Strength Focus'
                results['exercise']['optimal_activities'] = ['Weightlifting', 'Sprinting', 'HIIT', 'CrossFit']
                results['exercise']['recommendations'].append('ACTN3 power variant: Focus on explosive movements')
            elif genotype == 'TT':
                results['exercise']['type'] = 'Endurance Focus'
                results['exercise']['optimal_activities'] = ['Running', 'Cycling', 'Swimming', 'Rowing']
                results['exercise']['recommendations'].append('ACTN3 endurance variant: Excellent for aerobic activities')
            else:
                results['exercise']['type'] = 'Mixed Training'
                results['exercise']['optimal_activities'] = ['Soccer', 'Basketball', 'Tennis', 'General fitness']

        # Check IL6 for recovery
        if 'rs1800795' in self.snp_dict:
            genotype = self.snp_dict['rs1800795']
            if genotype == 'CC':
                results['exercise']['recommendations'].append('IL6 variant: Prioritize recovery days')
                add_supplement('Turmeric/Curcumin',
                    'IL6 high inflammation variant - natural anti-inflammatory',
                    '500mg with black pepper',
                    'medium')

        # ========== AGGREGATE FROM ANALYSIS MODULES ==========

        # From Health Traits - add relevant supplements and recommendations
        if health_traits:
            for condition in health_traits.get('conditions', []):
                risk = condition.get('risk_level', '')
                name = condition.get('condition', '')

                if 'Higher' in risk or 'Elevated' in risk:
                    # Add to screening recommendations
                    results['screening'].append(f'Monitor {name} - elevated genetic risk')

                    # Condition-specific supplements
                    if 'diabetes' in name.lower():
                        add_supplement('Berberine or Chromium',
                            f'Elevated {name} risk - supports blood sugar',
                            '500mg berberine or 200mcg chromium',
                            'medium')
                        results['diet']['foods_to_limit'].append('Refined carbohydrates')
                    elif 'heart' in name.lower() or 'cardiovascular' in name.lower():
                        add_supplement('CoQ10',
                            f'Elevated cardiovascular risk - heart support',
                            '100-200mg daily',
                            'medium')

        # From Athletic Genetics
        if athletic_genetics:
            muscle_type = athletic_genetics.get('muscle_fiber_type', '')
            if 'fast-twitch' in muscle_type.lower():
                if not results['exercise']['optimal_activities']:
                    results['exercise']['optimal_activities'] = ['Sprinting', 'Weightlifting', 'HIIT']
            elif 'slow-twitch' in muscle_type.lower():
                if not results['exercise']['optimal_activities']:
                    results['exercise']['optimal_activities'] = ['Marathon', 'Cycling', 'Swimming']

            recovery = athletic_genetics.get('recovery', {})
            if recovery.get('rate') == 'Slower':
                results['exercise']['recommendations'].append('Allow extra recovery time between sessions')
                add_supplement('Tart Cherry Extract',
                    'Slower recovery genetics - reduce inflammation',
                    '500mg or 8oz juice post-workout',
                    'low')

        # From Nutrition & Metabolism
        if nutrition_metabolism:
            # Caffeine metabolism
            caffeine = nutrition_metabolism.get('caffeine_metabolism', {})
            if caffeine.get('type') == 'Slow':
                results['lifestyle'].append('Limit caffeine to morning only - slow metabolizer')
                results['avoid'].append('Caffeine after 2 PM')

            # Lactose tolerance
            lactose = nutrition_metabolism.get('lactose_tolerance', {})
            if lactose.get('status') == 'Intolerant':
                results['diet']['foods_to_limit'].append('Dairy products')
                add_supplement('Lactase Enzyme',
                    'Lactose intolerant - take with dairy',
                    'As needed with dairy',
                    'low')

            # Alcohol metabolism
            alcohol = nutrition_metabolism.get('alcohol_metabolism', {})
            if alcohol.get('flush_risk') or 'slow' in str(alcohol.get('type', '')).lower():
                results['avoid'].append('Excessive alcohol - slow metabolism/flush risk')

        # From Cardiovascular Genetics
        if cardiovascular:
            for finding in cardiovascular.get('risk_factors', []):
                if finding.get('risk_level') in ['Higher', 'Elevated']:
                    results['screening'].append(f"Regular cardiovascular screening - {finding.get('factor', '')}")
                    add_supplement('Omega-3 Fish Oil',
                        'Cardiovascular risk - heart health support',
                        '2000mg EPA+DHA daily',
                        'medium')

        # From Cancer Risk Genetics
        if cancer_risk:
            for cancer in cancer_risk.get('risks', []):
                if cancer.get('risk_level') in ['Higher', 'Elevated']:
                    cancer_type = cancer.get('type', '')
                    results['screening'].append(f'Regular {cancer_type} screening recommended')

                    if 'skin' in cancer_type.lower():
                        results['lifestyle'].append('Use SPF 30+ sunscreen daily')
                    elif 'colon' in cancer_type.lower():
                        results['diet']['foods_to_increase'].append('Fiber-rich foods')

        # From Chronotype/Sleep
        if chronotype:
            chrono_type = chronotype.get('chronotype', '')
            if 'night' in chrono_type.lower() or 'owl' in chrono_type.lower():
                results['lifestyle'].append('Night owl genetics - may need blackout curtains, limit evening blue light')
                add_supplement('Melatonin',
                    'Night owl chronotype - may help sleep onset',
                    '0.5-3mg 30min before bed if needed',
                    'low')
            elif 'morning' in chrono_type.lower() or 'lark' in chrono_type.lower():
                results['lifestyle'].append('Morning person genetics - schedule important tasks for AM')

        # From Immunity
        if immunity:
            if immunity.get('inflammation_tendency') == 'Higher':
                add_supplement('Turmeric/Curcumin',
                    'Higher inflammation genetics - anti-inflammatory support',
                    '500mg with black pepper',
                    'medium')
                results['diet']['foods_to_increase'].extend(['Turmeric', 'Ginger', 'Green tea'])

        # From Pharmacogenomics - Drug interactions to avoid
        if pharmacogenomics:
            for drug in pharmacogenomics.get('interactions', []):
                if drug.get('recommendation') == 'Avoid' or 'increased' in str(drug.get('effect', '')).lower():
                    results['avoid'].append(f"{drug.get('drug', '')}: {drug.get('recommendation', '')}")

        # ========== DEFAULTS IF EMPTY ==========
        if not results['supplements']:
            results['supplements'] = [
                {'supplement': 'Vitamin D3', 'reason': 'General optimization', 'dose': '1000-2000 IU', 'priority': 'low'},
                {'supplement': 'Omega-3', 'reason': 'General health', 'dose': '1000mg EPA+DHA', 'priority': 'low'},
                {'supplement': 'Magnesium', 'reason': 'Most people deficient', 'dose': '200-400mg', 'priority': 'low'}
            ]

        if not results['diet']['recommendations']:
            results['diet']['recommendations'] = ['Balanced whole foods diet recommended']
            results['diet']['foods_to_increase'] = ['Vegetables', 'Lean protein', 'Whole grains', 'Healthy fats']
            results['diet']['foods_to_limit'] = ['Processed foods', 'Added sugars', 'Trans fats']

        if not results['exercise']['recommendations']:
            results['exercise']['recommendations'] = ['150 minutes moderate or 75 minutes vigorous exercise weekly']

        if not results['exercise']['optimal_activities']:
            results['exercise']['optimal_activities'] = ['Walking', 'Swimming', 'Cycling', 'Yoga']

        # Remove duplicates from lists
        results['diet']['foods_to_increase'] = list(set(results['diet']['foods_to_increase']))
        results['diet']['foods_to_limit'] = list(set(results['diet']['foods_to_limit']))
        results['screening'] = list(set(results['screening']))
        results['lifestyle'] = list(set(results['lifestyle']))
        results['avoid'] = list(set(results['avoid']))

        # Sort supplements by priority
        priority_order = {'high': 0, 'medium': 1, 'low': 2}
        results['supplements'].sort(key=lambda x: priority_order.get(x.get('priority', 'low'), 2))

        return results

    # -------------------------------------------------------------------------
    # SUMMARY GENERATION
    # -------------------------------------------------------------------------

    def generate_summary(self) -> Dict[str, Any]:
        """Generate overall summary of analysis"""
        return {
            'total_snps_analyzed': len(self.snp_dict),
            'analysis_modules': [
                'Ancestry Composition (604k+ markers)',
                'Physical Traits (25 traits)',
                'Health Traits (22 conditions)',
                'Pharmacogenomics (12 genes)',
                'Carrier Status (10 conditions)',
                'Haplogroups (mtDNA & Y-DNA)',
                'Immunity (9 markers)',
                'Longevity (15 markers)',
                'Nutrition & Fitness (18 markers)',
                'Climate Adaptation',
                'Blood Type (7 systems)',
                'Athletic Genetics (12 genes)',
                'Environmental Adaptation',
                'Polygenic Scores (5 conditions, 100+ markers each)',
                'Ancient DNA (Neanderthal & Denisovan)',
                'Facial Feature Prediction (15+ traits)',
                'Chronotype/Sleep Genetics',
                'Pain Sensitivity',
                'Addiction Risk Panel',
                'Mental Traits (Warrior/Worrier)',
                'Sensory Traits (Supertaster, Smell, Hearing)',
                'Ancient Population Matching (Vikings, Romans, etc.)',
                'Personalized Supplement/Diet/Exercise Plan'
            ],
            'analysis_date': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M'),
            'confidence_note': 'Results based on available genetic markers. Consult healthcare providers for medical decisions.',
            'data_sources': '1000 Genomes Project, gnomAD, ClinVar, PharmGKB, SNPedia, GWAS Catalog'
        }


# =============================================================================
# MAIN FUNCTION FOR TESTING
# =============================================================================

def run_comprehensive_analysis(dna_df: pd.DataFrame) -> ComprehensiveResults:
    """Main entry point for running comprehensive DNA analysis"""
    engine = ComprehensiveDNAAnalysisEngine()
    return engine.run_full_analysis(dna_df)


if __name__ == "__main__":
    # Test with sample data
    sample_data = [
        {'rsid': 'rs12913832', 'chromosome': '15', 'position': 28365618, 'genotype': 'GG'},
        {'rsid': 'rs1426654', 'chromosome': '15', 'position': 48426484, 'genotype': 'AA'},
        {'rsid': 'rs16891982', 'chromosome': '5', 'position': 33951693, 'genotype': 'GG'},
        {'rsid': 'rs4988235', 'chromosome': '2', 'position': 136608646, 'genotype': 'TT'},
        {'rsid': 'rs1805007', 'chromosome': '16', 'position': 89986117, 'genotype': 'CT'},
        {'rsid': 'rs762551', 'chromosome': '15', 'position': 75041917, 'genotype': 'AA'},
        {'rsid': 'rs1815739', 'chromosome': '11', 'position': 66560624, 'genotype': 'CT'},
        {'rsid': 'rs7903146', 'chromosome': '10', 'position': 114758349, 'genotype': 'CC'},
        {'rsid': 'rs1801133', 'chromosome': '1', 'position': 11856378, 'genotype': 'CT'},
    ]

    df = pd.DataFrame(sample_data)
    results = run_comprehensive_analysis(df)

    print("=" * 60)
    print("COMPREHENSIVE DNA ANALYSIS RESULTS")
    print("=" * 60)
    print(f"\nAncestry: {results.ancestry['composition']}")
    print(f"\nPhysical Traits: {len(results.physical_traits)} analyzed")
    print(f"Health Traits: {len(results.health_traits)} analyzed")
    print(f"Pharmacogenomics: {len(results.pharmacogenomics.get('gene_results', {}))} genes")
