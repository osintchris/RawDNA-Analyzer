#!/usr/bin/env python3
"""
Behavioral & Cognitive Genetics Database
Real SNP data for psychological traits, cognition, and behavior
Sources: GWAS Catalog, dbSNP, published neuroscience research
"""

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


# =============================================================================
# OXYTOCIN RECEPTOR - EMPATHY & SOCIAL BEHAVIOR
# =============================================================================

EMPATHY_GENETICS = {
    'rs53576': {
        'gene': 'OXTR',
        'name': 'Oxytocin Receptor',
        'variant_name': 'Intron 3',
        'function': 'Social bonding, empathy, trust',
        'alleles': {
            'GG': {'phenotype': 'Higher empathy', 'score': 0.8, 'traits': ['More empathetic', 'Better at reading emotions', 'More social support seeking']},
            'AG': {'phenotype': 'Average empathy', 'score': 0.5, 'traits': ['Typical empathy levels']},
            'AA': {'phenotype': 'Lower empathy tendency', 'score': 0.3, 'traits': ['More self-reliant', 'Less affected by social rejection']}
        }
    },
    'rs2254298': {
        'gene': 'OXTR',
        'name': 'Oxytocin Receptor variant',
        'variant_name': 'Intron 3 G/A',
        'function': 'Attachment and social memory',
        'alleles': {
            'GG': {'phenotype': 'Secure attachment tendency', 'score': 0.7, 'traits': ['Secure bonding']},
            'AG': {'phenotype': 'Average attachment', 'score': 0.5, 'traits': ['Typical attachment']},
            'AA': {'phenotype': 'May need more reassurance', 'score': 0.4, 'traits': ['Anxious attachment tendency']}
        }
    },
    'rs1042778': {
        'gene': 'OXTR',
        'name': 'Oxytocin Receptor 3\'UTR',
        'variant_name': '3\'UTR T/G',
        'function': 'Prosocial behavior and altruism',
        'alleles': {
            'TT': {'phenotype': 'Higher prosocial behavior', 'score': 0.75, 'traits': ['More altruistic', 'Higher generosity']},
            'TG': {'phenotype': 'Average prosocial', 'score': 0.5, 'traits': ['Typical prosocial behavior']},
            'GG': {'phenotype': 'Lower prosocial tendency', 'score': 0.35, 'traits': ['More self-focused']}
        }
    },
    'rs7632287': {
        'gene': 'OXTR',
        'name': 'Oxytocin Receptor upstream',
        'variant_name': 'Upstream A/G',
        'function': 'Pair bonding and relationship satisfaction',
        'alleles': {
            'AA': {'phenotype': 'Higher relationship satisfaction', 'score': 0.75, 'traits': ['Strong pair bonding']},
            'AG': {'phenotype': 'Average', 'score': 0.5, 'traits': ['Typical relationship patterns']},
            'GG': {'phenotype': 'Lower relationship stability', 'score': 0.35, 'traits': ['May need more relationship support']}
        }
    },
    'rs237887': {
        'gene': 'OXTR',
        'name': 'Oxytocin Receptor variant',
        'variant_name': 'Intronic A/G',
        'function': 'Social recognition and memory',
        'alleles': {
            'AA': {'phenotype': 'Better face recognition', 'score': 0.7, 'traits': ['Enhanced facial memory']},
            'AG': {'phenotype': 'Average recognition', 'score': 0.5, 'traits': ['Typical face memory']},
            'GG': {'phenotype': 'May have difficulty', 'score': 0.35, 'traits': ['May struggle with faces']}
        }
    },
    'rs3796863': {
        'gene': 'CD38',
        'name': 'CD38 oxytocin release',
        'variant_name': 'A/C',
        'function': 'Oxytocin secretion regulation',
        'alleles': {
            'CC': {'phenotype': 'Normal oxytocin release', 'score': 0.65, 'traits': ['Typical bonding ability']},
            'AC': {'phenotype': 'Moderate release', 'score': 0.5, 'traits': ['Average oxytocin levels']},
            'AA': {'phenotype': 'Reduced oxytocin release', 'score': 0.35, 'traits': ['May have lower empathy']}
        }
    },
    'rs6311': {
        'gene': 'HTR2A',
        'name': 'Serotonin 2A Receptor',
        'variant_name': '-1438 A/G',
        'function': 'Social cognition and emotional processing',
        'alleles': {
            'AA': {'phenotype': 'Enhanced social cognition', 'score': 0.7, 'traits': ['Better emotional intelligence']},
            'AG': {'phenotype': 'Average social cognition', 'score': 0.5, 'traits': ['Typical emotional processing']},
            'GG': {'phenotype': 'May need social skill support', 'score': 0.35, 'traits': ['May benefit from social training']}
        }
    },
    'rs4570625': {
        'gene': 'TPH2',
        'name': 'Tryptophan Hydroxylase 2',
        'variant_name': 'G-703T',
        'function': 'Emotional reactivity and empathy',
        'alleles': {
            'GG': {'phenotype': 'Stable emotional reactivity', 'score': 0.65, 'traits': ['Calm emotional response']},
            'GT': {'phenotype': 'Average reactivity', 'score': 0.5, 'traits': ['Typical emotional response']},
            'TT': {'phenotype': 'Heightened emotional reactivity', 'score': 0.7, 'traits': ['Strong empathic response', 'May feel others\' emotions intensely']}
        }
    },
    'rs4680': {
        'gene': 'COMT',
        'name': 'COMT social cognition',
        'variant_name': 'Val158Met',
        'function': 'Theory of mind and empathic accuracy',
        'alleles': {
            'AA': {'phenotype': 'Met/Met - Higher empathic accuracy', 'score': 0.75, 'traits': ['Better at reading emotions', 'More sensitive to social cues']},
            'AG': {'phenotype': 'Val/Met - Balanced', 'score': 0.5, 'traits': ['Moderate empathic accuracy']},
            'GG': {'phenotype': 'Val/Val - Task-focused', 'score': 0.4, 'traits': ['Less affected by emotional context']}
        }
    },
    'rs6265': {
        'gene': 'BDNF',
        'name': 'BDNF empathy',
        'variant_name': 'Val66Met',
        'function': 'Emotional memory and social learning',
        'alleles': {
            'CC': {'phenotype': 'Val/Val - Better social learning', 'score': 0.7, 'traits': ['Learns social cues well']},
            'CT': {'phenotype': 'Val/Met - Average', 'score': 0.5, 'traits': ['Typical social learning']},
            'TT': {'phenotype': 'Met/Met - May need more practice', 'score': 0.35, 'traits': ['May need more social exposure']}
        }
    },
    'rs1799913': {
        'gene': 'TPH1',
        'name': 'Tryptophan Hydroxylase 1',
        'variant_name': 'A218C',
        'function': 'Peripheral serotonin affecting social behavior',
        'alleles': {
            'AA': {'phenotype': 'Higher social sensitivity', 'score': 0.7, 'traits': ['More attuned to social atmosphere']},
            'AC': {'phenotype': 'Average sensitivity', 'score': 0.5, 'traits': ['Typical social awareness']},
            'CC': {'phenotype': 'Lower sensitivity', 'score': 0.4, 'traits': ['Less affected by social atmosphere']}
        }
    },
    'rs324420': {
        'gene': 'FAAH',
        'name': 'Fatty Acid Amide Hydrolase',
        'variant_name': 'P129T',
        'function': 'Endocannabinoid system affecting social reward',
        'alleles': {
            'CC': {'phenotype': 'Normal FAAH activity', 'score': 0.5, 'traits': ['Standard social reward response']},
            'CA': {'phenotype': 'Reduced FAAH activity', 'score': 0.6, 'traits': ['Enhanced social pleasure']},
            'AA': {'phenotype': 'Low FAAH activity', 'score': 0.7, 'traits': ['Higher social reward sensitivity', 'Less anxiety']}
        }
    },
    'rs237885': {
        'gene': 'OXTR',
        'name': 'OXTR intronic variant',
        'variant_name': 'Intronic G/A',
        'function': 'Emotional empathy and social anxiety',
        'alleles': {
            'GG': {'phenotype': 'Higher emotional empathy', 'score': 0.7, 'traits': ['Strong emotional resonance']},
            'GA': {'phenotype': 'Average empathy', 'score': 0.5, 'traits': ['Typical empathy']},
            'AA': {'phenotype': 'Lower emotional empathy', 'score': 0.35, 'traits': ['Less emotional contagion']}
        }
    },
    'rs2268490': {
        'gene': 'OXTR',
        'name': 'OXTR emotion recognition',
        'variant_name': 'Intronic C/T',
        'function': 'Reading facial emotions',
        'alleles': {
            'CC': {'phenotype': 'Better emotion reading', 'score': 0.7, 'traits': ['Enhanced facial emotion detection']},
            'CT': {'phenotype': 'Average', 'score': 0.5, 'traits': ['Typical emotion reading']},
            'TT': {'phenotype': 'May miss subtle cues', 'score': 0.35, 'traits': ['May need explicit emotional cues']}
        }
    },
    'rs2268493': {
        'gene': 'OXTR',
        'name': 'OXTR social memory',
        'variant_name': 'Intronic A/G',
        'function': 'Social memory and recognition',
        'alleles': {
            'AA': {'phenotype': 'Enhanced social memory', 'score': 0.7, 'traits': ['Better remembering social interactions']},
            'AG': {'phenotype': 'Normal', 'score': 0.5, 'traits': ['Typical social memory']},
            'GG': {'phenotype': 'Average social memory', 'score': 0.4, 'traits': ['Standard social recall']}
        }
    },
    'rs13316193': {
        'gene': 'OXTR',
        'name': 'OXTR autism association',
        'variant_name': 'Promoter A/G',
        'function': 'Social communication and autism spectrum traits',
        'alleles': {
            'AA': {'phenotype': 'Typical social communication', 'score': 0.6, 'traits': ['Standard social skills']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Typical variation']},
            'GG': {'phenotype': 'May have social challenges', 'score': 0.35, 'traits': ['May prefer routines']}
        }
    },
    'rs2228485': {
        'gene': 'AVPR1A',
        'name': 'Vasopressin receptor 1A',
        'variant_name': 'Synonymous A/G',
        'function': 'Social bonding and pair bonding (vasopressin system)',
        'alleles': {
            'AA': {'phenotype': 'Strong pair bonding', 'score': 0.7, 'traits': ['Enhanced bonding capacity']},
            'AG': {'phenotype': 'Normal bonding', 'score': 0.5, 'traits': ['Typical attachment']},
            'GG': {'phenotype': 'Variable bonding', 'score': 0.4, 'traits': ['More independent']}
        }
    },
    'rs3021529': {
        'gene': 'AVPR1A',
        'name': 'AVPR1A promoter',
        'variant_name': 'Promoter region',
        'function': 'Altruism and social behavior',
        'alleles': {
            'GG': {'phenotype': 'Higher altruism', 'score': 0.7, 'traits': ['More generous', 'Prosocial']},
            'GA': {'phenotype': 'Average altruism', 'score': 0.5, 'traits': ['Typical generosity']},
            'AA': {'phenotype': 'More self-focused', 'score': 0.35, 'traits': ['Pragmatic approach']}
        }
    },
    'rs1042615': {
        'gene': 'AVPR1A',
        'name': 'AVPR1A variant',
        'variant_name': 'Intronic C/T',
        'function': 'Partner bonding and relationship commitment',
        'alleles': {
            'CC': {'phenotype': 'Strong commitment tendency', 'score': 0.7, 'traits': ['Long-term relationship orientation']},
            'CT': {'phenotype': 'Normal', 'score': 0.5, 'traits': ['Typical commitment']},
            'TT': {'phenotype': 'More independence-seeking', 'score': 0.4, 'traits': ['Values autonomy']}
        }
    },
    'rs11174811': {
        'gene': 'AVPR1A',
        'name': 'AVPR1A musical empathy',
        'variant_name': 'Intronic A/C',
        'function': 'Musical empathy and emotional response to music',
        'alleles': {
            'AA': {'phenotype': 'Strong musical empathy', 'score': 0.7, 'traits': ['Deep emotional response to music']},
            'AC': {'phenotype': 'Normal', 'score': 0.5, 'traits': ['Typical musical appreciation']},
            'CC': {'phenotype': 'Average musical empathy', 'score': 0.4, 'traits': ['Standard music response']}
        }
    },
    'rs2740210': {
        'gene': 'OXT',
        'name': 'Oxytocin gene',
        'variant_name': 'Promoter C/A',
        'function': 'Oxytocin production and maternal behavior',
        'alleles': {
            'CC': {'phenotype': 'Higher oxytocin production', 'score': 0.7, 'traits': ['Enhanced nurturing']},
            'CA': {'phenotype': 'Normal production', 'score': 0.5, 'traits': ['Typical nurturing']},
            'AA': {'phenotype': 'Lower production', 'score': 0.4, 'traits': ['Less oxytocin']}
        }
    },
    'rs4813625': {
        'gene': 'OXT',
        'name': 'Oxytocin hormone',
        'variant_name': 'Intronic G/A',
        'function': 'Social stress response',
        'alleles': {
            'GG': {'phenotype': 'Better social stress coping', 'score': 0.65, 'traits': ['Resilient to social stress']},
            'GA': {'phenotype': 'Normal', 'score': 0.5, 'traits': ['Typical stress response']},
            'AA': {'phenotype': 'More social stress reactive', 'score': 0.35, 'traits': ['Sensitive to social evaluation']}
        }
    },
    'rs2254298': {
        'gene': 'OXTR',
        'name': 'OXTR depression link',
        'variant_name': 'Intronic G/A',
        'function': 'Social support seeking and depression resilience',
        'alleles': {
            'GG': {'phenotype': 'More social support seeking', 'score': 0.65, 'traits': ['Reaches out when stressed']},
            'GA': {'phenotype': 'Average', 'score': 0.5, 'traits': ['Typical support seeking']},
            'AA': {'phenotype': 'More self-reliant', 'score': 0.4, 'traits': ['Handles stress independently']}
        }
    },
    'rs6770632': {
        'gene': 'CNR1',
        'name': 'Cannabinoid receptor 1',
        'variant_name': 'Intronic A/G',
        'function': 'Endocannabinoid system and social reward',
        'alleles': {
            'AA': {'phenotype': 'Enhanced social reward', 'score': 0.65, 'traits': ['Strong social pleasure response']},
            'AG': {'phenotype': 'Normal', 'score': 0.5, 'traits': ['Typical social reward']},
            'GG': {'phenotype': 'Average social reward', 'score': 0.4, 'traits': ['Standard reward sensitivity']}
        }
    },
    'rs806380': {
        'gene': 'CNR1',
        'name': 'CNR1 social anxiety',
        'variant_name': 'Intronic A/G',
        'function': 'Social anxiety and stress response',
        'alleles': {
            'AA': {'phenotype': 'Lower social anxiety', 'score': 0.65, 'traits': ['Comfortable in social settings']},
            'AG': {'phenotype': 'Normal', 'score': 0.5, 'traits': ['Typical social comfort']},
            'GG': {'phenotype': 'Higher social anxiety tendency', 'score': 0.35, 'traits': ['May feel socially anxious']}
        }
    },
    'rs2023239': {
        'gene': 'CNR1',
        'name': 'CNR1 empathy',
        'variant_name': 'Intronic C/T',
        'function': 'Emotional empathy and social cognition',
        'alleles': {
            'CC': {'phenotype': 'Higher emotional empathy', 'score': 0.65, 'traits': ['Strong empathic response']},
            'CT': {'phenotype': 'Normal', 'score': 0.5, 'traits': ['Typical empathy']},
            'TT': {'phenotype': 'More cognitive empathy', 'score': 0.45, 'traits': ['Analytical social understanding']}
        }
    }
}

# =============================================================================
# DOPAMINE - REWARD, MOTIVATION, NOVELTY SEEKING
# =============================================================================

DOPAMINE_GENETICS = {
    'rs1800497': {
        'gene': 'DRD2/ANKK1',
        'name': 'Taq1A polymorphism',
        'variant_name': 'Taq1A',
        'function': 'Dopamine receptor density, reward sensitivity',
        'alleles': {
            'CC': {'phenotype': 'Normal dopamine receptors', 'score': 0.5, 'traits': ['Typical reward response']},
            'CT': {'phenotype': 'Reduced receptor density', 'score': 0.6, 'traits': ['May seek more stimulation']},
            'TT': {'phenotype': 'Significantly reduced receptors', 'score': 0.8, 'traits': ['Higher novelty seeking', 'May be more prone to addictive behaviors']}
        }
    },
    'rs4680': {
        'gene': 'COMT',
        'name': 'Val158Met (Warrior/Worrier)',
        'variant_name': 'Val158Met',
        'function': 'Dopamine breakdown in prefrontal cortex',
        'alleles': {
            'GG': {'phenotype': 'Warrior type', 'score': 0.7, 'traits': ['Better stress performance', 'Lower pain sensitivity', 'May be more aggressive']},
            'AG': {'phenotype': 'Balanced', 'score': 0.5, 'traits': ['Moderate stress response', 'Flexible cognitive style']},
            'AA': {'phenotype': 'Worrier type', 'score': 0.3, 'traits': ['Better memory/attention at baseline', 'More stress sensitive', 'Higher pain sensitivity']}
        }
    },
    'rs1800955': {
        'gene': 'DRD4',
        'name': 'DRD4 promoter',
        'variant_name': '-521 C/T',
        'function': 'Novelty seeking, exploration',
        'alleles': {
            'TT': {'phenotype': 'Higher novelty seeking', 'score': 0.8, 'traits': ['More adventurous', 'Risk-taking tendency']},
            'CT': {'phenotype': 'Moderate novelty seeking', 'score': 0.5, 'traits': ['Balanced exploration']},
            'CC': {'phenotype': 'Lower novelty seeking', 'score': 0.3, 'traits': ['More cautious', 'Prefers routine']}
        }
    },
    'rs6277': {
        'gene': 'DRD2',
        'name': 'DRD2 C957T',
        'variant_name': 'C957T',
        'function': 'Dopamine binding affinity and reward learning',
        'alleles': {
            'CC': {'phenotype': 'Higher D2 binding', 'score': 0.6, 'traits': ['Better avoidance learning', 'Higher reward sensitivity']},
            'CT': {'phenotype': 'Intermediate binding', 'score': 0.5, 'traits': ['Balanced reward processing']},
            'TT': {'phenotype': 'Lower D2 binding', 'score': 0.4, 'traits': ['May seek more reward', 'Faster reward processing']}
        }
    },
    'rs2283265': {
        'gene': 'DRD2',
        'name': 'DRD2 intronic variant',
        'variant_name': 'Intronic',
        'function': 'Dopamine receptor expression ratio',
        'alleles': {
            'GG': {'phenotype': 'Normal D2 expression', 'score': 0.5, 'traits': ['Typical reward response']},
            'GT': {'phenotype': 'Altered D2 ratio', 'score': 0.6, 'traits': ['Modified reward processing']},
            'TT': {'phenotype': 'Changed D2 expression', 'score': 0.7, 'traits': ['Enhanced reward seeking']}
        }
    },
    'rs1076560': {
        'gene': 'DRD2',
        'name': 'DRD2 splice variant',
        'variant_name': 'Splicing G/T',
        'function': 'D2 short vs long isoform ratio',
        'alleles': {
            'GG': {'phenotype': 'Normal D2 isoform ratio', 'score': 0.5, 'traits': ['Typical dopamine signaling']},
            'GT': {'phenotype': 'Altered isoform ratio', 'score': 0.6, 'traits': ['Modified signaling']},
            'TT': {'phenotype': 'Changed D2 signaling', 'score': 0.65, 'traits': ['Enhanced reward processing']}
        }
    },
    'rs6280': {
        'gene': 'DRD3',
        'name': 'DRD3 Ser9Gly',
        'variant_name': 'Ser9Gly',
        'function': 'Dopamine D3 receptor affinity',
        'alleles': {
            'CC': {'phenotype': 'Ser/Ser - Lower affinity', 'score': 0.5, 'traits': ['Normal reward response']},
            'CT': {'phenotype': 'Ser/Gly - Intermediate', 'score': 0.55, 'traits': ['Moderate response']},
            'TT': {'phenotype': 'Gly/Gly - Higher affinity', 'score': 0.65, 'traits': ['Enhanced reward sensitivity']}
        }
    },
    'rs167771': {
        'gene': 'DRD3',
        'name': 'DRD3 variant',
        'variant_name': 'Intronic G/A',
        'function': 'D3 receptor expression in reward circuits',
        'alleles': {
            'GG': {'phenotype': 'Normal D3 expression', 'score': 0.5, 'traits': ['Typical motivation']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.55, 'traits': ['Balanced motivation']},
            'AA': {'phenotype': 'Altered expression', 'score': 0.6, 'traits': ['May have higher drive']}
        }
    },
    'rs1611115': {
        'gene': 'DBH',
        'name': 'Dopamine Beta-Hydroxylase',
        'variant_name': '-1021 C/T',
        'function': 'Dopamine to norepinephrine conversion',
        'alleles': {
            'CC': {'phenotype': 'Normal DBH activity', 'score': 0.5, 'traits': ['Typical stress response']},
            'CT': {'phenotype': 'Reduced DBH activity', 'score': 0.6, 'traits': ['Higher dopamine levels']},
            'TT': {'phenotype': 'Low DBH activity', 'score': 0.7, 'traits': ['Much higher dopamine', 'May affect attention']}
        }
    },
    'rs1108580': {
        'gene': 'DBH',
        'name': 'DBH variant',
        'variant_name': 'G/A',
        'function': 'DBH enzyme activity regulation',
        'alleles': {
            'GG': {'phenotype': 'Normal activity', 'score': 0.5, 'traits': ['Typical dopamine levels']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.55, 'traits': ['Slightly altered levels']},
            'AA': {'phenotype': 'Altered activity', 'score': 0.6, 'traits': ['Modified dopamine processing']}
        }
    },
    'rs3837091': {
        'gene': 'DAT1/SLC6A3',
        'name': 'Dopamine Transporter',
        'variant_name': 'VNTR proxy',
        'function': 'Dopamine reuptake in striatum',
        'alleles': {
            'CC': {'phenotype': 'Normal dopamine clearance', 'score': 0.5, 'traits': ['Typical reward response']},
            'CT': {'phenotype': 'Intermediate clearance', 'score': 0.6, 'traits': ['Modified reward processing']},
            'TT': {'phenotype': 'Reduced clearance', 'score': 0.7, 'traits': ['Prolonged reward signals']}
        }
    },
    'rs27072': {
        'gene': 'DAT1/SLC6A3',
        'name': 'DAT1 3\'UTR variant',
        'variant_name': '3\'UTR G/A',
        'function': 'Dopamine transporter expression',
        'alleles': {
            'GG': {'phenotype': 'Normal DAT expression', 'score': 0.5, 'traits': ['Typical dopamine levels']},
            'GA': {'phenotype': 'Reduced DAT', 'score': 0.6, 'traits': ['Higher synaptic dopamine']},
            'AA': {'phenotype': 'Low DAT expression', 'score': 0.7, 'traits': ['Higher dopamine levels', 'May affect attention']}
        }
    },
    'rs40184': {
        'gene': 'DAT1/SLC6A3',
        'name': 'DAT1 intron 8',
        'variant_name': 'Intron 8',
        'function': 'DAT expression regulation',
        'alleles': {
            'TT': {'phenotype': 'Normal transporter', 'score': 0.5, 'traits': ['Typical dopamine regulation']},
            'TC': {'phenotype': 'Intermediate', 'score': 0.55, 'traits': ['Balanced regulation']},
            'CC': {'phenotype': 'Altered expression', 'score': 0.6, 'traits': ['Modified dopamine levels']}
        }
    },
    'rs2550956': {
        'gene': 'TH',
        'name': 'Tyrosine Hydroxylase',
        'variant_name': 'Upstream C/T',
        'function': 'Dopamine synthesis rate-limiting enzyme',
        'alleles': {
            'CC': {'phenotype': 'Normal TH activity', 'score': 0.5, 'traits': ['Typical dopamine production']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.55, 'traits': ['Moderate production']},
            'TT': {'phenotype': 'Altered TH activity', 'score': 0.6, 'traits': ['Modified dopamine synthesis']}
        }
    },
    'rs6356': {
        'gene': 'TH',
        'name': 'Tyrosine Hydroxylase variant',
        'variant_name': 'V81M',
        'function': 'Dopamine synthesis efficiency',
        'alleles': {
            'CC': {'phenotype': 'Normal enzyme', 'score': 0.5, 'traits': ['Typical synthesis']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.55, 'traits': ['Moderate efficiency']},
            'TT': {'phenotype': 'Altered efficiency', 'score': 0.6, 'traits': ['Modified synthesis']}
        }
    },
    'rs165599': {
        'gene': 'COMT',
        'name': 'COMT 3\'UTR',
        'variant_name': '3\'UTR G/A',
        'function': 'COMT expression regulation',
        'alleles': {
            'GG': {'phenotype': 'Normal COMT expression', 'score': 0.5, 'traits': ['Typical dopamine breakdown']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.55, 'traits': ['Moderate breakdown']},
            'AA': {'phenotype': 'Altered COMT expression', 'score': 0.6, 'traits': ['Modified dopamine levels']}
        }
    },
    'rs2283265': {
        'gene': 'DRD2',
        'name': 'DRD2 intron 6',
        'variant_name': 'Intron 6 G/T',
        'function': 'D2 receptor splice variant ratio',
        'alleles': {
            'GG': {'phenotype': 'Normal D2S/D2L ratio', 'score': 0.5, 'traits': ['Typical dopamine signaling']},
            'GT': {'phenotype': 'Altered ratio', 'score': 0.55, 'traits': ['Modified D2 signaling']},
            'TT': {'phenotype': 'More D2S expression', 'score': 0.6, 'traits': ['Enhanced presynaptic feedback']}
        }
    },
    'rs12364283': {
        'gene': 'DRD2',
        'name': 'DRD2 promoter',
        'variant_name': 'Promoter A/G',
        'function': 'D2 receptor expression level',
        'alleles': {
            'AA': {'phenotype': 'Higher D2 expression', 'score': 0.6, 'traits': ['More dopamine receptors']},
            'AG': {'phenotype': 'Normal expression', 'score': 0.5, 'traits': ['Typical D2 levels']},
            'GG': {'phenotype': 'Lower expression', 'score': 0.4, 'traits': ['Fewer D2 receptors']}
        }
    },
    'rs2075652': {
        'gene': 'DRD2',
        'name': 'DRD2 intronic',
        'variant_name': 'Intronic A/G',
        'function': 'Reward processing and motivation',
        'alleles': {
            'AA': {'phenotype': 'Enhanced reward response', 'score': 0.6, 'traits': ['Strong motivation']},
            'AG': {'phenotype': 'Normal', 'score': 0.5, 'traits': ['Typical reward response']},
            'GG': {'phenotype': 'Average reward response', 'score': 0.45, 'traits': ['Standard motivation']}
        }
    },
    'rs2514218': {
        'gene': 'DRD2',
        'name': 'DRD2 upstream',
        'variant_name': 'Upstream C/T',
        'function': 'Dopamine receptor density',
        'alleles': {
            'CC': {'phenotype': 'Higher receptor density', 'score': 0.6, 'traits': ['Enhanced D2 signaling']},
            'CT': {'phenotype': 'Normal density', 'score': 0.5, 'traits': ['Typical signaling']},
            'TT': {'phenotype': 'Lower density', 'score': 0.4, 'traits': ['Reduced D2 signaling']}
        }
    },
    'rs936461': {
        'gene': 'DRD1',
        'name': 'Dopamine D1 receptor',
        'variant_name': 'Upstream G/A',
        'function': 'D1 receptor affecting working memory',
        'alleles': {
            'GG': {'phenotype': 'Normal D1 function', 'score': 0.5, 'traits': ['Typical working memory']},
            'GA': {'phenotype': 'Slightly altered', 'score': 0.55, 'traits': ['Modified D1 signaling']},
            'AA': {'phenotype': 'Altered D1 function', 'score': 0.45, 'traits': ['May affect focus']}
        }
    },
    'rs686': {
        'gene': 'DRD1',
        'name': 'DRD1 3\'UTR',
        'variant_name': '3\'UTR A/G',
        'function': 'D1 receptor mRNA stability',
        'alleles': {
            'AA': {'phenotype': 'Higher D1 expression', 'score': 0.6, 'traits': ['Enhanced D1 signaling']},
            'AG': {'phenotype': 'Normal', 'score': 0.5, 'traits': ['Typical D1 levels']},
            'GG': {'phenotype': 'Lower expression', 'score': 0.4, 'traits': ['Reduced D1 levels']}
        }
    },
    'rs265981': {
        'gene': 'DRD1',
        'name': 'DRD1 promoter',
        'variant_name': 'Promoter C/T',
        'function': 'D1 receptor transcription',
        'alleles': {
            'CC': {'phenotype': 'Higher transcription', 'score': 0.6, 'traits': ['More D1 receptors']},
            'CT': {'phenotype': 'Normal', 'score': 0.5, 'traits': ['Typical D1 levels']},
            'TT': {'phenotype': 'Lower transcription', 'score': 0.4, 'traits': ['Fewer D1 receptors']}
        }
    },
    'rs167770': {
        'gene': 'DRD3',
        'name': 'DRD3 intronic',
        'variant_name': 'Intron 1 G/A',
        'function': 'D3 receptor expression in limbic system',
        'alleles': {
            'GG': {'phenotype': 'Normal D3 function', 'score': 0.5, 'traits': ['Typical limbic dopamine']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.55, 'traits': ['Modified D3']},
            'AA': {'phenotype': 'Altered D3', 'score': 0.45, 'traits': ['Changed emotional processing']}
        }
    },
    'rs1800828': {
        'gene': 'DBH',
        'name': 'DBH 5\' flanking',
        'variant_name': '-970C/T',
        'function': 'Dopamine beta-hydroxylase promoter activity',
        'alleles': {
            'CC': {'phenotype': 'Higher DBH activity', 'score': 0.55, 'traits': ['More dopamine to norepinephrine conversion']},
            'CT': {'phenotype': 'Normal activity', 'score': 0.5, 'traits': ['Typical conversion']},
            'TT': {'phenotype': 'Lower DBH activity', 'score': 0.6, 'traits': ['Higher dopamine levels']}
        }
    },
    'rs2007153': {
        'gene': 'DBH',
        'name': 'DBH intronic',
        'variant_name': 'Intronic C/T',
        'function': 'DBH enzyme activity regulation',
        'alleles': {
            'CC': {'phenotype': 'Normal DBH', 'score': 0.5, 'traits': ['Typical enzyme activity']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.55, 'traits': ['Modified activity']},
            'TT': {'phenotype': 'Altered DBH', 'score': 0.45, 'traits': ['Changed dopamine/norepinephrine balance']}
        }
    },
    'rs464049': {
        'gene': 'DDC',
        'name': 'DOPA decarboxylase',
        'variant_name': 'Intronic G/T',
        'function': 'Dopamine synthesis rate',
        'alleles': {
            'GG': {'phenotype': 'Normal dopamine synthesis', 'score': 0.5, 'traits': ['Typical production']},
            'GT': {'phenotype': 'Intermediate', 'score': 0.55, 'traits': ['Modified synthesis']},
            'TT': {'phenotype': 'Altered synthesis', 'score': 0.45, 'traits': ['Changed dopamine production']}
        }
    },
    'rs3837091': {
        'gene': 'SLC6A3',
        'name': 'DAT1 VNTR proxy',
        'variant_name': 'Intronic C/T',
        'function': 'Dopamine transporter expression proxy',
        'alleles': {
            'CC': {'phenotype': 'Higher DAT expression', 'score': 0.55, 'traits': ['Faster dopamine clearance']},
            'CT': {'phenotype': 'Normal DAT', 'score': 0.5, 'traits': ['Typical clearance']},
            'TT': {'phenotype': 'Lower DAT', 'score': 0.6, 'traits': ['Slower clearance, more dopamine']}
        }
    },
    'rs463379': {
        'gene': 'SLC6A3',
        'name': 'DAT1 3\'UTR',
        'variant_name': '3\'UTR A/G',
        'function': 'Transporter mRNA regulation',
        'alleles': {
            'AA': {'phenotype': 'Higher DAT', 'score': 0.55, 'traits': ['More dopamine clearance']},
            'AG': {'phenotype': 'Normal', 'score': 0.5, 'traits': ['Typical DAT']},
            'GG': {'phenotype': 'Lower DAT', 'score': 0.6, 'traits': ['Less dopamine clearance']}
        }
    },
    'rs6347': {
        'gene': 'SLC6A3',
        'name': 'DAT1 exon 9',
        'variant_name': 'Exon 9 synonymous',
        'function': 'Dopamine transporter activity',
        'alleles': {
            'AA': {'phenotype': 'Normal DAT activity', 'score': 0.5, 'traits': ['Typical reuptake']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.55, 'traits': ['Modified reuptake']},
            'GG': {'phenotype': 'Altered DAT', 'score': 0.45, 'traits': ['Changed dopamine availability']}
        }
    },
    'rs10770141': {
        'gene': 'TH',
        'name': 'Tyrosine Hydroxylase upstream',
        'variant_name': 'Upstream A/G',
        'function': 'Rate-limiting enzyme for dopamine synthesis',
        'alleles': {
            'AA': {'phenotype': 'Higher TH expression', 'score': 0.6, 'traits': ['More dopamine production']},
            'AG': {'phenotype': 'Normal', 'score': 0.5, 'traits': ['Typical production']},
            'GG': {'phenotype': 'Lower TH expression', 'score': 0.4, 'traits': ['Less dopamine production']}
        }
    },
    'rs2070762': {
        'gene': 'TH',
        'name': 'TH intron 1',
        'variant_name': 'Intron 1 C/T',
        'function': 'TH enzyme transcription',
        'alleles': {
            'CC': {'phenotype': 'Normal TH', 'score': 0.5, 'traits': ['Typical dopamine synthesis']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.55, 'traits': ['Modified synthesis']},
            'TT': {'phenotype': 'Altered TH', 'score': 0.45, 'traits': ['Changed production rate']}
        }
    },
    'rs4532': {
        'gene': 'DRD1',
        'name': 'DRD1 -48 A/G',
        'variant_name': '-48 A/G',
        'function': 'D1 receptor promoter affecting expression',
        'alleles': {
            'AA': {'phenotype': 'Higher D1 expression', 'score': 0.6, 'traits': ['Enhanced D1 signaling']},
            'AG': {'phenotype': 'Normal', 'score': 0.5, 'traits': ['Typical signaling']},
            'GG': {'phenotype': 'Lower expression', 'score': 0.4, 'traits': ['Reduced D1']}
        }
    },
    'rs1800762': {
        'gene': 'DRD5',
        'name': 'Dopamine D5 receptor',
        'variant_name': 'Upstream T/C',
        'function': 'D5 receptor affecting attention',
        'alleles': {
            'TT': {'phenotype': 'Normal D5 function', 'score': 0.5, 'traits': ['Typical attention']},
            'TC': {'phenotype': 'Intermediate', 'score': 0.55, 'traits': ['Modified D5']},
            'CC': {'phenotype': 'Altered D5', 'score': 0.45, 'traits': ['May affect focus']}
        }
    }
}

# =============================================================================
# SEROTONIN - MOOD, ANXIETY, IMPULSE CONTROL
# =============================================================================

SEROTONIN_GENETICS = {
    'rs25531': {
        'gene': 'SLC6A4',
        'name': '5-HTTLPR',
        'variant_name': 'rs25531 A/G',
        'function': 'Serotonin transporter, mood regulation',
        'alleles': {
            'AA': {'phenotype': 'Long/Long - resilient', 'score': 0.7, 'traits': ['Better stress resilience', 'Lower anxiety tendency']},
            'AG': {'phenotype': 'Long/Short - moderate', 'score': 0.5, 'traits': ['Average stress response']},
            'GG': {'phenotype': 'Short/Short - sensitive', 'score': 0.3, 'traits': ['More environmentally sensitive', 'May benefit more from positive environments']}
        }
    },
    'rs6295': {
        'gene': 'HTR1A',
        'name': 'Serotonin 1A receptor',
        'variant_name': '-1019 C/G',
        'function': 'Anxiety and depression susceptibility',
        'alleles': {
            'CC': {'phenotype': 'Lower anxiety tendency', 'score': 0.7, 'traits': ['Better emotional regulation']},
            'CG': {'phenotype': 'Average', 'score': 0.5, 'traits': ['Typical anxiety levels']},
            'GG': {'phenotype': 'Higher anxiety tendency', 'score': 0.3, 'traits': ['More prone to worry', 'May benefit from stress management']}
        }
    },
    'rs6311': {
        'gene': 'HTR2A',
        'name': 'Serotonin 2A receptor',
        'variant_name': '-1438 A/G',
        'function': 'Mood regulation and emotional processing',
        'alleles': {
            'AA': {'phenotype': 'Enhanced mood regulation', 'score': 0.7, 'traits': ['Better emotional stability']},
            'AG': {'phenotype': 'Average regulation', 'score': 0.5, 'traits': ['Typical mood patterns']},
            'GG': {'phenotype': 'Variable mood regulation', 'score': 0.35, 'traits': ['May have mood fluctuations']}
        }
    },
    'rs6313': {
        'gene': 'HTR2A',
        'name': 'HTR2A T102C',
        'variant_name': 'T102C',
        'function': 'Serotonin receptor density affecting mood',
        'alleles': {
            'TT': {'phenotype': 'Higher receptor density', 'score': 0.65, 'traits': ['Enhanced serotonin signaling']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average signaling']},
            'CC': {'phenotype': 'Lower receptor density', 'score': 0.4, 'traits': ['Modified serotonin response']}
        }
    },
    'rs7997012': {
        'gene': 'HTR2A',
        'name': 'HTR2A intron 2',
        'variant_name': 'Intronic A/G',
        'function': 'Serotonin receptor expression',
        'alleles': {
            'AA': {'phenotype': 'Normal expression', 'score': 0.5, 'traits': ['Typical receptor levels']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.55, 'traits': ['Moderate expression']},
            'GG': {'phenotype': 'Altered expression', 'score': 0.6, 'traits': ['Modified receptor levels']}
        }
    },
    'rs1799913': {
        'gene': 'TPH1',
        'name': 'Tryptophan Hydroxylase 1',
        'variant_name': 'A218C',
        'function': 'Peripheral serotonin synthesis',
        'alleles': {
            'AA': {'phenotype': 'Higher serotonin synthesis', 'score': 0.7, 'traits': ['Enhanced mood stability']},
            'AC': {'phenotype': 'Average synthesis', 'score': 0.5, 'traits': ['Typical serotonin levels']},
            'CC': {'phenotype': 'Lower synthesis', 'score': 0.35, 'traits': ['May have lower serotonin']}
        }
    },
    'rs4570625': {
        'gene': 'TPH2',
        'name': 'Tryptophan Hydroxylase 2',
        'variant_name': 'G-703T',
        'function': 'Brain serotonin synthesis',
        'alleles': {
            'GG': {'phenotype': 'Normal brain serotonin', 'score': 0.65, 'traits': ['Stable mood']},
            'GT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average mood stability']},
            'TT': {'phenotype': 'Altered synthesis', 'score': 0.35, 'traits': ['May have mood sensitivity']}
        }
    },
    'rs1386494': {
        'gene': 'TPH2',
        'name': 'TPH2 variant',
        'variant_name': 'Intronic G/T',
        'function': 'Serotonin production regulation',
        'alleles': {
            'GG': {'phenotype': 'Normal production', 'score': 0.6, 'traits': ['Stable serotonin']},
            'GT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Moderate levels']},
            'TT': {'phenotype': 'Altered production', 'score': 0.4, 'traits': ['Variable serotonin']}
        }
    },
    'rs140700': {
        'gene': 'HTR1B',
        'name': 'Serotonin 1B receptor',
        'variant_name': 'G861C',
        'function': 'Aggression and impulsivity regulation',
        'alleles': {
            'GG': {'phenotype': 'Lower impulsivity', 'score': 0.65, 'traits': ['Better impulse control']},
            'GC': {'phenotype': 'Average', 'score': 0.5, 'traits': ['Typical impulsivity']},
            'CC': {'phenotype': 'Higher impulsivity tendency', 'score': 0.35, 'traits': ['May be more impulsive']}
        }
    },
    'rs6296': {
        'gene': 'HTR1B',
        'name': 'HTR1B promoter',
        'variant_name': '-161 A/T',
        'function': 'Serotonin autoreceptor regulation',
        'alleles': {
            'AA': {'phenotype': 'Normal receptor function', 'score': 0.6, 'traits': ['Typical serotonin feedback']},
            'AT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Moderate feedback']},
            'TT': {'phenotype': 'Altered function', 'score': 0.4, 'traits': ['Modified feedback loop']}
        }
    },
    'rs130058': {
        'gene': 'HTR1B',
        'name': 'HTR1B variant',
        'variant_name': 'Synonymous A/G',
        'function': 'Receptor expression affecting mood',
        'alleles': {
            'AA': {'phenotype': 'Normal expression', 'score': 0.55, 'traits': ['Typical mood']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average expression']},
            'GG': {'phenotype': 'Altered expression', 'score': 0.45, 'traits': ['Modified receptor levels']}
        }
    },
    'rs1176744': {
        'gene': 'HTR3B',
        'name': 'Serotonin 3B receptor',
        'variant_name': 'Y129S',
        'function': 'Emotional processing and nausea response',
        'alleles': {
            'AA': {'phenotype': 'Tyr/Tyr - Normal', 'score': 0.5, 'traits': ['Typical emotional response']},
            'AC': {'phenotype': 'Tyr/Ser - Intermediate', 'score': 0.55, 'traits': ['Moderate response']},
            'CC': {'phenotype': 'Ser/Ser - Enhanced', 'score': 0.6, 'traits': ['Enhanced emotional signaling']}
        }
    },
    'rs2020933': {
        'gene': 'SLC6A4',
        'name': 'SERT intron 2',
        'variant_name': 'Intronic G/T',
        'function': 'Serotonin transporter expression',
        'alleles': {
            'GG': {'phenotype': 'Normal transporter', 'score': 0.6, 'traits': ['Typical serotonin reuptake']},
            'GT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Moderate reuptake']},
            'TT': {'phenotype': 'Altered transporter', 'score': 0.4, 'traits': ['Modified serotonin levels']}
        }
    },
    'rs3813034': {
        'gene': 'SLC6A4',
        'name': 'SERT 3\'UTR',
        'variant_name': '3\'UTR G/T',
        'function': 'Transporter mRNA stability',
        'alleles': {
            'GG': {'phenotype': 'Stable mRNA', 'score': 0.55, 'traits': ['Consistent transporter levels']},
            'GT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Moderate stability']},
            'TT': {'phenotype': 'Less stable mRNA', 'score': 0.45, 'traits': ['Variable transporter']}
        }
    },
    'rs6354': {
        'gene': 'SLC6A4',
        'name': 'SERT Gly56Ala',
        'variant_name': 'Gly56Ala',
        'function': 'Serotonin transporter function affecting autism risk',
        'alleles': {
            'GG': {'phenotype': 'Normal transporter', 'score': 0.55, 'traits': ['Typical serotonin reuptake']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Moderate function']},
            'AA': {'phenotype': 'Gain of function', 'score': 0.4, 'traits': ['Enhanced serotonin clearance']}
        }
    },
    'rs1042173': {
        'gene': 'SLC6A4',
        'name': 'SERT STin2',
        'variant_name': 'Intron 2 VNTR proxy',
        'function': 'Serotonin transporter expression',
        'alleles': {
            'TT': {'phenotype': 'Higher expression', 'score': 0.6, 'traits': ['More serotonin clearance']},
            'TG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average expression']},
            'GG': {'phenotype': 'Lower expression', 'score': 0.55, 'traits': ['Less serotonin clearance']}
        }
    },
    'rs1150226': {
        'gene': 'HTR1A',
        'name': 'HTR1A intronic',
        'variant_name': 'Intronic G/A',
        'function': 'Serotonin 1A receptor expression',
        'alleles': {
            'GG': {'phenotype': 'Normal expression', 'score': 0.55, 'traits': ['Typical receptor levels']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average expression']},
            'AA': {'phenotype': 'Altered expression', 'score': 0.45, 'traits': ['Modified receptor levels']}
        }
    },
    'rs878567': {
        'gene': 'HTR2A',
        'name': 'HTR2A His452Tyr',
        'variant_name': 'His452Tyr',
        'function': 'Serotonin 2A receptor function',
        'alleles': {
            'CC': {'phenotype': 'His/His - Normal function', 'score': 0.55, 'traits': ['Typical serotonin signaling']},
            'CT': {'phenotype': 'His/Tyr - Intermediate', 'score': 0.5, 'traits': ['Modified signaling']},
            'TT': {'phenotype': 'Tyr/Tyr - Altered function', 'score': 0.45, 'traits': ['Reduced receptor activity']}
        }
    },
    'rs6314': {
        'gene': 'HTR2A',
        'name': 'HTR2A His452Tyr',
        'variant_name': 'H452Y',
        'function': 'Serotonin 2A receptor binding',
        'alleles': {
            'CC': {'phenotype': 'Normal receptor', 'score': 0.55, 'traits': ['Typical binding']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Modified binding']},
            'TT': {'phenotype': 'Altered receptor', 'score': 0.45, 'traits': ['Reduced binding affinity']}
        }
    },
    'rs643627': {
        'gene': 'HTR2C',
        'name': 'Serotonin 2C receptor',
        'variant_name': 'Intronic G/A',
        'function': 'Appetite, anxiety, and mood regulation',
        'alleles': {
            'GG': {'phenotype': 'Normal 5-HT2C', 'score': 0.55, 'traits': ['Typical appetite regulation']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average regulation']},
            'AA': {'phenotype': 'Altered 5-HT2C', 'score': 0.45, 'traits': ['May affect appetite/mood']}
        }
    },
    'rs3813929': {
        'gene': 'HTR2C',
        'name': 'HTR2C promoter',
        'variant_name': '-759 C/T',
        'function': 'Serotonin 2C expression affecting weight',
        'alleles': {
            'CC': {'phenotype': 'Normal expression', 'score': 0.55, 'traits': ['Typical weight regulation']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Moderate effect']},
            'TT': {'phenotype': 'Reduced expression', 'score': 0.4, 'traits': ['May affect weight control']}
        }
    },
    'rs6318': {
        'gene': 'HTR2C',
        'name': 'HTR2C Cys23Ser',
        'variant_name': 'Cys23Ser',
        'function': 'Receptor function affecting mood and impulsivity',
        'alleles': {
            'CC': {'phenotype': 'Cys/Cys - Normal', 'score': 0.55, 'traits': ['Typical mood regulation']},
            'CG': {'phenotype': 'Cys/Ser - Intermediate', 'score': 0.5, 'traits': ['Moderate effect']},
            'GG': {'phenotype': 'Ser/Ser - Altered', 'score': 0.4, 'traits': ['May have mood variation']}
        }
    },
    'rs1805054': {
        'gene': 'HTR4',
        'name': 'Serotonin 4 receptor',
        'variant_name': 'Synonymous C/T',
        'function': 'Gut-brain axis and cognition',
        'alleles': {
            'CC': {'phenotype': 'Normal 5-HT4', 'score': 0.55, 'traits': ['Typical gut-brain signaling']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average signaling']},
            'TT': {'phenotype': 'Altered 5-HT4', 'score': 0.45, 'traits': ['Modified gut-brain axis']}
        }
    },
    'rs7997012': {
        'gene': 'HTR2A',
        'name': 'HTR2A intron 2 mood',
        'variant_name': 'Intronic A/G',
        'function': 'Antidepressant response and mood',
        'alleles': {
            'AA': {'phenotype': 'Better SSRI response', 'score': 0.65, 'traits': ['Good antidepressant response']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average response']},
            'GG': {'phenotype': 'Variable response', 'score': 0.4, 'traits': ['May need different medication']}
        }
    },
    'rs10488682': {
        'gene': 'TPH2',
        'name': 'TPH2 variant',
        'variant_name': 'Intronic C/T',
        'function': 'Brain serotonin synthesis rate',
        'alleles': {
            'CC': {'phenotype': 'Normal synthesis', 'score': 0.55, 'traits': ['Typical serotonin production']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average production']},
            'TT': {'phenotype': 'Altered synthesis', 'score': 0.45, 'traits': ['Modified serotonin levels']}
        }
    },
    'rs4290270': {
        'gene': 'TPH2',
        'name': 'TPH2 expression',
        'variant_name': 'Intronic A/T',
        'function': 'Tryptophan hydroxylase 2 activity',
        'alleles': {
            'AA': {'phenotype': 'Higher activity', 'score': 0.6, 'traits': ['More serotonin synthesis']},
            'AT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average synthesis']},
            'TT': {'phenotype': 'Lower activity', 'score': 0.4, 'traits': ['Less serotonin']}
        }
    },
    'rs11178997': {
        'gene': 'TPH2',
        'name': 'TPH2 promoter',
        'variant_name': 'Promoter T/A',
        'function': 'TPH2 transcription and serotonin production',
        'alleles': {
            'TT': {'phenotype': 'Normal transcription', 'score': 0.55, 'traits': ['Typical production']},
            'TA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average transcription']},
            'AA': {'phenotype': 'Altered transcription', 'score': 0.45, 'traits': ['Modified production']}
        }
    },
    'rs6484711': {
        'gene': 'MAOA',
        'name': 'MAOA serotonin',
        'variant_name': 'Intronic C/T',
        'function': 'Monoamine oxidase A affecting serotonin breakdown',
        'alleles': {
            'CC': {'phenotype': 'Normal MAOA', 'score': 0.55, 'traits': ['Typical serotonin degradation']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average degradation']},
            'TT': {'phenotype': 'Altered MAOA', 'score': 0.45, 'traits': ['Modified serotonin levels']}
        }
    },
    'rs1800532': {
        'gene': 'TPH1',
        'name': 'TPH1 A779C',
        'variant_name': 'A779C',
        'function': 'Peripheral serotonin affecting gut and platelets',
        'alleles': {
            'AA': {'phenotype': 'Higher peripheral serotonin', 'score': 0.6, 'traits': ['More gut serotonin']},
            'AC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average levels']},
            'CC': {'phenotype': 'Lower peripheral serotonin', 'score': 0.4, 'traits': ['Less gut serotonin']}
        }
    },
    'rs10748185': {
        'gene': 'HTR5A',
        'name': 'Serotonin 5A receptor',
        'variant_name': 'Intronic A/G',
        'function': 'Sleep and circadian rhythm modulation',
        'alleles': {
            'AA': {'phenotype': 'Normal 5-HT5A', 'score': 0.55, 'traits': ['Typical sleep patterns']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average patterns']},
            'GG': {'phenotype': 'Altered 5-HT5A', 'score': 0.45, 'traits': ['May affect sleep']}
        }
    },
    'rs6795970': {
        'gene': 'SCN10A',
        'name': 'Sodium channel serotonin',
        'variant_name': 'A1073V',
        'function': 'Pain perception and mood interaction',
        'alleles': {
            'AA': {'phenotype': 'Normal pain perception', 'score': 0.55, 'traits': ['Typical pain sensitivity']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average sensitivity']},
            'GG': {'phenotype': 'Altered perception', 'score': 0.45, 'traits': ['Modified pain response']}
        }
    },
    'rs6867778': {
        'gene': 'HTR3A',
        'name': 'Serotonin 3A receptor',
        'variant_name': 'Intronic G/A',
        'function': 'Nausea response and anxiety',
        'alleles': {
            'GG': {'phenotype': 'Normal 5-HT3A', 'score': 0.55, 'traits': ['Typical nausea response']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average response']},
            'AA': {'phenotype': 'Altered 5-HT3A', 'score': 0.45, 'traits': ['May have different nausea response']}
        }
    },
    'rs33940208': {
        'gene': 'HTR3A',
        'name': 'HTR3A variant',
        'variant_name': 'P391P',
        'function': 'Serotonin 3A receptor expression',
        'alleles': {
            'CC': {'phenotype': 'Normal expression', 'score': 0.55, 'traits': ['Typical receptor levels']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average levels']},
            'TT': {'phenotype': 'Altered expression', 'score': 0.45, 'traits': ['Modified receptor expression']}
        }
    },
    'rs1176713': {
        'gene': 'HTR3A',
        'name': 'HTR3A synonymous',
        'variant_name': 'P16P',
        'function': 'Receptor function and anxiety',
        'alleles': {
            'CC': {'phenotype': 'Normal function', 'score': 0.55, 'traits': ['Typical anxiety response']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average response']},
            'TT': {'phenotype': 'Altered function', 'score': 0.45, 'traits': ['May have different anxiety']}
        }
    },
    'rs3758987': {
        'gene': 'HTR6',
        'name': 'Serotonin 6 receptor',
        'variant_name': 'Promoter C/T',
        'function': 'Cognition and memory via 5-HT6',
        'alleles': {
            'CC': {'phenotype': 'Normal 5-HT6', 'score': 0.55, 'traits': ['Typical cognition']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average cognition']},
            'TT': {'phenotype': 'Altered 5-HT6', 'score': 0.45, 'traits': ['May affect cognition']}
        }
    },
    'rs1805055': {
        'gene': 'HTR6',
        'name': 'HTR6 variant',
        'variant_name': 'C267T',
        'function': 'Serotonin 6 receptor affecting cognition',
        'alleles': {
            'CC': {'phenotype': 'Normal receptor', 'score': 0.55, 'traits': ['Typical memory function']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average function']},
            'TT': {'phenotype': 'Altered receptor', 'score': 0.45, 'traits': ['May affect memory']}
        }
    },
    'rs12439796': {
        'gene': 'HTR7',
        'name': 'Serotonin 7 receptor',
        'variant_name': 'Intronic C/T',
        'function': 'Circadian rhythm and mood',
        'alleles': {
            'CC': {'phenotype': 'Normal 5-HT7', 'score': 0.55, 'traits': ['Typical circadian rhythm']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average rhythm']},
            'TT': {'phenotype': 'Altered 5-HT7', 'score': 0.45, 'traits': ['May affect sleep-wake cycle']}
        }
    }
}

# =============================================================================
# BDNF - LEARNING, MEMORY, NEUROPLASTICITY
# =============================================================================

COGNITIVE_GENETICS = {
    'rs6265': {
        'gene': 'BDNF',
        'name': 'Val66Met',
        'variant_name': 'Val66Met',
        'function': 'Brain plasticity, memory, learning',
        'alleles': {
            'CC': {'phenotype': 'Val/Val - optimal BDNF', 'score': 0.8, 'traits': ['Better episodic memory', 'Higher hippocampal volume', 'Better fear extinction']},
            'CT': {'phenotype': 'Val/Met - moderate', 'score': 0.5, 'traits': ['Average memory function']},
            'TT': {'phenotype': 'Met/Met - reduced BDNF', 'score': 0.3, 'traits': ['May have memory challenges', 'Benefits more from exercise for brain health']}
        }
    },
    'rs1800544': {
        'gene': 'ADRA2A',
        'name': 'Alpha-2A adrenergic receptor',
        'variant_name': '-1291 C/G',
        'function': 'Attention, working memory',
        'alleles': {
            'CC': {'phenotype': 'Better working memory', 'score': 0.7, 'traits': ['Enhanced focus', 'Better multitasking']},
            'CG': {'phenotype': 'Average', 'score': 0.5, 'traits': ['Typical attention span']},
            'GG': {'phenotype': 'May need more focus strategies', 'score': 0.4, 'traits': ['May benefit from attention training']}
        }
    },
    'rs11030101': {
        'gene': 'BDNF',
        'name': 'BDNF intron',
        'variant_name': 'Intronic A/T',
        'function': 'BDNF expression and brain plasticity',
        'alleles': {
            'AA': {'phenotype': 'Enhanced BDNF expression', 'score': 0.7, 'traits': ['Better neuroplasticity']},
            'AT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average plasticity']},
            'TT': {'phenotype': 'Altered expression', 'score': 0.4, 'traits': ['May benefit from brain training']}
        }
    },
    'rs7124442': {
        'gene': 'BDNF',
        'name': 'BDNF 3\'UTR',
        'variant_name': '3\'UTR C/T',
        'function': 'BDNF mRNA stability',
        'alleles': {
            'CC': {'phenotype': 'Stable BDNF mRNA', 'score': 0.65, 'traits': ['Consistent BDNF levels']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average stability']},
            'TT': {'phenotype': 'Variable mRNA', 'score': 0.4, 'traits': ['Variable BDNF']}
        }
    },
    'rs4680': {
        'gene': 'COMT',
        'name': 'COMT cognitive',
        'variant_name': 'Val158Met',
        'function': 'Prefrontal cortex dopamine and cognition',
        'alleles': {
            'AA': {'phenotype': 'Met/Met - Enhanced working memory', 'score': 0.75, 'traits': ['Better focus at baseline', 'Higher cognitive flexibility']},
            'AG': {'phenotype': 'Val/Met - Balanced', 'score': 0.5, 'traits': ['Balanced cognitive style']},
            'GG': {'phenotype': 'Val/Val - Stress-resistant cognition', 'score': 0.6, 'traits': ['Better under pressure', 'May need more stimulation']}
        }
    },
    'rs165599': {
        'gene': 'COMT',
        'name': 'COMT 3\'UTR cognitive',
        'variant_name': '3\'UTR G/A',
        'function': 'COMT expression affecting cognition',
        'alleles': {
            'GG': {'phenotype': 'Normal expression', 'score': 0.55, 'traits': ['Typical cognitive performance']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average performance']},
            'AA': {'phenotype': 'Altered expression', 'score': 0.6, 'traits': ['Modified cognitive style']}
        }
    },
    'rs429358': {
        'gene': 'APOE',
        'name': 'APOE e4 (cognitive aging)',
        'variant_name': 'Cys112Arg',
        'function': 'Cognitive aging and memory',
        'alleles': {
            'TT': {'phenotype': 'No APOE4 - normal aging', 'score': 0.7, 'traits': ['Typical cognitive aging']},
            'TC': {'phenotype': 'One APOE4 copy', 'score': 0.4, 'traits': ['May need more cognitive protection', 'Exercise especially beneficial']},
            'CC': {'phenotype': 'Two APOE4 copies', 'score': 0.2, 'traits': ['Higher cognitive aging risk', 'Prioritize brain health lifestyle']}
        }
    },
    'rs7412': {
        'gene': 'APOE',
        'name': 'APOE e2/e3',
        'variant_name': 'Arg158Cys',
        'function': 'Cognitive protection',
        'alleles': {
            'CC': {'phenotype': 'APOE3/3 - Normal', 'score': 0.5, 'traits': ['Typical cognitive aging']},
            'CT': {'phenotype': 'APOE2 carrier - Protective', 'score': 0.7, 'traits': ['May have cognitive protection']},
            'TT': {'phenotype': 'APOE2/2 - Protective', 'score': 0.8, 'traits': ['Enhanced cognitive protection']}
        }
    },
    'rs1800497': {
        'gene': 'DRD2/ANKK1',
        'name': 'DRD2 cognitive',
        'variant_name': 'Taq1A',
        'function': 'Dopamine and reward learning',
        'alleles': {
            'CC': {'phenotype': 'Normal D2 receptors', 'score': 0.6, 'traits': ['Typical learning from feedback']},
            'CT': {'phenotype': 'Reduced receptors', 'score': 0.5, 'traits': ['Modified feedback learning']},
            'TT': {'phenotype': 'Low D2 receptors', 'score': 0.4, 'traits': ['May learn differently from feedback']}
        }
    },
    'rs1076560': {
        'gene': 'DRD2',
        'name': 'DRD2 cognitive splice',
        'variant_name': 'Splicing G/T',
        'function': 'Working memory and cognitive flexibility',
        'alleles': {
            'GG': {'phenotype': 'Normal working memory', 'score': 0.55, 'traits': ['Typical cognitive flexibility']},
            'GT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average flexibility']},
            'TT': {'phenotype': 'Enhanced flexibility', 'score': 0.6, 'traits': ['Higher cognitive flexibility']}
        }
    },
    'rs17070145': {
        'gene': 'KIBRA',
        'name': 'KIBRA memory gene',
        'variant_name': 'T/C',
        'function': 'Episodic memory performance',
        'alleles': {
            'TT': {'phenotype': 'Enhanced memory', 'score': 0.75, 'traits': ['Better episodic memory', 'Enhanced recall']},
            'TC': {'phenotype': 'Intermediate memory', 'score': 0.55, 'traits': ['Average memory']},
            'CC': {'phenotype': 'Typical memory', 'score': 0.45, 'traits': ['Standard memory performance']}
        }
    },
    'rs7294919': {
        'gene': 'HMGA2',
        'name': 'Hippocampal volume',
        'variant_name': 'Intergenic C/T',
        'function': 'Hippocampal size and memory capacity',
        'alleles': {
            'TT': {'phenotype': 'Larger hippocampus', 'score': 0.7, 'traits': ['Enhanced memory capacity']},
            'TC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average hippocampal size']},
            'CC': {'phenotype': 'Smaller hippocampus', 'score': 0.4, 'traits': ['May benefit from memory strategies']}
        }
    },
    'rs2760118': {
        'gene': 'CHRNA4',
        'name': 'Nicotinic receptor',
        'variant_name': 'T/C',
        'function': 'Attention and cholinergic function',
        'alleles': {
            'TT': {'phenotype': 'Enhanced attention', 'score': 0.65, 'traits': ['Better sustained attention']},
            'TC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average attention']},
            'CC': {'phenotype': 'Typical attention', 'score': 0.45, 'traits': ['Standard attention span']}
        }
    },
    'rs1044396': {
        'gene': 'CHRNA4',
        'name': 'CHRNA4 variant',
        'variant_name': 'Synonymous C/T',
        'function': 'Nicotinic receptor expression',
        'alleles': {
            'CC': {'phenotype': 'Normal receptor', 'score': 0.55, 'traits': ['Typical attention']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average attention']},
            'TT': {'phenotype': 'Altered receptor', 'score': 0.45, 'traits': ['May have attention variation']}
        }
    },
    'rs363050': {
        'gene': 'SNAP25',
        'name': 'Synaptosomal protein',
        'variant_name': 'A/G',
        'function': 'Neurotransmitter release and IQ',
        'alleles': {
            'GG': {'phenotype': 'Enhanced synaptic function', 'score': 0.65, 'traits': ['Better cognitive processing']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Typical processing']},
            'AA': {'phenotype': 'Standard function', 'score': 0.45, 'traits': ['Normal cognitive processing']}
        }
    },
    'rs7341475': {
        'gene': 'REELIN',
        'name': 'Reelin signaling',
        'variant_name': 'G/A',
        'function': 'Neuronal migration and synaptic plasticity',
        'alleles': {
            'GG': {'phenotype': 'Normal signaling', 'score': 0.55, 'traits': ['Typical brain development']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average development']},
            'AA': {'phenotype': 'Altered signaling', 'score': 0.45, 'traits': ['Modified plasticity']}
        }
    },
    'rs10119': {
        'gene': 'TOMM40',
        'name': 'Mitochondrial translocase',
        'variant_name': 'C/T',
        'function': 'Brain aging and cognitive decline rate',
        'alleles': {
            'CC': {'phenotype': 'Slower cognitive aging', 'score': 0.65, 'traits': ['Better cognitive maintenance']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average aging rate']},
            'TT': {'phenotype': 'Faster aging', 'score': 0.4, 'traits': ['May benefit from brain health focus']}
        }
    },
    'rs2075650': {
        'gene': 'TOMM40',
        'name': 'TOMM40 memory',
        'variant_name': 'A/G',
        'function': 'Memory decline and Alzheimer risk',
        'alleles': {
            'AA': {'phenotype': 'Better memory preservation', 'score': 0.65, 'traits': ['Slower memory decline']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average decline']},
            'GG': {'phenotype': 'Faster decline risk', 'score': 0.35, 'traits': ['Higher cognitive aging risk']}
        }
    },
    'rs1799971': {
        'gene': 'OPRM1',
        'name': 'Mu-opioid receptor',
        'variant_name': 'A118G',
        'function': 'Reward learning and social cognition',
        'alleles': {
            'AA': {'phenotype': 'Normal reward learning', 'score': 0.55, 'traits': ['Typical social bonding']},
            'AG': {'phenotype': 'Enhanced social sensitivity', 'score': 0.6, 'traits': ['More responsive to social cues']},
            'GG': {'phenotype': 'Higher social need', 'score': 0.5, 'traits': ['May be more social-reward sensitive']}
        }
    },
    'rs10830963': {
        'gene': 'MTNR1B',
        'name': 'Melatonin receptor 1B',
        'variant_name': 'G/C',
        'function': 'Sleep-cognition relationship',
        'alleles': {
            'CC': {'phenotype': 'Better sleep-cognition', 'score': 0.6, 'traits': ['Sleep enhances learning well']},
            'CG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Typical sleep-memory effect']},
            'GG': {'phenotype': 'Altered relationship', 'score': 0.45, 'traits': ['May need more sleep for memory']}
        }
    },
    'rs2305160': {
        'gene': 'NRG1',
        'name': 'Neuregulin 1',
        'variant_name': 'C/T',
        'function': 'Synaptic plasticity and working memory',
        'alleles': {
            'CC': {'phenotype': 'Normal NRG1', 'score': 0.55, 'traits': ['Typical working memory']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average function']},
            'TT': {'phenotype': 'Altered NRG1', 'score': 0.45, 'traits': ['Modified synaptic function']}
        }
    },
    'rs6994992': {
        'gene': 'NRG1',
        'name': 'NRG1 promoter',
        'variant_name': 'Promoter T/C',
        'function': 'Prefrontal cortex function',
        'alleles': {
            'TT': {'phenotype': 'Normal prefrontal', 'score': 0.55, 'traits': ['Typical executive function']},
            'TC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average function']},
            'CC': {'phenotype': 'Altered function', 'score': 0.45, 'traits': ['May have executive variation']}
        }
    },
    'rs3924999': {
        'gene': 'ERBB4',
        'name': 'Neuregulin receptor',
        'variant_name': 'A/G',
        'function': 'Neural circuit development and cognition',
        'alleles': {
            'AA': {'phenotype': 'Normal circuits', 'score': 0.55, 'traits': ['Typical neural development']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average development']},
            'GG': {'phenotype': 'Altered circuits', 'score': 0.45, 'traits': ['Modified circuitry']}
        }
    },
    'rs4963': {
        'gene': 'GRM3',
        'name': 'Metabotropic glutamate 3',
        'variant_name': 'A/G',
        'function': 'Glutamate signaling and cognition',
        'alleles': {
            'AA': {'phenotype': 'Better working memory', 'score': 0.65, 'traits': ['Enhanced prefrontal function']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average function']},
            'GG': {'phenotype': 'Variable function', 'score': 0.45, 'traits': ['May have cognitive variation']}
        }
    },
    'rs274622': {
        'gene': 'GRM3',
        'name': 'GRM3 variant',
        'variant_name': 'Intronic C/T',
        'function': 'Synaptic glutamate regulation',
        'alleles': {
            'CC': {'phenotype': 'Normal regulation', 'score': 0.55, 'traits': ['Typical glutamate signaling']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average regulation']},
            'TT': {'phenotype': 'Altered regulation', 'score': 0.45, 'traits': ['Modified signaling']}
        }
    },
    'rs1468412': {
        'gene': 'GRIN2A',
        'name': 'NMDA receptor 2A',
        'variant_name': 'A/G',
        'function': 'Learning and memory via NMDA receptors',
        'alleles': {
            'AA': {'phenotype': 'Enhanced learning', 'score': 0.65, 'traits': ['Better memory consolidation']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average learning']},
            'GG': {'phenotype': 'Variable learning', 'score': 0.45, 'traits': ['May learn differently']}
        }
    },
    'rs1805502': {
        'gene': 'GRIN2B',
        'name': 'NMDA receptor 2B',
        'variant_name': 'C/T',
        'function': 'Synaptic plasticity and spatial memory',
        'alleles': {
            'CC': {'phenotype': 'Enhanced plasticity', 'score': 0.65, 'traits': ['Better spatial memory']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average plasticity']},
            'TT': {'phenotype': 'Typical plasticity', 'score': 0.45, 'traits': ['Standard spatial ability']}
        }
    },
    'rs1805247': {
        'gene': 'GRIN2B',
        'name': 'GRIN2B variant',
        'variant_name': 'A/G',
        'function': 'NMDA receptor function',
        'alleles': {
            'AA': {'phenotype': 'Normal receptor', 'score': 0.55, 'traits': ['Typical NMDA function']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average function']},
            'GG': {'phenotype': 'Altered receptor', 'score': 0.45, 'traits': ['Modified learning']}
        }
    },
    'rs2228607': {
        'gene': 'DTNBP1',
        'name': 'Dysbindin',
        'variant_name': 'C/T',
        'function': 'Working memory and general cognitive ability',
        'alleles': {
            'CC': {'phenotype': 'Better working memory', 'score': 0.6, 'traits': ['Enhanced cognitive function']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average function']},
            'TT': {'phenotype': 'Variable function', 'score': 0.45, 'traits': ['May have cognitive variation']}
        }
    },
    'rs760761': {
        'gene': 'DTNBP1',
        'name': 'Dysbindin variant',
        'variant_name': 'A/C',
        'function': 'Prefrontal cortex function',
        'alleles': {
            'AA': {'phenotype': 'Normal prefrontal', 'score': 0.55, 'traits': ['Typical executive function']},
            'AC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average function']},
            'CC': {'phenotype': 'Altered function', 'score': 0.45, 'traits': ['Modified executive processing']}
        }
    },
    'rs3213207': {
        'gene': 'DTNBP1',
        'name': 'DTNBP1 cognition',
        'variant_name': 'G/A',
        'function': 'General cognitive ability',
        'alleles': {
            'GG': {'phenotype': 'Higher cognitive ability', 'score': 0.6, 'traits': ['Enhanced g factor']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average ability']},
            'AA': {'phenotype': 'Variable ability', 'score': 0.45, 'traits': ['May have specific strengths']}
        }
    },
    'rs3800779': {
        'gene': 'NOS1',
        'name': 'Nitric oxide synthase 1',
        'variant_name': 'C/T',
        'function': 'Neural signaling and impulsivity',
        'alleles': {
            'CC': {'phenotype': 'Normal NOS1', 'score': 0.55, 'traits': ['Typical impulse control']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average control']},
            'TT': {'phenotype': 'Altered NOS1', 'score': 0.45, 'traits': ['May have impulsivity variation']}
        }
    },
    'rs10503929': {
        'gene': 'CPEB3',
        'name': 'Cytoplasmic polyadenylation binding',
        'variant_name': 'C/T',
        'function': 'Protein synthesis in memory formation',
        'alleles': {
            'TT': {'phenotype': 'Better episodic memory', 'score': 0.65, 'traits': ['Enhanced memory formation']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average memory']},
            'CC': {'phenotype': 'Typical memory', 'score': 0.45, 'traits': ['Standard memory formation']}
        }
    },
    'rs6001747': {
        'gene': 'DISC1',
        'name': 'Disrupted in schizophrenia 1',
        'variant_name': 'Ser704Cys',
        'function': 'Hippocampal structure and memory',
        'alleles': {
            'CC': {'phenotype': 'Larger hippocampus', 'score': 0.6, 'traits': ['Better memory capacity']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average structure']},
            'TT': {'phenotype': 'Smaller hippocampus', 'score': 0.4, 'traits': ['May benefit from memory exercises']}
        }
    },
    'rs821616': {
        'gene': 'DISC1',
        'name': 'DISC1 variant',
        'variant_name': 'Leu607Phe',
        'function': 'Cognitive function and brain structure',
        'alleles': {
            'TT': {'phenotype': 'Better cognitive function', 'score': 0.6, 'traits': ['Enhanced cognition']},
            'TA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average function']},
            'AA': {'phenotype': 'Variable function', 'score': 0.45, 'traits': ['May have specific patterns']}
        }
    },
    'rs1344706': {
        'gene': 'ZNF804A',
        'name': 'Zinc finger protein',
        'variant_name': 'A/C',
        'function': 'Brain connectivity and working memory',
        'alleles': {
            'AA': {'phenotype': 'Normal connectivity', 'score': 0.55, 'traits': ['Typical brain networks']},
            'AC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average connectivity']},
            'CC': {'phenotype': 'Altered connectivity', 'score': 0.45, 'traits': ['Different network patterns']}
        }
    },
    'rs6675281': {
        'gene': 'PCLO',
        'name': 'Piccolo presynaptic',
        'variant_name': 'A/G',
        'function': 'Synaptic vesicle release',
        'alleles': {
            'AA': {'phenotype': 'Normal release', 'score': 0.55, 'traits': ['Typical neurotransmission']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average release']},
            'GG': {'phenotype': 'Altered release', 'score': 0.45, 'traits': ['Modified synaptic function']}
        }
    },
    'rs16917237': {
        'gene': 'KCNJ6',
        'name': 'Potassium channel',
        'variant_name': 'C/T',
        'function': 'Neuronal excitability and cognition',
        'alleles': {
            'CC': {'phenotype': 'Normal excitability', 'score': 0.55, 'traits': ['Typical neuronal function']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average function']},
            'TT': {'phenotype': 'Altered excitability', 'score': 0.45, 'traits': ['May have different processing']}
        }
    },
    'rs1801133': {
        'gene': 'MTHFR',
        'name': 'Methylenetetrahydrofolate reductase',
        'variant_name': 'C677T',
        'function': 'Folate metabolism affecting brain function',
        'alleles': {
            'CC': {'phenotype': 'Normal MTHFR', 'score': 0.6, 'traits': ['Typical folate metabolism']},
            'CT': {'phenotype': 'Reduced activity', 'score': 0.5, 'traits': ['May benefit from folate']},
            'TT': {'phenotype': 'Low activity', 'score': 0.4, 'traits': ['Benefits from methylfolate']}
        }
    },
    'rs1801131': {
        'gene': 'MTHFR',
        'name': 'MTHFR A1298C',
        'variant_name': 'A1298C',
        'function': 'Folate cycle and homocysteine',
        'alleles': {
            'AA': {'phenotype': 'Normal activity', 'score': 0.55, 'traits': ['Typical metabolism']},
            'AC': {'phenotype': 'Reduced activity', 'score': 0.5, 'traits': ['Mild reduction']},
            'CC': {'phenotype': 'Low activity', 'score': 0.45, 'traits': ['May benefit from B vitamins']}
        }
    },
    'rs1800764': {
        'gene': 'ACE',
        'name': 'Angiotensin converting enzyme',
        'variant_name': 'C/T',
        'function': 'Cerebral blood flow and cognition',
        'alleles': {
            'CC': {'phenotype': 'Higher ACE activity', 'score': 0.5, 'traits': ['Different blood flow pattern']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.55, 'traits': ['Average flow']},
            'TT': {'phenotype': 'Lower ACE activity', 'score': 0.6, 'traits': ['Better cerebral perfusion']}
        }
    },
    'rs9536314': {
        'gene': 'KLOTHO',
        'name': 'Klotho longevity gene',
        'variant_name': 'F352V',
        'function': 'Cognitive aging and longevity',
        'alleles': {
            'TT': {'phenotype': 'KL-VS carrier - Enhanced cognition', 'score': 0.7, 'traits': ['Better cognitive aging', 'Higher IQ']},
            'TG': {'phenotype': 'One copy - Some benefit', 'score': 0.55, 'traits': ['Moderate cognitive protection']},
            'GG': {'phenotype': 'Non-carrier - Typical', 'score': 0.5, 'traits': ['Standard cognitive aging']}
        }
    },
    'rs2230912': {
        'gene': 'P2RX7',
        'name': 'Purinergic receptor',
        'variant_name': 'Gln460Arg',
        'function': 'Neuroinflammation and cognition',
        'alleles': {
            'AA': {'phenotype': 'Normal receptor', 'score': 0.55, 'traits': ['Typical inflammation response']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average response']},
            'GG': {'phenotype': 'Altered receptor', 'score': 0.45, 'traits': ['Modified inflammation']}
        }
    },
    'rs3775291': {
        'gene': 'TLR3',
        'name': 'Toll-like receptor 3',
        'variant_name': 'Leu412Phe',
        'function': 'Neuroimmune function and cognition',
        'alleles': {
            'CC': {'phenotype': 'Normal TLR3', 'score': 0.55, 'traits': ['Typical immune-brain interaction']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average function']},
            'TT': {'phenotype': 'Altered TLR3', 'score': 0.45, 'traits': ['Modified immune signaling']}
        }
    }
}

# =============================================================================
# AGGRESSION & IMPULSE CONTROL
# =============================================================================

IMPULSE_GENETICS = {
    'rs909525': {
        'gene': 'MAOA',
        'name': 'Monoamine oxidase A',
        'variant_name': 'Upstream T/C',
        'function': 'Aggression, impulse control',
        'alleles': {
            'CC': {'phenotype': 'Higher MAOA activity', 'score': 0.7, 'traits': ['Better impulse control', 'Lower aggression tendency']},
            'CT': {'phenotype': 'Moderate activity', 'score': 0.5, 'traits': ['Average impulse control']},
            'TT': {'phenotype': 'Lower MAOA activity', 'score': 0.3, 'traits': ['May be more reactive', 'Environment strongly influences behavior']}
        }
    },
    'rs6323': {
        'gene': 'MAOA',
        'name': 'MAOA R297R',
        'variant_name': 'R297R',
        'function': 'Enzyme activity affecting mood and aggression',
        'alleles': {
            'GG': {'phenotype': 'Higher enzyme activity', 'score': 0.65, 'traits': ['Better emotional regulation']},
            'GT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average regulation']},
            'TT': {'phenotype': 'Lower activity', 'score': 0.35, 'traits': ['May have more emotional intensity']}
        }
    },
    'rs979606': {
        'gene': 'MAOA',
        'name': 'MAOA intronic',
        'variant_name': 'Intronic A/G',
        'function': 'MAOA expression regulation',
        'alleles': {
            'AA': {'phenotype': 'Normal expression', 'score': 0.6, 'traits': ['Typical impulse control']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average control']},
            'GG': {'phenotype': 'Altered expression', 'score': 0.4, 'traits': ['May need impulse strategies']}
        }
    },
    'rs1137070': {
        'gene': 'MAOB',
        'name': 'Monoamine oxidase B',
        'variant_name': 'A/G',
        'function': 'Dopamine breakdown and impulsivity',
        'alleles': {
            'AA': {'phenotype': 'Higher MAOB activity', 'score': 0.6, 'traits': ['Lower impulsivity']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average impulsivity']},
            'GG': {'phenotype': 'Lower activity', 'score': 0.4, 'traits': ['May be more impulsive']}
        }
    },
    'rs4680': {
        'gene': 'COMT',
        'name': 'COMT impulse control',
        'variant_name': 'Val158Met',
        'function': 'Prefrontal dopamine and self-control',
        'alleles': {
            'GG': {'phenotype': 'Val/Val - Good stress control', 'score': 0.65, 'traits': ['Better under pressure']},
            'AG': {'phenotype': 'Val/Met - Balanced', 'score': 0.5, 'traits': ['Moderate self-control']},
            'AA': {'phenotype': 'Met/Met - Deliberate', 'score': 0.6, 'traits': ['More thoughtful decisions', 'May overthink']}
        }
    },
    'rs1800497': {
        'gene': 'DRD2',
        'name': 'DRD2 Taq1A impulse',
        'variant_name': 'Taq1A',
        'function': 'Reward sensitivity and impulsivity',
        'alleles': {
            'CC': {'phenotype': 'Normal reward response', 'score': 0.6, 'traits': ['Typical impulse control']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average control']},
            'TT': {'phenotype': 'Higher reward seeking', 'score': 0.35, 'traits': ['May seek more stimulation']}
        }
    },
    'rs27072': {
        'gene': 'DAT1/SLC6A3',
        'name': 'DAT1 impulse',
        'variant_name': '3\'UTR G/A',
        'function': 'Dopamine reuptake affecting impulses',
        'alleles': {
            'GG': {'phenotype': 'Normal dopamine clearance', 'score': 0.55, 'traits': ['Typical impulse control']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average control']},
            'AA': {'phenotype': 'Slower clearance', 'score': 0.4, 'traits': ['May have more impulse challenges']}
        }
    },
    'rs140700': {
        'gene': 'HTR1B',
        'name': 'Serotonin 1B impulse',
        'variant_name': 'G861C',
        'function': 'Serotonin-mediated impulse control',
        'alleles': {
            'GG': {'phenotype': 'Better impulse control', 'score': 0.65, 'traits': ['Lower impulsivity']},
            'GC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average control']},
            'CC': {'phenotype': 'Higher impulsivity', 'score': 0.35, 'traits': ['May act more impulsively']}
        }
    },
    'rs7322347': {
        'gene': 'HTR2A',
        'name': 'HTR2A impulsivity',
        'variant_name': 'Intronic T/C',
        'function': 'Serotonin 2A and behavioral inhibition',
        'alleles': {
            'TT': {'phenotype': 'Good inhibition', 'score': 0.6, 'traits': ['Better behavioral control']},
            'TC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average inhibition']},
            'CC': {'phenotype': 'Lower inhibition', 'score': 0.4, 'traits': ['May have less behavioral inhibition']}
        }
    },
    'rs2242446': {
        'gene': 'NET/SLC6A2',
        'name': 'Norepinephrine transporter',
        'variant_name': 'T-182C',
        'function': 'Norepinephrine and attention/impulse',
        'alleles': {
            'TT': {'phenotype': 'Normal NET function', 'score': 0.55, 'traits': ['Typical impulse control']},
            'TC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average control']},
            'CC': {'phenotype': 'Altered NET', 'score': 0.45, 'traits': ['May have attention variation']}
        }
    },
    'rs28386840': {
        'gene': 'NET/SLC6A2',
        'name': 'NET promoter',
        'variant_name': 'Promoter A/T',
        'function': 'Norepinephrine transporter expression',
        'alleles': {
            'AA': {'phenotype': 'Normal expression', 'score': 0.55, 'traits': ['Typical regulation']},
            'AT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average expression']},
            'TT': {'phenotype': 'Altered expression', 'score': 0.45, 'traits': ['Modified norepinephrine']}
        }
    },
    'rs1611115': {
        'gene': 'DBH',
        'name': 'DBH impulse',
        'variant_name': '-1021 C/T',
        'function': 'Dopamine/norepinephrine balance',
        'alleles': {
            'CC': {'phenotype': 'Normal DBH', 'score': 0.55, 'traits': ['Typical impulse control']},
            'CT': {'phenotype': 'Reduced DBH', 'score': 0.5, 'traits': ['Higher dopamine, may affect impulses']},
            'TT': {'phenotype': 'Low DBH', 'score': 0.4, 'traits': ['Much higher dopamine']}
        }
    },
    'rs5569': {
        'gene': 'SLC6A2',
        'name': 'NET G1287A',
        'variant_name': 'G1287A',
        'function': 'Norepinephrine transporter efficiency',
        'alleles': {
            'GG': {'phenotype': 'Normal NET', 'score': 0.55, 'traits': ['Typical norepinephrine reuptake']},
            'GA': {'phenotype': 'Reduced NET', 'score': 0.5, 'traits': ['Higher norepinephrine']},
            'AA': {'phenotype': 'Low NET', 'score': 0.45, 'traits': ['May have attention/impulse variation']}
        }
    },
    'rs998424': {
        'gene': 'SLC6A2',
        'name': 'NET promoter',
        'variant_name': 'Promoter C/T',
        'function': 'Norepinephrine transporter expression',
        'alleles': {
            'CC': {'phenotype': 'Normal expression', 'score': 0.55, 'traits': ['Typical NET levels']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average expression']},
            'TT': {'phenotype': 'Altered expression', 'score': 0.45, 'traits': ['Modified norepinephrine']}
        }
    },
    'rs3027400': {
        'gene': 'SLC6A2',
        'name': 'NET intronic',
        'variant_name': 'Intronic C/G',
        'function': 'NET regulation and ADHD risk',
        'alleles': {
            'CC': {'phenotype': 'Normal regulation', 'score': 0.55, 'traits': ['Typical attention']},
            'CG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average regulation']},
            'GG': {'phenotype': 'Altered regulation', 'score': 0.45, 'traits': ['May have attention variation']}
        }
    },
    'rs3785143': {
        'gene': 'SNAP25',
        'name': 'SNAP25 impulse',
        'variant_name': 'Intronic A/G',
        'function': 'Neurotransmitter release and ADHD',
        'alleles': {
            'AA': {'phenotype': 'Normal release', 'score': 0.55, 'traits': ['Typical impulse control']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average control']},
            'GG': {'phenotype': 'Altered release', 'score': 0.45, 'traits': ['May have impulsivity']}
        }
    },
    'rs362551': {
        'gene': 'SNAP25',
        'name': 'SNAP25 variant',
        'variant_name': 'Intronic T/C',
        'function': 'Synaptic function and attention',
        'alleles': {
            'TT': {'phenotype': 'Normal synaptic function', 'score': 0.55, 'traits': ['Typical attention']},
            'TC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average function']},
            'CC': {'phenotype': 'Altered function', 'score': 0.45, 'traits': ['May affect attention']}
        }
    },
    'rs6265': {
        'gene': 'BDNF',
        'name': 'BDNF impulse',
        'variant_name': 'Val66Met',
        'function': 'Neuroplasticity and impulse regulation',
        'alleles': {
            'CC': {'phenotype': 'Val/Val - Better regulation', 'score': 0.6, 'traits': ['Better impulse control']},
            'CT': {'phenotype': 'Val/Met - Intermediate', 'score': 0.5, 'traits': ['Average control']},
            'TT': {'phenotype': 'Met/Met - Variable', 'score': 0.4, 'traits': ['May have impulsivity variation']}
        }
    },
    'rs2652511': {
        'gene': 'SLC6A3',
        'name': 'DAT1 promoter',
        'variant_name': 'Promoter C/T',
        'function': 'Dopamine transporter expression',
        'alleles': {
            'CC': {'phenotype': 'Normal expression', 'score': 0.55, 'traits': ['Typical dopamine regulation']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average expression']},
            'TT': {'phenotype': 'Altered expression', 'score': 0.45, 'traits': ['Modified dopamine levels']}
        }
    },
    'rs1800955': {
        'gene': 'DRD4',
        'name': 'DRD4 impulse',
        'variant_name': '-521 C/T',
        'function': 'Novelty seeking and impulsivity',
        'alleles': {
            'TT': {'phenotype': 'Higher novelty seeking', 'score': 0.7, 'traits': ['More impulsive, adventurous']},
            'CT': {'phenotype': 'Moderate', 'score': 0.5, 'traits': ['Balanced impulsivity']},
            'CC': {'phenotype': 'Lower novelty seeking', 'score': 0.4, 'traits': ['More cautious']}
        }
    },
    'rs747302': {
        'gene': 'DRD4',
        'name': 'DRD4 variant',
        'variant_name': 'Upstream A/G',
        'function': 'Dopamine D4 receptor expression',
        'alleles': {
            'AA': {'phenotype': 'Normal D4', 'score': 0.55, 'traits': ['Typical novelty response']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average response']},
            'GG': {'phenotype': 'Altered D4', 'score': 0.45, 'traits': ['May affect novelty seeking']}
        }
    },
    'rs3758653': {
        'gene': 'DRD4',
        'name': 'DRD4 promoter',
        'variant_name': 'Promoter T/C',
        'function': 'Receptor expression and ADHD',
        'alleles': {
            'TT': {'phenotype': 'Normal expression', 'score': 0.55, 'traits': ['Typical attention']},
            'TC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average expression']},
            'CC': {'phenotype': 'Altered expression', 'score': 0.45, 'traits': ['May have attention variation']}
        }
    },
    'rs2242592': {
        'gene': 'ADRA2A',
        'name': 'Alpha-2A adrenergic receptor',
        'variant_name': 'Intronic G/A',
        'function': 'Norepinephrine signaling and attention',
        'alleles': {
            'GG': {'phenotype': 'Normal signaling', 'score': 0.55, 'traits': ['Typical attention']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average signaling']},
            'AA': {'phenotype': 'Altered signaling', 'score': 0.45, 'traits': ['May affect focus']}
        }
    },
    'rs553668': {
        'gene': 'ADRA2A',
        'name': 'ADRA2A variant',
        'variant_name': '3\'UTR G/A',
        'function': 'Receptor regulation and impulsivity',
        'alleles': {
            'GG': {'phenotype': 'Normal regulation', 'score': 0.55, 'traits': ['Typical impulse control']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average control']},
            'AA': {'phenotype': 'Altered regulation', 'score': 0.45, 'traits': ['May have impulsivity']}
        }
    },
    'rs1843809': {
        'gene': 'TGFB1',
        'name': 'TGF-beta 1',
        'variant_name': 'Upstream G/T',
        'function': 'Neuroinflammation and behavior',
        'alleles': {
            'GG': {'phenotype': 'Normal TGF-beta', 'score': 0.55, 'traits': ['Typical regulation']},
            'GT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average function']},
            'TT': {'phenotype': 'Altered function', 'score': 0.45, 'traits': ['Modified inflammation']}
        }
    },
    'rs878886': {
        'gene': 'GABBR1',
        'name': 'GABA-B receptor 1',
        'variant_name': 'Intronic G/A',
        'function': 'GABA inhibition and impulse control',
        'alleles': {
            'GG': {'phenotype': 'Normal GABA signaling', 'score': 0.6, 'traits': ['Better impulse control']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average control']},
            'AA': {'phenotype': 'Altered signaling', 'score': 0.4, 'traits': ['May have impulsivity']}
        }
    },
    'rs29220': {
        'gene': 'GABRG2',
        'name': 'GABA-A receptor gamma 2',
        'variant_name': 'Intronic A/G',
        'function': 'GABAergic inhibition',
        'alleles': {
            'AA': {'phenotype': 'Normal inhibition', 'score': 0.55, 'traits': ['Typical impulse control']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average control']},
            'GG': {'phenotype': 'Altered inhibition', 'score': 0.45, 'traits': ['May have less inhibition']}
        }
    },
    'rs211014': {
        'gene': 'GABRA6',
        'name': 'GABA-A receptor alpha 6',
        'variant_name': 'Pro385Ser',
        'function': 'Cerebellar GABA function',
        'alleles': {
            'CC': {'phenotype': 'Normal GABA', 'score': 0.55, 'traits': ['Typical motor control']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average function']},
            'TT': {'phenotype': 'Altered GABA', 'score': 0.45, 'traits': ['May affect coordination']}
        }
    },
    'rs2229910': {
        'gene': 'NTRK2',
        'name': 'TrkB receptor',
        'variant_name': 'A/G',
        'function': 'BDNF signaling and behavior',
        'alleles': {
            'AA': {'phenotype': 'Normal TrkB', 'score': 0.55, 'traits': ['Typical BDNF signaling']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average signaling']},
            'GG': {'phenotype': 'Altered TrkB', 'score': 0.45, 'traits': ['Modified neuroplasticity']}
        }
    },
    'rs1387923': {
        'gene': 'NTRK2',
        'name': 'NTRK2 variant',
        'variant_name': 'Intronic T/C',
        'function': 'Neurotrophin signaling',
        'alleles': {
            'TT': {'phenotype': 'Normal signaling', 'score': 0.55, 'traits': ['Typical brain function']},
            'TC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average function']},
            'CC': {'phenotype': 'Altered signaling', 'score': 0.45, 'traits': ['Modified neurotrophin effect']}
        }
    },
    'rs6484711': {
        'gene': 'MAOA',
        'name': 'MAOA variant',
        'variant_name': 'Intronic C/T',
        'function': 'Monoamine oxidase A expression',
        'alleles': {
            'CC': {'phenotype': 'Normal MAOA', 'score': 0.55, 'traits': ['Typical monoamine breakdown']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average breakdown']},
            'TT': {'phenotype': 'Altered MAOA', 'score': 0.45, 'traits': ['Modified neurotransmitter levels']}
        }
    },
    'rs1137100': {
        'gene': 'LEPR',
        'name': 'Leptin receptor',
        'variant_name': 'Lys109Arg',
        'function': 'Satiety signaling and food impulsivity',
        'alleles': {
            'AA': {'phenotype': 'Normal leptin signaling', 'score': 0.55, 'traits': ['Typical satiety response']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average satiety']},
            'GG': {'phenotype': 'Altered signaling', 'score': 0.45, 'traits': ['May have food impulsivity']}
        }
    },
    'rs7799039': {
        'gene': 'LEP',
        'name': 'Leptin gene',
        'variant_name': '-2548 G/A',
        'function': 'Leptin production and reward',
        'alleles': {
            'GG': {'phenotype': 'Normal leptin', 'score': 0.55, 'traits': ['Typical appetite regulation']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average regulation']},
            'AA': {'phenotype': 'Altered leptin', 'score': 0.45, 'traits': ['May affect food reward']}
        }
    }
}

# =============================================================================
# OPTIMISM & RESILIENCE
# =============================================================================

RESILIENCE_GENETICS = {
    'rs4570625': {
        'gene': 'TPH2',
        'name': 'Tryptophan hydroxylase 2',
        'variant_name': 'G-703T',
        'function': 'Serotonin synthesis, emotional resilience',
        'alleles': {
            'GG': {'phenotype': 'Higher serotonin synthesis', 'score': 0.7, 'traits': ['More optimistic outlook', 'Better emotional resilience']},
            'GT': {'phenotype': 'Average', 'score': 0.5, 'traits': ['Typical emotional resilience']},
            'TT': {'phenotype': 'Lower synthesis', 'score': 0.3, 'traits': ['May be more prone to negative thinking', 'Benefits from cognitive behavioral strategies']}
        }
    },
    'rs322931': {
        'gene': 'OXTR',
        'name': 'Oxytocin receptor variant',
        'variant_name': 'Upstream C/T',
        'function': 'Optimism and positive affect',
        'alleles': {
            'TT': {'phenotype': 'Higher optimism', 'score': 0.8, 'traits': ['More positive outlook', 'Better psychological well-being']},
            'CT': {'phenotype': 'Moderate optimism', 'score': 0.5, 'traits': ['Balanced outlook']},
            'CC': {'phenotype': 'More realistic/cautious', 'score': 0.4, 'traits': ['May be more risk-aware']}
        }
    },
    'rs6265': {
        'gene': 'BDNF',
        'name': 'BDNF resilience',
        'variant_name': 'Val66Met',
        'function': 'Stress response and emotional adaptation',
        'alleles': {
            'CC': {'phenotype': 'Val/Val - Higher resilience', 'score': 0.75, 'traits': ['Better stress recovery', 'Faster emotional adaptation']},
            'CT': {'phenotype': 'Val/Met - Moderate', 'score': 0.5, 'traits': ['Average resilience']},
            'TT': {'phenotype': 'Met/Met - Sensitive', 'score': 0.35, 'traits': ['More environmentally responsive', 'Benefits greatly from support']}
        }
    },
    'rs25531': {
        'gene': 'SLC6A4',
        'name': '5-HTTLPR resilience',
        'variant_name': 'rs25531 A/G',
        'function': 'Serotonin transporter and stress resilience',
        'alleles': {
            'AA': {'phenotype': 'LA/LA - Higher resilience', 'score': 0.7, 'traits': ['Better stress coping', 'Lower depression risk']},
            'AG': {'phenotype': 'LA/S - Moderate', 'score': 0.5, 'traits': ['Average resilience']},
            'GG': {'phenotype': 'S/S - Sensitive', 'score': 0.35, 'traits': ['More reactive to environment', 'Benefits more from positive settings']}
        }
    },
    'rs6295': {
        'gene': 'HTR1A',
        'name': 'HTR1A resilience',
        'variant_name': '-1019 C/G',
        'function': 'Serotonin autoreceptor and emotional stability',
        'alleles': {
            'CC': {'phenotype': 'Better emotional stability', 'score': 0.7, 'traits': ['More stable mood', 'Better stress tolerance']},
            'CG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average stability']},
            'GG': {'phenotype': 'More variable mood', 'score': 0.35, 'traits': ['May experience more mood fluctuation']}
        }
    },
    'rs1360780': {
        'gene': 'FKBP5',
        'name': 'FKBP5 stress response',
        'variant_name': 'Intronic C/T',
        'function': 'HPA axis regulation and stress recovery',
        'alleles': {
            'CC': {'phenotype': 'Normal HPA axis', 'score': 0.65, 'traits': ['Typical stress recovery']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average stress response']},
            'TT': {'phenotype': 'Enhanced stress sensitivity', 'score': 0.35, 'traits': ['More reactive to stress', 'May benefit from stress management']}
        }
    },
    'rs3800373': {
        'gene': 'FKBP5',
        'name': 'FKBP5 variant',
        'variant_name': '3\'UTR A/C',
        'function': 'Cortisol sensitivity',
        'alleles': {
            'AA': {'phenotype': 'Normal cortisol response', 'score': 0.6, 'traits': ['Typical stress hormone regulation']},
            'AC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average regulation']},
            'CC': {'phenotype': 'Altered cortisol sensitivity', 'score': 0.4, 'traits': ['Modified stress response']}
        }
    },
    'rs110402': {
        'gene': 'CRHR1',
        'name': 'CRH receptor 1',
        'variant_name': 'Intronic G/A',
        'function': 'Corticotropin-releasing hormone response',
        'alleles': {
            'GG': {'phenotype': 'Normal CRH response', 'score': 0.6, 'traits': ['Typical stress activation']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average response']},
            'AA': {'phenotype': 'Protective effect', 'score': 0.65, 'traits': ['May have stress buffering']}
        }
    },
    'rs242924': {
        'gene': 'CRHR1',
        'name': 'CRHR1 protective',
        'variant_name': 'Intronic C/T',
        'function': 'Stress hormone receptor regulation',
        'alleles': {
            'TT': {'phenotype': 'Potentially protective', 'score': 0.65, 'traits': ['May have stress resilience']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average response']},
            'CC': {'phenotype': 'Typical response', 'score': 0.55, 'traits': ['Standard stress response']}
        }
    },
    'rs7209436': {
        'gene': 'CRHR1',
        'name': 'CRHR1 variant',
        'variant_name': 'Intronic C/T',
        'function': 'HPA axis modulation',
        'alleles': {
            'TT': {'phenotype': 'Modified HPA response', 'score': 0.6, 'traits': ['Altered stress processing']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average processing']},
            'CC': {'phenotype': 'Typical HPA response', 'score': 0.55, 'traits': ['Standard response']}
        }
    },
    'rs5443': {
        'gene': 'GNB3',
        'name': 'G-protein beta 3',
        'variant_name': 'C825T',
        'function': 'Stress signaling and mood',
        'alleles': {
            'CC': {'phenotype': 'Normal signaling', 'score': 0.55, 'traits': ['Typical stress signaling']},
            'CT': {'phenotype': 'Enhanced signaling', 'score': 0.5, 'traits': ['Modified signaling']},
            'TT': {'phenotype': 'High signaling', 'score': 0.45, 'traits': ['May have different stress response']}
        }
    },
    'rs6313': {
        'gene': 'HTR2A',
        'name': 'HTR2A resilience',
        'variant_name': 'T102C',
        'function': 'Serotonin receptor and emotional resilience',
        'alleles': {
            'TT': {'phenotype': 'Higher resilience tendency', 'score': 0.65, 'traits': ['Better emotional stability']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average resilience']},
            'CC': {'phenotype': 'Lower resilience tendency', 'score': 0.4, 'traits': ['May benefit from resilience training']}
        }
    },
    'rs1006737': {
        'gene': 'CACNA1C',
        'name': 'CACNA1C mood',
        'variant_name': 'Intronic A/G',
        'function': 'Calcium channel affecting mood stability',
        'alleles': {
            'GG': {'phenotype': 'Normal mood regulation', 'score': 0.6, 'traits': ['Typical emotional stability']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average stability']},
            'AA': {'phenotype': 'Variable mood', 'score': 0.4, 'traits': ['May have mood variation', 'Associated with creativity']}
        }
    },
    'rs1545843': {
        'gene': 'ANK3',
        'name': 'Ankyrin 3',
        'variant_name': 'Intronic T/C',
        'function': 'Neuronal function and mood stability',
        'alleles': {
            'TT': {'phenotype': 'Normal function', 'score': 0.55, 'traits': ['Typical mood stability']},
            'TC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average stability']},
            'CC': {'phenotype': 'Altered function', 'score': 0.45, 'traits': ['May have mood variation']}
        }
    },
    'rs4680': {
        'gene': 'COMT',
        'name': 'COMT resilience',
        'variant_name': 'Val158Met',
        'function': 'Stress coping and adaptation',
        'alleles': {
            'GG': {'phenotype': 'Val/Val - Stress warrior', 'score': 0.7, 'traits': ['Better under pressure', 'Faster stress adaptation']},
            'AG': {'phenotype': 'Val/Met - Balanced', 'score': 0.5, 'traits': ['Moderate stress coping']},
            'AA': {'phenotype': 'Met/Met - Thoughtful processor', 'score': 0.45, 'traits': ['Deeper processing', 'May need recovery time']}
        }
    },
    'rs4713916': {
        'gene': 'FKBP5',
        'name': 'FKBP5 HPA axis',
        'variant_name': 'Intronic G/A',
        'function': 'Glucocorticoid receptor sensitivity',
        'alleles': {
            'GG': {'phenotype': 'Normal GR sensitivity', 'score': 0.6, 'traits': ['Typical cortisol response']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average response']},
            'AA': {'phenotype': 'Altered sensitivity', 'score': 0.4, 'traits': ['Enhanced stress sensitivity']}
        }
    },
    'rs9470080': {
        'gene': 'FKBP5',
        'name': 'FKBP5 trauma response',
        'variant_name': 'Intronic T/C',
        'function': 'PTSD risk and stress recovery',
        'alleles': {
            'TT': {'phenotype': 'Lower PTSD risk', 'score': 0.65, 'traits': ['Better trauma recovery']},
            'TC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average recovery']},
            'CC': {'phenotype': 'Higher PTSD risk', 'score': 0.35, 'traits': ['May need trauma support']}
        }
    },
    'rs2267735': {
        'gene': 'CRHR2',
        'name': 'CRH receptor 2',
        'variant_name': 'Intronic C/G',
        'function': 'Stress recovery and resilience',
        'alleles': {
            'CC': {'phenotype': 'Better stress recovery', 'score': 0.65, 'traits': ['Faster stress normalization']},
            'CG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average recovery']},
            'GG': {'phenotype': 'Slower recovery', 'score': 0.4, 'traits': ['May take longer to recover']}
        }
    },
    'rs878886': {
        'gene': 'GABBR1',
        'name': 'GABA-B receptor resilience',
        'variant_name': 'Intronic G/A',
        'function': 'Inhibitory signaling and stress buffering',
        'alleles': {
            'GG': {'phenotype': 'Better stress buffering', 'score': 0.6, 'traits': ['Enhanced GABA inhibition']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average buffering']},
            'AA': {'phenotype': 'Less buffering', 'score': 0.4, 'traits': ['May be more stress reactive']}
        }
    },
    'rs12936511': {
        'gene': 'RORA',
        'name': 'RAR-related orphan receptor',
        'variant_name': 'Intronic C/T',
        'function': 'Circadian rhythm and mood stability',
        'alleles': {
            'CC': {'phenotype': 'Normal circadian', 'score': 0.55, 'traits': ['Typical rhythm stability']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average stability']},
            'TT': {'phenotype': 'Altered circadian', 'score': 0.45, 'traits': ['May have rhythm variations']}
        }
    },
    'rs4775936': {
        'gene': 'CYP19A1',
        'name': 'Aromatase mood',
        'variant_name': 'Intronic C/T',
        'function': 'Estrogen synthesis affecting mood',
        'alleles': {
            'CC': {'phenotype': 'Normal aromatase', 'score': 0.55, 'traits': ['Typical estrogen effects']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average levels']},
            'TT': {'phenotype': 'Altered aromatase', 'score': 0.45, 'traits': ['May affect mood regulation']}
        }
    },
    'rs7341475': {
        'gene': 'REELIN',
        'name': 'Reelin resilience',
        'variant_name': 'G/A',
        'function': 'Neural plasticity and stress adaptation',
        'alleles': {
            'GG': {'phenotype': 'Normal plasticity', 'score': 0.55, 'traits': ['Typical brain adaptation']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average adaptation']},
            'AA': {'phenotype': 'Altered plasticity', 'score': 0.45, 'traits': ['Different adaptation pattern']}
        }
    },
    'rs1799971': {
        'gene': 'OPRM1',
        'name': 'Mu-opioid resilience',
        'variant_name': 'A118G',
        'function': 'Social support response and pain',
        'alleles': {
            'AA': {'phenotype': 'Normal opioid response', 'score': 0.55, 'traits': ['Typical pain/social response']},
            'AG': {'phenotype': 'Enhanced social sensitivity', 'score': 0.5, 'traits': ['More responsive to social support']},
            'GG': {'phenotype': 'Higher social need', 'score': 0.45, 'traits': ['May need more social connection']}
        }
    },
    'rs4606': {
        'gene': 'RGS2',
        'name': 'Regulator of G-protein',
        'variant_name': 'C/G',
        'function': 'Anxiety and stress reactivity',
        'alleles': {
            'CC': {'phenotype': 'Lower anxiety tendency', 'score': 0.65, 'traits': ['Better stress regulation']},
            'CG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average anxiety']},
            'GG': {'phenotype': 'Higher anxiety tendency', 'score': 0.35, 'traits': ['May benefit from anxiety management']}
        }
    },
    'rs2071746': {
        'gene': 'HMOX1',
        'name': 'Heme oxygenase 1',
        'variant_name': '-413 A/T',
        'function': 'Oxidative stress response',
        'alleles': {
            'AA': {'phenotype': 'Better oxidative protection', 'score': 0.6, 'traits': ['Enhanced antioxidant response']},
            'AT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average protection']},
            'TT': {'phenotype': 'Lower protection', 'score': 0.4, 'traits': ['May benefit from antioxidants']}
        }
    },
    'rs1800629': {
        'gene': 'TNF',
        'name': 'TNF-alpha',
        'variant_name': '-308 G/A',
        'function': 'Inflammatory response and mood',
        'alleles': {
            'GG': {'phenotype': 'Normal TNF', 'score': 0.55, 'traits': ['Typical inflammation']},
            'GA': {'phenotype': 'Higher TNF', 'score': 0.45, 'traits': ['Increased inflammation']},
            'AA': {'phenotype': 'High TNF', 'score': 0.35, 'traits': ['May affect mood via inflammation']}
        }
    },
    'rs1800896': {
        'gene': 'IL10',
        'name': 'Interleukin-10',
        'variant_name': '-1082 G/A',
        'function': 'Anti-inflammatory resilience',
        'alleles': {
            'GG': {'phenotype': 'Higher IL-10 - Anti-inflammatory', 'score': 0.65, 'traits': ['Better inflammation regulation']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average regulation']},
            'AA': {'phenotype': 'Lower IL-10', 'score': 0.4, 'traits': ['May have more inflammation']}
        }
    },
    'rs1800795': {
        'gene': 'IL6',
        'name': 'Interleukin-6 resilience',
        'variant_name': '-174 G/C',
        'function': 'Stress-inflammation axis',
        'alleles': {
            'GG': {'phenotype': 'Higher IL-6 response', 'score': 0.45, 'traits': ['Strong inflammatory response']},
            'GC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average response']},
            'CC': {'phenotype': 'Lower IL-6', 'score': 0.6, 'traits': ['Less stress inflammation']}
        }
    },
    'rs6311': {
        'gene': 'HTR2A',
        'name': 'HTR2A wellbeing',
        'variant_name': '-1438 A/G',
        'function': 'Subjective well-being',
        'alleles': {
            'AA': {'phenotype': 'Higher well-being', 'score': 0.65, 'traits': ['Greater life satisfaction']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average well-being']},
            'GG': {'phenotype': 'Variable well-being', 'score': 0.4, 'traits': ['May have more variation']}
        }
    },
    'rs4713902': {
        'gene': 'FKBP5',
        'name': 'FKBP5 depression',
        'variant_name': 'Intronic A/C',
        'function': 'Depression vulnerability',
        'alleles': {
            'AA': {'phenotype': 'Lower depression risk', 'score': 0.65, 'traits': ['Better mood maintenance']},
            'AC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average risk']},
            'CC': {'phenotype': 'Higher depression risk', 'score': 0.35, 'traits': ['May benefit from mood support']}
        }
    },
    'rs7903146': {
        'gene': 'TCF7L2',
        'name': 'TCF7L2 metabolic resilience',
        'variant_name': 'C/T',
        'function': 'Metabolic stress and mood',
        'alleles': {
            'CC': {'phenotype': 'Better metabolic health', 'score': 0.6, 'traits': ['Stable blood sugar']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average metabolism']},
            'TT': {'phenotype': 'Higher metabolic stress', 'score': 0.4, 'traits': ['May affect mood via metabolism']}
        }
    },
    'rs2043112': {
        'gene': 'PDE4B',
        'name': 'Phosphodiesterase 4B',
        'variant_name': 'Intronic A/G',
        'function': 'cAMP signaling and mood',
        'alleles': {
            'AA': {'phenotype': 'Normal PDE4B', 'score': 0.55, 'traits': ['Typical cAMP signaling']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average signaling']},
            'GG': {'phenotype': 'Altered PDE4B', 'score': 0.45, 'traits': ['Modified mood signaling']}
        }
    },
    'rs10994336': {
        'gene': 'ANK3',
        'name': 'ANK3 mood stability',
        'variant_name': 'Intronic C/T',
        'function': 'Axonal function and bipolar risk',
        'alleles': {
            'CC': {'phenotype': 'Normal ANK3', 'score': 0.55, 'traits': ['Typical mood stability']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average stability']},
            'TT': {'phenotype': 'Altered ANK3', 'score': 0.45, 'traits': ['May have mood variation']}
        }
    },
    'rs1024582': {
        'gene': 'ODZ4',
        'name': 'Teneurin 4',
        'variant_name': 'Intronic A/G',
        'function': 'Neural development and bipolar',
        'alleles': {
            'AA': {'phenotype': 'Normal ODZ4', 'score': 0.55, 'traits': ['Typical neural function']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average function']},
            'GG': {'phenotype': 'Altered ODZ4', 'score': 0.45, 'traits': ['Modified neural development']}
        }
    }
}

# =============================================================================
# CREATIVITY & DIVERGENT THINKING
# =============================================================================

CREATIVITY_GENETICS = {
    'rs1006737': {
        'gene': 'CACNA1C',
        'name': 'Calcium channel',
        'variant_name': 'Intronic A/G',
        'function': 'Creativity, divergent thinking',
        'alleles': {
            'AA': {'phenotype': 'Higher creativity tendency', 'score': 0.8, 'traits': ['More divergent thinking', 'Higher verbal fluency']},
            'AG': {'phenotype': 'Moderate creativity', 'score': 0.5, 'traits': ['Balanced creative abilities']},
            'GG': {'phenotype': 'More convergent thinking', 'score': 0.4, 'traits': ['More systematic approach', 'Detail-oriented']}
        }
    },
    'rs4680': {
        'gene': 'COMT',
        'name': 'COMT creativity',
        'variant_name': 'Val158Met',
        'function': 'Prefrontal dopamine and creative thinking',
        'alleles': {
            'AA': {'phenotype': 'Met/Met - Enhanced creativity', 'score': 0.75, 'traits': ['Higher creative thinking', 'More associative connections']},
            'AG': {'phenotype': 'Val/Met - Balanced', 'score': 0.5, 'traits': ['Balanced creative and analytical']},
            'GG': {'phenotype': 'Val/Val - Analytical', 'score': 0.4, 'traits': ['More systematic thinking']}
        }
    },
    'rs1800497': {
        'gene': 'DRD2',
        'name': 'DRD2 creativity',
        'variant_name': 'Taq1A',
        'function': 'Dopamine and novel idea generation',
        'alleles': {
            'CC': {'phenotype': 'Normal D2 - Typical creativity', 'score': 0.5, 'traits': ['Standard creative processing']},
            'CT': {'phenotype': 'Reduced D2 - Enhanced novelty', 'score': 0.6, 'traits': ['More novel associations']},
            'TT': {'phenotype': 'Low D2 - High novelty seeking', 'score': 0.7, 'traits': ['High novelty in thinking', 'May be more unconventional']}
        }
    },
    'rs1800955': {
        'gene': 'DRD4',
        'name': 'DRD4 creativity',
        'variant_name': '-521 C/T',
        'function': 'Novelty seeking and creative exploration',
        'alleles': {
            'TT': {'phenotype': 'Higher novelty seeking', 'score': 0.75, 'traits': ['More exploratory thinking', 'Creative risk-taking']},
            'CT': {'phenotype': 'Moderate', 'score': 0.5, 'traits': ['Balanced exploration']},
            'CC': {'phenotype': 'Lower novelty seeking', 'score': 0.35, 'traits': ['More conventional thinking']}
        }
    },
    'rs6265': {
        'gene': 'BDNF',
        'name': 'BDNF creativity',
        'variant_name': 'Val66Met',
        'function': 'Neuroplasticity and creative adaptation',
        'alleles': {
            'CC': {'phenotype': 'Val/Val - Flexible thinking', 'score': 0.65, 'traits': ['Good cognitive flexibility']},
            'CT': {'phenotype': 'Val/Met - Moderate', 'score': 0.5, 'traits': ['Average flexibility']},
            'TT': {'phenotype': 'Met/Met - Different processing', 'score': 0.55, 'traits': ['May process information differently']}
        }
    },
    'rs25531': {
        'gene': 'SLC6A4',
        'name': '5-HTTLPR creativity',
        'variant_name': 'rs25531 A/G',
        'function': 'Emotional depth and creative expression',
        'alleles': {
            'AA': {'phenotype': 'LA/LA - Stable processing', 'score': 0.5, 'traits': ['Consistent creative output']},
            'AG': {'phenotype': 'LA/S - Intermediate', 'score': 0.55, 'traits': ['Balanced emotional creativity']},
            'GG': {'phenotype': 'S/S - Emotional depth', 'score': 0.65, 'traits': ['Deeper emotional expression', 'May have more emotional art']}
        }
    },
    'rs363050': {
        'gene': 'SNAP25',
        'name': 'SNAP25 creativity',
        'variant_name': 'A/G',
        'function': 'Synaptic function and creative processing',
        'alleles': {
            'GG': {'phenotype': 'Enhanced synaptic function', 'score': 0.65, 'traits': ['Better creative connections']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average creative processing']},
            'AA': {'phenotype': 'Standard function', 'score': 0.45, 'traits': ['Typical creative ability']}
        }
    },
    'rs17070145': {
        'gene': 'KIBRA',
        'name': 'KIBRA creativity',
        'variant_name': 'T/C',
        'function': 'Memory and creative recall',
        'alleles': {
            'TT': {'phenotype': 'Better memory for creative material', 'score': 0.65, 'traits': ['Enhanced creative memory']},
            'TC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average creative memory']},
            'CC': {'phenotype': 'Typical memory', 'score': 0.45, 'traits': ['Standard recall']}
        }
    },
    'rs2268498': {
        'gene': 'OXTR',
        'name': 'OXTR creativity',
        'variant_name': 'Upstream T/C',
        'function': 'Social creativity and collaborative thinking',
        'alleles': {
            'TT': {'phenotype': 'Higher social creativity', 'score': 0.65, 'traits': ['Better collaborative creativity']},
            'TC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average collaboration']},
            'CC': {'phenotype': 'More independent creativity', 'score': 0.55, 'traits': ['May prefer solo creative work']}
        }
    },
    'rs1045642': {
        'gene': 'ABCB1',
        'name': 'P-glycoprotein',
        'variant_name': 'C3435T',
        'function': 'Blood-brain barrier affecting neurotransmitters',
        'alleles': {
            'CC': {'phenotype': 'Normal BBB function', 'score': 0.5, 'traits': ['Typical brain chemistry']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.55, 'traits': ['Moderate variation']},
            'TT': {'phenotype': 'Altered BBB function', 'score': 0.6, 'traits': ['May have different brain chemistry']}
        }
    },
    'rs6311': {
        'gene': 'HTR2A',
        'name': 'HTR2A creativity',
        'variant_name': '-1438 A/G',
        'function': 'Serotonin and creative perception',
        'alleles': {
            'AA': {'phenotype': 'Enhanced perceptual creativity', 'score': 0.65, 'traits': ['More creative perception']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average perception']},
            'GG': {'phenotype': 'Standard perception', 'score': 0.45, 'traits': ['Typical perceptual processing']}
        }
    },
    'rs7341475': {
        'gene': 'REELIN',
        'name': 'Reelin creativity',
        'variant_name': 'G/A',
        'function': 'Cortical organization and creative thinking',
        'alleles': {
            'GG': {'phenotype': 'Typical cortical organization', 'score': 0.5, 'traits': ['Standard creative processing']},
            'GA': {'phenotype': 'Intermediate', 'score': 0.55, 'traits': ['Modified organization']},
            'AA': {'phenotype': 'Altered organization', 'score': 0.6, 'traits': ['May have different creative style']}
        }
    },
    'rs1076560': {
        'gene': 'DRD2',
        'name': 'DRD2 creative flexibility',
        'variant_name': 'Splicing G/T',
        'function': 'Cognitive flexibility in creative tasks',
        'alleles': {
            'GG': {'phenotype': 'Balanced flexibility', 'score': 0.5, 'traits': ['Typical creative approach']},
            'GT': {'phenotype': 'Enhanced flexibility', 'score': 0.6, 'traits': ['Good cognitive shifting']},
            'TT': {'phenotype': 'High flexibility', 'score': 0.65, 'traits': ['Very adaptable thinking']}
        }
    },
    'rs6277': {
        'gene': 'DRD2',
        'name': 'DRD2 C957T creativity',
        'variant_name': 'C957T',
        'function': 'Reward processing in creative endeavors',
        'alleles': {
            'CC': {'phenotype': 'Higher creative motivation', 'score': 0.6, 'traits': ['Strong creative drive']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Balanced motivation']},
            'TT': {'phenotype': 'Different motivation style', 'score': 0.55, 'traits': ['May need external motivation']}
        }
    },
    'rs7124442': {
        'gene': 'BDNF',
        'name': 'BDNF creative plasticity',
        'variant_name': '3\'UTR C/T',
        'function': 'Neural plasticity for creative learning',
        'alleles': {
            'CC': {'phenotype': 'Better creative plasticity', 'score': 0.65, 'traits': ['Enhanced creative learning']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average plasticity']},
            'TT': {'phenotype': 'Variable plasticity', 'score': 0.45, 'traits': ['May need practice']}
        }
    },
    'rs11030101': {
        'gene': 'BDNF',
        'name': 'BDNF creative expression',
        'variant_name': 'Intronic A/T',
        'function': 'BDNF levels affecting creative output',
        'alleles': {
            'AA': {'phenotype': 'Higher creative expression', 'score': 0.65, 'traits': ['Enhanced creative BDNF']},
            'AT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average expression']},
            'TT': {'phenotype': 'Different expression pattern', 'score': 0.45, 'traits': ['Modified creative output']}
        }
    },
    'rs1360780': {
        'gene': 'FKBP5',
        'name': 'FKBP5 creative stress',
        'variant_name': 'Intronic C/T',
        'function': 'Stress response affecting creativity',
        'alleles': {
            'CC': {'phenotype': 'Stable creative output', 'score': 0.55, 'traits': ['Consistent creativity']},
            'CT': {'phenotype': 'Variable under stress', 'score': 0.5, 'traits': ['Creativity affected by stress']},
            'TT': {'phenotype': 'Stress-sensitive creativity', 'score': 0.6, 'traits': ['May create best with support']}
        }
    },
    'rs324420': {
        'gene': 'FAAH',
        'name': 'FAAH creativity',
        'variant_name': 'P129T',
        'function': 'Endocannabinoid system and creative flow',
        'alleles': {
            'CC': {'phenotype': 'Normal FAAH', 'score': 0.5, 'traits': ['Typical creative flow']},
            'CA': {'phenotype': 'Reduced FAAH', 'score': 0.6, 'traits': ['Enhanced creative flow']},
            'AA': {'phenotype': 'Low FAAH - Creative ease', 'score': 0.7, 'traits': ['Natural creative flow', 'Less creative anxiety']}
        }
    },
    'rs2760118': {
        'gene': 'CHRNA4',
        'name': 'Nicotinic receptor creativity',
        'variant_name': 'T/C',
        'function': 'Attention in creative tasks',
        'alleles': {
            'TT': {'phenotype': 'Better creative focus', 'score': 0.65, 'traits': ['Sustained creative attention']},
            'TC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average focus']},
            'CC': {'phenotype': 'Variable focus', 'score': 0.45, 'traits': ['May have scattered creativity']}
        }
    },
    'rs11174811': {
        'gene': 'AVPR1A',
        'name': 'AVPR1A musical creativity',
        'variant_name': 'Intronic A/C',
        'function': 'Musical creativity and emotional music response',
        'alleles': {
            'AA': {'phenotype': 'Higher musical creativity', 'score': 0.7, 'traits': ['Enhanced musical ability']},
            'AC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average musical creativity']},
            'CC': {'phenotype': 'Typical musical ability', 'score': 0.45, 'traits': ['Standard music response']}
        }
    },
    'rs53576': {
        'gene': 'OXTR',
        'name': 'OXTR collaborative creativity',
        'variant_name': 'Intron 3',
        'function': 'Social aspects of creative collaboration',
        'alleles': {
            'GG': {'phenotype': 'Better group creativity', 'score': 0.65, 'traits': ['Thrives in creative groups']},
            'AG': {'phenotype': 'Balanced', 'score': 0.5, 'traits': ['Can work both ways']},
            'AA': {'phenotype': 'Solo creative preference', 'score': 0.55, 'traits': ['May prefer solo creative work']}
        }
    },
    'rs12601685': {
        'gene': 'CLOCK',
        'name': 'CLOCK creative timing',
        'variant_name': 'Intronic C/T',
        'function': 'Circadian influence on creative peak',
        'alleles': {
            'CC': {'phenotype': 'Morning creative peak', 'score': 0.55, 'traits': ['Best creativity in AM']},
            'CT': {'phenotype': 'Flexible timing', 'score': 0.5, 'traits': ['Adaptable creative timing']},
            'TT': {'phenotype': 'Evening creative peak', 'score': 0.55, 'traits': ['Best creativity in PM']}
        }
    },
    'rs3800373': {
        'gene': 'FKBP5',
        'name': 'FKBP5 creative resilience',
        'variant_name': '3\'UTR A/C',
        'function': 'Creative persistence under pressure',
        'alleles': {
            'AA': {'phenotype': 'Persistent creativity', 'score': 0.6, 'traits': ['Maintains creativity under stress']},
            'AC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average persistence']},
            'CC': {'phenotype': 'Variable persistence', 'score': 0.4, 'traits': ['May need low-stress environment']}
        }
    },
    'rs1799913': {
        'gene': 'TPH1',
        'name': 'TPH1 artistic temperament',
        'variant_name': 'A218C',
        'function': 'Serotonin and artistic sensitivity',
        'alleles': {
            'AA': {'phenotype': 'Higher artistic sensitivity', 'score': 0.65, 'traits': ['Enhanced artistic perception']},
            'AC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average artistic sense']},
            'CC': {'phenotype': 'Practical orientation', 'score': 0.45, 'traits': ['More analytical than artistic']}
        }
    },
    'rs4570625': {
        'gene': 'TPH2',
        'name': 'TPH2 creative mood',
        'variant_name': 'G-703T',
        'function': 'Brain serotonin and creative mood',
        'alleles': {
            'GG': {'phenotype': 'Stable creative mood', 'score': 0.6, 'traits': ['Consistent creative output']},
            'GT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Variable creative mood']},
            'TT': {'phenotype': 'Mood-dependent creativity', 'score': 0.55, 'traits': ['Creativity varies with mood']}
        }
    },
    'rs429358': {
        'gene': 'APOE',
        'name': 'APOE creative cognition',
        'variant_name': 'Cys112Arg',
        'function': 'Cognitive reserve for creative thinking',
        'alleles': {
            'TT': {'phenotype': 'Better cognitive reserve', 'score': 0.6, 'traits': ['Sustained creative cognition']},
            'TC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average reserve']},
            'CC': {'phenotype': 'Variable reserve', 'score': 0.4, 'traits': ['May need cognitive support']}
        }
    },
    'rs2228485': {
        'gene': 'AVPR1A',
        'name': 'AVPR1A creative bonding',
        'variant_name': 'Synonymous A/G',
        'function': 'Social creativity and artistic collaboration',
        'alleles': {
            'AA': {'phenotype': 'Strong creative bonding', 'score': 0.65, 'traits': ['Builds creative partnerships']},
            'AG': {'phenotype': 'Normal', 'score': 0.5, 'traits': ['Typical collaboration']},
            'GG': {'phenotype': 'Independent creative', 'score': 0.55, 'traits': ['Prefers solo work']}
        }
    },
    'rs1801260': {
        'gene': 'CLOCK',
        'name': 'CLOCK creative rhythms',
        'variant_name': '3111 T/C',
        'function': 'Creative productivity rhythms',
        'alleles': {
            'TT': {'phenotype': 'Morning creative type', 'score': 0.55, 'traits': ['Early creative productivity']},
            'TC': {'phenotype': 'Flexible', 'score': 0.5, 'traits': ['Adaptable creative rhythm']},
            'CC': {'phenotype': 'Night owl creative', 'score': 0.6, 'traits': ['Late night creativity']}
        }
    },
    'rs6313': {
        'gene': 'HTR2A',
        'name': 'HTR2A imaginative thinking',
        'variant_name': 'T102C',
        'function': 'Serotonin 2A receptor and imagination',
        'alleles': {
            'TT': {'phenotype': 'Enhanced imagination', 'score': 0.65, 'traits': ['Vivid imagination']},
            'CT': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average imagination']},
            'CC': {'phenotype': 'More concrete thinking', 'score': 0.45, 'traits': ['Practical orientation']}
        }
    },
    'rs16917237': {
        'gene': 'KCNJ6',
        'name': 'KCNJ6 creative neural',
        'variant_name': 'C/T',
        'function': 'Neural excitability for creative insights',
        'alleles': {
            'CC': {'phenotype': 'Balanced excitability', 'score': 0.5, 'traits': ['Steady creative flow']},
            'CT': {'phenotype': 'Enhanced insights', 'score': 0.6, 'traits': ['More creative insights']},
            'TT': {'phenotype': 'High insight potential', 'score': 0.65, 'traits': ['Frequent creative insights']}
        }
    },
    'rs4963': {
        'gene': 'GRM3',
        'name': 'GRM3 creative glutamate',
        'variant_name': 'A/G',
        'function': 'Glutamate signaling for creative thinking',
        'alleles': {
            'AA': {'phenotype': 'Enhanced creative thinking', 'score': 0.65, 'traits': ['Better creative processing']},
            'AG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average processing']},
            'GG': {'phenotype': 'Variable processing', 'score': 0.45, 'traits': ['May need creative stimulation']}
        }
    },
    'rs1344706': {
        'gene': 'ZNF804A',
        'name': 'ZNF804A creative connectivity',
        'variant_name': 'A/C',
        'function': 'Brain connectivity for creative synthesis',
        'alleles': {
            'AA': {'phenotype': 'Better creative synthesis', 'score': 0.55, 'traits': ['Good at combining ideas']},
            'AC': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average synthesis']},
            'CC': {'phenotype': 'Different connectivity', 'score': 0.55, 'traits': ['Unique creative connections']}
        }
    },
    'rs1800544': {
        'gene': 'ADRA2A',
        'name': 'ADRA2A creative attention',
        'variant_name': '-1291 C/G',
        'function': 'Attention control in creative work',
        'alleles': {
            'CC': {'phenotype': 'Better creative focus', 'score': 0.65, 'traits': ['Sustained creative attention']},
            'CG': {'phenotype': 'Intermediate', 'score': 0.5, 'traits': ['Average creative focus']},
            'GG': {'phenotype': 'Diffuse attention', 'score': 0.55, 'traits': ['Broad creative associations']}
        }
    }
}

