"""
Pharmacogenomics UI Module
CustomTkinter frames for displaying drug metabolism genetics analysis
"""

import customtkinter as ctk
from typing import Dict, Any, Optional


class PharmacogenomicsFrame(ctk.CTkScrollableFrame):
    """Main frame for pharmacogenomics display"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results
        self.configure(fg_color="transparent")
        self.build_ui()

    def build_ui(self):
        """Build the pharmacogenomics UI"""
        # Title
        title = ctk.CTkLabel(
            self,
            text="Pharmacogenomics - Drug Response Genetics",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(20, 5), padx=20, anchor="w")

        subtitle = ctk.CTkLabel(
            self,
            text="How your genes affect drug metabolism and response",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle.pack(pady=(0, 20), padx=20, anchor="w")

        if not self.results:
            no_data = ctk.CTkLabel(
                self,
                text="No DNA data loaded. Please load a DNA file to see pharmacogenomics analysis.",
                font=ctk.CTkFont(size=14)
            )
            no_data.pack(pady=50)
            return

        # Create sections
        self.create_summary_section()
        self.create_cyp2d6_section()
        self.create_cyp2c19_section()
        self.create_cyp2c9_section()
        self.create_warfarin_section()
        self.create_statin_section()
        self.create_tpmt_section()
        self.create_dpyd_section()
        self.create_opioid_section()
        self.create_caffeine_section()
        self.create_mthfr_section()
        self.create_drug_guidance_section()

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
        if any(word in value_lower for word in ["normal", "standard", "good"]):
            return "#4ECDC4"
        elif any(word in value_lower for word in ["poor", "deficient", "avoid", "high", "contraindicated"]):
            return "#FF6B6B"
        elif any(word in value_lower for word in ["intermediate", "reduced", "moderate"]):
            return "#FFE66D"
        elif any(word in value_lower for word in ["rapid", "ultrarapid", "fast"]):
            return "#9B59B6"
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
                snp_text += f" ({snp.get('gene')}"
                if snp.get('variant'):
                    snp_text += f" {snp.get('variant')}"
                snp_text += ")"

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
        data = self.results.get("summary", {})
        if not data:
            return

        frame = self.create_section_frame("Pharmacogenomics Summary")

        self.create_result_row(
            frame, "Genes Analyzed:",
            str(data.get("total_genes_analyzed", 0))
        )

        actionable = data.get("actionable_findings", 0)
        self.create_result_row(
            frame, "Actionable Findings:",
            str(actionable),
            "variants affecting drug dosing" if actionable > 0 else ""
        )

        if actionable > 0:
            warning = ctk.CTkLabel(
                frame,
                text="Share these results with your healthcare provider before starting new medications",
                font=ctk.CTkFont(size=12),
                text_color="orange"
            )
            warning.pack(pady=(5, 15), padx=15, anchor="w")

    def create_cyp2d6_section(self):
        """Create CYP2D6 section"""
        data = self.results.get("cyp2d6", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("CYP2D6 - Opioids, SSRIs, Beta-blockers")

        self.create_result_row(
            frame, "Metabolizer Status:",
            data.get("phenotype", "Unknown")
        )

        rec = data.get("recommendation", "")
        if rec:
            rec_label = ctk.CTkLabel(
                frame,
                text=f"Recommendation: {rec}",
                font=ctk.CTkFont(size=12),
                text_color="#4ECDC4",
                wraplength=600
            )
            rec_label.pack(pady=5, padx=15, anchor="w")

        drugs = data.get("affected_drugs", [])
        if drugs:
            drugs_label = ctk.CTkLabel(
                frame,
                text=f"Affected drugs: {', '.join(drugs[:6])}",
                font=ctk.CTkFont(size=11),
                text_color="gray"
            )
            drugs_label.pack(pady=2, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_cyp2c19_section(self):
        """Create CYP2C19 section"""
        data = self.results.get("cyp2c19", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("CYP2C19 - Clopidogrel, PPIs, SSRIs")

        self.create_result_row(
            frame, "Metabolizer Status:",
            data.get("phenotype", "Unknown")
        )

        rec = data.get("recommendation", "")
        if rec:
            rec_label = ctk.CTkLabel(
                frame,
                text=f"Recommendation: {rec}",
                font=ctk.CTkFont(size=12),
                text_color="#4ECDC4",
                wraplength=600
            )
            rec_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_cyp2c9_section(self):
        """Create CYP2C9 section"""
        data = self.results.get("cyp2c9", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("CYP2C9 - Warfarin, NSAIDs, Sulfonylureas")

        self.create_result_row(
            frame, "Metabolizer Status:",
            data.get("phenotype", "Unknown")
        )

        rec = data.get("recommendation", "")
        if rec:
            rec_label = ctk.CTkLabel(
                frame,
                text=f"Recommendation: {rec}",
                font=ctk.CTkFont(size=12),
                text_color="#4ECDC4",
                wraplength=600
            )
            rec_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_warfarin_section(self):
        """Create warfarin sensitivity section"""
        data = self.results.get("vkorc1_warfarin", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("VKORC1 - Warfarin Sensitivity")

        self.create_result_row(
            frame, "Warfarin Sensitivity:",
            data.get("sensitivity", "Unknown").title()
        )

        dose = data.get("dose_adjustment", "")
        if dose:
            dose_label = ctk.CTkLabel(
                frame,
                text=f"Dose adjustment: {dose}",
                font=ctk.CTkFont(size=12),
                text_color="#FFE66D"
            )
            dose_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_statin_section(self):
        """Create statin myopathy section"""
        data = self.results.get("slco1b1_statins", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("SLCO1B1 - Statin Myopathy Risk")

        self.create_result_row(
            frame, "Myopathy Risk:",
            data.get("myopathy_risk", "Unknown")
        )

        rec = data.get("recommendation", "")
        if rec:
            rec_label = ctk.CTkLabel(
                frame,
                text=f"Recommendation: {rec}",
                font=ctk.CTkFont(size=12),
                text_color="#4ECDC4",
                wraplength=600
            )
            rec_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_tpmt_section(self):
        """Create TPMT section"""
        data = self.results.get("tpmt_thiopurines", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("TPMT - Thiopurine Toxicity Risk")

        self.create_result_row(
            frame, "TPMT Status:",
            data.get("status", "Unknown")
        )

        rec = data.get("recommendation", "")
        if rec:
            rec_label = ctk.CTkLabel(
                frame,
                text=f"Recommendation: {rec}",
                font=ctk.CTkFont(size=12),
                text_color="#4ECDC4" if "Standard" in rec else "#FF6B6B",
                wraplength=600
            )
            rec_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_dpyd_section(self):
        """Create DPYD section"""
        data = self.results.get("dpyd_fluoropyrimidines", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("DPYD - Fluoropyrimidine Toxicity Risk")

        self.create_result_row(
            frame, "DPYD Status:",
            data.get("status", "Unknown")
        )

        rec = data.get("recommendation", "")
        if rec:
            color = "#FF6B6B" if "CONTRAINDICATED" in rec else "#4ECDC4"
            rec_label = ctk.CTkLabel(
                frame,
                text=f"Recommendation: {rec}",
                font=ctk.CTkFont(size=12),
                text_color=color,
                wraplength=600
            )
            rec_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_opioid_section(self):
        """Create opioid response section"""
        data = self.results.get("oprm1_opioids", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("OPRM1 - Opioid Response")

        self.create_result_row(
            frame, "Opioid Response:",
            data.get("response", "Unknown")
        )

        rec = data.get("recommendation", "")
        if rec:
            rec_label = ctk.CTkLabel(
                frame,
                text=f"Recommendation: {rec}",
                font=ctk.CTkFont(size=12),
                text_color="gray"
            )
            rec_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_caffeine_section(self):
        """Create caffeine metabolism section"""
        data = self.results.get("cyp1a2_caffeine", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("CYP1A2 - Caffeine Metabolism")

        self.create_result_row(
            frame, "Caffeine Metabolism:",
            data.get("metabolism", "Unknown")
        )

        rec = data.get("recommendation", "")
        if rec:
            rec_label = ctk.CTkLabel(
                frame,
                text=f"Recommendation: {rec}",
                font=ctk.CTkFont(size=12),
                text_color="gray",
                wraplength=600
            )
            rec_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_mthfr_section(self):
        """Create MTHFR section"""
        data = self.results.get("mthfr_folate", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("MTHFR - Folate Metabolism")

        self.create_result_row(
            frame, "MTHFR Status:",
            data.get("status", "Unknown")
        )

        rec = data.get("recommendation", "")
        if rec:
            rec_label = ctk.CTkLabel(
                frame,
                text=f"Recommendation: {rec}",
                font=ctk.CTkFont(size=12),
                text_color="gray"
            )
            rec_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_drug_guidance_section(self):
        """Create actionable drug guidance section"""
        data = self.results.get("summary", {})
        guidance = data.get("drugs_with_guidance", [])
        if not guidance:
            return

        frame = self.create_section_frame("Actionable Drug Guidance")

        for item in guidance:
            drug_class = item.get("drug_class", "Unknown")
            rec = item.get("guidance", "")

            drug_label = ctk.CTkLabel(
                frame,
                text=f"{drug_class}:",
                font=ctk.CTkFont(size=13, weight="bold"),
                text_color="#FF6B6B"
            )
            drug_label.pack(pady=(10, 2), padx=15, anchor="w")

            guidance_label = ctk.CTkLabel(
                frame,
                text=f"  {rec}",
                font=ctk.CTkFont(size=12),
                text_color="white",
                wraplength=600
            )
            guidance_label.pack(pady=2, padx=15, anchor="w")

        # Disclaimer
        disclaimer = ctk.CTkLabel(
            frame,
            text="Always consult your healthcare provider before making medication changes.",
            font=ctk.CTkFont(size=11),
            text_color="orange"
        )
        disclaimer.pack(pady=(15, 15), padx=15, anchor="w")


class PharmacogenomicsSummaryCard(ctk.CTkFrame):
    """Compact summary card for pharmacogenomics"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results or {}
        self.build_ui()

    def build_ui(self):
        """Build the summary card UI"""
        title = ctk.CTkLabel(
            self,
            text="Drug Response Genetics",
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
        summary = self.results.get("summary", {})
        actionable = summary.get("actionable_findings", 0)

        if actionable > 0:
            alert = ctk.CTkLabel(
                self,
                text=f"{actionable} Actionable Finding(s)",
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color="#FF6B6B"
            )
            alert.pack(pady=2, padx=15, anchor="w")

        # Show key metabolizer statuses
        if self.results.get("cyp2d6", {}).get("phenotype"):
            status = ctk.CTkLabel(
                self,
                text=f"CYP2D6: {self.results['cyp2d6']['phenotype']}",
                font=ctk.CTkFont(size=11),
                text_color="gray"
            )
            status.pack(pady=2, padx=15, anchor="w")

        if self.results.get("cyp2c19", {}).get("phenotype"):
            status = ctk.CTkLabel(
                self,
                text=f"CYP2C19: {self.results['cyp2c19']['phenotype']}",
                font=ctk.CTkFont(size=11),
                text_color="gray"
            )
            status.pack(pady=2, padx=15, anchor="w")

        ctk.CTkLabel(self, text="").pack(pady=(0, 10))
