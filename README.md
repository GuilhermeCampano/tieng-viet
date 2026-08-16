# Tiếng Việt — AI-Assisted Vietnamese Practice

A set of [agent skills](https://opencode.ai) for practicing Vietnamese through writing.
Paste a sentence, get corrected. Look up tone families. Learn from song lyrics.

**This is a complement to traditional study, not a replacement.** You learn from
a teacher or textbook. This is where you practice writing and get instant,
native-level feedback.

## Skills

| Skill | Trigger | What it does |
|-------|---------|--------------|
| **vietnamese-polish** | Paste any Vietnamese sentence | 2-pass feedback: (1) fix grammar/spelling, (2) show how a native would say it — with multiple natural alternatives |
| **tone-family** | `/tone-family <word>` | Shows all tonal variants of a syllable with corpus-based frequency ranking. Quiz mode: `/tone-family-quiz <word>` |
| **song-lyrics** | Paste lyrics or a transcript | Word-by-word breakdown, grammar explanations from the lyrics, comprehension questions |

## Methodology

### Why write, not just read?

Vietnamese is tonal. The difference between *la* (shout), *là* (to be), *lá* (leaf),
and *lạ* (strange) is one diacritic. Reading recognizes the word — writing recalls it.
Producing a sentence from memory forces you to get the tones right.

### Why AI feedback?

A textbook tells you the rule. A tutor corrects you hours later. An AI agent
corrects you instantly, every sentence, as many times as you want.

### Why tone families?

Learning *là* alone is fragile. Learning *la / là / lá / lả / lã / lạ* together
makes the tones stick — because you see the contrast. Each family comes with
corpus-based frequency so you know which ones matter.

### Why song lyrics?

Real Vietnamese, with real grammar, real emotion. The song-lyrics skill breaks
down every line, explains the grammar in context, and tests comprehension —
turning passive listening into active learning.

## Install

1. Clone the repo:
   ```
   git clone https://github.com/GuilhermeCampano/tieng-viet.git
   ```

2. Register the skills with your agent (opencode, Claude Code, etc.):
   ```
   opencode skill add ./tieng-viet/.agents/skills/vietnamese-polish
   opencode skill add ./tieng-viet/.agents/skills/tone-family
   opencode skill add ./tieng-viet/.agents/skills/song-lyrics
   ```

   Or if your agent auto-discovers skills from `.agents/skills/`, just open the repo.

## Structure

```
grammar/          Grammar reference (particles, classifiers, tense-aspect…)
                  — shared by all skills
tone-families.md  Tone family database with frequency rankings
lessons/          Study materials and flashcards
.agents/skills/   The three skills
```

## Resources

Skills reference these sources when checking words:

- [VDict](https://vdict.com) — VI-EN dictionary
- [Wiktionary](https://vi.wiktionary.org) — etymology and breakdowns
- [SEAlang](http://sealang.net/vietnamese/) — dictionary and corpus frequency

## License

MIT