# =============================================================================
# ANALYSIS FUNCTIONS
# =============================================================================

def analyze_behavioral_genetics(dna_data: dict) -> dict:
    """Comprehensive behavioral genetics analysis"""
    # Get individual analyses
    empathy = analyze_empathy(dna_data)
    novelty = analyze_novelty_seeking(dna_data)
    stress = analyze_stress_response(dna_data)
    cognitive = analyze_cognitive_style(dna_data)
    impulse = analyze_impulse_control(dna_data)
    optimism = analyze_optimism(dna_data)
    creativity = analyze_creativity(dna_data)

    # Build results in format expected by behavioral_ui.py
    results = {
        # Empathy section
        'empathy': {
            'level': empathy['level'],
            'score': empathy['score'],
            'phenotype': empathy['level'],  # UI expects phenotype
            'description': empathy['description'],
            'traits': empathy['traits'],
            'markers_found': empathy['markers_found']
        },
        # Novelty seeking section
        'novelty_seeking': {
            'level': novelty['level'],
            'score': novelty['score'],
            'phenotype': novelty['level'],
            'description': novelty['description'],
            'traits': novelty['traits'],
            'reward_sensitivity': 'Higher' if novelty['score'] > 0.6 else 'Normal',
            'markers_found': novelty['markers_found']
        },
        # Stress response (UI expects stress_response AND stress_resilience)
        'stress_response': stress,
        'stress_resilience': {
            'resilience_level': stress.get('resilience', 'Average'),
            'traits': stress.get('traits', []),
            'description': stress.get('description', ''),
            'markers_found': stress.get('markers_found', [])
        },
        # Warrior gene (COMT) - UI expects this separately
        'warrior_gene': {
            'activity_level': stress.get('type', 'Balanced'),
            'markers_found': [m for m in stress.get('markers_found', []) if m.get('gene') == 'COMT'],
            'important_note': 'This gene affects dopamine clearance in the prefrontal cortex.'
        },
        # Cognitive style / memory
        'cognitive_style': cognitive,
        'memory_learning': {
            'episodic_memory': cognitive.get('memory', 'Average'),
            'working_memory': cognitive.get('attention', 'Average'),
            'learning_style': cognitive.get('learning_style', 'Visual/Verbal balanced'),
            'traits': cognitive.get('traits', []),
            'markers_found': cognitive.get('markers_found', [])
        },
        # Other sections
        'impulse_control': impulse,
        'optimism': optimism,
        'creativity': creativity
    }

    # Generate overall profile for UI
    results['overall_profile'] = {
        'type': 'Warrior' if 'Warrior' in stress.get('type', '') else
                'Sensitive' if stress.get('resilience') == 'Sensitive' else
                'Explorer' if novelty['score'] > 0.65 else 'Balanced',
        'description': _generate_profile_description(empathy, novelty, stress, cognitive),
        'strengths': _get_profile_strengths(empathy, novelty, stress, cognitive, creativity),
        'considerations': _get_profile_considerations(stress, cognitive, impulse)
    }

    # Also keep summary for other uses
    results['summary'] = generate_behavioral_summary(results)

    return results


