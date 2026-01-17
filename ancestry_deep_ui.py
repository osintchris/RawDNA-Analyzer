"""
Deep Ancestry Genetics UI Module
CustomTkinter frames for displaying detailed regional ancestry analysis
"""

import customtkinter as ctk
from typing import Dict, Any, Optional


class DeepAncestryFrame(ctk.CTkScrollableFrame):
    """Main frame for deep ancestry genetics display"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results
        self.configure(fg_color="transparent")
        self.build_ui()

    def build_ui(self):
        """Build the deep ancestry genetics UI"""
        # Title
        title = ctk.CTkLabel(
            self,
            text="Deep Ancestry Analysis",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(20, 5), padx=20, anchor="w")

        subtitle = ctk.CTkLabel(
            self,
            text="Detailed regional ancestry markers and ancient migration patterns",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle.pack(pady=(0, 20), padx=20, anchor="w")

        if not self.results:
            no_data = ctk.CTkLabel(
                self,
                text="No DNA data loaded. Please load a DNA file to see deep ancestry analysis.",
                font=ctk.CTkFont(size=14)
            )
            no_data.pack(pady=50)
            return

        # Create sections
        self.create_summary_section()
        self.create_european_section()
        self.create_african_section()
        self.create_east_asian_section()
        self.create_south_asian_section()
        self.create_native_american_section()
        self.create_mena_section()
        self.create_jewish_section()
        self.create_migration_section()
        self.create_isolated_section()

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
            width=220,
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
        if any(word in value_lower for word in ["high", "strong", "likely", "yes", "detected"]):
            return "#4ECDC4"
        elif any(word in value_lower for word in ["low", "unlikely", "no", "absent"]):
            return "#FF6B6B"
        elif any(word in value_lower for word in ["moderate", "possible", "some"]):
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
            text="Ancestry Markers Analyzed:",
            font=ctk.CTkFont(size=12, weight="bold")
        )
        header.pack(pady=(10, 5), padx=10, anchor="w")

        for snp in snps[:5]:
            snp_text = f"{snp.get('rsid', 'Unknown')}: {snp.get('genotype', 'N/A')}"
            if snp.get('marker'):
                snp_text += f" ({snp.get('marker')})"

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
                text=f"... and {len(snps) - 5} more markers",
                font=ctk.CTkFont(size=11),
                text_color="gray"
            )
            more_label.pack(pady=(2, 10), padx=15, anchor="w")

    def create_summary_section(self):
        """Create summary section"""
        data = self.results.get("overall", {})
        if not data:
            return

        frame = self.create_section_frame("Ancestry Profile Summary")

        self.create_result_row(
            frame, "Total Markers Analyzed:",
            str(data.get("total_markers_analyzed", 0))
        )

        regions = data.get("regions_detected", [])
        if regions:
            regions_text = ", ".join(regions[:5])
            if len(regions) > 5:
                regions_text += f" +{len(regions) - 5} more"
            self.create_result_row(frame, "Regions Detected:", regions_text)

        migrations = data.get("migration_patterns", [])
        if migrations:
            for migration in migrations[:3]:
                mig_label = ctk.CTkLabel(
                    frame,
                    text=f"  {migration}",
                    font=ctk.CTkFont(size=12),
                    text_color="#4ECDC4"
                )
                mig_label.pack(pady=2, padx=15, anchor="w")

    def create_european_section(self):
        """Create European ancestry section"""
        data = self.results.get("european_regional", {})
        if not data or data.get("markers_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("European Regional Ancestry")

        self.create_result_row(
            frame, "Northern European:",
            data.get("northern_european", "Unknown"),
            f"Score: {data.get('northern_score', 0)}"
        )

        self.create_result_row(
            frame, "Mediterranean:",
            data.get("mediterranean", "Unknown"),
            f"Score: {data.get('mediterranean_score', 0)}"
        )

        self.create_result_row(
            frame, "Eastern European:",
            data.get("eastern_european", "Unknown"),
            f"Score: {data.get('eastern_score', 0)}"
        )

        if data.get("lactase_persistence"):
            lp_label = ctk.CTkLabel(
                frame,
                text="Lactase persistence detected - Northern European heritage marker",
                font=ctk.CTkFont(size=11),
                text_color="#4ECDC4"
            )
            lp_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_african_section(self):
        """Create African ancestry section"""
        data = self.results.get("african_regional", {})
        if not data or data.get("markers_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("African Regional Ancestry")

        self.create_result_row(
            frame, "Sub-Saharan African:",
            data.get("sub_saharan", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        if data.get("duffy_null"):
            duffy_label = ctk.CTkLabel(
                frame,
                text="Duffy null allele detected - malaria resistance marker, West/Central African",
                font=ctk.CTkFont(size=11),
                text_color="#4ECDC4"
            )
            duffy_label.pack(pady=5, padx=15, anchor="w")

        if data.get("sickle_cell_carrier"):
            sc_label = ctk.CTkLabel(
                frame,
                text="Sickle cell trait detected - African/Mediterranean ancestry marker",
                font=ctk.CTkFont(size=11),
                text_color="orange"
            )
            sc_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_east_asian_section(self):
        """Create East Asian ancestry section"""
        data = self.results.get("east_asian_regional", {})
        if not data or data.get("markers_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("East Asian Regional Ancestry")

        self.create_result_row(
            frame, "East Asian Markers:",
            data.get("likelihood", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        if data.get("edar_variant"):
            edar_label = ctk.CTkLabel(
                frame,
                text="EDAR variant detected - thicker hair, distinct teeth, East Asian marker",
                font=ctk.CTkFont(size=11),
                text_color="#4ECDC4"
            )
            edar_label.pack(pady=5, padx=15, anchor="w")

        if data.get("alcohol_flush"):
            flush_label = ctk.CTkLabel(
                frame,
                text="Alcohol flush reaction variant - common in East Asian populations",
                font=ctk.CTkFont(size=11),
                text_color="orange"
            )
            flush_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_south_asian_section(self):
        """Create South Asian ancestry section"""
        data = self.results.get("south_asian_regional", {})
        if not data or data.get("markers_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("South Asian Regional Ancestry")

        self.create_result_row(
            frame, "South Asian Markers:",
            data.get("likelihood", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_native_american_section(self):
        """Create Native American ancestry section"""
        data = self.results.get("native_american", {})
        if not data or data.get("markers_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Native American Ancestry")

        self.create_result_row(
            frame, "Native American Markers:",
            data.get("likelihood", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        if data.get("beringian_marker"):
            bering_label = ctk.CTkLabel(
                frame,
                text="Beringian ancestry marker detected - ancient migration from Asia",
                font=ctk.CTkFont(size=11),
                text_color="#4ECDC4"
            )
            bering_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_mena_section(self):
        """Create Middle Eastern/North African section"""
        data = self.results.get("mena_regional", {})
        if not data or data.get("markers_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Middle Eastern & North African Ancestry")

        self.create_result_row(
            frame, "MENA Markers:",
            data.get("likelihood", "Unknown"),
            f"Score: {data.get('score', 0)}"
        )

        if data.get("levantine_markers"):
            lev_label = ctk.CTkLabel(
                frame,
                text="Levantine ancestry markers detected",
                font=ctk.CTkFont(size=11),
                text_color="#4ECDC4"
            )
            lev_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_jewish_section(self):
        """Create Jewish ancestry section"""
        data = self.results.get("jewish_ancestry", {})
        if not data or data.get("markers_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Jewish Ancestry Markers")

        self.create_result_row(
            frame, "Ashkenazi Markers:",
            data.get("ashkenazi_likelihood", "Unknown")
        )

        self.create_result_row(
            frame, "Sephardic Markers:",
            data.get("sephardic_likelihood", "Unknown")
        )

        founder_mutations = data.get("founder_mutations", [])
        if founder_mutations:
            fm_label = ctk.CTkLabel(
                frame,
                text="Ashkenazi founder mutations detected - consult genetic counselor",
                font=ctk.CTkFont(size=11),
                text_color="orange"
            )
            fm_label.pack(pady=5, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_migration_section(self):
        """Create ancient migration patterns section"""
        data = self.results.get("migration_patterns", {})
        if not data or data.get("markers_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Ancient Migration Patterns")

        if data.get("neolithic_farmer"):
            self.create_result_row(
                frame, "Neolithic Farmer Ancestry:",
                "Detected",
                "Ancient Near Eastern farmers who spread to Europe"
            )

        if data.get("bronze_age_steppe"):
            self.create_result_row(
                frame, "Steppe Ancestry:",
                "Detected",
                "Bronze Age Yamnaya/Indo-European ancestry"
            )

        if data.get("out_of_africa_early"):
            self.create_result_row(
                frame, "Early Out-of-Africa:",
                "Detected",
                "Early human migration markers"
            )

        if data.get("austronesian"):
            self.create_result_row(
                frame, "Austronesian Expansion:",
                "Detected",
                "Pacific Islander migration markers"
            )

        timeline = data.get("timeline", [])
        if timeline:
            tl_header = ctk.CTkLabel(
                frame,
                text="Migration Timeline:",
                font=ctk.CTkFont(size=12, weight="bold")
            )
            tl_header.pack(pady=(10, 5), padx=15, anchor="w")

            for event in timeline[:5]:
                tl_label = ctk.CTkLabel(
                    frame,
                    text=f"  {event}",
                    font=ctk.CTkFont(size=11),
                    text_color="gray"
                )
                tl_label.pack(pady=2, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_isolated_section(self):
        """Create isolated population section"""
        data = self.results.get("isolated_populations", {})
        if not data or data.get("markers_analyzed", 0) == 0:
            return

        frame = self.create_section_frame("Isolated Population Markers")

        populations = data.get("populations_detected", [])
        if populations:
            for pop in populations:
                pop_label = ctk.CTkLabel(
                    frame,
                    text=f"  {pop}",
                    font=ctk.CTkFont(size=12),
                    text_color="#4ECDC4"
                )
                pop_label.pack(pady=3, padx=15, anchor="w")

        self.create_snp_details(frame, data.get("snps_analyzed", []))

        # Disclaimer
        disclaimer = ctk.CTkLabel(
            frame,
            text="Note: Ancestry analysis is based on population genetics and provides estimates, not absolute determinations.",
            font=ctk.CTkFont(size=11),
            text_color="orange",
            wraplength=600
        )
        disclaimer.pack(pady=(10, 15), padx=15, anchor="w")


class DeepAncestrySummaryCard(ctk.CTkFrame):
    """Compact summary card for deep ancestry genetics"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results or {}
        self.build_ui()

    def build_ui(self):
        """Build the summary card UI"""
        title = ctk.CTkLabel(
            self,
            text="Deep Ancestry",
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
        overall = self.results.get("overall", {})
        regions = overall.get("regions_detected", [])
        if regions:
            regions_text = ", ".join(regions[:3])
            regions_label = ctk.CTkLabel(
                self,
                text=f"Regions: {regions_text}",
                font=ctk.CTkFont(size=11)
            )
            regions_label.pack(pady=2, padx=15, anchor="w")

        migrations = overall.get("migration_patterns", [])
        if migrations:
            mig_label = ctk.CTkLabel(
                self,
                text=f"Migrations: {len(migrations)} detected",
                font=ctk.CTkFont(size=11),
                text_color="gray"
            )
            mig_label.pack(pady=2, padx=15, anchor="w")

        ctk.CTkLabel(self, text="").pack(pady=(0, 10))
