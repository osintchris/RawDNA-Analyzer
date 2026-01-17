"""
Reproduction & Fertility Genetics UI Module
CustomTkinter frames for displaying reproduction-related genetic analysis
"""

import customtkinter as ctk
from typing import Dict, Any, Optional


class ReproductionGeneticsFrame(ctk.CTkScrollableFrame):
    """Main frame for reproduction and fertility genetics display"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results
        self.configure(fg_color="transparent")
        self.build_ui()

    def build_ui(self):
        """Build the reproduction genetics UI"""
        # Title
        title = ctk.CTkLabel(
            self,
            text="Reproduction & Fertility Genetics",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(20, 5), padx=20, anchor="w")

        subtitle = ctk.CTkLabel(
            self,
            text="Genetic factors influencing fertility, hormones, and reproductive health",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle.pack(pady=(0, 10), padx=20, anchor="w")

        # Info note about Unknown values
        info_frame = ctk.CTkFrame(self, fg_color="#1e3a5f", corner_radius=8)
        info_frame.pack(fill="x", padx=20, pady=(0, 15))
        ctk.CTkLabel(
            info_frame,
            text="Note: 'Unknown' means your DNA test file doesn't include that specific marker. Consumer tests (23andMe, AncestryDNA) only cover ~600,000 of the ~3 billion base pairs in your genome. Many reproductive health markers may not be included.",
            font=ctk.CTkFont(size=11), text_color="#93c5fd",
            wraplength=700, justify="left"
        ).pack(padx=15, pady=8)

        if not self.results:
            no_data = ctk.CTkLabel(
                self,
                text="No DNA data loaded. Please load a DNA file to see reproduction genetics analysis.",
                font=ctk.CTkFont(size=14)
            )
            no_data.pack(pady=50)
            return

        # Create sections for each category
        self.create_male_fertility_section()
        self.create_female_fertility_section()
        self.create_menopause_section()
        self.create_twin_section()
        self.create_endometriosis_section()
        self.create_pcos_section()
        self.create_testosterone_section()
        self.create_estrogen_section()
        self.create_pregnancy_section()

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
        if any(word in value_lower for word in ["high", "increased", "elevated", "risk", "reduced"]):
            return "#FF6B6B"
        elif any(word in value_lower for word in ["low", "decreased", "protected", "normal"]):
            return "#4ECDC4"
        elif any(word in value_lower for word in ["moderate", "average", "typical"]):
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

        for snp in snps[:5]:  # Limit display
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

    def create_male_fertility_section(self):
        """Create male fertility section"""
        data = self.results.get("male_fertility", {})
        if not data:
            return

        frame = self.create_section_frame("Male Fertility Factors")

        self.create_result_row(
            frame, "Sperm Quality Score:",
            data.get("sperm_quality_score", "Unknown"),
            f"{data.get('risk_factors_found', 0)} genetic factors analyzed"
        )

        self.create_result_row(
            frame, "Overall Assessment:",
            data.get("overall_assessment", "Unknown")
        )

        # Show specific findings
        if data.get("specific_findings"):
            findings_label = ctk.CTkLabel(
                frame,
                text="Key Findings:",
                font=ctk.CTkFont(size=13, weight="bold")
            )
            findings_label.pack(pady=(10, 5), padx=15, anchor="w")

            for finding in data.get("specific_findings", [])[:3]:
                finding_label = ctk.CTkLabel(
                    frame,
                    text=f"  • {finding}",
                    font=ctk.CTkFont(size=12),
                    text_color="gray"
                )
                finding_label.pack(pady=2, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_female_fertility_section(self):
        """Create female fertility section"""
        data = self.results.get("female_fertility", {})
        if not data:
            return

        frame = self.create_section_frame("Female Fertility Factors")

        self.create_result_row(
            frame, "Ovarian Reserve Score:",
            data.get("ovarian_reserve_score", "Unknown"),
            f"{data.get('risk_factors_found', 0)} genetic factors analyzed"
        )

        self.create_result_row(
            frame, "Overall Assessment:",
            data.get("overall_assessment", "Unknown")
        )

        if data.get("specific_findings"):
            findings_label = ctk.CTkLabel(
                frame,
                text="Key Findings:",
                font=ctk.CTkFont(size=13, weight="bold")
            )
            findings_label.pack(pady=(10, 5), padx=15, anchor="w")

            for finding in data.get("specific_findings", [])[:3]:
                finding_label = ctk.CTkLabel(
                    frame,
                    text=f"  • {finding}",
                    font=ctk.CTkFont(size=12),
                    text_color="gray"
                )
                finding_label.pack(pady=2, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_menopause_section(self):
        """Create menopause timing section"""
        data = self.results.get("menopause_timing", {})
        if not data:
            return

        frame = self.create_section_frame("Menopause Timing")

        self.create_result_row(
            frame, "Predicted Timing:",
            data.get("predicted_timing", "Unknown")
        )

        self.create_result_row(
            frame, "Early Menopause Risk:",
            data.get("early_menopause_risk", "Unknown")
        )

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_twin_section(self):
        """Create twin probability section"""
        data = self.results.get("twin_probability", {})
        if not data:
            return

        frame = self.create_section_frame("Twin Probability")

        self.create_result_row(
            frame, "Fraternal Twin Probability:",
            data.get("fraternal_twin_probability", "Unknown")
        )

        self.create_result_row(
            frame, "FSH Level Tendency:",
            data.get("fsh_level_tendency", "Unknown")
        )

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_endometriosis_section(self):
        """Create endometriosis risk section"""
        data = self.results.get("endometriosis_risk", {})
        if not data:
            return

        frame = self.create_section_frame("Endometriosis Risk")

        self.create_result_row(
            frame, "Genetic Risk Level:",
            data.get("risk_level", "Unknown"),
            f"{data.get('risk_variants_found', 0)} risk variants found"
        )

        self.create_result_row(
            frame, "Risk Score:",
            data.get("risk_score", "Unknown")
        )

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_pcos_section(self):
        """Create PCOS risk section"""
        data = self.results.get("pcos_risk", {})
        if not data:
            return

        frame = self.create_section_frame("PCOS Risk")

        self.create_result_row(
            frame, "Genetic Risk Level:",
            data.get("risk_level", "Unknown"),
            f"{data.get('risk_variants_found', 0)} risk variants found"
        )

        self.create_result_row(
            frame, "Risk Score:",
            data.get("risk_score", "Unknown")
        )

        if data.get("risk_factors"):
            factors_label = ctk.CTkLabel(
                frame,
                text="Contributing Factors:",
                font=ctk.CTkFont(size=13, weight="bold")
            )
            factors_label.pack(pady=(10, 5), padx=15, anchor="w")

            for factor in data.get("risk_factors", [])[:3]:
                factor_label = ctk.CTkLabel(
                    frame,
                    text=f"  • {factor}",
                    font=ctk.CTkFont(size=12),
                    text_color="gray"
                )
                factor_label.pack(pady=2, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_testosterone_section(self):
        """Create testosterone levels section"""
        data = self.results.get("testosterone_levels", {})
        if not data:
            return

        frame = self.create_section_frame("Testosterone Genetics")

        self.create_result_row(
            frame, "Predicted Level Tendency:",
            data.get("level_tendency", "Unknown")
        )

        self.create_result_row(
            frame, "SHBG Level:",
            data.get("shbg_level", "Unknown")
        )

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_estrogen_section(self):
        """Create estrogen metabolism section"""
        data = self.results.get("estrogen_metabolism", {})
        if not data:
            return

        frame = self.create_section_frame("Estrogen Metabolism")

        self.create_result_row(
            frame, "Metabolism Rate:",
            data.get("metabolism_rate", "Unknown")
        )

        self.create_result_row(
            frame, "Estrogen Clearance:",
            data.get("estrogen_clearance", "Unknown")
        )

        if data.get("implications"):
            impl_label = ctk.CTkLabel(
                frame,
                text="Health Implications:",
                font=ctk.CTkFont(size=13, weight="bold")
            )
            impl_label.pack(pady=(10, 5), padx=15, anchor="w")

            for impl in data.get("implications", [])[:3]:
                impl_item = ctk.CTkLabel(
                    frame,
                    text=f"  • {impl}",
                    font=ctk.CTkFont(size=12),
                    text_color="gray"
                )
                impl_item.pack(pady=2, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_pregnancy_section(self):
        """Create pregnancy complications section"""
        data = self.results.get("pregnancy_complications", {})
        if not data:
            return

        frame = self.create_section_frame("Pregnancy Risk Factors")

        self.create_result_row(
            frame, "Thrombosis Risk:",
            data.get("thrombosis_risk", "Unknown")
        )

        self.create_result_row(
            frame, "Factor V Leiden:",
            data.get("factor_v_leiden_status", "Unknown")
        )

        self.create_result_row(
            frame, "Prothrombin Mutation:",
            data.get("prothrombin_status", "Unknown")
        )

        self.create_result_row(
            frame, "Folate Metabolism:",
            data.get("folate_metabolism", "Unknown")
        )

        # Risk recommendations
        if data.get("recommendations"):
            rec_label = ctk.CTkLabel(
                frame,
                text="Recommendations:",
                font=ctk.CTkFont(size=13, weight="bold")
            )
            rec_label.pack(pady=(10, 5), padx=15, anchor="w")

            for rec in data.get("recommendations", [])[:4]:
                rec_item = ctk.CTkLabel(
                    frame,
                    text=f"  • {rec}",
                    font=ctk.CTkFont(size=12),
                    text_color="gray"
                )
                rec_item.pack(pady=2, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

        # Add disclaimer
        disclaimer = ctk.CTkLabel(
            frame,
            text="Note: These are genetic risk factors only. Consult healthcare providers for medical advice.",
            font=ctk.CTkFont(size=11),
            text_color="orange"
        )
        disclaimer.pack(pady=(10, 15), padx=15, anchor="w")


class ReproductionSummaryCard(ctk.CTkFrame):
    """Compact summary card for reproduction genetics"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results or {}
        self.build_ui()

    def build_ui(self):
        """Build the summary card UI"""
        title = ctk.CTkLabel(
            self,
            text="Reproduction & Fertility",
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
        metrics = []

        if self.results.get("pcos_risk", {}).get("risk_level"):
            metrics.append(f"PCOS Risk: {self.results['pcos_risk']['risk_level']}")

        if self.results.get("endometriosis_risk", {}).get("risk_level"):
            metrics.append(f"Endometriosis Risk: {self.results['endometriosis_risk']['risk_level']}")

        if self.results.get("pregnancy_complications", {}).get("thrombosis_risk"):
            metrics.append(f"Pregnancy Thrombosis: {self.results['pregnancy_complications']['thrombosis_risk']}")

        if self.results.get("twin_probability", {}).get("fraternal_twin_probability"):
            metrics.append(f"Twin Probability: {self.results['twin_probability']['fraternal_twin_probability']}")

        for metric in metrics[:4]:
            metric_label = ctk.CTkLabel(
                self,
                text=metric,
                font=ctk.CTkFont(size=12)
            )
            metric_label.pack(pady=2, padx=15, anchor="w")

        # Spacer
        ctk.CTkLabel(self, text="").pack(pady=(0, 10))
