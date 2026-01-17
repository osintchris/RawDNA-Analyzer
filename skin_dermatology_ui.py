"""
Skin & Dermatology Genetics UI Module
CustomTkinter frames for displaying skin genetics analysis
"""

import customtkinter as ctk
from typing import Dict, Any, Optional


class SkinDermatologyFrame(ctk.CTkScrollableFrame):
    """Main frame for skin dermatology genetics display"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results
        self.configure(fg_color="transparent")
        self.build_ui()

    def build_ui(self):
        """Build the skin dermatology genetics UI"""
        # Title
        title = ctk.CTkLabel(
            self,
            text="Skin & Dermatology Genetics",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(20, 5), padx=20, anchor="w")

        subtitle = ctk.CTkLabel(
            self,
            text="Genetic factors affecting skin aging, UV sensitivity, and skin conditions",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle.pack(pady=(0, 20), padx=20, anchor="w")

        if not self.results:
            no_data = ctk.CTkLabel(
                self,
                text="No DNA data loaded. Please load a DNA file to see skin genetics analysis.",
                font=ctk.CTkFont(size=14)
            )
            no_data.pack(pady=50)
            return

        # Create sections
        self.create_summary_section()
        self.create_aging_section()
        self.create_uv_section()
        self.create_eczema_section()
        self.create_psoriasis_section()
        self.create_rosacea_section()
        self.create_acne_section()
        self.create_elasticity_section()
        self.create_vitamin_d_section()
        self.create_recommendations_section()

    def create_section_frame(self, title: str) -> ctk.CTkFrame:
        """Create a styled section frame"""
        frame = ctk.CTkFrame(self)
        frame.pack(fill="x", padx=20, pady=10)

        header = ctk.CTkLabel(
            frame,
            text=title,
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
        if any(word in value_lower for word in ["good", "lower", "slower", "efficient", "less"]):
            return "#4ECDC4"
        elif any(word in value_lower for word in ["elevated", "high", "faster", "reduced", "prone"]):
            return "#FF6B6B"
        elif any(word in value_lower for word in ["average", "normal", "moderate"]):
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

    def create_summary_section(self):
        """Create summary section"""
        data = self.results.get("overall", {})
        if not data:
            return

        frame = self.create_section_frame("Skin Profile Summary")

        summary = data.get("skin_type_summary", "")
        if summary:
            summary_label = ctk.CTkLabel(
                frame,
                text=summary,
                font=ctk.CTkFont(size=14),
                text_color="white"
            )
            summary_label.pack(pady=5, padx=15, anchor="w")

        self.create_result_row(
            frame, "Variants Analyzed:",
            str(data.get("total_variants_analyzed", 0))
        )

    def create_aging_section(self):
        """Create skin aging section"""
        data = self.results.get("skin_aging", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Skin Aging Genetics")

        self.create_result_row(
            frame, "Aging Tendency:",
            data.get("tendency", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        recs = data.get("recommendations", [])
        if recs:
            for rec in recs[:2]:
                rec_label = ctk.CTkLabel(
                    frame,
                    text=f"  {rec}",
                    font=ctk.CTkFont(size=11),
                    text_color="gray"
                )
                rec_label.pack(pady=2, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_uv_section(self):
        """Create UV sensitivity section"""
        data = self.results.get("uv_sensitivity", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("UV Sensitivity & Sun Damage")

        self.create_result_row(
            frame, "UV Sensitivity:",
            data.get("level", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        if data.get("has_mc1r_variant"):
            mc1r_label = ctk.CTkLabel(
                frame,
                text="MC1R variant detected - fair skin/red hair genetics",
                font=ctk.CTkFont(size=12),
                text_color="#FF6B6B"
            )
            mc1r_label.pack(pady=5, padx=15, anchor="w")

        if data.get("burn_easily"):
            burn_label = ctk.CTkLabel(
                frame,
                text="You likely burn easily in the sun",
                font=ctk.CTkFont(size=11),
                text_color="orange"
            )
            burn_label.pack(pady=2, padx=15, anchor="w")

        rec = data.get("recommendation", "")
        if rec:
            rec_label = ctk.CTkLabel(
                frame,
                text=rec,
                font=ctk.CTkFont(size=12),
                text_color="#4ECDC4"
            )
            rec_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_eczema_section(self):
        """Create eczema risk section"""
        data = self.results.get("eczema_risk", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Eczema / Atopic Dermatitis Risk")

        self.create_result_row(
            frame, "Eczema Risk:",
            data.get("risk_level", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        if data.get("has_filaggrin_variant"):
            flg_label = ctk.CTkLabel(
                frame,
                text="Filaggrin variant detected - skin barrier may be impaired",
                font=ctk.CTkFont(size=12),
                text_color="#FF6B6B"
            )
            flg_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_psoriasis_section(self):
        """Create psoriasis risk section"""
        data = self.results.get("psoriasis_risk", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Psoriasis Risk")

        self.create_result_row(
            frame, "Psoriasis Risk:",
            data.get("risk_level", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_rosacea_section(self):
        """Create rosacea risk section"""
        data = self.results.get("rosacea_risk", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Rosacea Risk")

        self.create_result_row(
            frame, "Rosacea Risk:",
            data.get("risk_level", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_acne_section(self):
        """Create acne tendency section"""
        data = self.results.get("acne_tendency", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Acne Tendency")

        self.create_result_row(
            frame, "Acne Tendency:",
            data.get("tendency", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_elasticity_section(self):
        """Create skin elasticity section"""
        data = self.results.get("skin_elasticity", {})
        stretch = self.results.get("stretch_marks", {})

        if (not data or data.get("variants_analyzed", 0) == 0) and \
           (not stretch or stretch.get("variants_analyzed", 0) == 0):
            return

        frame = self.create_section_frame("Skin Elasticity & Stretch Marks")

        if data.get("variants_analyzed", 0) > 0:
            self.create_result_row(
                frame, "Skin Elasticity:",
                data.get("level", "Unknown")
            )

            if data.get("cellulite_prone"):
                cellulite_label = ctk.CTkLabel(
                    frame,
                    text="May be more prone to cellulite",
                    font=ctk.CTkFont(size=11),
                    text_color="gray"
                )
                cellulite_label.pack(pady=2, padx=15, anchor="w")

        if stretch.get("variants_analyzed", 0) > 0:
            self.create_result_row(
                frame, "Stretch Mark Susceptibility:",
                stretch.get("susceptibility", "Unknown")
            )

        all_snps = data.get("snps_analyzed", []) + stretch.get("snps_analyzed", [])
        self.create_snp_details(frame, all_snps)

    def create_vitamin_d_section(self):
        """Create vitamin D synthesis section"""
        data = self.results.get("vitamin_d_synthesis", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Vitamin D Skin Synthesis")

        self.create_result_row(
            frame, "Vitamin D Synthesis:",
            data.get("efficiency", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        if data.get("may_need_supplementation"):
            supp_label = ctk.CTkLabel(
                frame,
                text="May benefit from vitamin D supplementation",
                font=ctk.CTkFont(size=11),
                text_color="orange"
            )
            supp_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_recommendations_section(self):
        """Create recommendations section"""
        data = self.results.get("overall", {})
        recommendations = data.get("recommendations", [])
        if not recommendations:
            return

        frame = self.create_section_frame("Personalized Skincare Recommendations")

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
            text="Consult a dermatologist for personalized skincare advice.",
            font=ctk.CTkFont(size=11),
            text_color="orange"
        )
        disclaimer.pack(pady=(10, 15), padx=15, anchor="w")


class SkinDermatologySummaryCard(ctk.CTkFrame):
    """Compact summary card for skin dermatology genetics"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results or {}
        self.build_ui()

    def build_ui(self):
        """Build the summary card UI"""
        title = ctk.CTkLabel(
            self,
            text="Skin Genetics",
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
        uv = self.results.get("uv_sensitivity", {})
        if uv.get("level"):
            uv_label = ctk.CTkLabel(
                self,
                text=f"UV: {uv['level']}",
                font=ctk.CTkFont(size=11)
            )
            uv_label.pack(pady=2, padx=15, anchor="w")

        aging = self.results.get("skin_aging", {})
        if aging.get("tendency"):
            aging_label = ctk.CTkLabel(
                self,
                text=f"Aging: {aging['tendency']}",
                font=ctk.CTkFont(size=11),
                text_color="gray"
            )
            aging_label.pack(pady=2, padx=15, anchor="w")

        ctk.CTkLabel(self, text="").pack(pady=(0, 10))
