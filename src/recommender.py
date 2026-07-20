import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from the CSV into dicts, casting id to int and audio features to float."""
    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            for col in ("energy", "tempo_bpm", "valence", "danceability", "acousticness"):
                row[col] = float(row[col])
            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user_prefs on a renormalized 10-point budget; returns (score, reasons)."""
    earned = 0.0
    active_budget = 0.0
    reasons: List[str] = []

    # Numeric features: (name, max points)
    numeric_recipe = [
        ("energy", 3.0),
        ("valence", 2.5),
        ("acousticness", 2.0),
    ]
    for feature, max_points in numeric_recipe:
        if feature not in user_prefs:
            continue
        active_budget += max_points
        gap = abs(user_prefs[feature] - song[feature])
        points = max_points * (1 - gap)
        earned += points
        reasons.append(f"{feature} within {gap:.2f} of target (+{points:.2f})")

    # Categorical features: (name, bonus points)
    categorical_recipe = [
        ("mood", 1.5),
        ("genre", 1.0),
    ]
    for feature, bonus in categorical_recipe:
        if feature not in user_prefs:
            continue
        active_budget += bonus
        if song[feature] == user_prefs[feature]:
            earned += bonus
            reasons.append(f"{feature} matches '{song[feature]}' (+{bonus:.1f})")

    # Empty profile: no preferences means no basis to score.
    if active_budget == 0:
        return 0.0, ["no preferences provided"]

    # Renormalize to the 10-point scale so partial and full profiles
    # produce comparable scores.
    score = (earned / active_budget) * 10.0
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song, sort highest-first, and return the top k as (song, score, explanation) tuples."""
    # Score every song, joining its reasons into one explanation string.
    scored: List[Tuple[Dict, float, str]] = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, ", ".join(reasons)))

    # Sort by score (item index 1), highest first, and keep the top k.
    ranked = sorted(scored, key=lambda item: item[1], reverse=True)
    return ranked[:k]
