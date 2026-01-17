"""
Mental Health Genetics UI Module
CustomTkinter frames for displaying mental health genetics analysis
"""

import customtkinter as ctk
from typing import Dict, Any, Optional


class MentalHealthGeneticsFrame(ctk.CTkScrollableFrame):
    """Main frame for mental health genetics display"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results
        self.configure(fg_color="transparent")
        self.build_ui()

    def build_ui(self):
        """Build the mental health genetics UI"""
        # Title
        title = ctk.CTkLabel(
            self,
            text="Mental Health Genetics",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(20, 5), padx=20, anchor="w")

        subtitle = ctk.CTkLabel(
            self,
            text="Genetic factors influencing mental health and cognitive function",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle.pack(pady=(0, 10), padx=20, anchor="w")

        # Important disclaimer
        disclaimer = ctk.CTkLabel(
            self,
            text="Note: Mental health is influenced by many factors. Genetics is only one piece. These results do not diagnose conditions.",
            font=ctk.CTkFont(size=11),
            text_color="orange",
            wraplength=700
        )
        disclaimer.pack(pady=(0, 20), padx=20, anchor="w")

        if not self.results:
            no_data = ctk.CTkLabel(
                self,
                text="No DNA data loaded. Please load a DNA file to see mental health genetics analysis.",
                font=ctk.CTkFont(size=14)
            )
            no_data.pack(pady=50)
            return

        # Create sections
        self.create_overall_section()
        self.create_cognitive_section()
        self.create_depression_section()
        self.create_anxiety_section()
        self.create_adhd_section()
        self.create_ptsd_section()
        self.create_addiction_section()
        self.create_bipolar_section()
        self.create_schizophrenia_section()
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
        if any(word in value_lower for word in ["below average", "low", "resilience", "protective", "optimal", "enhanced"]):
            return "#4ECDC4"
        elif any(word in value_lower for word in ["elevated", "high", "vulnerability", "multiple"]):
            return "#FF6B6B"
        elif any(word in value_lower for word in ["average", "typical", "moderate", "slight"]):
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
        """Create overall mental health section"""
        data = self.results.get("overall", {})
        if not data:
            return

        frame = self.create_section_frame("Overall Mental Health Profile")

        self.create_result_row(
            frame, "Mental Health Resilience:",
            data.get("resilience", "Unknown"),
            f"Score: {data.get('total_risk_score', 0)}"
        )

        self.create_result_row(
            frame, "Variants Analyzed:",
            str(data.get("variants_analyzed", 0))
        )

    def create_cognitive_section(self):
        """Create cognitive profile section"""
        data = self.results.get("cognitive_profile", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Cognitive Profile")

        profile = data.get("profile", {})

        if profile.get("stress_cognition"):
            stress_type = profile["stress_cognition"]
            if stress_type == "warrior":
                desc = "Warrior type - performs well under stress, may seek stimulation"
            elif stress_type == "worrier":
                desc = "Worrier type - higher baseline cognition, stress-sensitive"
            else:
                desc = "Balanced cognitive profile"

            self.create_result_row(frame, "Stress-Cognition Type:", stress_type.title())
            info = ctk.CTkLabel(
                frame,
                text=f"  {desc}",
                font=ctk.CTkFont(size=12),
                text_color="gray"
            )
            info.pack(pady=2, padx=15, anchor="w")

        if profile.get("memory"):
            self.create_result_row(frame, "Memory Formation:", profile["memory"].title())

        if profile.get("cognitive_aging"):
            self.create_result_row(frame, "Cognitive Aging:", profile["cognitive_aging"].title())

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_depression_section(self):
        """Create depression risk section"""
        data = self.results.get("depression", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Depression Risk Factors")

        self.create_result_row(
            frame, "Risk Level:",
            data.get("risk_level", "Unknown"),
            f"Score: {data.get('risk_score', 0)}"
        )

        findings = data.get("key_findings", [])
        if findings:
            for finding in findings[:2]:
                finding_label = ctk.CTkLabel(
                    frame,
                    text=f"  {finding.get('gene', '')}: {finding.get('description', '')}",
                    font=ctk.CTkFont(size=11),
                    text_color="gray"
                )
                finding_label.pack(pady=2, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_anxiety_section(self):
        """Create anxiety risk section"""
        data = self.results.get("anxiety", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Anxiety Risk Factors")

        self.create_result_row(
            frame, "Risk Level:",
            data.get("risk_level", "Unknown"),
            f"Score: {data.get('risk_score', 0)}"
        )

        findings = data.get("key_findings", [])
        if findings:
            for finding in findings[:2]:
                finding_label = ctk.CTkLabel(
                    frame,
                    text=f"  {finding.get('gene', '')}: {finding.get('description', '')}",
                    font=ctk.CTkFont(size=11),
                    text_color="gray"
                )
                finding_label.pack(pady=2, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_adhd_section(self):
        """Create ADHD risk section"""
        data = self.results.get("adhd", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("ADHD Risk Factors")

        self.create_result_row(
            frame, "Risk Level:",
            data.get("risk_level", "Unknown"),
            f"Score: {data.get('risk_score', 0)}"
        )

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_ptsd_section(self):
        """Create PTSD vulnerability section"""
        data = self.results.get("ptsd_vulnerability", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("PTSD/Stress Vulnerability")

        self.create_result_row(
            frame, "Vulnerability Level:",
            data.get("risk_level", "Unknown"),
            f"Score: {data.get('risk_score', 0)}"
        )

        info = ctk.CTkLabel(
            frame,
            text="These genes affect stress hormone response and fear extinction learning",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        )
        info.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_addiction_section(self):
        """Create addiction vulnerability section"""
        data = self.results.get("addiction_vulnerability", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Addiction Vulnerability")

        self.create_result_row(
            frame, "Vulnerability Level:",
            data.get("risk_level", "Unknown"),
            f"Score: {data.get('risk_score', 0)}"
        )

        info = ctk.CTkLabel(
            frame,
            text="These genes affect reward sensitivity and substance metabolism",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        )
        info.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_bipolar_section(self):
        """Create bipolar risk section"""
        data = self.results.get("bipolar", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Bipolar Disorder Risk Factors")

        self.create_result_row(
            frame, "Risk Level:",
            data.get("risk_level", "Unknown"),
            f"Score: {data.get('risk_score', 0)}"
        )

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_schizophrenia_section(self):
        """Create schizophrenia risk section"""
        data = self.results.get("schizophrenia", {})
        if not data or data.get("variants_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Schizophrenia Risk Factors")

        self.create_result_row(
            frame, "Risk Level:",
            data.get("risk_level", "Unknown"),
            f"Score: {data.get('risk_score', 0)}"
        )

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_recommendations_section(self):
        """Create personalized recommendations section"""
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

        # Professional help note
        note = ctk.CTkLabel(
            frame,
            text="If you're experiencing mental health challenges, please consult a healthcare professional.",
            font=ctk.CTkFont(size=11),
            text_color="orange"
        )
        note.pack(pady=(10, 15), padx=15, anchor="w")


class MentalHealthSummaryCard(ctk.CTkFrame):
    """Compact summary card for mental health genetics"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results or {}
        self.build_ui()

    def build_ui(self):
        """Build the summary card UI"""
        title = ctk.CTkLabel(
            self,
            text="Mental Health Genetics",
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
        if overall.get("resilience"):
            metric_label = ctk.CTkLabel(
                self,
                text=overall["resilience"],
                font=ctk.CTkFont(size=12)
            )
            metric_label.pack(pady=2, padx=15, anchor="w")

        # Cognitive type
        cognitive = self.results.get("cognitive_profile", {}).get("profile", {})
        if cognitive.get("stress_cognition"):
            cog_label = ctk.CTkLabel(
                self,
                text=f"Type: {cognitive['stress_cognition'].title()}",
                font=ctk.CTkFont(size=11),
                text_color="gray"
            )
            cog_label.pack(pady=2, padx=15, anchor="w")

        ctk.CTkLabel(self, text="").pack(pady=(0, 10))
