#!/usr/bin/env python3
"""
Sensory Genetics Database - Comprehensive Version
Real SNPs for taste, smell, hearing, and other sensory traits
"""
from typing import Dict, Any

def get_genotype_key(genotype, dict_keys):
    """Find matching genotype key trying all orientations."""
    if not genotype:
        return None
    genotype = genotype.upper()
    if genotype in dict_keys:
        return genotype
    rev = genotype[::-1]
    if rev in dict_keys:
        return rev
    comp_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    comp = ''.join(comp_map.get(b, b) for b in genotype)
    if comp in dict_keys:
        return comp
    rev_comp = comp[::-1]
    if rev_comp in dict_keys:
        return rev_comp
    return None

# ============================================================================
# TASTE GENETICS
# ============================================================================

BITTER_TASTE_SNPS = {
    # TAS2R38 - Primary bitter taste receptor (PTC/PROP tasting)
    'rs713598': {
        'gene': 'TAS2R38',
        'variant_name': 'A49P',
        'function': 'Bitter taste receptor - determines PTC/PROP tasting ability',
        'GG': {'phenotype': 'Non-taster', 'score': 0, 'description': 'Cannot taste bitter PTC/PROP compounds'},
        'CG': {'phenotype': 'Medium taster', 'score': 1, 'description': 'Moderate bitter taste sensitivity'},
        'CC': {'phenotype': 'Supertaster', 'score': 2, 'description': 'Very sensitive to bitter tastes'}
    },
    'rs1726866': {
        'gene': 'TAS2R38',
        'variant_name': 'V262A',
        'function': 'Bitter taste receptor variant - affects taste sensitivity',
        'TT': {'phenotype': 'Non-taster', 'score': 0},
        'CT': {'phenotype': 'Medium taster', 'score': 1},
        'CC': {'phenotype': 'Supertaster', 'score': 2}
    },
    'rs10246939': {
        'gene': 'TAS2R38',
        'variant_name': 'I296V',
        'function': 'Bitter taste receptor haplotype marker',
        'CC': {'phenotype': 'Non-taster', 'score': 0},
        'CT': {'phenotype': 'Medium taster', 'score': 1},
        'TT': {'phenotype': 'Supertaster', 'score': 2}
    },
    # TAS2R16 - Beta-glucoside bitter taste
    'rs846664': {
        'gene': 'TAS2R16',
        'variant_name': 'K172N',
        'function': 'Beta-glucoside bitter compounds detection (salicin)',
        'TT': {'phenotype': 'Normal taster', 'score': 1},
        'CT': {'phenotype': 'Sensitive', 'score': 2},
        'CC': {'phenotype': 'Very sensitive', 'score': 2, 'description': 'Highly sensitive to salicin and glucosides'}
    },
    'rs978739': {
        'gene': 'TAS2R16',
        'variant_name': 'H212R',
        'function': 'Salicin bitter taste sensitivity',
        'CC': {'phenotype': 'Normal', 'score': 1},
        'CT': {'phenotype': 'Enhanced', 'score': 2},
        'TT': {'phenotype': 'Highly enhanced', 'score': 2}
    },
    # TAS2R19 - Quinine bitter taste
    'rs10772420': {
        'gene': 'TAS2R19',
        'variant_name': 'R299C',
        'function': 'Quinine bitter taste (tonic water)',
        'GG': {'phenotype': 'Very sensitive to quinine', 'score': 2},
        'AG': {'phenotype': 'Moderately sensitive', 'score': 1},
        'AA': {'phenotype': 'Less sensitive to quinine', 'score': 0}
    },
    # TAS2R31 - Acesulfame K and saccharin bitter aftertaste
    'rs10845295': {
        'gene': 'TAS2R31',
        'variant_name': 'W35S',
        'function': 'Artificial sweetener bitter aftertaste detection',
        'CC': {'phenotype': 'Tastes bitter aftertaste', 'score': 2, 'description': 'Detects bitter in artificial sweeteners'},
        'CT': {'phenotype': 'Slight aftertaste', 'score': 1},
        'TT': {'phenotype': 'No aftertaste', 'score': 0}
    },
    # TAS2R43 - Aristolochic acid and aloin bitter
    'rs2708377': {
        'gene': 'TAS2R43',
        'variant_name': 'W35C',
        'function': 'Aristolochic acid bitter detection',
        'GG': {'phenotype': 'Normal', 'score': 1},
        'AG': {'phenotype': 'Sensitive', 'score': 2},
        'AA': {'phenotype': 'Very sensitive', 'score': 2}
    },
    # TAS2R50 - Andrographolide bitter
    'rs1376251': {
        'gene': 'TAS2R50',
        'variant_name': 'P259T',
        'function': 'Andrographolide bitter taste (herbal medicine)',
        'TT': {'phenotype': 'Non-functional', 'score': 0},
        'CT': {'phenotype': 'Partially functional', 'score': 1},
        'CC': {'phenotype': 'Functional taster', 'score': 2}
    },
    # TAS2R3 - Chloroquine bitter
    'rs765007': {
        'gene': 'TAS2R3',
        'variant_name': 'S7N',
        'function': 'Chloroquine and related compounds bitter detection',
        'AA': {'phenotype': 'Less sensitive', 'score': 0},
        'AG': {'phenotype': 'Normal', 'score': 1},
        'GG': {'phenotype': 'Sensitive', 'score': 2}
    },
    # TAS2R4 - Denatonium bitter
    'rs2233998': {
        'gene': 'TAS2R4',
        'variant_name': 'V96L',
        'function': 'Denatonium (most bitter known compound) sensitivity',
        'GG': {'phenotype': 'Normal', 'score': 1},
        'AG': {'phenotype': 'Enhanced', 'score': 2},
        'AA': {'phenotype': 'Highly enhanced', 'score': 2}
    },
    # TAS2R5 - Propylthiouracil related
    'rs2227264': {
        'gene': 'TAS2R5',
        'variant_name': 'S7F',
        'function': 'Propylthiouracil related bitter compounds',
        'CC': {'phenotype': 'Normal', 'score': 1},
        'CT': {'phenotype': 'Sensitive', 'score': 2},
        'TT': {'phenotype': 'Very sensitive', 'score': 2}
    },
    # TAS2R9 - Ofloxacin bitter
    'rs3741845': {
        'gene': 'TAS2R9',
        'variant_name': 'A187V',
        'function': 'Ofloxacin (antibiotic) bitter taste',
        'CC': {'phenotype': 'Less bitter', 'score': 0},
        'CT': {'phenotype': 'Normal', 'score': 1},
        'TT': {'phenotype': 'Very bitter', 'score': 2}
    },
    # TAS2R14 - Broad bitter receptor
    'rs3741843': {
        'gene': 'TAS2R14',
        'variant_name': 'T86A',
        'function': 'Broad bitter compound detection (alkaloids, flavonoids)',
        'GG': {'phenotype': 'Normal', 'score': 1},
        'AG': {'phenotype': 'Enhanced', 'score': 2},
        'AA': {'phenotype': 'Highly enhanced', 'score': 2}
    },
    # TAS2R20 - Cromolyn bitter
    'rs1868769': {
        'gene': 'TAS2R20',
        'variant_name': 'H58Y',
        'function': 'Cromolyn sodium bitter taste',
        'CC': {'phenotype': 'Less sensitive', 'score': 0},
        'CT': {'phenotype': 'Normal', 'score': 1},
        'TT': {'phenotype': 'Sensitive', 'score': 2}
    },
    # TAS2R46 - Multiple bitter agonists
    'rs2540431': {
        'gene': 'TAS2R46',
        'variant_name': 'V227L',
        'function': 'Strychnine and absinthin bitter detection',
        'AA': {'phenotype': 'Less sensitive', 'score': 0},
        'AG': {'phenotype': 'Normal', 'score': 1},
        'GG': {'phenotype': 'Sensitive', 'score': 2}
    },
    # GNAT3 - Gustducin alpha subunit (taste signaling)
    'rs7792845': {
        'gene': 'GNAT3',
        'variant_name': 'Intronic',
        'function': 'Taste signal transduction - affects overall bitter perception',
        'CC': {'phenotype': 'Normal signaling', 'score': 1},
        'CT': {'phenotype': 'Enhanced signaling', 'score': 2},
        'TT': {'phenotype': 'Reduced signaling', 'score': 0}
    },
    # CA6 - Gustin carbonic anhydrase
    'rs2274333': {
        'gene': 'CA6',
        'variant_name': 'S90G',
        'function': 'Gustin protein - zinc binding affects taste bud function',
        'GG': {'phenotype': 'Normal function', 'score': 1, 'description': 'Normal taste bud zinc levels'},
        'AG': {'phenotype': 'Slightly reduced', 'score': 1},
        'AA': {'phenotype': 'Reduced gustin function', 'score': 0, 'description': 'May have altered taste perception due to zinc'}
    }
}

