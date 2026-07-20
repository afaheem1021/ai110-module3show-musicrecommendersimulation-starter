# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

When doing research on how real-world recommendations work, I mostly focoused on spotify and youtube and found that those 2 platforms rely on complex hybrid recommendation systems. They primarily use collaborative filtering, and use content-based filtering for when collaborative filtering is not helpful. and because our application wont have data from millions of users using out app, we will rely on a pure content-based approach in which math will be used to accurately match the "vibe" of a song to a user's explicit requests without having all the data from users. The Song and UserProfile objects will use the math from energy of the song, the mood and the acousticness. 

Step 5: Document Your Plan - 
the recommendation engine that we are using for our application is a pure content-based approach ( unlike the hybrid ones that spotify and youtube use), meaning it connects users to music based on the actual audio profile of the tracks rather than relying on other people's listening habits because we dont have alot of user data. To rank the catalog, the system scores each song out of 10 possible points. The bulk of the score—up to 7.5 points—is calculated based on how mathematically close a song's energy, valence, and acousticness match the user's exact targets. The remaining 2.5 points act as a bonus for exact categorical matches in mood and genre. We intentionally designed the math this way so that a track with the perfect emotional "vibe" doesn't get buried just because it happens to be labeled "indie pop" instead of "pop." However, this literal, math-first approach does introduce a few limitations. Because the system is completely blind to cultural context, it might confidently pair two songs that share the exact same tempo and energy but belong to completely different fanbases. Additionally, without a mechanism to randomly throw in new or unexpected tracks, the algorithm risks trapping users in a repetitive "filter bubble" where they see the exact same mathematically safe songs every single time.




Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.


---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Top 5 recommendations:
==================================================

1. Sunrise City — Neon Echo
   (pop / happy)
   Score: 9.77 / 10
   Why:
     - energy within 0.03 of target (+2.91)
     - valence within 0.04 of target (+2.40)
     - acousticness within 0.02 of target (+1.96)
     - mood matches 'happy' (+1.5)
     - genre matches 'pop' (+1.0)

--------------------------------------------------

2. Rooftop Lights — Indigo Parade
   (indie pop / happy)
   Score: 8.41 / 10
   Why:
     - energy within 0.09 of target (+2.73)
     - valence within 0.01 of target (+2.48)
     - acousticness within 0.15 of target (+1.70)
     - mood matches 'happy' (+1.5)

--------------------------------------------------

3. Gym Hero — Max Pulse
   (pop / intense)
   Score: 7.88 / 10
   Why:
     - energy within 0.08 of target (+2.76)
     - valence within 0.03 of target (+2.42)
     - acousticness within 0.15 of target (+1.70)
     - genre matches 'pop' (+1.0)

--------------------------------------------------

4. Groove Machine — Brass Attack
   (funk / upbeat)
   Score: 7.20 / 10
   Why:
     - energy within 0.05 of target (+2.85)
     - valence within 0.06 of target (+2.35)
     - acousticness within 0.00 of target (+2.00)

--------------------------------------------------

5. Skyline Rush — DJ Meridian
   (house / euphoric)
   Score: 7.10 / 10
   Why:
     - energy within 0.03 of target (+2.91)
     - valence within 0.01 of target (+2.48)
     - acousticness within 0.14 of target (+1.72)

--------------------------------------------------
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