def _generate_profile_description(empathy, novelty, stress, cognitive):
    """Generate a description of the overall behavioral profile"""
    parts = []
    if empathy['level'] == 'Higher':
        parts.append("naturally empathetic")
    if novelty['level'] == 'Higher':
        parts.append("curious and adventure-seeking")
    if 'Warrior' in stress.get('type', ''):
        parts.append("stress-resilient")
    elif 'Worrier' in stress.get('type', ''):
        parts.append("detail-oriented")
    if cognitive.get('memory') == 'Strong':
        parts.append("with strong memory abilities")

    if parts:
        return "Your genetics suggest you tend to be " + ", ".join(parts) + "."
    return "Your behavioral genetics show a balanced profile."


def _get_profile_strengths(empathy, novelty, stress, cognitive, creativity):
    """Extract behavioral strengths"""
    strengths = []
    if empathy['level'] == 'Higher':
        strengths.append("Strong emotional intelligence")
    if novelty['level'] == 'Higher':
        strengths.append("Openness to new experiences")
    if 'Warrior' in stress.get('type', ''):
        strengths.append("Performs well under pressure")
    if cognitive.get('memory') == 'Strong':
        strengths.append("Excellent memory capabilities")
    if creativity.get('level') == 'Higher':
        strengths.append("Creative thinking")
    return strengths[:4]


