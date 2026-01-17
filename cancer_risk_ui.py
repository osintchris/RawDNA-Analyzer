"""
Cancer Risk Genetics UI Module
CustomTkinter frames for displaying cancer risk genetics analysis
"""

import customtkinter as ctk
from typing import Dict, Any, Optional


class CancerRiskGeneticsFrame(ctk.CTkScrollableFrame):
    """Main frame for cancer risk genetics display"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results
        self.configure(fg_color="transparent")
        self.build_ui()

    def build_ui(self):
        """Build the cancer risk genetics UI"""
        # Title
        title = ctk.CTkLabel(
            self,
            text="Cancer Risk Genetics",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(20, 5), padx=20, anchor="w")

        subtitle = ctk.CTkLabel(
            self,
            text="Common genetic variants associated with cancer risk",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle.pack(pady=(0, 10), padx=20, anchor="w")

        # Important disclaimer
        disclaimer = ctk.CTkLabel(
            self,
            text="IMPORTANT: This analyzes common risk variants only. It does NOT test for rare pathogenic mutations (like BRCA1/2 pathogenic variants). Consult a genetic counselor for comprehensive cancer genetic testing.",
            font=ctk.CTkFont(size=11),
            text_color="orange",
            wraplength=700
        )
        disclaimer.pack(pady=(0, 20), padx=20, anchor="w")

        if not self.results:
            no_data = ctk.CTkLabel(
                self,
                text="No DNA data loaded. Please load a DNA file to see cancer risk genetics analysis.",
                font=ctk.CTkFont(size=14)
            )
            no_data.pack(pady=50)
            return

        # Create sections
        self.create_overall_section()
        self.create_breast_section()
        self.create_colorectal_section()
        self.create_prostate_section()
        self.create_lung_section()
        self.create_melanoma_section()
        self.create_thyroid_section()
        self.create_pancreatic_section()
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
        if any(word in value_lower for word in ["below average", "lower", "protective"]):
            return "#4ECDC4"
        elif any(word in value_lower for word in ["elevated", "high"]):
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

    def create_overall_section(self):
        """Create overall summary section"""
        data = self.results.get("overall", {})
        if not data:
            return

        frame = self.create_section_frame("Summary")

        self.create_result_row(
            frame, "Variants Analyzed:",
            str(data.get("total_variants_analyzed", 0))
        )

        elevated = data.get("elevated_risk_cancers", [])
        if elevated:
            elevated_label = ctk.CTkLabel(
                frame,
                text=f"Elevated risk found for: {', '.join(elevated)}",
                font=ctk.CTkFont(size=12),
                text_color="#FF6B6B"
            )
            elevated_label.pack(pady=5, padx=15, anchor="w")
        else:
            normal_label = ctk.CTkLabel(
                frame,
                text="No significantly elevated genetic risk factors detected",
                font=ctk.CTkFont(size=12),
                text_color="#4ECDC4"
            )
            normal_label.pack(pady=5, padx=15, anchor="w")

    def create_cancer_section(self, cancer_type: str, display_name: str):
        """Create a generic cancer section"""
        data = self.results.get(cancer_type, {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return None

        frame = self.create_section_frame(display_name)

        self.create_result_row(
            frame, "Risk Level:",
            data.get("risk_level", "Unknown"),
            f"Score: {data.get('risk_score', 0)}"
        )

        note = data.get("note") or data.get("recommendation")
        if note:
            note_label = ctk.CTkLabel(
                frame,
                text=note,
                font=ctk.CTkFont(size=11),
                text_color="gray",
                wraplength=600
            )
            note_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))
        return frame

    def create_breast_section(self):
        """Create breast cancer section"""
        self.create_cancer_section("breast_cancer", "Breast Cancer")

    def create_colorectal_section(self):
        """Create colorectal cancer section"""
        self.create_cancer_section("colorectal_cancer", "Colorectal Cancer")

    def create_prostate_section(self):
        """Create prostate cancer section"""
        self.create_cancer_section("prostate_cancer", "Prostate Cancer")

    def create_lung_section(self):
        """Create lung cancer section"""
        self.create_cancer_section("lung_cancer", "Lung Cancer")

    def create_melanoma_section(self):
        """Create melanoma section"""
        self.create_cancer_section("melanoma", "Melanoma/Skin Cancer")

    def create_thyroid_section(self):
        """Create thyroid cancer section"""
        self.create_cancer_section("thyroid_cancer", "Thyroid Cancer")

    def create_pancreatic_section(self):
        """Create pancreatic cancer section"""
        self.create_cancer_section("pancreatic_cancer", "Pancreatic Cancer")

    def create_recommendations_section(self):
        """Create recommendations section"""
        data = self.results.get("overall", {})
        recommendations = data.get("recommendations", [])
        if not recommendations:
            return

        frame = self.create_section_frame("Recommendations")

        for rec in recommendations:
            rec_label = ctk.CTkLabel(
                frame,
                text=f"  {rec}",
                font=ctk.CTkFont(size=12),
                text_color="#4ECDC4",
                wraplength=600
            )
            rec_label.pack(pady=3, padx=15, anchor="w")

        # Genetic counseling note
        note = ctk.CTkLabel(
            frame,
            text="For comprehensive cancer genetic testing, consult a certified genetic counselor.",
            font=ctk.CTkFont(size=11),
            text_color="orange"
        )
        note.pack(pady=(10, 15), padx=15, anchor="w")


class CancerRiskSummaryCard(ctk.CTkFrame):
    """Compact summary card for cancer risk genetics"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results or {}
        self.build_ui()

    def build_ui(self):
        """Build the summary card UI"""
        title = ctk.CTkLabel(
            self,
            text="Cancer Risk Genetics",
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

        # Show elevated risks
        elevated = self.results.get("overall", {}).get("elevated_risk_cancers", [])
        if elevated:
            for cancer in elevated[:3]:
                label = ctk.CTkLabel(
                    self,
                    text=f"Elevated: {cancer}",
                    font=ctk.CTkFont(size=11),
                    text_color="#FF6B6B"
                )
                label.pack(pady=2, padx=15, anchor="w")
        else:
            label = ctk.CTkLabel(
                self,
                text="No elevated genetic risks",
                font=ctk.CTkFont(size=11),
                text_color="#4ECDC4"
            )
            label.pack(pady=2, padx=15, anchor="w")

        ctk.CTkLabel(self, text="").pack(pady=(0, 10))
