"""
Cardiovascular Genetics UI Module
CustomTkinter frames for displaying cardiovascular genetics analysis
"""

import customtkinter as ctk
from typing import Dict, Any, Optional


class CardiovascularGeneticsFrame(ctk.CTkScrollableFrame):
    """Main frame for cardiovascular genetics display"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results
        self.configure(fg_color="transparent")
        self.build_ui()

    def build_ui(self):
        """Build the cardiovascular genetics UI"""
        # Title
        title = ctk.CTkLabel(
            self,
            text="Cardiovascular Genetics",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(20, 5), padx=20, anchor="w")

        subtitle = ctk.CTkLabel(
            self,
            text="Genetic factors affecting heart health, cholesterol, blood pressure, and clotting",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle.pack(pady=(0, 20), padx=20, anchor="w")

        if not self.results:
            no_data = ctk.CTkLabel(
                self,
                text="No DNA data loaded. Please load a DNA file to see cardiovascular genetics analysis.",
                font=ctk.CTkFont(size=14)
            )
            no_data.pack(pady=50)
            return

        # Create sections
        self.create_cad_section()
        self.create_cholesterol_section()
        self.create_blood_pressure_section()
        self.create_stroke_section()
        self.create_afib_section()
        self.create_clotting_section()
        self.create_recommendations_section()

    def create_section_frame(self, title: str, icon: str = "") -> ctk.CTkFrame:
        """Create a styled section frame"""
        frame = ctk.CTkFrame(self)
        frame.pack(fill="x", padx=20, pady=10)

        header = ctk.CTkLabel(
            frame,
            text=f"{icon} {title}" if icon else title,
            font=ctk.CTkFont(size=18, weight="bold")
        )
        header.pack(pady=(15, 10), padx=15, anchor="w")

        return frame

    def create_result_row(self, parent: ctk.CTkFrame, label: str, value: str,
                          detail: str = "", color: str = None):
        """Create a row displaying a result"""
        row = ctk.CTkFrame(parent, fg_color="transparent")
        row.pack(fill="x", padx=15, pady=5)

        label_widget = ctk.CTkLabel(
            row,
            text=label,
            font=ctk.CTkFont(size=14, weight="bold"),
            width=200,
            anchor="w"
        )
        label_widget.pack(side="left")

        value_str = str(value) if value is not None else "Unknown"
        value_color = color if color else self.get_color_for_value(value_str)
        value_widget = ctk.CTkLabel(
            row,
            text=value_str,
            font=ctk.CTkFont(size=14),
            text_color=value_color
        )
        value_widget.pack(side="left", padx=(10, 0))

        if detail:
            detail_widget = ctk.CTkLabel(
                row,
                text=f"({detail})",
                font=ctk.CTkFont(size=12),
                text_color="gray"
            )
            detail_widget.pack(side="left", padx=(10, 0))

    def get_color_for_value(self, value: str) -> str:
        """Get color based on value content"""
        value_lower = str(value).lower()
        if any(word in value_lower for word in ["below average", "lower", "protective", "normal"]):
            return "#4ECDC4"
        elif any(word in value_lower for word in ["elevated", "higher", "high", "detected"]):
            return "#FF6B6B"
        elif any(word in value_lower for word in ["average", "population", "slight"]):
            return "#FFE66D"
        return "white"

    def create_snp_details(self, parent: ctk.CTkFrame, snps: list):
        """Create SNP details display"""
        if not snps:
            return

        details_frame = ctk.CTkFrame(parent, fg_color=("gray90", "gray20"))
        details_frame.pack(fill="x", padx=15, pady=(5, 15))

        header = ctk.CTkLabel(
            details_frame,
            text="Analyzed Variants:",
            font=ctk.CTkFont(size=12, weight="bold")
        )
        header.pack(pady=(10, 5), padx=10, anchor="w")

        for snp in snps[:5]:
            snp_text = f"{snp.get('rsid', 'Unknown')}: {snp.get('genotype', 'N/A')}"
            if snp.get('gene'):
                snp_text += f" ({snp.get('gene')})"

            snp_label = ctk.CTkLabel(
                details_frame,
                text=snp_text,
                font=ctk.CTkFont(size=11),
                text_color="gray"
            )
            snp_label.pack(pady=2, padx=15, anchor="w")

        if len(snps) > 5:
            more_label = ctk.CTkLabel(
                details_frame,
                text=f"... and {len(snps) - 5} more variants",
                font=ctk.CTkFont(size=11),
                text_color="gray"
            )
            more_label.pack(pady=(2, 10), padx=15, anchor="w")

    def create_cad_section(self):
        """Create coronary artery disease section"""
        data = self.results.get("coronary_artery_disease", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Coronary Artery Disease Risk")

        self.create_result_row(
            frame, "CAD Risk Level:",
            data.get("risk_level", "Unknown"),
            f"Score: {data.get('risk_score', 0)}"
        )

        if data.get("has_lpa_risk"):
            lpa_alert = ctk.CTkLabel(
                frame,
                text="Elevated Lp(a) genetic variant detected - consider Lp(a) blood test",
                font=ctk.CTkFont(size=12),
                text_color="#FF6B6B"
            )
            lpa_alert.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_cholesterol_section(self):
        """Create cholesterol section"""
        frame = self.create_section_frame("Cholesterol Genetics")

        # LDL
        ldl_data = self.results.get("ldl_cholesterol", {})
        if ldl_data.get("variants_analyzed", 0) > 0:
            self.create_result_row(
                frame, "LDL Cholesterol:",
                ldl_data.get("tendency", "Unknown")
            )

        # HDL
        hdl_data = self.results.get("hdl_cholesterol", {})
        if hdl_data.get("variants_analyzed", 0) > 0:
            self.create_result_row(
                frame, "HDL Cholesterol:",
                hdl_data.get("tendency", "Unknown")
            )

        # Triglycerides
        tg_data = self.results.get("triglycerides", {})
        if tg_data.get("variants_analyzed", 0) > 0:
            self.create_result_row(
                frame, "Triglycerides:",
                tg_data.get("tendency", "Unknown")
            )

        # Show SNPs from all three
        all_snps = (ldl_data.get("snps_analyzed", []) +
                   hdl_data.get("snps_analyzed", []) +
                   tg_data.get("snps_analyzed", []))
        self.create_snp_details(frame, all_snps)

    def create_blood_pressure_section(self):
        """Create blood pressure section"""
        data = self.results.get("blood_pressure", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Blood Pressure Genetics")

        self.create_result_row(
            frame, "BP Tendency:",
            data.get("tendency", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        beta_response = data.get("beta_blocker_response", "normal")
        if beta_response != "normal":
            self.create_result_row(
                frame, "Beta-blocker Response:",
                beta_response.replace("_", " ").title()
            )

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_stroke_section(self):
        """Create stroke risk section"""
        data = self.results.get("stroke", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Stroke Risk")

        self.create_result_row(
            frame, "Stroke Risk:",
            data.get("risk_level", "Unknown"),
            f"Score: {data.get('risk_score', 0)}"
        )

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_afib_section(self):
        """Create atrial fibrillation section"""
        data = self.results.get("atrial_fibrillation", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Atrial Fibrillation Risk")

        self.create_result_row(
            frame, "AFib Risk:",
            data.get("risk_level", "Unknown"),
            f"Score: {data.get('risk_score', 0)}"
        )

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_clotting_section(self):
        """Create clotting risk section"""
        data = self.results.get("clotting_risk", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Clotting / Thrombosis Risk")

        self.create_result_row(
            frame, "Thrombosis Risk:",
            data.get("risk_level", "Unknown")
        )

        if data.get("has_factor_v_leiden"):
            fvl_alert = ctk.CTkLabel(
                frame,
                text="Factor V Leiden DETECTED - significantly increased VTE risk",
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color="#FF6B6B"
            )
            fvl_alert.pack(pady=5, padx=15, anchor="w")

        if data.get("has_prothrombin_mutation"):
            f2_alert = ctk.CTkLabel(
                frame,
                text="Prothrombin G20210A DETECTED - increased VTE risk",
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color="#FF6B6B"
            )
            f2_alert.pack(pady=5, padx=15, anchor="w")

        note = data.get("note")
        if note:
            note_label = ctk.CTkLabel(
                frame,
                text=note,
                font=ctk.CTkFont(size=11),
                text_color="orange",
                wraplength=600
            )
            note_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_recommendations_section(self):
        """Create recommendations section"""
        data = self.results.get("overall", {})
        recommendations = data.get("recommendations", [])
        if not recommendations:
            return

        frame = self.create_section_frame("Personalized Recommendations")

        for rec in recommendations:
            rec_label = ctk.CTkLabel(
                frame,
                text=f"  {rec}",
                font=ctk.CTkFont(size=12),
                text_color="#4ECDC4",
                wraplength=600
            )
            rec_label.pack(pady=3, padx=15, anchor="w")

        # Disclaimer
        disclaimer = ctk.CTkLabel(
            frame,
            text="Discuss cardiovascular risk factors with your healthcare provider.",
            font=ctk.CTkFont(size=11),
            text_color="orange"
        )
        disclaimer.pack(pady=(10, 15), padx=15, anchor="w")


class CardiovascularSummaryCard(ctk.CTkFrame):
    """Compact summary card for cardiovascular genetics"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results or {}
        self.build_ui()

    def build_ui(self):
        """Build the summary card UI"""
        title = ctk.CTkLabel(
            self,
            text="Cardiovascular Genetics",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        title.pack(pady=(15, 10), padx=15, anchor="w")

        if not self.results:
            no_data = ctk.CTkLabel(
                self,
                text="No data available",
                font=ctk.CTkFont(size=12),
                text_color="gray"
            )
            no_data.pack(pady=(0, 15), padx=15, anchor="w")
            return

        # Key findings
        cad = self.results.get("coronary_artery_disease", {})
        if cad.get("risk_level"):
            cad_label = ctk.CTkLabel(
                self,
                text=f"CAD: {cad['risk_level']}",
                font=ctk.CTkFont(size=11)
            )
            cad_label.pack(pady=2, padx=15, anchor="w")

        bp = self.results.get("blood_pressure", {})
        if bp.get("tendency"):
            bp_label = ctk.CTkLabel(
                self,
                text=f"BP: {bp['tendency']}",
                font=ctk.CTkFont(size=11),
                text_color="gray"
            )
            bp_label.pack(pady=2, padx=15, anchor="w")

        clotting = self.results.get("clotting_risk", {})
        if clotting.get("has_factor_v_leiden") or clotting.get("has_prothrombin_mutation"):
            alert = ctk.CTkLabel(
                self,
                text="Thrombophilia variant detected",
                font=ctk.CTkFont(size=11),
                text_color="#FF6B6B"
            )
            alert.pack(pady=2, padx=15, anchor="w")

        ctk.CTkLabel(self, text="").pack(pady=(0, 10))
