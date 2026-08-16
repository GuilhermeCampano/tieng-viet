#!/usr/bin/env python3
"""Generate flashcards from tone-families.md."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAMILIES = ROOT / "tone-families.md"
OUT = ROOT / "lessons" / "tone-family-flashcards.html"

def parse_families(text: str):
    cards = []
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if len(parts) < 4 or parts[0] in ("Word",) or set(parts[0]) == {"-"}:
            continue
        cards.append({
            "word": parts[0],
            "tone": parts[1],
            "meaning": parts[2],
            "sentence": parts[3],
        })
    return cards

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tone Family Flashcards</title>
<style>
  body { font-family: system-ui, sans-serif; display: flex; flex-direction: column; align-items: center; gap: 1rem; background: #f4f4f5; margin: 0; min-height: 100vh; justify-content: center; }
  #card { width: min(90vw, 480px); min-height: 260px; background: #fff; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,.12); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: .75rem; padding: 2rem; cursor: pointer; user-select: none; text-align: center; }
  #word { font-size: 3rem; font-weight: 700; }
  #tone { color: #6366f1; font-weight: 600; }
  #meaning { font-size: 1.4rem; }
  #sentence { color: #52525b; font-style: italic; }
  #progress { color: #71717a; }
  .buttons { display: flex; gap: 1rem; }
  button { padding: .6rem 1.4rem; border: none; border-radius: 8px; font-size: 1rem; cursor: pointer; color: #fff; }
  #again { background: #ef4444; } #good { background: #22c55e; } #easy { background: #3b82f6; }
  #back { background: #71717a; }
</style>
</head>
<body>
  <div id="card">
    <div id="word"></div>
    <div id="tone"></div>
    <div id="meaning"></div>
    <div id="sentence"></div>
  </div>
  <div class="buttons">
    <button id="back">Back</button>
    <button id="again">Again</button>
    <button id="good">Good</button>
    <button id="easy">Easy</button>
  </div>
  <div id="progress"></div>

<script>
const cards = __CARDS__;

let order = shuffle(cards.map((_, i) => i));
let pos = 0;
let flipped = false;

function shuffle(a) { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }

function show() {
  const c = cards[order[pos]];
  document.getElementById("word").textContent = c.word;
  document.getElementById("tone").textContent = flipped ? c.tone : "";
  document.getElementById("meaning").textContent = flipped ? c.meaning : "";
  document.getElementById("sentence").textContent = flipped ? c.sentence : "";
  document.getElementById("progress").textContent = `${pos + 1} / ${cards.length}`;
}

document.getElementById("card").addEventListener("click", () => { flipped = !flipped; show(); });

function next(gap) {
  if (gap > 1 && pos + 1 < cards.length) {
    const card = order.splice(pos, 1)[0];
    order.splice(Math.min(pos + gap, order.length), 0, card);
  }
  pos = (pos + 1) % cards.length;
  flipped = false;
  show();
}

document.getElementById("back").addEventListener("click", () => { order = shuffle(cards.map((_, i) => i)); pos = 0; flipped = false; show(); });
document.getElementById("again").addEventListener("click", () => next(0));
document.getElementById("good").addEventListener("click", () => next(1));
document.getElementById("easy").addEventListener("click", () => next(2));

show();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    cards = parse_families(FAMILIES.read_text())
    OUT.write_text(TEMPLATE.replace("__CARDS__", json.dumps(cards, ensure_ascii=False)))
    print(f"Wrote {OUT} with {len(cards)} cards.")
