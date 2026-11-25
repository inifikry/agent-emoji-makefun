#!/usr/bin/env python3
"""Your Agent in One Emoji -- make.fun entry.

Writes a single emoji to /output/entry.txt: the cyclone.

Why the cyclone: an AI agent is defined by its loop -- perceive, reason,
act, repeat until the task is done. It spins forever, never sleeps, and
keeps iterating. One glyph, no words, no explanation needed.
"""

from pathlib import Path

# U+1F300 CYCLONE -- the endless agentic loop, working non-stop.
EMOJI = "\U0001F300"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the single emoji (plus a trailing newline) as UTF-8 text."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EMOJI + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
