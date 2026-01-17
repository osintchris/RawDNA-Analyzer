#!/usr/bin/env python3
"""
Physical Traits Expanded UI Components
Comprehensive display for expanded physical trait genetic analysis
"""

import customtkinter as ctk
from typing import Dict, Any


class PhysicalTraitsExpandedFrame(ctk.CTkFrame):
    """Comprehensive expanded physical traits display"""

    def __init__(self, parent, traits_data: Dict[str, Any], dna_data: dict):
        super().__init__(parent, fg_color="transparent")

        self.traits_data = traits_data
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
        self._create_summary_section()
        self._create_height_section()
        self._create_hair_section()
        self._create_facial_features_section()
        self._create_other_traits_section()

    def _create_header(self):
        """Create page header"""
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Physical Traits Expanded",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Additional genetic traits and characteristics",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

    def _create_summary_section(self):
        """Create summary of notable traits"""
        summary = self.traits_data.get('summary', {})
        notable = summary.get('notable_traits', [])
        rare = summary.get('rare_traits', [])

        if not notable and not rare:
            return

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Notable Genetic Traits",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        if rare:
            rare_frame = ctk.CTkFrame(frame, fg_color="#1e3a5f", corner_radius=8)
            rare_frame.pack(fill="x", padx=20, pady=5)

            ctk.CTkLabel(
                rare_frame, text="Rare Variants Detected:",
                font=ctk.CTkFont(size=12, weight="bold"), text_color="#60a5fa"
            ).pack(anchor="w", padx=10, pady=(8, 5))

            for trait in rare:
                ctk.CTkLabel(
                    rare_frame, text=f"* {trait}",
                    font=ctk.CTkFont(size=11), text_color="gray60"
                ).pack(anchor="w", padx=10, pady=1)

            ctk.CTkFrame(rare_frame, height=5, fg_color="transparent").pack()

        if notable:
            traits_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
            traits_frame.pack(fill="x", padx=20, pady=(5, 15))

            for trait in notable[:8]:
                ctk.CTkLabel(
                    traits_frame, text=f"- {trait}",
                    font=ctk.CTkFont(size=12), text_color="gray60"
                ).pack(anchor="w", padx=15, pady=2)

            ctk.CTkFrame(traits_frame, height=5, fg_color="transparent").pack()

    def _create_height_section(self):
        """Create height genetics section"""
        height = self.traits_data.get('height', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(15, 10))

        ctk.CTkLabel(
            header, text="Height Genetics",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(side="left")

        prediction = height.get('prediction', 'Average')
        cm_adj = height.get('cm_adjustment', 0)

        if cm_adj > 0:
            color = "#22c55e"
            adj_text = f"+{cm_adj:.1f}cm"
        elif cm_adj < 0:
            color = "#f59e0b"
            adj_text = f"{cm_adj:.1f}cm"
        else:
            color = "#3b82f6"
            adj_text = "Average"

        ctk.CTkLabel(
            header, text=adj_text,
            font=ctk.CTkFont(size=16, weight="bold"), text_color=color
        ).pack(side="right")

        # Description
        desc = height.get('description', '')
        if desc:
            ctk.CTkLabel(
                frame, text=desc,
                font=ctk.CTkFont(size=12), text_color="gray60",
                wraplength=700
            ).pack(anchor="w", padx=20, pady=(0, 10))

        # Confidence
        confidence = height.get('confidence', 0.5)
        conf_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
        conf_frame.pack(fill="x", padx=20, pady=(0, 10))

        ctk.CTkLabel(
            conf_frame, text=f"Confidence: {confidence*100:.0f}%",
            font=ctk.CTkFont(size=11), text_color="gray60"
        ).pack(side="left", padx=15, pady=8)

        ctk.CTkLabel(
            conf_frame, text="Note: Height is ~80% genetic, environment matters too",
            font=ctk.CTkFont(size=10), text_color="gray50"
        ).pack(side="right", padx=15, pady=8)

        # Markers found
        markers = height.get('markers_found', [])
        if markers:
            self._create_markers_grid(frame, markers, ['gene', 'genotype', 'effect'])

    def _create_hair_section(self):
        """Create hair genetics section (texture + loss)"""
        texture = self.traits_data.get('hair_texture', {})
        loss = self.traits_data.get('hair_loss', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Hair Genetics",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        cards_frame = ctk.CTkFrame(frame, fg_color="transparent")
        cards_frame.pack(fill="x", padx=20, pady=(0, 10))
        cards_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Texture card
        texture_colors = {'Curly': '#ec4899', 'Wavy': '#8b5cf6', 'Straight': '#3b82f6'}
        self._create_trait_card(
            cards_frame, 0, 0,
            "Hair Texture",
            texture.get('texture', 'Unknown'),
            texture.get('description', ''),
            texture_colors.get(texture.get('texture', 'Wavy'), '#8b5cf6')
        )

        # Thickness card
        thickness = texture.get('thickness', 'Normal')
        thick_colors = {'Very thick': '#22c55e', 'Increased': '#22c55e', 'Normal': '#3b82f6'}
        self._create_trait_card(
            cards_frame, 0, 1,
            "Hair Thickness",
            thickness,
            '',
            thick_colors.get(thickness, '#3b82f6')
        )

        # Hair loss risk card
        loss_level = loss.get('risk_level', 'Average')
        loss_colors = {'Higher': '#ef4444', 'Average': '#eab308', 'Lower': '#22c55e'}
        self._create_trait_card(
            cards_frame, 0, 2,
            "Hair Loss Risk",
            loss_level,
            loss.get('onset_likelihood', ''),
            loss_colors.get(loss_level, '#eab308')
        )

        # Hair loss description
        loss_desc = loss.get('description', '')
        if loss_desc:
            ctk.CTkLabel(
                frame, text=loss_desc,
                font=ctk.CTkFont(size=11), text_color="gray60",
                wraplength=700
            ).pack(anchor="w", padx=20, pady=(0, 15))

    def _create_facial_features_section(self):
        """Create facial features section"""
        freckles = self.traits_data.get('freckles', {})
        dimples = self.traits_data.get('dimples', {})
        widows_peak = self.traits_data.get('widows_peak', {})
        cleft_chin = self.traits_data.get('cleft_chin', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Facial Features",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        cards_frame = ctk.CTkFrame(frame, fg_color="transparent")
        cards_frame.pack(fill="x", padx=20, pady=(0, 15))
        cards_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Freckles
        freckle_likelihood = freckles.get('likelihood', 'Average')
        freckle_colors = {'High': '#f97316', 'Average': '#eab308', 'Low': '#3b82f6'}
        self._create_mini_trait_card(
            cards_frame, 0, 0,
            "Freckles",
            freckle_likelihood,
            freckle_colors.get(freckle_likelihood, '#eab308')
        )

        # Dimples
        dimple_likelihood = dimples.get('likelihood', 'Possible')
        dimple_colors = {'Likely': '#22c55e', 'Possible': '#eab308', 'Less likely': '#6b7280'}
        self._create_mini_trait_card(
            cards_frame, 0, 1,
            "Dimples",
            dimple_likelihood,
            dimple_colors.get(dimple_likelihood, '#eab308')
        )

        # Widow's peak
        wp_likelihood = widows_peak.get('likelihood', 'Possible')
        self._create_mini_trait_card(
            cards_frame, 0, 2,
            "Widow's Peak",
            wp_likelihood,
            dimple_colors.get(wp_likelihood, '#eab308')
        )

        # Cleft chin
        cc_likelihood = cleft_chin.get('likelihood', 'Possible')
        self._create_mini_trait_card(
            cards_frame, 0, 3,
            "Cleft Chin",
            cc_likelihood,
            dimple_colors.get(cc_likelihood, '#eab308')
        )

    def _create_other_traits_section(self):
        """Create other traits section"""
        earlobes = self.traits_data.get('earlobes', {})
        tongue = self.traits_data.get('tongue_rolling', {})
        finger = self.traits_data.get('finger_ratio', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Other Physical Traits",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        cards_frame = ctk.CTkFrame(frame, fg_color="transparent")
        cards_frame.pack(fill="x", padx=20, pady=(0, 10))
        cards_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Earlobes
        earlobe_type = earlobes.get('type', 'Variable')
        earlobe_colors = {'Free (Detached)': '#3b82f6', 'Partially Attached': '#8b5cf6', 'Attached': '#6366f1'}
        self._create_trait_card(
            cards_frame, 0, 0,
            "Earlobes",
            earlobe_type,
            earlobes.get('description', ''),
            earlobe_colors.get(earlobe_type, '#8b5cf6')
        )

        # Tongue rolling
        tongue_ability = tongue.get('ability', 'Possible')
        tongue_colors = {'Likely can': '#22c55e', 'Possible': '#eab308', 'May need practice': '#6b7280'}
        self._create_trait_card(
            cards_frame, 0, 1,
            "Tongue Rolling",
            tongue_ability,
            tongue.get('description', ''),
            tongue_colors.get(tongue_ability, '#eab308')
        )

        # Finger ratio
        finger_tendency = finger.get('tendency', 'Average 2D:4D')
        finger_colors = {
            'Lower 2D:4D': '#3b82f6',
            'Higher 2D:4D': '#ec4899',
            'Average 2D:4D': '#8b5cf6'
        }
        self._create_trait_card(
            cards_frame, 0, 2,
            "Finger Ratio",
            finger_tendency,
            finger.get('description', ''),
            finger_colors.get(finger_tendency, '#8b5cf6')
        )

        # Disclaimer
        disclaimer = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
        disclaimer.pack(fill="x", padx=20, pady=(5, 15))

        ctk.CTkLabel(
            disclaimer, text="Note",
            font=ctk.CTkFont(size=11, weight="bold"), text_color="#eab308"
        ).pack(anchor="w", padx=12, pady=(8, 3))

        ctk.CTkLabel(
            disclaimer,
            text="Physical traits are influenced by many genes and environmental factors. These predictions are probabilistic, not deterministic.",
            font=ctk.CTkFont(size=10), text_color="gray50",
            wraplength=680
        ).pack(anchor="w", padx=12, pady=(0, 8))

    def _create_trait_card(self, parent, row, col, title, value, description, color):
        """Create a trait card with title, value, and description"""
        card = ctk.CTkFrame(parent, fg_color="gray25", corner_radius=10)
        card.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        ctk.CTkLabel(
            card, text=title,
            font=ctk.CTkFont(size=11), text_color="gray50"
        ).pack(anchor="w", padx=12, pady=(10, 2))

        ctk.CTkLabel(
            card, text=value,
            font=ctk.CTkFont(size=14, weight="bold"), text_color=color
        ).pack(anchor="w", padx=12)

        if description:
            ctk.CTkLabel(
                card, text=description,
                font=ctk.CTkFont(size=9), text_color="gray50",
                wraplength=200
            ).pack(anchor="w", padx=12, pady=(5, 10))
        else:
            ctk.CTkFrame(card, height=10, fg_color="transparent").pack()

    def _create_mini_trait_card(self, parent, row, col, title, value, color):
        """Create a smaller trait card"""
        card = ctk.CTkFrame(parent, fg_color="gray25", corner_radius=8)
        card.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

        ctk.CTkLabel(
            card, text=title,
            font=ctk.CTkFont(size=10), text_color="gray50"
        ).pack(pady=(8, 2))

        ctk.CTkLabel(
            card, text=value,
            font=ctk.CTkFont(size=12, weight="bold"), text_color=color
        ).pack(pady=(0, 8))

    def _create_markers_grid(self, parent, markers, columns):
        """Create a grid showing markers"""
        markers_frame = ctk.CTkFrame(parent, fg_color="gray25", corner_radius=8)
        markers_frame.pack(fill="x", padx=20, pady=(5, 15))

        ctk.CTkLabel(
            markers_frame, text="Genetic Markers:",
            font=ctk.CTkFont(size=11, weight="bold"), text_color="gray60"
        ).pack(anchor="w", padx=10, pady=(8, 5))

        for marker in markers[:6]:
            row = ctk.CTkFrame(markers_frame, fg_color="transparent")
            row.pack(fill="x", padx=10, pady=1)

            ctk.CTkLabel(
                row, text=f"{marker.get('gene', '')}",
                font=ctk.CTkFont(size=10), text_color="gray50"
            ).pack(side="left")

            ctk.CTkLabel(
                row, text=f"{marker.get('genotype', '')} - {marker.get('effect', '')}",
                font=ctk.CTkFont(size=10, weight="bold")
            ).pack(side="right")

        if len(markers) > 6:
            ctk.CTkLabel(
                markers_frame, text=f"+ {len(markers) - 6} more",
                font=ctk.CTkFont(size=9), text_color="gray50"
            ).pack(anchor="w", padx=10)

        ctk.CTkFrame(markers_frame, height=5, fg_color="transparent").pack()
