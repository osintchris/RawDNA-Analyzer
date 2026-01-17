#!/usr/bin/env python3
"""
DNA Analysis Desktop Application
A comprehensive genetic analysis tool with modern UI
Integrates all analysis modules for complete DNA insights
"""

import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dna_parser import parse_dna_file
from comprehensive_analysis import ComprehensiveDNAAnalysisEngine

# Import unique features UI
from unique_features_ui import (
    SuperpowersFrame,
    SurvivalScenariosFrame,
    HistoricalMatchFrame,
    TimeMachineFrame,
    EpigeneticAgeFrame,
    ArchaicDNAFrame,
    DietTrainingFrame,
    AncestryStoryFrame,
    AllMarkersFrame
)
# Import comprehensive sensory genetics UI
from sensory_ui import SensoryGeneticsFrame

# Import comprehensive carrier status UI
from carrier_ui import CarrierStatusExpandedFrame

# Import comprehensive behavioral genetics UI
from behavioral_ui import BehavioralGeneticsFrame

# Import comprehensive sleep genetics UI
from sleep_ui import SleepGeneticsFrame

# Import expanded physical traits UI
from physical_traits_expanded_ui import PhysicalTraitsExpandedFrame

# Import sports genetics UI
from sports_ui import SportsGeneticsFrame

# Import reproduction genetics UI
from reproduction_ui import ReproductionGeneticsFrame

# Import immune deep genetics UI
from immune_deep_ui import ImmuneDeepGeneticsFrame

# Import nutrition metabolism UI
from nutrition_metabolism_ui import NutritionMetabolismFrame

# Import ancient DNA history UI
from ancient_dna_history_ui import AncientDNAHistoryFrame

# Import longevity genetics UI
from longevity_ui import LongevityGeneticsFrame

# Import pharmacogenomics UI
from pharmacogenomics_ui import PharmacogenomicsFrame as PharmacogenomicsDetailedFrame

# Import mental health genetics UI
from mental_health_ui import MentalHealthGeneticsFrame

# Import cancer risk genetics UI
from cancer_risk_ui import CancerRiskGeneticsFrame

# Import cardiovascular genetics UI
from cardiovascular_ui import CardiovascularGeneticsFrame

# Import skin dermatology genetics UI
from skin_dermatology_ui import SkinDermatologyFrame

# Import deep ancestry genetics UI
from ancestry_deep_ui import DeepAncestryFrame
from ancestry_ethnicity_ui import AncestryEthnicityFrame

# Configure appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# =============================================================================
# SIDEBAR FRAME
# =============================================================================

class SidebarFrame(ctk.CTkFrame):
    """Sidebar navigation with scrollable sections"""

    def __init__(self, parent, on_load_file, on_navigate):
        super().__init__(parent, width=280, corner_radius=0)
        self.on_load_file = on_load_file
        self.on_navigate = on_navigate
        self.active_button = None
        self.nav_buttons = {}

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Top section (fixed)
        top_frame = ctk.CTkFrame(self, fg_color="transparent")
        top_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 5))

        ctk.CTkLabel(
            top_frame, text="DNA Analysis", font=ctk.CTkFont(size=22, weight="bold")
        ).pack(pady=(5, 2))

        ctk.CTkLabel(
            top_frame, text="Genetic Insights", font=ctk.CTkFont(size=11), text_color="gray"
        ).pack(pady=(0, 10))

        self.load_btn = ctk.CTkButton(
            top_frame, text="Load DNA File", command=on_load_file,
            font=ctk.CTkFont(size=13, weight="bold"),
            height=40, fg_color="#2563eb", hover_color="#1d4ed8"
        )
        self.load_btn.pack(fill="x", padx=10, pady=(0, 5))

        # Scrollable nav section
        self.nav_scroll = ctk.CTkScrollableFrame(self, fg_color="transparent", width=250)
        self.nav_scroll.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        nav_sections = [
            # Core Analysis
            ("ethnicity", "Ancestry Analysis"),
            ("haplogroup", "Lineage & Migration"),
            ("archaicdna", "Archaic DNA"),
            ("ancienthistory", "Ancient Populations"),
            # Traits
            ("physical", "Physical Traits"),
            ("health", "Health Traits"),
            ("athletic", "Athletic Profile"),
            ("behavioral", "Behavioral"),
            ("sleep", "Sleep & Circadian"),
            ("sensory", "Sensory Traits"),
            # Medical
            ("pharma", "Drug Response"),
            ("carrier", "Carrier Status"),
            ("polygenic", "Disease Risks"),
            ("cancerrisk", "Cancer Risk"),
            ("cardiovasc", "Cardiovascular"),
            # Lifestyle
            ("immunity", "Immunity"),
            ("longevity", "Longevity"),
            ("nutrimetab", "Nutrition"),
            ("diettraining", "Diet & Training"),
            ("sportsgen", "Sports & Injury"),
            ("reproduction", "Reproduction"),
            ("skinderm", "Skin & Hair"),
            ("mentalhealth", "Mental Health"),
            # Tools
            ("allmarkers", "All Markers"),
            ("historical", "Historical Match"),
            ("superpowers", "Notable Variants"),
            ("survival", "Survival Sim"),
            ("epiage", "Biological Age"),
            ("plan", "Your Plan"),
            ("export", "Export")
        ]

        for key, label in nav_sections:
            btn = ctk.CTkButton(
                self.nav_scroll, text=label, anchor="w",
                command=lambda k=key: self.navigate(k),
                font=ctk.CTkFont(size=12),
                height=32, fg_color="transparent", text_color="gray60",
                hover_color="gray25", state="disabled"
            )
            btn.pack(fill="x", padx=5, pady=1)
            self.nav_buttons[key] = btn

        # Bottom section (fixed) - file info
        bottom_frame = ctk.CTkFrame(self, fg_color="gray20", corner_radius=8)
        bottom_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

        self.file_info = ctk.CTkLabel(
            bottom_frame, text="No file loaded", font=ctk.CTkFont(size=10),
            text_color="gray50", wraplength=220
        )
        self.file_info.pack(padx=10, pady=(8, 2))

        self.snp_info = ctk.CTkLabel(
            bottom_frame, text="", font=ctk.CTkFont(size=11, weight="bold"),
            text_color="#22c55e"
        )
        self.snp_info.pack(padx=10, pady=(0, 8))

    def navigate(self, section):
        """Handle navigation"""
        self.on_navigate(section)

    def set_active(self, section):
        """Highlight active section"""
        for key, btn in self.nav_buttons.items():
            if key == section:
                btn.configure(fg_color="#2563eb", text_color="white")
            else:
                btn.configure(fg_color="transparent", text_color="gray70")

    def enable_navigation(self, snp_count, file_name):
        """Enable navigation buttons after file load"""
        for btn in self.nav_buttons.values():
            btn.configure(state="normal", text_color="gray70")

        self.file_info.configure(text=f"File: {file_name}")
        self.snp_info.configure(text=f"{snp_count:,} SNPs analyzed")


# =============================================================================
# WELCOME FRAME
# =============================================================================

class WelcomeFrame(ctk.CTkFrame):
    """Welcome/landing screen"""

    def __init__(self, parent, on_load_file):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Center content
        center = ctk.CTkFrame(self, fg_color="transparent")
        center.grid(row=0, column=0)

        # Title
        title = ctk.CTkLabel(
            center, text="DNA Analysis Tool",
            font=ctk.CTkFont(size=42, weight="bold")
        )
        title.pack(pady=(0, 10))

        subtitle = ctk.CTkLabel(
            center, text="Comprehensive Genetic Analysis",
            font=ctk.CTkFont(size=18), text_color="gray60"
        )
        subtitle.pack(pady=(0, 40))

        # Feature list
        features = [
            "Ancestry Composition (177+ populations)",
            "Genetic Superpowers (rare mutations)",
            "Survival Scenario Simulator",
            "Historical Figure DNA Matching",
            "DNA Time Machine (migration paths)",
            "Biological Age Calculator",
            "Face Reconstruction from DNA",
            "Neanderthal/Denisovan Genes",
            "Personalized Diet & Training",
            "Ancestry Story Generator",
            "30+ Analysis Categories"
        ]

        features_frame = ctk.CTkFrame(center, fg_color="gray20", corner_radius=15)
        features_frame.pack(pady=20, padx=40, fill="x")

        for feature in features:
            row = ctk.CTkFrame(features_frame, fg_color="transparent")
            row.pack(fill="x", padx=20, pady=5)

            check = ctk.CTkLabel(row, text="", font=ctk.CTkFont(size=14))
            check.pack(side="left", padx=(0, 10))

            label = ctk.CTkLabel(row, text=feature, font=ctk.CTkFont(size=13))
            label.pack(side="left")

        # Load button
        load_btn = ctk.CTkButton(
            center, text="Load DNA File",
            command=on_load_file,
            font=ctk.CTkFont(size=18, weight="bold"),
            height=55, width=300,
            fg_color="#2563eb", hover_color="#1d4ed8"
        )
        load_btn.pack(pady=40)

        # Supported formats
        formats = ctk.CTkLabel(
            center, text="Supports: 23andMe, AncestryDNA, MyHeritage, FamilyTreeDNA",
            font=ctk.CTkFont(size=12), text_color="gray50"
        )
        formats.pack()


# =============================================================================
# LOADING FRAME
# =============================================================================

class LoadingFrame(ctk.CTkFrame):
    """Loading/progress indicator"""

    def __init__(self, parent, message="Analyzing..."):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        center = ctk.CTkFrame(self, fg_color="transparent")
        center.grid(row=0, column=0)

        self.progress = ctk.CTkProgressBar(center, width=400, mode="indeterminate")
        self.progress.pack(pady=20)
        self.progress.start()

        self.label = ctk.CTkLabel(
            center, text=message,
            font=ctk.CTkFont(size=16)
        )
        self.label.pack()


# =============================================================================
# ANCESTRY FRAME
# =============================================================================

