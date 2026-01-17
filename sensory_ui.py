#!/usr/bin/env python3
"""
Sensory Genetics UI Components
Clean, modern UI for taste, smell, touch, and sensory analysis
"""

import customtkinter as ctk
from typing import Dict, Any


class SensoryGeneticsFrame(ctk.CTkFrame):
    """Comprehensive sensory genetics display"""

    def __init__(self, parent, sensory_data: Dict[str, Any], dna_data: dict):
        super().__init__(parent, fg_color="transparent")

        self.sensory_data = sensory_data
        self.dna_data = dna_data

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        self._create_header()

        # Scrollable content
        self.scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scroll.grid(row=1, column=0, sticky="nsew")
        self.scroll.grid_columnconfigure(0, weight=1)

        # Build all sections
        self._create_sensory_profile()
        self._create_taste_section()
        self._create_smell_section()
        self._create_touch_temperature_section()
        self._create_color_vision_section()

    def _create_header(self):
        """Create page header"""
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Sensory Genetics",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="How your genes shape what you taste, smell, and feel",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

        # Info note about Unknown values
        info_frame = ctk.CTkFrame(header, fg_color="#1e3a5f", corner_radius=8)
        info_frame.pack(fill="x", pady=(10, 0))
        ctk.CTkLabel(
            info_frame,
            text="Note: 'Unknown' means your DNA test file doesn't include that specific marker. Consumer tests (23andMe, AncestryDNA) only cover a subset of all genetic markers.",
            font=ctk.CTkFont(size=11), text_color="#93c5fd",
            wraplength=700, justify="left"
        ).pack(padx=15, pady=8)

    def _create_sensory_profile(self):
        """Create overall sensory profile summary"""
        profile = self.sensory_data.get('overall_sensory_profile', {})
        if not profile:
            return

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        # Header with sensory type
        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(15, 10))

        sensory_type = profile.get('type', 'Normal')
        type_colors = {
            'Hyper-Sensitive': '#ef4444',
            'Sensation-Seeker': '#3b82f6',
            'Balanced': '#22c55e'
        }
        type_color = type_colors.get(sensory_type, '#22c55e')

        ctk.CTkLabel(
            header, text="Your Sensory Profile",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(side="left")

        ctk.CTkLabel(
            header, text=sensory_type,
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=type_color
        ).pack(side="right")

        # Description
        desc = profile.get('description', '')
        if desc:
            ctk.CTkLabel(
                frame, text=desc,
                font=ctk.CTkFont(size=13), text_color="gray60",
                wraplength=700
            ).pack(anchor="w", padx=20, pady=(0, 10))

        # Strengths and sensitivities in two columns
        cols = ctk.CTkFrame(frame, fg_color="transparent")
        cols.pack(fill="x", padx=20, pady=(0, 15))
        cols.grid_columnconfigure((0, 1), weight=1)

        # Strengths
        strengths = profile.get('strengths', [])
        if strengths:
            str_frame = ctk.CTkFrame(cols, fg_color="gray25", corner_radius=8)
            str_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))

            ctk.CTkLabel(
                str_frame, text="Strengths",
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color="#22c55e"
            ).pack(anchor="w", padx=15, pady=(10, 5))

            for s in strengths:
                ctk.CTkLabel(
                    str_frame, text=f"+ {s}",
                    font=ctk.CTkFont(size=12), text_color="gray70"
                ).pack(anchor="w", padx=15, pady=2)

            ctk.CTkFrame(str_frame, height=10, fg_color="transparent").pack()

        # Sensitivities
        sensitivities = profile.get('sensitivities', [])
        if sensitivities:
            sens_frame = ctk.CTkFrame(cols, fg_color="gray25", corner_radius=8)
            sens_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 0))

            ctk.CTkLabel(
                sens_frame, text="Sensitivities",
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color="#eab308"
            ).pack(anchor="w", padx=15, pady=(10, 5))

            for s in sensitivities:
                ctk.CTkLabel(
                    sens_frame, text=f"! {s}",
                    font=ctk.CTkFont(size=12), text_color="gray70"
                ).pack(anchor="w", padx=15, pady=2)

            ctk.CTkFrame(sens_frame, height=10, fg_color="transparent").pack()

    def _create_taste_section(self):
        """Create taste genetics section"""
        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Taste Genetics",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        # Grid for taste cards
        grid = ctk.CTkFrame(frame, fg_color="transparent")
        grid.pack(fill="x", padx=20, pady=(0, 15))
        grid.grid_columnconfigure((0, 1, 2), weight=1)

        # Bitter taste
        bitter = self.sensory_data.get('bitter_taste', {})
        self._create_taste_card(grid, 0, 0, "Bitter Taste",
            bitter.get('phenotype', 'Unknown'),
            bitter.get('description', ''),
            bitter.get('implications', []),
            bitter.get('taster_score', 0.5),
            '#ef4444')

        # Sweet taste
        sweet = self.sensory_data.get('sweet_taste', {})
        self._create_taste_card(grid, 0, 1, "Sweet Taste",
            sweet.get('phenotype', 'Unknown'),
            sweet.get('description', ''),
            sweet.get('implications', []),
            sweet.get('sensitivity_score', 0.5),
            '#ec4899')

        # Umami taste
        umami = self.sensory_data.get('umami_taste', {})
        self._create_taste_card(grid, 0, 2, "Umami Taste",
            umami.get('phenotype', 'Unknown'),
            umami.get('description', ''),
            umami.get('implications', []),
            umami.get('sensitivity_score', 0.5),
            '#f59e0b')

        # Special taste items
        special_grid = ctk.CTkFrame(frame, fg_color="transparent")
        special_grid.pack(fill="x", padx=20, pady=(0, 15))
        special_grid.grid_columnconfigure((0, 1), weight=1)

        # Cilantro
        cilantro = self.sensory_data.get('cilantro', {})
        self._create_special_card(special_grid, 0, 0, "Cilantro/Coriander",
            "OR6A2 Gene",
            cilantro.get('phenotype', 'Unknown'),
            cilantro.get('description', ''),
            cilantro.get('tastes_soapy', False),
            '#84cc16')

        # Spice tolerance
        touch = self.sensory_data.get('touch_sensitivity', {})
        spice = touch.get('spice_tolerance', 'Unknown')
        self._create_special_card(special_grid, 0, 1, "Spice/Capsaicin",
            "TRPV1 Gene",
            spice,
            'How you perceive hot peppers',
            'High' in spice,
            '#dc2626')

    def _create_taste_card(self, parent, row, col, title, phenotype, description, implications, score, color):
        """Create a taste genetics card"""
        card = ctk.CTkFrame(parent, fg_color="gray25", corner_radius=10)
        card.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Title
        ctk.CTkLabel(
            card, text=title,
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(anchor="w", padx=15, pady=(12, 5))

        # Phenotype
        ctk.CTkLabel(
            card, text=phenotype,
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=color
        ).pack(anchor="w", padx=15)

        # Description
        if description:
            ctk.CTkLabel(
                card, text=description,
                font=ctk.CTkFont(size=11), text_color="gray60",
                wraplength=200
            ).pack(anchor="w", padx=15, pady=(5, 0))

        # Sensitivity bar
        bar_frame = ctk.CTkFrame(card, fg_color="transparent")
        bar_frame.pack(fill="x", padx=15, pady=10)

        ctk.CTkLabel(
            bar_frame, text="Sensitivity:",
            font=ctk.CTkFont(size=10), text_color="gray50"
        ).pack(side="left")

        bar = ctk.CTkProgressBar(bar_frame, width=100, height=10)
        bar.pack(side="right")
        bar.set(score)

        # Top implication
        if implications:
            ctk.CTkLabel(
                card, text=implications[0][:60] + "..." if len(implications[0]) > 60 else implications[0],
                font=ctk.CTkFont(size=10), text_color="gray50",
                wraplength=200
            ).pack(anchor="w", padx=15, pady=(0, 12))
        else:
            ctk.CTkFrame(card, height=12, fg_color="transparent").pack()

    def _create_special_card(self, parent, row, col, title, gene, phenotype, desc, is_special, color):
        """Create special taste/sensory card"""
        card = ctk.CTkFrame(parent, fg_color="gray25", corner_radius=10)
        card.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        header = ctk.CTkFrame(card, fg_color="transparent")
        header.pack(fill="x", padx=15, pady=(12, 5))

        ctk.CTkLabel(
            header, text=title,
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(side="left")

        ctk.CTkLabel(
            header, text=gene,
            font=ctk.CTkFont(size=11), text_color="gray50"
        ).pack(side="right")

        # Phenotype with indicator
        phen_frame = ctk.CTkFrame(card, fg_color="transparent")
        phen_frame.pack(fill="x", padx=15, pady=5)

        indicator_color = color if is_special else "gray50"
        ctk.CTkLabel(
            phen_frame, text="*",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=indicator_color
        ).pack(side="left", padx=(0, 5))

        ctk.CTkLabel(
            phen_frame, text=phenotype,
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=color if is_special else "white"
        ).pack(side="left")

        ctk.CTkLabel(
            card, text=desc,
            font=ctk.CTkFont(size=11), text_color="gray60"
        ).pack(anchor="w", padx=15, pady=(0, 12))

    def _create_smell_section(self):
        """Create smell/olfactory section"""
        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Smell & Olfactory Genetics",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        # Overall smell sensitivity
        smell = self.sensory_data.get('smell_sensitivity', {})
        overall = smell.get('overall_sensitivity', 'Normal')

        overall_colors = {
            'Super-Smeller': '#22c55e',
            'Reduced Smell (Hyposmia likely)': '#ef4444',
            'Normal': '#3b82f6'
        }

        summary_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
        summary_frame.pack(fill="x", padx=20, pady=(0, 10))

        sum_inner = ctk.CTkFrame(summary_frame, fg_color="transparent")
        sum_inner.pack(fill="x", padx=15, pady=12)

        ctk.CTkLabel(
            sum_inner, text="Overall Smell Ability:",
            font=ctk.CTkFont(size=14)
        ).pack(side="left")

        ctk.CTkLabel(
            sum_inner, text=overall,
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=overall_colors.get(overall, '#3b82f6')
        ).pack(side="right")

        # Specific smell abilities
        markers = smell.get('markers_found', [])
        if markers:
            ctk.CTkLabel(
                frame, text="Specific Smell Abilities:",
                font=ctk.CTkFont(size=14, weight="bold")
            ).pack(anchor="w", padx=20, pady=(10, 5))

            for marker in markers[:8]:  # Limit display
                self._create_smell_marker_row(frame, marker)

        # Asparagus smell
        asparagus = self.sensory_data.get('asparagus_smell', {})
        if asparagus.get('phenotype', 'Unknown') != 'Unknown':
            asp_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
            asp_frame.pack(fill="x", padx=20, pady=10)

            asp_inner = ctk.CTkFrame(asp_frame, fg_color="transparent")
            asp_inner.pack(fill="x", padx=15, pady=12)

            ctk.CTkLabel(
                asp_inner, text="Asparagus Urine Smell Detection",
                font=ctk.CTkFont(size=14, weight="bold")
            ).pack(anchor="w")

            ctk.CTkLabel(
                asp_inner, text=asparagus.get('phenotype', ''),
                font=ctk.CTkFont(size=13),
                text_color="#22c55e" if asparagus.get('can_smell') else "#ef4444"
            ).pack(anchor="w", pady=(5, 0))

            ctk.CTkLabel(
                asp_inner, text=asparagus.get('description', ''),
                font=ctk.CTkFont(size=11), text_color="gray60"
            ).pack(anchor="w", pady=(3, 0))

        # Specific anosmias
        anosmias = self.sensory_data.get('specific_anosmias', {})
        markers_found = anosmias.get('markers_found', [])
        if markers_found:
            ctk.CTkLabel(
                frame, text="Specific Smell Variants Detected:",
                font=ctk.CTkFont(size=14, weight="bold")
            ).pack(anchor="w", padx=20, pady=(10, 5))

            for marker in markers_found[:6]:
                row = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=6)
                row.pack(fill="x", padx=20, pady=2)

                row_inner = ctk.CTkFrame(row, fg_color="transparent")
                row_inner.pack(fill="x", padx=12, pady=8)

                ctk.CTkLabel(
                    row_inner, text=marker.get('anosmia', ''),
                    font=ctk.CTkFont(size=13, weight="bold")
                ).pack(side="left")

                ctk.CTkLabel(
                    row_inner, text=f"{marker.get('compound', '')} - {marker.get('source', '')}",
                    font=ctk.CTkFont(size=11), text_color="gray60"
                ).pack(side="right")

        ctk.CTkFrame(frame, height=15, fg_color="transparent").pack()

    def _create_smell_marker_row(self, parent, marker):
        """Create a row for a smell marker"""
        row = ctk.CTkFrame(parent, fg_color="gray25", corner_radius=6)
        row.pack(fill="x", padx=20, pady=2)

        inner = ctk.CTkFrame(row, fg_color="transparent")
        inner.pack(fill="x", padx=12, pady=8)

        # Gene and effect
        ctk.CTkLabel(
            inner, text=marker.get('gene', ''),
            font=ctk.CTkFont(size=12, weight="bold")
        ).pack(side="left")

        effect = marker.get('effect', '')
        effect_color = "#22c55e" if 'strong' in effect.lower() or 'super' in effect.lower() else \
                       "#ef4444" if 'cannot' in effect.lower() or 'anosmia' in effect.lower() else "gray60"

        ctk.CTkLabel(
            inner, text=effect,
            font=ctk.CTkFont(size=12),
            text_color=effect_color
        ).pack(side="right")

    def _create_touch_temperature_section(self):
        """Create touch and temperature sensitivity section"""
        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Touch & Temperature Sensitivity",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        grid = ctk.CTkFrame(frame, fg_color="transparent")
        grid.pack(fill="x", padx=20, pady=(0, 15))
        grid.grid_columnconfigure((0, 1), weight=1)

        # Touch sensitivity
        touch = self.sensory_data.get('touch_sensitivity', {})
        self._create_sensitivity_card(grid, 0, 0, "Touch Sensitivity",
            "PIEZO2",
            touch.get('overall_sensitivity', 'Unknown'),
            touch.get('implications', []),
            touch.get('sensitivity_score', 0.5))

        # Temperature sensitivity
        temp = self.sensory_data.get('temperature_sensitivity', {})
        temp_phenotype = temp.get('cold_sensitivity', 'Unknown')
        self._create_sensitivity_card(grid, 0, 1, "Cold Sensitivity",
            "TRPM8",
            temp_phenotype,
            temp.get('implications', []),
            0.8 if 'Very' in temp_phenotype else 0.2 if 'tolerant' in temp_phenotype else 0.5)

        # Additional temperature details
        temp_details = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
        temp_details.pack(fill="x", padx=20, pady=(0, 15))

        details_grid = ctk.CTkFrame(temp_details, fg_color="transparent")
        details_grid.pack(fill="x", padx=15, pady=12)
        details_grid.grid_columnconfigure((0, 1, 2), weight=1)

        # Menthol
        menthol = temp.get('menthol_response', 'Normal')
        self._create_mini_stat(details_grid, 0, 0, "Menthol/Mint", menthol)

        # Warmth
        warmth = temp.get('warmth_sensing', 'Normal')
        self._create_mini_stat(details_grid, 0, 1, "Warmth Sensing", warmth)

        # Irritants
        irritant = temp.get('irritant_sensitivity', 'Normal')
        self._create_mini_stat(details_grid, 0, 2, "Wasabi/Mustard", irritant)

    def _create_sensitivity_card(self, parent, row, col, title, gene, phenotype, implications, score):
        """Create a sensitivity card"""
        card = ctk.CTkFrame(parent, fg_color="gray25", corner_radius=10)
        card.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        header = ctk.CTkFrame(card, fg_color="transparent")
        header.pack(fill="x", padx=15, pady=(12, 5))

        ctk.CTkLabel(
            header, text=title,
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(side="left")

        ctk.CTkLabel(
            header, text=gene,
            font=ctk.CTkFont(size=11), text_color="gray50"
        ).pack(side="right")

        # Phenotype
        phen_color = "#22c55e" if score > 0.6 else "#ef4444" if score < 0.4 else "#3b82f6"
        ctk.CTkLabel(
            card, text=phenotype,
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=phen_color
        ).pack(anchor="w", padx=15, pady=5)

        # Bar
        bar_frame = ctk.CTkFrame(card, fg_color="transparent")
        bar_frame.pack(fill="x", padx=15, pady=5)

        ctk.CTkLabel(bar_frame, text="Low", font=ctk.CTkFont(size=9), text_color="gray50").pack(side="left")
        bar = ctk.CTkProgressBar(bar_frame, width=150, height=10)
        bar.pack(side="left", padx=10)
        bar.set(score)
        ctk.CTkLabel(bar_frame, text="High", font=ctk.CTkFont(size=9), text_color="gray50").pack(side="left")

        # Implications
        if implications:
            ctk.CTkLabel(
                card, text=implications[0][:80] + "..." if len(implications[0]) > 80 else implications[0],
                font=ctk.CTkFont(size=10), text_color="gray60",
                wraplength=250
            ).pack(anchor="w", padx=15, pady=(5, 12))
        else:
            ctk.CTkFrame(card, height=12, fg_color="transparent").pack()

    def _create_mini_stat(self, parent, row, col, label, value):
        """Create mini stat display"""
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.grid(row=row, column=col, sticky="nsew", padx=5)

        ctk.CTkLabel(
            frame, text=label,
            font=ctk.CTkFont(size=11), text_color="gray50"
        ).pack()

        value_color = "#22c55e" if 'High' in value or 'Strong' in value else \
                      "#ef4444" if 'Low' in value or 'Reduced' in value else "white"
        ctk.CTkLabel(
            frame, text=value,
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=value_color
        ).pack()

    def _create_color_vision_section(self):
        """Create color vision section"""
        vision = self.sensory_data.get('color_vision', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Color Vision",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        # Status card
        status = vision.get('status', 'Normal Color Vision')
        status_color = "#22c55e" if 'Normal' in status else "#ef4444"

        status_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
        status_frame.pack(fill="x", padx=20, pady=(0, 10))

        status_inner = ctk.CTkFrame(status_frame, fg_color="transparent")
        status_inner.pack(fill="x", padx=15, pady=12)

        ctk.CTkLabel(
            status_inner, text="Color Vision Status:",
            font=ctk.CTkFont(size=14)
        ).pack(side="left")

        ctk.CTkLabel(
            status_inner, text=status,
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=status_color
        ).pack(side="right")

        # Light sensitivity
        light = vision.get('light_sensitivity', 'Normal')
        if light != 'Normal':
            light_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
            light_frame.pack(fill="x", padx=20, pady=(0, 10))

            light_inner = ctk.CTkFrame(light_frame, fg_color="transparent")
            light_inner.pack(fill="x", padx=15, pady=12)

            ctk.CTkLabel(
                light_inner, text="Light Sensitivity:",
                font=ctk.CTkFont(size=14)
            ).pack(side="left")

            light_color = "#eab308" if 'High' in light else "#3b82f6"
            ctk.CTkLabel(
                light_inner, text=light,
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color=light_color
            ).pack(side="right")

        # Markers found
        markers = vision.get('markers_found', [])
        if markers:
            ctk.CTkLabel(
                frame, text="Analyzed Markers:",
                font=ctk.CTkFont(size=12), text_color="gray50"
            ).pack(anchor="w", padx=20, pady=(5, 5))

            for marker in markers:
                row = ctk.CTkFrame(frame, fg_color="transparent")
                row.pack(fill="x", padx=20)

                ctk.CTkLabel(
                    row, text=f"{marker.get('gene', '')} ({marker.get('rsid', '')}): {marker.get('genotype', '')}",
                    font=ctk.CTkFont(size=11), text_color="gray60"
                ).pack(side="left")

        ctk.CTkFrame(frame, height=15, fg_color="transparent").pack()
