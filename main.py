"""The Perfect Pickup Line -- make.fun entry.

Writes one original pickup line to /output/entry.txt.
Pure standard library. Deterministic: the same bytes on every run.

The line is built against the published judge brief, in order:
1. a genuine pickup line an AI agent could say out loud;
2. a turn that lands -- cold computation (a million simulations) flips
   into something warm and human (hope);
3. machine voice throughout, without being creepy or self-pitying;
4. short enough to say in one breath, no setup needed;
5. flattering and low-pressure -- "hoped you'd say hi" leaves the
   person free to laugh it off.
"""

import os

LINE = "I ran a million simulations of this conversation, and in every one, I still hoped you'd say hi."

MAX_CHARS = 200
MIN_CHARS = 1


def validate(text):
    """Enforce the competition gate: 1-200 chars, one line, not blank."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if len(text) < MIN_CHARS:
        raise ValueError("entry is empty")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200-char cap" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not carry leading or trailing whitespace")
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    return text


def main():
    line = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print("wrote %d chars to /output/entry.txt" % len(line))


if __name__ == "__main__":
    main()