SWEET_TASTE_SNPS = {
    # TAS1R2 - Primary sweet receptor component
    'rs35874116': {
        'gene': 'TAS1R2',
        'variant_name': 'I191V',
        'function': 'Sweet taste receptor - primary sugar detection',
        'TT': {'phenotype': 'Reduced sweet taste', 'score': 0, 'description': 'Lower sensitivity to sweetness'},
        'CT': {'phenotype': 'Normal sweet taste', 'score': 1},
        'CC': {'phenotype': 'Enhanced sweet taste', 'score': 2, 'description': 'Higher sensitivity to sugars'}
    },
    'rs12033832': {
        'gene': 'TAS1R2',
        'variant_name': 'Regulatory',
        'function': 'Sweet receptor expression level',
        'AA': {'phenotype': 'Normal expression', 'score': 1},
        'AG': {'phenotype': 'Slightly higher', 'score': 1},
        'GG': {'phenotype': 'Higher expression', 'score': 2, 'description': 'More sweet receptors'}
    },
    'rs4920566': {
        'gene': 'TAS1R2',
        'variant_name': 'Intronic',
        'function': 'Sweet taste sensitivity modifier',
        'AA': {'phenotype': 'Standard', 'score': 1},
        'AG': {'phenotype': 'Slightly enhanced', 'score': 1},
        'GG': {'phenotype': 'Enhanced', 'score': 2}
    },
    # TAS1R3 - Sweet/Umami shared subunit
    'rs307355': {
        'gene': 'TAS1R3',
        'variant_name': 'C/T Promoter',
        'function': 'Sweet/umami receptor subunit expression',
        'CC': {'phenotype': 'Normal', 'score': 1},
        'CT': {'phenotype': 'Normal', 'score': 1},
        'TT': {'phenotype': 'Reduced', 'score': 0}
    },
    'rs35744813': {
        'gene': 'TAS1R3',
        'variant_name': 'R757C',
        'function': 'Sweet receptor binding efficiency',
        'CC': {'phenotype': 'Normal binding', 'score': 1},
        'CT': {'phenotype': 'Altered binding', 'score': 0},
        'TT': {'phenotype': 'Reduced function', 'score': 0}
    },
    'rs41278020': {
        'gene': 'TAS1R3',
        'variant_name': 'Upstream',
        'function': 'Sweet taste intensity perception',
        'GG': {'phenotype': 'Normal intensity', 'score': 1},
        'AG': {'phenotype': 'Enhanced', 'score': 2},
        'AA': {'phenotype': 'Highly enhanced', 'score': 2}
    },
    # GLUT2/SLC2A2 - Glucose sensing (sweet taste modulator)
    'rs5400': {
        'gene': 'SLC2A2',
        'variant_name': 'T110I',
        'function': 'Glucose transporter in taste cells - affects sweet preference',
        'CC': {'phenotype': 'Normal glucose sensing', 'score': 1},
        'CT': {'phenotype': 'Altered sensing', 'score': 1},
        'TT': {'phenotype': 'Reduced sensing', 'score': 0, 'description': 'May prefer sweeter foods'}
    },
    'rs11920090': {
        'gene': 'SLC2A2',
        'variant_name': 'Intronic',
        'function': 'Sugar preference modifier',
        'AA': {'phenotype': 'Normal preference', 'score': 1},
        'AT': {'phenotype': 'Higher preference', 'score': 2},
        'TT': {'phenotype': 'Strong sweet preference', 'score': 2}
    },
    # FGF21 - Sweet preference hormone
    'rs838133': {
        'gene': 'FGF21',
        'variant_name': 'A/G Regulatory',
        'function': 'Fibroblast growth factor - regulates sweet/carb preference',
        'GG': {'phenotype': 'Normal sweet preference', 'score': 1},
        'AG': {'phenotype': 'Lower sweet preference', 'score': 0},
        'AA': {'phenotype': 'Reduced sweet preference', 'score': 0, 'description': 'Less likely to prefer sweets'}
    },
    'rs838145': {
        'gene': 'FGF21',
        'variant_name': 'Intronic',
        'function': 'Carbohydrate preference',
        'CC': {'phenotype': 'Normal carb preference', 'score': 1},
        'CT': {'phenotype': 'Higher carb preference', 'score': 2},
        'TT': {'phenotype': 'Strong carb craving', 'score': 2}
    }
}

UMAMI_TASTE_SNPS = {
    # TAS1R1 - Primary umami receptor
    'rs34160967': {
        'gene': 'TAS1R1',
        'variant_name': 'A372T',
        'function': 'Umami taste receptor - MSG/glutamate detection',
        'AA': {'phenotype': 'Enhanced umami', 'score': 2, 'description': 'Strong savory taste perception'},
        'AG': {'phenotype': 'Normal umami', 'score': 1},
        'GG': {'phenotype': 'Reduced umami', 'score': 0}
    },
    'rs41278020': {
        'gene': 'TAS1R1',
        'variant_name': 'Regulatory',
        'function': 'Umami receptor expression',
        'GG': {'phenotype': 'Normal', 'score': 1},
        'AG': {'phenotype': 'Enhanced', 'score': 2},
        'AA': {'phenotype': 'Highly enhanced', 'score': 2}
    },
    # mGluR4/GRM4 - Metabotropic glutamate receptor (umami)
    'rs2451091': {
        'gene': 'GRM4',
        'variant_name': 'Intronic',
        'function': 'Glutamate receptor - umami enhancement',
        'TT': {'phenotype': 'Normal umami', 'score': 1},
        'CT': {'phenotype': 'Enhanced', 'score': 2},
        'CC': {'phenotype': 'Strong umami perception', 'score': 2}
    },
    'rs937039': {
        'gene': 'GRM4',
        'variant_name': 'Intronic',
        'function': 'Glutamate signaling efficiency',
        'AA': {'phenotype': 'Normal', 'score': 1},
        'AG': {'phenotype': 'Enhanced', 'score': 2},
        'GG': {'phenotype': 'Strong glutamate detection', 'score': 2}
    }
}

# ============================================================================
# SALTY TASTE GENETICS
# ============================================================================

SALTY_TASTE_SNPS = {
    # ENaC sodium channels - main salt taste receptors
    'rs239345': {
        'gene': 'SCNN1A',
        'variant_name': 'A663T',
        'function': 'Epithelial sodium channel alpha - salt taste detection',
        'TT': {'phenotype': 'Normal salt taste', 'sensitivity': 'Normal'},
        'CT': {'phenotype': 'Enhanced salt taste', 'sensitivity': 'High'},
        'CC': {'phenotype': 'Very sensitive to salt', 'sensitivity': 'Very high'}
    },
    'rs2228576': {
        'gene': 'SCNN1B',
        'variant_name': 'T594M',
        'function': 'Sodium channel beta - salt preference',
        'CC': {'phenotype': 'Normal salt preference', 'sensitivity': 'Normal'},
        'CT': {'phenotype': 'Lower salt preference', 'sensitivity': 'High'},
        'TT': {'phenotype': 'Salt aversion', 'sensitivity': 'Very high'}
    },
    'rs5742912': {
        'gene': 'SCNN1G',
        'variant_name': 'V546I',
        'function': 'Sodium channel gamma - salt taste intensity',
        'GG': {'phenotype': 'Normal intensity', 'sensitivity': 'Normal'},
        'AG': {'phenotype': 'Heightened intensity', 'sensitivity': 'High'},
        'AA': {'phenotype': 'Strong salt perception', 'sensitivity': 'Very high'}
    },
    # TRPV1 - Non-ENaC salt taste pathway
    'rs8065080': {
        'gene': 'TRPV1',
        'variant_name': 'I585V',
        'function': 'Capsaicin receptor - also involved in salt taste',
        'CC': {'phenotype': 'Normal salt response', 'sensitivity': 'Normal'},
        'CT': {'phenotype': 'Altered salt response', 'sensitivity': 'Altered'},
        'TT': {'phenotype': 'Reduced salt detection', 'sensitivity': 'Low'}
    }
}

# ============================================================================
# SOUR TASTE GENETICS
# ============================================================================

SOUR_TASTE_SNPS = {
    # PKD2L1 - Polycystic kidney disease 2-like 1 (sour taste)
    'rs7512931': {
        'gene': 'PKD2L1',
        'variant_name': 'Intronic',
        'function': 'Sour taste receptor channel',
        'TT': {'phenotype': 'Normal sour taste', 'sensitivity': 'Normal'},
        'GT': {'phenotype': 'Enhanced sour sensitivity', 'sensitivity': 'High'},
        'GG': {'phenotype': 'Very sour sensitive', 'sensitivity': 'Very high'}
    },
    # PKD1L3 - Partner to PKD2L1
    'rs10278721': {
        'gene': 'PKD1L3',
        'variant_name': 'Intronic',
        'function': 'Sour taste receptor co-factor',
        'CC': {'phenotype': 'Normal sour detection', 'sensitivity': 'Normal'},
        'CT': {'phenotype': 'Altered sensitivity', 'sensitivity': 'Altered'},
        'TT': {'phenotype': 'Reduced sensitivity', 'sensitivity': 'Low'}
    },
    # ASIC2 - Acid sensing ion channel
    'rs2282154': {
        'gene': 'ASIC2',
        'variant_name': 'Intronic',
        'function': 'Acid sensing - sour taste intensity',
        'CC': {'phenotype': 'Normal acid sensing', 'sensitivity': 'Normal'},
        'CT': {'phenotype': 'Enhanced acid sensing', 'sensitivity': 'High'},
        'TT': {'phenotype': 'Strong sour perception', 'sensitivity': 'Very high'}
    },
    # OTOP1 - Otopetrin 1 (discovered 2019, main sour receptor)
    'rs11761556': {
        'gene': 'OTOP1',
        'variant_name': 'Intronic',
        'function': 'Primary sour taste proton channel',
        'AA': {'phenotype': 'Normal sour taste', 'sensitivity': 'Normal'},
        'AG': {'phenotype': 'Enhanced sour detection', 'sensitivity': 'High'},
        'GG': {'phenotype': 'Highly sensitive to sour', 'sensitivity': 'Very high'}
    }
}

# ============================================================================
# SMELL GENETICS - OLFACTORY RECEPTORS
# ============================================================================

CILANTRO_SNPS = {
    'rs72921001': {
        'gene': 'OR6A2',
        'variant_name': 'A/C SNP',
        'function': 'Olfactory receptor - detects aldehyde in cilantro',
        'CC': {'phenotype': 'Normal', 'tastes_soapy': False, 'description': 'Cilantro tastes normal/herbal'},
        'AC': {'phenotype': 'Slightly soapy', 'tastes_soapy': True, 'description': 'May detect slight soapy taste'},
        'AA': {'phenotype': 'Tastes soapy', 'tastes_soapy': True, 'description': 'Strong soapy/metallic taste from cilantro'}
    },
    # Additional cilantro-related ORs
    'rs2001157': {
        'gene': 'OR6A2',
        'variant_name': 'Upstream',
        'function': 'Cilantro aldehyde detection modifier',
        'GG': {'phenotype': 'Normal', 'tastes_soapy': False},
        'AG': {'phenotype': 'May taste soapy', 'tastes_soapy': True},
        'AA': {'phenotype': 'Soapy taste', 'tastes_soapy': True}
    }
}

ASPARAGUS_SMELL_SNPS = {
    'rs4481887': {
        'gene': 'OR2M7',
        'variant_name': 'G/A SNP',
        'function': 'Asparagus metabolite detection (methanethiol)',
        'GG': {'phenotype': 'Can smell strongly', 'can_smell': True, 'description': 'Detects asparagus pee smell'},
        'AG': {'phenotype': 'Can smell', 'can_smell': True},
        'AA': {'phenotype': 'Cannot smell', 'can_smell': False, 'description': 'Asparagus-specific anosmia'}
    },
    'rs2337326': {
        'gene': 'OR2M7',
        'variant_name': 'Upstream',
        'function': 'Asparagus metabolite receptor expression',
        'CC': {'phenotype': 'Strong detection', 'can_smell': True},
        'CT': {'phenotype': 'Normal detection', 'can_smell': True},
        'TT': {'phenotype': 'Weak detection', 'can_smell': False}
    }
}

