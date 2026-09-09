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