class AncestryFrame(ctk.CTkFrame):
    """Ancestry composition display"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        title = ctk.CTkLabel(
            header, text="Ancestry Composition",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            header, text="Your genetic heritage based on 600,000+ markers from public databases",
            font=ctk.CTkFont(size=14), text_color="gray60"
        )
        subtitle.pack(anchor="w")

        # Scrollable content
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")
        scroll.grid_columnconfigure(0, weight=1)

        # Add important note about data limitations
        note_frame = ctk.CTkFrame(scroll, fg_color="#1a3d5c", corner_radius=10)
        note_frame.pack(fill="x", pady=(0, 15))

        ctk.CTkLabel(
            note_frame, text="About This Ancestry Analysis",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#7dd3fc"
        ).pack(anchor="w", padx=15, pady=(12, 5))

        note_text = (
            "This analysis uses public datasets (1000 Genomes, gnomAD) with ~50 reference populations. "
            "Commercial services like AncestryDNA use proprietary data from millions of customers with verified "
            "genealogy, allowing them to distinguish 1000+ granular regions (e.g., 'Sicily' vs 'Northern Italy', "
            "'Munster, Ireland' vs 'Ireland'). Our analysis shows accurate CONTINENTAL ancestry and BROAD regional "
            "estimates, but cannot match the fine-grained regional specificity of commercial services. "
            "For the most detailed regional breakdown, use your raw data with AncestryDNA, 23andMe, or similar services."
        )
        ctk.CTkLabel(
            note_frame, text=note_text,
            font=ctk.CTkFont(size=11), text_color="#bae6fd",
            wraplength=700, justify="left"
        ).pack(anchor="w", padx=15, pady=(0, 12))

        ancestry = results.ancestry.get('composition', {})
        details = results.ancestry.get('population_details', [])
        time_depths = results.ancestry.get('time_depths', {})

        if not ancestry:
            no_data = ctk.CTkLabel(
                scroll, text="No ancestry data available",
                font=ctk.CTkFont(size=16), text_color="gray50"
            )
            no_data.pack(pady=50)
            return

        # Regional summary first
        regional = results.ancestry.get('regional_summary', {})
        if regional:
            region_frame = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            region_frame.pack(fill="x", pady=10)

            region_title = ctk.CTkLabel(
                region_frame, text="Regional Summary",
                font=ctk.CTkFont(size=18, weight="bold")
            )
            region_title.pack(anchor="w", padx=20, pady=(15, 10))

            for region, pct in sorted(regional.items(), key=lambda x: x[1], reverse=True):
                row = ctk.CTkFrame(region_frame, fg_color="transparent")
                row.pack(fill="x", padx=20, pady=5)

                ctk.CTkLabel(
                    row, text=region, font=ctk.CTkFont(size=14)
                ).pack(side="left")

                ctk.CTkLabel(
                    row, text=f"{pct:.1f}%",
                    font=ctk.CTkFont(size=14, weight="bold"),
                    text_color="#22c55e"
                ).pack(side="right")

                # Progress bar
                bar = ctk.CTkProgressBar(row, width=200, height=12)
                bar.pack(side="right", padx=10)
                bar.set(min(pct / 100, 1.0))

            ctk.CTkFrame(region_frame, height=10, fg_color="transparent").pack()

        # Full Ancestry Composition
        pop_frame = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
        pop_frame.pack(fill="x", pady=10)

        pop_title = ctk.CTkLabel(
            pop_frame, text="Full Ancestry Breakdown",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        pop_title.pack(anchor="w", padx=20, pady=(15, 10))

        # Show marker counts
        markers_continental = results.ancestry.get('markers_continental', 0)
        markers_subpop = results.ancestry.get('markers_subpop', 0)
        pop_note = ctk.CTkLabel(
            pop_frame,
            text=f"Based on {markers_continental:,} continental markers + {markers_subpop} regional markers",
            font=ctk.CTkFont(size=11), text_color="gray50"
        )
        pop_note.pack(anchor="w", padx=20, pady=(0, 10))

        # Show ancestry composition
        for pop, pct in sorted(ancestry.items(), key=lambda x: x[1], reverse=True):
            row = ctk.CTkFrame(pop_frame, fg_color="gray25", corner_radius=8)
            row.pack(fill="x", padx=20, pady=5)

            top_row = ctk.CTkFrame(row, fg_color="transparent")
            top_row.pack(fill="x", padx=15, pady=10)

            ctk.CTkLabel(
                top_row, text=pop,
                font=ctk.CTkFont(size=15, weight="bold")
            ).pack(side="left")

            pct_color = "#22c55e" if pct >= 20 else "#3b82f6" if pct >= 5 else "gray60"
            ctk.CTkLabel(
                top_row, text=f"{pct:.1f}%",
                font=ctk.CTkFont(size=16, weight="bold"),
                text_color=pct_color
            ).pack(side="right")

            # Progress bar
            bar_frame = ctk.CTkFrame(top_row, fg_color="transparent")
            bar_frame.pack(side="right", padx=10)
            bar = ctk.CTkProgressBar(bar_frame, width=150, height=10)
            bar.pack()
            bar.set(min(pct / 100, 1.0))

        ctk.CTkFrame(pop_frame, height=10, fg_color="transparent").pack()

        # Time depth section
        if time_depths:
            time_frame = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            time_frame.pack(fill="x", pady=10)

            time_title = ctk.CTkLabel(
                time_frame, text="Ancestry Time Depths",
                font=ctk.CTkFont(size=18, weight="bold")
            )
            time_title.pack(anchor="w", padx=20, pady=(15, 10))

            for pop, depth in list(time_depths.items())[:10]:
                row = ctk.CTkFrame(time_frame, fg_color="transparent")
                row.pack(fill="x", padx=20, pady=3)

                ctk.CTkLabel(
                    row, text=pop.replace('_', ' '),
                    font=ctk.CTkFont(size=13)
                ).pack(side="left")

                ctk.CTkLabel(
                    row, text=depth,
                    font=ctk.CTkFont(size=12), text_color="gray60"
                ).pack(side="right")

            ctk.CTkFrame(time_frame, height=10, fg_color="transparent").pack()


# =============================================================================
# PHYSICAL TRAITS FRAME
# =============================================================================

class PhysicalTraitsFrame(ctk.CTkFrame):
    """Physical traits display - MERGED with expanded traits"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Physical Traits",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Complete genetic analysis of physical characteristics",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

        # Scrollable content
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")
        scroll.grid_columnconfigure((0, 1), weight=1)

        # === BASIC TRAITS SECTION ===
        traits = results.physical_traits
        row_idx = 0

        if traits:
            # Section header
            section_header = ctk.CTkFrame(scroll, fg_color="transparent")
            section_header.grid(row=row_idx, column=0, columnspan=2, sticky="w", padx=10, pady=(0, 10))
            ctk.CTkLabel(section_header, text="Core Traits",
                        font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w")
            row_idx += 1

            col_idx = 0
            for trait_name, trait_data in traits.items():
                if isinstance(trait_data, dict):
                    t_name = trait_data.get('trait_name', trait_name.replace('_', ' ').title())
                    t_confidence = trait_data.get('confidence', 0)
                    t_prediction = trait_data.get('prediction', 'N/A')
                    t_genotype = trait_data.get('genotype', 'N/A')
                    t_pop_comparison = trait_data.get('population_comparison')
                else:
                    t_name = trait_data.trait_name
                    t_confidence = trait_data.confidence
                    t_prediction = trait_data.prediction
                    t_genotype = trait_data.genotype
                    t_pop_comparison = None

                card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=12)
                card.grid(row=row_idx, column=col_idx, sticky="nsew", padx=10, pady=10)

                ctk.CTkLabel(card, text=t_name, font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="w", padx=20, pady=(15, 5))

                pred_color = "#22c55e" if t_confidence > 0.7 else "#eab308"
                ctk.CTkLabel(card, text=t_prediction, font=ctk.CTkFont(size=18, weight="bold"), text_color=pred_color).pack(anchor="w", padx=20, pady=5)

                conf_frame = ctk.CTkFrame(card, fg_color="transparent")
                conf_frame.pack(fill="x", padx=20, pady=5)
                ctk.CTkLabel(conf_frame, text="Confidence:", font=ctk.CTkFont(size=12), text_color="gray60").pack(side="left")
                bar = ctk.CTkProgressBar(conf_frame, width=100, height=10)
                bar.pack(side="left", padx=10)
                bar.set(t_confidence)
                ctk.CTkLabel(conf_frame, text=f"{t_confidence*100:.0f}%", font=ctk.CTkFont(size=12, weight="bold")).pack(side="left")

                ctk.CTkLabel(card, text=f"Genotype: {t_genotype}", font=ctk.CTkFont(size=11), text_color="gray50").pack(anchor="w", padx=20, pady=(5, 5))

                if t_pop_comparison:
                    ctk.CTkLabel(card, text=f"Population: {t_pop_comparison}", font=ctk.CTkFont(size=11), text_color="gray50").pack(anchor="w", padx=20, pady=(0, 15))
                else:
                    ctk.CTkLabel(card, text="").pack(pady=(0, 10))

                col_idx += 1
                if col_idx >= 2:
                    col_idx = 0
                    row_idx += 1

            if col_idx != 0:
                row_idx += 1

        # === EXPANDED TRAITS SECTION ===
        exp_traits = getattr(results, 'physical_traits_expanded', None)
        if exp_traits:
            # Section header
            section_header2 = ctk.CTkFrame(scroll, fg_color="transparent")
            section_header2.grid(row=row_idx, column=0, columnspan=2, sticky="w", padx=10, pady=(20, 10))
            ctk.CTkLabel(section_header2, text="Additional Traits",
                        font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w")
            row_idx += 1

            # Height
            height = exp_traits.get('height', {})
            if height:
                self._add_expanded_card(scroll, row_idx, 0, "Height Genetics",
                    height.get('prediction', 'N/A'), height.get('percentile', ''), height.get('markers', []))
                row_idx += 1

            # Hair texture
            hair = exp_traits.get('hair_texture', {})
            if hair:
                self._add_expanded_card(scroll, row_idx, 0, "Hair Texture",
                    hair.get('prediction', 'N/A'), hair.get('description', ''), hair.get('markers', []))

            # Hair loss
            loss = exp_traits.get('hair_loss', {})
            if loss:
                self._add_expanded_card(scroll, row_idx, 1, "Hair Loss Risk",
                    loss.get('risk_level', 'N/A'), loss.get('description', ''), loss.get('markers', []))
            row_idx += 1

            # Freckles & Dimples
            freckles = exp_traits.get('freckles', {})
            if freckles:
                self._add_expanded_card(scroll, row_idx, 0, "Freckles",
                    freckles.get('prediction', 'N/A'), '', freckles.get('markers', []))

            dimples = exp_traits.get('dimples', {})
            if dimples:
                self._add_expanded_card(scroll, row_idx, 1, "Dimples",
                    dimples.get('prediction', 'N/A'), '', dimples.get('markers', []))
            row_idx += 1

            # Widow's peak & Cleft chin
            widows = exp_traits.get('widows_peak', {})
            if widows:
                self._add_expanded_card(scroll, row_idx, 0, "Widow's Peak",
                    widows.get('prediction', 'N/A'), '', widows.get('markers', []))

            cleft = exp_traits.get('cleft_chin', {})
            if cleft:
                self._add_expanded_card(scroll, row_idx, 1, "Cleft Chin",
                    cleft.get('prediction', 'N/A'), '', cleft.get('markers', []))
            row_idx += 1

            # Earlobes & Tongue rolling
            earlobes = exp_traits.get('earlobes', {})
            if earlobes:
                self._add_expanded_card(scroll, row_idx, 0, "Earlobe Type",
                    earlobes.get('prediction', 'N/A'), '', earlobes.get('markers', []))

            tongue = exp_traits.get('tongue_rolling', {})
            if tongue:
                self._add_expanded_card(scroll, row_idx, 1, "Tongue Rolling",
                    tongue.get('prediction', 'N/A'), '', tongue.get('markers', []))

        if not traits and not exp_traits:
            ctk.CTkLabel(scroll, text="No physical trait data available",
                font=ctk.CTkFont(size=16), text_color="gray50").grid(row=0, column=0, columnspan=2, pady=50)

    def _add_expanded_card(self, parent, row, col, title, prediction, description, markers):
        """Helper to add an expanded trait card"""
        card = ctk.CTkFrame(parent, fg_color="gray20", corner_radius=12)
        card.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)

        ctk.CTkLabel(card, text=title, font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="w", padx=20, pady=(15, 5))
        ctk.CTkLabel(card, text=str(prediction), font=ctk.CTkFont(size=18, weight="bold"), text_color="#22c55e").pack(anchor="w", padx=20, pady=5)

        if description:
            ctk.CTkLabel(card, text=description, font=ctk.CTkFont(size=12), text_color="gray60", wraplength=250).pack(anchor="w", padx=20, pady=5)

        if markers:
            markers_text = ", ".join([m.get('rsid', '') for m in markers[:3]] if isinstance(markers, list) else [])
            if markers_text:
                ctk.CTkLabel(card, text=f"Markers: {markers_text}", font=ctk.CTkFont(size=10), text_color="gray50").pack(anchor="w", padx=20, pady=(5, 15))
            else:
                ctk.CTkLabel(card, text="").pack(pady=(0, 10))
        else:
            ctk.CTkLabel(card, text="").pack(pady=(0, 10))


# =============================================================================
# HEALTH TRAITS FRAME
# =============================================================================

