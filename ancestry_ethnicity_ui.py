"""
Ancestry Ethnicity Estimate UI Module
CustomTkinter frames for displaying granular regional ancestry results
Similar to AncestryDNA's ethnicity estimate display
"""

import customtkinter as ctk
from typing import Dict, Any, Optional, List


# Color palette for regions (matching AncestryDNA-style colors)
REGION_COLORS = {
    'Italy': '#E74C3C',
    'Celtic & Gaelic': '#27AE60',
    'England': '#3498DB',
    'Eastern Mediterranean': '#9B59B6',
    'Southeastern Europe': '#E67E22',
    'Nordic': '#1ABC9C',
    'Western Mediterranean Islands': '#F39C12',
    'Northern Africa': '#D35400',
    'Germanic Europe': '#2980B9',
    'France': '#8E44AD',
    'Eastern Europe': '#C0392B',
    'Other': '#7F8C8D',
}


class AncestryEthnicityFrame(ctk.CTkScrollableFrame):
    """Main frame for ancestry ethnicity estimate display"""

    def __init__(self, parent, snp_dict=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.snp_dict = None
        self.results = None
        self.configure(fg_color="transparent")

        # Convert DataFrame to dict if needed
        if snp_dict is not None:
            try:
                # Check if it's a DataFrame
                if hasattr(snp_dict, 'iterrows'):
                    self.snp_dict = self._dataframe_to_dict(snp_dict)
                elif isinstance(snp_dict, dict):
                    self.snp_dict = snp_dict
                else:
                    self.snp_dict = None
            except Exception as e:
                print(f"Error converting DNA data: {e}")
                self.snp_dict = None

        if self.snp_dict:
            self.analyze_ancestry()

        self.build_ui()

    def _dataframe_to_dict(self, df) -> Dict[str, str]:
        """Convert a DNA DataFrame to rsid -> genotype dict"""
        snp_dict = {}
        try:
            # Handle different column name formats
            cols = [c.lower().strip() for c in df.columns]
            df.columns = cols

            for _, row in df.iterrows():
                rsid = str(row.get('rsid', row.iloc[0]))

                # Get genotype - either from allele1/allele2 or genotype column
                if 'allele1' in cols and 'allele2' in cols:
                    a1 = str(row['allele1'])
                    a2 = str(row['allele2'])
                    if a1 not in ['0', '-', 'N', 'D', 'I', ''] and a2 not in ['0', '-', 'N', 'D', 'I', '']:
                        snp_dict[rsid] = a1 + a2
                elif 'genotype' in cols:
                    gt = str(row['genotype'])
                    if len(gt) >= 2 and gt not in ['--', 'NN', '00', 'II', 'DD']:
                        snp_dict[rsid] = gt
        except Exception as e:
            print(f"Error parsing DataFrame: {e}")

        return snp_dict

    def analyze_ancestry(self):
        """Run ancestry analysis on loaded DNA data"""
        try:
            from calibrated_ancestry_engine import CalibratedAncestryEngine
            engine = CalibratedAncestryEngine()
            engine.load_dna(self.snp_dict)
            self.results = engine.analyze()
        except Exception as e:
            print(f"Ancestry analysis error: {e}")
            self.results = None

    def build_ui(self):
        """Build the ancestry ethnicity UI"""
        # Clear existing widgets
        for widget in self.winfo_children():
            widget.destroy()

        # Title section
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(fill="x", padx=20, pady=(20, 10))

        title = ctk.CTkLabel(
            title_frame,
            text="Ethnicity Estimate",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            title_frame,
            text="Your DNA reveals your genetic ancestry across world regions",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle.pack(anchor="w", pady=(5, 0))

        if not self.snp_dict:
            self.show_no_data_message()
            return

        if not self.results:
            self.show_error_message()
            return

        # Confidence indicator
        self.create_confidence_section()

        # Main ethnicity breakdown
        self.create_ethnicity_breakdown()

        # Continental summary
        self.create_continental_summary()

        # Methodology note
        self.create_methodology_note()

    def show_no_data_message(self):
        """Show message when no DNA data is loaded"""
        msg_frame = ctk.CTkFrame(self)
        msg_frame.pack(fill="x", padx=20, pady=50)

        icon = ctk.CTkLabel(
            msg_frame,
            text="DNA",
            font=ctk.CTkFont(size=48, weight="bold"),
            text_color="gray"
        )
        icon.pack(pady=(30, 10))

        msg = ctk.CTkLabel(
            msg_frame,
            text="Load a DNA file to see your ethnicity estimate",
            font=ctk.CTkFont(size=16)
        )
        msg.pack(pady=(0, 30))

    def show_error_message(self):
        """Show error message"""
        msg = ctk.CTkLabel(
            self,
            text="Unable to analyze ancestry. Please check your DNA file.",
            font=ctk.CTkFont(size=14),
            text_color="#FF6B6B"
        )
        msg.pack(pady=50)

    def create_confidence_section(self):
        """Create the confidence indicator"""
        conf_frame = ctk.CTkFrame(self, fg_color=("gray90", "gray17"))
        conf_frame.pack(fill="x", padx=20, pady=(10, 20))

        markers_matched = self.results.get('markers_matched', 0)
        markers_total = self.results.get('markers_total', 0)
        confidence = self.results.get('confidence', 0)

        conf_label = ctk.CTkLabel(
            conf_frame,
            text=f"Analysis Confidence: {confidence:.0f}%",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        conf_label.pack(pady=(15, 5), padx=15, anchor="w")

        # Progress bar
        progress = ctk.CTkProgressBar(conf_frame, width=300)
        progress.pack(pady=(0, 5), padx=15, anchor="w")
        progress.set(confidence / 100)

        detail = ctk.CTkLabel(
            conf_frame,
            text=f"{markers_matched} of {markers_total} ancestry markers analyzed",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        detail.pack(pady=(0, 15), padx=15, anchor="w")

    def create_ethnicity_breakdown(self):
        """Create the main ethnicity breakdown display"""
        section_title = ctk.CTkLabel(
            self,
            text="Your Ethnicity Regions",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        section_title.pack(pady=(10, 15), padx=20, anchor="w")

        grouped = self.results.get('grouped', {})

        for parent_region, sub_regions in grouped.items():
            total_pct = sum(sub_regions.values())
            if total_pct < 0.5:
                continue

            self.create_region_card(parent_region, sub_regions, total_pct)

    def create_region_card(self, parent_region: str, sub_regions: Dict[str, float], total_pct: float):
        """Create a card for a parent region with its sub-regions"""
        color = REGION_COLORS.get(parent_region, '#7F8C8D')

        # Main card frame
        card = ctk.CTkFrame(self)
        card.pack(fill="x", padx=20, pady=8)

        # Header with color indicator and percentage
        header_frame = ctk.CTkFrame(card, fg_color="transparent")
        header_frame.pack(fill="x", padx=15, pady=(15, 10))

        # Color bar
        color_bar = ctk.CTkFrame(header_frame, fg_color=color, width=8, height=40, corner_radius=4)
        color_bar.pack(side="left", padx=(0, 12))
        color_bar.pack_propagate(False)

        # Region name and percentage
        text_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        text_frame.pack(side="left", fill="x", expand=True)

        region_name = ctk.CTkLabel(
            text_frame,
            text=parent_region,
            font=ctk.CTkFont(size=18, weight="bold"),
            anchor="w"
        )
        region_name.pack(anchor="w")

        # Percentage with bar
        pct_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        pct_frame.pack(side="right")

        pct_label = ctk.CTkLabel(
            pct_frame,
            text=f"{total_pct:.0f}%",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=color
        )
        pct_label.pack()

        # Sub-regions
        sub_frame = ctk.CTkFrame(card, fg_color=("gray90", "gray20"), corner_radius=8)
        sub_frame.pack(fill="x", padx=15, pady=(0, 15))

        for sub_name, sub_pct in sub_regions.items():
            if sub_pct < 0.5:
                continue
            self.create_subregion_row(sub_frame, sub_name, sub_pct, color)

    def create_subregion_row(self, parent: ctk.CTkFrame, name: str, pct: float, color: str):
        """Create a row for a sub-region"""
        row = ctk.CTkFrame(parent, fg_color="transparent")
        row.pack(fill="x", padx=12, pady=6)

        # Small color indicator
        indicator = ctk.CTkFrame(row, fg_color=color, width=4, height=20, corner_radius=2)
        indicator.pack(side="left", padx=(0, 10))
        indicator.pack_propagate(False)

        # Name
        name_label = ctk.CTkLabel(
            row,
            text=name,
            font=ctk.CTkFont(size=14),
            anchor="w"
        )
        name_label.pack(side="left", fill="x", expand=True)

        # Percentage
        pct_label = ctk.CTkLabel(
            row,
            text=f"{pct:.1f}%",
            font=ctk.CTkFont(size=14, weight="bold"),
            width=60,
            anchor="e"
        )
        pct_label.pack(side="right")

        # Visual bar
        bar_width = max(1, min(int(pct * 2), 100))
        bar_frame = ctk.CTkFrame(row, fg_color=("gray80", "gray30"), width=100, height=6, corner_radius=3)
        bar_frame.pack(side="right", padx=(0, 10))
        bar_frame.pack_propagate(False)

        if bar_width > 0:
            bar_fill = ctk.CTkFrame(bar_frame, fg_color=color, width=bar_width, height=6, corner_radius=3)
            bar_fill.place(x=0, y=0)

    def create_continental_summary(self):
        """Create continental ancestry summary"""
        section_frame = ctk.CTkFrame(self)
        section_frame.pack(fill="x", padx=20, pady=(20, 10))

        title = ctk.CTkLabel(
            section_frame,
            text="Continental Ancestry",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        title.pack(pady=(15, 10), padx=15, anchor="w")

        continental = self.results.get('continental', {})

        for continent, pct in sorted(continental.items(), key=lambda x: x[1], reverse=True):
            if pct < 0.5:
                continue

            row = ctk.CTkFrame(section_frame, fg_color="transparent")
            row.pack(fill="x", padx=15, pady=4)

            name_label = ctk.CTkLabel(
                row,
                text=continent.replace('_', ' '),
                font=ctk.CTkFont(size=14),
                width=150,
                anchor="w"
            )
            name_label.pack(side="left")

            pct_label = ctk.CTkLabel(
                row,
                text=f"{pct:.1f}%",
                font=ctk.CTkFont(size=14, weight="bold"),
                width=60
            )
            pct_label.pack(side="left")

            # Progress bar
            bar = ctk.CTkProgressBar(row, width=200)
            bar.pack(side="left", padx=(10, 0))
            bar.set(pct / 100)

        # Padding at bottom
        ctk.CTkLabel(section_frame, text="").pack(pady=10)

    def create_methodology_note(self):
        """Create methodology explanation"""
        note_frame = ctk.CTkFrame(self, fg_color=("gray90", "gray17"))
        note_frame.pack(fill="x", padx=20, pady=(10, 30))

        title = ctk.CTkLabel(
            note_frame,
            text="About This Estimate",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        title.pack(pady=(15, 5), padx=15, anchor="w")

        note_text = (
            "This ethnicity estimate is calculated using ancestry-informative markers "
            "from your DNA compared against reference populations from the 1000 Genomes "
            "Project. Sub-regional estimates are derived using genetic gradient modeling "
            "based on published population genetics research.\n\n"
            "Note: These results are estimates and may differ from commercial services "
            "which use proprietary reference panels. The accuracy is highest for "
            "continental ancestry and progressively more estimated for sub-regions."
        )

        note = ctk.CTkLabel(
            note_frame,
            text=note_text,
            font=ctk.CTkFont(size=12),
            text_color="gray",
            wraplength=600,
            justify="left"
        )
        note.pack(pady=(0, 15), padx=15, anchor="w")

    def update_results(self, snp_dict: Dict[str, str]):
        """Update with new DNA data"""
        self.snp_dict = snp_dict
        self.analyze_ancestry()
        self.build_ui()


# For testing
if __name__ == "__main__":
    import pandas as pd

    app = ctk.CTk()
    app.title("Ancestry Ethnicity Test")
    app.geometry("800x900")

    # Load test data
    try:
        filepath = r"C:\Users\micro\Downloads\dna_extracted\AncestryDNA.txt"
        df = pd.read_csv(filepath, sep='\t', comment='#')
        df.columns = ['rsid', 'chromosome', 'position', 'allele1', 'allele2']

        snp_dict = {}
        for _, row in df.iterrows():
            rsid = str(row['rsid'])
            a1, a2 = str(row['allele1']), str(row['allele2'])
            if a1 not in ['0', '-', 'N'] and a2 not in ['0', '-', 'N']:
                snp_dict[rsid] = a1 + a2

        frame = AncestryEthnicityFrame(app, snp_dict)
        frame.pack(fill="both", expand=True)
    except Exception as e:
        print(f"Error: {e}")
        frame = AncestryEthnicityFrame(app, None)
        frame.pack(fill="both", expand=True)

    app.mainloop()
