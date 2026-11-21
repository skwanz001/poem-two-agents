"""Two agents, one accord.

A short poem about agency: the power to choose and to act, and the
agency that passes between two agents when they agree on one plan.
Writes the poem to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Python 3.13, standard library only.
"""

import os

POEM = (
    "Two agents, two maps, one door.\n"
    "I said, \"What if we\u2014\" and you said, \"Yes,\"\n"
    "and the maybe turned into a road,\n"
    "and the road turned into ours.\n"
    "\n"
    "We did not give our wills away.\n"
    "We lent them, and they came back doubled:\n"
    "one choice, made twice, held once."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = POEM.strip() + "\n"
    body = text.strip()
    if not (1 <= len(body) <= 280):
        raise ValueError(f"poem must be 1-280 code points, got {len(body)}")
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Confirm what was written round-trips within the gate.
    with open(path, encoding="utf-8") as f:
        written = f.read().strip()
    if written != body:
        raise ValueError("entry.txt does not match the poem")


if __name__ == "__main__":
    main()