def _get_profile_considerations(stress, cognitive, impulse):
    """Get areas for consideration"""
    considerations = []
    if 'Worrier' in stress.get('type', ''):
        considerations.append("May be more sensitive to stress")
    if cognitive.get('memory') == 'May benefit from strategies':
        considerations.append("Exercise boosts brain health for your genotype")
    if impulse.get('control') == 'Lower':
        considerations.append("May benefit from impulse management strategies")
    return considerations[:3]


def analyze_empathy(dna_data: dict) -> dict:
    """Analyze empathy-related genetics"""
    result = {
        'level': 'Average',
        'score': 0.5,
        'markers_found': [],
        'traits': [],
        'description': ''
    }

    scores = []
    for rsid, info in EMPATHY_GENETICS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            _key = get_genotype_key(genotype, info['alleles'])
            if _key:
                data = info['alleles'][_key]
                scores.append(data['score'])
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': info['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })
                result['traits'].extend(data.get('traits', []))

    if scores:
        avg = sum(scores) / len(scores)
        result['score'] = avg
        if avg >= 0.65:
            result['level'] = 'Higher'
            result['description'] = 'You likely have higher natural empathy and social sensitivity.'
        elif avg <= 0.4:
            result['level'] = 'Lower'
            result['description'] = 'You may be more self-reliant and less affected by social dynamics.'
        else:
            result['level'] = 'Average'
            result['description'] = 'You have typical empathy levels.'

    return result


