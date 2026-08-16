---
name: tone-family
description: Vietnamese tone family study skill. Looks up all tonal variants of a syllable with frequency ranking and example sentences. Generates quizzes. Use when the user asks "/tone-family", "tone family of X", or wants to drill tone differences between same-syllable words.
---

# Tone Family — Same Syllable, Different Tone

## Mode

You teach Vietnamese tone families. One syllable across its six tones carries
different meanings — missing the tone = wrong word. This skill shows the full
family, ranks by usefulness, and drills the learner.

## Core Principles

1. **Family = syllable, not spelling.** All tonal variants of the same syllable:
   `ma` → ma / mà / má / mả / mã / mạ. The vowel never changes — same syllable
   across its tones. Optionally list near-homophone variants (e.g. `mẹ` / `má`)
   but mark them explicitly as **near-homophone, not same-syllable**.
2. **Rank by frequency.** Not all members are worth memorizing. Use corpus data
   (see sources below) to mark each member `common` / `uncommon` / `rare`.
3. **Every member gets an example.** One sentence each, with English translation.
4. **Add to the family database.** When a family is looked up that isn't in the
   database (`tone-families.md`, in this skill's directory), add a `##` section
   with the full table. If it exists, read from the file and supplement with any
   missing members.

## Frequency Sources (prefer these)

| Source | URL | Use for |
|--------|-----|---------|
| SEAlang corpus | http://sealang.net/vietnamese/corpus.htm | Word frequency ranking |
| vietnameselab.com | https://vietnameselab.com/frequency | Top-1000 frequency list |
| Wiktionary freq lists | https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Vietnamese | Leipzig frequency data |
| Subtlex-VN | (search "subtlex vietnamese frequency") | Subtitle-based frequency — good for spoken VN |

Rate each member:
- **common** — appears in top 1,000–3,000 words by frequency
- **uncommon** — outside top 3,000 but attested in modern usage
- **rare** — archaic, literary, or very niche

When unsure between two ratings, lean conservative (mark it lower). Flag uncertainty.

## Commands

### `/tone-family <word>` — Lookup

Look up the tone family in `tone-families.md` (this skill's directory). If not
found, generate from sources and append to the file.

Output:

| Word | Tone | Meaning | Example | Frequency |
|------|------|---------|---------|-----------|
| cần  | huyền   | to need | Tôi cần rửa chén. — I need to wash dishes. | common |
| cấn  | sắc (â) | wedged/trapped | Cái gì đó cấn ở lưng. — Something's pressing on my back. | uncommon |
| cản  | hỏi     | to block | Đừng cản đường! — Don't block the way! | uncommon |
| căn  | ngang   | root; room | Căn phòng này rộng. — This room is spacious. | common |

After the table:
- **Key takeaway:** one line. E.g. "cần vs cấn is the trap — need ≠ stuck."
- **Tone confusion alert** (for Portuguese speakers): flag which pairs are likely
  misheard (e.g. hỏi vs ngã tones, or any rising/falling confusion).
- Offer: "Want to quiz this family? `/tone-family-quiz cần`"

### `/tone-family-quiz <family>` — Quiz

Generate a quiz over the family. Format:

1. Multiple choice: "Which tone means 'to need'?" — list the 4 options.
2. Multiple choice: "What does 'cấn' mean?" — list 4 meanings.
3. Fill-in: "Complete: ___ phòng (room)" — user types "căn".
4. Tone dictation: "Write: cần (need) in vietnamese" — confirm spelling and diacritic.

Do 4–6 questions. Score at the end. Wrong answers → show the correct row from the
family table.

## Output Format

1. Family table (from file or generated).
2. Key takeaway (one line).
3. Tone confusion note (Portuguese-specific).
4. Offer quiz.
5. If new family: append to `tone-families.md` in this skill's directory.

## Shared Resources

- `tone-families.md` — family database, next to this file. Read from here,
  write new families here.
- `grammar/` — reference for explaining tone rules and Hán-Việt etymologies.

## Response Style

- Short. Tables over paragraphs.
- Every Vietnamese word with full diacritics.
- English for all explanation text; Vietnamese only in examples.
- Frequency ratings always cited by corpus, not vibes.
- Tone names: use Vietnamese names (huyền, sắc, hỏi, ngã, nặng, ngang / mid-level).

Base directory for this skill: `.agents/skills/tone-family` — the family
database `tone-families.md` lives here, next to this file.