class HealthTraitsFrame(ctk.CTkFrame):
    """Health traits display"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Health Traits",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Genetic factors affecting health and wellness",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

        # Scrollable content
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        traits = results.health_traits
        if not traits:
            ctk.CTkLabel(
                scroll, text="No health trait data available",
                font=ctk.CTkFont(size=16), text_color="gray50"
            ).pack(pady=50)
            return

        for trait_name, data in traits.items():
            card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            card.pack(fill="x", pady=8, padx=10)

            content = ctk.CTkFrame(card, fg_color="transparent")
            content.pack(fill="x", padx=20, pady=15)

            # Get trait display name
            display_name = data.get('trait_name', trait_name.replace('_', ' ').title())

            left = ctk.CTkFrame(content, fg_color="transparent")
            left.pack(side="left", fill="x", expand=True)

            ctk.CTkLabel(
                left, text=display_name,
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w")

            # Get description from findings or direct
            description = ''
            if data.get('all_findings') and len(data['all_findings']) > 0:
                description = data['all_findings'][0].get('description', '')
            else:
                description = data.get('description', '')

            ctk.CTkLabel(
                left, text=description,
                font=ctk.CTkFont(size=12), text_color="gray60",
                wraplength=400
            ).pack(anchor="w")

            # Action recommendation (new)
            action = data.get('action', '')
            if action:
                ctk.CTkLabel(
                    left, text=f"→ {action}",
                    font=ctk.CTkFont(size=11), text_color="#22c55e",
                    wraplength=400
                ).pack(anchor="w", pady=(5, 0))

            right = ctk.CTkFrame(content, fg_color="transparent")
            right.pack(side="right")

            status = data.get('status', 'Unknown')
            status_color = "#22c55e" if 'Normal' in status or 'tolerant' in status.lower() or 'Fast' in status else "#eab308"
            ctk.CTkLabel(
                right, text=status,
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color=status_color
            ).pack()


# =============================================================================
# PHARMACOGENOMICS FRAME
# =============================================================================

class PharmacogenomicsFrame(ctk.CTkFrame):
    """Drug metabolism genetics display"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Pharmacogenomics",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="How your genes affect drug metabolism",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

        # Warning
        warning = ctk.CTkFrame(header, fg_color="#7f1d1d", corner_radius=8)
        warning.pack(fill="x", pady=10)
        ctk.CTkLabel(
            warning, text="This information is for educational purposes. Consult healthcare providers before making medication changes.",
            font=ctk.CTkFont(size=12), text_color="#fca5a5", wraplength=800
        ).pack(padx=15, pady=10)

        # Scrollable content
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        # High priority alerts first
        alerts = results.pharmacogenomics.get('high_priority_alerts', [])
        if alerts:
            alert_frame = ctk.CTkFrame(scroll, fg_color="#7f1d1d", corner_radius=10)
            alert_frame.pack(fill="x", pady=8, padx=10)
            ctk.CTkLabel(
                alert_frame, text="⚠ HIGH PRIORITY ALERTS",
                font=ctk.CTkFont(size=16, weight="bold"), text_color="#fca5a5"
            ).pack(anchor="w", padx=20, pady=(15, 5))
            for alert in alerts:
                ctk.CTkLabel(
                    alert_frame, text=f"{alert['gene']}: {alert['alert']}",
                    font=ctk.CTkFont(size=14, weight="bold"), text_color="#fecaca"
                ).pack(anchor="w", padx=20)
                ctk.CTkLabel(
                    alert_frame, text=f"Affected: {', '.join(alert['affected_drugs'])}",
                    font=ctk.CTkFont(size=12), text_color="#fca5a5"
                ).pack(anchor="w", padx=20, pady=(0, 10))

        pharma = results.pharmacogenomics.get('gene_results', {})
        if not pharma:
            ctk.CTkLabel(
                scroll, text="No pharmacogenomic data available",
                font=ctk.CTkFont(size=16), text_color="gray50"
            ).pack(pady=50)
            return

        for gene, data in pharma.items():
            card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            card.pack(fill="x", pady=8, padx=10)

            header_row = ctk.CTkFrame(card, fg_color="transparent")
            header_row.pack(fill="x", padx=20, pady=(15, 10))

            ctk.CTkLabel(
                header_row, text=gene,
                font=ctk.CTkFont(size=18, weight="bold")
            ).pack(side="left")

            phenotype = data.get('overall_phenotype', 'Unknown')
            pheno_color = "#ef4444" if 'Poor' in phenotype or 'Ultra' in phenotype else "#22c55e"
            ctk.CTkLabel(
                header_row, text=phenotype,
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color=pheno_color
            ).pack(side="right")

            ctk.CTkLabel(
                card, text=data.get('description', ''),
                font=ctk.CTkFont(size=12), text_color="gray60"
            ).pack(anchor="w", padx=20)

            # Action recommendation (new)
            action = data.get('primary_action', '')
            if action:
                ctk.CTkLabel(
                    card, text=f"→ {action}",
                    font=ctk.CTkFont(size=12), text_color="#22c55e"
                ).pack(anchor="w", padx=20, pady=(5, 0))

            # Affected drugs
            drugs = data.get('affected_drugs', [])
            if drugs:
                ctk.CTkLabel(
                    card, text=f"Affected medications: {', '.join(drugs[:6])}{'...' if len(drugs) > 6 else ''}",
                    font=ctk.CTkFont(size=12), text_color="gray50"
                ).pack(anchor="w", padx=20, pady=(10, 15))

        # === DETAILED PHARMACOGENOMICS SECTION ===
        detailed = getattr(results, 'pharmacogenomics_detailed', None)
        if detailed and isinstance(detailed, dict):
            # Section header
            section_header = ctk.CTkFrame(scroll, fg_color="transparent")
            section_header.pack(fill="x", padx=10, pady=(20, 10))
            ctk.CTkLabel(section_header, text="Detailed Drug Metabolism",
                        font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w")

            # Display detailed categories
            for category, cat_data in detailed.items():
                if not isinstance(cat_data, dict):
                    continue

                cat_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
                cat_card.pack(fill="x", pady=8, padx=10)

                ctk.CTkLabel(cat_card, text=category.replace('_', ' ').title(),
                    font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="w", padx=20, pady=(15, 5))

                for gene, gene_data in cat_data.items():
                    if isinstance(gene_data, dict):
                        status = gene_data.get('status', gene_data.get('metabolism', 'Unknown'))
                        genotype = gene_data.get('genotype', '')
                        gene_row = ctk.CTkFrame(cat_card, fg_color="transparent")
                        gene_row.pack(fill="x", padx=20, pady=3)
                        ctk.CTkLabel(gene_row, text=f"{gene}: ", font=ctk.CTkFont(size=12)).pack(side="left")
                        status_color = "#ef4444" if 'poor' in str(status).lower() or 'high' in str(status).lower() else "#22c55e"
                        ctk.CTkLabel(gene_row, text=status, font=ctk.CTkFont(size=12, weight="bold"), text_color=status_color).pack(side="left")
                        if genotype:
                            ctk.CTkLabel(gene_row, text=f" ({genotype})", font=ctk.CTkFont(size=11), text_color="gray50").pack(side="left")

                ctk.CTkLabel(cat_card, text="").pack(pady=(0, 10))


# =============================================================================
# HAPLOGROUP FRAME
# =============================================================================

class HaplogroupFrame(ctk.CTkFrame):
    """Combined Haplogroup and Migration Timeline display"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Lineage & Migration",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Your ancient maternal and paternal lineages with migration history",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

        # Scrollable content
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")
        scroll.grid_columnconfigure((0, 1), weight=1)

        haplos = results.haplogroups

        # Get time machine data from unique_features
        tm = results.unique_features.get('time_machine', {}) if hasattr(results, 'unique_features') else {}

        # mtDNA Card
        mtdna = haplos.get('mtDNA', {})
        mtdna_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=15)
        mtdna_card.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        ctk.CTkLabel(
            mtdna_card, text="Maternal Lineage (mtDNA)",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=25, pady=(25, 10))

        ctk.CTkLabel(
            mtdna_card, text=mtdna.get('haplogroup', 'Unknown'),
            font=ctk.CTkFont(size=42, weight="bold"),
            text_color="#ec4899"
        ).pack(padx=25, pady=10)

        ctk.CTkLabel(
            mtdna_card, text=f"Origin: {mtdna.get('origin', 'Unknown')}",
            font=ctk.CTkFont(size=14)
        ).pack(padx=25)

        ctk.CTkLabel(
            mtdna_card, text=mtdna.get('description', ''),
            font=ctk.CTkFont(size=12), text_color="gray60", wraplength=280
        ).pack(padx=25, pady=(10, 25))

        # Y-DNA Card
        ydna = haplos.get('Y_DNA', {})
        ydna_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=15)
        ydna_card.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        ctk.CTkLabel(
            ydna_card, text="Paternal Lineage (Y-DNA)",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=25, pady=(25, 10))

        ctk.CTkLabel(
            ydna_card, text=ydna.get('haplogroup', 'Unknown'),
            font=ctk.CTkFont(size=42, weight="bold"),
            text_color="#3b82f6"
        ).pack(padx=25, pady=10)

        ctk.CTkLabel(
            ydna_card, text=f"Origin: {ydna.get('origin', 'Unknown')}",
            font=ctk.CTkFont(size=14)
        ).pack(padx=25)

        ctk.CTkLabel(
            ydna_card, text=ydna.get('description', ''),
            font=ctk.CTkFont(size=12), text_color="gray60", wraplength=280
        ).pack(padx=25, pady=(10, 25))

        # Migration Timeline Section
        timeline_header = ctk.CTkFrame(scroll, fg_color="transparent")
        timeline_header.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=(20, 10))

        ctk.CTkLabel(
            timeline_header, text="Migration Timeline",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            timeline_header, text="Trace your ancestors' journey through time",
            font=ctk.CTkFont(size=12), text_color="gray60"
        ).pack(anchor="w")

        # Maternal Migration Journey
        maternal = tm.get('maternal_journey', [])
        if maternal:
            maternal_section = ctk.CTkFrame(scroll, fg_color="transparent")
            maternal_section.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)

            ctk.CTkLabel(
                maternal_section, text="MATERNAL LINE (mtDNA)",
                font=ctk.CTkFont(size=12, weight="bold"), text_color="#ec4899"
            ).pack(anchor="w", pady=(0, 8))

            for step in maternal[:5]:
                row = ctk.CTkFrame(maternal_section, fg_color="gray20", corner_radius=8, height=60)
                row.pack(fill="x", pady=2)
                row.pack_propagate(False)

                left = ctk.CTkFrame(row, fg_color="transparent")
                left.pack(side="left", padx=12, pady=8)

                ctk.CTkLabel(
                    left, text=f"Haplogroup {step.get('haplogroup', '?')}",
                    font=ctk.CTkFont(size=14, weight="bold"), text_color="#ec4899"
                ).pack(anchor="w")
                ctk.CTkLabel(
                    left, text=f"{step.get('origin', 'Unknown')} - {step.get('age_formatted', 'Unknown')}",
                    font=ctk.CTkFont(size=10), text_color="gray50"
                ).pack(anchor="w")

        # Paternal Migration Journey
        paternal = tm.get('paternal_journey', [])
        if paternal:
            paternal_section = ctk.CTkFrame(scroll, fg_color="transparent")
            paternal_section.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

            ctk.CTkLabel(
                paternal_section, text="PATERNAL LINE (Y-DNA)",
                font=ctk.CTkFont(size=12, weight="bold"), text_color="#3b82f6"
            ).pack(anchor="w", pady=(0, 8))

            for step in paternal[:5]:
                row = ctk.CTkFrame(paternal_section, fg_color="gray20", corner_radius=8, height=60)
                row.pack(fill="x", pady=2)
                row.pack_propagate(False)

                left = ctk.CTkFrame(row, fg_color="transparent")
                left.pack(side="left", padx=12, pady=8)

                ctk.CTkLabel(
                    left, text=f"Haplogroup {step.get('haplogroup', '?')}",
                    font=ctk.CTkFont(size=14, weight="bold"), text_color="#3b82f6"
                ).pack(anchor="w")
                ctk.CTkLabel(
                    left, text=f"{step.get('origin', 'Unknown')} - {step.get('age_formatted', 'Unknown')}",
                    font=ctk.CTkFont(size=10), text_color="gray50"
                ).pack(anchor="w")

        # If no migration data available
        if not maternal and not paternal:
            no_data = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            no_data.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
            ctk.CTkLabel(
                no_data, text="Migration timeline data not available",
                font=ctk.CTkFont(size=14), text_color="gray50"
            ).pack(pady=20)


# =============================================================================
# IMMUNITY FRAME
# =============================================================================

class ImmunityFrame(ctk.CTkFrame):
    """Immunity and pathogen resistance display"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Immunity & Pathogen Resistance",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Your genetic resistance to diseases and pathogens",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

        # Scrollable content
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        immunity = results.immunity
        pathogens = immunity.get('pathogen_resistance', [])

        if not pathogens:
            ctk.CTkLabel(
                scroll, text="No immunity data available",
                font=ctk.CTkFont(size=16), text_color="gray50"
            ).pack(pady=50)
            return

        # Disease susceptibility section
        susceptibility = immunity.get('disease_susceptibility', [])
        if susceptibility:
            for item in susceptibility:
                card = ctk.CTkFrame(scroll, fg_color="#7f1d1d" if 'Higher' in str(item.get('risk', '')) else "gray20", corner_radius=10)
                card.pack(fill="x", pady=8, padx=10)

                ctk.CTkLabel(
                    card, text=item.get('condition', 'Unknown'),
                    font=ctk.CTkFont(size=16, weight="bold"),
                    text_color="#fca5a5" if 'Higher' in str(item.get('risk', '')) else "white"
                ).pack(anchor="w", padx=20, pady=(15, 5))

                ctk.CTkLabel(
                    card, text=f"Risk: {item.get('risk', 'Unknown')}",
                    font=ctk.CTkFont(size=14),
                    text_color="#fca5a5" if 'Higher' in str(item.get('risk', '')) else "gray60"
                ).pack(anchor="w", padx=20)

                if item.get('action'):
                    ctk.CTkLabel(
                        card, text=f"→ {item['action']}",
                        font=ctk.CTkFont(size=12), text_color="#22c55e"
                    ).pack(anchor="w", padx=20, pady=(5, 15))

        # Pathogen resistance section
        for pathogen in pathogens:
            card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            card.pack(fill="x", pady=8, padx=10)

            content = ctk.CTkFrame(card, fg_color="transparent")
            content.pack(fill="x", padx=20, pady=15)

            left = ctk.CTkFrame(content, fg_color="transparent")
            left.pack(side="left", fill="x", expand=True)

            ctk.CTkLabel(
                left, text=pathogen.get('pathogen', 'Unknown'),
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w")

            # Description
            desc = pathogen.get('description', '')
            if desc:
                ctk.CTkLabel(
                    left, text=desc,
                    font=ctk.CTkFont(size=12), text_color="gray60",
                    wraplength=400
                ).pack(anchor="w")

            # Action
            action = pathogen.get('action', '')
            if action:
                ctk.CTkLabel(
                    left, text=f"→ {action}",
                    font=ctk.CTkFont(size=11), text_color="#22c55e"
                ).pack(anchor="w", pady=(5, 0))

            resistance = pathogen.get('resistance', 'Unknown')
            res_color = "#22c55e" if resistance in ['High', 'Strong', 'Partial', 'Resistant', 'Immune'] else "gray60"
            ctk.CTkLabel(
                content, text=f"Resistance: {resistance}",
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color=res_color
            ).pack(side="right")

        # === DEEP IMMUNE GENETICS SECTION ===
        immune_deep = getattr(results, 'immune_deep_genetics', None)
        if immune_deep and isinstance(immune_deep, dict):
            # Section header
            section_header = ctk.CTkFrame(scroll, fg_color="transparent")
            section_header.pack(fill="x", padx=10, pady=(20, 10))
            ctk.CTkLabel(section_header, text="Advanced Immune Genetics",
                        font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w")
            ctk.CTkLabel(section_header, text="HLA types, autoimmune risks, inflammatory markers",
                        font=ctk.CTkFont(size=12), text_color="gray60").pack(anchor="w")

            # Display immune categories
            for category, cat_data in immune_deep.items():
                if not isinstance(cat_data, dict):
                    continue

                cat_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
                cat_card.pack(fill="x", pady=8, padx=10)

                cat_name = category.replace('_', ' ').title()
                ctk.CTkLabel(cat_card, text=cat_name,
                    font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="w", padx=20, pady=(15, 5))

                for item, item_data in cat_data.items():
                    if isinstance(item_data, dict):
                        risk = item_data.get('risk', item_data.get('status', 'Unknown'))
                        genotype = item_data.get('genotype', '')
                        item_row = ctk.CTkFrame(cat_card, fg_color="transparent")
                        item_row.pack(fill="x", padx=20, pady=3)
                        ctk.CTkLabel(item_row, text=f"{item.replace('_', ' ').title()}: ", font=ctk.CTkFont(size=12)).pack(side="left")
                        risk_color = "#ef4444" if 'high' in str(risk).lower() or 'increased' in str(risk).lower() else "#22c55e"
                        ctk.CTkLabel(item_row, text=str(risk), font=ctk.CTkFont(size=12, weight="bold"), text_color=risk_color).pack(side="left")
                        if genotype:
                            ctk.CTkLabel(item_row, text=f" ({genotype})", font=ctk.CTkFont(size=11), text_color="gray50").pack(side="left")

                ctk.CTkLabel(cat_card, text="").pack(pady=(0, 10))


# =============================================================================
# LONGEVITY FRAME
# =============================================================================

class LongevityFrame(ctk.CTkFrame):
    """Longevity and aging genetics display with progress bars"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Longevity & Aging Genetics",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Genetic factors influencing healthy aging",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        longevity = results.longevity
        overall_score = longevity.get('overall_score', 50)
        category = longevity.get('category', 'Average')
        interpretation = longevity.get('interpretation', '')

        # Big score card with circular-style display
        score_card = ctk.CTkFrame(scroll, fg_color="#1e3a5f", corner_radius=15)
        score_card.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            score_card, text="LONGEVITY SCORE",
            font=ctk.CTkFont(size=12, weight="bold"), text_color="gray60"
        ).pack(pady=(20, 5))

        score_color = "#22c55e" if overall_score >= 60 else "#eab308" if overall_score >= 45 else "#ef4444"
        ctk.CTkLabel(
            score_card, text=f"{overall_score:.0f}",
            font=ctk.CTkFont(size=64, weight="bold"), text_color=score_color
        ).pack()

        # Progress bar for overall score
        bar_frame = ctk.CTkFrame(score_card, fg_color="transparent")
        bar_frame.pack(fill="x", padx=40, pady=10)
        overall_bar = ctk.CTkProgressBar(bar_frame, height=20, corner_radius=10, progress_color=score_color)
        overall_bar.pack(fill="x")
        overall_bar.set(overall_score / 100)

        ctk.CTkLabel(
            score_card, text=category, font=ctk.CTkFont(size=16, weight="bold"), text_color="white"
        ).pack(pady=(5, 5))

        if interpretation:
            ctk.CTkLabel(
                score_card, text=interpretation, font=ctk.CTkFont(size=12), text_color="gray60"
            ).pack(pady=(0, 15))

        # Stats row
        stats_frame = ctk.CTkFrame(scroll, fg_color="transparent")
        stats_frame.pack(fill="x", pady=10, padx=10)

        longevity_vars = longevity.get('longevity_variants', 0)
        centenarian_vars = longevity.get('centenarian_variants', 0)
        markers_analyzed = longevity.get('markers_analyzed', 0)

        for stat_name, stat_val, stat_color in [
            ("Longevity Variants", longevity_vars, "#22c55e"),
            ("Centenarian Variants", centenarian_vars, "#a855f7"),
            ("Markers Analyzed", markers_analyzed, "#3b82f6")
        ]:
            stat_card = ctk.CTkFrame(stats_frame, fg_color="gray20", corner_radius=10)
            stat_card.pack(side="left", expand=True, fill="both", padx=5, pady=5)
            ctk.CTkLabel(stat_card, text=str(stat_val), font=ctk.CTkFont(size=28, weight="bold"), text_color=stat_color).pack(pady=(15, 0))
            ctk.CTkLabel(stat_card, text=stat_name, font=ctk.CTkFont(size=11), text_color="gray60").pack(pady=(0, 15))

        # Aging factors with progress bars
        factors = longevity.get('aging_factors', [])
        if factors:
            factors_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            factors_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                factors_card, text="Longevity Genes Analyzed",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for factor in factors:
                row = ctk.CTkFrame(factors_card, fg_color="gray25", corner_radius=8)
                row.pack(fill="x", padx=20, pady=4)

                top_row = ctk.CTkFrame(row, fg_color="transparent")
                top_row.pack(fill="x", padx=15, pady=(8, 2))

                gene = factor.get('gene', factor.get('factor', 'Unknown'))
                rsid = factor.get('rsid', '')
                genotype = factor.get('genotype', '')
                effect = factor.get('effect', '')
                score = factor.get('score', 50)
                is_centenarian = factor.get('centenarian_enriched', False)

                gene_text = f"{gene}"
                if rsid:
                    gene_text += f" ({rsid})"
                if is_centenarian:
                    gene_text += " *"

                ctk.CTkLabel(top_row, text=gene_text, font=ctk.CTkFont(size=13, weight="bold")).pack(side="left")

                score_clr = "#22c55e" if score >= 60 else "#eab308" if score >= 45 else "#ef4444"
                ctk.CTkLabel(top_row, text=f"{score:.0f}", font=ctk.CTkFont(size=14, weight="bold"), text_color=score_clr).pack(side="right")

                # Progress bar
                bar_row = ctk.CTkFrame(row, fg_color="transparent")
                bar_row.pack(fill="x", padx=15, pady=(0, 4))
                factor_bar = ctk.CTkProgressBar(bar_row, height=8, corner_radius=4, progress_color=score_clr)
                factor_bar.pack(fill="x")
                factor_bar.set(score / 100)

                if effect or genotype:
                    info_row = ctk.CTkFrame(row, fg_color="transparent")
                    info_row.pack(fill="x", padx=15, pady=(0, 8))
                    info_text = f"{genotype}: {effect}" if genotype and effect else effect or genotype
                    ctk.CTkLabel(info_row, text=info_text, font=ctk.CTkFont(size=11), text_color="gray60").pack(anchor="w")

            ctk.CTkLabel(factors_card, text="* Found in centenarian studies", font=ctk.CTkFont(size=10), text_color="#a855f7").pack(anchor="w", padx=20, pady=(5, 15))

        # Recommendations
        recs = longevity.get('recommendations', [])
        if recs:
            rec_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            rec_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(rec_card, text="Longevity Recommendations", font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="w", padx=20, pady=(15, 10))

            for rec in recs:
                rec_row = ctk.CTkFrame(rec_card, fg_color="gray25", corner_radius=6)
                rec_row.pack(fill="x", padx=20, pady=3)
                ctk.CTkLabel(rec_row, text=rec, font=ctk.CTkFont(size=12), wraplength=500).pack(anchor="w", padx=15, pady=8)

            ctk.CTkFrame(rec_card, height=10, fg_color="transparent").pack()

        # === DETAILED LONGEVITY GENETICS SECTION ===
        longevity_detailed = getattr(results, 'longevity_genetics', None)
        if longevity_detailed and isinstance(longevity_detailed, dict):
            # Section header
            section_header = ctk.CTkFrame(scroll, fg_color="transparent")
            section_header.pack(fill="x", padx=10, pady=(20, 10))
            ctk.CTkLabel(section_header, text="Advanced Longevity Pathways",
                        font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w")

            # Display pathway categories
            for pathway, pathway_data in longevity_detailed.items():
                if not isinstance(pathway_data, dict):
                    continue

                path_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
                path_card.pack(fill="x", pady=8, padx=10)

                # Pathway name
                pathway_name = pathway.replace('_', ' ').title()
                ctk.CTkLabel(path_card, text=pathway_name,
                    font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="w", padx=20, pady=(15, 5))

                # Pathway genes
                for gene, gene_data in pathway_data.items():
                    if isinstance(gene_data, dict):
                        status = gene_data.get('status', gene_data.get('effect', 'Unknown'))
                        genotype = gene_data.get('genotype', '')
                        gene_row = ctk.CTkFrame(path_card, fg_color="transparent")
                        gene_row.pack(fill="x", padx=20, pady=3)
                        ctk.CTkLabel(gene_row, text=f"{gene}: ", font=ctk.CTkFont(size=12)).pack(side="left")
                        status_color = "#22c55e" if 'beneficial' in str(status).lower() or 'good' in str(status).lower() else "#eab308"
                        ctk.CTkLabel(gene_row, text=str(status), font=ctk.CTkFont(size=12, weight="bold"), text_color=status_color).pack(side="left")
                        if genotype:
                            ctk.CTkLabel(gene_row, text=f" ({genotype})", font=ctk.CTkFont(size=11), text_color="gray50").pack(side="left")

                ctk.CTkLabel(path_card, text="").pack(pady=(0, 10))


# =============================================================================
# NUTRITION & FITNESS FRAME
# =============================================================================

class NutritionFitnessFrame(ctk.CTkFrame):
    """Nutrition and fitness genetics display"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Nutrition & Fitness Genetics",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Personalized nutrition and exercise recommendations based on your DNA",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

        # Scrollable content
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")
        scroll.grid_columnconfigure((0, 1), weight=1)

        nf = results.nutrition_fitness

        # Supplement recommendations first
        supplements = nf.get('supplement_recommendations', [])
        if supplements:
            supp_card = ctk.CTkFrame(scroll, fg_color="gray25", corner_radius=10)
            supp_card.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

            ctk.CTkLabel(
                supp_card, text="Personalized Supplement Recommendations",
                font=ctk.CTkFont(size=18, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for supp in supplements:
                ctk.CTkLabel(
                    supp_card, text=f"• {supp.get('nutrient', '')}: {supp.get('recommendation', '')}",
                    font=ctk.CTkFont(size=13), text_color="#22c55e",
                    wraplength=700
                ).pack(anchor="w", padx=25, pady=3)
            ctk.CTkFrame(supp_card, height=10, fg_color="transparent").pack()

        # Nutrition section
        nutrition = nf.get('nutrition', {})
        if nutrition:
            nutr_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            nutr_card.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

            ctk.CTkLabel(
                nutr_card, text="Nutrition Insights",
                font=ctk.CTkFont(size=18, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for trait, data in nutrition.items():
                row = ctk.CTkFrame(nutr_card, fg_color="gray25", corner_radius=8)
                row.pack(fill="x", padx=20, pady=5)

                display_name = data.get('trait_name', trait.replace('_', ' ').title())
                ctk.CTkLabel(
                    row, text=display_name,
                    font=ctk.CTkFont(size=13, weight="bold")
                ).pack(anchor="w", padx=15, pady=(10, 3))

                need = data.get('need', '')
                if need:
                    ctk.CTkLabel(
                        row, text=f"Status: {need}",
                        font=ctk.CTkFont(size=12), text_color="gray60"
                    ).pack(anchor="w", padx=15)

                rec = data.get('recommendation', '')
                if rec:
                    ctk.CTkLabel(
                        row, text=f"→ {rec}",
                        font=ctk.CTkFont(size=11), text_color="#22c55e",
                        wraplength=300
                    ).pack(anchor="w", padx=15, pady=(3, 10))
                else:
                    ctk.CTkFrame(row, height=10, fg_color="transparent").pack()

            ctk.CTkFrame(nutr_card, height=15, fg_color="transparent").pack()

        # Fitness section
        fitness = nf.get('fitness', {})
        if fitness:
            fit_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            fit_card.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

            ctk.CTkLabel(
                fit_card, text="Fitness Insights",
                font=ctk.CTkFont(size=18, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for trait, data in fitness.items():
                row = ctk.CTkFrame(fit_card, fg_color="gray25", corner_radius=8)
                row.pack(fill="x", padx=20, pady=5)

                display_name = data.get('trait_name', trait.replace('_', ' ').title())
                ctk.CTkLabel(
                    row, text=display_name,
                    font=ctk.CTkFont(size=13, weight="bold")
                ).pack(anchor="w", padx=15, pady=(10, 3))

                trait_type = data.get('type', '')
                type_color = "#22c55e" if 'Power' in str(trait_type) else "#3b82f6" if 'Endurance' in str(trait_type) else "white"
                if trait_type:
                    ctk.CTkLabel(
                        row, text=trait_type,
                        font=ctk.CTkFont(size=14), text_color=type_color
                    ).pack(anchor="w", padx=15)

                training = data.get('training_focus', data.get('focus', ''))
                if training:
                    ctk.CTkLabel(
                        row, text=f"→ {training}",
                        font=ctk.CTkFont(size=11), text_color="#22c55e",
                        wraplength=300
                    ).pack(anchor="w", padx=15, pady=(3, 10))
                else:
                    ctk.CTkFrame(row, height=10, fg_color="transparent").pack()

            ctk.CTkFrame(fit_card, height=15, fg_color="transparent").pack()

        # Exercise recommendations
        ex_recs = nf.get('exercise_recommendations', [])
        if ex_recs:
            rec_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            rec_card.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

            ctk.CTkLabel(
                rec_card, text="Exercise Recommendations",
                font=ctk.CTkFont(size=18, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for rec in ex_recs:
                ctk.CTkLabel(
                    rec_card, text=f"• {rec}",
                    font=ctk.CTkFont(size=13), wraplength=700
                ).pack(anchor="w", padx=25, pady=3)
            ctk.CTkFrame(rec_card, height=15, fg_color="transparent").pack()


# =============================================================================
# CLIMATE ADAPTATION FRAME
# =============================================================================

class ClimateFrame(ctk.CTkFrame):
    """Climate adaptation genetics display"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Climate Adaptation",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="How your genetics adapted to different climates",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

        # Content
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        climate = results.climate_adaptation
        adaptations = climate.get('adaptations', [])

        if not adaptations:
            ctk.CTkLabel(
                scroll, text="No climate adaptation data available",
                font=ctk.CTkFont(size=16), text_color="gray50"
            ).pack(pady=50)
            return

        for adapt in adaptations:
            card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            card.pack(fill="x", pady=8, padx=10)

            content = ctk.CTkFrame(card, fg_color="transparent")
            content.pack(fill="x", padx=20, pady=15)

            ctk.CTkLabel(
                content, text=adapt.get('trait', ''),
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(side="left")

            adaptation = adapt.get('adaptation', 'Unknown')
            adapt_color = "#22c55e" if 'High' in adaptation or 'Enhanced' in adaptation else "gray60"
            ctk.CTkLabel(
                content, text=adaptation,
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color=adapt_color
            ).pack(side="right")


# =============================================================================
# POLYGENIC SCORES FRAME
# =============================================================================

class PolygenicFrame(ctk.CTkFrame):
    """Polygenic risk scores display"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Disease Risk Scores",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Polygenic risk estimates for complex conditions",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

        # Warning
        warning = ctk.CTkFrame(header, fg_color="#7f1d1d", corner_radius=8)
        warning.pack(fill="x", pady=10)
        ctk.CTkLabel(
            warning, text="These are genetic risk estimates only. Many factors affect disease risk. Consult a healthcare provider.",
            font=ctk.CTkFont(size=12), text_color="#fca5a5", wraplength=800
        ).pack(padx=15, pady=10)

        # Content
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        prs = results.polygenic_scores

        if not prs:
            ctk.CTkLabel(
                scroll, text="No polygenic risk data available",
                font=ctk.CTkFont(size=16), text_color="gray50"
            ).pack(pady=50)
            return

        for condition, data in prs.items():
            card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            card.pack(fill="x", pady=8, padx=10)

            header_row = ctk.CTkFrame(card, fg_color="transparent")
            header_row.pack(fill="x", padx=20, pady=(15, 10))

            ctk.CTkLabel(
                header_row, text=data.get('condition', condition.replace('_', ' ').title()),
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(side="left")

            risk = data.get('risk_level', 'Unknown')
            risk_color = "#ef4444" if 'Higher' in risk else "#22c55e" if 'Lower' in risk else "#eab308"
            ctk.CTkLabel(
                header_row, text=risk,
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color=risk_color
            ).pack(side="right")

            # Percentile with progress bar
            percentile = data.get('percentile', 50)
            pct_frame = ctk.CTkFrame(card, fg_color="transparent")
            pct_frame.pack(fill="x", padx=20, pady=5)

            ctk.CTkLabel(pct_frame, text=f"{percentile}th percentile", font=ctk.CTkFont(size=12), text_color="gray60").pack(side="left")

            bar_frame = ctk.CTkFrame(pct_frame, fg_color="transparent")
            bar_frame.pack(side="right", fill="x", expand=True, padx=(20, 0))
            pct_bar = ctk.CTkProgressBar(bar_frame, height=12, corner_radius=6, progress_color=risk_color)
            pct_bar.pack(fill="x")
            pct_bar.set(percentile / 100)

            # Recommendations
            recs = data.get('recommendations', [])
            if recs:
                rec_frame = ctk.CTkFrame(card, fg_color="gray25", corner_radius=6)
                rec_frame.pack(fill="x", padx=20, pady=(5, 0))
                for rec in recs[:3]:
                    ctk.CTkLabel(rec_frame, text=f"  {rec}", font=ctk.CTkFont(size=11), text_color="gray50").pack(anchor="w", padx=10, pady=2)

            ctk.CTkFrame(card, height=12, fg_color="transparent").pack()


# =============================================================================
# CARRIER STATUS FRAME
# =============================================================================

class CarrierStatusFrame(ctk.CTkFrame):
    """
    Comprehensive Carrier Status Screening

    Tests for 11+ genetic conditions:
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

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Get carrier status data
        carrier_data = results.carrier_status if hasattr(results, 'carrier_status') else {}

        # Use the comprehensive CarrierStatusExpandedFrame
        comprehensive_frame = CarrierStatusExpandedFrame(self, carrier_data, dna_data)
        comprehensive_frame.grid(row=0, column=0, sticky="nsew")


# =============================================================================
# BLOOD TYPE FRAME
# =============================================================================

class BloodTypeFrame(ctk.CTkFrame):
    """Blood type genetics display"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Blood Type Genetics",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Your blood group genetics across 7 systems",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

        # Content
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        blood = results.blood_type

        # Main blood type display
        if blood.get('full_type'):
            main_card = ctk.CTkFrame(scroll, fg_color="#dc2626", corner_radius=15)
            main_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                main_card, text="Your Blood Type",
                font=ctk.CTkFont(size=14), text_color="white"
            ).pack(pady=(15, 5))

            ctk.CTkLabel(
                main_card, text=blood.get('full_type', 'Unknown'),
                font=ctk.CTkFont(size=48, weight="bold"), text_color="white"
            ).pack()

            ctk.CTkLabel(
                main_card, text=f"ABO: {blood.get('abo_type', '?')} | Rh: {blood.get('rh_factor', '?')}",
                font=ctk.CTkFont(size=12), text_color="white"
            ).pack(pady=(5, 15))

        # Transfusion notes
        transfusion = blood.get('transfusion_notes', [])
        if transfusion:
            trans_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            trans_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                trans_card, text="Transfusion Compatibility",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for note in transfusion:
                row = ctk.CTkFrame(trans_card, fg_color="transparent")
                row.pack(fill="x", padx=20, pady=3)

                ctk.CTkLabel(
                    row, text="*", font=ctk.CTkFont(size=12), text_color="#3b82f6"
                ).pack(side="left")

                ctk.CTkLabel(
                    row, text=note, font=ctk.CTkFont(size=12)
                ).pack(side="left", padx=10)

            ctk.CTkFrame(trans_card, height=15, fg_color="transparent").pack()

        # Clinical significance
        clinical = blood.get('clinical_significance', [])
        if clinical:
            clin_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            clin_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                clin_card, text="Clinical Significance",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for item in clinical:
                row = ctk.CTkFrame(clin_card, fg_color="gray25", corner_radius=8)
                row.pack(fill="x", padx=20, pady=5)

                ctk.CTkLabel(
                    row, text=f"{item.get('system', '')} - {item.get('finding', '')}",
                    font=ctk.CTkFont(size=13, weight="bold")
                ).pack(anchor="w", padx=15, pady=(10, 5))

                ctk.CTkLabel(
                    row, text=item.get('clinical', ''),
                    font=ctk.CTkFont(size=12), text_color="#22c55e"
                ).pack(anchor="w", padx=15, pady=(0, 10))

            ctk.CTkFrame(clin_card, height=15, fg_color="transparent").pack()

        # Other blood systems
        systems = blood.get('blood_systems', {})
        if systems:
            sys_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            sys_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                sys_card, text="Other Blood Group Systems",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for sys_name, sys_data in systems.items():
                if sys_name not in ['abo_blood_type', 'rh_factor']:
                    sys_row = ctk.CTkFrame(sys_card, fg_color="gray25", corner_radius=8)
                    sys_row.pack(fill="x", padx=20, pady=5)

                    ctk.CTkLabel(
                        sys_row, text=sys_data.get('system', sys_name.replace('_', ' ').title()),
                        font=ctk.CTkFont(size=13, weight="bold")
                    ).pack(anchor="w", padx=15, pady=(10, 5))

                    for marker in sys_data.get('markers_found', [])[:1]:
                        result = marker.get('result', {})
                        status = list(result.values())[0] if isinstance(result, dict) and result else str(result)
                        ctk.CTkLabel(
                            sys_row, text=f"{marker.get('genotype', '')} - {status}",
                            font=ctk.CTkFont(size=11), text_color="gray60"
                        ).pack(anchor="w", padx=15, pady=(0, 10))

            ctk.CTkFrame(sys_card, height=15, fg_color="transparent").pack()


# =============================================================================
# ATHLETIC GENETICS FRAME
# =============================================================================

class AthleticFrame(ctk.CTkFrame):
    """Athletic genetics display"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Athletic Genetics",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Your genetic potential for sports and fitness",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

        # Content
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        athletic = results.athletic_genetics

        # Overall profile card
        profile = athletic.get('overall_profile', 'Mixed')
        power = athletic.get('power_score', 50)
        endurance = athletic.get('endurance_score', 50)

        profile_color = "#ef4444" if 'Power' in profile else "#3b82f6" if 'Endurance' in profile else "#22c55e"

        main_card = ctk.CTkFrame(scroll, fg_color=profile_color, corner_radius=15)
        main_card.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            main_card, text="Your Athletic Profile",
            font=ctk.CTkFont(size=14), text_color="white"
        ).pack(pady=(15, 5))

        ctk.CTkLabel(
            main_card, text=profile,
            font=ctk.CTkFont(size=32, weight="bold"), text_color="white"
        ).pack()

        # Power vs Endurance bars
        bar_frame = ctk.CTkFrame(main_card, fg_color="transparent")
        bar_frame.pack(fill="x", padx=30, pady=15)

        ctk.CTkLabel(
            bar_frame, text=f"Power: {power}%", font=ctk.CTkFont(size=12), text_color="white"
        ).pack(anchor="w")

        power_bar = ctk.CTkProgressBar(bar_frame, width=250, height=12)
        power_bar.pack(fill="x", pady=5)
        power_bar.set(power / 100)

        ctk.CTkLabel(
            bar_frame, text=f"Endurance: {endurance}%", font=ctk.CTkFont(size=12), text_color="white"
        ).pack(anchor="w", pady=(10, 0))

        endurance_bar = ctk.CTkProgressBar(bar_frame, width=250, height=12)
        endurance_bar.pack(fill="x", pady=5)
        endurance_bar.set(endurance / 100)

        # Recommended sports
        sports = athletic.get('primary_sports', [])
        if sports:
            sports_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            sports_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                sports_card, text="Recommended Sports",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            sports_row = ctk.CTkFrame(sports_card, fg_color="transparent")
            sports_row.pack(fill="x", padx=20, pady=(0, 15))

            for sport in sports[:5]:
                sport_chip = ctk.CTkFrame(sports_row, fg_color="gray30", corner_radius=15)
                sport_chip.pack(side="left", padx=5, pady=5)
                ctk.CTkLabel(
                    sport_chip, text=sport, font=ctk.CTkFont(size=11)
                ).pack(padx=12, pady=6)

        # Genes analyzed
        genes = athletic.get('genes_analyzed', [])
        if genes:
            genes_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            genes_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                genes_card, text="Genes Analyzed",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for gene in genes:
                gene_row = ctk.CTkFrame(genes_card, fg_color="gray25", corner_radius=8)
                gene_row.pack(fill="x", padx=20, pady=4)

                left = ctk.CTkFrame(gene_row, fg_color="transparent")
                left.pack(side="left", fill="x", expand=True, padx=15, pady=10)

                ctk.CTkLabel(
                    left, text=gene.get('gene', ''),
                    font=ctk.CTkFont(size=13, weight="bold")
                ).pack(anchor="w")

                ctk.CTkLabel(
                    left, text=gene.get('category', ''),
                    font=ctk.CTkFont(size=11), text_color="gray60"
                ).pack(anchor="w")

                phenotype = gene.get('phenotype', '')
                pheno_color = "#ef4444" if 'Power' in phenotype else "#3b82f6" if 'Endurance' in phenotype else "white"
                ctk.CTkLabel(
                    gene_row, text=phenotype,
                    font=ctk.CTkFont(size=12, weight="bold"), text_color=pheno_color
                ).pack(side="right", padx=15, pady=10)

            ctk.CTkFrame(genes_card, height=15, fg_color="transparent").pack()

        # Training recommendations
        training = athletic.get('training_recommendations', [])
        if training:
            train_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            train_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                train_card, text="Training Recommendations",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for rec in training[:6]:
                row = ctk.CTkFrame(train_card, fg_color="transparent")
                row.pack(fill="x", padx=20, pady=3)

                ctk.CTkLabel(
                    row, text="*", font=ctk.CTkFont(size=12), text_color="#22c55e"
                ).pack(side="left")

                ctk.CTkLabel(
                    row, text=rec, font=ctk.CTkFont(size=12), wraplength=500
                ).pack(side="left", padx=10)

            ctk.CTkFrame(train_card, height=15, fg_color="transparent").pack()

        # Injury risk
        injury = athletic.get('injury_risk', {})
        if injury:
            injury_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            injury_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                injury_card, text="Injury Risk Profile",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for gene, data in injury.items():
                risk = data.get('risk_level', '')
                risk_color = "#ef4444" if 'Higher' in risk else "#eab308" if 'Moderate' in risk else "#22c55e"

                row = ctk.CTkFrame(injury_card, fg_color="gray25", corner_radius=8)
                row.pack(fill="x", padx=20, pady=4)

                ctk.CTkLabel(
                    row, text=gene, font=ctk.CTkFont(size=13, weight="bold")
                ).pack(side="left", padx=15, pady=10)

                ctk.CTkLabel(
                    row, text=risk, font=ctk.CTkFont(size=12, weight="bold"), text_color=risk_color
                ).pack(side="right", padx=15, pady=10)

            ctk.CTkFrame(injury_card, height=15, fg_color="transparent").pack()


# =============================================================================
# ANCIENT DNA FRAME
# =============================================================================

class AncientDNAFrame(ctk.CTkFrame):
    """Ancient DNA connections display - Neanderthal & Denisovan ancestry"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Ancient DNA Connections",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Your Neanderthal and Denisovan ancestry with inherited traits",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

        # Content
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        ancient = results.ancient_dna

        # Neanderthal percentage card
        neanderthal = ancient.get('neanderthal', {})
        neander_pct = neanderthal.get('percentage', 0)

        neander_card = ctk.CTkFrame(scroll, fg_color="#7c3aed", corner_radius=15)
        neander_card.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            neander_card, text="Neanderthal Ancestry",
            font=ctk.CTkFont(size=14), text_color="white"
        ).pack(pady=(15, 5))

        ctk.CTkLabel(
            neander_card, text=f"{neander_pct:.1f}%",
            font=ctk.CTkFont(size=48, weight="bold"), text_color="white"
        ).pack()

        ctk.CTkLabel(
            neander_card, text=f"{neanderthal.get('markers_found', 0)} of {neanderthal.get('markers_tested', 100)} markers detected",
            font=ctk.CTkFont(size=12), text_color="white"
        ).pack(pady=(5, 15))

        # Denisovan percentage card
        denisovan = ancient.get('denisovan', {})
        denis_pct = denisovan.get('percentage', 0)

        denis_card = ctk.CTkFrame(scroll, fg_color="#0891b2", corner_radius=15)
        denis_card.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            denis_card, text="Denisovan Ancestry",
            font=ctk.CTkFont(size=14), text_color="white"
        ).pack(pady=(15, 5))

        ctk.CTkLabel(
            denis_card, text=f"{denis_pct:.2f}%",
            font=ctk.CTkFont(size=36, weight="bold"), text_color="white"
        ).pack()

        ctk.CTkLabel(
            denis_card, text=f"{denisovan.get('markers_found', 0)} of {denisovan.get('markers_tested', 20)} markers detected",
            font=ctk.CTkFont(size=12), text_color="white"
        ).pack(pady=(5, 15))

        # Neanderthal trait categories
        trait_cats = neanderthal.get('trait_categories', {})
        if trait_cats:
            trait_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            trait_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                trait_card, text="Inherited Neanderthal Traits by Category",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for cat_id, cat_data in trait_cats.items():
                cat_row = ctk.CTkFrame(trait_card, fg_color="gray25", corner_radius=8)
                cat_row.pack(fill="x", padx=20, pady=4)

                left = ctk.CTkFrame(cat_row, fg_color="transparent")
                left.pack(side="left", fill="x", expand=True, padx=15, pady=10)

                ctk.CTkLabel(
                    left, text=cat_data.get('name', cat_id.replace('_', ' ').title()),
                    font=ctk.CTkFont(size=13, weight="bold")
                ).pack(anchor="w")

                ctk.CTkLabel(
                    left, text=cat_data.get('description', ''),
                    font=ctk.CTkFont(size=11), text_color="gray60", wraplength=400
                ).pack(anchor="w")

                ctk.CTkLabel(
                    cat_row, text=f"{cat_data.get('traits_inherited', 0)}/{cat_data.get('total_markers', 0)}",
                    font=ctk.CTkFont(size=14, weight="bold"), text_color="#a855f7"
                ).pack(side="right", padx=15, pady=10)

            ctk.CTkFrame(trait_card, height=15, fg_color="transparent").pack()

        # Inherited traits details
        inherited = neanderthal.get('inherited_traits', [])
        if inherited:
            inherited_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            inherited_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                inherited_card, text="Your Inherited Neanderthal Traits",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for trait in inherited[:10]:  # Show top 10
                trait_row = ctk.CTkFrame(inherited_card, fg_color="gray25", corner_radius=8)
                trait_row.pack(fill="x", padx=20, pady=4)

                left = ctk.CTkFrame(trait_row, fg_color="transparent")
                left.pack(side="left", fill="x", expand=True, padx=15, pady=10)

                gene_text = trait.get('gene', 'Unknown')
                copies = trait.get('copies', 1)
                copy_badge = f" ({copies} copies)" if copies > 1 else ""

                ctk.CTkLabel(
                    left, text=f"{gene_text}{copy_badge}",
                    font=ctk.CTkFont(size=13, weight="bold")
                ).pack(anchor="w")

                ctk.CTkLabel(
                    left, text=trait.get('function', ''),
                    font=ctk.CTkFont(size=11), text_color="gray60"
                ).pack(anchor="w")

                ctk.CTkLabel(
                    trait_row, text=trait.get('trait', ''),
                    font=ctk.CTkFont(size=11), text_color="#a855f7", wraplength=200
                ).pack(side="right", padx=15, pady=10)

            if len(inherited) > 10:
                ctk.CTkLabel(
                    inherited_card, text=f"... and {len(inherited) - 10} more traits",
                    font=ctk.CTkFont(size=12), text_color="gray50"
                ).pack(pady=(5, 15))

            ctk.CTkFrame(inherited_card, height=15, fg_color="transparent").pack()

        # Maternal Journey (mtDNA - from mother's mother's mother...)
        maternal_journey = ancient.get('maternal_journey', [])
        if maternal_journey:
            maternal_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            maternal_card.pack(fill="x", pady=10, padx=10)

            maternal_header = ctk.CTkFrame(maternal_card, fg_color="transparent")
            maternal_header.pack(anchor="w", padx=20, pady=(15, 10))

            ctk.CTkLabel(
                maternal_header, text="Maternal Ancestral Journey",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(side="left")

            ctk.CTkLabel(
                maternal_header, text="  (mtDNA - Your mother's mother's mother...)",
                font=ctk.CTkFont(size=12), text_color="#ec4899"
            ).pack(side="left")

            for event in maternal_journey:
                event_row = ctk.CTkFrame(maternal_card, fg_color="gray25", corner_radius=8)
                event_row.pack(fill="x", padx=20, pady=4)

                ctk.CTkLabel(
                    event_row, text=event.get('period', ''),
                    font=ctk.CTkFont(size=12, weight="bold"),
                    text_color="#ec4899", width=140
                ).pack(side="left", padx=15, pady=10)

                right = ctk.CTkFrame(event_row, fg_color="transparent")
                right.pack(side="left", fill="x", expand=True, padx=10, pady=10)

                ctk.CTkLabel(
                    right, text=event.get('event', ''),
                    font=ctk.CTkFont(size=12, weight="bold")
                ).pack(anchor="w")

                ctk.CTkLabel(
                    right, text=event.get('description', ''),
                    font=ctk.CTkFont(size=11), text_color="gray60", wraplength=400
                ).pack(anchor="w")

            ctk.CTkFrame(maternal_card, height=15, fg_color="transparent").pack()

        # Paternal Journey (Y-DNA - from father's father's father...)
        paternal_journey = ancient.get('paternal_journey', [])
        if paternal_journey:
            paternal_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            paternal_card.pack(fill="x", pady=10, padx=10)

            paternal_header = ctk.CTkFrame(paternal_card, fg_color="transparent")
            paternal_header.pack(anchor="w", padx=20, pady=(15, 10))

            ctk.CTkLabel(
                paternal_header, text="Paternal Ancestral Journey",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(side="left")

            ctk.CTkLabel(
                paternal_header, text="  (Y-DNA - Your father's father's father...)",
                font=ctk.CTkFont(size=12), text_color="#3b82f6"
            ).pack(side="left")

            for event in paternal_journey:
                event_row = ctk.CTkFrame(paternal_card, fg_color="gray25", corner_radius=8)
                event_row.pack(fill="x", padx=20, pady=4)

                ctk.CTkLabel(
                    event_row, text=event.get('period', ''),
                    font=ctk.CTkFont(size=12, weight="bold"),
                    text_color="#3b82f6", width=140
                ).pack(side="left", padx=15, pady=10)

                right = ctk.CTkFrame(event_row, fg_color="transparent")
                right.pack(side="left", fill="x", expand=True, padx=10, pady=10)

                ctk.CTkLabel(
                    right, text=event.get('event', ''),
                    font=ctk.CTkFont(size=12, weight="bold")
                ).pack(anchor="w")

                ctk.CTkLabel(
                    right, text=event.get('description', ''),
                    font=ctk.CTkFont(size=11), text_color="gray60", wraplength=400
                ).pack(anchor="w")

            ctk.CTkFrame(paternal_card, height=15, fg_color="transparent").pack()

        # Combined story if available (fallback)
        story = ancient.get('your_story', [])
        if story and not maternal_journey and not paternal_journey:
            story_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            story_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                story_card, text="Your Ancestral Journey",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for event in story:
                event_row = ctk.CTkFrame(story_card, fg_color="gray25", corner_radius=8)
                event_row.pack(fill="x", padx=20, pady=4)

                ctk.CTkLabel(
                    event_row, text=event.get('period', ''),
                    font=ctk.CTkFont(size=12, weight="bold"),
                    text_color="#3b82f6", width=140
                ).pack(side="left", padx=15, pady=10)

                right = ctk.CTkFrame(event_row, fg_color="transparent")
                right.pack(side="left", fill="x", expand=True, padx=10, pady=10)

                ctk.CTkLabel(
                    right, text=event.get('event', ''),
                    font=ctk.CTkFont(size=12, weight="bold")
                ).pack(anchor="w")

                ctk.CTkLabel(
                    right, text=event.get('description', ''),
                    font=ctk.CTkFont(size=11), text_color="gray60", wraplength=400
                ).pack(anchor="w")

            ctk.CTkFrame(story_card, height=15, fg_color="transparent").pack()

        # Human migration timeline
        timeline = ancient.get('timeline', [])
        if timeline:
            time_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            time_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                time_card, text="Human Migration Timeline",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for event in timeline[:8]:  # Show first 8
                row = ctk.CTkFrame(time_card, fg_color="gray25", corner_radius=8)
                row.pack(fill="x", padx=20, pady=3)

                period = event.get('years_ago', event.get('period', ''))
                if isinstance(period, int):
                    period = f"{period:,} years ago"

                ctk.CTkLabel(
                    row, text=str(period),
                    font=ctk.CTkFont(size=11, weight="bold"),
                    text_color="#22c55e", width=130
                ).pack(side="left", padx=10, pady=8)

                ctk.CTkLabel(
                    row, text=event.get('event', event.get('description', '')),
                    font=ctk.CTkFont(size=11), wraplength=400
                ).pack(side="left", padx=10, pady=8)

            ctk.CTkFrame(time_card, height=15, fg_color="transparent").pack()


# =============================================================================
# FACIAL FEATURES FRAME
# =============================================================================

class FacialFeaturesFrame(ctk.CTkFrame):
    """Facial feature prediction display"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Facial Feature Prediction",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Your genetic facial characteristics",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        facial = results.facial_features
        features = facial.get('features', {})

        if features:
            for feature_id, feature_data in features.items():
                card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
                card.pack(fill="x", pady=5, padx=10)

                left = ctk.CTkFrame(card, fg_color="transparent")
                left.pack(side="left", fill="x", expand=True, padx=20, pady=15)

                ctk.CTkLabel(
                    left, text=feature_data.get('name', feature_id),
                    font=ctk.CTkFont(size=14, weight="bold")
                ).pack(anchor="w")

                ctk.CTkLabel(
                    left, text=f"Gene: {feature_data.get('gene', 'Unknown')} | {feature_data.get('genotype', '')}",
                    font=ctk.CTkFont(size=11), text_color="gray60"
                ).pack(anchor="w")

                ctk.CTkLabel(
                    card, text=feature_data.get('prediction', ''),
                    font=ctk.CTkFont(size=13, weight="bold"), text_color="#a855f7"
                ).pack(side="right", padx=20, pady=15)
        else:
            ctk.CTkLabel(
                scroll, text="Limited facial feature data in your DNA file",
                font=ctk.CTkFont(size=14), text_color="gray50"
            ).pack(pady=50)


# =============================================================================
# CHRONOTYPE FRAME
# =============================================================================

class ChronotypeFrame(ctk.CTkFrame):
    """Sleep and chronotype display"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Sleep & Chronotype",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        chrono = results.chronotype
        chronotype = chrono.get('chronotype', 'Unknown')

        # Main chronotype card
        color = "#f59e0b" if 'Morning' in chronotype else "#6366f1" if 'Night' in chronotype else "#22c55e"
        main_card = ctk.CTkFrame(scroll, fg_color=color, corner_radius=15)
        main_card.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            main_card, text="Your Chronotype",
            font=ctk.CTkFont(size=14), text_color="white"
        ).pack(pady=(15, 5))

        ctk.CTkLabel(
            main_card, text=chronotype or "Intermediate",
            font=ctk.CTkFont(size=36, weight="bold"), text_color="white"
        ).pack()

        ctk.CTkLabel(
            main_card, text=f"Ideal wake: {chrono.get('ideal_wake_time', '7:00 AM')} | Sleep: {chrono.get('ideal_sleep_time', '11:00 PM')}",
            font=ctk.CTkFont(size=12), text_color="white"
        ).pack(pady=(5, 15))

        # Sleep need
        need_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
        need_card.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            need_card, text=f"Your sleep need: {chrono.get('sleep_duration_need', 7.5):.1f} hours",
            font=ctk.CTkFont(size=16, weight="bold")
        ).pack(pady=15)

        # Recommendations
        recs = chrono.get('recommendations', [])
        if recs:
            rec_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            rec_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                rec_card, text="Recommendations",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for rec in recs:
                ctk.CTkLabel(
                    rec_card, text=f"* {rec}",
                    font=ctk.CTkFont(size=12), wraplength=500
                ).pack(anchor="w", padx=20, pady=3)

            ctk.CTkFrame(rec_card, height=15, fg_color="transparent").pack()


# =============================================================================
# PAIN SENSITIVITY FRAME
# =============================================================================

class PainFrame(ctk.CTkFrame):
    """Pain sensitivity display"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Pain Sensitivity",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        pain = results.pain_sensitivity
        sensitivity = pain.get('overall_sensitivity', 'Average')

        color = "#ef4444" if 'High' in sensitivity else "#22c55e" if 'Low' in sensitivity else "#3b82f6"

        main_card = ctk.CTkFrame(scroll, fg_color=color, corner_radius=15)
        main_card.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            main_card, text="Pain Sensitivity",
            font=ctk.CTkFont(size=14), text_color="white"
        ).pack(pady=(15, 5))

        ctk.CTkLabel(
            main_card, text=sensitivity,
            font=ctk.CTkFont(size=28, weight="bold"), text_color="white"
        ).pack()

        ctk.CTkLabel(
            main_card, text=f"Threshold: {pain.get('threshold', 'Medium')} | Migraine risk: {pain.get('migraine_risk', 'Average')}",
            font=ctk.CTkFont(size=12), text_color="white"
        ).pack(pady=(5, 15))

        # Drug response
        drug_resp = pain.get('drug_response', {})
        if drug_resp:
            drug_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            drug_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                drug_card, text="Drug Response",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for gene, response in drug_resp.items():
                ctk.CTkLabel(
                    drug_card, text=f"{gene}: {response}",
                    font=ctk.CTkFont(size=12)
                ).pack(anchor="w", padx=20, pady=3)

            ctk.CTkFrame(drug_card, height=15, fg_color="transparent").pack()


# =============================================================================
# ADDICTION RISK FRAME
# =============================================================================

class AddictionFrame(ctk.CTkFrame):
    """Addiction risk display with visual bars"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(header, text="Addiction Susceptibility", font=ctk.CTkFont(size=28, weight="bold")).pack(anchor="w")
        ctk.CTkLabel(header, text="Genetic factors affecting addiction risk", font=ctk.CTkFont(size=14), text_color="gray60").pack(anchor="w")

        # Warning
        warning = ctk.CTkFrame(header, fg_color="#7f1d1d", corner_radius=8)
        warning.pack(fill="x", pady=10)
        ctk.CTkLabel(warning, text="Genetics is only one factor. Environment, behavior, and choices matter more.", font=ctk.CTkFont(size=11), text_color="#fca5a5").pack(padx=15, pady=8)

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        addiction = results.addiction_risk
        overall = addiction.get('overall_risk', 'Average')

        # Overall risk card
        overall_card = ctk.CTkFrame(scroll, fg_color="#1e3a5f", corner_radius=15)
        overall_card.pack(fill="x", pady=10, padx=10)
        ctk.CTkLabel(overall_card, text="OVERALL GENETIC RISK", font=ctk.CTkFont(size=11), text_color="gray60").pack(pady=(15, 5))
        overall_color = "#ef4444" if 'Elevated' in overall else "#22c55e" if 'Lower' in overall else "#eab308"
        ctk.CTkLabel(overall_card, text=overall, font=ctk.CTkFont(size=24, weight="bold"), text_color=overall_color).pack(pady=(0, 15))

        categories = [
            ('alcohol', 'Alcohol', 'ADH1B/ALDH2 genes affect alcohol metabolism'),
            ('nicotine', 'Nicotine', 'CHRNA5 affects nicotine receptor sensitivity'),
            ('dopamine_reward', 'Dopamine Reward', 'DRD2 affects reward sensitivity'),
            ('gambling', 'Gambling', 'Impulse control genetics'),
            ('cannabis', 'Cannabis', 'CNR1 cannabinoid receptor variants')
        ]

        for cat_key, cat_name, cat_desc in categories:
            if cat_key in addiction and isinstance(addiction[cat_key], dict):
                data = addiction[cat_key]
                risk = data.get('risk', data.get('profile', 'Unknown'))
                score = data.get('score', 50)

                color = "#ef4444" if score >= 60 else "#22c55e" if score <= 35 else "#eab308"

                card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
                card.pack(fill="x", pady=6, padx=10)

                top_row = ctk.CTkFrame(card, fg_color="transparent")
                top_row.pack(fill="x", padx=20, pady=(12, 5))

                ctk.CTkLabel(top_row, text=cat_name, font=ctk.CTkFont(size=15, weight="bold")).pack(side="left")
                ctk.CTkLabel(top_row, text=f"{score:.0f}", font=ctk.CTkFont(size=18, weight="bold"), text_color=color).pack(side="right")

                # Progress bar
                bar_frame = ctk.CTkFrame(card, fg_color="transparent")
                bar_frame.pack(fill="x", padx=20, pady=5)
                bar = ctk.CTkProgressBar(bar_frame, height=14, corner_radius=7, progress_color=color)
                bar.pack(fill="x")
                bar.set(score / 100)

                info_row = ctk.CTkFrame(card, fg_color="transparent")
                info_row.pack(fill="x", padx=20, pady=(0, 12))
                ctk.CTkLabel(info_row, text=cat_desc, font=ctk.CTkFont(size=11), text_color="gray60").pack(side="left")
                ctk.CTkLabel(info_row, text=risk, font=ctk.CTkFont(size=12, weight="bold"), text_color=color).pack(side="right")

        # Recommendations
        recs = addiction.get('recommendations', [])
        if recs:
            rec_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            rec_card.pack(fill="x", pady=10, padx=10)
            ctk.CTkLabel(rec_card, text="Recommendations", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=20, pady=(12, 8))
            for rec in recs:
                ctk.CTkLabel(rec_card, text=f"  {rec}", font=ctk.CTkFont(size=11), text_color="gray60").pack(anchor="w", padx=20, pady=2)
            ctk.CTkFrame(rec_card, height=10, fg_color="transparent").pack()


# =============================================================================
# MENTAL TRAITS FRAME
# =============================================================================

class MentalTraitsFrame(ctk.CTkFrame):
    """Mental traits / stress response display"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Mental Traits & Stress Response",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        mental = results.mental_traits
        stress_type = mental.get('stress_type', 'Unknown')

        color = "#ef4444" if 'Warrior' in stress_type else "#3b82f6" if 'Worrier' in stress_type else "#22c55e"

        main_card = ctk.CTkFrame(scroll, fg_color=color, corner_radius=15)
        main_card.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            main_card, text="Your Stress Type",
            font=ctk.CTkFont(size=14), text_color="white"
        ).pack(pady=(15, 5))

        ctk.CTkLabel(
            main_card, text=stress_type or "Balanced",
            font=ctk.CTkFont(size=42, weight="bold"), text_color="white"
        ).pack()

        ctk.CTkLabel(
            main_card, text=f"Anxiety tendency: {mental.get('anxiety_tendency', 'Average')}",
            font=ctk.CTkFont(size=12), text_color="white"
        ).pack(pady=(5, 15))

        # Strengths
        strengths = mental.get('strengths', [])
        if strengths:
            str_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            str_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                str_card, text="Your Strengths",
                font=ctk.CTkFont(size=16, weight="bold")
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for s in strengths:
                ctk.CTkLabel(
                    str_card, text=f"+ {s}",
                    font=ctk.CTkFont(size=12), text_color="#22c55e"
                ).pack(anchor="w", padx=20, pady=3)

            ctk.CTkFrame(str_card, height=15, fg_color="transparent").pack()


# =============================================================================
# SENSORY TRAITS FRAME (Comprehensive)
# =============================================================================

class SensoryFrame(ctk.CTkFrame):
    """
    Comprehensive Sensory Genetics Display

    Features:
    - Bitter taste (TAS2R38 supertaster)
    - Sweet taste (TAS1R2/TAS1R3)
    - Umami taste (TAS1R1)
    - Cilantro soap gene (OR6A2)
    - Asparagus smell (OR2M7)
    - Color vision / blindness
    - Smell sensitivity
    - Specific anosmias
    - Touch sensitivity (PIEZO2)
    - Temperature sensitivity (TRP channels)
    - Body odor / earwax (ABCC11)
    """

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Get comprehensive sensory data
        sensory = results.sensory_traits

        # Use the comprehensive SensoryGeneticsFrame
        comprehensive_frame = SensoryGeneticsFrame(self, sensory, dna_data)
        comprehensive_frame.grid(row=0, column=0, sticky="nsew")


# =============================================================================
# BEHAVIORAL GENETICS FRAME (Comprehensive)
# =============================================================================

class BehavioralFrame(ctk.CTkFrame):
    """
    Comprehensive Behavioral & Cognitive Genetics Display

    Features:
    - Empathy levels (OXTR)
    - Novelty/risk seeking (DRD4, DRD2)
    - Warrior gene (MAOA)
    - Stress resilience (CRHR1, FKBP5)
    - Depression susceptibility (SLC6A4)
    - Social bonding (AVPR1A)
    - Memory & learning (KIBRA, BDNF, COMT)
    - Attention & impulsivity (DAT1, ADRA2A)
    """

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Get comprehensive behavioral genetics data
        behavioral = results.behavioral_genetics

        # Use the comprehensive BehavioralGeneticsFrame
        comprehensive_frame = BehavioralGeneticsFrame(self, behavioral, dna_data)
        comprehensive_frame.grid(row=0, column=0, sticky="nsew")


# =============================================================================
# SLEEP GENETICS FRAME (Comprehensive)
# =============================================================================

class SleepFrame(ctk.CTkFrame):
    """
    Comprehensive Sleep & Circadian Genetics Display

    Features:
    - Chronotype (morning lark vs night owl)
    - Sleep duration need
    - Sleep quality genetics
    - Insomnia susceptibility
    - Deep sleep (slow-wave sleep)
    - REM sleep patterns
    - Sleep latency
    - Shift work tolerance
    - Delayed sleep phase syndrome risk
    - Caffeine and sleep interaction
    """

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Get comprehensive sleep genetics data
        sleep = results.sleep_genetics

        # Use the comprehensive SleepGeneticsFrame
        comprehensive_frame = SleepGeneticsFrame(self, sleep, dna_data)
        comprehensive_frame.grid(row=0, column=0, sticky="nsew")


# =============================================================================
# PHYSICAL TRAITS EXPANDED FRAME
# =============================================================================

class PhysicalExpandedFrame(ctk.CTkFrame):
    """
    Expanded Physical Traits Display

    Features:
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

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Get expanded physical traits data
        physical_exp = results.physical_traits_expanded

        # Use the comprehensive PhysicalTraitsExpandedFrame
        comprehensive_frame = PhysicalTraitsExpandedFrame(self, physical_exp, dna_data)
        comprehensive_frame.grid(row=0, column=0, sticky="nsew")


# =============================================================================
# SPORTS GENETICS FRAME
# =============================================================================

class SportsFrame(ctk.CTkFrame):
    """
    Sports & Injury Genetics Display

    Features:
    - Muscle fiber composition (ACTN3)
    - VO2 max potential
    - ACL injury risk
    - Tendon injury risk
    - Muscle cramping
    - Recovery speed
    - Fatigue resistance
    - Blood pressure response
    - Lactate clearance
    """

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Get sports genetics data
        sports = results.sports_genetics

        # Use the comprehensive SportsGeneticsFrame
        comprehensive_frame = SportsGeneticsFrame(self, sports, dna_data)
        comprehensive_frame.grid(row=0, column=0, sticky="nsew")


# =============================================================================
# REPRODUCTION & FERTILITY FRAME
# =============================================================================

class ReproductionFrame(ctk.CTkFrame):
    """
    Reproduction & Fertility Genetics Display

    Features:
    - Male fertility factors
    - Female fertility factors
    - Menopause timing
    - Twin probability
    - Endometriosis risk
    - PCOS risk
    - Testosterone levels
    - Estrogen metabolism
    - Pregnancy complications
    """

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Get reproduction genetics data
        reproduction = results.reproduction_genetics

        # Use the comprehensive ReproductionGeneticsFrame
        comprehensive_frame = ReproductionGeneticsFrame(self, reproduction)
        comprehensive_frame.grid(row=0, column=0, sticky="nsew")


# =============================================================================
# IMMUNE SYSTEM DEEP DIVE FRAME
# =============================================================================

class ImmuneDeepFrame(ctk.CTkFrame):
    """
    Immune System Deep Dive Display

    Features:
    - HLA type analysis
    - Cytokine response
    - Inflammatory markers
    - Allergy susceptibility
    - Celiac disease risk
    - Lupus (SLE) risk
    - Multiple sclerosis risk
    - Rheumatoid arthritis risk
    - Psoriasis risk
    - IBD/Crohn's disease risk
    """

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Get immune deep genetics data
        immune_deep = results.immune_deep_genetics

        # Use the comprehensive ImmuneDeepGeneticsFrame
        comprehensive_frame = ImmuneDeepGeneticsFrame(self, immune_deep)
        comprehensive_frame.grid(row=0, column=0, sticky="nsew")


# =============================================================================
# NUTRITION & METABOLISM FRAME
# =============================================================================

class NutritionMetabFrame(ctk.CTkFrame):
    """
    Nutrition & Metabolism Genetics Display

    Features:
    - Vitamin A metabolism
    - Vitamin B12 metabolism
    - Vitamin C & E metabolism
    - Omega-3 fatty acid metabolism
    - Saturated fat response
    - Carbohydrate metabolism
    - Protein & satiety
    - Sodium sensitivity
    - Alcohol metabolism
    """

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Get nutrition metabolism data
        nutrition = results.nutrition_metabolism

        # Use the comprehensive NutritionMetabolismFrame
        comprehensive_frame = NutritionMetabolismFrame(self, nutrition)
        comprehensive_frame.grid(row=0, column=0, sticky="nsew")


# =============================================================================
# ANCIENT DNA & HISTORY FRAME
# =============================================================================

class AncientHistoryFrame(ctk.CTkFrame):
    """
    Ancient DNA & Historical Genetics Display

    Features:
    - Neanderthal ancestry
    - Denisovan ancestry
    - Ancient farmer ancestry
    - Hunter-gatherer ancestry
    - Steppe/Yamnaya ancestry
    - Pathogen resistance history
    - Pigmentation evolution
    - Migration markers
    """

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Get ancient DNA history data
        ancient_history = results.ancient_dna_history

        # Use the comprehensive AncientDNAHistoryFrame
        comprehensive_frame = AncientDNAHistoryFrame(self, ancient_history)
        comprehensive_frame.grid(row=0, column=0, sticky="nsew")


# =============================================================================
# LONGEVITY GENETICS EXPANDED FRAME
# =============================================================================

class LongevityExpFrame(ctk.CTkFrame):
    """
    Longevity & Aging Genetics Display

    Features:
    - Telomere length genetics
    - Sirtuin pathway
    - FOXO longevity genes
    - IGF-1/growth hormone pathway
    - Autophagy genetics
    - Mitochondrial function
    - Inflammaging markers
    - Klotho anti-aging hormone
    """

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        longevity_data = results.longevity_genetics
        comprehensive_frame = LongevityGeneticsFrame(self, longevity_data)
        comprehensive_frame.grid(row=0, column=0, sticky="nsew")


# =============================================================================
# PHARMACOGENOMICS EXPANDED FRAME
# =============================================================================

class PharmacoExpFrame(ctk.CTkFrame):
    """
    Pharmacogenomics - Drug Response Genetics Display

    Features:
    - CYP2D6, CYP2C19, CYP2C9 metabolism
    - Warfarin sensitivity (VKORC1)
    - Statin myopathy risk (SLCO1B1)
    - Thiopurine/fluoropyrimidine toxicity
    - Opioid response
    - Caffeine metabolism
    - MTHFR/folate metabolism
    """

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        pharmaco_data = results.pharmacogenomics_detailed
        comprehensive_frame = PharmacogenomicsDetailedFrame(self, pharmaco_data)
        comprehensive_frame.grid(row=0, column=0, sticky="nsew")


# =============================================================================
# MENTAL HEALTH GENETICS FRAME
# =============================================================================

class MentalHealthFrame(ctk.CTkFrame):
    """
    Mental Health Genetics Display

    Features:
    - Depression risk factors
    - Anxiety vulnerability
    - ADHD genetics
    - Bipolar disorder risk
    - Schizophrenia risk
    - PTSD vulnerability
    - Addiction vulnerability
    - Cognitive profile (warrior/worrier)
    """

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        mental_health_data = results.mental_health_genetics
        comprehensive_frame = MentalHealthGeneticsFrame(self, mental_health_data)
        comprehensive_frame.grid(row=0, column=0, sticky="nsew")


# =============================================================================
# CANCER RISK GENETICS FRAME
# =============================================================================

class CancerRiskFrame(ctk.CTkFrame):
    """
    Cancer Risk Genetics Display

    Features:
    - Breast cancer risk (common variants)
    - Colorectal cancer risk
    - Prostate cancer risk
    - Lung cancer risk
    - Melanoma/skin cancer risk
    - Thyroid cancer risk
    - Pancreatic cancer risk
    Note: Does not include rare pathogenic mutations
    """

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        cancer_data = results.cancer_risk_genetics
        comprehensive_frame = CancerRiskGeneticsFrame(self, cancer_data)
        comprehensive_frame.grid(row=0, column=0, sticky="nsew")


# =============================================================================
# CARDIOVASCULAR GENETICS FRAME
# =============================================================================

class CardiovascFrame(ctk.CTkFrame):
    """
    Cardiovascular Genetics Display

    Features:
    - Coronary artery disease risk
    - LDL/HDL cholesterol genetics
    - Triglyceride genetics
    - Blood pressure/hypertension
    - Stroke risk
    - Atrial fibrillation risk
    - Clotting/thrombosis (Factor V Leiden, etc.)
    """

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        cardio_data = results.cardiovascular_genetics
        comprehensive_frame = CardiovascularGeneticsFrame(self, cardio_data)
        comprehensive_frame.grid(row=0, column=0, sticky="nsew")


# =============================================================================
# SKIN & DERMATOLOGY GENETICS FRAME
# =============================================================================

class SkinDermFrame(ctk.CTkFrame):
    """
    Skin & Dermatology genetics display with:
    - Skin aging genetics
    - UV sensitivity and sun damage
    - Eczema/atopic dermatitis risk
    - Psoriasis risk
    - Rosacea risk
    - Acne tendency
    - Skin elasticity and stretch marks
    - Vitamin D synthesis
    """

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        skin_data = results.skin_dermatology
        comprehensive_frame = SkinDermatologyFrame(self, skin_data)
        comprehensive_frame.grid(row=0, column=0, sticky="nsew")


# =============================================================================
# DEEP ANCESTRY GENETICS FRAME
# =============================================================================

class DeepAncestryWrapperFrame(ctk.CTkFrame):
    """
    Deep Ancestry genetics display with:
    - European regional markers
    - African regional markers
    - East Asian markers
    - South Asian markers
    - Native American markers
    - Middle Eastern/North African markers
    - Jewish ancestry markers
    - Ancient migration patterns
    - Isolated population markers
    """

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        ancestry_data = results.deep_ancestry
        comprehensive_frame = DeepAncestryFrame(self, ancestry_data)
        comprehensive_frame.grid(row=0, column=0, sticky="nsew")


# =============================================================================
# ANCIENT POPULATION MATCH FRAME
# =============================================================================

class AncientPopulationFrame(ctk.CTkFrame):
    """Ancient population matching display"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Ancient Population Match",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="How your DNA compares to ancient peoples",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        ancient = results.ancient_population_match
        matches = ancient.get('matches', [])

        if matches:
            for i, match in enumerate(matches):
                color = "#7c3aed" if i == 0 else "gray20"

                card = ctk.CTkFrame(scroll, fg_color=color, corner_radius=10)
                card.pack(fill="x", pady=8, padx=10)

                text_color = "white" if i == 0 else None

                ctk.CTkLabel(
                    card, text=match.get('name', ''),
                    font=ctk.CTkFont(size=16, weight="bold"), text_color=text_color
                ).pack(anchor="w", padx=20, pady=(15, 5))

                ctk.CTkLabel(
                    card, text=f"{match.get('time_period', '')} | {match.get('location', '')}",
                    font=ctk.CTkFont(size=12), text_color=text_color or "gray60"
                ).pack(anchor="w", padx=20)

                ctk.CTkLabel(
                    card, text=f"Match: {match.get('score', 0)}%",
                    font=ctk.CTkFont(size=14, weight="bold"), text_color=text_color or "#22c55e"
                ).pack(anchor="w", padx=20, pady=(5, 15))
        else:
            ctk.CTkLabel(
                scroll, text="Limited ancient population data available",
                font=ctk.CTkFont(size=14), text_color="gray50"
            ).pack(pady=50)


# =============================================================================
# PERSONALIZED PLAN FRAME
# =============================================================================

class PersonalizedPlanFrame(ctk.CTkFrame):
    """Personalized supplement/diet/exercise plan display"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Your Personalized Plan",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Supplements, diet, and exercise based on YOUR genetics",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        plan = results.personalized_plan

        # Supplements
        supplements = plan.get('supplements', [])
        if supplements:
            supp_card = ctk.CTkFrame(scroll, fg_color="#059669", corner_radius=10)
            supp_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                supp_card, text="Recommended Supplements",
                font=ctk.CTkFont(size=18, weight="bold"), text_color="white"
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for supp in supplements:
                row = ctk.CTkFrame(supp_card, fg_color="white", corner_radius=8)
                row.pack(fill="x", padx=20, pady=5)

                priority = supp.get('priority', 'low')
                priority_color = "#ef4444" if priority == 'high' else "#f59e0b" if priority == 'medium' else "#22c55e"

                ctk.CTkLabel(
                    row, text=supp.get('supplement', ''),
                    font=ctk.CTkFont(size=13, weight="bold"), text_color="gray20"
                ).pack(anchor="w", padx=15, pady=(10, 2))

                ctk.CTkLabel(
                    row, text=supp.get('reason', ''),
                    font=ctk.CTkFont(size=11), text_color="gray50"
                ).pack(anchor="w", padx=15)

                ctk.CTkLabel(
                    row, text=f"Dose: {supp.get('dose', '')} | Priority: {priority.upper()}",
                    font=ctk.CTkFont(size=10), text_color=priority_color
                ).pack(anchor="w", padx=15, pady=(0, 10))

            ctk.CTkFrame(supp_card, height=15, fg_color="transparent").pack()

        # Diet
        diet = plan.get('diet', {})
        diet_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
        diet_card.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            diet_card, text=f"Diet Type: {diet.get('type', 'Balanced')}",
            font=ctk.CTkFont(size=16, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        for rec in diet.get('recommendations', [])[:3]:
            ctk.CTkLabel(
                diet_card, text=f"* {rec}",
                font=ctk.CTkFont(size=12), wraplength=500
            ).pack(anchor="w", padx=20, pady=2)

        foods_inc = diet.get('foods_to_increase', [])
        if foods_inc:
            ctk.CTkLabel(
                diet_card, text="Increase: " + ", ".join(foods_inc[:5]),
                font=ctk.CTkFont(size=11), text_color="#22c55e"
            ).pack(anchor="w", padx=20, pady=(10, 0))

        foods_lim = diet.get('foods_to_limit', [])
        if foods_lim:
            ctk.CTkLabel(
                diet_card, text="Limit: " + ", ".join(foods_lim[:5]),
                font=ctk.CTkFont(size=11), text_color="#ef4444"
            ).pack(anchor="w", padx=20, pady=(5, 15))

        # Exercise
        exercise = plan.get('exercise', {})
        ex_card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
        ex_card.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            ex_card, text=f"Exercise Type: {exercise.get('type', 'Mixed')}",
            font=ctk.CTkFont(size=16, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        activities = exercise.get('optimal_activities', [])
        if activities:
            ctk.CTkLabel(
                ex_card, text="Best for you: " + ", ".join(activities[:5]),
                font=ctk.CTkFont(size=12), text_color="#3b82f6"
            ).pack(anchor="w", padx=20, pady=5)

        for rec in exercise.get('recommendations', [])[:3]:
            ctk.CTkLabel(
                ex_card, text=f"* {rec}",
                font=ctk.CTkFont(size=12), wraplength=500
            ).pack(anchor="w", padx=20, pady=2)

        ctk.CTkFrame(ex_card, height=15, fg_color="transparent").pack()

        # Lifestyle recommendations
        lifestyle = plan.get('lifestyle', [])
        if lifestyle:
            life_card = ctk.CTkFrame(scroll, fg_color="#1e3a5f", corner_radius=10)
            life_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                life_card, text="Lifestyle Recommendations",
                font=ctk.CTkFont(size=16, weight="bold"), text_color="white"
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for rec in lifestyle[:5]:
                ctk.CTkLabel(
                    life_card, text=f"* {rec}",
                    font=ctk.CTkFont(size=12), text_color="#93c5fd", wraplength=500
                ).pack(anchor="w", padx=20, pady=2)

            ctk.CTkFrame(life_card, height=15, fg_color="transparent").pack()

        # Screening recommendations
        screening = plan.get('screening', [])
        if screening:
            screen_card = ctk.CTkFrame(scroll, fg_color="#7c2d12", corner_radius=10)
            screen_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                screen_card, text="Recommended Screenings",
                font=ctk.CTkFont(size=16, weight="bold"), text_color="white"
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for rec in screening[:5]:
                ctk.CTkLabel(
                    screen_card, text=f"* {rec}",
                    font=ctk.CTkFont(size=12), text_color="#fdba74", wraplength=500
                ).pack(anchor="w", padx=20, pady=2)

            ctk.CTkFrame(screen_card, height=15, fg_color="transparent").pack()

        # Things to avoid
        avoid = plan.get('avoid', [])
        if avoid:
            avoid_card = ctk.CTkFrame(scroll, fg_color="#7f1d1d", corner_radius=10)
            avoid_card.pack(fill="x", pady=10, padx=10)

            ctk.CTkLabel(
                avoid_card, text="Things to Avoid/Limit",
                font=ctk.CTkFont(size=16, weight="bold"), text_color="white"
            ).pack(anchor="w", padx=20, pady=(15, 10))

            for item in avoid[:5]:
                ctk.CTkLabel(
                    avoid_card, text=f"* {item}",
                    font=ctk.CTkFont(size=12), text_color="#fca5a5", wraplength=500
                ).pack(anchor="w", padx=20, pady=2)

            ctk.CTkFrame(avoid_card, height=15, fg_color="transparent").pack()


# =============================================================================
# EXPORT FRAME
# =============================================================================

class ExportFrame(ctk.CTkFrame):
    """Export results display"""

    def __init__(self, parent, results, dna_data):
        super().__init__(parent, fg_color="transparent")
        self.results = results
        self.dna_data = dna_data

        self.grid_columnconfigure(0, weight=1)

        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Export Results",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Save your analysis results",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

        # Export options
        options = ctk.CTkFrame(self, fg_color="gray20", corner_radius=15)
        options.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

        ctk.CTkButton(
            options, text="Export as Text Report",
            command=self.export_text,
            font=ctk.CTkFont(size=14),
            height=45, width=300
        ).pack(pady=20)

        ctk.CTkButton(
            options, text="Export as JSON",
            command=self.export_json,
            font=ctk.CTkFont(size=14),
            height=45, width=300
        ).pack(pady=20)

        ctk.CTkButton(
            options, text="Export as PDF Report",
            command=self.export_pdf,
            font=ctk.CTkFont(size=14),
            height=45, width=300,
            fg_color="#2563eb"
        ).pack(pady=20)

        # Summary
        summary = results.summary
        ctk.CTkLabel(
            options, text=f"Analysis includes: {summary.get('total_snps_analyzed', 0):,} SNPs",
            font=ctk.CTkFont(size=12), text_color="gray60"
        ).pack(pady=(10, 20))

    def export_text(self):
        """Export as comprehensive text file"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")]
        )
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write("=" * 70 + "\n")
                    f.write("              COMPREHENSIVE DNA ANALYSIS REPORT\n")
                    f.write("=" * 70 + "\n")
                    f.write(f"Generated: {self.results.summary.get('analysis_date', 'N/A')}\n")
                    f.write(f"SNPs Analyzed: {self.results.summary.get('total_snps_analyzed', 0):,}\n\n")

                    # ANCESTRY
                    f.write("\n" + "=" * 70 + "\n")
                    f.write("ANCESTRY COMPOSITION\n")
                    f.write("=" * 70 + "\n")
                    f.write(f"Continental markers: {self.results.ancestry.get('markers_continental', 'N/A'):,}\n")
                    f.write(f"Sub-population markers: {self.results.ancestry.get('markers_subpop', 'N/A')}\n\n")
                    for pop, pct in sorted(self.results.ancestry.get('composition', {}).items(), key=lambda x: x[1], reverse=True):
                        f.write(f"  {pop.replace('_', ' ')}: {pct:.1f}%\n")

                    # PHYSICAL TRAITS
                    f.write("\n" + "=" * 70 + "\n")
                    f.write("PHYSICAL TRAITS (25 traits analyzed)\n")
                    f.write("=" * 70 + "\n")
                    for trait_name, data in self.results.physical_traits.items():
                        f.write(f"\n{data.get('trait_name', trait_name)}:\n")
                        f.write(f"  Prediction: {data.get('prediction', 'N/A')}\n")
                        f.write(f"  Confidence: {data.get('confidence', 0)*100:.0f}%\n")
                        if data.get('population_comparison'):
                            f.write(f"  Population: {data['population_comparison']}\n")

                    # HEALTH TRAITS
                    f.write("\n" + "=" * 70 + "\n")
                    f.write("HEALTH TRAITS (22 conditions analyzed)\n")
                    f.write("=" * 70 + "\n")
                    for trait_name, data in self.results.health_traits.items():
                        f.write(f"\n{data.get('trait_name', trait_name)}:\n")
                        f.write(f"  Status: {data.get('status', 'N/A')}\n")
                        if data.get('action'):
                            f.write(f"  Action: {data['action']}\n")

                    # CARRIER STATUS
                    if hasattr(self.results, 'carrier_status'):
                        f.write("\n" + "=" * 70 + "\n")
                        f.write("CARRIER STATUS (10 conditions screened)\n")
                        f.write("=" * 70 + "\n")
                        cs = self.results.carrier_status
                        if cs.get('carriers_found'):
                            f.write("\n** CARRIER STATUS DETECTED **\n")
                            for carrier in cs['carriers_found']:
                                f.write(f"  {carrier['condition']}: {carrier['status']}\n")
                                f.write(f"    {carrier['description']}\n")
                        else:
                            f.write("\nNo carrier status detected for tested conditions.\n")

                    # PHARMACOGENOMICS
                    f.write("\n" + "=" * 70 + "\n")
                    f.write("PHARMACOGENOMICS (12 drug metabolism genes)\n")
                    f.write("=" * 70 + "\n")
                    pharma = self.results.pharmacogenomics
                    if pharma.get('high_priority_alerts'):
                        f.write("\n** HIGH PRIORITY ALERTS **\n")
                        for alert in pharma['high_priority_alerts']:
                            f.write(f"  {alert['gene']}: {alert['alert']}\n")
                            f.write(f"    Affected drugs: {', '.join(alert['affected_drugs'])}\n")
                    for gene, data in pharma.get('gene_results', {}).items():
                        f.write(f"\n{gene}:\n")
                        f.write(f"  Phenotype: {data.get('overall_phenotype', 'N/A')}\n")
                        f.write(f"  Action: {data.get('primary_action', 'Standard dosing')}\n")

                    # IMMUNITY
                    f.write("\n" + "=" * 70 + "\n")
                    f.write("IMMUNITY & PATHOGEN RESISTANCE\n")
                    f.write("=" * 70 + "\n")
                    for item in self.results.immunity.get('pathogen_resistance', []):
                        f.write(f"\n{item['pathogen']}:\n")
                        f.write(f"  Resistance: {item['resistance']}\n")
                        if item.get('action'):
                            f.write(f"  Action: {item['action']}\n")

                    # NUTRITION & FITNESS
                    f.write("\n" + "=" * 70 + "\n")
                    f.write("NUTRITION & FITNESS\n")
                    f.write("=" * 70 + "\n")
                    nf = self.results.nutrition_fitness
                    for nutrient, data in nf.get('nutrition', {}).items():
                        f.write(f"\n{data.get('trait_name', nutrient)}:\n")
                        f.write(f"  Need: {data.get('need', 'N/A')}\n")
                        if data.get('recommendation'):
                            f.write(f"  Recommendation: {data['recommendation']}\n")

                    f.write("\nFitness:\n")
                    for fitness, data in nf.get('fitness', {}).items():
                        f.write(f"  {data.get('trait_name', fitness)}: {data.get('type', 'N/A')}\n")

                    # DISCLAIMER
                    f.write("\n" + "=" * 70 + "\n")
                    f.write("DISCLAIMER\n")
                    f.write("=" * 70 + "\n")
                    f.write("This report is for educational and informational purposes only.\n")
                    f.write("It is NOT a medical diagnosis. Consult healthcare providers\n")
                    f.write("for medical decisions and genetic counseling.\n")
                    f.write(f"\nData sources: {self.results.summary.get('data_sources', 'N/A')}\n")

                messagebox.showinfo("Success", f"Report saved to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {str(e)}")

    def export_json(self):
        """Export as comprehensive JSON file"""
        import json

        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")]
        )
        if file_path:
            try:
                data = {
                    'ancestry': self.results.ancestry,
                    'physical_traits': self.results.physical_traits,
                    'health_traits': self.results.health_traits,
                    'pharmacogenomics': self.results.pharmacogenomics,
                    'carrier_status': self.results.carrier_status if hasattr(self.results, 'carrier_status') else {},
                    'immunity': self.results.immunity,
                    'nutrition_fitness': self.results.nutrition_fitness,
                    'longevity': self.results.longevity,
                    'haplogroups': self.results.haplogroups,
                    'summary': self.results.summary
                }
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, default=str)

                messagebox.showinfo("Success", f"Data saved to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {str(e)}")

    def export_pdf(self):
        """Export as PDF-ready HTML file"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".html",
            filetypes=[("HTML files (print to PDF)", "*.html")]
        )
        if file_path:
            try:
                html = self._generate_html_report()
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(html)

                # Open in browser for printing to PDF
                import webbrowser
                webbrowser.open(f'file://{file_path}')

                messagebox.showinfo(
                    "Success",
                    f"Report saved to {file_path}\n\nThe file has been opened in your browser.\nUse Ctrl+P (or Cmd+P) to print/save as PDF."
                )
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {str(e)}")

    def _generate_html_report(self) -> str:
        """Generate comprehensive HTML report for PDF export"""
        html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>DNA Analysis Report</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; max-width: 900px; margin: 0 auto; padding: 40px; color: #333; }
        h1 { color: #1e40af; border-bottom: 3px solid #1e40af; padding-bottom: 10px; }
        h2 { color: #1e3a8a; margin-top: 30px; border-bottom: 1px solid #ddd; padding-bottom: 5px; }
        h3 { color: #374151; margin-top: 20px; }
        .section { margin-bottom: 30px; page-break-inside: avoid; }
        .ancestry-bar { background: #e5e7eb; height: 24px; border-radius: 12px; margin: 8px 0; overflow: hidden; }
        .ancestry-fill { background: linear-gradient(90deg, #3b82f6, #1d4ed8); height: 100%; border-radius: 12px; }
        .trait-card { background: #f9fafb; border-left: 4px solid #3b82f6; padding: 12px; margin: 10px 0; }
        .alert { background: #fef2f2; border-left: 4px solid #ef4444; padding: 12px; margin: 10px 0; }
        .carrier { background: #fefce8; border-left: 4px solid #eab308; padding: 12px; margin: 10px 0; }
        .action { color: #059669; font-style: italic; margin-top: 5px; }
        .label { font-weight: bold; color: #374151; }
        .value { color: #1f2937; }
        .confidence { color: #6b7280; font-size: 0.9em; }
        .disclaimer { background: #f3f4f6; padding: 20px; border-radius: 8px; margin-top: 40px; font-size: 0.9em; }
        table { width: 100%; border-collapse: collapse; margin: 10px 0; }
        th, td { padding: 8px; text-align: left; border-bottom: 1px solid #e5e7eb; }
        th { background: #f3f4f6; }
        @media print { .section { page-break-inside: avoid; } }
    </style>
</head>
<body>
    <h1>Comprehensive DNA Analysis Report</h1>
    <p><strong>Generated:</strong> """ + self.results.summary.get('analysis_date', 'N/A') + """</p>
    <p><strong>SNPs Analyzed:</strong> """ + f"{self.results.summary.get('total_snps_analyzed', 0):,}" + """</p>
"""

        # ANCESTRY
        html += """<div class="section"><h2>Ancestry Composition</h2>"""
        html += f"<p>Using {self.results.ancestry.get('markers_continental', 'N/A'):,} continental + {self.results.ancestry.get('markers_subpop', 'N/A')} sub-population markers</p>"
        for pop, pct in sorted(self.results.ancestry.get('composition', {}).items(), key=lambda x: x[1], reverse=True):
            html += f"""<div><span class="label">{pop.replace('_', ' ')}: {pct:.1f}%</span>
            <div class="ancestry-bar"><div class="ancestry-fill" style="width: {pct}%"></div></div></div>"""
        html += "</div>"

        # PHYSICAL TRAITS
        html += """<div class="section"><h2>Physical Traits</h2>"""
        for trait_name, data in self.results.physical_traits.items():
            html += f"""<div class="trait-card">
            <span class="label">{data.get('trait_name', trait_name)}</span><br>
            <span class="value">Prediction: {data.get('prediction', 'N/A')}</span>
            <span class="confidence"> (Confidence: {data.get('confidence', 0)*100:.0f}%)</span>
            </div>"""
        html += "</div>"

        # HEALTH TRAITS
        html += """<div class="section"><h2>Health Traits</h2>"""
        for trait_name, data in self.results.health_traits.items():
            html += f"""<div class="trait-card">
            <span class="label">{data.get('trait_name', trait_name)}</span><br>
            <span class="value">Status: {data.get('status', 'N/A')}</span>"""
            if data.get('action'):
                html += f"""<div class="action">Action: {data['action']}</div>"""
            html += "</div>"
        html += "</div>"

        # CARRIER STATUS
        if hasattr(self.results, 'carrier_status'):
            cs = self.results.carrier_status
            html += """<div class="section"><h2>Carrier Status</h2>"""
            if cs.get('carriers_found'):
                html += """<p><strong>Carrier status detected for the following conditions:</strong></p>"""
                for carrier in cs['carriers_found']:
                    html += f"""<div class="carrier">
                    <span class="label">{carrier['condition']}</span><br>
                    <span class="value">{carrier['status']}</span><br>
                    <span>{carrier['description']}</span>
                    </div>"""
            else:
                html += "<p>No carrier status detected for tested conditions.</p>"
            html += "</div>"

        # PHARMACOGENOMICS
        pharma = self.results.pharmacogenomics
        html += """<div class="section"><h2>Pharmacogenomics</h2>"""
        if pharma.get('high_priority_alerts'):
            html += """<h3>High Priority Alerts</h3>"""
            for alert in pharma['high_priority_alerts']:
                html += f"""<div class="alert">
                <span class="label">{alert['gene']}</span>: {alert['alert']}<br>
                <span>Affected drugs: {', '.join(alert['affected_drugs'])}</span>
                </div>"""
        html += """<table><tr><th>Gene</th><th>Phenotype</th><th>Action</th></tr>"""
        for gene, data in pharma.get('gene_results', {}).items():
            html += f"""<tr><td>{gene}</td><td>{data.get('overall_phenotype', 'N/A')}</td>
            <td>{data.get('primary_action', 'Standard dosing')}</td></tr>"""
        html += "</table></div>"

        # IMMUNITY
        html += """<div class="section"><h2>Immunity & Pathogen Resistance</h2>"""
        for item in self.results.immunity.get('pathogen_resistance', []):
            html += f"""<div class="trait-card">
            <span class="label">{item['pathogen']}</span><br>
            <span class="value">Resistance: {item['resistance']}</span>"""
            if item.get('action'):
                html += f"""<div class="action">{item['action']}</div>"""
            html += "</div>"
        html += "</div>"

        # NUTRITION
        nf = self.results.nutrition_fitness
        html += """<div class="section"><h2>Nutrition</h2>"""
        for nutrient, data in nf.get('nutrition', {}).items():
            html += f"""<div class="trait-card">
            <span class="label">{data.get('trait_name', nutrient)}</span><br>
            <span class="value">Need: {data.get('need', 'N/A')}</span>"""
            if data.get('recommendation'):
                html += f"""<div class="action">{data['recommendation']}</div>"""
            html += "</div>"
        html += "</div>"

        # FITNESS
        html += """<div class="section"><h2>Fitness</h2>"""
        for fitness, data in nf.get('fitness', {}).items():
            html += f"""<div class="trait-card">
            <span class="label">{data.get('trait_name', fitness)}</span><br>
            <span class="value">{data.get('type', 'N/A')}</span>"""
            if data.get('training_focus'):
                html += f"""<div class="action">{data['training_focus']}</div>"""
            html += "</div>"
        html += "</div>"

        # DISCLAIMER
        html += """<div class="disclaimer">
        <h3>Disclaimer</h3>
        <p>This report is for <strong>educational and informational purposes only</strong>.
        It is NOT a medical diagnosis. Genetic information should be interpreted in consultation
        with qualified healthcare providers and genetic counselors.</p>
        <p><strong>Data Sources:</strong> """ + self.results.summary.get('data_sources', 'N/A') + """</p>
        </div>
</body>
</html>"""

        return html


# =============================================================================
# MAIN APPLICATION
# =============================================================================

class DNAAnalysisApp(ctk.CTk):
    """Main DNA Analysis Application"""

    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("DNA Analysis Tool - Comprehensive Genetic Insights")
        self.geometry("1500x950")
        self.minsize(1300, 850)

        # Application state
        self.dna_data = None
        self.analysis_results = None
        self.analysis_engine = ComprehensiveDNAAnalysisEngine()
        self.current_frame = None

        # Configure grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create sidebar
        self.sidebar = SidebarFrame(
            self,
            on_load_file=self.load_dna_file,
            on_navigate=self.navigate_to
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        # Create main content frame
        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

        # Show welcome screen
        self.show_welcome()

        # Bind keyboard shortcuts
        self.bind("<Control-o>", lambda e: self.load_dna_file())
        self.bind("<Control-e>", lambda e: self.navigate_to("export") if self.dna_data is not None else None)
        self.bind("<Escape>", lambda e: self.show_welcome())

    def clear_content(self):
        """Clear the main content area"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_welcome(self):
        """Show welcome/landing screen"""
        self.clear_content()
        self.current_frame = WelcomeFrame(
            self.content_frame,
            on_load_file=self.load_dna_file
        )
        self.current_frame.grid(row=0, column=0, sticky="nsew")

    def show_loading(self, message="Analyzing your DNA..."):
        """Show loading screen during analysis"""
        self.clear_content()
        self.current_frame = LoadingFrame(self.content_frame, message)
        self.current_frame.grid(row=0, column=0, sticky="nsew")
        self.update()

    def load_dna_file(self):
        """Open file dialog and load DNA data"""
        file_path = filedialog.askopenfilename(
            title="Select DNA Data File",
            filetypes=[
                ("DNA Files", "*.txt *.csv *.zip"),
                ("Text Files", "*.txt"),
                ("CSV Files", "*.csv"),
                ("ZIP Archives", "*.zip"),
                ("All Files", "*.*")
            ]
        )

        if file_path:
            self.process_dna_file(file_path)

    def process_dna_file(self, file_path):
        """Process the loaded DNA file"""
        self.show_loading("Loading and parsing DNA data...")

        def analyze():
            try:
                # Parse DNA file
                with open(file_path, 'rb') as f:
                    self.dna_data = parse_dna_file(f, file_path)

                if self.dna_data is None or len(self.dna_data) == 0:
                    self.after(0, lambda: messagebox.showerror(
                        "Error",
                        "Could not parse DNA file. Please check the file format."
                    ))
                    self.after(0, self.show_welcome)
                    return

                # Update loading message
                self.after(0, lambda: self.show_loading(
                    f"Running comprehensive analysis on {len(self.dna_data):,} genetic markers..."
                ))

                # Run comprehensive analysis
                self.analysis_results = self.analysis_engine.run_full_analysis(self.dna_data)

                # Update sidebar with results
                self.after(0, lambda: self.sidebar.enable_navigation(
                    snp_count=len(self.dna_data),
                    file_name=os.path.basename(file_path)
                ))

                # Show ethnicity estimate by default
                self.after(0, lambda: self.navigate_to("ethnicity"))

            except Exception as e:
                import traceback
                traceback.print_exc()
                self.after(0, lambda: messagebox.showerror(
                    "Error",
                    f"Failed to analyze DNA data:\n{str(e)}"
                ))
                self.after(0, self.show_welcome)

        # Run analysis in background thread
        thread = threading.Thread(target=analyze, daemon=True)
        thread.start()

    def navigate_to(self, section):
        """Navigate to a specific analysis section"""
        if self.dna_data is None or self.analysis_results is None:
            messagebox.showwarning("No Data", "Please load a DNA file first.")
            return

        self.clear_content()

        frame_map = {
            "physical": PhysicalTraitsFrame,
            "facial": FacialFeaturesFrame,
            "health": HealthTraitsFrame,
            "bloodtype": BloodTypeFrame,
            "athletic": AthleticFrame,
            "chronotype": ChronotypeFrame,
            "pain": PainFrame,
            "addiction": AddictionFrame,
            "mental": MentalTraitsFrame,
            "sensory": SensoryFrame,
            "behavioral": BehavioralFrame,
            "sleep": SleepFrame,
            "physicalexp": PhysicalExpandedFrame,
            "sportsgen": SportsFrame,
            "reproduction": ReproductionFrame,
            "immunedeep": ImmuneDeepFrame,
            "nutrimetab": NutritionMetabFrame,
            "ancienthistory": AncientHistoryFrame,
            "longevityexp": LongevityExpFrame,
            "pharmacoexp": PharmacoExpFrame,
            "mentalhealth": MentalHealthFrame,
            "cancerrisk": CancerRiskFrame,
            "cardiovasc": CardiovascFrame,
            "skinderm": SkinDermFrame,
            "carrier": CarrierStatusFrame,
            "pharma": PharmacogenomicsFrame,
            "haplogroup": HaplogroupFrame,
            "immunity": ImmunityFrame,
            "longevity": LongevityFrame,
            "nutrition": NutritionFitnessFrame,
            "climate": ClimateFrame,
            "polygenic": PolygenicFrame,
            "ancient": AncientDNAFrame,
            "ancientpop": AncientPopulationFrame,
            "plan": PersonalizedPlanFrame,
            "export": ExportFrame
        }

        # Unique features frame map (uses unique_features data)
        unique_frame_map = {
            "superpowers": SuperpowersFrame,
            "survival": SurvivalScenariosFrame,
            "historical": HistoricalMatchFrame,
            "timemachine": TimeMachineFrame,
            "epiage": EpigeneticAgeFrame,
            "archaicdna": ArchaicDNAFrame,
            "diettraining": DietTrainingFrame,
            "ancestrystory": AncestryStoryFrame,
            "allmarkers": AllMarkersFrame
        }

        if section == "ethnicity":
            # Special handling for ancestry ethnicity frame
            self.current_frame = AncestryEthnicityFrame(
                self.content_frame,
                snp_dict=self.dna_data
            )
            self.current_frame.grid(row=0, column=0, sticky="nsew")
            self.sidebar.set_active(section)
        elif section in frame_map:
            self.current_frame = frame_map[section](
                self.content_frame,
                self.analysis_results,
                self.dna_data
            )
            self.current_frame.grid(row=0, column=0, sticky="nsew")
            self.sidebar.set_active(section)
        elif section in unique_frame_map:
            # Unique feature frames take unique_features data
            unique_data = self.analysis_results.unique_features
            self.current_frame = unique_frame_map[section](
                self.content_frame,
                unique_data
            )
            self.current_frame.grid(row=0, column=0, sticky="nsew")
            self.sidebar.set_active(section)


def main():
    """Main entry point"""
    app = DNAAnalysisApp()
    app.mainloop()


if __name__ == "__main__":
    main()
