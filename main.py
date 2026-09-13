"""
Typing Speed Test

Type the given passage as fast and accurately as you can. Timing starts on
your first keystroke, not when the passage appears, so you can read it
first. Tracks WPM, accuracy, and keeps a local history you can review.
"""

import time

import customtkinter as ctk

import typing_stats as stats

ctk.set_appearance_mode("dark")

BG = "#0c0d10"
PANEL = "#191a1f"
ACCENT = "#ff9d5c"

PASSAGES = [
    "The quiet ones are usually the ones who notice everything first.",
    "Good code reads like a clear explanation of the problem it solves.",
    "Momentum is easier to keep than it is to start from nothing.",
    "A small consistent habit beats a big burst of effort every time.",
    "Most bugs are not mysterious, they are just unexamined assumptions.",
]


class TypingTestApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Typing Speed Test")
        self.geometry("700x560")
        self.configure(fg_color=BG)

        self.passage = stats.random_passage(PASSAGES)
        self.start_time = None

        ctk.CTkLabel(self, text="Type this:", text_color=ACCENT).pack(anchor="w", padx=24, pady=(24, 4))
        self.passage_label = ctk.CTkLabel(
            self, text=self.passage, wraplength=620, justify="left",
            font=ctk.CTkFont(size=16),
        )
        self.passage_label.pack(anchor="w", padx=24)

        self.input_box = ctk.CTkTextbox(self, fg_color=PANEL, height=140, width=640)
        self.input_box.pack(padx=24, pady=20)
        self.input_box.bind("<KeyRelease>", self._on_key)

        self.result_var = ctk.StringVar(value="")
        ctk.CTkLabel(self, textvariable=self.result_var, text_color=ACCENT,
                     font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(0, 10))