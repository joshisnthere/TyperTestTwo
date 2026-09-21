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

    correct = sum(1 for a, b in zip(passage, typed) if a == b)
    accuracy = round(100 * correct / max(1, len(passage)))

    return wpm, accuracy


def load_history():
    if os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH) as f:
            return json.load(f)
    return []


def save_result(wpm, accuracy):
    history = load_history()
    history.append({
        "when": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "wpm": wpm,
        "accuracy": accuracy,
    })
    with open(HISTORY_PATH, "w") as f:
        json.dump(history, f, indent=2)