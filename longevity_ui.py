"""
Longevity Genetics UI Module
CustomTkinter frames for displaying longevity and aging genetics analysis
"""

import customtkinter as ctk
from typing import Dict, Any, Optional


class LongevityGeneticsFrame(ctk.CTkScrollableFrame):
    """Main frame for longevity genetics display"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results
        self.configure(fg_color="transparent")
        self.build_ui()

    def build_ui(self):
        """Build the longevity genetics UI"""
        # Title
        title = ctk.CTkLabel(
            self,
            text="Longevity & Aging Genetics",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(20, 5), padx=20, anchor="w")

        subtitle = ctk.CTkLabel(
            self,
            text="Genetic factors influencing lifespan, cellular aging, and longevity pathways",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle.pack(pady=(0, 20), padx=20, anchor="w")

        if not self.results:
            no_data = ctk.CTkLabel(
                self,
                text="No DNA data loaded. Please load a DNA file to see longevity genetics analysis.",
                font=ctk.CTkFont(size=14)
            )
            no_data.pack(pady=50)
            return

        # Create sections
        self.create_overall_section()
        self.create_telomere_section()
        self.create_sirtuin_section()
        self.create_foxo_section()
        self.create_igf1_section()
        self.create_autophagy_section()
        self.create_mitochondrial_section()
        self.create_inflammaging_section()
        self.create_klotho_section()
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
        if any(word in value_lower for word in ["exceptional", "favorable", "enhanced", "optimal", "positive", "higher", "longevity"]):
            return "#4ECDC4"
        elif any(word in value_lower for word in ["reduced", "below", "impaired", "lower", "pro-inflammatory"]):
            return "#FF6B6B"
        elif any(word in value_lower for word in ["normal", "average", "typical"]):
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
        """Create overall longevity score section"""
        data = self.results.get("overall", {})
        if not data:
            return

        frame = self.create_section_frame("Overall Longevity Profile")

        self.create_result_row(
            frame, "Longevity Assessment:",
            data.get("assessment", "Unknown"),
            f"Score: {data.get('total_score', 0)}"
        )

        percentile = data.get("percentile")
        if percentile:
            self.create_result_row(
                frame, "Population Percentile:",
                f"{percentile}th percentile"
            )

        self.create_result_row(
            frame, "Variants Analyzed:",
            str(data.get("variants_analyzed", 0))
        )

    def create_telomere_section(self):
        """Create telomere length section"""
        data = self.results.get("telomere_length", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Telomere Length Genetics")

        self.create_result_row(
            frame, "Telomere Assessment:",
            data.get("assessment", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_sirtuin_section(self):
        """Create sirtuin pathway section"""
        data = self.results.get("sirtuin_pathway", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Sirtuin Pathway (Caloric Restriction)")

        self.create_result_row(
            frame, "Sirtuin Assessment:",
            data.get("assessment", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        # Add info about sirtuins
        info_label = ctk.CTkLabel(
            frame,
            text="Sirtuins regulate cellular metabolism and mimic effects of caloric restriction",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        )
        info_label.pack(pady=(5, 10), padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_foxo_section(self):
        """Create FOXO pathway section"""
        data = self.results.get("foxo_pathway", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("FOXO Longevity Pathway")

        self.create_result_row(
            frame, "FOXO Assessment:",
            data.get("assessment", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        if data.get("has_centenarian_variant"):
            special_label = ctk.CTkLabel(
                frame,
                text="You carry the FOXO3 longevity variant commonly found in centenarians!",
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color="#4ECDC4"
            )
            special_label.pack(pady=(5, 10), padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_igf1_section(self):
        """Create IGF-1 pathway section"""
        data = self.results.get("igf1_pathway", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("IGF-1/Growth Hormone Pathway")

        self.create_result_row(
            frame, "IGF-1 Assessment:",
            data.get("assessment", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        info_label = ctk.CTkLabel(
            frame,
            text="Lower IGF-1 signaling is associated with increased lifespan in multiple species",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        )
        info_label.pack(pady=(5, 10), padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_autophagy_section(self):
        """Create autophagy section"""
        data = self.results.get("autophagy", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Autophagy (Cellular Cleanup)")

        self.create_result_row(
            frame, "Autophagy Assessment:",
            data.get("assessment", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        info_label = ctk.CTkLabel(
            frame,
            text="Autophagy removes damaged cells and proteins - enhanced by fasting and exercise",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        )
        info_label.pack(pady=(5, 10), padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_mitochondrial_section(self):
        """Create mitochondrial function section"""
        data = self.results.get("mitochondrial_function", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Mitochondrial Function")

        self.create_result_row(
            frame, "Mitochondrial Assessment:",
            data.get("assessment", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_inflammaging_section(self):
        """Create inflammaging section"""
        data = self.results.get("inflammaging", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Inflammaging (Chronic Inflammation)")

        self.create_result_row(
            frame, "Inflammation Assessment:",
            data.get("assessment", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        info_label = ctk.CTkLabel(
            frame,
            text="Low-grade chronic inflammation accelerates aging - can be modified by diet",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        )
        info_label.pack(pady=(5, 10), padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_klotho_section(self):
        """Create klotho section"""
        data = self.results.get("klotho", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Klotho Anti-Aging Hormone")

        self.create_result_row(
            frame, "Klotho Assessment:",
            data.get("assessment", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        if data.get("has_klvs_variant"):
            special_label = ctk.CTkLabel(
                frame,
                text="You carry the KL-VS variant - associated with enhanced cognition and longevity!",
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color="#4ECDC4"
            )
            special_label.pack(pady=(5, 10), padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_recommendations_section(self):
        """Create personalized recommendations section"""
        data = self.results.get("overall", {})
        recommendations = data.get("recommendations", [])
        if not recommendations:
            return

        frame = self.create_section_frame("Personalized Longevity Recommendations")

        for rec in recommendations:
            rec_label = ctk.CTkLabel(
                frame,
                text=f"  {rec}",
                font=ctk.CTkFont(size=12),
                text_color="#4ECDC4"
            )
            rec_label.pack(pady=3, padx=15, anchor="w")

        # Disclaimer
        disclaimer = ctk.CTkLabel(
            frame,
            text="These recommendations are based on genetic analysis and general longevity research.",
            font=ctk.CTkFont(size=11),
            text_color="orange"
        )
        disclaimer.pack(pady=(10, 15), padx=15, anchor="w")


class LongevitySummaryCard(ctk.CTkFrame):
    """Compact summary card for longevity genetics"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results or {}
        self.build_ui()

    def build_ui(self):
        """Build the summary card UI"""
        title = ctk.CTkLabel(
            self,
            text="Longevity Genetics",
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

        # Key metrics
        overall = self.results.get("overall", {})
        if overall.get("assessment"):
            metric_label = ctk.CTkLabel(
                self,
                text=overall["assessment"],
                font=ctk.CTkFont(size=12)
            )
            metric_label.pack(pady=2, padx=15, anchor="w")

        if overall.get("percentile"):
            percentile_label = ctk.CTkLabel(
                self,
                text=f"Percentile: {overall['percentile']}th",
                font=ctk.CTkFont(size=12),
                text_color="gray"
            )
            percentile_label.pack(pady=2, padx=15, anchor="w")

        # Special variants
        if self.results.get("foxo_pathway", {}).get("has_centenarian_variant"):
            special = ctk.CTkLabel(
                self,
                text="FOXO3 Longevity Variant",
                font=ctk.CTkFont(size=11),
                text_color="#4ECDC4"
            )
            special.pack(pady=2, padx=15, anchor="w")

        if self.results.get("klotho", {}).get("has_klvs_variant"):
            special = ctk.CTkLabel(
                self,
                text="KL-VS Cognitive Variant",
                font=ctk.CTkFont(size=11),
                text_color="#4ECDC4"
            )
            special.pack(pady=2, padx=15, anchor="w")

        ctk.CTkLabel(self, text="").pack(pady=(0, 10))
