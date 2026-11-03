# Talks built from the study (version 5 numbers)

Two non-technical talks derived from the analysis report and paper, written for people with no background in robotics, AI or law.

| Talk | Deck (editable) | Script | Video |
|---|---|---|---|
| Expanded edition, version-4 numbers (41 slides, about 34 minutes) | https://claude.ai/artifact/47f5QuWtn598ui7JVAo7zw | `../who_governs_the_robots_v2_script.md` | https://claude.ai/artifact/LRUSm9G4dbFFXMYwsgWppH (player page) and `../who_governs_the_robots_v2.mp4` |
| Keynote for an AI research or AI governance conference (20 slides, about 21 minutes) | https://claude.ai/artifact/FaM6krx6snfSm69VKW4d98 and `keynote_deck/` | `keynote_script.md` | https://claude.ai/artifact/J16RBooUfYnqT1y5bdSCEx (player page) and `who_governs_the_robots_keynote.mp4` (+ `.srt`) |
| Main-stage talk in the TED format (15 slides, about 13 minutes) | https://claude.ai/artifact/MMcpN4zupd3k9EifNgSksq and `mainstage_deck/` | `mainstage_script.md` | https://claude.ai/artifact/QDW4WpoZntkYr6L3B3KpZ6 (player page) and `who_governs_the_robots_mainstage.mp4` (+ `.srt`) |

The first, 23-slide deck is at https://claude.ai/artifact/BQAsXb71m8uLkpKDNFxXTw (no video). The player pages hold the videos as attached parts that hand over at slide boundaries, with chapters and the script beside the player.

Each deck folder holds `build.py` (generates the slides) and `project/` (the slide files as published). `render_deck.js` renders a deck to 1920x1080 frames and checks for overflow; `make_talk.py` narrates a script with Edge neural text-to-speech (one voice per talk: en-GB-Ryan for the keynote, en-US-Ava for the main stage) and assembles the MP4 with chapters and an SRT. Every number in the scripts comes from the v5 tables (`tables/`, `data/results.json`); the slides cite the table each figure comes from. The talks are drafts for a human speaker to adapt: the anecdotes are framed as invitations to the audience ("you have seen the videos"), not as the speaker's own experiences.
