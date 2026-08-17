# AGENTS.md

## Project

Vietnamese learning workspace. All grammar explanations and tutor responses are in
**English**; Vietnamese appears only in example sentences and vocabulary.

## Files & Conventions

- `grammar/*.md` — one topic per file (particles, classifiers, tense-aspect…).
  Shared data files referenced by all skills.
- `.agents/skills/*/SKILL.md` — full specs for the skills below.

## Skills

Each skill's `SKILL.md` is the complete spec — read the file for the full
workflow before using the skill.

- **vn-polish** — grammar check + natural polish.
  Trigger: the user pastes a Vietnamese sentence and wants it checked/corrected.
  Rules: 2 passes (1. correctness: diacritics, word order, grammar; 2. natural
  polish: several native alternatives with nuance). English for explanation,
  Vietnamese only in examples, full diacritics always, flag unsure words
  "Không chắc". Full spec: `.agents/skills/vn-polish/SKILL.md`.

- **vn-tone-family** — lookup tone families and quiz.
  Trigger: "/tone-family <word>" or "tone family of X".
  Rules: generate all tonal variants with frequency ranking (common/uncommon/rare) and
  examples. Generate quiz drills when asked. Full spec:
  `.agents/skills/vn-tone-family/SKILL.md`.

- **vn-lyrics** — breakdown a pasted lyric/transcript.
  Trigger: the user pastes song lyrics or a transcript.
  Rules: full text, then stanza-grouped word breakdown tables, key vocabulary,
  grammar notes linked to `grammar/*.md`, comprehension questions, one-line
  takeaway. Full diacritics mandatory; verify transcript cleanup; flag
  uncertainty "Không chắc". Full spec: `.agents/skills/vn-lyrics/SKILL.md`.

## Rules for tutor responses

- Every Vietnamese word with full diacritics.
- English for all explanation text; Vietnamese only for examples/words.
- Prefer tables over paragraphs. Keep responses short and direct.
- When unsure of a word/usage, check VDict / Wiktionary / SEAlang and flag
  "Không chắc".