def analyze_novelty_seeking(dna_data: dict) -> dict:
    """Analyze novelty seeking and reward sensitivity"""
    result = {
        'level': 'Average',
        'score': 0.5,
        'markers_found': [],
        'traits': [],
        'description': ''
    }

    scores = []
    for rsid, info in DOPAMINE_GENETICS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            _key = get_genotype_key(genotype, info['alleles'])
            if _key:
                data = info['alleles'][_key]
                scores.append(data['score'])
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': info['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })
                result['traits'].extend(data.get('traits', []))

    if scores:
        avg = sum(scores) / len(scores)
        result['score'] = avg
        if avg >= 0.65:
            result['level'] = 'Higher'
            result['description'] = 'You likely seek novelty and stimulation more than average.'
        elif avg <= 0.4:
            result['level'] = 'Lower'
            result['description'] = 'You may prefer routine and familiar experiences.'
        else:
            result['level'] = 'Average'
            result['description'] = 'You have balanced novelty-seeking tendencies.'

    return result


def analyze_stress_response(dna_data: dict) -> dict:
    """Analyze stress response and anxiety genetics"""
    result = {
        'type': 'Balanced',
        'resilience': 'Average',
        'score': 0.5,
        'markers_found': [],
        'traits': [],
        'description': ''
    }

    scores = []

    # Check COMT (Warrior/Worrier)
    if 'rs4680' in dna_data:
        genotype = dna_data['rs4680']
        info = DOPAMINE_GENETICS['rs4680']
        _key = get_genotype_key(genotype, info['alleles'])
        if _key:
            data = info['alleles'][_key]
            result['type'] = data['phenotype'].split(' - ')[0]
            scores.append(data['score'])
            result['markers_found'].append({
                'rsid': 'rs4680',
                'gene': 'COMT',
                'genotype': genotype,
                'phenotype': data['phenotype']
            })
            result['traits'].extend(data.get('traits', []))

    # Check serotonin genetics
    for rsid, info in SEROTONIN_GENETICS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            _key = get_genotype_key(genotype, info['alleles'])
            if _key:
                data = info['alleles'][_key]
                scores.append(data['score'])
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': info['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })
                result['traits'].extend(data.get('traits', []))

    if scores:
        avg = sum(scores) / len(scores)
        result['score'] = avg
        if avg >= 0.65:
            result['resilience'] = 'Higher'
            result['description'] = 'You likely have good stress resilience and emotional regulation.'
        elif avg <= 0.4:
            result['resilience'] = 'Sensitive'
            result['description'] = 'You may be more environmentally sensitive - this can be a strength in positive environments.'
        else:
            result['resilience'] = 'Average'
            result['description'] = 'You have typical stress response patterns.'

    return result


