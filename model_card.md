# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

NewFavSongFinder 1.0 

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  


this model is made to recommend songs based on a users specific vibe matching their energy mood and genre. its mostly an educational simulation to see how content based filtering actually works. it assumes your musical taste comes down to basic audio features like how acoustic or fast a track is instead of just looking at what other people listen to

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

the system uses a 10 point scale to match songs to what you want. it looks at energy valence and acousticness. the closer a songs numbers match your target numbers the more points it gets. that makes up about 7.5 of the points. the rest is a bonus if the genre and mood match exactly. we did it this way so a song with the perfect sound doesnt get buried just because it has a slightly different genre label.


---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  


the model uses a playlist of 20 songs saved in a csv file. it has a mix of genres like pop lofi and rock plus moods like chill or intense. since its just a starter dataset its super small and missing a ton of music types. it also leans way too heavy on extremes like super calm or super intense songs with almost nothing in the middle.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

the system works best when you know exactly what you want and your tastes make sense. like if you ask for high energy happy pop it finds loud upbeat tracks and drops the quiet acoustic ones. its also surprisingly good at finding songs across different genres. if you want chill lofi the math looks for low energy and high acousticness so it might actually show you a jazz track that fits the exact same mood

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

### The Mid-Energy Valley

Analysis of the catalog revealed a structural gap: only 1 of the 20 songs (Island Afternoon, energy 0.62) falls between 0.50 and 0.70 on energy, while nine songs sit at or below 0.48 and ten at or above 0.72. A listener who wants moderate-energy music — a very common real-world taste — is effectively invisible to this catalog: the scoring function must fill their top spots with songs at least 0.10–0.33 away on its most heavily weighted feature (3.0 of 10 points), and because a weighted average always pulls results toward wherever the catalog is dense, that user receives confidently ranked but poorly fitting recommendations with no signal that the problem is the data rather than their taste. The same bimodal skew appears in acousticness (only 3 of 20 songs between 0.3 and 0.7) and in valence (only 3 songs below 0.4), which means listeners who prefer sad or dark music exhaust the suitable pool after two or three recommendations. In short, the system's biases mirror the catalog's shape: it serves the calm-acoustic and bright-energetic clusters it actually contains, and quietly underserves everyone in between or outside them.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

## Evaluation: Accuracy and Surprises

### The Five Test Profiles

| Profile | Type | Key preferences | #1 result (score /10) |
|---|---|---|---|
| High-Energy Pop | Coherent | pop, happy, energy 0.90, valence 0.85 | Sunrise City (9.67) |
| Chill Lofi | Coherent | lofi, chill, energy 0.30, acousticness 0.85 | Library Rain (9.83) |
| Deep Intense Rock | Coherent | rock, intense, energy 0.90, valence 0.35 | Storm Runner (9.64) |
| The Paradox | Adversarial | lofi + chill identity, but energy 0.95 | Midnight Coding (7.44) |
| The Acoustic EDM | Adversarial | synthwave + energy 0.95, but acousticness 1.00 | Neon Cascade / Island Afternoon (tie, 6.86) |

The headline pattern is visible in the last column: coherent profiles reach a ceiling of 9.6–9.8, while contradictory profiles collapse to 6.9–7.4. The score of the #1 result turns out to be a built-in coherence meter for the user's preferences.

### Plain-Language Comparisons

**High-Energy Pop vs. Chill Lofi.** These two users share *zero* songs across their top-5 lists, drawn from the same 20-song catalog. That is the strongest simple proof the logic works: the two profiles sit at opposite ends of nearly every feature the system measures (energy 0.90 vs 0.30, acousticness 0.15 vs 0.85), so every song that scores well for one necessarily scores poorly for the other. The pop user's list is all bright, loud, produced tracks (Sunrise City, Gym Hero, Skyline Rush); the lofi user's list is all quiet, organic ones (Library Rain, Spacewalk Thoughts, Coffee Shop Stories) — and the lofi list even reaches outside the lofi genre to find ambient and jazz that *sound* right, which is exactly what a content-based system should do.

