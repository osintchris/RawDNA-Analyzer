#!/usr/bin/env python3
"""
Sports & Injury Genetics UI Components
Comprehensive display for athletic and injury risk genetic analysis
"""

import customtkinter as ctk
from typing import Dict, Any


class SportsGeneticsFrame(ctk.CTkFrame):
    """Comprehensive sports genetics display"""

    def __init__(self, parent, sports_data: Dict[str, Any], dna_data: dict):
        super().__init__(parent, fg_color="transparent")

        self.sports_data = sports_data
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
        self._create_athletic_profile()
        self._create_muscle_fiber_section()
        self._create_endurance_section()
        self._create_injury_risk_section()
        self._create_recovery_section()
        self._create_recommendations_section()

    def _create_header(self):
        """Create page header"""
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Sports & Injury Genetics",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Your genetic blueprint for athletic performance",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

    def _create_athletic_profile(self):
        """Create overall athletic profile summary"""
        profile = self.sports_data.get('athletic_profile', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(15, 10))

        ctk.CTkLabel(
            header, text="Your Athletic Profile",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(side="left")

        athlete_type = profile.get('type', 'All-Rounder')
        type_colors = {
            'Power Athlete': '#ef4444',
            'Endurance Athlete': '#3b82f6',
            'All-Rounder': '#22c55e'
        }
        ctk.CTkLabel(
            header, text=athlete_type,
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=type_colors.get(athlete_type, '#22c55e')
        ).pack(side="right")

        # Power vs Endurance bar
        scores_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
        scores_frame.pack(fill="x", padx=20, pady=(0, 10))

        power_score = profile.get('power_score', 0.5)
        endurance_score = profile.get('endurance_score', 0.5)

        # Labels
        label_row = ctk.CTkFrame(scores_frame, fg_color="transparent")
        label_row.pack(fill="x", padx=15, pady=(10, 5))

        ctk.CTkLabel(
            label_row, text=f"Power: {power_score*100:.0f}%",
            font=ctk.CTkFont(size=11), text_color="#ef4444"
        ).pack(side="left")

        ctk.CTkLabel(
            label_row, text=f"Endurance: {endurance_score*100:.0f}%",
            font=ctk.CTkFont(size=11), text_color="#3b82f6"
        ).pack(side="right")

        # Bar
        bar_frame = ctk.CTkFrame(scores_frame, fg_color="gray30", height=12, corner_radius=6)
        bar_frame.pack(fill="x", padx=15, pady=(0, 10))
        bar_frame.pack_propagate(False)

        # Power fill (from left)
        power_fill = ctk.CTkFrame(bar_frame, fg_color="#ef4444", corner_radius=6)
        power_fill.place(relx=0, rely=0.5, relwidth=power_score * 0.5, anchor="w", relheight=1)

        # Endurance fill (from right)
        endurance_fill = ctk.CTkFrame(bar_frame, fg_color="#3b82f6", corner_radius=6)
        endurance_fill.place(relx=1, rely=0.5, relwidth=endurance_score * 0.5, anchor="e", relheight=1)

        # Recommended sports
        sports = profile.get('recommended_sports', [])
        if sports:
            sports_frame = ctk.CTkFrame(frame, fg_color="transparent")
            sports_frame.pack(fill="x", padx=20, pady=(0, 10))

            ctk.CTkLabel(
                sports_frame, text="Best Suited For:",
                font=ctk.CTkFont(size=12, weight="bold"), text_color="gray60"
            ).pack(anchor="w")

            ctk.CTkLabel(
                sports_frame, text=", ".join(sports[:5]),
                font=ctk.CTkFont(size=12), text_color="#22c55e"
            ).pack(anchor="w")

        # Strengths and challenges
        strengths = profile.get('strengths', [])
        challenges = profile.get('challenges', [])

        if strengths or challenges:
            traits_frame = ctk.CTkFrame(frame, fg_color="transparent")
            traits_frame.pack(fill="x", padx=20, pady=(5, 15))
            traits_frame.grid_columnconfigure((0, 1), weight=1)

            if strengths:
                str_frame = ctk.CTkFrame(traits_frame, fg_color="gray25", corner_radius=8)
                str_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5), pady=5)

                ctk.CTkLabel(
                    str_frame, text="Genetic Advantages",
                    font=ctk.CTkFont(size=12, weight="bold"), text_color="#22c55e"
                ).pack(anchor="w", padx=10, pady=(8, 5))

                for s in strengths[:4]:
                    ctk.CTkLabel(
                        str_frame, text=f"+ {s}",
                        font=ctk.CTkFont(size=11), text_color="gray60"
                    ).pack(anchor="w", padx=10, pady=1)
                ctk.CTkFrame(str_frame, height=8, fg_color="transparent").pack()

            if challenges:
                ch_frame = ctk.CTkFrame(traits_frame, fg_color="gray25", corner_radius=8)
                ch_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 0), pady=5)

                ctk.CTkLabel(
                    ch_frame, text="Watch Points",
                    font=ctk.CTkFont(size=12, weight="bold"), text_color="#eab308"
                ).pack(anchor="w", padx=10, pady=(8, 5))

                for c in challenges[:4]:
                    ctk.CTkLabel(
                        ch_frame, text=f"! {c}",
                        font=ctk.CTkFont(size=11), text_color="gray60"
                    ).pack(anchor="w", padx=10, pady=1)
                ctk.CTkFrame(ch_frame, height=8, fg_color="transparent").pack()

    def _create_muscle_fiber_section(self):
        """Create muscle fiber composition section"""
        fiber = self.sports_data.get('muscle_fiber', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(15, 10))

        ctk.CTkLabel(
            header, text="Muscle Fiber Type",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(side="left")

        fiber_type = fiber.get('type', 'Mixed')
        type_colors = {'Fast-twitch dominant': '#ef4444', 'Slow-twitch dominant': '#3b82f6', 'Balanced': '#22c55e', 'Mixed': '#8b5cf6'}
        ctk.CTkLabel(
            header, text=fiber_type,
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=type_colors.get(fiber_type, '#8b5cf6')
        ).pack(side="right")

        # ACTN3 status
        actn3 = fiber.get('actn3_status', 'Unknown')
        if actn3 != 'Unknown':
            actn3_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
            actn3_frame.pack(fill="x", padx=20, pady=(0, 10))

            ctk.CTkLabel(
                actn3_frame, text="ACTN3 Speed Gene:",
                font=ctk.CTkFont(size=11), text_color="gray50"
            ).pack(side="left", padx=15, pady=8)

            ctk.CTkLabel(
                actn3_frame, text=actn3,
                font=ctk.CTkFont(size=12, weight="bold")
            ).pack(side="right", padx=15, pady=8)

        # Description
        desc = fiber.get('description', '')
        if desc:
            ctk.CTkLabel(
                frame, text=desc,
                font=ctk.CTkFont(size=12), text_color="gray60",
                wraplength=700
            ).pack(anchor="w", padx=20, pady=(0, 15))

    def _create_endurance_section(self):
        """Create endurance/VO2 max section"""
        vo2 = self.sports_data.get('vo2max', {})
        lactate = self.sports_data.get('lactate', {})
        fatigue = self.sports_data.get('fatigue', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Endurance Capacity",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        cards_frame = ctk.CTkFrame(frame, fg_color="transparent")
        cards_frame.pack(fill="x", padx=20, pady=(0, 15))
        cards_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # VO2 max card
        vo2_potential = vo2.get('potential', 'Average')
        vo2_colors = {'High': '#22c55e', 'Average': '#eab308', 'Lower': '#ef4444'}
        self._create_metric_card(
            cards_frame, 0, 0,
            "VO2 Max Potential",
            vo2_potential,
            vo2.get('trainability', ''),
            vo2_colors.get(vo2_potential, '#eab308')
        )

        # Lactate clearance
        lactate_clear = lactate.get('clearance', 'Normal')
        lac_colors = {'Fast': '#22c55e', 'Normal': '#eab308', 'Slow': '#ef4444'}
        self._create_metric_card(
            cards_frame, 0, 1,
            "Lactate Clearance",
            lactate_clear,
            lactate.get('description', '')[:50] + '...' if len(lactate.get('description', '')) > 50 else lactate.get('description', ''),
            lac_colors.get(lactate_clear, '#eab308')
        )

        # Fatigue resistance
        fatigue_res = fatigue.get('resistance', 'Normal')
        fat_colors = {'High': '#22c55e', 'Normal': '#eab308', 'Lower': '#ef4444'}
        self._create_metric_card(
            cards_frame, 0, 2,
            "Fatigue Resistance",
            fatigue_res,
            '',
            fat_colors.get(fatigue_res, '#eab308')
        )

    def _create_injury_risk_section(self):
        """Create injury risk section"""
        acl = self.sports_data.get('acl_injury', {})
        tendon = self.sports_data.get('tendon_injury', {})
        cramp = self.sports_data.get('muscle_cramp', {})
        bp = self.sports_data.get('bp_response', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Injury Risk Profile",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        cards_frame = ctk.CTkFrame(frame, fg_color="transparent")
        cards_frame.pack(fill="x", padx=20, pady=(0, 10))
        cards_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        risk_colors = {'Lower': '#22c55e', 'Average': '#eab308', 'Elevated': '#ef4444', 'Higher': '#ef4444'}

        # ACL risk
        acl_risk = acl.get('risk_level', 'Average')
        self._create_risk_card(cards_frame, 0, 0, "ACL Injury", acl_risk, risk_colors.get(acl_risk, '#eab308'))

        # Tendon risk
        tendon_risk = tendon.get('risk_level', 'Average')
        self._create_risk_card(cards_frame, 0, 1, "Tendon Injury", tendon_risk, risk_colors.get(tendon_risk, '#eab308'))

        # Cramp risk
        cramp_risk = cramp.get('risk_level', 'Average')
        self._create_risk_card(cards_frame, 0, 2, "Muscle Cramps", cramp_risk, risk_colors.get(cramp_risk, '#eab308'))

        # BP response
        bp_resp = bp.get('response', 'Normal')
        bp_colors = {'Lower': '#22c55e', 'Normal': '#22c55e', 'Elevated': '#ef4444'}
        self._create_risk_card(cards_frame, 0, 3, "BP Response", bp_resp, bp_colors.get(bp_resp, '#eab308'))

        # Descriptions for elevated risks
        desc_frame = ctk.CTkFrame(frame, fg_color="transparent")
        desc_frame.pack(fill="x", padx=20, pady=(0, 15))

        if acl.get('risk_level') == 'Elevated':
            ctk.CTkLabel(
                desc_frame, text="ACL: " + acl.get('description', ''),
                font=ctk.CTkFont(size=11), text_color="gray60", wraplength=700
            ).pack(anchor="w", pady=2)

        if tendon.get('risk_level') == 'Elevated':
            ctk.CTkLabel(
                desc_frame, text="Tendon: " + tendon.get('description', ''),
                font=ctk.CTkFont(size=11), text_color="gray60", wraplength=700
            ).pack(anchor="w", pady=2)

    def _create_recovery_section(self):
        """Create recovery section"""
        recovery = self.sports_data.get('recovery', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(15, 10))

        ctk.CTkLabel(
            header, text="Recovery Speed",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(side="left")

        speed = recovery.get('speed', 'Normal')
        speed_colors = {'Fast': '#22c55e', 'Normal': '#eab308', 'Slower': '#ef4444'}
        ctk.CTkLabel(
            header, text=speed,
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=speed_colors.get(speed, '#eab308')
        ).pack(side="right")

        # Info
        info_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
        info_frame.pack(fill="x", padx=20, pady=(0, 10))

        ctk.CTkLabel(
            info_frame, text="Inflammation Tendency:",
            font=ctk.CTkFont(size=11), text_color="gray50"
        ).pack(side="left", padx=15, pady=8)

        inflammation = recovery.get('inflammation_tendency', 'Normal')
        ctk.CTkLabel(
            info_frame, text=inflammation,
            font=ctk.CTkFont(size=12, weight="bold")
        ).pack(side="right", padx=15, pady=8)

        desc = recovery.get('description', '')
        if desc:
            ctk.CTkLabel(
                frame, text=desc,
                font=ctk.CTkFont(size=12), text_color="gray60",
                wraplength=700
            ).pack(anchor="w", padx=20, pady=(0, 15))

    def _create_recommendations_section(self):
        """Create recommendations section"""
        recommendations = self.sports_data.get('recommendations', [])

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Training Recommendations",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        if recommendations:
            for i, rec in enumerate(recommendations[:8]):
                rec_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
                rec_frame.pack(fill="x", padx=20, pady=3)

                ctk.CTkLabel(
                    rec_frame, text=f"{i+1}.",
                    font=ctk.CTkFont(size=12, weight="bold"), text_color="#3b82f6"
                ).pack(side="left", padx=(10, 5), pady=8)

                ctk.CTkLabel(
                    rec_frame, text=rec,
                    font=ctk.CTkFont(size=11), text_color="gray60",
                    wraplength=650
                ).pack(side="left", padx=(0, 10), pady=8)

        ctk.CTkFrame(frame, height=15, fg_color="transparent").pack()

    def _create_metric_card(self, parent, row, col, title, value, desc, color):
        """Create a metric card"""
        card = ctk.CTkFrame(parent, fg_color="gray25", corner_radius=10)
        card.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        ctk.CTkLabel(
            card, text=title,
            font=ctk.CTkFont(size=10), text_color="gray50"
        ).pack(anchor="w", padx=12, pady=(10, 2))

        ctk.CTkLabel(
            card, text=value,
            font=ctk.CTkFont(size=14, weight="bold"), text_color=color
        ).pack(anchor="w", padx=12)

        if desc:
            ctk.CTkLabel(
                card, text=desc,
                font=ctk.CTkFont(size=9), text_color="gray50",
                wraplength=180
            ).pack(anchor="w", padx=12, pady=(5, 10))
        else:
            ctk.CTkFrame(card, height=10, fg_color="transparent").pack()

    def _create_risk_card(self, parent, row, col, title, value, color):
        """Create a risk card"""
        card = ctk.CTkFrame(parent, fg_color="gray25", corner_radius=8)
        card.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

        ctk.CTkLabel(
            card, text=title,
            font=ctk.CTkFont(size=9), text_color="gray50"
        ).pack(pady=(8, 2))

        ctk.CTkLabel(
            card, text=value,
            font=ctk.CTkFont(size=12, weight="bold"), text_color=color
        ).pack(pady=(0, 8))