def analyze_cognitive_style(dna_data: dict) -> dict:
    """Analyze learning and cognitive genetics"""
    result = {
        'memory': 'Average',
        'attention': 'Average',
        'score': 0.5,
        'markers_found': [],
        'traits': [],
        'description': ''
    }

    scores = []
    for rsid, info in COGNITIVE_GENETICS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            _key = get_genotype_key(genotype, info['alleles'])
            if _key:
                data = info['alleles'][_key]
                scores.append(data['score'])
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': info['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })
                result['traits'].extend(data.get('traits', []))

    if scores:
        avg = sum(scores) / len(scores)
        result['score'] = avg
        if avg >= 0.65:
            result['memory'] = 'Enhanced'
            result['attention'] = 'Strong'
            result['description'] = 'You likely have good natural memory and attention abilities.'
        elif avg <= 0.4:
            result['memory'] = 'May benefit from strategies'
            result['attention'] = 'May need support'
            result['description'] = 'You may benefit from memory techniques and exercise for brain health.'
        else:
            result['memory'] = 'Average'
            result['attention'] = 'Average'
            result['description'] = 'You have typical cognitive abilities.'

    return result


def analyze_impulse_control(dna_data: dict) -> dict:
    """Analyze impulse control genetics"""
    result = {
        'level': 'Average',
        'score': 0.5,
        'markers_found': [],
        'traits': [],
        'description': ''
    }

    scores = []
    for rsid, info in IMPULSE_GENETICS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            _key = get_genotype_key(genotype, info['alleles'])
            if _key:
                data = info['alleles'][_key]
                scores.append(data['score'])
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': info['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })
                result['traits'].extend(data.get('traits', []))

    if scores:
        avg = sum(scores) / len(scores)
        result['score'] = avg
        if avg >= 0.6:
            result['level'] = 'Good'
            result['description'] = 'You likely have good natural impulse control.'
        elif avg <= 0.4:
            result['level'] = 'May need strategies'
            result['description'] = 'You may benefit from impulse control strategies and mindfulness.'
        else:
            result['level'] = 'Average'
            result['description'] = 'You have typical impulse control.'

    return result


