# 🇻🇳 Tiếng Việt — AI-Assisted Vietnamese Practice

A set of [agent skills](https://opencode.ai) for practicing Vietnamese through
writing, tone families, and real content. Write a sentence, get told what you got
right and how to sound more natural. Look up tones. Learn from songs.
Built by a learner, for learners.

## Skills

| Skill | How you use it | What it does |
|-------|----------------|--------------|
| **vietnamese-polish** | Write a sentence first, then ask the skill to check it | Feedback on *your* sentence: what you got right, what to fix, and how a native would say it — with multiple natural alternatives |
| **tone-family** | `/tone-family <word>` | All tonal variants of a syllable with corpus-based frequency ranking. Quiz mode: `/tone-family-quiz <word>` |
| **song-lyrics** | Paste a lyric or transcript from the song you're listening to | Word-by-word breakdown, grammar explanations from the lyrics, comprehension questions |

### Example

The polish skill checks your sentence, then shows how a native would say it:

> You: *Em rất vui khi anh gọi cho em.*
> Fix: **gọi** alone = to call (a name/summon); calling *on the phone* is **gọi điện**.
> → *Em rất vui khi anh gọi điện cho em.* — I'm happy when you call me.

## Install

One command, works with 30+ skill-capable agents:

```
npx skills add GuilhermeCampano/tieng-viet
```

Or per agent:

| Agent | How |
|-------|-----|
| opencode | `opencode skill add ./tieng-viet/.agents/skills/<name>` |
| Claude Code / Codex / Gemini | clone the repo — `AGENTS.md` auto-loads, skills are in `.agents/skills/` |
| Cursor | copy `.cursor/rules/tieng-viet.mdc` from the repo |
| Copilot | `.github/copilot-instructions.md` is read automatically |

A skill is a single `SKILL.md` file with `name` and `description` frontmatter:

```yaml
---
name: song-lyrics
description: Paste a Vietnamese lyric and get a word breakdown, grammar, and questions.
---
```

## Why these skills exist

I learn Vietnamese the traditional way — a tutor once a week. In between, my
routine is simple:

- **Watch one Vietnamese video or listen to one Vietnamese song every day.**
- **Write at least 5 sentences a day.**

I write the sentences myself, then ask the polish skill to check them: what did I
do right, what can improve, how would a native say this. That's where the tones
break. Reading *recognizes* a word; writing *recalls* it — and recall forces you
to get the diacritics right. These skills fill the gap between tutor sessions, so
every day has feedback even when nobody's grading you.

### Why tone families

Tones are the hard part. Memorizing *la* in isolation is fragile — you'll mistake
the tone later. But learning it as a family:

> *la* (shout) — *là* (to be) — *lá* (leaf) — *lạ* (strange)

makes the contrast stick. You don't need to remember every variant — but once
you've seen the family, you stop guessing which tone a word takes. Each entry
carries a corpus-based frequency (common / uncommon / rare) so you know which
ones actually matter.

### Why songs

Song lyrics are real Vietnamese with real grammar. The song-lyrics skill breaks
down every line, explains the grammar in context, and asks comprehension
questions — turning passive listening into active learning.

## Structure

```
tieng-viet/
├── grammar/            Grammar reference (particles, classifiers, tense-aspect…)
│                       — shared by all skills
├── .agents/skills/     The three skills (vietnamese-polish, tone-family, song-lyrics)
│   └── tone-family/
│       └── tone-families.md    Tone family database with frequency rankings
├── .cursor/rules/      Cursor pointer file
└── .github/            Copilot instructions
```

## Resources

Skills check words against reliable sources, not guesses:

- [VDict](https://vdict.com) — VI-EN dictionary
- [Wiktionary](https://vi.wiktionary.org) — etymology and breakdowns
- [SEAlang](http://sealang.net/vietnamese/) — dictionary and corpus frequency

## License

MIT

---

Maintained by a learner, for learners. Issues and suggestions welcome — open an
issue or a PR with a new tone family, grammar note, or example.