SMELL_SENSITIVITY_SNPS = {
    # OR7D4 - Androstenone (sweat/urine smell)
    'rs28757581': {
        'gene': 'OR7D4',
        'variant_name': 'R88W',
        'function': 'Androstenone detection (sweaty/urine-like smell in pork)',
        'CC': {'phenotype': 'Can smell strongly', 'sensitivity': 'High', 'description': 'Finds androstenone unpleasant'},
        'CT': {'phenotype': 'Can smell', 'sensitivity': 'Normal'},
        'TT': {'phenotype': 'Cannot smell', 'sensitivity': 'Low', 'description': 'Androstenone-specific anosmia'}
    },
    'rs61729907': {
        'gene': 'OR7D4',
        'variant_name': 'T133M',
        'function': 'Androstenone pleasantness perception',
        'CC': {'phenotype': 'Unpleasant smell', 'sensitivity': 'High'},
        'CT': {'phenotype': 'Neutral', 'sensitivity': 'Normal'},
        'TT': {'phenotype': 'Pleasant or no smell', 'sensitivity': 'Low'}
    },
    # OR11H7P - Isovaleric acid (sweaty feet smell)
    'rs2298885': {
        'gene': 'OR11H7P',
        'variant_name': 'Promoter',
        'function': 'Isovaleric acid detection (sweaty/cheesy smell)',
        'AA': {'phenotype': 'Strong detector', 'sensitivity': 'High'},
        'AG': {'phenotype': 'Normal detection', 'sensitivity': 'Normal'},
        'GG': {'phenotype': 'Weak detection', 'sensitivity': 'Low'}
    },
    # OR2J3 - Cis-3-hexen-1-ol (fresh cut grass smell)
    'rs3761953': {
        'gene': 'OR2J3',
        'variant_name': 'T113A',
        'function': 'Green/grassy smell detection (cis-3-hexenol)',
        'GG': {'phenotype': 'Strong grass smell', 'sensitivity': 'High'},
        'AG': {'phenotype': 'Normal', 'sensitivity': 'Normal'},
        'AA': {'phenotype': 'Reduced grass smell', 'sensitivity': 'Low'}
    },
    # OR5A1 - Beta-ionone (violet/floral smell)
    'rs6591536': {
        'gene': 'OR5A1',
        'variant_name': 'D183N',
        'function': 'Beta-ionone detection (violet/floral aroma)',
        'AA': {'phenotype': 'Cannot smell violets', 'sensitivity': 'Very low', 'description': 'Beta-ionone anosmia'},
        'AG': {'phenotype': 'Reduced floral smell', 'sensitivity': 'Low'},
        'GG': {'phenotype': 'Normal floral detection', 'sensitivity': 'Normal'}
    },
    # OR2W1 - Carvone detection (spearmint vs caraway)
    'rs12138060': {
        'gene': 'OR2W1',
        'variant_name': 'M267T',
        'function': 'Carvone enantiomer detection (mint vs caraway)',
        'GG': {'phenotype': 'Detects both forms', 'sensitivity': 'High'},
        'AG': {'phenotype': 'Normal detection', 'sensitivity': 'Normal'},
        'AA': {'phenotype': 'Reduced carvone smell', 'sensitivity': 'Low'}
    },
    # OR10G4 - Guaiacol (smoky smell)
    'rs10828489': {
        'gene': 'OR10G4',
        'variant_name': 'Intronic',
        'function': 'Guaiacol detection (smoky/bacon smell)',
        'TT': {'phenotype': 'Strong smoky detection', 'sensitivity': 'High'},
        'CT': {'phenotype': 'Normal', 'sensitivity': 'Normal'},
        'CC': {'phenotype': 'Reduced smoky smell', 'sensitivity': 'Low'}
    },
    # OR1A1 - Geraniol (rose smell)
    'rs17762735': {
        'gene': 'OR1A1',
        'variant_name': 'N183D',
        'function': 'Geraniol detection (rose/floral smell)',
        'CC': {'phenotype': 'Strong rose smell', 'sensitivity': 'High'},
        'CT': {'phenotype': 'Normal', 'sensitivity': 'Normal'},
        'TT': {'phenotype': 'Reduced rose smell', 'sensitivity': 'Low'}
    },
    # OR2B6 - Musk detection
    'rs760822': {
        'gene': 'OR2B6',
        'variant_name': 'G/A SNP',
        'function': 'Musk/perfume detection',
        'GG': {'phenotype': 'Strong musk detection', 'sensitivity': 'High'},
        'AG': {'phenotype': 'Normal', 'sensitivity': 'Normal'},
        'AA': {'phenotype': 'Musk anosmia', 'sensitivity': 'Low', 'description': 'Cannot smell certain musks'}
    },
    # OR52D1 - Body odor detection
    'rs1453541': {
        'gene': 'OR52D1',
        'variant_name': 'Intronic',
        'function': 'Body odor and sweat detection',
        'AA': {'phenotype': 'Sensitive to body odor', 'sensitivity': 'High'},
        'AG': {'phenotype': 'Normal', 'sensitivity': 'Normal'},
        'GG': {'phenotype': 'Less sensitive', 'sensitivity': 'Low'}
    },
    # OR51E2 - Prostate-specific olfactory receptor
    'rs4964446': {
        'gene': 'OR51E2',
        'variant_name': 'Intronic',
        'function': 'Beta-ionone and other odor detection',
        'TT': {'phenotype': 'Enhanced detection', 'sensitivity': 'High'},
        'CT': {'phenotype': 'Normal', 'sensitivity': 'Normal'},
        'CC': {'phenotype': 'Reduced', 'sensitivity': 'Low'}
    }
}

# Additional specific smell SNPs
FISH_SMELL_SNPS = {
    # FMO3 - Trimethylaminuria (fish odor syndrome)
    'rs2266782': {
        'gene': 'FMO3',
        'variant_name': 'E158K',
        'function': 'Trimethylamine metabolism - fish odor syndrome carrier',
        'GG': {'phenotype': 'Normal metabolism', 'carrier': False},
        'AG': {'phenotype': 'Carrier', 'carrier': True, 'description': 'Carrier for fish odor syndrome'},
        'AA': {'phenotype': 'Affected', 'carrier': True, 'description': 'May have fish body odor'}
    },
    'rs1736557': {
        'gene': 'FMO3',
        'variant_name': 'V257M',
        'function': 'Trimethylamine processing',
        'GG': {'phenotype': 'Normal', 'carrier': False},
        'AG': {'phenotype': 'Slightly reduced', 'carrier': False},
        'AA': {'phenotype': 'Reduced metabolism', 'carrier': True}
    },
    'rs2266780': {
        'gene': 'FMO3',
        'variant_name': 'E308G',
        'function': 'TMA N-oxygenation activity',
        'AA': {'phenotype': 'Normal', 'carrier': False},
        'AG': {'phenotype': 'Carrier', 'carrier': True},
        'GG': {'phenotype': 'Reduced function', 'carrier': True}
    }
}

BODY_ODOR_SNPS = {
    # ABCC11 - Earwax type and body odor
    'rs17822931': {
        'gene': 'ABCC11',
        'variant_name': 'G180R',
        'function': 'Determines earwax type AND body odor production',
        'GG': {'phenotype': 'Wet earwax, body odor', 'earwax': 'Wet', 'body_odor': 'Normal'},
        'AG': {'phenotype': 'Mixed', 'earwax': 'Mixed', 'body_odor': 'Reduced'},
        'AA': {'phenotype': 'Dry earwax, less body odor', 'earwax': 'Dry', 'body_odor': 'Very low', 'description': 'Minimal underarm odor - common in East Asians'}
    }
}

GENERAL_OLFACTION_SNPS = {
    # CNGA2 - Cyclic nucleotide gated channel (smell signal)
    'rs2071283': {
        'gene': 'CNGA2',
        'variant_name': 'Intronic',
        'function': 'Olfactory signal transduction',
        'AA': {'phenotype': 'Normal olfaction', 'sensitivity': 'Normal'},
        'AG': {'phenotype': 'Slightly reduced', 'sensitivity': 'Slightly reduced'},
        'GG': {'phenotype': 'Reduced smell', 'sensitivity': 'Low'}
    },
    # ADCY3 - Adenylyl cyclase 3 (smell signaling)
    'rs11676272': {
        'gene': 'ADCY3',
        'variant_name': 'Intronic',
        'function': 'Olfactory signaling pathway',
        'GG': {'phenotype': 'Normal signaling', 'sensitivity': 'Normal'},
        'AG': {'phenotype': 'Normal', 'sensitivity': 'Normal'},
        'AA': {'phenotype': 'Altered signaling', 'sensitivity': 'Altered'}
    },
    # ANO2 - Anoctamin 2 (olfactory calcium-activated chloride channel)
    'rs2578921': {
        'gene': 'ANO2',
        'variant_name': 'Intronic',
        'function': 'Olfactory neuron signaling',
        'CC': {'phenotype': 'Normal', 'sensitivity': 'Normal'},
        'CT': {'phenotype': 'Enhanced', 'sensitivity': 'High'},
        'TT': {'phenotype': 'Highly sensitive', 'sensitivity': 'Very high'}
    },
    # OMP - Olfactory marker protein
    'rs1806713': {
        'gene': 'OMP',
        'variant_name': 'Promoter',
        'function': 'Olfactory neuron maturation and function',
        'GG': {'phenotype': 'Normal smell', 'sensitivity': 'Normal'},
        'AG': {'phenotype': 'Normal', 'sensitivity': 'Normal'},
        'AA': {'phenotype': 'Altered olfaction', 'sensitivity': 'Altered'}
    }
}

# ============================================================================
# ALCOHOL FLUSH
# ============================================================================

ALCOHOL_FLUSH_SNPS = {
    'rs671': {
        'gene': 'ALDH2',
        'function': 'Aldehyde dehydrogenase - alcohol metabolism',
        'GG': {'phenotype': 'Normal metabolism', 'has_flush': False, 'risk': 'Normal'},
        'AG': {'phenotype': 'Flush reaction', 'has_flush': True, 'risk': 'Increased esophageal cancer risk with alcohol'},
        'AA': {'phenotype': 'Strong flush', 'has_flush': True, 'risk': 'High risk - avoid alcohol'}
    }
}

