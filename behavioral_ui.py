#!/usr/bin/env python3
"""
Behavioral & Cognitive Genetics UI
Display for psychological traits, cognition, and behavior analysis
"""

import customtkinter as ctk
from typing import Dict, Any


class BehavioralGeneticsFrame(ctk.CTkFrame):
    """Comprehensive behavioral genetics display"""

    def __init__(self, parent, behavioral_data: Dict[str, Any], dna_data: dict):
        super().__init__(parent, fg_color="transparent")

        self.behavioral_data = behavioral_data
        self.dna_data = dna_data

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        self._create_header()

        # Scrollable content
        self.scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scroll.grid(row=1, column=0, sticky="nsew")
        self.scroll.grid_columnconfigure(0, weight=1)

        # Build sections
        self._create_disclaimer()
        self._create_profile_summary()
        self._create_empathy_section()
        self._create_novelty_section()
        self._create_stress_section()
        self._create_memory_section()
        self._create_additional_traits()

    def _create_header(self):
        """Create page header"""
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Behavioral & Cognitive Genetics",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Genetic influences on personality, cognition, and behavior",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

    def _create_disclaimer(self):
        """Create important disclaimer"""
        frame = ctk.CTkFrame(self.scroll, fg_color="#1e3a5f", corner_radius=10)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Important: Nature vs Nurture",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#93c5fd"
        ).pack(anchor="w", padx=20, pady=(12, 5))

        disclaimer = (
            "Behavioral traits are influenced by many genes AND environment. "
            "These are statistical associations, not predictions. "
            "Your experiences, choices, and environment shape who you are far more than any single gene. "
            "Use this information for self-understanding, not limitation."
        )
        ctk.CTkLabel(
            frame, text=disclaimer,
            font=ctk.CTkFont(size=12), text_color="#bfdbfe",
            wraplength=750, justify="left"
        ).pack(anchor="w", padx=20, pady=(0, 12))

    def _create_profile_summary(self):
        """Create overall behavioral profile"""
        profile = self.behavioral_data.get('overall_profile', {})
        if not profile:
            return

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        # Header
        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(15, 10))

        ctk.CTkLabel(
            header, text="Your Behavioral Profile",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(side="left")

        profile_type = profile.get('type', 'Balanced')
        type_colors = {
            'Explorer': '#f59e0b',
            'Sensitive': '#ec4899',
            'Resilient': '#22c55e',
            'Balanced': '#3b82f6'
        }
        ctk.CTkLabel(
            header, text=profile_type,
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=type_colors.get(profile_type, '#3b82f6')
        ).pack(side="right")

        # Description
        desc = profile.get('description', '')
        if desc:
            ctk.CTkLabel(
                frame, text=desc,
                font=ctk.CTkFont(size=14), text_color="gray60"
            ).pack(anchor="w", padx=20, pady=(0, 10))

        # Strengths and considerations
        cols = ctk.CTkFrame(frame, fg_color="transparent")
        cols.pack(fill="x", padx=20, pady=(0, 15))
        cols.grid_columnconfigure((0, 1), weight=1)

        # Strengths
        strengths = profile.get('strengths', [])
        if strengths:
            str_frame = ctk.CTkFrame(cols, fg_color="gray25", corner_radius=8)
            str_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))

            ctk.CTkLabel(
                str_frame, text="Genetic Tendencies",
                font=ctk.CTkFont(size=13, weight="bold"),
                text_color="#22c55e"
            ).pack(anchor="w", padx=12, pady=(10, 5))

            for s in strengths:
                ctk.CTkLabel(
                    str_frame, text=f"+ {s}",
                    font=ctk.CTkFont(size=11), text_color="gray70"
                ).pack(anchor="w", padx=12, pady=1)

            ctk.CTkFrame(str_frame, height=10, fg_color="transparent").pack()

        # Considerations
        considerations = profile.get('considerations', [])
        if considerations:
            con_frame = ctk.CTkFrame(cols, fg_color="gray25", corner_radius=8)
            con_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 0))

            ctk.CTkLabel(
                con_frame, text="Things to Consider",
                font=ctk.CTkFont(size=13, weight="bold"),
                text_color="#eab308"
            ).pack(anchor="w", padx=12, pady=(10, 5))

            for c in considerations:
                ctk.CTkLabel(
                    con_frame, text=f"- {c}",
                    font=ctk.CTkFont(size=11), text_color="gray70"
                ).pack(anchor="w", padx=12, pady=1)

            ctk.CTkFrame(con_frame, height=10, fg_color="transparent").pack()

    def _create_empathy_section(self):
        """Create empathy genetics section"""
        empathy = self.behavioral_data.get('empathy', {})
        if not empathy.get('markers_found'):
            return

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        self._create_trait_card(frame, "Empathy & Social Sensitivity", "OXTR",
            empathy.get('phenotype', 'Unknown'),
            empathy.get('description', ''),
            empathy.get('traits', []),
            empathy.get('level', 'Average'),
            '#ec4899')

    def _create_novelty_section(self):
        """Create novelty seeking section"""
        novelty = self.behavioral_data.get('novelty_seeking', {})
        if not novelty.get('markers_found'):
            return

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        self._create_trait_card(frame, "Novelty & Risk Seeking", "DRD4/DRD2",
            novelty.get('phenotype', 'Unknown'),
            novelty.get('description', ''),
            novelty.get('traits', []),
            novelty.get('level', 'Average'),
            '#f59e0b')

        # Reward sensitivity sub-card
        reward = novelty.get('reward_sensitivity', 'Normal')
        if reward != 'Normal':
            sub_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
            sub_frame.pack(fill="x", padx=20, pady=(0, 15))

            inner = ctk.CTkFrame(sub_frame, fg_color="transparent")
            inner.pack(fill="x", padx=12, pady=10)

            ctk.CTkLabel(
                inner, text="Reward Sensitivity (DRD2):",
                font=ctk.CTkFont(size=12)
            ).pack(side="left")

            ctk.CTkLabel(
                inner, text=reward,
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color="#f59e0b"
            ).pack(side="right")

    def _create_stress_section(self):
        """Create stress resilience section"""
        stress = self.behavioral_data.get('stress_resilience', {})
        warrior = self.behavioral_data.get('warrior_gene', {})

        if not stress.get('markers_found') and not warrior.get('markers_found'):
            return

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Stress Response & Resilience",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        # Stress resilience
        if stress.get('markers_found'):
            level = stress.get('resilience_level', 'Average')
            level_color = "#22c55e" if level == 'High' else "#ef4444" if level == 'Low' else "#3b82f6"

            res_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
            res_frame.pack(fill="x", padx=20, pady=5)

            inner = ctk.CTkFrame(res_frame, fg_color="transparent")
            inner.pack(fill="x", padx=15, pady=12)

            ctk.CTkLabel(
                inner, text="Stress Resilience:",
                font=ctk.CTkFont(size=14)
            ).pack(side="left")

            ctk.CTkLabel(
                inner, text=level,
                font=ctk.CTkFont(size=16, weight="bold"),
                text_color=level_color
            ).pack(side="right")

            # Traits
            traits = stress.get('traits', [])
            for trait in traits[:3]:
                ctk.CTkLabel(
                    res_frame, text=f"  - {trait}",
                    font=ctk.CTkFont(size=11), text_color="gray60"
                ).pack(anchor="w", padx=15, pady=1)

            ctk.CTkFrame(res_frame, height=10, fg_color="transparent").pack()

        # Warrior gene
        if warrior.get('markers_found'):
            war_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
            war_frame.pack(fill="x", padx=20, pady=5)

            inner = ctk.CTkFrame(war_frame, fg_color="transparent")
            inner.pack(fill="x", padx=15, pady=12)

            ctk.CTkLabel(
                inner, text="MAOA (Warrior/Worrier Gene):",
                font=ctk.CTkFont(size=14)
            ).pack(side="left")

            activity = warrior.get('activity_level', 'Unknown')
            activity_color = "#ef4444" if 'Warrior' in activity else "#3b82f6"
            ctk.CTkLabel(
                inner, text=activity,
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color=activity_color
            ).pack(side="right")

            # Important note
            note = warrior.get('important_note', '')
            if note:
                ctk.CTkLabel(
                    war_frame, text=f"Note: {note[:100]}...",
                    font=ctk.CTkFont(size=10), text_color="gray50",
                    wraplength=700
                ).pack(anchor="w", padx=15, pady=(0, 10))

        ctk.CTkFrame(frame, height=10, fg_color="transparent").pack()

    def _create_memory_section(self):
        """Create memory and learning section"""
        memory = self.behavioral_data.get('memory_learning', {})
        if not memory.get('markers_found'):
            return

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Memory & Cognition",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        # Grid of memory traits
        grid = ctk.CTkFrame(frame, fg_color="transparent")
        grid.pack(fill="x", padx=20, pady=(0, 15))
        grid.grid_columnconfigure((0, 1, 2), weight=1)

        # Episodic memory
        self._create_mini_trait(grid, 0, 0, "Episodic Memory",
            memory.get('episodic_memory', 'Average'), "KIBRA")

        # Working memory
        self._create_mini_trait(grid, 0, 1, "Working Memory",
            memory.get('working_memory', 'Average'), "COMT")

        # Brain plasticity
        self._create_mini_trait(grid, 0, 2, "Brain Plasticity",
            memory.get('brain_plasticity', 'Normal'), "BDNF")

        # Cognitive style
        style = memory.get('cognitive_style', 'Balanced')
        if style != 'Balanced':
            style_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
            style_frame.pack(fill="x", padx=20, pady=(0, 15))

            inner = ctk.CTkFrame(style_frame, fg_color="transparent")
            inner.pack(fill="x", padx=15, pady=12)

            ctk.CTkLabel(
                inner, text="Cognitive Style (COMT Val/Met):",
                font=ctk.CTkFont(size=13)
            ).pack(side="left")

            style_color = "#f59e0b" if 'Warrior' in style else "#a855f7"
            ctk.CTkLabel(
                inner, text=style,
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color=style_color
            ).pack(side="right")

    def _create_additional_traits(self):
        """Create additional behavioral traits section"""
        # Depression susceptibility
        depression = self.behavioral_data.get('depression_susceptibility', {})
        bonding = self.behavioral_data.get('social_bonding', {})
        attention = self.behavioral_data.get('attention_impulsivity', {})

        if not any([depression.get('markers_found'), bonding.get('markers_found'), attention.get('markers_found')]):
            return

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Additional Behavioral Traits",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        # Depression susceptibility
        if depression.get('markers_found'):
            self._create_simple_trait_row(frame, "Mood Regulation", "SLC6A4",
                depression.get('susceptibility', 'Average'))

        # Social bonding
        if bonding.get('markers_found'):
            self._create_simple_trait_row(frame, "Pair Bonding Intensity", "AVPR1A",
                bonding.get('bonding_intensity', 'Average'))

        # Attention
        if attention.get('markers_found'):
            self._create_simple_trait_row(frame, "Attention Regulation", "DAT1",
                attention.get('attention_regulation', 'Normal'))

        ctk.CTkFrame(frame, height=10, fg_color="transparent").pack()

    def _create_trait_card(self, parent, title, gene, phenotype, description, traits, level, color):
        """Create a behavioral trait card"""
        ctk.CTkLabel(
            parent, text=title,
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 5))

        # Gene and level
        info = ctk.CTkFrame(parent, fg_color="transparent")
        info.pack(fill="x", padx=20)

        ctk.CTkLabel(
            info, text=f"Gene: {gene}",
            font=ctk.CTkFont(size=12), text_color="gray60"
        ).pack(side="left")

        level_colors = {'High': '#22c55e', 'Higher': '#22c55e', 'Low': '#ef4444', 'Lower': '#ef4444', 'Average': '#3b82f6'}
        ctk.CTkLabel(
            info, text=f"Level: {level}",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=level_colors.get(level, color)
        ).pack(side="right")

        # Phenotype
        ctk.CTkLabel(
            parent, text=phenotype,
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=color
        ).pack(anchor="w", padx=20, pady=(10, 5))

        # Description
        if description:
            ctk.CTkLabel(
                parent, text=description,
                font=ctk.CTkFont(size=12), text_color="gray60"
            ).pack(anchor="w", padx=20)

        # Traits
        if traits:
            traits_frame = ctk.CTkFrame(parent, fg_color="gray25", corner_radius=8)
            traits_frame.pack(fill="x", padx=20, pady=10)

            for trait in traits[:5]:
                ctk.CTkLabel(
                    traits_frame, text=f"  - {trait}",
                    font=ctk.CTkFont(size=11), text_color="gray70"
                ).pack(anchor="w", padx=10, pady=2)

            ctk.CTkFrame(traits_frame, height=5, fg_color="transparent").pack()

        ctk.CTkFrame(parent, height=5, fg_color="transparent").pack()

    def _create_mini_trait(self, parent, row, col, label, value, gene):
        """Create mini trait display"""
        card = ctk.CTkFrame(parent, fg_color="gray25", corner_radius=8)
        card.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

        ctk.CTkLabel(
            card, text=label,
            font=ctk.CTkFont(size=11), text_color="gray60"
        ).pack(pady=(10, 2))

        value_color = "#22c55e" if 'Enhanced' in value or 'Better' in value else \
                     "#ef4444" if 'Reduced' in value or 'Lower' in value else "#3b82f6"
        ctk.CTkLabel(
            card, text=value,
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=value_color
        ).pack()

        ctk.CTkLabel(
            card, text=f"({gene})",
            font=ctk.CTkFont(size=9), text_color="gray50"
        ).pack(pady=(2, 10))

    def _create_simple_trait_row(self, parent, label, gene, value):
        """Create simple trait row"""
        row = ctk.CTkFrame(parent, fg_color="gray25", corner_radius=8)
        row.pack(fill="x", padx=20, pady=3)

        inner = ctk.CTkFrame(row, fg_color="transparent")
        inner.pack(fill="x", padx=15, pady=10)

        ctk.CTkLabel(
            inner, text=f"{label} ({gene}):",
            font=ctk.CTkFont(size=13)
        ).pack(side="left")

        value_color = "#22c55e" if 'Higher' in value or 'High' in value else \
                     "#ef4444" if 'Lower' in value or 'Low' in value else "#3b82f6"
        ctk.CTkLabel(
            inner, text=value,
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=value_color
        ).pack(side="right")
