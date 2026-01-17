#!/usr/bin/env python3
"""
Carrier Status UI Components
Comprehensive display for genetic disease carrier screening results
"""

import customtkinter as ctk
from typing import Dict, Any


class CarrierStatusExpandedFrame(ctk.CTkFrame):
    """Comprehensive carrier status display"""

    def __init__(self, parent, carrier_data: Dict[str, Any], dna_data: dict):
        super().__init__(parent, fg_color="transparent")

        self.carrier_data = carrier_data
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
        self._create_summary()
        self._create_high_risk_section()
        self._create_carrier_section()
        self._create_clear_section()
        self._create_recommendations()

    def _create_header(self):
        """Create page header"""
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header, text="Carrier Status Screening",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            header, text="Genetic disease carrier screening for family planning",
            font=ctk.CTkFont(size=14), text_color="gray60"
        ).pack(anchor="w")

    def _create_summary(self):
        """Create summary statistics"""
        summary = self.carrier_data.get('summary', {})

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(15, 10))

        ctk.CTkLabel(
            header, text="Screening Summary",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(side="left")

        # Stats grid
        stats_frame = ctk.CTkFrame(frame, fg_color="transparent")
        stats_frame.pack(fill="x", padx=20, pady=(0, 15))
        stats_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Total conditions
        self._create_stat_box(stats_frame, 0, 0, "Conditions Tested",
            str(summary.get('total_conditions_tested', 0)), "#3b82f6")

        # Clear
        self._create_stat_box(stats_frame, 0, 1, "Clear",
            str(summary.get('clear_conditions', 0)), "#22c55e")

        # Carriers
        carriers = summary.get('carriers_detected', 0)
        carrier_color = "#eab308" if carriers > 0 else "#22c55e"
        self._create_stat_box(stats_frame, 0, 2, "Carrier Status",
            str(carriers), carrier_color)

        # High risk
        high_risk = summary.get('high_risk_detected', 0)
        risk_color = "#ef4444" if high_risk > 0 else "#22c55e"
        self._create_stat_box(stats_frame, 0, 3, "High Risk",
            str(high_risk), risk_color)

    def _create_stat_box(self, parent, row, col, label, value, color):
        """Create a stat box"""
        box = ctk.CTkFrame(parent, fg_color="gray25", corner_radius=8)
        box.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        ctk.CTkLabel(
            box, text=value,
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=color
        ).pack(pady=(12, 2))

        ctk.CTkLabel(
            box, text=label,
            font=ctk.CTkFont(size=11), text_color="gray60"
        ).pack(pady=(0, 12))

    def _create_high_risk_section(self):
        """Create high risk conditions section"""
        high_risk = self.carrier_data.get('high_risk_conditions', [])
        if not high_risk:
            return

        frame = ctk.CTkFrame(self.scroll, fg_color="#3f1f1f", corner_radius=12)
        frame.pack(fill="x", pady=10)

        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(15, 10))

        ctk.CTkLabel(
            header, text="HIGH RISK CONDITIONS DETECTED",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#ef4444"
        ).pack(side="left")

        ctk.CTkLabel(
            header, text="Consult genetic counselor",
            font=ctk.CTkFont(size=12),
            text_color="#ef4444"
        ).pack(side="right")

        for condition in high_risk:
            self._create_condition_card(frame, condition, is_high_risk=True)

        ctk.CTkFrame(frame, height=10, fg_color="transparent").pack()

    def _create_carrier_section(self):
        """Create carrier status section"""
        carriers = self.carrier_data.get('carriers_found', [])
        if not carriers:
            return

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(15, 10))

        ctk.CTkLabel(
            header, text="Carrier Status Detected",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#eab308"
        ).pack(side="left")

        ctk.CTkLabel(
            header, text="No symptoms expected - relevant for family planning",
            font=ctk.CTkFont(size=11), text_color="gray60"
        ).pack(side="right")

        for condition in carriers:
            self._create_condition_card(frame, condition, is_high_risk=False)

        ctk.CTkFrame(frame, height=10, fg_color="transparent").pack()

    def _create_condition_card(self, parent, condition, is_high_risk=False):
        """Create a condition detail card"""
        border_color = "#ef4444" if is_high_risk else "#eab308"
        card = ctk.CTkFrame(parent, fg_color="gray25", corner_radius=10,
                           border_width=2, border_color=border_color)
        card.pack(fill="x", padx=20, pady=5)

        # Header row
        header = ctk.CTkFrame(card, fg_color="transparent")
        header.pack(fill="x", padx=15, pady=(12, 5))

        ctk.CTkLabel(
            header, text=condition.get('condition', 'Unknown'),
            font=ctk.CTkFont(size=16, weight="bold")
        ).pack(side="left")

        status_color = "#ef4444" if is_high_risk else "#eab308"
        ctk.CTkLabel(
            header, text=condition.get('status', 'Unknown'),
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=status_color
        ).pack(side="right")

        # Gene and inheritance
        info_row = ctk.CTkFrame(card, fg_color="transparent")
        info_row.pack(fill="x", padx=15)

        ctk.CTkLabel(
            info_row, text=f"Gene: {condition.get('gene', 'Unknown')}",
            font=ctk.CTkFont(size=12), text_color="gray60"
        ).pack(side="left")

        ctk.CTkLabel(
            info_row, text=condition.get('inheritance', ''),
            font=ctk.CTkFont(size=11), text_color="gray50"
        ).pack(side="right")

        # Description
        desc = condition.get('description', '')
        if desc:
            ctk.CTkLabel(
                card, text=desc,
                font=ctk.CTkFont(size=12), text_color="gray60",
                wraplength=700, justify="left"
            ).pack(anchor="w", padx=15, pady=(5, 0))

        # Variants found
        variants = condition.get('variants_found', [])
        if variants:
            var_frame = ctk.CTkFrame(card, fg_color="gray30", corner_radius=6)
            var_frame.pack(fill="x", padx=15, pady=10)

            ctk.CTkLabel(
                var_frame, text="Variants Detected:",
                font=ctk.CTkFont(size=11, weight="bold"), text_color="gray70"
            ).pack(anchor="w", padx=10, pady=(8, 5))

            for var in variants:
                var_row = ctk.CTkFrame(var_frame, fg_color="transparent")
                var_row.pack(fill="x", padx=10, pady=2)

                ctk.CTkLabel(
                    var_row, text=f"{var.get('name', '')} ({var.get('rsid', '')})",
                    font=ctk.CTkFont(size=11, weight="bold")
                ).pack(side="left")

                ctk.CTkLabel(
                    var_row, text=f"Genotype: {var.get('genotype', '')}",
                    font=ctk.CTkFont(size=11), text_color="gray60"
                ).pack(side="right")

            ctk.CTkFrame(var_frame, height=8, fg_color="transparent").pack()

        # Carrier frequency
        freq = condition.get('carrier_frequency', {})
        if freq:
            freq_text = "Carrier frequency: " + ", ".join([f"{k}: {v}" for k, v in list(freq.items())[:3]])
            ctk.CTkLabel(
                card, text=freq_text,
                font=ctk.CTkFont(size=10), text_color="gray50"
            ).pack(anchor="w", padx=15, pady=(0, 5))

        # Implications
        implications = condition.get('implications', [])
        if implications:
            imp_frame = ctk.CTkFrame(card, fg_color="transparent")
            imp_frame.pack(fill="x", padx=15, pady=(0, 12))

            ctk.CTkLabel(
                imp_frame, text="What this means:",
                font=ctk.CTkFont(size=11, weight="bold"), text_color="#3b82f6"
            ).pack(anchor="w")

            for imp in implications[:4]:
                ctk.CTkLabel(
                    imp_frame, text=f"  - {imp}",
                    font=ctk.CTkFont(size=11), text_color="gray60",
                    wraplength=650, justify="left"
                ).pack(anchor="w")

    def _create_clear_section(self):
        """Create clear conditions section"""
        clear = self.carrier_data.get('conditions_clear', [])
        if not clear:
            return

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        # Collapsible header
        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(15, 10))

        ctk.CTkLabel(
            header, text="Conditions Clear",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#22c55e"
        ).pack(side="left")

        ctk.CTkLabel(
            header, text=f"{len(clear)} conditions - no pathogenic variants detected",
            font=ctk.CTkFont(size=12), text_color="gray60"
        ).pack(side="right")

        # List clear conditions
        list_frame = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
        list_frame.pack(fill="x", padx=20, pady=(0, 15))

        for i, condition in enumerate(clear):
            row = ctk.CTkFrame(list_frame, fg_color="transparent")
            row.pack(fill="x", padx=15, pady=3)

            ctk.CTkLabel(
                row, text="[checkmark]",
                font=ctk.CTkFont(size=14),
                text_color="#22c55e"
            ).pack(side="left")

            ctk.CTkLabel(
                row, text=f"  {condition.get('condition', '')}",
                font=ctk.CTkFont(size=13)
            ).pack(side="left")

            ctk.CTkLabel(
                row, text=f"({condition.get('gene', '')})",
                font=ctk.CTkFont(size=11), text_color="gray50"
            ).pack(side="right")

        ctk.CTkFrame(list_frame, height=5, fg_color="transparent").pack()

    def _create_recommendations(self):
        """Create recommendations section"""
        recommendations = self.carrier_data.get('recommendations', [])

        frame = ctk.CTkFrame(self.scroll, fg_color="gray20", corner_radius=12)
        frame.pack(fill="x", pady=10)

        ctk.CTkLabel(
            frame, text="Recommendations",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(anchor="w", padx=20, pady=(15, 10))

        if recommendations:
            for rec in recommendations:
                rec_row = ctk.CTkFrame(frame, fg_color="transparent")
                rec_row.pack(fill="x", padx=20, pady=3)

                ctk.CTkLabel(
                    rec_row, text="[>]",
                    font=ctk.CTkFont(size=14),
                    text_color="#3b82f6"
                ).pack(side="left")

                ctk.CTkLabel(
                    rec_row, text=f"  {rec}",
                    font=ctk.CTkFont(size=13)
                ).pack(side="left")
        else:
            ctk.CTkLabel(
                frame, text="No specific recommendations based on your results.",
                font=ctk.CTkFont(size=13), text_color="gray60"
            ).pack(anchor="w", padx=20)

        # Disclaimer
        disclaimer = ctk.CTkFrame(frame, fg_color="gray25", corner_radius=8)
        disclaimer.pack(fill="x", padx=20, pady=(10, 15))

        ctk.CTkLabel(
            disclaimer, text="Important Disclaimer",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#eab308"
        ).pack(anchor="w", padx=15, pady=(10, 5))

        disclaimer_text = (
            "This carrier screening is for informational purposes only. Not all disease-causing variants are tested. "
            "A negative result does not eliminate carrier risk. For comprehensive carrier screening, consult a "
            "genetic counselor and consider clinical-grade expanded carrier screening panels that test 100+ conditions."
        )
        ctk.CTkLabel(
            disclaimer, text=disclaimer_text,
            font=ctk.CTkFont(size=11), text_color="gray60",
            wraplength=700, justify="left"
        ).pack(anchor="w", padx=15, pady=(0, 10))