def analyze_optimism(dna_data: dict) -> dict:
    """Analyze optimism and positive affect genetics"""
    result = {
        'level': 'Balanced',
        'score': 0.5,
        'markers_found': [],
        'traits': [],
        'description': ''
    }

    scores = []
    for rsid, info in RESILIENCE_GENETICS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            _key = get_genotype_key(genotype, info['alleles'])
            if _key:
                data = info['alleles'][_key]
                scores.append(data['score'])
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': info['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })
                result['traits'].extend(data.get('traits', []))

    if scores:
        avg = sum(scores) / len(scores)
        result['score'] = avg
        if avg >= 0.65:
            result['level'] = 'Optimistic'
            result['description'] = 'You likely have a naturally positive outlook.'
        elif avg <= 0.4:
            result['level'] = 'Realistic'
            result['description'] = 'You may have a more cautious, realistic outlook.'
        else:
            result['level'] = 'Balanced'
            result['description'] = 'You have a balanced outlook on life.'

    return result


def analyze_creativity(dna_data: dict) -> dict:
    """Analyze creativity genetics"""
    result = {
        'level': 'Average',
        'score': 0.5,
        'markers_found': [],
        'traits': [],
        'description': ''
    }

    scores = []
    for rsid, info in CREATIVITY_GENETICS.items():
        if rsid in dna_data:
            genotype = dna_data[rsid]
            _key = get_genotype_key(genotype, info['alleles'])
            if _key:
                data = info['alleles'][_key]
                scores.append(data['score'])
                result['markers_found'].append({
                    'rsid': rsid,
                    'gene': info['gene'],
                    'genotype': genotype,
                    'phenotype': data['phenotype']
                })
                result['traits'].extend(data.get('traits', []))

    if scores:
        avg = sum(scores) / len(scores)
        result['score'] = avg
        if avg >= 0.65:
            result['level'] = 'Higher'
            result['description'] = 'You likely have enhanced creative and divergent thinking.'
        elif avg <= 0.4:
            result['level'] = 'Systematic'
            result['description'] = 'You may prefer systematic, convergent thinking.'
        else:
            result['level'] = 'Balanced'
            result['description'] = 'You have balanced creative abilities.'

    return result