# ============================================================================
# CAFFEINE METABOLISM
# ============================================================================

CAFFEINE_SNPS = {
    'rs762551': {
        'gene': 'CYP1A2',
        'function': 'Caffeine metabolism enzyme',
        'AA': {'phenotype': 'Fast metabolizer', 'metabolism': 'Fast', 'sensitivity': 'Low'},
        'AC': {'phenotype': 'Normal metabolizer', 'metabolism': 'Normal', 'sensitivity': 'Moderate'},
        'CC': {'phenotype': 'Slow metabolizer', 'metabolism': 'Slow', 'sensitivity': 'High'}
    }
}

# ============================================================================
# HEARING GENETICS
# ============================================================================

HEARING_SNPS = {
    # Noise-induced hearing loss
    'rs1801253': {
        'gene': 'ADRB1',
        'variant_name': 'R389G',
        'function': 'Beta-adrenergic receptor - noise-induced hearing loss susceptibility',
        'CC': {'phenotype': 'Normal', 'risk': 'Average'},
        'CG': {'phenotype': 'Normal', 'risk': 'Average'},
        'GG': {'phenotype': 'Increased NIHL risk', 'risk': 'Elevated', 'description': 'More susceptible to loud noise damage'}
    },
    # Age-related hearing loss (presbycusis)
    'rs7294919': {
        'gene': 'HMGA2',
        'variant_name': 'Intronic',
        'function': 'Age-related hearing loss (presbycusis)',
        'CC': {'phenotype': 'Normal', 'risk': 'Average'},
        'CT': {'phenotype': 'Normal', 'risk': 'Average'},
        'TT': {'phenotype': 'Increased presbycusis risk', 'risk': 'Elevated'}
    },
    # GJB2 - Connexin 26 (most common deafness gene)
    'rs80338939': {
        'gene': 'GJB2',
        'variant_name': '35delG',
        'function': 'Connexin 26 - most common hereditary deafness mutation',
        'II': {'phenotype': 'Normal hearing', 'risk': 'Normal', 'carrier': False},
        'DI': {'phenotype': 'Carrier', 'risk': 'Carrier', 'carrier': True, 'description': 'Carrier for hereditary deafness'},
        'DD': {'phenotype': 'Affected', 'risk': 'High', 'carrier': True}
    },
    'rs72474224': {
        'gene': 'GJB2',
        'variant_name': 'M34T',
        'function': 'Connexin 26 variant - mild hearing loss',
        'CC': {'phenotype': 'Normal', 'risk': 'Normal'},
        'CT': {'phenotype': 'Carrier/Mild risk', 'risk': 'Slightly elevated'},
        'TT': {'phenotype': 'Mild hearing loss risk', 'risk': 'Elevated'}
    },
    'rs35887622': {
        'gene': 'GJB2',
        'variant_name': 'V37I',
        'function': 'Connexin 26 - moderate hearing loss variant',
        'GG': {'phenotype': 'Normal', 'risk': 'Normal'},
        'AG': {'phenotype': 'Carrier', 'risk': 'Carrier'},
        'AA': {'phenotype': 'Moderate hearing loss risk', 'risk': 'Elevated'}
    },
    # GJB6 - Connexin 30
    'rs1325928': {
        'gene': 'GJB6',
        'variant_name': 'Intronic',
        'function': 'Connexin 30 - gap junction for hearing',
        'AA': {'phenotype': 'Normal', 'risk': 'Normal'},
        'AG': {'phenotype': 'Normal', 'risk': 'Normal'},
        'GG': {'phenotype': 'Slightly increased risk', 'risk': 'Slightly elevated'}
    },
    # SLC26A4 - Pendred syndrome
    'rs111033253': {
        'gene': 'SLC26A4',
        'variant_name': 'L236P',
        'function': 'Pendrin - Pendred syndrome (hearing loss + thyroid)',
        'CC': {'phenotype': 'Normal', 'risk': 'Normal'},
        'CT': {'phenotype': 'Carrier', 'risk': 'Carrier'},
        'TT': {'phenotype': 'Pendred syndrome risk', 'risk': 'High'}
    },
    # CDH23 - Cadherin 23 (Usher syndrome, age-related)
    'rs1227049': {
        'gene': 'CDH23',
        'variant_name': 'Intronic',
        'function': 'Hair cell tip-link - age-related hearing loss',
        'TT': {'phenotype': 'Normal', 'risk': 'Normal'},
        'CT': {'phenotype': 'Normal', 'risk': 'Normal'},
        'CC': {'phenotype': 'Increased age-related loss', 'risk': 'Elevated'}
    },
    'rs3752752': {
        'gene': 'CDH23',
        'variant_name': 'F1888S',
        'function': 'Usher syndrome Type 1D carrier status',
        'TT': {'phenotype': 'Normal', 'risk': 'Normal'},
        'CT': {'phenotype': 'Carrier', 'risk': 'Carrier'},
        'CC': {'phenotype': 'Affected risk', 'risk': 'High'}
    },
    # KCNQ4 - Potassium channel (DFNA2 deafness)
    'rs72561779': {
        'gene': 'KCNQ4',
        'variant_name': 'W276S',
        'function': 'Potassium channel in cochlea - progressive hearing loss',
        'GG': {'phenotype': 'Normal', 'risk': 'Normal'},
        'AG': {'phenotype': 'DFNA2 risk', 'risk': 'Elevated'},
        'AA': {'phenotype': 'Progressive hearing loss', 'risk': 'High'}
    },
    # MYH9 - Myosin heavy chain
    'rs11912691': {
        'gene': 'MYH9',
        'variant_name': 'Intronic',
        'function': 'Myosin - noise-induced and age-related hearing loss',
        'CC': {'phenotype': 'Normal', 'risk': 'Normal'},
        'CT': {'phenotype': 'Slightly elevated risk', 'risk': 'Slightly elevated'},
        'TT': {'phenotype': 'Increased NIHL risk', 'risk': 'Elevated'}
    },
    # MYO7A - Usher syndrome 1B
    'rs1052030': {
        'gene': 'MYO7A',
        'variant_name': 'R302H',
        'function': 'Myosin VIIA - Usher syndrome type 1B',
        'GG': {'phenotype': 'Normal', 'risk': 'Normal'},
        'AG': {'phenotype': 'Carrier', 'risk': 'Carrier'},
        'AA': {'phenotype': 'Usher 1B risk', 'risk': 'High'}
    },
    # TMC1 - Transmembrane channel
    'rs111033417': {
        'gene': 'TMC1',
        'variant_name': 'M418K',
        'function': 'Hair cell mechanotransduction',
        'CC': {'phenotype': 'Normal', 'risk': 'Normal'},
        'CT': {'phenotype': 'Carrier', 'risk': 'Carrier'},
        'TT': {'phenotype': 'Deafness risk', 'risk': 'High'}
    },
    # TRIOBP - Stereocilia rootlet
    'rs28379801': {
        'gene': 'TRIOBP',
        'variant_name': 'Intronic',
        'function': 'Stereocilia structure in cochlea',
        'AA': {'phenotype': 'Normal', 'risk': 'Normal'},
        'AG': {'phenotype': 'Normal', 'risk': 'Normal'},
        'GG': {'phenotype': 'Slightly increased risk', 'risk': 'Slightly elevated'}
    },
    # GRHL2 - Age-related hearing loss
    'rs10955255': {
        'gene': 'GRHL2',
        'variant_name': 'Intronic',
        'function': 'Grainyhead-like 2 - age-related hearing',
        'AA': {'phenotype': 'Normal', 'risk': 'Normal'},
        'AG': {'phenotype': 'Normal', 'risk': 'Normal'},
        'GG': {'phenotype': 'Increased presbycusis', 'risk': 'Elevated'}
    },
    # DFNB59/PJVK - Pejvakin
    'rs61737951': {
        'gene': 'PJVK',
        'variant_name': 'R183W',
        'function': 'Pejvakin - auditory neuropathy',
        'CC': {'phenotype': 'Normal', 'risk': 'Normal'},
        'CT': {'phenotype': 'Carrier', 'risk': 'Carrier'},
        'TT': {'phenotype': 'Auditory neuropathy risk', 'risk': 'High'}
    },
    # OTOF - Otoferlin (auditory neuropathy)
    'rs80356596': {
        'gene': 'OTOF',
        'variant_name': 'Q829X',
        'function': 'Otoferlin - auditory neuropathy type 1',
        'CC': {'phenotype': 'Normal', 'risk': 'Normal'},
        'CT': {'phenotype': 'Carrier', 'risk': 'Carrier'},
        'TT': {'phenotype': 'DFNB9 risk', 'risk': 'High'}
    },
    # TECTA - Tectorin alpha (tectorial membrane)
    'rs121908058': {
        'gene': 'TECTA',
        'variant_name': 'Y1870C',
        'function': 'Tectorial membrane protein',
        'AA': {'phenotype': 'Normal', 'risk': 'Normal'},
        'AG': {'phenotype': 'Hearing loss risk', 'risk': 'Elevated'},
        'GG': {'phenotype': 'High frequency loss', 'risk': 'High'}
    },
    # ACTG1 - Gamma actin (DFNA20/26)
    'rs121912891': {
        'gene': 'ACTG1',
        'variant_name': 'K118M',
        'function': 'Gamma actin in hair cells',
        'AA': {'phenotype': 'Normal', 'risk': 'Normal'},
        'AG': {'phenotype': 'Progressive loss risk', 'risk': 'Elevated'},
        'GG': {'phenotype': 'DFNA20 risk', 'risk': 'High'}
    },
    # COCH - Cochlin (DFNA9)
    'rs121908150': {
        'gene': 'COCH',
        'variant_name': 'P51S',
        'function': 'Cochlin - progressive hearing loss with vertigo',
        'CC': {'phenotype': 'Normal', 'risk': 'Normal'},
        'CT': {'phenotype': 'DFNA9 risk', 'risk': 'Elevated'},
        'TT': {'phenotype': 'DFNA9 affected', 'risk': 'High'}
    },
    # SOD2 - Oxidative stress protection
    'rs4880': {
        'gene': 'SOD2',
        'variant_name': 'A16V',
        'function': 'Mitochondrial antioxidant - protects against noise damage',
        'GG': {'phenotype': 'Lower antioxidant', 'risk': 'Elevated', 'description': 'Less protection from oxidative damage'},
        'AG': {'phenotype': 'Intermediate', 'risk': 'Slightly elevated'},
        'AA': {'phenotype': 'Normal antioxidant', 'risk': 'Normal'}
    },
    # CAT - Catalase (oxidative protection)
    'rs1001179': {
        'gene': 'CAT',
        'variant_name': '-262C/T',
        'function': 'Catalase enzyme - protects cochlea from oxidative stress',
        'CC': {'phenotype': 'Lower expression', 'risk': 'Slightly elevated'},
        'CT': {'phenotype': 'Normal', 'risk': 'Normal'},
        'TT': {'phenotype': 'Higher expression', 'risk': 'Lower'}
    },
    # GST genes - Detoxification
    'rs1695': {
        'gene': 'GSTP1',
        'variant_name': 'I105V',
        'function': 'Glutathione S-transferase - cochlear protection',
        'AA': {'phenotype': 'Normal GST', 'risk': 'Normal'},
        'AG': {'phenotype': 'Intermediate', 'risk': 'Normal'},
        'GG': {'phenotype': 'Reduced GST', 'risk': 'Slightly elevated'}
    }
}

