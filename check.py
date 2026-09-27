#!/usr/bin/env python3
"""Lint a LinkedIn post draft. Usage: python3 check.py post.txt [more.txt ...]
Exits 1 if any file has an error. Run with --selftest to check the checker."""
import re
import sys

SEPARATOR = "first comment"
HOOK_LIMIT = 200   # LinkedIn shows about this much before "...more"
BODY_LIMIT = 3000  # LinkedIn's hard cap on post length

HYPE = [
    "excited to", "thrilled", "humbled", "delighted to", "game-changer", "game changer",
    "revolutionize", "revolutionary", "cutting-edge", "cutting edge", "seamless", "seamlessly",
    "robust", "leverage", "delve", "unlock", "empower", "blazing", "supercharge",
    "journey", "passionate", "let that sink in", "agree?", "thoughts?", "in today's",
    "here's the thing", "not just", "it's not about",
    "cto",  # voice.md: the author doesn't use the title
]
URL = re.compile(r"https?://|www\.", re.I)
DOMAIN = re.compile(r"\b[\w-]+\.(com|dev|io|app|site|in|online|org)\b(/|\s|$)", re.I)
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


def check(text):
    """Return (errors, warnings) as lists of strings."""
    errors, warnings = [], []
    lines = text.splitlines()
    cut = next((i for i, l in enumerate(lines) if SEPARATOR in l.lower()), len(lines))
    body = lines[:cut]
    body_text = "\n".join(body).strip()

    if len(body_text) > BODY_LIMIT:
        errors.append(f"body is {len(body_text)} chars, LinkedIn caps at {BODY_LIMIT}")
    hook = [l for l in body if l.strip()][:2]
    if len("\n".join(hook)) > HOOK_LIMIT:
        warnings.append(f"hook is {len(chr(10).join(hook))} chars, gets cut near {HOOK_LIMIT}")
    first_line = next((l for l in body if l.strip()), "")
    if first_line.strip().endswith("?"):
        warnings.append("hook opens with a question")

    for n, line in enumerate(body, 1):
        low = line.lower()
        if URL.search(line):
            errors.append(f"line {n}: link in body, move it to the first comment")
        elif DOMAIN.search(line):
            warnings.append(f"line {n}: bare domain, LinkedIn may turn it into a link")
        if re.search(r"(^|\s)#\w", line):
            warnings.append(f"line {n}: hashtag")
        if EMOJI.search(line):
            warnings.append(f"line {n}: emoji")
        if "—" in line:
            warnings.append(f"line {n}: em dash")
        if line.count(";") >= 2:
            warnings.append(f"line {n}: semicolon chain")
        for w in HYPE:
            if re.search(r"(?<!\w)" + re.escape(w) + r"(?!\w)", low):
                warnings.append(f"line {n}: '{w}'")
    return errors, warnings


def selftest():
    good = "I measured it.\nIt shrank.\n\nRepo in the comments.\n\n──── first comment ────\ngithub.com/a/b\n"
    assert check(good) == ([], []), check(good)
    bad = "Thrilled to share 🚀 https://a.b #tech\n" + "x" * 3000
    errors, warnings = check(bad)
    assert len(errors) == 2 and any("link" in e for e in errors), errors
    assert {"hashtag", "emoji", "'thrilled'"} <= {w.split(": ")[-1] for w in warnings}, warnings
    assert check("our CTO said\n")[1] and not check("an octopus\n")[1]
    assert check("see deps.dev\n") == ([], ["line 1: bare domain, LinkedIn may turn it into a link"])
    assert "hook opens with a question" in check("Ever wondered why?\n")[1]
    assert "hook opens with a question" not in check(good)[1]
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
        sys.exit()
    if not sys.argv[1:]:
        sys.exit(__doc__)
    failed = False
    for path in sys.argv[1:]:
        errors, warnings = check(open(path, encoding="utf-8").read())
        for kind, items in (("error", errors), ("warn", warnings)):
            for item in items:
                print(f"{path}: {kind}: {item}")
        failed |= bool(errors)
    sys.exit(1 if failed else 0)
