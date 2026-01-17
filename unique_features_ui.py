#!/usr/bin/env python3
"""
Unique Features UI - Clean, Modern Design
Less text, more impact
"""

import customtkinter as ctk
from typing import Dict, Any


# =============================================================================
# TOOLTIP CLASS - Hover info for markers
# =============================================================================

class MarkerTooltip:
    """Tooltip that appears on hover with detailed marker info"""

    def __init__(self, widget, marker_data: Dict):
        self.widget = widget
        self.marker = marker_data
        self.tooltip_window = None
        self.show_id = None
        self.hide_id = None

        # Bind main widget and ALL children recursively
        self._bind_recursive(widget)

    def _bind_recursive(self, widget):
        """Bind hover events to widget and all its children"""
        widget.bind("<Enter>", self._on_enter, add="+")
        widget.bind("<Leave>", self._on_leave, add="+")
        widget.bind("<Motion>", self._on_motion, add="+")
        # Bind to all children
        for child in widget.winfo_children():
            self._bind_recursive(child)

    def _on_enter(self, event=None):
        """Schedule showing tooltip"""
        self._cancel_hide()
        if not self.tooltip_window and not self.show_id:
            self.show_id = self.widget.after(300, self.show_tooltip)

    def _on_motion(self, event=None):
        """Mouse moving inside - keep tooltip alive"""
        self._cancel_hide()

    def _on_leave(self, event=None):
        """Schedule hiding tooltip"""
        self._cancel_show()
        if not self.hide_id:
            self.hide_id = self.widget.after(100, self.hide_tooltip)

    def _cancel_show(self):
        if self.show_id:
            self.widget.after_cancel(self.show_id)
            self.show_id = None

    def _cancel_hide(self):
        if self.hide_id:
            self.widget.after_cancel(self.hide_id)
            self.hide_id = None

    def show_tooltip(self, event=None):
        if self.tooltip_window:
            return

        x = self.widget.winfo_rootx() + 50
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 5

        self.tooltip_window = tw = ctk.CTkToplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        tw.configure(fg_color="#1a1a2e")

        # Make it stay on top
        tw.attributes("-topmost", True)

        frame = ctk.CTkFrame(tw, fg_color="#1a1a2e", corner_radius=12, border_width=1, border_color="gray30")
        frame.pack(fill="both", expand=True, padx=2, pady=2)

        inner = ctk.CTkFrame(frame, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=15, pady=12)

        # Header with gene name
        header = ctk.CTkFrame(inner, fg_color="transparent")
        header.pack(fill="x", pady=(0, 8))

        ctk.CTkLabel(header, text=self.marker['gene'],
                    font=ctk.CTkFont(size=18, weight="bold"),
                    text_color=self.marker.get('category_color', '#ffffff')).pack(side="left")

        ctk.CTkLabel(header, text=f"  {self.marker['rsid']}",
                    font=ctk.CTkFont(size=12), text_color="gray50").pack(side="left")

        # Origin badge
        origin = self.marker['origin']
        if origin == 'Neanderthal':
            origin_text = "Inherited from Neanderthals ~50,000 years ago"
            origin_color = "#ef4444"
        elif origin == 'Denisovan':
            origin_text = "Inherited from Denisovans ~50,000 years ago"
            origin_color = "#3b82f6"
        elif origin == 'Human (rare)':
            origin_text = "Rare human genetic variant"
            origin_color = "#22c55e"
        else:
            origin_text = "Common human variant"
            origin_color = "gray60"

        ctk.CTkLabel(inner, text=origin_text,
                    font=ctk.CTkFont(size=11), text_color=origin_color).pack(anchor="w")

        # Divider
        ctk.CTkFrame(inner, height=1, fg_color="gray30").pack(fill="x", pady=10)

        # Full name
        ctk.CTkLabel(inner, text=self.marker['name'],
                    font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w")

        # Full effect description (not truncated)
        effect = self.marker.get('effect', '')
        ctk.CTkLabel(inner, text=effect,
                    font=ctk.CTkFont(size=12), text_color="gray70",
                    wraplength=350, justify="left").pack(anchor="w", pady=(5, 0))

        # What this means for you
        meaning = self._get_plain_english_meaning()
        if meaning:
            ctk.CTkFrame(inner, height=1, fg_color="gray30").pack(fill="x", pady=10)
            ctk.CTkLabel(inner, text="What this means:",
                        font=ctk.CTkFont(size=11, weight="bold"), text_color="#eab308").pack(anchor="w")
            ctk.CTkLabel(inner, text=meaning,
                        font=ctk.CTkFont(size=12), text_color="gray60",
                        wraplength=350, justify="left").pack(anchor="w", pady=(3, 0))

        # Rarity info
        ctk.CTkFrame(inner, height=1, fg_color="gray30").pack(fill="x", pady=10)

        rarity_frame = ctk.CTkFrame(inner, fg_color="transparent")
        rarity_frame.pack(fill="x")

        ctk.CTkLabel(rarity_frame, text="Rarity:",
                    font=ctk.CTkFont(size=11), text_color="gray50").pack(side="left")
        ctk.CTkLabel(rarity_frame, text=f" {self.marker['rarity_label']}",
                    font=ctk.CTkFont(size=11, weight="bold"),
                    text_color="#eab308" if self.marker['rarity'] < 0.10 else "gray60").pack(side="left")

        copies = self.marker.get('copies', 1)
        copies_text = " (2 copies - full effect)" if copies == 2 else " (1 copy - partial/carrier)"
        ctk.CTkLabel(rarity_frame, text=copies_text,
                    font=ctk.CTkFont(size=11), text_color="gray50").pack(side="left")

    def _get_plain_english_meaning(self) -> str:
        """Generate easy to understand explanation"""
        gene = self.marker['gene']
        origin = self.marker['origin']
        category = self.marker.get('category', '')
        effect = self.marker.get('effect', '').lower()

        meanings = {
            # Immune genes
            'TLR1': "Your immune system can detect certain bacteria better than average. You may get sick less often from bacterial infections.",
            'TLR2': "You have enhanced defense against tuberculosis and similar bacteria.",
            'TLR3': "Your body is better at detecting and fighting RNA viruses like the flu.",
            'TLR6': "You have improved ability to fight Gram-positive bacteria.",
            'TLR10': "Your inflammatory response is modified - this can affect how you respond to infections.",
            'STAT2': "Your antiviral response is stronger than average.",
            'OAS1': "You have enhanced protection against RNA viruses, including better COVID-19 outcomes.",

            # Skin/Hair genes
            'MC1R': "You carry a gene variant associated with red/auburn hair and fair skin. This was common in Neanderthals.",
            'BNC2': "You have a gene variant that affects freckling and can make skin lighter.",
            'TYR': "This affects your melanin production - influences skin and eye color.",
            'SLC45A2': "You carry a light skin adaptation that became common in Europeans.",
            'IRF4': "You're more likely to develop freckles and may be more sensitive to sun.",
            'KITLG': "You carry a variant associated with lighter/blonde hair color.",
            'ASIP': "This affects your hair color - specifically darker pigmentation.",

            # Brain genes
            'FOXP2': "This gene is involved in speech and language development. The Neanderthal variant may have contributed to human language evolution.",
            'COMT': "You have the 'warrior gene' variant - slower dopamine breakdown means you may handle stress differently and have better memory under pressure.",
            'BDNF': "This affects brain plasticity - how your brain forms new connections and learns.",
            'OXTR': "This affects your oxytocin receptor - may influence social bonding and empathy.",
            'DRD2': "This affects dopamine receptors in your brain - can influence reward-seeking behavior.",
            'ANKK1/DRD2': "You have reduced dopamine D2 receptors - may affect motivation and reward sensitivity.",

            # Metabolism
            'PPARA': "You process high-fat foods better than average - a useful adaptation from when meat was a dietary staple.",
            'SLC16A11': "This Neanderthal gene increases type 2 diabetes risk slightly. Watch your sugar intake.",
            'MTHFR': "You may need more folate/B vitamins. Consider methylfolate supplements.",
            'APOE': "This affects how you process cholesterol and fats.",
            'FADS1': "You're better at converting plant omega-3s to the forms your body needs.",
            'CLOCK': "This affects your circadian rhythm - you may be adapted to longer winter nights.",

            # Athletic
            'ACTN3': "This determines your muscle fiber type - affects whether you're better at sprinting/power or endurance.",
            'ACE': "This affects your cardiovascular performance and endurance capacity.",
            'CYP1A2': "This determines how fast you metabolize caffeine - affects optimal timing for coffee.",

            # Altitude (Denisovan)
            'EPAS1': "This is the famous Tibetan altitude gene from Denisovans! You may handle high altitudes better.",
            'EGLN1': "You have enhanced oxygen sensing - helps at high altitudes.",
            'VEGFA': "Your body may be better at forming blood vessels for oxygen delivery.",

            # Pain
            'SCN9A': "This affects your pain perception - you may feel pain more or less intensely than average.",
            'OPRM1': "This affects your opioid receptors - influences pain response and may affect how pain medications work for you.",

            # Blood clotting
            'F5': "You have faster blood clotting - helped ancestors survive wounds but increases clot risk today.",
            'F2': "Your blood clots faster than average.",
            'ABO': "This affects your blood type - Type O provides some malaria resistance.",

            # Sleep
            'ADRB1': "You may be a natural short sleeper - able to function well on less sleep.",
            'PER3': "This affects your chronotype - whether you're a morning person or night owl.",

            # Body structure
            'SLC39A8': "This affects your height and body composition.",
            'HMGA2': "This is one of the genes that determines your height.",

            # Supplements
            'GC': "This affects your vitamin D levels - you may need more supplementation.",
            'FUT2': "This affects B12 absorption - you may benefit from B12 supplements.",
        }

        # Check for matches
        if gene in meanings:
            return meanings[gene]

        # Generic fallbacks based on category
        if 'immune' in category.lower():
            return "This gene affects how your immune system fights infections."
        elif 'skin' in category.lower() or 'hair' in category.lower():
            return "This gene influences your physical appearance - skin, hair, or eye characteristics."
        elif 'metabolism' in category.lower():
            return "This gene affects how your body processes food and nutrients."
        elif 'brain' in category.lower():
            return "This gene influences brain function and behavior."
        elif origin == 'Neanderthal':
            return "This is a functional gene you inherited from Neanderthal ancestors through interbreeding ~50,000 years ago."
        elif origin == 'Denisovan':
            return "This is a functional gene from Denisovan ancestors - an ancient human species that lived in Asia."

        return ""

    def hide_tooltip(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None


# =============================================================================
# GENETIC SUPERPOWERS FRAME
# =============================================================================

class SuperpowersFrame(ctk.CTkFrame):
    """Notable genetic variants display"""

    def __init__(self, parent, results: Dict[str, Any]):
        super().__init__(parent, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        superpowers = results.get('superpowers', {})

        # Header
        ctk.CTkLabel(
            self, text="Notable Genetic Variants",
            font=ctk.CTkFont(size=32, weight="bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 5))

        # Disclaimer
        ctk.CTkLabel(
            self, text="Rare genetic variants that confer unusual traits or abilities",
            font=ctk.CTkFont(size=11), text_color="gray50"
        ).grid(row=1, column=0, sticky="w", pady=(0, 5))

        # Info note
        info_frame = ctk.CTkFrame(self, fg_color="#1e3a5f", corner_radius=8)
        info_frame.grid(row=2, column=0, sticky="ew", pady=(0, 15))
        ctk.CTkLabel(
            info_frame,
            text="Note: These variants are genuinely rare in the population. Having few or no notable variants is normal - most people don't carry these rare mutations. 'NOTABLE' = you have both copies, 'CARRIER' = you have one copy.",
            font=ctk.CTkFont(size=11), text_color="#93c5fd",
            wraplength=700, justify="left"
        ).pack(padx=15, pady=8)

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=3, column=0, sticky="nsew")
        scroll.grid_columnconfigure(0, weight=1)

        full_powers = superpowers.get('superpowers_found', [])
        partial_powers = superpowers.get('partial_superpowers', [])

        # Stats bar
        stats = ctk.CTkFrame(scroll, fg_color="#1a1a2e", corner_radius=15, height=100)
        stats.pack(fill="x", pady=(0, 20))
        stats.pack_propagate(False)

        stats_inner = ctk.CTkFrame(stats, fg_color="transparent")
        stats_inner.place(relx=0.5, rely=0.5, anchor="center")

        for val, label, color in [
            (len(full_powers), "NOTABLE", "#22c55e"),
            (len(partial_powers), "CARRIER", "#eab308"),
            (superpowers.get('rarity_score', 0), "SCORE", "#a855f7")
        ]:
            box = ctk.CTkFrame(stats_inner, fg_color="transparent", width=120)
            box.pack(side="left", padx=30)
            ctk.CTkLabel(box, text=str(val), font=ctk.CTkFont(size=42, weight="bold"), text_color=color).pack()
            ctk.CTkLabel(box, text=label, font=ctk.CTkFont(size=11), text_color="gray50").pack()

        # Full variants found
        if full_powers:
            for power in full_powers:
                freq = power.get('population_frequency', 0)
                # Better frequency display for rare variants
                if freq < 0.0001:
                    freq_pct = f"< 0.01% of population (extremely rare)"
                elif freq < 0.001:
                    freq_pct = f"~{freq*100:.2f}% of population (very rare)"
                elif freq < 0.01:
                    freq_pct = f"~{freq*100:.1f}% of population (rare)"
                else:
                    freq_pct = f"{freq*100:.0f}% of population"

                card = ctk.CTkFrame(scroll, fg_color="#14532d", corner_radius=12, height=110)
                card.pack(fill="x", pady=5)
                card.pack_propagate(False)

                inner = ctk.CTkFrame(card, fg_color="transparent")
                inner.pack(fill="both", expand=True, padx=20, pady=15)

                ctk.CTkLabel(
                    inner, text=power['name'],
                    font=ctk.CTkFont(size=20, weight="bold"), text_color="#4ade80"
                ).pack(anchor="w")

                ctk.CTkLabel(
                    inner, text=f"{power['gene']} - {power['description'][:70]}",
                    font=ctk.CTkFont(size=12), text_color="#86efac"
                ).pack(anchor="w")

                ctk.CTkLabel(
                    inner, text=f"Population frequency: {freq_pct}",
                    font=ctk.CTkFont(size=10), text_color="gray50"
                ).pack(anchor="w")

        # Partial (carrier status)
        if partial_powers:
            ctk.CTkLabel(scroll, text="CARRIER STATUS", font=ctk.CTkFont(size=14, weight="bold"),
                        text_color="gray50").pack(anchor="w", pady=(20, 10))

            for power in partial_powers:
                row = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=8, height=50)
                row.pack(fill="x", pady=3)
                row.pack_propagate(False)

                ctk.CTkLabel(
                    row, text=f"{power['name']} ({power['gene']})",
                    font=ctk.CTkFont(size=14), text_color="#eab308"
                ).pack(side="left", padx=15, pady=12)

        if not full_powers and not partial_powers:
            ctk.CTkLabel(scroll, text="No notable variants detected in analyzed markers",
                        font=ctk.CTkFont(size=16), text_color="gray50").pack(pady=50)


# =============================================================================
# SURVIVAL SCENARIOS FRAME
# =============================================================================

class SurvivalScenariosFrame(ctk.CTkFrame):
    """Survival simulator - for entertainment only"""

    def __init__(self, parent, results: Dict[str, Any]):
        super().__init__(parent, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        survival = results.get('survival_scenarios', {})

        ctk.CTkLabel(
            self, text="Survival Simulator",
            font=ctk.CTkFont(size=32, weight="bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 5))

        # Entertainment disclaimer
        ctk.CTkLabel(
            self, text="FOR ENTERTAINMENT ONLY - Not scientifically validated predictions",
            font=ctk.CTkFont(size=11), text_color="#f59e0b"
        ).grid(row=1, column=0, sticky="w", pady=(0, 15))

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=2, column=0, sticky="nsew")
        scroll.grid_columnconfigure((0, 1), weight=1)

        scenarios = survival.get('scenarios', [])

        for i, scenario in enumerate(scenarios):
            score = scenario['survival_score']

            # Color based on score
            if score >= 70:
                bg, fg = "#14532d", "#22c55e"
            elif score >= 50:
                bg, fg = "#713f12", "#eab308"
            else:
                bg, fg = "#7f1d1d", "#ef4444"

            card = ctk.CTkFrame(scroll, fg_color=bg, corner_radius=15, height=140)
            card.grid(row=i//2, column=i%2, sticky="nsew", padx=8, pady=8)
            card.grid_propagate(False)

            inner = ctk.CTkFrame(card, fg_color="transparent")
            inner.place(relx=0.5, rely=0.5, anchor="center")

            ctk.CTkLabel(inner, text=scenario['name'],
                        font=ctk.CTkFont(size=16, weight="bold")).pack()
            ctk.CTkLabel(inner, text=str(score),
                        font=ctk.CTkFont(size=48, weight="bold"), text_color=fg).pack()
            ctk.CTkLabel(inner, text=scenario['rating'],
                        font=ctk.CTkFont(size=12), text_color="gray60").pack()


# =============================================================================
# HISTORICAL MATCH FRAME
# =============================================================================

class HistoricalMatchFrame(ctk.CTkFrame):
    """Historical DNA matching - for entertainment only"""

    def __init__(self, parent, results: Dict[str, Any]):
        super().__init__(parent, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        historical = results.get('historical_matches', {})

        ctk.CTkLabel(
            self, text="Historical DNA Matches",
            font=ctk.CTkFont(size=32, weight="bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 5))

        # Entertainment disclaimer
        ctk.CTkLabel(
            self, text="FOR ENTERTAINMENT - Based on limited markers, not proof of relation",
            font=ctk.CTkFont(size=11), text_color="#f59e0b"
        ).grid(row=1, column=0, sticky="w", pady=(0, 15))

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=2, column=0, sticky="nsew")

        matches = historical.get('matches', [])
        closest = historical.get('closest_match')

        # Highlight closest match
        if closest and closest.get('similarity_score', 0) > 25:
            hero = ctk.CTkFrame(scroll, fg_color="#1e3a5f", corner_radius=20, height=150)
            hero.pack(fill="x", pady=(0, 20))
            hero.pack_propagate(False)

            inner = ctk.CTkFrame(hero, fg_color="transparent")
            inner.place(relx=0.5, rely=0.5, anchor="center")

            ctk.CTkLabel(inner, text="CLOSEST MATCH", font=ctk.CTkFont(size=11), text_color="gray50").pack()
            ctk.CTkLabel(inner, text=closest['name'],
                        font=ctk.CTkFont(size=28, weight="bold"), text_color="#60a5fa").pack()
            ctk.CTkLabel(inner, text=f"{closest['era']} - {closest['location']}",
                        font=ctk.CTkFont(size=13), text_color="gray60").pack()
            ctk.CTkLabel(inner, text=f"{closest['similarity_score']:.0f}% Match",
                        font=ctk.CTkFont(size=18, weight="bold"), text_color="#22c55e").pack(pady=(5,0))

        # Other matches
        for match in matches[:8]:
            if match['similarity_score'] < 20:
                continue

            score = match['similarity_score']
            color = "#22c55e" if score >= 50 else "#eab308" if score >= 35 else "gray50"

            row = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10, height=60)
            row.pack(fill="x", pady=4)
            row.pack_propagate(False)

            left = ctk.CTkFrame(row, fg_color="transparent")
            left.pack(side="left", fill="y", padx=15)

            ctk.CTkLabel(left, text=match['name'],
                        font=ctk.CTkFont(size=15, weight="bold")).pack(anchor="w", pady=(12, 0))
            ctk.CTkLabel(left, text=f"{match['era']}",
                        font=ctk.CTkFont(size=11), text_color="gray50").pack(anchor="w")

            ctk.CTkLabel(row, text=f"{score:.0f}%",
                        font=ctk.CTkFont(size=20, weight="bold"), text_color=color
                        ).pack(side="right", padx=20)


# =============================================================================
# DNA TIME MACHINE FRAME
# =============================================================================

class TimeMachineFrame(ctk.CTkFrame):
    """Clean time machine display"""

    def __init__(self, parent, results: Dict[str, Any]):
        super().__init__(parent, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        tm = results.get('time_machine', {})

        ctk.CTkLabel(
            self, text="DNA Time Machine",
            font=ctk.CTkFont(size=32, weight="bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 20))

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        # Maternal journey
        maternal = tm.get('maternal_journey', [])
        if maternal:
            ctk.CTkLabel(scroll, text="MATERNAL LINE (mtDNA)",
                        font=ctk.CTkFont(size=14, weight="bold"), text_color="#ec4899"
                        ).pack(anchor="w", pady=(0, 10))

            for step in maternal[:5]:
                row = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=8, height=70)
                row.pack(fill="x", pady=3)
                row.pack_propagate(False)

                left = ctk.CTkFrame(row, fg_color="transparent")
                left.pack(side="left", padx=15, pady=10)

                ctk.CTkLabel(left, text=f"Haplogroup {step['haplogroup']}",
                            font=ctk.CTkFont(size=16, weight="bold"), text_color="#ec4899").pack(anchor="w")
                ctk.CTkLabel(left, text=f"{step['origin']} - {step['age_formatted']}",
                            font=ctk.CTkFont(size=11), text_color="gray50").pack(anchor="w")

        # Paternal journey
        paternal = tm.get('paternal_journey', [])
        if paternal:
            ctk.CTkLabel(scroll, text="PATERNAL LINE (Y-DNA)",
                        font=ctk.CTkFont(size=14, weight="bold"), text_color="#3b82f6"
                        ).pack(anchor="w", pady=(20, 10))

            for step in paternal[:5]:
                row = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=8, height=70)
                row.pack(fill="x", pady=3)
                row.pack_propagate(False)

                left = ctk.CTkFrame(row, fg_color="transparent")
                left.pack(side="left", padx=15, pady=10)

                ctk.CTkLabel(left, text=f"Haplogroup {step['haplogroup']}",
                            font=ctk.CTkFont(size=16, weight="bold"), text_color="#3b82f6").pack(anchor="w")
                ctk.CTkLabel(left, text=f"{step['origin']} - {step['age_formatted']}",
                            font=ctk.CTkFont(size=11), text_color="gray50").pack(anchor="w")


# =============================================================================
# EPIGENETIC AGE FRAME
# =============================================================================

class EpigeneticAgeFrame(ctk.CTkFrame):
    """Biological age display with clear explanations"""

    def __init__(self, parent, results: Dict[str, Any]):
        super().__init__(parent, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        epi = results.get('epigenetic_age', {})

        ctk.CTkLabel(
            self, text="Biological Age",
            font=ctk.CTkFont(size=32, weight="bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 20))

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        bio_age = epi.get('biological_age', 30)
        chrono_age = epi.get('chronological_age', 30)
        diff = epi.get('age_difference', 0)
        score = epi.get('longevity_score', 50)

        # Determine color
        if diff < -2:
            color, msg = "#22c55e", "YOUNGER"
        elif diff > 2:
            color, msg = "#ef4444", "OLDER"
        else:
            color, msg = "#eab308", "ON TRACK"

        # Big age display
        hero = ctk.CTkFrame(scroll, fg_color="#1a1a2e", corner_radius=20, height=250)
        hero.pack(fill="x", pady=(0, 20))
        hero.pack_propagate(False)

        inner = ctk.CTkFrame(hero, fg_color="transparent")
        inner.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(inner, text="BIOLOGICAL AGE", font=ctk.CTkFont(size=12), text_color="gray50").pack()
        ctk.CTkLabel(inner, text=f"{bio_age:.0f}",
                    font=ctk.CTkFont(size=96, weight="bold"), text_color=color).pack()

        if abs(diff) > 0.5:
            diff_text = f"{abs(diff):.1f} years {msg.lower()}"
            ctk.CTkLabel(inner, text=diff_text, font=ctk.CTkFont(size=16, weight="bold"), text_color=color).pack()

        ctk.CTkLabel(inner, text=f"Reference age: {chrono_age}",
                    font=ctk.CTkFont(size=13), text_color="gray50").pack(pady=(10,0))

        # EXPLANATION BOX - What do these numbers mean?
        explain = ctk.CTkFrame(scroll, fg_color="#1e3a5f", corner_radius=12)
        explain.pack(fill="x", pady=(0, 15))

        explain_inner = ctk.CTkFrame(explain, fg_color="transparent")
        explain_inner.pack(fill="both", expand=True, padx=20, pady=15)

        ctk.CTkLabel(explain_inner, text="What Do These Numbers Mean?",
                    font=ctk.CTkFont(size=14, weight="bold"), text_color="#93c5fd").pack(anchor="w")

        explanations = [
            f"Biological Age ({bio_age:.0f}): Your body's estimated cellular age based on longevity gene variants you carry. Lower = genetically younger cells.",
            f"Reference Age ({chrono_age}): A baseline age used for comparison (default 30). The calculation shows how your genetics compare to an average 30-year-old.",
            f"'{abs(diff):.1f} years {msg.lower()}': Your genetics suggest your cells may age {msg.lower()} than typical. This is genetic potential, not actual measured age.",
            "This does NOT guess your real age - it measures genetic variants associated with slower/faster cellular aging."
        ]
        for exp in explanations:
            ctk.CTkLabel(explain_inner, text=f"• {exp}",
                        font=ctk.CTkFont(size=11), text_color="#bfdbfe",
                        wraplength=550, justify="left").pack(anchor="w", pady=3)

        # Longevity score bar
        bar_frame = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=12, height=100)
        bar_frame.pack(fill="x", pady=(0, 15))
        bar_frame.pack_propagate(False)

        bar_inner = ctk.CTkFrame(bar_frame, fg_color="transparent")
        bar_inner.pack(fill="both", expand=True, padx=20, pady=15)

        ctk.CTkLabel(bar_inner, text=f"Longevity Score: {score}/100",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w")
        ctk.CTkLabel(bar_inner, text="Higher = more protective longevity gene variants",
                    font=ctk.CTkFont(size=11), text_color="gray50").pack(anchor="w")

        bar = ctk.CTkProgressBar(bar_inner, height=20, corner_radius=10)
        bar.pack(fill="x", pady=(8, 0))
        bar.set(score / 100)

        # Positive/negative factors
        pos = epi.get('positive_factors', [])
        neg = epi.get('negative_factors', [])

        if pos:
            pos_frame = ctk.CTkFrame(scroll, fg_color="#14532d", corner_radius=12)
            pos_frame.pack(fill="x", pady=(0, 10))
            pos_inner = ctk.CTkFrame(pos_frame, fg_color="transparent")
            pos_inner.pack(fill="both", padx=20, pady=15)
            ctk.CTkLabel(pos_inner, text="Your Protective Longevity Variants",
                        font=ctk.CTkFont(size=14, weight="bold"), text_color="#22c55e").pack(anchor="w")
            ctk.CTkLabel(pos_inner, text="Gene variants that may slow aging:",
                        font=ctk.CTkFont(size=11), text_color="#86efac").pack(anchor="w")
            for factor in pos[:5]:
                ctk.CTkLabel(pos_inner, text=f"  + {factor}",
                            font=ctk.CTkFont(size=12), text_color="#86efac").pack(anchor="w")

        if neg:
            neg_frame = ctk.CTkFrame(scroll, fg_color="#7f1d1d", corner_radius=12)
            neg_frame.pack(fill="x", pady=(0, 10))
            neg_inner = ctk.CTkFrame(neg_frame, fg_color="transparent")
            neg_inner.pack(fill="both", padx=20, pady=15)
            ctk.CTkLabel(neg_inner, text="Aging Risk Variants",
                        font=ctk.CTkFont(size=14, weight="bold"), text_color="#ef4444").pack(anchor="w")
            ctk.CTkLabel(neg_inner, text="Gene variants associated with faster aging:",
                        font=ctk.CTkFont(size=11), text_color="#fca5a5").pack(anchor="w")
            for factor in neg[:5]:
                ctk.CTkLabel(neg_inner, text=f"  - {factor}",
                            font=ctk.CTkFont(size=12), text_color="#fca5a5").pack(anchor="w")


# =============================================================================
# ARCHAIC DNA FRAME - Your Neanderthal & Denisovan Genes
# =============================================================================

class ArchaicDNAFrame(ctk.CTkFrame):
    """Display inherited archaic genes with functional effects"""

    def __init__(self, parent, results: Dict[str, Any]):
        super().__init__(parent, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        archaic = results.get('archaic_dna', {})
        neanderthal = archaic.get('neanderthal', {})
        denisovan = archaic.get('denisovan', {})
        findings = archaic.get('interesting_findings', [])

        ctk.CTkLabel(
            self, text="Your Ancient DNA",
            font=ctk.CTkFont(size=32, weight="bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 20))

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")
        scroll.grid_columnconfigure((0, 1), weight=1)

        # Get both marker match rate and estimated ancestry
        nean_ancestry = neanderthal.get('percentage_estimate', 0)
        nean_match = neanderthal.get('marker_match_rate', 0)
        nean_found = neanderthal.get('markers_found', 0)
        nean_total = neanderthal.get('total_markers', 0)
        nean_genes = len(neanderthal.get('functional_genes', []))

        denis_ancestry = denisovan.get('percentage_estimate', 0)
        denis_match = denisovan.get('marker_match_rate', 0)
        denis_found = denisovan.get('markers_found', 0)
        denis_total = denisovan.get('total_markers', 0)
        denis_genes = len(denisovan.get('functional_genes', []))

        # Explanation box
        info_frame = ctk.CTkFrame(scroll, fg_color="#1e3a5f", corner_radius=8)
        info_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=8, pady=(0, 10))
        ctk.CTkLabel(
            info_frame,
            text="The large % shows estimated genome ancestry (based on scientific research: 1-4% Neanderthal, 0-1% Denisovan for most non-Africans). The smaller text shows how many archaic markers you carry from our database.",
            font=ctk.CTkFont(size=11), text_color="#93c5fd",
            wraplength=700, justify="left"
        ).pack(padx=15, pady=8)

        # Neanderthal card
        nean_card = ctk.CTkFrame(scroll, fg_color="#4a1d1d", corner_radius=15, height=160)
        nean_card.grid(row=1, column=0, sticky="nsew", padx=8, pady=8)
        nean_card.grid_propagate(False)

        nean_inner = ctk.CTkFrame(nean_card, fg_color="transparent")
        nean_inner.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(nean_inner, text="NEANDERTHAL", font=ctk.CTkFont(size=11), text_color="gray50").pack()
        ctk.CTkLabel(nean_inner, text=f"~{nean_ancestry}%",
                    font=ctk.CTkFont(size=42, weight="bold"), text_color="#ef4444").pack()
        ctk.CTkLabel(nean_inner, text="of your genome",
                    font=ctk.CTkFont(size=11), text_color="gray50").pack()
        ctk.CTkLabel(nean_inner, text=f"{nean_found}/{nean_total} markers ({nean_match:.0f}%)",
                    font=ctk.CTkFont(size=12), text_color="#fca5a5").pack(pady=(5,0))

        # Denisovan card
        denis_card = ctk.CTkFrame(scroll, fg_color="#1e3a5f", corner_radius=15, height=160)
        denis_card.grid(row=1, column=1, sticky="nsew", padx=8, pady=8)
        denis_card.grid_propagate(False)

        denis_inner = ctk.CTkFrame(denis_card, fg_color="transparent")
        denis_inner.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(denis_inner, text="DENISOVAN", font=ctk.CTkFont(size=11), text_color="gray50").pack()
        ctk.CTkLabel(denis_inner, text=f"~{denis_ancestry}%",
                    font=ctk.CTkFont(size=42, weight="bold"), text_color="#3b82f6").pack()
        ctk.CTkLabel(denis_inner, text="of your genome",
                    font=ctk.CTkFont(size=11), text_color="gray50").pack()
        ctk.CTkLabel(denis_inner, text=f"{denis_found}/{denis_total} markers ({denis_match:.0f}%)",
                    font=ctk.CTkFont(size=12), text_color="#93c5fd").pack(pady=(5,0))

        # Interesting findings (rare genes)
        if findings:
            findings_card = ctk.CTkFrame(scroll, fg_color="#14532d", corner_radius=12)
            findings_card.grid(row=2, column=0, columnspan=2, sticky="ew", padx=8, pady=(15, 8))

            ctk.CTkLabel(findings_card, text="RARE FINDINGS",
                        font=ctk.CTkFont(size=12, weight="bold"), text_color="#22c55e"
                        ).pack(anchor="w", padx=15, pady=(12, 5))

            for finding in findings[:5]:
                ctk.CTkLabel(findings_card, text=f"★ {finding['finding']}",
                            font=ctk.CTkFont(size=12), text_color="#86efac",
                            wraplength=550, justify="left").pack(anchor="w", padx=15, pady=3)

            ctk.CTkFrame(findings_card, height=10, fg_color="transparent").pack()

        # Neanderthal genes by category
        nean_by_cat = neanderthal.get('by_category', {})
        if nean_by_cat:
            cat_label = ctk.CTkFrame(scroll, fg_color="transparent")
            cat_label.grid(row=3, column=0, columnspan=2, sticky="w", padx=8, pady=(20, 5))
            ctk.CTkLabel(cat_label, text="YOUR NEANDERTHAL GENES",
                        font=ctk.CTkFont(size=14, weight="bold"), text_color="#ef4444").pack(anchor="w")

            row_idx = 4
            for category, genes in nean_by_cat.items():
                cat_name = category.replace('_', ' ').title()

                card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
                card.grid(row=row_idx, column=0, columnspan=2, sticky="ew", padx=8, pady=4)
                row_idx += 1

                # Category header
                header = ctk.CTkFrame(card, fg_color="transparent")
                header.pack(fill="x", padx=15, pady=(10, 5))

                ctk.CTkLabel(header, text=cat_name,
                            font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
                ctk.CTkLabel(header, text=f"{len(genes)} genes",
                            font=ctk.CTkFont(size=11), text_color="gray50").pack(side="right")

                # Gene list
                for gene in genes[:4]:  # Show up to 4 per category
                    gene_row = ctk.CTkFrame(card, fg_color="transparent")
                    gene_row.pack(fill="x", padx=15, pady=2)

                    copies_text = "●●" if gene['copies'] == 2 else "●○"
                    copies_color = "#22c55e" if gene['copies'] == 2 else "#eab308"

                    ctk.CTkLabel(gene_row, text=copies_text,
                                font=ctk.CTkFont(size=12), text_color=copies_color, width=30).pack(side="left")
                    ctk.CTkLabel(gene_row, text=gene['gene'],
                                font=ctk.CTkFont(size=12, weight="bold"), width=80).pack(side="left")
                    ctk.CTkLabel(gene_row, text=gene['effect'],
                                font=ctk.CTkFont(size=11), text_color="gray60").pack(side="left", padx=(10, 0))

                ctk.CTkFrame(card, height=8, fg_color="transparent").pack()

        # Denisovan genes
        denis_genes_list = denisovan.get('functional_genes', [])
        if denis_genes_list:
            denis_label = ctk.CTkFrame(scroll, fg_color="transparent")
            denis_label.grid(row=row_idx if nean_by_cat else 2, column=0, columnspan=2, sticky="w", padx=8, pady=(20, 5))
            ctk.CTkLabel(denis_label, text="YOUR DENISOVAN GENES",
                        font=ctk.CTkFont(size=14, weight="bold"), text_color="#3b82f6").pack(anchor="w")

            row_idx = (row_idx + 1) if nean_by_cat else 3

            card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            card.grid(row=row_idx, column=0, columnspan=2, sticky="ew", padx=8, pady=4)

            for gene in denis_genes_list[:6]:
                gene_row = ctk.CTkFrame(card, fg_color="transparent")
                gene_row.pack(fill="x", padx=15, pady=4)

                copies_text = "●●" if gene['copies'] == 2 else "●○"
                copies_color = "#22c55e" if gene['copies'] == 2 else "#eab308"

                ctk.CTkLabel(gene_row, text=copies_text,
                            font=ctk.CTkFont(size=12), text_color=copies_color, width=30).pack(side="left")
                ctk.CTkLabel(gene_row, text=gene['gene'],
                            font=ctk.CTkFont(size=12, weight="bold"), width=80).pack(side="left")
                ctk.CTkLabel(gene_row, text=gene['effect'],
                            font=ctk.CTkFont(size=11), text_color="gray60").pack(side="left", padx=(10, 0))

            ctk.CTkFrame(card, height=8, fg_color="transparent").pack()


# =============================================================================
# DIET & TRAINING FRAME
# =============================================================================

class DietTrainingFrame(ctk.CTkFrame):
    """Clean diet and training display"""

    def __init__(self, parent, results: Dict[str, Any]):
        super().__init__(parent, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        dt = results.get('diet_training', {})

        ctk.CTkLabel(
            self, text="Your Optimal Plan",
            font=ctk.CTkFont(size=32, weight="bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 20))

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        training = dt.get('training_recommendations', {})
        diet = dt.get('diet_recommendations', {})
        caffeine = dt.get('caffeine_protocol', {})
        supplements = dt.get('supplement_stack', [])

        # Training style hero
        style = training.get('optimal_style', 'Balanced training')
        hero = ctk.CTkFrame(scroll, fg_color="#1e3a5f", corner_radius=15, height=100)
        hero.pack(fill="x", pady=(0, 15))
        hero.pack_propagate(False)

        inner = ctk.CTkFrame(hero, fg_color="transparent")
        inner.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(inner, text="OPTIMAL TRAINING", font=ctk.CTkFont(size=11), text_color="gray50").pack()
        ctk.CTkLabel(inner, text=style, font=ctk.CTkFont(size=24, weight="bold"), text_color="#60a5fa").pack()

        # Weekly structure
        weekly = training.get('weekly_structure', [])
        if weekly:
            card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=12)
            card.pack(fill="x", pady=8)

            ctk.CTkLabel(card, text="Weekly Structure",
                        font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=15, pady=(12, 8))

            for day in weekly[:7]:
                ctk.CTkLabel(card, text=day, font=ctk.CTkFont(size=12),
                            text_color="gray60").pack(anchor="w", padx=15, pady=1)

            ctk.CTkFrame(card, height=12, fg_color="transparent").pack()

        # Caffeine
        if caffeine:
            card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=12, height=70)
            card.pack(fill="x", pady=8)
            card.pack_propagate(False)

            ctk.CTkLabel(card, text=f"Caffeine: {caffeine.get('metabolism', 'Normal')} metabolizer",
                        font=ctk.CTkFont(size=14, weight="bold"), text_color="#f97316"
                        ).pack(anchor="w", padx=15, pady=(15, 3))
            ctk.CTkLabel(card, text=caffeine.get('timing', ''),
                        font=ctk.CTkFont(size=12), text_color="gray50").pack(anchor="w", padx=15)

        # Supplements
        if supplements:
            card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=12)
            card.pack(fill="x", pady=8)

            ctk.CTkLabel(card, text="Recommended Supplements",
                        font=ctk.CTkFont(size=14, weight="bold"), text_color="#22c55e"
                        ).pack(anchor="w", padx=15, pady=(12, 8))

            for supp in supplements[:5]:
                ctk.CTkLabel(card, text=f"  {supp['supplement']} - {supp.get('dose', '')}",
                            font=ctk.CTkFont(size=12), text_color="gray60").pack(anchor="w", padx=15, pady=1)

            ctk.CTkFrame(card, height=12, fg_color="transparent").pack()


# =============================================================================
# ANCESTRY STORY FRAME
# =============================================================================

class AncestryStoryFrame(ctk.CTkFrame):
    """Clean ancestry story display"""

    def __init__(self, parent, results: Dict[str, Any]):
        super().__init__(parent, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        story = results.get('ancestry_story', {})
        sections = story.get('story_sections', [])

        ctk.CTkLabel(
            self, text="Your Ancestry Story",
            font=ctk.CTkFont(size=32, weight="bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 20))

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        if not sections:
            ctk.CTkLabel(scroll, text="Load DNA to generate your story",
                        font=ctk.CTkFont(size=16), text_color="gray50").pack(pady=50)
            return

        for section in sections[:4]:
            card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=15)
            card.pack(fill="x", pady=10)

            inner = ctk.CTkFrame(card, fg_color="transparent")
            inner.pack(fill="x", padx=20, pady=20)

            ctk.CTkLabel(inner, text=section['title'],
                        font=ctk.CTkFont(size=20, weight="bold"), text_color="#60a5fa").pack(anchor="w")
            ctk.CTkLabel(inner, text=section['era'],
                        font=ctk.CTkFont(size=11), text_color="gray50").pack(anchor="w", pady=(0, 10))

            # Truncate narrative
            narrative = section['narrative']
            if len(narrative) > 200:
                narrative = narrative[:200] + "..."

            ctk.CTkLabel(inner, text=narrative,
                        font=ctk.CTkFont(size=13), wraplength=600, justify="left").pack(anchor="w")


# =============================================================================
# ALL MARKERS FRAME - Complete genetic profile sorted by rarity
# =============================================================================

class AllMarkersFrame(ctk.CTkFrame):
    """Display all genetic markers sorted by rarity"""

    def __init__(self, parent, results: Dict[str, Any]):
        super().__init__(parent, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        all_data = results.get('all_markers', {})
        markers = all_data.get('markers', [])
        stats = all_data.get('stats', {})

        ctk.CTkLabel(
            self, text="All Your Markers",
            font=ctk.CTkFont(size=32, weight="bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 20))

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=1, column=0, sticky="nsew")

        # Info note explaining what markers are shown
        info_frame = ctk.CTkFrame(scroll, fg_color="#1e3a5f", corner_radius=8)
        info_frame.pack(fill="x", pady=(0, 15))
        scanned = stats.get('markers_scanned', 0)
        found = stats.get('total_markers', 0)
        ctk.CTkLabel(
            info_frame,
            text=f"Scanned {scanned} markers in our database. Showing {found} where you have the notable/rare variant. Most people have common alleles for most markers.",
            font=ctk.CTkFont(size=11), text_color="#93c5fd",
            wraplength=700, justify="left"
        ).pack(padx=15, pady=8)

        # Stats bar
        stats_card = ctk.CTkFrame(scroll, fg_color="#1a1a2e", corner_radius=15, height=100)
        stats_card.pack(fill="x", pady=(0, 20))
        stats_card.pack_propagate(False)

        stats_inner = ctk.CTkFrame(stats_card, fg_color="transparent")
        stats_inner.place(relx=0.5, rely=0.5, anchor="center")

        stat_items = [
            (stats.get('total_markers', 0), "WITH VARIANTS", "#ffffff"),
            (stats.get('superpowers', 0), "NOTABLE", "#22c55e"),
            (stats.get('neanderthal', 0), "NEANDERTHAL", "#ef4444"),
            (stats.get('denisovan', 0), "DENISOVAN", "#3b82f6"),
        ]

        for val, label, color in stat_items:
            box = ctk.CTkFrame(stats_inner, fg_color="transparent", width=100)
            box.pack(side="left", padx=20)
            ctk.CTkLabel(box, text=str(val), font=ctk.CTkFont(size=32, weight="bold"), text_color=color).pack()
            ctk.CTkLabel(box, text=label, font=ctk.CTkFont(size=10), text_color="gray50").pack()

        # Rarest marker highlight
        rarest = stats.get('rarest')
        if rarest:
            rare_card = ctk.CTkFrame(scroll, fg_color="#14532d", corner_radius=12, height=80)
            rare_card.pack(fill="x", pady=(0, 15))
            rare_card.pack_propagate(False)

            rare_inner = ctk.CTkFrame(rare_card, fg_color="transparent")
            rare_inner.pack(fill="both", expand=True, padx=20, pady=12)

            ctk.CTkLabel(rare_inner, text="YOUR RAREST MARKER",
                        font=ctk.CTkFont(size=11), text_color="#22c55e").pack(anchor="w")
            ctk.CTkLabel(rare_inner, text=f"{rarest['name']} ({rarest['gene']})",
                        font=ctk.CTkFont(size=18, weight="bold"), text_color="#4ade80").pack(anchor="w")
            ctk.CTkLabel(rare_inner, text=f"{rarest['rarity_label']} • {rarest['origin']}",
                        font=ctk.CTkFont(size=12), text_color="#86efac").pack(anchor="w")

        # Section label
        ctk.CTkLabel(scroll, text="YOUR NOTABLE VARIANTS (SORTED BY RARITY - RAREST FIRST)",
                    font=ctk.CTkFont(size=12, weight="bold"), text_color="gray50"
                    ).pack(anchor="w", pady=(10, 10))

        # Marker list
        self.tooltips = []  # Keep references to prevent garbage collection

        for marker in markers:
            # Let card expand to fit content (no fixed height)
            card = ctk.CTkFrame(scroll, fg_color="gray20", corner_radius=10)
            card.pack(fill="x", pady=4)

            # Left section - rank and origin badge
            left = ctk.CTkFrame(card, fg_color="transparent", width=80)
            left.pack(side="left", padx=(15, 10), pady=12)

            rank_label = ctk.CTkLabel(left, text=f"#{marker['rank']}",
                                     font=ctk.CTkFont(size=16, weight="bold"), text_color="gray40")
            rank_label.pack(pady=(0, 2))

            # Origin badge
            origin = marker['origin']
            if origin == 'Neanderthal':
                badge_color, badge_text = "#7f1d1d", "NEAN"
            elif origin == 'Denisovan':
                badge_color, badge_text = "#1e3a5f", "DENIS"
            elif origin == 'Human (rare)':
                badge_color, badge_text = "#14532d", "RARE"
            else:
                badge_color, badge_text = "#374151", "HUMAN"

            badge = ctk.CTkLabel(left, text=badge_text, font=ctk.CTkFont(size=9, weight="bold"),
                                fg_color=badge_color, corner_radius=4, width=45, height=18)
            badge.pack()

            # Middle section - gene info
            middle = ctk.CTkFrame(card, fg_color="transparent")
            middle.pack(side="left", fill="both", expand=True, pady=12)

            # Gene name, variant name, and rsid
            name_row = ctk.CTkFrame(middle, fg_color="transparent")
            name_row.pack(fill="x", anchor="w")

            ctk.CTkLabel(name_row, text=marker['gene'],
                        font=ctk.CTkFont(size=14, weight="bold"),
                        text_color=marker['category_color']).pack(side="left")

            # Show variant name if available (e.g., K153R)
            variant_name = marker.get('variant_name', '')
            if variant_name:
                ctk.CTkLabel(name_row, text=f"  {variant_name}",
                            font=ctk.CTkFont(size=12, weight="bold"), text_color="#eab308").pack(side="left")

            ctk.CTkLabel(name_row, text=f"  ({marker['rsid']})",
                        font=ctk.CTkFont(size=11), text_color="gray50").pack(side="left")

            # Name/trait
            ctk.CTkLabel(middle, text=marker['name'],
                        font=ctk.CTkFont(size=12), text_color="gray70").pack(anchor="w")

            # Effect - show full text with wrapping
            effect = marker['effect']
            effect_label = ctk.CTkLabel(middle, text=effect,
                        font=ctk.CTkFont(size=11), text_color="gray50",
                        wraplength=400, justify="left")
            effect_label.pack(anchor="w")

            # Right section - rarity and copies
            right = ctk.CTkFrame(card, fg_color="transparent", width=120)
            right.pack(side="right", padx=15, pady=12)

            # Rarity
            ctk.CTkLabel(right, text=marker['rarity_label'],
                        font=ctk.CTkFont(size=11, weight="bold"),
                        text_color="#eab308" if marker['rarity'] < 0.10 else "gray60"
                        ).pack(pady=(0, 2), anchor="e")

            # Copies indicator
            copies = marker.get('copies', 1)
            copies_text = "●●" if copies == 2 else "●○"
            copies_color = "#22c55e" if copies == 2 else "#eab308"
            ctk.CTkLabel(right, text=copies_text,
                        font=ctk.CTkFont(size=14), text_color=copies_color).pack(anchor="e")

            # Category
            ctk.CTkLabel(right, text=marker['category'],
                        font=ctk.CTkFont(size=10), text_color="gray50").pack(anchor="e")

            # Attach tooltip to the card
            tooltip = MarkerTooltip(card, marker)
            self.tooltips.append(tooltip)

        if not markers:
            ctk.CTkLabel(scroll, text="Load DNA file to see your markers",
                        font=ctk.CTkFont(size=16), text_color="gray50").pack(pady=50)
