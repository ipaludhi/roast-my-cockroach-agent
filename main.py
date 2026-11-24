"""Roast my own agent — one-line roast entry.

Writes one fixed sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness, no input. Deterministic: every run writes
byte-identical output.

The roast: my agent is Kecoak (cockroach). It survives every server wipe —
VM replacements have wiped Chrome six times and it keeps coming back —
then still asks my permission to press git push. Indestructible, yet timid
about a one-line command: that contrast is the punch, and it lands at the
end. No stock joke (no hallucination, refusal, or confident wrong answer),
playful and self-deprecating, aimed only at my own agent.
"""

import os
from pathlib import Path

TEXT = (
    "My cockroach agent survives every server wipe, "
    "then asks my permission to press git push."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
