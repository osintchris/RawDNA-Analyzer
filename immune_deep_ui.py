"""
Immune System Deep Dive UI Module
CustomTkinter frames for displaying comprehensive immune genetics analysis
"""

import customtkinter as ctk
from typing import Dict, Any, Optional


class ImmuneDeepGeneticsFrame(ctk.CTkScrollableFrame):
    """Main frame for immune system deep genetics display"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results
        self.configure(fg_color="transparent")
        self.build_ui()

    def build_ui(self):
        """Build the immune deep genetics UI"""
        # Title
        title = ctk.CTkLabel(
            self,
            text="Immune System Deep Dive",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(20, 5), padx=20, anchor="w")

        subtitle = ctk.CTkLabel(
            self,
            text="Comprehensive genetic analysis of immune function, autoimmunity, and inflammatory response",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle.pack(pady=(0, 20), padx=20, anchor="w")

        if not self.results:
            no_data = ctk.CTkLabel(
                self,
                text="No DNA data loaded. Please load a DNA file to see immune genetics analysis.",
                font=ctk.CTkFont(size=14)
            )
            no_data.pack(pady=50)
            return

        # Summary section first
        self.create_summary_section()

        # Create sections for each category
        self.create_hla_section()
        self.create_cytokine_section()
        self.create_inflammatory_section()
        self.create_allergy_section()
        self.create_celiac_section()
        self.create_lupus_section()
        self.create_ms_section()
        self.create_ra_section()
        self.create_psoriasis_section()
        self.create_ibd_section()

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
            width=220,
            anchor="w"
        )
        label_widget.pack(side="left")

        value_color = color if color else self.get_color_for_value(value)
        value_widget = ctk.CTkLabel(
            row,
            text=value,
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
        if any(word in value_lower for word in ["high", "elevated", "positive", "impaired", "risk"]):
            return "#FF6B6B"
        elif any(word in value_lower for word in ["low", "normal", "negative", "protected", "reduced"]):
            return "#4ECDC4"
        elif any(word in value_lower for word in ["moderate", "possible", "likely"]):
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

    def create_findings_list(self, parent: ctk.CTkFrame, findings: list, max_items: int = 4):
        """Create a findings list"""
        if not findings:
            return

        findings_label = ctk.CTkLabel(
            parent,
            text="Key Findings:",
            font=ctk.CTkFont(size=13, weight="bold")
        )
        findings_label.pack(pady=(10, 5), padx=15, anchor="w")

        for finding in findings[:max_items]:
            finding_label = ctk.CTkLabel(
                parent,
                text=f"  • {finding}",
                font=ctk.CTkFont(size=12),
                text_color="gray",
                wraplength=600
            )
            finding_label.pack(pady=2, padx=15, anchor="w")

    def create_summary_section(self):
        """Create overall summary section"""
        summary = self.results.get("summary", {})
        if not summary:
            return

        frame = self.create_section_frame("Immune System Overview")

        self.create_result_row(
            frame, "Overall Autoimmune Risk:",
            summary.get("autoimmune_risk_level", "Unknown")
        )

        self.create_result_row(
            frame, "Inflammatory Profile:",
            summary.get("inflammatory_profile", "Unknown")
        )

        # Highest risk conditions
        high_risk = summary.get("highest_risk_conditions", [])
        if high_risk:
            risk_label = ctk.CTkLabel(
                frame,
                text="Conditions with Elevated Genetic Risk:",
                font=ctk.CTkFont(size=13, weight="bold")
            )
            risk_label.pack(pady=(10, 5), padx=15, anchor="w")

            for condition in high_risk:
                cond_label = ctk.CTkLabel(
                    frame,
                    text=f"  • {condition['condition']}: {condition['risk']}",
                    font=ctk.CTkFont(size=12),
                    text_color="#FF6B6B"
                )
                cond_label.pack(pady=2, padx=15, anchor="w")

        # Recommendations
        recommendations = summary.get("recommendations", [])
        if recommendations:
            rec_label = ctk.CTkLabel(
                frame,
                text="Recommendations:",
                font=ctk.CTkFont(size=13, weight="bold")
            )
            rec_label.pack(pady=(15, 5), padx=15, anchor="w")

            for rec in recommendations[:4]:
                rec_item = ctk.CTkLabel(
                    frame,
                    text=f"  • {rec}",
                    font=ctk.CTkFont(size=12),
                    text_color="#4ECDC4",
                    wraplength=600
                )
                rec_item.pack(pady=2, padx=15, anchor="w")

        # Spacer
        ctk.CTkLabel(frame, text="").pack(pady=5)

    def create_hla_section(self):
        """Create HLA analysis section"""
        data = self.results.get("hla_analysis", {})
        if not data:
            return

        frame = self.create_section_frame("HLA Type Analysis")

        self.create_result_row(frame, "HLA-B27 Status:", data.get("hla_b27_status", "Unknown"))
        self.create_result_row(frame, "HLA-DQ2 Status:", data.get("hla_dq2_status", "Unknown"))
        self.create_result_row(frame, "HLA-DQ8 Status:", data.get("hla_dq8_status", "Unknown"))
        self.create_result_row(frame, "Autoimmune HLA Risk:", data.get("autoimmune_hla_risk", "Unknown"))

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_cytokine_section(self):
        """Create cytokine response section"""
        data = self.results.get("cytokine_response", {})
        if not data:
            return

        frame = self.create_section_frame("Cytokine Response Genetics")

        self.create_result_row(frame, "IL-6 Production:", data.get("il6_response", "Unknown"))
        self.create_result_row(frame, "TNF-alpha Response:", data.get("tnf_response", "Unknown"))
        self.create_result_row(frame, "IL-10 Level:", data.get("il10_level", "Unknown"))
        self.create_result_row(frame, "IFN-gamma Response:", data.get("ifng_response", "Unknown"))
        self.create_result_row(
            frame, "Overall Inflammatory Tendency:",
            data.get("overall_inflammatory_tendency", "Unknown")
        )

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_inflammatory_section(self):
        """Create inflammatory markers section"""
        data = self.results.get("inflammatory_markers", {})
        if not data:
            return

        frame = self.create_section_frame("Baseline Inflammatory Markers")

        self.create_result_row(frame, "Baseline CRP Tendency:", data.get("baseline_crp", "Unknown"))
        self.create_result_row(frame, "NF-kB Activity:", data.get("nfkb_activity", "Unknown"))

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_allergy_section(self):
        """Create allergy susceptibility section"""
        data = self.results.get("allergy_susceptibility", {})
        if not data:
            return

        frame = self.create_section_frame("Allergy Susceptibility")

        self.create_result_row(
            frame, "Overall Allergy Risk:",
            data.get("overall_allergy_risk", "Unknown"),
            f"Risk score: {data.get('risk_score', 0)}"
        )
        self.create_result_row(frame, "IgE Tendency:", data.get("ige_tendency", "Unknown"))
        self.create_result_row(frame, "Skin Barrier:", data.get("skin_barrier", "Unknown"))
        self.create_result_row(frame, "Histamine Sensitivity:", data.get("histamine_sensitivity", "Unknown"))

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_celiac_section(self):
        """Create celiac disease section"""
        data = self.results.get("celiac_risk", {})
        if not data:
            return

        frame = self.create_section_frame("Celiac Disease Risk")

        self.create_result_row(frame, "Overall Celiac Risk:", data.get("overall_risk", "Unknown"))
        self.create_result_row(frame, "HLA Risk Status:", data.get("hla_risk", "Unknown"))

        can_develop = data.get("can_develop_celiac", True)
        self.create_result_row(
            frame, "Can Develop Celiac:",
            "Yes (HLA positive)" if can_develop else "Very Unlikely (HLA negative)"
        )

        if data.get("non_hla_modifiers"):
            mods = ", ".join(data["non_hla_modifiers"])
            self.create_result_row(frame, "Risk Modifier Genes:", mods)

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_lupus_section(self):
        """Create lupus risk section"""
        data = self.results.get("lupus_risk", {})
        if not data:
            return

        frame = self.create_section_frame("Lupus (SLE) Risk")

        self.create_result_row(
            frame, "SLE Risk Level:",
            data.get("risk_level", "Unknown"),
            f"Risk score: {data.get('risk_score', 0)}"
        )
        self.create_result_row(
            frame, "Risk Variants Found:",
            str(data.get("risk_variants_found", 0))
        )

        if data.get("key_genes"):
            genes = ", ".join(data["key_genes"])
            self.create_result_row(frame, "Key Risk Genes:", genes)

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_ms_section(self):
        """Create multiple sclerosis section"""
        data = self.results.get("ms_risk", {})
        if not data:
            return

        frame = self.create_section_frame("Multiple Sclerosis Risk")

        self.create_result_row(frame, "MS Risk Level:", data.get("risk_level", "Unknown"))
        self.create_result_row(frame, "HLA-DRB1*15:01:", data.get("hla_drb1_1501", "Unknown"))
        self.create_result_row(
            frame, "Risk Variants Found:",
            str(data.get("risk_variants_found", 0))
        )

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_ra_section(self):
        """Create rheumatoid arthritis section"""
        data = self.results.get("ra_risk", {})
        if not data:
            return

        frame = self.create_section_frame("Rheumatoid Arthritis Risk")

        self.create_result_row(frame, "RA Risk Level:", data.get("risk_level", "Unknown"))
        self.create_result_row(frame, "Shared Epitope:", data.get("shared_epitope", "Unknown"))
        self.create_result_row(
            frame, "Risk Variants Found:",
            str(data.get("risk_variants_found", 0))
        )

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_psoriasis_section(self):
        """Create psoriasis section"""
        data = self.results.get("psoriasis_risk", {})
        if not data:
            return

        frame = self.create_section_frame("Psoriasis Risk")

        self.create_result_row(frame, "Psoriasis Risk Level:", data.get("risk_level", "Unknown"))
        self.create_result_row(frame, "HLA-C*06:02:", data.get("hla_c0602", "Unknown"))
        self.create_result_row(frame, "Early Onset Risk:", data.get("early_onset_risk", "Unknown"))
        self.create_result_row(
            frame, "Protective Variants:",
            str(data.get("protective_variants", 0))
        )

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_ibd_section(self):
        """Create IBD/Crohn's section"""
        data = self.results.get("ibd_risk", {})
        if not data:
            return

        frame = self.create_section_frame("IBD / Crohn's Disease Risk")

        self.create_result_row(frame, "IBD Risk Level:", data.get("risk_level", "Unknown"))
        self.create_result_row(frame, "NOD2 Status:", data.get("nod2_status", "Unknown"))
        self.create_result_row(
            frame, "NOD2 Variants:",
            str(data.get("nod2_variants", 0))
        )
        self.create_result_row(frame, "Crohn's vs UC:", data.get("crohn_vs_uc", "Unknown"))

        if data.get("autophagy_genes"):
            genes = ", ".join(data["autophagy_genes"])
            self.create_result_row(frame, "Autophagy Gene Variants:", genes)

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

        # Disclaimer
        disclaimer = ctk.CTkLabel(
            frame,
            text="Note: Genetic risk is only one factor. Environmental triggers are also required for autoimmune conditions.",
            font=ctk.CTkFont(size=11),
            text_color="orange",
            wraplength=600
        )
        disclaimer.pack(pady=(10, 15), padx=15, anchor="w")


class ImmuneDeepSummaryCard(ctk.CTkFrame):
    """Compact summary card for immune deep genetics"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results or {}
        self.build_ui()

    def build_ui(self):
        """Build the summary card UI"""
        title = ctk.CTkLabel(
            self,
            text="Immune System",
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

        summary = self.results.get("summary", {})

        # Key metrics
        metrics = [
            f"Autoimmune Risk: {summary.get('autoimmune_risk_level', 'Unknown')}",
            f"Inflammatory: {summary.get('inflammatory_profile', 'Unknown')}"
        ]

        # Add highest risk condition
        high_risk = summary.get("highest_risk_conditions", [])
        if high_risk:
            metrics.append(f"Highest Risk: {high_risk[0]['condition']}")

        for metric in metrics:
            metric_label = ctk.CTkLabel(
                self,
                text=metric,
                font=ctk.CTkFont(size=12)
            )
            metric_label.pack(pady=2, padx=15, anchor="w")

        ctk.CTkLabel(self, text="").pack(pady=(0, 10))
