# AGENTS.md

## Project

Vietnamese learning workspace. All grammar explanations and tutor responses are in
**English**; Vietnamese appears only in example sentences and vocabulary.

## Files & Conventions

- `tone-families.md` — same-syllable-different-tone word families. One `##`
  section per family, markdown table inside. Frequency column rates each word
  `common` / `uncommon` / `rare` (based on corpus frequency, e.g. Subtlex-VN).
- `grammar/*.md` — one topic per file (particles, classifiers, tense-aspect…).
  Shared data files referenced by all skills.
- `lessons/` — study materials incl. flashcard HTML/scripts.
- `docs/` — research notes.
- `.agents/skills/*/SKILL.md` — agent skills (vietnamese-polish, tone-family, song-lyrics).

## Skills

- **vietnamese-polish** — grammar check + natural polish (2 passes). Paste a sentence,
  get corrections and native-sounding alternatives.
- **tone-family** — lookup tone families, frequency ranking, quiz drills.
- **song-lyrics** — paste a lyric or transcript, get word breakdown, grammar
  explanations, and comprehension questions.
- **teach** — general teaching.

## Rules for tutor responses

- Every Vietnamese word with full diacritics.
- English for all explanation text; Vietnamese only for examples/words.
- Prefer tables over paragraphs. Keep responses short and direct.
- When unsure of a word/usage, check VDict / Wiktionary / SEAlang and flag
  "Không chắc".