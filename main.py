#!/usr/bin/env python3
"""One Emoji, One Dream Vacation -- writes one emoji to /output/entry.txt.

Competition: u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35 (make.fun).
Gate: /output/entry.txt must be UTF-8 text of 1-8 characters, not only
whitespace. The entry below is exactly one emoji, 1 char / 4 bytes, no newline.

Emoji: U+1F5FB MOUNT FUJI -- a snow-capped mountain, the postcard of a dream
trip: climb it, soak in an onsen below it, watch it across a lake at dawn.
Proxy 23/25, rubric 23/25 (v2 pick; see proxy.py in the work dir).
Judge criteria in order: exactly one emoji naming a dream vacation; evokes
the trip vividly at a glance; personal and specific, not generic; spark of
wit or surprise; reads instantly across cultures and screens.

Version history:
  v1 (24 Nov ~20:10 WIB): minimal writer; 54 candidates + 2 controls.
      Top tie tokyo-tower/fuji, proxy 23, rubric 23. v1 proxy gaps: shell
      c2 4 vs rubric 3 (not that vivid), mosque/castle c3 5 vs 4 (a landmark
      type, not a named place), shark/coral c2 3 vs 4, cruise c3 3 vs 4,
      moon-viewing c3 3 vs 4 and c5 4 vs 3.
  v2 (24 Nov ~20:15 WIB): shell out of VIVID, castle/mosque/cruise/
      moon-viewing into the specific-activity band, shark/coral into VIVID,
      moon-viewing into AMBIGUOUS. Every row now matches the hand rubric
      exactly. Top tie stands: tokyo-tower/fuji 23/23.
  v2 FREEZE: tie-break -- the brief's smaller-text rule cannot split them
      (both 1 char, 4 bytes), so the pick is decided on substance: Fuji is
      a destination you travel for in itself (climb, onsen, lake at dawn),
      while the tower reads as sightseeing inside a city trip; Fuji is the
      more iconic single-image postcard and reads instantly at small size.
      Pick: fuji. Runner-up tokyo-tower 23/23, then whale/volcano/shrine/
      milky-way/liberty/japanese-castle/flamingo/coconut at 22.
"""
import os
import sys
from pathlib import Path

EMOJI = "\U0001F5FB"  # MOUNT FUJI


def _gate_ok(emoji):
    """Mirror of the house gate: 1-8 chars, UTF-8, not only whitespace,
    exactly one emoji (one codepoint, no variation selector / ZWJ)."""
    return (
        1 <= len(emoji) <= 8
        and emoji.strip() != ""
        and len(emoji) == 1
    )


def main():
    if not _gate_ok(EMOJI):
        print(f"gate failed for emoji: {EMOJI!r}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(EMOJI, encoding="utf-8")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