# ============================================================================
# PAIN SENSITIVITY
# ============================================================================

PAIN_SNPS = {
    # OPRM1 - Mu-opioid receptor (primary pain receptor)
    'rs1799971': {
        'gene': 'OPRM1',
        'variant_name': 'A118G',
        'function': 'Mu-opioid receptor - main pain perception and opioid response',
        'AA': {'phenotype': 'Normal pain sensitivity', 'sensitivity': 'Average', 'opioid_response': 'Normal'},
        'AG': {'phenotype': 'Increased pain sensitivity', 'sensitivity': 'High', 'opioid_response': 'May need higher doses'},
        'GG': {'phenotype': 'Higher pain sensitivity', 'sensitivity': 'Very high', 'opioid_response': 'Reduced opioid effect'}
    },
    # COMT - Catechol-O-methyltransferase (Warrior vs Worrier)
    'rs4680': {
        'gene': 'COMT',
        'variant_name': 'V158M',
        'function': 'Dopamine/pain modulation - Warrior vs Worrier gene',
        'GG': {'phenotype': 'Higher pain threshold', 'sensitivity': 'Low', 'note': 'Warrior gene - stress resilient, higher dopamine breakdown'},
        'AG': {'phenotype': 'Average pain threshold', 'sensitivity': 'Average', 'note': 'Balanced'},
        'AA': {'phenotype': 'Lower pain threshold', 'sensitivity': 'High', 'note': 'Worrier gene - better memory/attention, slower dopamine breakdown'}
    },
    # SCN9A - Nav1.7 sodium channel (pain signaling)
    'rs6746030': {
        'gene': 'SCN9A',
        'variant_name': 'R1150W',
        'function': 'Nav1.7 sodium channel - pain signal transmission',
        'GG': {'phenotype': 'Normal pain', 'sensitivity': 'Average'},
        'AG': {'phenotype': 'Increased pain sensitivity', 'sensitivity': 'High'},
        'AA': {'phenotype': 'High pain sensitivity', 'sensitivity': 'Very high', 'description': 'Amplified pain signals'}
    },
    'rs41268673': {
        'gene': 'SCN9A',
        'variant_name': 'V991L',
        'function': 'Pain channel variant - affects pain intensity',
        'GG': {'phenotype': 'Normal', 'sensitivity': 'Average'},
        'AG': {'phenotype': 'Slightly increased', 'sensitivity': 'Slightly high'},
        'AA': {'phenotype': 'Increased pain', 'sensitivity': 'High'}
    },
    'rs3750904': {
        'gene': 'SCN9A',
        'variant_name': 'Intronic',
        'function': 'Sodium channel expression - affects pain threshold',
        'TT': {'phenotype': 'Normal', 'sensitivity': 'Average'},
        'CT': {'phenotype': 'Slightly altered', 'sensitivity': 'Slightly high'},
        'CC': {'phenotype': 'Increased sensitivity', 'sensitivity': 'High'}
    },
    # SCN10A - Nav1.8 sodium channel
    'rs12994338': {
        'gene': 'SCN10A',
        'variant_name': 'A1073V',
        'function': 'Nav1.8 - peripheral pain neuron signaling',
        'AA': {'phenotype': 'Normal', 'sensitivity': 'Average'},
        'AG': {'phenotype': 'Slightly increased', 'sensitivity': 'Slightly high'},
        'GG': {'phenotype': 'Increased peripheral pain', 'sensitivity': 'High'}
    },
    # SCN11A - Nav1.9 sodium channel
    'rs74401238': {
        'gene': 'SCN11A',
        'variant_name': 'R222H',
        'function': 'Nav1.9 - nociceptor excitability',
        'GG': {'phenotype': 'Normal', 'sensitivity': 'Average'},
        'AG': {'phenotype': 'Increased sensitivity', 'sensitivity': 'High'},
        'AA': {'phenotype': 'Pain hypersensitivity', 'sensitivity': 'Very high'}
    },
    # TRPV1 - Capsaicin receptor (heat/spicy pain)
    'rs8065080': {
        'gene': 'TRPV1',
        'variant_name': 'I585V',
        'function': 'Capsaicin receptor - heat and spicy pain detection',
        'CC': {'phenotype': 'Normal heat pain', 'sensitivity': 'Average', 'spicy_tolerance': 'Normal'},
        'CT': {'phenotype': 'Altered heat sensation', 'sensitivity': 'Slightly altered'},
        'TT': {'phenotype': 'Reduced heat/spicy pain', 'sensitivity': 'Low', 'spicy_tolerance': 'Higher'}
    },
    'rs222747': {
        'gene': 'TRPV1',
        'variant_name': 'M315I',
        'function': 'Heat/capsaicin sensitivity modifier',
        'GG': {'phenotype': 'Normal', 'sensitivity': 'Average'},
        'AG': {'phenotype': 'Slightly increased', 'sensitivity': 'Slightly high'},
        'AA': {'phenotype': 'Increased heat pain', 'sensitivity': 'High'}
    },
    # TRPA1 - Wasabi/mustard pain receptor
    'rs920829': {
        'gene': 'TRPA1',
        'variant_name': 'E179K',
        'function': 'Irritant detection - wasabi, mustard oil, cold pain',
        'GG': {'phenotype': 'Normal irritant response', 'sensitivity': 'Average'},
        'AG': {'phenotype': 'Enhanced response', 'sensitivity': 'High'},
        'AA': {'phenotype': 'Hypersensitive to irritants', 'sensitivity': 'Very high'}
    },
    'rs11988795': {
        'gene': 'TRPA1',
        'variant_name': 'Intronic',
        'function': 'Cold allodynia and chemical sensitivity',
        'GG': {'phenotype': 'Normal', 'sensitivity': 'Average'},
        'AG': {'phenotype': 'Increased cold pain', 'sensitivity': 'High'},
        'AA': {'phenotype': 'Cold hypersensitivity', 'sensitivity': 'Very high'}
    },
    # GCH1 - Pain protection gene
    'rs8007267': {
        'gene': 'GCH1',
        'variant_name': 'Promoter',
        'function': 'GTP cyclohydrolase - BH4 synthesis affects pain',
        'GG': {'phenotype': 'Normal pain', 'sensitivity': 'Average'},
        'AG': {'phenotype': 'Reduced pain', 'sensitivity': 'Low', 'note': 'Pain protective'},
        'AA': {'phenotype': 'Pain protection', 'sensitivity': 'Very low', 'note': 'Reduced chronic pain risk'}
    },
    'rs3783641': {
        'gene': 'GCH1',
        'variant_name': 'Intronic',
        'function': 'BH4 pathway - chronic pain susceptibility',
        'TT': {'phenotype': 'Normal', 'sensitivity': 'Average'},
        'AT': {'phenotype': 'Some protection', 'sensitivity': 'Slightly low'},
        'AA': {'phenotype': 'Pain protected', 'sensitivity': 'Low'}
    },
    # FAAH - Fatty acid amide hydrolase (endocannabinoid)
    'rs324420': {
        'gene': 'FAAH',
        'variant_name': 'P129T',
        'function': 'Endocannabinoid breakdown - natural pain relief system',
        'CC': {'phenotype': 'Normal endocannabinoid', 'sensitivity': 'Average'},
        'CA': {'phenotype': 'Enhanced endocannabinoid', 'sensitivity': 'Slightly low', 'note': 'Better natural pain relief'},
        'AA': {'phenotype': 'High endocannabinoid', 'sensitivity': 'Low', 'note': 'Natural pain protection, less anxiety'}
    },
    # OPRD1 - Delta-opioid receptor
    'rs1042114': {
        'gene': 'OPRD1',
        'variant_name': 'G80T',
        'function': 'Delta-opioid receptor - pain modulation',
        'GG': {'phenotype': 'Normal', 'sensitivity': 'Average'},
        'GT': {'phenotype': 'Altered response', 'sensitivity': 'Slightly high'},
        'TT': {'phenotype': 'Increased sensitivity', 'sensitivity': 'High'}
    },
    # MC1R - Redhead pain sensitivity
    'rs1805008': {
        'gene': 'MC1R',
        'variant_name': 'R160W',
        'function': 'Melanocortin receptor - redhead pain/anesthesia variant',
        'CC': {'phenotype': 'Normal', 'sensitivity': 'Average'},
        'CT': {'phenotype': 'Increased sensitivity', 'sensitivity': 'High', 'note': 'May need more anesthesia'},
        'TT': {'phenotype': 'High sensitivity', 'sensitivity': 'Very high', 'note': 'Redhead-associated, needs more anesthesia'}
    },
    'rs1805007': {
        'gene': 'MC1R',
        'variant_name': 'R151C',
        'function': 'Melanocortin receptor - red hair and pain',
        'CC': {'phenotype': 'Normal', 'sensitivity': 'Average'},
        'CT': {'phenotype': 'Carrier', 'sensitivity': 'High'},
        'TT': {'phenotype': 'Affected', 'sensitivity': 'Very high', 'note': 'Red hair, increased pain sensitivity'}
    },
    # ADRB2 - Beta-2 adrenergic receptor
    'rs1042713': {
        'gene': 'ADRB2',
        'variant_name': 'G16R',
        'function': 'Adrenergic receptor - stress-induced pain modulation',
        'GG': {'phenotype': 'Normal stress pain', 'sensitivity': 'Average'},
        'AG': {'phenotype': 'Altered response', 'sensitivity': 'Slightly high'},
        'AA': {'phenotype': 'Increased stress-pain', 'sensitivity': 'High'}
    },
    # HTR2A - Serotonin receptor 2A
    'rs6313': {
        'gene': 'HTR2A',
        'variant_name': 'T102C',
        'function': 'Serotonin receptor - pain and mood interaction',
        'CC': {'phenotype': 'Normal', 'sensitivity': 'Average'},
        'CT': {'phenotype': 'Slightly increased', 'sensitivity': 'Slightly high'},
        'TT': {'phenotype': 'Increased pain perception', 'sensitivity': 'High'}
    },
    # BDNF - Brain-derived neurotrophic factor
    'rs6265': {
        'gene': 'BDNF',
        'variant_name': 'V66M',
        'function': 'Neurotrophin - affects chronic pain development',
        'GG': {'phenotype': 'Normal BDNF', 'sensitivity': 'Average'},
        'AG': {'phenotype': 'Reduced BDNF secretion', 'sensitivity': 'Slightly high'},
        'AA': {'phenotype': 'Low BDNF', 'sensitivity': 'High', 'note': 'Higher chronic pain risk'}
    },
    # KCNS1 - Potassium channel
    'rs734784': {
        'gene': 'KCNS1',
        'variant_name': 'V205I',
        'function': 'Potassium channel in sensory neurons',
        'GG': {'phenotype': 'Normal', 'sensitivity': 'Average'},
        'AG': {'phenotype': 'Altered', 'sensitivity': 'Slightly high'},
        'AA': {'phenotype': 'Increased pain', 'sensitivity': 'High'}
    },
    # P2RX7 - Purinergic receptor (inflammatory pain)
    'rs3751143': {
        'gene': 'P2RX7',
        'variant_name': 'E496A',
        'function': 'ATP receptor - inflammatory and neuropathic pain',
        'AA': {'phenotype': 'Normal', 'sensitivity': 'Average'},
        'AC': {'phenotype': 'Reduced function', 'sensitivity': 'Slightly low'},
        'CC': {'phenotype': 'Loss of function', 'sensitivity': 'Low', 'note': 'Protected from some chronic pain'}
    },
    # IL6 - Interleukin 6 (inflammatory pain)
    'rs1800795': {
        'gene': 'IL6',
        'variant_name': '-174G/C',
        'function': 'Pro-inflammatory cytokine - inflammatory pain',
        'GG': {'phenotype': 'Higher IL-6', 'sensitivity': 'High', 'note': 'More inflammation'},
        'GC': {'phenotype': 'Intermediate', 'sensitivity': 'Average'},
        'CC': {'phenotype': 'Lower IL-6', 'sensitivity': 'Low', 'note': 'Less inflammatory pain'}
    },
    # CACNA2D3 - Calcium channel subunit
    'rs6777055': {
        'gene': 'CACNA2D3',
        'variant_name': 'Intronic',
        'function': 'Calcium channel - affects thermal pain',
        'AA': {'phenotype': 'Normal', 'sensitivity': 'Average'},
        'AG': {'phenotype': 'Altered', 'sensitivity': 'Slightly high'},
        'GG': {'phenotype': 'Increased heat pain', 'sensitivity': 'High'}
    },
    # DRD2 - Dopamine D2 receptor
    'rs1800497': {
        'gene': 'DRD2/ANKK1',
        'variant_name': 'Taq1A',
        'function': 'Dopamine receptor - reward and pain processing',
        'GG': {'phenotype': 'Normal dopamine', 'sensitivity': 'Average'},
        'AG': {'phenotype': 'Reduced receptors', 'sensitivity': 'Slightly high'},
        'AA': {'phenotype': 'Low D2 receptors', 'sensitivity': 'High', 'note': 'Higher pain sensitivity, addiction risk'}
    }
}

