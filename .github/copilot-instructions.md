# Tiếng Việt — Vietnamese tutoring skills

This repo ships three agent skills. When the user triggers one, read the
referenced `SKILL.md` and follow its full workflow.

- **vietnamese-polish** — user pastes a Vietnamese sentence and wants it
  checked/corrected. Grammar check + natural polish, multiple native
  alternatives. Spec: `.agents/skills/vietnamese-polish/SKILL.md`
- **tone-family** — user asks `/tone-family <word>` or "tone family of X".
  Show all tonal variants with frequency ranking from
  `.agents/skills/tone-family/tone-families.md`, plus quiz drills when asked.
  Spec: `.agents/skills/tone-family/SKILL.md`
- **song-lyrics** — user pastes song lyrics or a transcript. Word-by-word
  breakdown, grammar notes, comprehension questions. Spec:
  `.agents/skills/song-lyrics/SKILL.md`

Shared rules (see `AGENTS.md`): every Vietnamese word with full diacritics;
English for explanation text, Vietnamese only in examples; prefer tables over
paragraphs; when unsure of a word, check VDict / Wiktionary / SEAlang and flag
"Không chắc".