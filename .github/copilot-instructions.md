# Tiếng Việt — Vietnamese tutoring skills

This repo ships three agent skills. When the user triggers one, read the
referenced `SKILL.md` and follow its full workflow.

- **vn-polish** — user pastes a Vietnamese sentence and wants it
  checked/corrected. Grammar check + natural polish, multiple native
  alternatives. Spec: `.agents/skills/vn-polish/SKILL.md`
- **vn-tone-family** — user asks `/tone-family <word>` or "tone family of X".
  Generate all tonal variants with frequency ranking, plus quiz drills when asked.
  Spec: `.agents/skills/vn-tone-family/SKILL.md`
- **vn-lyrics** — user pastes song lyrics or a transcript. Word-by-word
  breakdown, grammar notes, comprehension questions. Spec:
  `.agents/skills/vn-lyrics/SKILL.md`

Shared rules (see `AGENTS.md`): every Vietnamese word with full diacritics;
English for explanation text, Vietnamese only in examples; prefer tables over
paragraphs; when unsure of a word, check VDict / Wiktionary / SEAlang and flag
"Không chắc".