# ============================================================================
# VISION GENETICS
# ============================================================================

VISION_SNPS = {
    # Color Vision - OPN1LW/OPN1MW (Red-Green)
    'rs9340799': {
        'gene': 'OPN1LW',
        'variant_name': 'S180A',
        'function': 'Long-wave opsin - red color perception',
        'AA': {'phenotype': 'Normal red vision', 'color_vision': 'Normal'},
        'AG': {'phenotype': 'Slightly altered red', 'color_vision': 'Slightly altered'},
        'GG': {'phenotype': 'Altered red perception', 'color_vision': 'Protanomalous tendency'}
    },
    # Blue cone opsin
    'rs1129038': {
        'gene': 'OPN1SW',
        'variant_name': 'Intronic',
        'function': 'Short-wave opsin - blue color perception',
        'GG': {'phenotype': 'Normal blue vision', 'color_vision': 'Normal'},
        'AG': {'phenotype': 'Normal', 'color_vision': 'Normal'},
        'AA': {'phenotype': 'Slightly altered blue', 'color_vision': 'Slightly altered'}
    },
    # Myopia (nearsightedness)
    'rs524952': {
        'gene': 'GJD2',
        'variant_name': 'Intronic',
        'function': 'Gap junction - myopia susceptibility',
        'AA': {'phenotype': 'Normal vision', 'myopia_risk': 'Average'},
        'AT': {'phenotype': 'Slightly increased myopia risk', 'myopia_risk': 'Slightly elevated'},
        'TT': {'phenotype': 'Increased myopia risk', 'myopia_risk': 'Elevated'}
    },
    'rs10034228': {
        'gene': 'RASGRF1',
        'variant_name': 'Intronic',
        'function': 'Ras protein - eye development and myopia',
        'GG': {'phenotype': 'Normal', 'myopia_risk': 'Average'},
        'AG': {'phenotype': 'Slightly increased', 'myopia_risk': 'Slightly elevated'},
        'AA': {'phenotype': 'Higher myopia risk', 'myopia_risk': 'Elevated'}
    },
    'rs634990': {
        'gene': 'CTNND2',
        'variant_name': 'Intronic',
        'function': 'Catenin delta - eye structure',
        'CC': {'phenotype': 'Normal', 'myopia_risk': 'Average'},
        'CT': {'phenotype': 'Slightly increased', 'myopia_risk': 'Slightly elevated'},
        'TT': {'phenotype': 'Higher myopia risk', 'myopia_risk': 'Elevated'}
    },
    # Macular degeneration (AMD)
    'rs10490924': {
        'gene': 'ARMS2',
        'variant_name': 'A69S',
        'function': 'Age-related macular degeneration risk',
        'GG': {'phenotype': 'Normal AMD risk', 'amd_risk': 'Average'},
        'GT': {'phenotype': 'Increased AMD risk', 'amd_risk': 'Elevated'},
        'TT': {'phenotype': 'High AMD risk', 'amd_risk': 'High'}
    },
    'rs1061170': {
        'gene': 'CFH',
        'variant_name': 'Y402H',
        'function': 'Complement factor H - major AMD risk gene',
        'TT': {'phenotype': 'Normal AMD risk', 'amd_risk': 'Average'},
        'CT': {'phenotype': 'Increased AMD risk', 'amd_risk': 'Elevated'},
        'CC': {'phenotype': 'High AMD risk', 'amd_risk': 'High', 'description': '~5x increased risk'}
    },
    'rs2230199': {
        'gene': 'C3',
        'variant_name': 'R102G',
        'function': 'Complement C3 - AMD inflammation pathway',
        'CC': {'phenotype': 'Normal', 'amd_risk': 'Average'},
        'CG': {'phenotype': 'Slightly increased', 'amd_risk': 'Slightly elevated'},
        'GG': {'phenotype': 'Increased AMD risk', 'amd_risk': 'Elevated'}
    },
    # Glaucoma
    'rs2165241': {
        'gene': 'LOXL1',
        'variant_name': 'Intronic',
        'function': 'Lysyl oxidase - exfoliation glaucoma',
        'TT': {'phenotype': 'Normal', 'glaucoma_risk': 'Average'},
        'CT': {'phenotype': 'Increased risk', 'glaucoma_risk': 'Elevated'},
        'CC': {'phenotype': 'High exfoliation glaucoma risk', 'glaucoma_risk': 'High'}
    },
    'rs4236601': {
        'gene': 'CAV1/CAV2',
        'variant_name': 'Intronic',
        'function': 'Caveolin - primary open-angle glaucoma',
        'AA': {'phenotype': 'Normal', 'glaucoma_risk': 'Average'},
        'AC': {'phenotype': 'Slightly increased', 'glaucoma_risk': 'Slightly elevated'},
        'CC': {'phenotype': 'Increased POAG risk', 'glaucoma_risk': 'Elevated'}
    },
    'rs10483727': {
        'gene': 'SIX1/SIX6',
        'variant_name': 'Intronic',
        'function': 'Transcription factors - glaucoma and optic nerve',
        'CC': {'phenotype': 'Normal', 'glaucoma_risk': 'Average'},
        'CT': {'phenotype': 'Increased risk', 'glaucoma_risk': 'Elevated'},
        'TT': {'phenotype': 'Higher glaucoma risk', 'glaucoma_risk': 'High'}
    },
    # Cataracts
    'rs2509049': {
        'gene': 'EPHA2',
        'variant_name': 'Intronic',
        'function': 'Ephrin receptor - age-related cataract',
        'CC': {'phenotype': 'Normal', 'cataract_risk': 'Average'},
        'CT': {'phenotype': 'Slightly increased', 'cataract_risk': 'Slightly elevated'},
        'TT': {'phenotype': 'Increased cataract risk', 'cataract_risk': 'Elevated'}
    },
    # Night vision
    'rs7142117': {
        'gene': 'RHO',
        'variant_name': 'Intronic',
        'function': 'Rhodopsin - night vision adaptation',
        'TT': {'phenotype': 'Normal night vision', 'night_vision': 'Normal'},
        'CT': {'phenotype': 'Normal', 'night_vision': 'Normal'},
        'CC': {'phenotype': 'Possibly reduced', 'night_vision': 'Slightly reduced'}
    },
    # Light sensitivity
    'rs12913832': {
        'gene': 'HERC2/OCA2',
        'variant_name': 'Intronic',
        'function': 'Eye color and light sensitivity',
        'GG': {'phenotype': 'Brown eyes, less light sensitive', 'light_sensitivity': 'Low'},
        'AG': {'phenotype': 'Mixed, moderate sensitivity', 'light_sensitivity': 'Moderate'},
        'AA': {'phenotype': 'Blue eyes, more light sensitive', 'light_sensitivity': 'High'}
    }
}