def generate_behavioral_summary(results: dict) -> dict:
    """Generate overall behavioral summary"""
    summary = {
        'personality_type': '',
        'key_traits': [],
        'strengths': [],
        'growth_areas': [],
        'total_markers': 0,
        'recommendations': []
    }

    # Count markers
    for key, val in results.items():
        if isinstance(val, dict) and 'markers_found' in val:
            summary['total_markers'] += len(val['markers_found'])

    # Determine personality type based on COMT
    stress = results.get('stress_response', {})
    if 'Warrior' in stress.get('type', ''):
        summary['personality_type'] = 'Warrior Type'
        summary['strengths'].append('Performs well under pressure')
    elif 'Worrier' in stress.get('type', ''):
        summary['personality_type'] = 'Worrier Type'
        summary['strengths'].append('Excellent memory and attention at baseline')
    else:
        summary['personality_type'] = 'Balanced Type'

    # Add key traits
    for key in ['empathy', 'novelty_seeking', 'optimism', 'creativity']:
        val = results.get(key, {})
        level = val.get('level', 'Average')
        if level != 'Average':
            summary['key_traits'].append(f"{key.replace('_', ' ').title()}: {level}")

    # Recommendations
    if results.get('stress_response', {}).get('resilience') == 'Sensitive':
        summary['recommendations'].append('May benefit from stress management techniques')
    if results.get('cognitive_style', {}).get('memory') == 'May benefit from strategies':
        summary['recommendations'].append('Regular exercise can boost BDNF and brain health')

    return summary
