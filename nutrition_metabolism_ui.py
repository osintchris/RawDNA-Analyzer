"""
Nutrition & Metabolism UI Module
CustomTkinter frames for displaying personalized nutrition genetics analysis
"""

import customtkinter as ctk
from typing import Dict, Any, Optional


class NutritionMetabolismFrame(ctk.CTkScrollableFrame):
    """Main frame for nutrition and metabolism genetics display"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results
        self.configure(fg_color="transparent")
        self.build_ui()

    def build_ui(self):
        """Build the nutrition metabolism UI"""
        # Title
        title = ctk.CTkLabel(
            self,
            text="Personalized Nutrition Genetics",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(20, 5), padx=20, anchor="w")

        subtitle = ctk.CTkLabel(
            self,
            text="Genetic insights for personalized diet and nutrient optimization",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle.pack(pady=(0, 10), padx=20, anchor="w")

        # Info note about Unknown values
        info_frame = ctk.CTkFrame(self, fg_color="#1e3a5f", corner_radius=8)
        info_frame.pack(fill="x", padx=20, pady=(0, 15))
        ctk.CTkLabel(
            info_frame,
            text="Note: 'Unknown' means your DNA test file doesn't include that specific marker. Consumer tests (23andMe, AncestryDNA) only cover a subset of all genetic markers.",
            font=ctk.CTkFont(size=11), text_color="#93c5fd",
            wraplength=700, justify="left"
        ).pack(padx=15, pady=8)

        if not self.results:
            no_data = ctk.CTkLabel(
                self,
                text="No DNA data loaded. Please load a DNA file to see nutrition genetics analysis.",
                font=ctk.CTkFont(size=14)
            )
            no_data.pack(pady=50)
            return

        # Summary section first
        self.create_summary_section()

        # Create sections for each category
        self.create_vitamin_a_section()
        self.create_vitamin_b12_section()
        self.create_vitamin_c_section()
        self.create_vitamin_e_section()
        self.create_omega3_section()
        self.create_saturated_fat_section()
        self.create_carbohydrate_section()
        self.create_protein_section()
        self.create_sodium_section()
        self.create_alcohol_section()

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
        if any(word in value_lower for word in ["poor", "low", "reduced", "high risk", "sensitive", "deficiency"]):
            return "#FF6B6B"
        elif any(word in value_lower for word in ["good", "normal", "efficient", "standard"]):
            return "#4ECDC4"
        elif any(word in value_lower for word in ["moderate", "slightly"]):
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
            if snp.get('common_name'):
                snp_text += f" - {snp.get('common_name')}"

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

    def create_findings_list(self, parent: ctk.CTkFrame, findings: list, max_items: int = 3):
        """Create a findings list"""
        if not findings:
            return

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

        frame = self.create_section_frame("Your Personalized Nutrition Profile")

        # Metabolism profile
        self.create_result_row(
            frame, "Metabolism Profile:",
            summary.get("metabolism_profile", "Unknown")
        )

        # Key nutrient needs
        nutrients = summary.get("key_nutrient_needs", [])
        if nutrients:
            nutrients_label = ctk.CTkLabel(
                frame,
                text="Key Nutrient Needs:",
                font=ctk.CTkFont(size=14, weight="bold")
            )
            nutrients_label.pack(pady=(10, 5), padx=15, anchor="w")

            for nutrient in nutrients:
                nut_label = ctk.CTkLabel(
                    frame,
                    text=f"  • {nutrient}",
                    font=ctk.CTkFont(size=12),
                    text_color="#FF6B6B"
                )
                nut_label.pack(pady=2, padx=15, anchor="w")

        # Dietary sensitivities
        sensitivities = summary.get("dietary_sensitivities", [])
        if sensitivities:
            sens_label = ctk.CTkLabel(
                frame,
                text="Dietary Sensitivities:",
                font=ctk.CTkFont(size=14, weight="bold")
            )
            sens_label.pack(pady=(10, 5), padx=15, anchor="w")

            for sens in sensitivities:
                s_label = ctk.CTkLabel(
                    frame,
                    text=f"  • {sens}",
                    font=ctk.CTkFont(size=12),
                    text_color="#FFE66D"
                )
                s_label.pack(pady=2, padx=15, anchor="w")

        # Personalized recommendations
        recommendations = summary.get("personalized_recommendations", [])
        if recommendations:
            rec_label = ctk.CTkLabel(
                frame,
                text="Personalized Recommendations:",
                font=ctk.CTkFont(size=14, weight="bold")
            )
            rec_label.pack(pady=(15, 5), padx=15, anchor="w")

            for rec in recommendations[:6]:
                rec_item = ctk.CTkLabel(
                    frame,
                    text=f"  • {rec}",
                    font=ctk.CTkFont(size=12),
                    text_color="#4ECDC4",
                    wraplength=600
                )
                rec_item.pack(pady=2, padx=15, anchor="w")

        ctk.CTkLabel(frame, text="").pack(pady=5)

    def create_vitamin_a_section(self):
        """Create vitamin A section"""
        data = self.results.get("vitamin_a_metabolism", {})
        if not data:
            return

        frame = self.create_section_frame("Vitamin A / Beta-Carotene")

        self.create_result_row(
            frame, "Beta-Carotene Converter:",
            data.get("beta_carotene_converter", "Unknown")
        )
        self.create_result_row(
            frame, "Conversion Efficiency:",
            data.get("conversion_efficiency", "Unknown")
        )

        if data.get("recommendation"):
            rec = ctk.CTkLabel(
                frame,
                text=f"Recommendation: {data['recommendation']}",
                font=ctk.CTkFont(size=12),
                text_color="#4ECDC4",
                wraplength=600
            )
            rec.pack(pady=(10, 5), padx=15, anchor="w")

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_vitamin_b12_section(self):
        """Create vitamin B12 section"""
        data = self.results.get("vitamin_b12_metabolism", {})
        if not data:
            return

        frame = self.create_section_frame("Vitamin B12 & Folate Metabolism")

        self.create_result_row(frame, "B12 Need:", data.get("overall_b12_need", "Unknown"))
        self.create_result_row(frame, "Secretor Status:", data.get("secretor_status", "Unknown"))
        self.create_result_row(frame, "B12 Transport:", data.get("b12_transport", "Unknown"))
        self.create_result_row(frame, "MTHFR Status:", data.get("mthfr_status", "Unknown"))

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_vitamin_c_section(self):
        """Create vitamin C section"""
        data = self.results.get("vitamin_c_metabolism", {})
        if not data:
            return

        frame = self.create_section_frame("Vitamin C & Antioxidants")

        self.create_result_row(frame, "Vitamin C Transport:", data.get("vitamin_c_transport", "Unknown"))
        self.create_result_row(frame, "Antioxidant Capacity:", data.get("antioxidant_capacity", "Unknown"))

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_vitamin_e_section(self):
        """Create vitamin E section"""
        data = self.results.get("vitamin_e_metabolism", {})
        if not data:
            return

        frame = self.create_section_frame("Vitamin E Metabolism")

        self.create_result_row(frame, "Vitamin E Retention:", data.get("vitamin_e_retention", "Unknown"))
        self.create_result_row(frame, "Metabolism Rate:", data.get("metabolism_rate", "Unknown"))

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_omega3_section(self):
        """Create omega-3 section"""
        data = self.results.get("omega3_metabolism", {})
        if not data:
            return

        frame = self.create_section_frame("Omega-3 Fatty Acid Metabolism")

        self.create_result_row(
            frame, "Overall Conversion:",
            data.get("overall_conversion_ability", "Unknown")
        )
        self.create_result_row(
            frame, "ALA to EPA:",
            data.get("ala_to_epa_conversion", "Unknown")
        )
        self.create_result_row(
            frame, "EPA to DHA:",
            data.get("epa_to_dha_conversion", "Unknown")
        )

        if data.get("recommendation"):
            rec = ctk.CTkLabel(
                frame,
                text=f"Recommendation: {data['recommendation']}",
                font=ctk.CTkFont(size=12),
                text_color="#4ECDC4",
                wraplength=600
            )
            rec.pack(pady=(10, 5), padx=15, anchor="w")

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_saturated_fat_section(self):
        """Create saturated fat section"""
        data = self.results.get("saturated_fat_response", {})
        if not data:
            return

        frame = self.create_section_frame("Saturated Fat Response")

        self.create_result_row(
            frame, "Sat Fat Sensitivity:",
            data.get("sat_fat_sensitivity", "Unknown")
        )
        self.create_result_row(
            frame, "APOE Status:",
            data.get("apoe_status", "Unknown")
        )
        self.create_result_row(
            frame, "Weight Risk with Sat Fat:",
            data.get("weight_risk_with_sat_fat", "Unknown")
        )

        if data.get("recommendation"):
            rec = ctk.CTkLabel(
                frame,
                text=f"Recommendation: {data['recommendation']}",
                font=ctk.CTkFont(size=12),
                text_color="#4ECDC4",
                wraplength=600
            )
            rec.pack(pady=(10, 5), padx=15, anchor="w")

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_carbohydrate_section(self):
        """Create carbohydrate section"""
        data = self.results.get("carbohydrate_metabolism", {})
        if not data:
            return

        frame = self.create_section_frame("Carbohydrate Metabolism")

        self.create_result_row(frame, "Starch Digestion:", data.get("starch_digestion", "Unknown"))
        self.create_result_row(frame, "Insulin Response:", data.get("insulin_response", "Unknown"))
        self.create_result_row(frame, "T2D Genetic Risk:", data.get("t2d_genetic_risk", "Unknown"))
        self.create_result_row(frame, "Sugar Preference:", data.get("sugar_preference", "Unknown"))

        if data.get("recommendation"):
            rec = ctk.CTkLabel(
                frame,
                text=f"Recommendation: {data['recommendation']}",
                font=ctk.CTkFont(size=12),
                text_color="#4ECDC4",
                wraplength=600
            )
            rec.pack(pady=(10, 5), padx=15, anchor="w")

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_protein_section(self):
        """Create protein section"""
        data = self.results.get("protein_metabolism", {})
        if not data:
            return

        frame = self.create_section_frame("Protein & Satiety")

        self.create_result_row(frame, "Satiety Response:", data.get("satiety_response", "Unknown"))
        self.create_result_row(frame, "Protein Benefit:", data.get("protein_benefit", "Unknown"))
        self.create_result_row(frame, "Metabolic Efficiency:", data.get("metabolic_efficiency", "Unknown"))

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_sodium_section(self):
        """Create sodium section"""
        data = self.results.get("sodium_sensitivity", {})
        if not data:
            return

        frame = self.create_section_frame("Sodium Sensitivity")

        self.create_result_row(frame, "Salt Sensitivity:", data.get("salt_sensitivity", "Unknown"))
        self.create_result_row(frame, "BP Response to Salt:", data.get("blood_pressure_response", "Unknown"))

        if data.get("recommendation"):
            rec = ctk.CTkLabel(
                frame,
                text=f"Recommendation: {data['recommendation']}",
                font=ctk.CTkFont(size=12),
                text_color="#4ECDC4",
                wraplength=600
            )
            rec.pack(pady=(10, 5), padx=15, anchor="w")

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_alcohol_section(self):
        """Create alcohol section"""
        data = self.results.get("alcohol_metabolism", {})
        if not data:
            return

        frame = self.create_section_frame("Alcohol Metabolism")

        self.create_result_row(frame, "ADH Activity:", data.get("adh_activity", "Unknown"))
        self.create_result_row(frame, "ALDH Activity:", data.get("aldh_activity", "Unknown"))
        self.create_result_row(frame, "Alcohol Tolerance:", data.get("alcohol_tolerance", "Unknown"))
        self.create_result_row(frame, "Flushing Risk:", data.get("flushing_risk", "Unknown"))

        self.create_findings_list(frame, data.get("findings", []))

        # Health implications
        implications = data.get("health_implications", [])
        if implications:
            impl_label = ctk.CTkLabel(
                frame,
                text="Health Implications:",
                font=ctk.CTkFont(size=13, weight="bold")
            )
            impl_label.pack(pady=(10, 5), padx=15, anchor="w")

            for impl in implications:
                impl_item = ctk.CTkLabel(
                    frame,
                    text=f"  • {impl}",
                    font=ctk.CTkFont(size=12),
                    text_color="orange",
                    wraplength=600
                )
                impl_item.pack(pady=2, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))


class NutritionSummaryCard(ctk.CTkFrame):
    """Compact summary card for nutrition genetics"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results or {}
        self.build_ui()

    def build_ui(self):
        """Build the summary card UI"""
        title = ctk.CTkLabel(
            self,
            text="Nutrition Genetics",
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
        profile = summary.get("metabolism_profile", "Unknown")
        metric_label = ctk.CTkLabel(
            self,
            text=f"Profile: {profile}",
            font=ctk.CTkFont(size=12)
        )
        metric_label.pack(pady=2, padx=15, anchor="w")

        # Key sensitivities
        sensitivities = summary.get("dietary_sensitivities", [])
        if sensitivities:
            sens_text = f"Sensitive: {', '.join(sensitivities[:2])}"
            sens_label = ctk.CTkLabel(
                self,
                text=sens_text,
                font=ctk.CTkFont(size=12),
                text_color="#FFE66D"
            )
            sens_label.pack(pady=2, padx=15, anchor="w")

        ctk.CTkLabel(self, text="").pack(pady=(0, 10))