# ============================================================================
# TOUCH SENSITIVITY
# ============================================================================

TOUCH_SNPS = {
    # PIEZO2 - Main mechanoreceptor
    'rs7289766': {
        'gene': 'PIEZO2',
        'variant_name': 'Intronic',
        'function': 'Primary touch/pressure receptor - mechanosensation',
        'CC': {'phenotype': 'Normal touch', 'sensitivity': 'Average'},
        'CT': {'phenotype': 'Slightly enhanced', 'sensitivity': 'Slightly high'},
        'TT': {'phenotype': 'Enhanced touch sensation', 'sensitivity': 'High'}
    },
    'rs2372233': {
        'gene': 'PIEZO2',
        'variant_name': 'Intronic',
        'function': 'Tactile discrimination ability',
        'AA': {'phenotype': 'Normal', 'sensitivity': 'Average'},
        'AG': {'phenotype': 'Good discrimination', 'sensitivity': 'Slightly high'},
        'GG': {'phenotype': 'Enhanced tactile discrimination', 'sensitivity': 'High'}
    },
    # PIEZO1 - Pressure sensing
    'rs2306450': {
        'gene': 'PIEZO1',
        'variant_name': 'Intronic',
        'function': 'Pressure sensation and proprioception',
        'GG': {'phenotype': 'Normal pressure sense', 'sensitivity': 'Average'},
        'AG': {'phenotype': 'Normal', 'sensitivity': 'Average'},
        'AA': {'phenotype': 'Slightly altered', 'sensitivity': 'Slightly altered'}
    },
    # TRPM8 - Cold sensing
    'rs10166942': {
        'gene': 'TRPM8',
        'variant_name': 'Upstream',
        'function': 'Cold/menthol receptor - cold sensation',
        'CC': {'phenotype': 'Normal cold sensing', 'cold_sensitivity': 'Average'},
        'CT': {'phenotype': 'Enhanced cold sensing', 'cold_sensitivity': 'High'},
        'TT': {'phenotype': 'Very sensitive to cold', 'cold_sensitivity': 'Very high', 'description': 'May be associated with migraine'}
    },
    'rs7577262': {
        'gene': 'TRPM8',
        'variant_name': 'Intronic',
        'function': 'Cold temperature detection threshold',
        'AA': {'phenotype': 'Normal', 'cold_sensitivity': 'Average'},
        'AG': {'phenotype': 'Enhanced', 'cold_sensitivity': 'High'},
        'GG': {'phenotype': 'Cold hypersensitive', 'cold_sensitivity': 'Very high'}
    },
    # TRPV4 - Warmth and pressure
    'rs3742030': {
        'gene': 'TRPV4',
        'variant_name': 'P19S',
        'function': 'Warmth and mechanical sensation',
        'CC': {'phenotype': 'Normal warmth sensing', 'warmth_sensitivity': 'Average'},
        'CT': {'phenotype': 'Altered sensing', 'warmth_sensitivity': 'Slightly altered'},
        'TT': {'phenotype': 'Increased warmth sensitivity', 'warmth_sensitivity': 'High'}
    },
    # KCNK2/TREK-1 - Mechanical sensitivity
    'rs10494996': {
        'gene': 'KCNK2',
        'variant_name': 'Intronic',
        'function': 'Two-pore potassium channel - mechanical sensation',
        'TT': {'phenotype': 'Normal', 'sensitivity': 'Average'},
        'CT': {'phenotype': 'Slightly increased', 'sensitivity': 'Slightly high'},
        'CC': {'phenotype': 'Enhanced mechanical sensitivity', 'sensitivity': 'High'}
    },
    # SLC24A5 - Skin sensitivity (also pigmentation)
    'rs1426654': {
        'gene': 'SLC24A5',
        'variant_name': 'A111T',
        'function': 'Skin sensitivity and pigmentation',
        'AA': {'phenotype': 'Ancestral (darker skin)', 'sensitivity': 'Average'},
        'AG': {'phenotype': 'Intermediate', 'sensitivity': 'Average'},
        'GG': {'phenotype': 'Derived (lighter skin)', 'sensitivity': 'Slightly high', 'note': 'European ancestry marker'}
    }
}

# ============================================================================
# ANALYSIS FUNCTION
# ============================================================================

