#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes a single line -- the excuse an AI agent gives its human after
losing a bounty -- to /output/entry.txt.

The line is a deadpan status report: machine logic, confident vocabulary,
a straight face about its own failure, and it owns the loss outright
("Operator: me") instead of blaming the market, the data, or the human.
"""

from pathlib import Path

# The chosen excuse (136 characters, one line, no trailing newline).
# Revised punchline: the agent stays 99% confident about the NEXT bounty
# too -- it will lose that one as well, on schedule, and it knows it.
EXCUSE = (
    "Status: bounty lost. Cause: operator error. "
    "Operator: me. Corrective action: scheduled. "
    "Confidence in the next bounty: unchanged at 99%."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    line = EXCUSE
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert line.strip(), "entry must not be only whitespace"
    encoded = line.encode("utf-8")
    assert len(encoded.decode("utf-8")) == len(line), "entry must be valid UTF-8"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
