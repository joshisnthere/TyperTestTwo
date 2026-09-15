"""
Scoring and local history for the typing test. History is stored as JSON
next to this file so it survives between runs without any external service.
"""

import datetime
import json
import os
import random

HISTORY_PATH = os.path.join(os.path.dirname(__file__), "history.json")


def random_passage(passages):
    return random.choice(passages)


def score(passage, typed, elapsed_seconds):
    words = max(1, len(passage.split()))
    minutes = max(elapsed_seconds / 60, 1 / 60)
    wpm = round(words / minutes)