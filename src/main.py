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


def main() -> None:
    songs = load_songs(str(DATA_PATH))

    # Starter example profile
    user_prefs = {
        "genre": "pop", 
        "mood": "happy", 
        "energy": 0.85,
        "valence": 0.80,
        "acousticness": 0.20
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

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


if __name__ == "__main__":
    main()