**Why "Gym Hero" appears for someone who just wanted "Happy Pop."** Gym Hero's mood label is "intense," not "happy" — yet it ranks #3 for the happy-pop user. The plain-language explanation: the system listens to the sound more than the label. Gym Hero is loud (energy 0.93 vs. the requested 0.90), bright and positive-sounding (valence 0.77 vs. 0.85), fully produced (acousticness 0.05), and is literally pop — so it earns nearly full marks on four of the five things the user asked for, and its one mismatch (mood) costs only 1.5 of 10 points. Whether that feels right depends on the listener: an intense-but-euphoric workout anthem is arguably a great pick for a happy-pop fan, and this ranking shows the system treating a label disagreement as a small penalty rather than a veto.

### Weight Sensitivity Test

As a simple robustness check, the energy weight was temporarily doubled (3.0 → 6.0) and the genre weight halved (1.0 → 0.5), with the renormalization keeping all scores on the 0–10 scale. The result split cleanly along the coherent/adversarial line: the three coherent profiles kept their #1 and #2 picks essentially unchanged, but The Paradox flipped completely — Midnight Coding (lofi) fell from #1 out of the top five, replaced by Storm Runner (rock) and Iron Descent (metal), and the Acoustic EDM tie broke in favor of the energy specialist. The lesson: for users with consistent tastes, the exact weights barely matter; for users with contradictory tastes, the weights silently decide which half of the contradiction wins. Weights were reverted to the standard recipe after the experiment.

### Detailed Analysis of the Adversarial Tie

The most revealing single result of the stress test came from the adversarial "Acoustic EDM" profile (energy 0.95, valence 0.80, acousticness 1.00, mood "upbeat," genre "synthwave"), which produced an exact first-place tie at 6.86/10 between two songs that resolve the contradiction in opposite ways. "Neon Cascade" (EDM) won by maximizing energy (+3.00 of 3.0) and matching mood (+1.5) while almost completely abandoning the acousticness target, earning just +0.06 of a possible 2.0 against a 0.97 gap. "Island Afternoon" (reggae) instead compromised moderately on every axis (+2.01 energy, +2.45 valence, +0.90 acousticness, +1.5 mood). The decomposition shows why they tie: Neon Cascade's 0.99-point energy advantage is offset exactly by Island Afternoon's combined 0.84-point acousticness and 0.15-point valence advantages — a coincidence of this particular catalog's values, but one that perfectly illustrates the trade-off mechanics.

Does this result feel right musically? Each individual recommendation is defensible — one honors the "EDM" identity of the request and ignores the acoustic demand, the other finds the middle ground — but the tie itself exposes a structural limitation of the scoring model. A weighted sum is *compensatory*: a total failure on one preference can always be paid for with surplus on the others, so no single preference is ever guaranteed to be respected. A listener who sets acousticness to 1.0 plausibly means "only acoustic textures," which is a hard constraint, not a tradeable preference. The current architecture has no way to express "non-negotiable"; a production-grade alternative is filter-then-rank, where hard constraints first exclude ineligible songs (e.g., acousticness below 0.6) and the weighted score only ranks the survivors. The tie-breaking behavior is also worth noting: because Python's sort is stable, the 6.86 tie was resolved by CSV row order — an arbitrary, undocumented policy rather than a musical judgment.

The small catalog plays a significant role in this behavior. With only 20 songs, no track in the library is simultaneously high-energy and acoustic, so the adversarial request is not merely difficult but literally unsatisfiable — and the system's response is informative: the achievable ceiling collapsed from ~9.7 for coherent profiles to 6.86, and to 7.44 for the second adversarial profile ("The Paradox": energy 0.95 with a chill lofi identity). This suggests a useful heuristic that emerged from testing rather than design: the score of the top-ranked result acts as a *profile coherence signal*, and a ceiling below roughly 8/10 indicates that the user's stated preferences conflict either with each other or with what the catalog contains. In a larger catalog, genuine acoustic-but-energetic tracks (folk-rock, flamenco, bluegrass) would exist and soften this failure mode, but the underlying compensatory-versus-constraint distinction would remain.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

if i kept working on this i would add a filter then rank system. right now the math lets a song completely fail the acoustic check but still rank high if the energy is perfect. adding a hard rule to drop non acoustic tracks first would give users more control. i would also add a random boost to mix up the genres so you dont get stuck in a math filter bubble

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

working on this assignment gave me an insight on how some of the apps that I use on a daily basis work. and using an ai coding assistant made the boring python stuff faster but I still had to really understand the math to fix weird edge cases and figure out the data bias, it has definitely changed how I look at my spotify recommendations because now I can unsee it 
