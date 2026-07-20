"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from pathlib import Path

from recommender import load_songs, recommend_songs

# Resolve the CSV relative to this file, so the script works
# no matter which directory it is run from.
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "songs.csv"


# Stress-test profiles: three normal listeners plus two adversarial
# profiles with internally conflicting preferences.
# NOTE: danceability is not part of the scoring recipe, so "The Acoustic
# EDM" expresses its contradiction via acousticness 1.0 vs synthwave
# genre + high energy instead.
PROFILES = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.90,
        "valence": 0.85,
        "acousticness": 0.15,
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.30,
        "valence": 0.60,
        "acousticness": 0.85,
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.90,
        "valence": 0.35,
        "acousticness": 0.10,
    },
    # Adversarial: demands rave-level energy but a chill lofi identity.
    "The Paradox": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.95,
        "valence": 0.50,
        "acousticness": 0.30,
    },
    # Adversarial: fully acoustic texture but an electronic genre and
    # club-level energy.
    "The Acoustic EDM": {
        "genre": "synthwave",
        "mood": "upbeat",
        "energy": 0.95,
        "valence": 0.80,
        "acousticness": 1.00,
    },
}


def print_recommendations(recommendations: list) -> None:
    """Print ranked results: title/artist, score out of 10, bulleted reasons."""
    print(f"\nTop {len(recommendations)} recommendations:")
    print("=" * 50)

    # Each item is (song_dict, float_score, string_explanation).
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n{rank}. {song['title']} — {song['artist']}")
        print(f"   ({song['genre']} / {song['mood']})")
        print(f"   Score: {score:.2f} / 10")
        print("   Why:")
        # The explanation is a comma-joined reasons string; split it
        # back into one bullet per reason for readability.
        for reason in explanation.split(", "):
            print(f"     - {reason}")
        print("\n" + "-" * 50)


def main() -> None:
    songs = load_songs(str(DATA_PATH))

    for name, prefs in PROFILES.items():
        # Large banner so each profile's block is easy to find and
        # copy into model_card.md.
        print("\n\n" + "#" * 60)
        print(f"##  PROFILE: {name}")
        print(f"##  prefs:   {prefs}")
        print("#" * 60)

        recommendations = recommend_songs(prefs, songs, k=5)
        print_recommendations(recommendations)


if __name__ == "__main__":
    main()