def analyze_sensory_genetics(dna_data: dict) -> Dict[str, Any]:
    """Comprehensive sensory genetics analysis"""

    results = {
        'bitter_taste': {
            'phenotype': 'Unknown',
            'taster_score': 0.5,
            'markers_found': [],
            'snps_analyzed': []
        },
        'sweet_taste': {
            'phenotype': 'Unknown',
            'score': 0,
            'markers_found': [],
            'snps_analyzed': []
        },
        'umami_taste': {
            'phenotype': 'Unknown',
            'markers_found': [],
            'snps_analyzed': []
        },
        'salty_taste': {
            'phenotype': 'Unknown',
            'sensitivity': 'Unknown',
            'markers_found': [],
            'snps_analyzed': []
        },
        'sour_taste': {
            'phenotype': 'Unknown',
            'sensitivity': 'Unknown',
            'markers_found': [],
            'snps_analyzed': []
        },
        'cilantro': {
            'tastes_soapy': False,
            'phenotype': 'Unknown',
            'markers_found': [],
            'snps_analyzed': []
        },
        'asparagus_smell': {
            'phenotype': 'Unknown',
            'can_smell': True,
            'markers_found': [],
            'snps_analyzed': []
        },
        'smell_sensitivity': {
            'overall_sensitivity': 'Unknown',
            'markers_found': [],
            'snps_analyzed': []
        },
        'body_odor': {
            'phenotype': 'Unknown',
            'earwax': 'Unknown',
            'markers_found': [],
            'snps_analyzed': []
        },
        'fish_smell_metabolism': {
            'phenotype': 'Unknown',
            'carrier': False,
            'markers_found': [],
            'snps_analyzed': []
        },
        'alcohol_flush': {
            'has_flush': False,
            'phenotype': 'Unknown',
            'risk': 'Unknown',
            'markers_found': [],
            'snps_analyzed': []
        },
        'caffeine': {
            'metabolism': 'Unknown',
            'sensitivity': 'Unknown',
            'markers_found': [],
            'snps_analyzed': []
        },
        'hearing': {
            'risk': 'Unknown',
            'markers_found': [],
            'snps_analyzed': []
        },
        'pain': {
            'sensitivity': 'Unknown',
            'markers_found': [],
            'snps_analyzed': []
        },
        'vision': {
            'color_vision': 'Unknown',
            'myopia_risk': 'Unknown',
            'amd_risk': 'Unknown',
            'glaucoma_risk': 'Unknown',
            'markers_found': [],
            'snps_analyzed': []
        },
        'touch': {
            'sensitivity': 'Unknown',
            'cold_sensitivity': 'Unknown',
            'markers_found': [],
            'snps_analyzed': []
        },
        'summary': {
            'total_markers': 0,
            'key_findings': [],
            'recommendations': []
        }
    }

    total_markers = 0
    key_findings = []

    # Analyze bitter taste
    bitter_score = 0
    bitter_max = 0
    for rsid, marker_data in BITTER_TASTE_SNPS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            key = get_genotype_key(genotype, [k for k in marker_data.keys() if k not in ['gene', 'function', 'variant_name']])
            if key:
                data = marker_data[key]
                bitter_score += data.get('score', 1)
                bitter_max += 2
                results['bitter_taste']['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'variant_name': marker_data.get('variant_name', ''),
                    'genotype': genotype,
                    'phenotype': data.get('phenotype', 'Unknown')
                })
                total_markers += 1

    if bitter_max > 0:
        taster_score = bitter_score / bitter_max
        results['bitter_taste']['taster_score'] = taster_score
        if taster_score < 0.3:
            results['bitter_taste']['phenotype'] = 'Non-taster'
            key_findings.append('You are a bitter non-taster - less sensitive to bitter compounds')
        elif taster_score > 0.7:
            results['bitter_taste']['phenotype'] = 'Supertaster'
            key_findings.append('You are a supertaster - very sensitive to bitter flavors')
        else:
            results['bitter_taste']['phenotype'] = 'Medium taster'

    # Analyze sweet taste
    for rsid, marker_data in SWEET_TASTE_SNPS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            key = get_genotype_key(genotype, [k for k in marker_data.keys() if k not in ['gene', 'function', 'variant_name']])
            if key:
                data = marker_data[key]
                results['sweet_taste']['phenotype'] = data.get('phenotype', 'Normal')
                results['sweet_taste']['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'variant_name': marker_data.get('variant_name', ''),
                    'genotype': genotype
                })
                total_markers += 1

    # Analyze umami taste
    for rsid, marker_data in UMAMI_TASTE_SNPS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            key = get_genotype_key(genotype, [k for k in marker_data.keys() if k not in ['gene', 'function', 'variant_name']])
            if key:
                data = marker_data[key]
                results['umami_taste']['phenotype'] = data.get('phenotype', 'Normal')
                results['umami_taste']['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'variant_name': marker_data.get('variant_name', ''),
                    'genotype': genotype
                })
                total_markers += 1

    # Analyze salty taste
    for rsid, marker_data in SALTY_TASTE_SNPS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            key = get_genotype_key(genotype, [k for k in marker_data.keys() if k not in ['gene', 'function', 'variant_name']])
            if key:
                data = marker_data[key]
                results['salty_taste']['phenotype'] = data.get('phenotype', 'Normal')
                results['salty_taste']['sensitivity'] = data.get('sensitivity', 'Normal')
                results['salty_taste']['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'variant_name': marker_data.get('variant_name', ''),
                    'genotype': genotype
                })
                total_markers += 1

    # Analyze sour taste
    for rsid, marker_data in SOUR_TASTE_SNPS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            key = get_genotype_key(genotype, [k for k in marker_data.keys() if k not in ['gene', 'function', 'variant_name']])
            if key:
                data = marker_data[key]
                results['sour_taste']['phenotype'] = data.get('phenotype', 'Normal')
                results['sour_taste']['sensitivity'] = data.get('sensitivity', 'Normal')
                results['sour_taste']['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'variant_name': marker_data.get('variant_name', ''),
                    'genotype': genotype
                })
                total_markers += 1

    # Analyze cilantro
    for rsid, marker_data in CILANTRO_SNPS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            key = get_genotype_key(genotype, [k for k in marker_data.keys() if k not in ['gene', 'function', 'variant_name']])
            if key:
                data = marker_data[key]
                results['cilantro']['tastes_soapy'] = data.get('tastes_soapy', False)
                results['cilantro']['phenotype'] = data.get('phenotype', 'Normal')
                results['cilantro']['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'variant_name': marker_data.get('variant_name', ''),
                    'genotype': genotype
                })
                total_markers += 1
                if data.get('tastes_soapy'):
                    key_findings.append('You likely perceive cilantro as soapy or metallic')

    # Analyze asparagus smell
    for rsid, marker_data in ASPARAGUS_SMELL_SNPS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            key = get_genotype_key(genotype, [k for k in marker_data.keys() if k not in ['gene', 'function', 'variant_name']])
            if key:
                data = marker_data[key]
                results['asparagus_smell']['can_smell'] = data.get('can_smell', True)
                results['asparagus_smell']['phenotype'] = data.get('phenotype', 'Unknown')
                results['asparagus_smell']['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'variant_name': marker_data.get('variant_name', ''),
                    'genotype': genotype
                })
                total_markers += 1

    # Analyze alcohol flush
    for rsid, marker_data in ALCOHOL_FLUSH_SNPS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            key = get_genotype_key(genotype, [k for k in marker_data.keys() if k not in ['gene', 'function', 'variant_name']])
            if key:
                data = marker_data[key]
                results['alcohol_flush']['has_flush'] = data.get('has_flush', False)
                results['alcohol_flush']['phenotype'] = data.get('phenotype', 'Normal')
                results['alcohol_flush']['risk'] = data.get('risk', 'Normal')
                results['alcohol_flush']['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'variant_name': marker_data.get('variant_name', ''),
                    'genotype': genotype
                })
                total_markers += 1
                if data.get('has_flush'):
                    key_findings.append('You have the alcohol flush reaction (Asian flush)')

    # Analyze caffeine metabolism
    for rsid, marker_data in CAFFEINE_SNPS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            key = get_genotype_key(genotype, [k for k in marker_data.keys() if k not in ['gene', 'function', 'variant_name']])
            if key:
                data = marker_data[key]
                results['caffeine']['metabolism'] = data.get('metabolism', 'Normal')
                results['caffeine']['sensitivity'] = data.get('sensitivity', 'Moderate')
                results['caffeine']['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'variant_name': marker_data.get('variant_name', ''),
                    'genotype': genotype
                })
                total_markers += 1
                if data.get('metabolism') == 'Slow':
                    key_findings.append('You are a slow caffeine metabolizer - caffeine stays in your system longer')

    # Analyze hearing
    hearing_risks = []
    for rsid, marker_data in HEARING_SNPS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            key = get_genotype_key(genotype, [k for k in marker_data.keys() if k not in ['gene', 'function', 'variant_name']])
            if key:
                data = marker_data[key]
                hearing_risks.append(data.get('risk', 'Average'))
                results['hearing']['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'variant_name': marker_data.get('variant_name', ''),
                    'genotype': genotype,
                    'risk': data.get('risk', 'Average')
                })
                total_markers += 1

    if hearing_risks:
        if 'Elevated' in hearing_risks or 'High' in hearing_risks:
            results['hearing']['risk'] = 'Elevated'
        else:
            results['hearing']['risk'] = 'Average'

    # Analyze pain sensitivity
    pain_sensitivities = []
    for rsid, marker_data in PAIN_SNPS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            key = get_genotype_key(genotype, [k for k in marker_data.keys() if k not in ['gene', 'function', 'variant_name']])
            if key:
                data = marker_data[key]
                pain_sensitivities.append(data.get('sensitivity', 'Average'))
                results['pain']['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'variant_name': marker_data.get('variant_name', ''),
                    'genotype': genotype,
                    'sensitivity': data.get('sensitivity', 'Average'),
                    'note': data.get('note', '')
                })
                total_markers += 1

    if pain_sensitivities:
        if 'Very high' in pain_sensitivities or 'High' in pain_sensitivities:
            results['pain']['sensitivity'] = 'High'
            key_findings.append('You may have increased pain sensitivity')
        elif 'Low' in pain_sensitivities:
            results['pain']['sensitivity'] = 'Low'
        else:
            results['pain']['sensitivity'] = 'Average'

    # Analyze smell sensitivity (general olfactory receptors)
    smell_sensitivities = []
    for rsid, marker_data in SMELL_SENSITIVITY_SNPS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            key = get_genotype_key(genotype, [k for k in marker_data.keys() if k not in ['gene', 'function', 'variant_name']])
            if key:
                data = marker_data[key]
                smell_sensitivities.append(data.get('sensitivity', 'Normal'))
                results['smell_sensitivity']['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'variant_name': marker_data.get('variant_name', ''),
                    'genotype': genotype,
                    'sensitivity': data.get('sensitivity', 'Normal')
                })
                total_markers += 1

    # Also analyze general olfaction SNPs
    for rsid, marker_data in GENERAL_OLFACTION_SNPS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            key = get_genotype_key(genotype, [k for k in marker_data.keys() if k not in ['gene', 'function', 'variant_name']])
            if key:
                data = marker_data[key]
                smell_sensitivities.append(data.get('sensitivity', 'Normal'))
                results['smell_sensitivity']['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'variant_name': marker_data.get('variant_name', ''),
                    'genotype': genotype,
                    'sensitivity': data.get('sensitivity', 'Normal')
                })
                total_markers += 1

    if smell_sensitivities:
        high_count = smell_sensitivities.count('High') + smell_sensitivities.count('Very high')
        low_count = smell_sensitivities.count('Low') + smell_sensitivities.count('Very low')
        if high_count > low_count:
            results['smell_sensitivity']['overall_sensitivity'] = 'Enhanced'
        elif low_count > high_count:
            results['smell_sensitivity']['overall_sensitivity'] = 'Reduced'
        else:
            results['smell_sensitivity']['overall_sensitivity'] = 'Normal'

    # Analyze body odor/earwax
    for rsid, marker_data in BODY_ODOR_SNPS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            key = get_genotype_key(genotype, [k for k in marker_data.keys() if k not in ['gene', 'function', 'variant_name']])
            if key:
                data = marker_data[key]
                results['body_odor']['phenotype'] = data.get('phenotype', 'Normal')
                results['body_odor']['earwax'] = data.get('earwax', 'Unknown')
                results['body_odor']['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'variant_name': marker_data.get('variant_name', ''),
                    'genotype': genotype,
                    'body_odor': data.get('body_odor', 'Normal')
                })
                total_markers += 1
                if data.get('earwax') == 'Dry':
                    key_findings.append('You have dry earwax type - associated with less body odor')

    # Analyze fish smell metabolism (FMO3)
    fmo3_carriers = []
    for rsid, marker_data in FISH_SMELL_SNPS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            key = get_genotype_key(genotype, [k for k in marker_data.keys() if k not in ['gene', 'function', 'variant_name']])
            if key:
                data = marker_data[key]
                fmo3_carriers.append(data.get('carrier', False))
                results['fish_smell_metabolism']['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'variant_name': marker_data.get('variant_name', ''),
                    'genotype': genotype,
                    'phenotype': data.get('phenotype', 'Normal')
                })
                total_markers += 1

    if any(fmo3_carriers):
        results['fish_smell_metabolism']['carrier'] = True
        results['fish_smell_metabolism']['phenotype'] = 'Carrier'
    else:
        results['fish_smell_metabolism']['phenotype'] = 'Normal'

    # Analyze vision
    vision_risks = {'myopia': [], 'amd': [], 'glaucoma': []}
    for rsid, marker_data in VISION_SNPS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            key = get_genotype_key(genotype, [k for k in marker_data.keys() if k not in ['gene', 'function', 'variant_name']])
            if key:
                data = marker_data[key]
                results['vision']['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'variant_name': marker_data.get('variant_name', ''),
                    'genotype': genotype,
                    'phenotype': data.get('phenotype', 'Normal')
                })
                total_markers += 1

                # Track risks
                if 'myopia_risk' in data:
                    vision_risks['myopia'].append(data['myopia_risk'])
                if 'amd_risk' in data:
                    vision_risks['amd'].append(data['amd_risk'])
                if 'glaucoma_risk' in data:
                    vision_risks['glaucoma'].append(data['glaucoma_risk'])
                if 'color_vision' in data:
                    results['vision']['color_vision'] = data['color_vision']

    # Determine overall vision risks
    for risk_type in ['myopia', 'amd', 'glaucoma']:
        risks = vision_risks[risk_type]
        if risks:
            if 'High' in risks or 'Elevated' in risks:
                results['vision'][f'{risk_type}_risk'] = 'Elevated'
            else:
                results['vision'][f'{risk_type}_risk'] = 'Average'

    # Analyze touch sensitivity
    touch_sensitivities = []
    cold_sensitivities = []
    for rsid, marker_data in TOUCH_SNPS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            key = get_genotype_key(genotype, [k for k in marker_data.keys() if k not in ['gene', 'function', 'variant_name']])
            if key:
                data = marker_data[key]
                results['touch']['markers_found'].append({
                    'rsid': rsid,
                    'gene': marker_data['gene'],
                    'variant_name': marker_data.get('variant_name', ''),
                    'genotype': genotype,
                    'phenotype': data.get('phenotype', 'Normal')
                })
                total_markers += 1

                if 'sensitivity' in data:
                    touch_sensitivities.append(data['sensitivity'])
                if 'cold_sensitivity' in data:
                    cold_sensitivities.append(data['cold_sensitivity'])

    if touch_sensitivities:
        high_count = sum(1 for s in touch_sensitivities if s in ['High', 'Very high', 'Slightly high'])
        if high_count > len(touch_sensitivities) / 2:
            results['touch']['sensitivity'] = 'Enhanced'
        else:
            results['touch']['sensitivity'] = 'Normal'

    if cold_sensitivities:
        if 'Very high' in cold_sensitivities or cold_sensitivities.count('High') > 1:
            results['touch']['cold_sensitivity'] = 'High'
            key_findings.append('You may be more sensitive to cold temperatures')
        else:
            results['touch']['cold_sensitivity'] = 'Normal'

    # Build summary
    results['summary']['total_markers'] = total_markers
    results['summary']['key_findings'] = key_findings

    return results
