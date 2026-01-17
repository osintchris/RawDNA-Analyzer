"""
Ancient DNA & History UI Module
CustomTkinter frames for displaying ancient ancestry and historical genetics
"""

import customtkinter as ctk
from typing import Dict, Any, Optional


class AncientDNAHistoryFrame(ctk.CTkScrollableFrame):
    """Main frame for ancient DNA and history genetics display"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results
        self.configure(fg_color="transparent")
        self.build_ui()

    def build_ui(self):
        """Build the ancient DNA history UI"""
        # Title
        title = ctk.CTkLabel(
            self,
            text="Ancient DNA & Historical Genetics",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(20, 5), padx=20, anchor="w")

        subtitle = ctk.CTkLabel(
            self,
            text="Explore your genetic connection to ancient populations and human history",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle.pack(pady=(0, 10), padx=20, anchor="w")

        # Info note explaining the percentages
        info_frame = ctk.CTkFrame(self, fg_color="#1e3a5f", corner_radius=8)
        info_frame.pack(fill="x", padx=20, pady=(0, 15))
        ctk.CTkLabel(
            info_frame,
            text="What the percentages mean: The % shown is the proportion of known archaic markers you carry. If it shows '35.7%' for Neanderthal (15/42), that means you have 15 of the 42 known Neanderthal-derived variants in our database. Your actual Neanderthal ancestry is estimated at 1-4% of your total genome.",
            font=ctk.CTkFont(size=11), text_color="#93c5fd",
            wraplength=700, justify="left"
        ).pack(padx=15, pady=8)

        if not self.results:
            no_data = ctk.CTkLabel(
                self,
                text="No DNA data loaded. Please load a DNA file to see ancient DNA analysis.",
                font=ctk.CTkFont(size=14)
            )
            no_data.pack(pady=50)
            return

        # Summary section first
        self.create_summary_section()

        # Create sections for each category
        self.create_neanderthal_section()
        self.create_denisovan_section()
        self.create_farmer_section()
        self.create_hunter_gatherer_section()
        self.create_steppe_section()
        self.create_pathogen_section()
        self.create_pigmentation_section()
        self.create_migration_section()

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

        value_color = color if color else "#4ECDC4"  # Default to teal for ancient DNA
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

    def create_snp_details(self, parent: ctk.CTkFrame, snps: list):
        """Create SNP details display"""
        if not snps:
            return

        details_frame = ctk.CTkFrame(parent, fg_color=("gray90", "gray20"))
        details_frame.pack(fill="x", padx=15, pady=(5, 15))

        header = ctk.CTkLabel(
            details_frame,
            text="Ancient Markers Analyzed:",
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
                text=f"... and {len(snps) - 5} more markers",
                font=ctk.CTkFont(size=11),
                text_color="gray"
            )
            more_label.pack(pady=(2, 10), padx=15, anchor="w")

    def create_findings_list(self, parent: ctk.CTkFrame, findings: list, max_items: int = 4):
        """Create a findings list"""
        if not findings:
            return

        for finding in findings[:max_items]:
            finding_label = ctk.CTkLabel(
                parent,
                text=f"  • {finding}",
                font=ctk.CTkFont(size=12),
                text_color="#FFE66D",  # Amber for historical findings
                wraplength=600
            )
            finding_label.pack(pady=2, padx=15, anchor="w")

    def create_summary_section(self):
        """Create overall summary section"""
        summary = self.results.get("summary", {})
        if not summary:
            return

        frame = self.create_section_frame("Your Ancient Ancestry Overview")

        # Archaic ancestry
        archaic = summary.get("archaic_ancestry", [])
        if archaic:
            archaic_label = ctk.CTkLabel(
                frame,
                text="Archaic Human Ancestry:",
                font=ctk.CTkFont(size=14, weight="bold")
            )
            archaic_label.pack(pady=(5, 5), padx=15, anchor="w")

            for item in archaic:
                item_label = ctk.CTkLabel(
                    frame,
                    text=f"  • {item}",
                    font=ctk.CTkFont(size=12),
                    text_color="#9B59B6"  # Purple for archaic
                )
                item_label.pack(pady=2, padx=15, anchor="w")

        # Historical ancestry markers
        historical = summary.get("historical_ancestry_markers", [])
        if historical:
            hist_label = ctk.CTkLabel(
                frame,
                text="Historical Population Markers:",
                font=ctk.CTkFont(size=14, weight="bold")
            )
            hist_label.pack(pady=(15, 5), padx=15, anchor="w")

            for item in historical:
                item_label = ctk.CTkLabel(
                    frame,
                    text=f"  • {item}",
                    font=ctk.CTkFont(size=12),
                    text_color="#3498DB"  # Blue for historical
                )
                item_label.pack(pady=2, padx=15, anchor="w")

        # Selected traits
        traits = summary.get("selected_traits", [])
        if traits:
            traits_label = ctk.CTkLabel(
                frame,
                text="Historically Selected Traits:",
                font=ctk.CTkFont(size=14, weight="bold")
            )
            traits_label.pack(pady=(15, 5), padx=15, anchor="w")

            for trait in traits[:5]:
                trait_label = ctk.CTkLabel(
                    frame,
                    text=f"  • {trait}",
                    font=ctk.CTkFont(size=12),
                    text_color="#4ECDC4"
                )
                trait_label.pack(pady=2, padx=15, anchor="w")

        # Historical context
        context = summary.get("historical_context", [])
        if context:
            ctx_label = ctk.CTkLabel(
                frame,
                text="Historical Context:",
                font=ctk.CTkFont(size=14, weight="bold")
            )
            ctx_label.pack(pady=(15, 5), padx=15, anchor="w")

            for ctx in context:
                ctx_item = ctk.CTkLabel(
                    frame,
                    text=f"  {ctx}",
                    font=ctk.CTkFont(size=12),
                    text_color="gray",
                    wraplength=600
                )
                ctx_item.pack(pady=2, padx=15, anchor="w")

        ctk.CTkLabel(frame, text="").pack(pady=5)

    def create_neanderthal_section(self):
        """Create Neanderthal ancestry section"""
        data = self.results.get("neanderthal_ancestry", {})
        if not data:
            return

        frame = self.create_section_frame("Neanderthal Ancestry")

        self.create_result_row(
            frame, "Estimated Percentage:",
            data.get("percentage_estimate", "Unknown"),
            color="#9B59B6"
        )

        self.create_result_row(
            frame, "Neanderthal Score:",
            f"{data.get('neanderthal_score', 0)} / {data.get('max_possible_score', 0)}",
            "markers with Neanderthal variants"
        )

        # Neanderthal traits
        traits = data.get("neanderthal_traits", [])
        if traits:
            traits_label = ctk.CTkLabel(
                frame,
                text="Neanderthal-Derived Traits:",
                font=ctk.CTkFont(size=13, weight="bold")
            )
            traits_label.pack(pady=(10, 5), padx=15, anchor="w")

            for trait in traits[:5]:
                trait_item = ctk.CTkLabel(
                    frame,
                    text=f"  • {trait}",
                    font=ctk.CTkFont(size=12),
                    text_color="#9B59B6"
                )
                trait_item.pack(pady=2, padx=15, anchor="w")

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_denisovan_section(self):
        """Create Denisovan ancestry section"""
        data = self.results.get("denisovan_ancestry", {})
        if not data or not data.get("snps_analyzed"):
            return

        frame = self.create_section_frame("Denisovan Ancestry")

        self.create_result_row(
            frame, "Denisovan Score:",
            str(data.get("denisovan_score", 0)),
            color="#E74C3C"
        )

        traits = data.get("denisovan_traits", [])
        if traits:
            for trait in traits:
                trait_item = ctk.CTkLabel(
                    frame,
                    text=f"  • {trait}",
                    font=ctk.CTkFont(size=12),
                    text_color="#E74C3C"
                )
                trait_item.pack(pady=2, padx=15, anchor="w")

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_farmer_section(self):
        """Create ancient farmer section"""
        data = self.results.get("ancient_farmer", {})
        if not data:
            return

        frame = self.create_section_frame("Neolithic Farmer Ancestry")

        self.create_result_row(
            frame, "Lactase Persistence:",
            data.get("lactase_persistent", "Unknown"),
            color="#27AE60"
        )

        self.create_result_row(
            frame, "Farmer Markers Found:",
            str(data.get("farmer_markers_found", 0))
        )

        traits = data.get("neolithic_traits", [])
        if traits:
            for trait in traits:
                trait_item = ctk.CTkLabel(
                    frame,
                    text=f"  • {trait}",
                    font=ctk.CTkFont(size=12),
                    text_color="#27AE60"
                )
                trait_item.pack(pady=2, padx=15, anchor="w")

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_hunter_gatherer_section(self):
        """Create hunter-gatherer section"""
        data = self.results.get("hunter_gatherer", {})
        if not data:
            return

        frame = self.create_section_frame("Mesolithic Hunter-Gatherer Ancestry")

        self.create_result_row(
            frame, "Blue Eye Origin:",
            data.get("blue_eye_origin", "Unknown"),
            color="#3498DB"
        )

        light_skin = data.get("light_skin_genes", [])
        if light_skin:
            self.create_result_row(
                frame, "Light Skin Genes:",
                ", ".join(light_skin)
            )

        traits = data.get("whg_traits", [])
        if traits:
            for trait in traits:
                trait_item = ctk.CTkLabel(
                    frame,
                    text=f"  • {trait}",
                    font=ctk.CTkFont(size=12),
                    text_color="#3498DB"
                )
                trait_item.pack(pady=2, padx=15, anchor="w")

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_steppe_section(self):
        """Create Steppe/Yamnaya section"""
        data = self.results.get("steppe_ancestry", {})
        if not data:
            return

        frame = self.create_section_frame("Bronze Age Steppe Ancestry")

        self.create_result_row(
            frame, "Steppe Markers Found:",
            str(data.get("steppe_markers_found", 0)),
            color="#F39C12"
        )

        traits = data.get("steppe_traits", [])
        if traits:
            for trait in traits:
                trait_item = ctk.CTkLabel(
                    frame,
                    text=f"  • {trait}",
                    font=ctk.CTkFont(size=12),
                    text_color="#F39C12"
                )
                trait_item.pack(pady=2, padx=15, anchor="w")

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_pathogen_section(self):
        """Create pathogen resistance section"""
        data = self.results.get("pathogen_resistance", {})
        if not data:
            return

        frame = self.create_section_frame("Ancient Pathogen Resistance")

        protective = data.get("protective_variants", [])
        if protective:
            prot_label = ctk.CTkLabel(
                frame,
                text="Protective Variants:",
                font=ctk.CTkFont(size=13, weight="bold")
            )
            prot_label.pack(pady=(5, 5), padx=15, anchor="w")

            for variant in protective:
                var_item = ctk.CTkLabel(
                    frame,
                    text=f"  • {variant}",
                    font=ctk.CTkFont(size=12),
                    text_color="#4ECDC4"
                )
                var_item.pack(pady=2, padx=15, anchor="w")

        selection = data.get("historical_selection", [])
        if selection:
            sel_label = ctk.CTkLabel(
                frame,
                text="Historical Selection Events:",
                font=ctk.CTkFont(size=13, weight="bold")
            )
            sel_label.pack(pady=(10, 5), padx=15, anchor="w")

            for event in selection:
                event_item = ctk.CTkLabel(
                    frame,
                    text=f"  • {event}",
                    font=ctk.CTkFont(size=12),
                    text_color="gray"
                )
                event_item.pack(pady=2, padx=15, anchor="w")

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_pigmentation_section(self):
        """Create pigmentation history section"""
        data = self.results.get("pigmentation_history", {})
        if not data:
            return

        frame = self.create_section_frame("Pigmentation Adaptation History")

        self.create_result_row(
            frame, "Red Hair Variants:",
            str(data.get("red_hair_variants", 0)),
            color="#E74C3C" if data.get("red_hair_variants", 0) >= 2 else "white"
        )

        self.create_result_row(
            frame, "Light Skin Adaptation:",
            data.get("light_skin_adaptation", "Unknown")
        )

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

    def create_migration_section(self):
        """Create migration markers section"""
        data = self.results.get("migration_markers", {})
        if not data:
            return

        frame = self.create_section_frame("Historical Migration Markers")

        markers = data.get("east_asian_markers", [])
        if markers:
            mark_label = ctk.CTkLabel(
                frame,
                text="East Asian Migration Markers:",
                font=ctk.CTkFont(size=13, weight="bold")
            )
            mark_label.pack(pady=(5, 5), padx=15, anchor="w")

            for marker in markers:
                mark_item = ctk.CTkLabel(
                    frame,
                    text=f"  • {marker}",
                    font=ctk.CTkFont(size=12),
                    text_color="#E67E22"
                )
                mark_item.pack(pady=2, padx=15, anchor="w")

        patterns = data.get("migration_patterns", [])
        if patterns:
            pat_label = ctk.CTkLabel(
                frame,
                text="Migration Patterns:",
                font=ctk.CTkFont(size=13, weight="bold")
            )
            pat_label.pack(pady=(10, 5), padx=15, anchor="w")

            for pattern in patterns:
                pat_item = ctk.CTkLabel(
                    frame,
                    text=f"  • {pattern}",
                    font=ctk.CTkFont(size=12),
                    text_color="gray"
                )
                pat_item.pack(pady=2, padx=15, anchor="w")

        self.create_findings_list(frame, data.get("findings", []))
        self.create_snp_details(frame, data.get("snps_analyzed", []))

        # Final note
        note = ctk.CTkLabel(
            frame,
            text="Note: Ancient DNA percentages are estimates based on marker analysis. Full genome sequencing provides more accurate results.",
            font=ctk.CTkFont(size=11),
            text_color="gray",
            wraplength=600
        )
        note.pack(pady=(15, 15), padx=15, anchor="w")


class AncientDNASummaryCard(ctk.CTkFrame):
    """Compact summary card for ancient DNA"""

    def __init__(self, parent, results: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(parent, **kwargs)
        self.results = results or {}
        self.build_ui()

    def build_ui(self):
        """Build the summary card UI"""
        title = ctk.CTkLabel(
            self,
            text="Ancient DNA",
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

        # Neanderthal
        neanderthal = self.results.get("neanderthal_ancestry", {})
        if neanderthal.get("percentage_estimate"):
            metric_label = ctk.CTkLabel(
                self,
                text=f"Neanderthal: {neanderthal.get('percentage_estimate', 'Unknown')}",
                font=ctk.CTkFont(size=12),
                text_color="#9B59B6"
            )
            metric_label.pack(pady=2, padx=15, anchor="w")

        # Summary markers
        summary = self.results.get("summary", {})
        historical = summary.get("historical_ancestry_markers", [])
        if historical:
            for marker in historical[:2]:
                marker_label = ctk.CTkLabel(
                    self,
                    text=marker,
                    font=ctk.CTkFont(size=11),
                    text_color="gray"
                )
                marker_label.pack(pady=1, padx=15, anchor="w")

        ctk.CTkLabel(self, text="").pack(pady=(0, 10))
