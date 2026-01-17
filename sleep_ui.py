#!/usr/bin/env python3
"""
Sleep & Circadian Genetics UI Components
Comprehensive display for sleep-related genetic analysis
"""

import customtkinter as ctk
from typing import Dict, Any


class SleepGeneticsFrame(ctk.CTkFrame):
    """Comprehensive sleep genetics display"""

    def __init__(self, parent, sleep_data: Dict[str, Any], dna_data: dict):
        super().__init__(parent, fg_color="transparent")

        self.sleep_data = sleep_data
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
        self._create_sleep_profile()
        self._create_chronotype_section()
        self._create_sleep_duration_section()
        self._create_sleep_quality_section()
        self._create_sleep_stages_section()
        self._create_sleep_challenges_section()
        self._create_caffeine_section()
        self._create_recommendations_section()

    def _create_header(self):
        """Create page header"""
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Sleep & Circadian Genetics",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Your genetic blueprint for optimal sleep",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

    def _create_sleep_profile(self):
        """Create overall sleep profile summary"""
        profile = self.sleep_data.get('overall_profile', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        # Header
        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(15, 10))

        ctk.CTkLabel(
            header, text="Your Sleep Profile",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(side="left")

        profile_type = profile.get('type', 'Balanced')
        type_colors = {
            'Morning-oriented': '#f59e0b',
            'Evening-oriented': '#6366f1',
            'Balanced': '#22c55e'
        }
        ctk.CTkLabel(
            header, text=profile_type,
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=type_colors.get(profile_type, '#22c55e')
        ).pack(side="right")

        # Description
        desc = profile.get('description', '')
        if desc:
            ctk.CTkLabel(
                frame, text=desc,
                font=ctk.CTkFont(size=13), text_color="gray60",
                wraplength=700, justify="left"
            ).pack(anchor="w", padx=20, pady=(0, 10))

        # Optimal schedule
        schedule = profile.get('optimal_schedule', {})
        if schedule:
            sched_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
            sched_frame.pack(fill="x", padx=20, pady=(0, 10))
            sched_frame.grid_columnconfigure((0, 1, 2), weight=1)

            self._create_schedule_box(sched_frame, 0, "Optimal Bedtime",
                                     schedule.get('bedtime', 'N/A'), "#6366f1")
            self._create_schedule_box(sched_frame, 1, "Optimal Wake Time",
                                     schedule.get('wake_time', 'N/A'), "#f59e0b")
            self._create_schedule_box(sched_frame, 2, "Peak Hours",
                                     schedule.get('peak_hours', 'N/A'), "#22c55e")

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
                    str_frame, text="Genetic Strengths",
                    font=ctk.CTkFont(size=12, weight="bold"), text_color="#22c55e"
                ).pack(anchor="w", padx=10, pady=(8, 5))

                for strength in strengths[:4]:
                    ctk.CTkLabel(
                        str_frame, text=f"+ {strength}",
                        font=ctk.CTkFont(size=11), text_color="gray60"
                    ).pack(anchor="w", padx=10, pady=1)

                ctk.CTkFrame(str_frame, height=8, fg_color="transparent").pack()

            if challenges:
                chal_frame = ctk.CTkFrame(traits_frame, fg_color="gray25", corner_radius=8)
                chal_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 0), pady=5)

                ctk.CTkLabel(
                    chal_frame, text="Watch Points",
                    font=ctk.CTkFont(size=12, weight="bold"), text_color="#eab308"
                ).pack(anchor="w", padx=10, pady=(8, 5))

                for challenge in challenges[:4]:
                    ctk.CTkLabel(
                        chal_frame, text=f"! {challenge}",
                        font=ctk.CTkFont(size=11), text_color="gray60"
                    ).pack(anchor="w", padx=10, pady=1)

                ctk.CTkFrame(chal_frame, height=8, fg_color="transparent").pack()

    def _create_schedule_box(self, parent, col, label, value, color):
        """Create a schedule info box"""
        box = ctk.CTkFrame(parent, fg_color="transparent")
        box.grid(row=0, column=col, sticky="nsew", padx=10, pady=10)

        ctk.CTkLabel(
            box, text=label,
            font=ctk.CTkFont(size=10), text_color="gray50"
        ).pack()

        ctk.CTkLabel(
            box, text=value,
            font=ctk.CTkFont(size=14, weight="bold"), text_color=color
        ).pack()

    def _create_chronotype_section(self):
        """Create chronotype section"""
        chrono = self.sleep_data.get('chronotype', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(15, 10))

        ctk.CTkLabel(
            header, text="Chronotype",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(side="left")

        phenotype = chrono.get('phenotype', 'Unknown')
        score = chrono.get('score', 0.5)

        # Color based on chronotype
        if score >= 0.6:
            color = "#f59e0b"  # Morning - amber
            icon = "[SUN]"
        elif score <= 0.4:
            color = "#6366f1"  # Evening - indigo
            icon = "[MOON]"
        else:
            color = "#22c55e"  # Balanced - green
            icon = "[CLOCK]"

        ctk.CTkLabel(
            header, text=f"{icon} {phenotype}",
            font=ctk.CTkFont(size=14, weight="bold"), text_color=color
        ).pack(side="right")

        # Description
        desc = chrono.get('description', '')
        if desc:
            ctk.CTkLabel(
                frame, text=desc,
                font=ctk.CTkFont(size=12), text_color="gray60",
                wraplength=700
            ).pack(anchor="w", padx=20, pady=(0, 10))

        # Chronotype scale
        scale_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
        scale_frame.pack(fill="x", padx=20, pady=(0, 10))

        ctk.CTkLabel(
            scale_frame, text="Lark                    Intermediate                    Owl",
            font=ctk.CTkFont(size=10), text_color="gray50"
        ).pack(pady=(8, 2))

        # Visual scale bar
        bar_frame = ctk.CTkFrame(scale_frame, fg_color="gray30", height=20, corner_radius=10)
        bar_frame.pack(fill="x", padx=15, pady=5)
        bar_frame.pack_propagate(False)

        # Position indicator
        indicator_pos = 1 - score  # Invert so morning is left
        indicator = ctk.CTkFrame(bar_frame, width=10, height=16, fg_color=color, corner_radius=5)
        indicator.place(relx=indicator_pos, rely=0.5, anchor="center")

        ctk.CTkFrame(scale_frame, height=8, fg_color="transparent").pack()

        # Markers found
        markers = chrono.get('markers_found', [])
        if markers:
            self._create_markers_list(frame, markers)

    def _create_sleep_duration_section(self):
        """Create sleep duration section"""
        duration = self.sleep_data.get('sleep_duration', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(15, 10))

        ctk.CTkLabel(
            header, text="Sleep Duration Need",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(side="left")

        hours = duration.get('hours_needed', '7-8 hours')
        ctk.CTkLabel(
            header, text=hours,
            font=ctk.CTkFont(size=16, weight="bold"), text_color="#3b82f6"
        ).pack(side="right")

        # Short sleeper variant check
        if duration.get('short_sleeper_variant'):
            rare_frame = ctk.CTkFrame(frame, fg_color="#1e3a5f", corner_radius=8)
            rare_frame.pack(fill="x", padx=20, pady=5)

            ctk.CTkLabel(
                rare_frame, text="RARE: Natural Short Sleeper Variant Detected",
                font=ctk.CTkFont(size=12, weight="bold"), text_color="#60a5fa"
            ).pack(anchor="w", padx=10, pady=5)

            ctk.CTkLabel(
                rare_frame, text="You carry a rare genetic variant that allows some people to function well on less sleep.",
                font=ctk.CTkFont(size=11), text_color="gray60"
            ).pack(anchor="w", padx=10, pady=(0, 8))

        # Description
        desc = duration.get('description', '')
        if desc:
            ctk.CTkLabel(
                frame, text=desc,
                font=ctk.CTkFont(size=12), text_color="gray60",
                wraplength=700
            ).pack(anchor="w", padx=20, pady=(5, 15))

    def _create_sleep_quality_section(self):
        """Create sleep quality section"""
        quality = self.sleep_data.get('sleep_quality', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(15, 10))

        ctk.CTkLabel(
            header, text="Sleep Quality Genetics",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(side="left")

        score = quality.get('quality_score', 0.5)
        if score >= 0.6:
            quality_text = "Good"
            color = "#22c55e"
        elif score >= 0.45:
            quality_text = "Normal"
            color = "#3b82f6"
        else:
            quality_text = "Variable"
            color = "#eab308"

        ctk.CTkLabel(
            header, text=quality_text,
            font=ctk.CTkFont(size=14, weight="bold"), text_color=color
        ).pack(side="right")

        # Description
        desc = quality.get('description', '')
        if desc:
            ctk.CTkLabel(
                frame, text=desc,
                font=ctk.CTkFont(size=12), text_color="gray60",
                wraplength=700
            ).pack(anchor="w", padx=20, pady=(0, 15))

    def _create_sleep_stages_section(self):
        """Create sleep stages section (deep sleep & REM)"""
        deep = self.sleep_data.get('deep_sleep', {})
        rem = self.sleep_data.get('rem_sleep', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Sleep Architecture",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        stages_frame = ctk.CTkFrame(frame, fg_color="transparent")
        stages_frame.pack(fill="x", padx=20, pady=(0, 15))
        stages_frame.grid_columnconfigure((0, 1), weight=1)

        # Deep sleep card
        deep_card = ctk.CTkFrame(stages_frame, fg_color="gray25", corner_radius=10)
        deep_card.grid(row=0, column=0, sticky="nsew", padx=(0, 5), pady=5)

        ctk.CTkLabel(
            deep_card, text="Deep Sleep (SWS)",
            font=ctk.CTkFont(size=14, weight="bold"), text_color="#6366f1"
        ).pack(anchor="w", padx=12, pady=(10, 5))

        deep_pct = deep.get('percentage', 'Average (20-25%)')
        ctk.CTkLabel(
            deep_card, text=deep_pct,
            font=ctk.CTkFont(size=12, weight="bold")
        ).pack(anchor="w", padx=12)

        deep_desc = deep.get('description', '')
        if deep_desc:
            ctk.CTkLabel(
                deep_card, text=deep_desc,
                font=ctk.CTkFont(size=10), text_color="gray50",
                wraplength=280
            ).pack(anchor="w", padx=12, pady=(5, 10))

        # REM sleep card
        rem_card = ctk.CTkFrame(stages_frame, fg_color="gray25", corner_radius=10)
        rem_card.grid(row=0, column=1, sticky="nsew", padx=(5, 0), pady=5)

        ctk.CTkLabel(
            rem_card, text="REM Sleep",
            font=ctk.CTkFont(size=14, weight="bold"), text_color="#ec4899"
        ).pack(anchor="w", padx=12, pady=(10, 5))

        rem_pct = rem.get('percentage', 'Average (20-25%)')
        ctk.CTkLabel(
            rem_card, text=rem_pct,
            font=ctk.CTkFont(size=12, weight="bold")
        ).pack(anchor="w", padx=12)

        dreaming = rem.get('dreaming', '')
        if dreaming:
            ctk.CTkLabel(
                rem_card, text=f"Dreams: {dreaming}",
                font=ctk.CTkFont(size=10), text_color="gray50"
            ).pack(anchor="w", padx=12, pady=(5, 10))

    def _create_sleep_challenges_section(self):
        """Create sleep challenges section (insomnia, latency, DSPS, shift work)"""
        insomnia = self.sleep_data.get('insomnia_risk', {})
        latency = self.sleep_data.get('sleep_latency', {})
        dsps = self.sleep_data.get('dsps_risk', {})
        shift = self.sleep_data.get('shift_work_tolerance', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Sleep Challenges & Tolerance",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        # Grid of challenge cards
        cards_frame = ctk.CTkFrame(frame, fg_color="transparent")
        cards_frame.pack(fill="x", padx=20, pady=(0, 15))
        cards_frame.grid_columnconfigure((0, 1), weight=1)

        # Insomnia risk
        self._create_challenge_card(
            cards_frame, 0, 0, "Insomnia Risk",
            insomnia.get('risk_level', 'Average'),
            insomnia.get('description', ''),
            self._get_risk_color(insomnia.get('risk_level', 'Average'))
        )

        # Sleep latency
        latency_val = latency.get('latency_minutes', '10-20 min')
        self._create_challenge_card(
            cards_frame, 0, 1, "Time to Fall Asleep",
            latency_val,
            latency.get('description', ''),
            "#3b82f6"
        )

        # DSPS risk
        dsps_risk = dsps.get('risk_level', 'Low')
        self._create_challenge_card(
            cards_frame, 1, 0, "Delayed Phase Risk",
            dsps_risk,
            dsps.get('description', ''),
            self._get_risk_color(dsps_risk)
        )

        # Shift work tolerance
        shift_tol = shift.get('tolerance', 'Moderate')
        tol_colors = {'Good': '#22c55e', 'Moderate': '#eab308', 'Poor': '#ef4444'}
        self._create_challenge_card(
            cards_frame, 1, 1, "Shift Work Tolerance",
            shift_tol,
            f"Jet lag recovery: {shift.get('jet_lag_recovery', 'Average')}",
            tol_colors.get(shift_tol, '#eab308')
        )

    def _create_challenge_card(self, parent, row, col, title, value, desc, color):
        """Create a challenge info card"""
        card = ctk.CTkFrame(parent, fg_color="gray25", corner_radius=10)
        card.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        ctk.CTkLabel(
            card, text=title,
            font=ctk.CTkFont(size=12), text_color="gray50"
        ).pack(anchor="w", padx=12, pady=(10, 2))

        ctk.CTkLabel(
            card, text=value,
            font=ctk.CTkFont(size=14, weight="bold"), text_color=color
        ).pack(anchor="w", padx=12)

        if desc:
            ctk.CTkLabel(
                card, text=desc,
                font=ctk.CTkFont(size=10), text_color="gray50",
                wraplength=260
            ).pack(anchor="w", padx=12, pady=(5, 10))

    def _get_risk_color(self, risk_level: str) -> str:
        """Get color for risk level"""
        colors = {
            'Low': '#22c55e',
            'Lower': '#22c55e',
            'Average': '#eab308',
            'Moderate': '#eab308',
            'Elevated': '#ef4444',
            'High': '#ef4444',
            'Very high': '#dc2626'
        }
        return colors.get(risk_level, '#eab308')

    def _create_caffeine_section(self):
        """Create caffeine and sleep section"""
        caffeine = self.sleep_data.get('caffeine_sleep', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(15, 10))

        ctk.CTkLabel(
            header, text="Caffeine & Sleep",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(side="left")

        metabolism = caffeine.get('metabolism', 'Average')
        met_colors = {'Rapid': '#22c55e', 'Average': '#eab308', 'Slow': '#ef4444'}
        ctk.CTkLabel(
            header, text=f"{metabolism} Metabolizer",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=met_colors.get(metabolism, '#eab308')
        ).pack(side="right")

        # Caffeine cutoff
        cutoff = caffeine.get('evening_cutoff', '2-4 PM')
        cutoff_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
        cutoff_frame.pack(fill="x", padx=20, pady=(0, 10))

        ctk.CTkLabel(
            cutoff_frame, text="Recommended Caffeine Cutoff:",
            font=ctk.CTkFont(size=12), text_color="gray60"
        ).pack(side="left", padx=15, pady=10)

        ctk.CTkLabel(
            cutoff_frame, text=cutoff,
            font=ctk.CTkFont(size=14, weight="bold"), text_color="#8b5cf6"
        ).pack(side="right", padx=15, pady=10)

        # Description
        desc = caffeine.get('description', '')
        if desc:
            ctk.CTkLabel(
                frame, text=desc,
                font=ctk.CTkFont(size=12), text_color="gray60",
                wraplength=700
            ).pack(anchor="w", padx=20, pady=(0, 15))

    def _create_recommendations_section(self):
        """Create personalized recommendations section"""
        recommendations = self.sleep_data.get('recommendations', [])

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Personalized Sleep Recommendations",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        if recommendations:
            for i, rec in enumerate(recommendations):
                rec_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
                rec_frame.pack(fill="x", padx=20, pady=3)

                ctk.CTkLabel(
                    rec_frame, text=f"{i+1}.",
                    font=ctk.CTkFont(size=12, weight="bold"), text_color="#3b82f6"
                ).pack(side="left", padx=(10, 5), pady=8)

                ctk.CTkLabel(
                    rec_frame, text=rec,
                    font=ctk.CTkFont(size=12), text_color="gray60",
                    wraplength=650, justify="left"
                ).pack(side="left", padx=(0, 10), pady=8)
        else:
            ctk.CTkLabel(
                frame, text="Maintain good sleep hygiene: consistent schedule, dark room, cool temperature.",
                font=ctk.CTkFont(size=12), text_color="gray60"
            ).pack(anchor="w", padx=20, pady=(0, 15))

        # Disclaimer
        disclaimer = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
        disclaimer.pack(fill="x", padx=20, pady=(10, 15))

        ctk.CTkLabel(
            disclaimer, text="Note",
            font=ctk.CTkFont(size=11, weight="bold"), text_color="#eab308"
        ).pack(anchor="w", padx=12, pady=(8, 3))

        ctk.CTkLabel(
            disclaimer,
            text="Genetics is just one factor affecting sleep. Environment, lifestyle, stress, and health conditions also play major roles. Consult a sleep specialist for persistent sleep problems.",
            font=ctk.CTkFont(size=10), text_color="gray50",
            wraplength=680, justify="left"
        ).pack(anchor="w", padx=12, pady=(0, 8))

    def _create_markers_list(self, parent, markers):
        """Create expandable markers list"""
        markers_frame = ctk.CTkFrame(parent, fg_color="gray25", corner_radius=8)
        markers_frame.pack(fill="x", padx=20, pady=(5, 15))

        ctk.CTkLabel(
            markers_frame, text="Genetic Markers Analyzed:",
            font=ctk.CTkFont(size=11, weight="bold"), text_color="gray60"
        ).pack(anchor="w", padx=10, pady=(8, 5))

        for marker in markers[:5]:
            row = ctk.CTkFrame(markers_frame, fg_color="transparent")
            row.pack(fill="x", padx=10, pady=1)

            ctk.CTkLabel(
                row, text=f"{marker.get('gene', '')} ({marker.get('rsid', '')})",
                font=ctk.CTkFont(size=10), text_color="gray50"
            ).pack(side="left")

            ctk.CTkLabel(
                row, text=marker.get('genotype', ''),
                font=ctk.CTkFont(size=10, weight="bold")
            ).pack(side="right")

        if len(markers) > 5:
            ctk.CTkLabel(
                markers_frame, text=f"... and {len(markers) - 5} more markers",
                font=ctk.CTkFont(size=10), text_color="gray50"
            ).pack(anchor="w", padx=10, pady=(0, 8))
        else:
            ctk.CTkFrame(markers_frame, height=5, fg_color="transparent").pack()
