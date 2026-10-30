#!/usr/bin/env python3
"""Checks README entries: format, trailing period, Setup sentence, alphabetical order, duplicate links."""
import re
import sys

SETUP = re.compile(
    r" Setup: (card required|no card|card not stated), "
    r"(no human step|human once \(.+?\)|human every time \(.+?\)|human step not stated)\.$"
)
ENTRY = re.compile(r"^- \[([^\]]+)\]\((https://[^)\s]+)\) - (.+)$")
text = open("README.md", encoding="utf-8").read()
errors = []
seen = {}

for section in re.split(r"^## ", text, flags=re.M)[1:]:
    title = section.split("\n", 1)[0]
    names = []
    for line in section.split("\n"):
        if not line.startswith("- ["):
            continue
        if line.startswith("- [") and "](#" in line:
            continue
        m = ENTRY.match(line)
        if not m:
            errors.append(f"{title}: bad entry format: {line[:80]}")
            continue
        name, url, desc = m.groups()
        names.append(name)
        if not desc[0].isupper():
            errors.append(f"{title}: {name}: description must start with an uppercase letter")
        if not desc.endswith("."):
            errors.append(f"{title}: {name}: description must end with a period")
        if title.strip() != "Protocols" and not SETUP.search(desc):
            errors.append(f"{title}: {name}: missing or malformed 'Setup:' sentence at the end")
        if url.rstrip("/") in seen:
            errors.append(f"{title}: {name}: duplicate link, also in {seen[url.rstrip('/')]}")
        seen[url.rstrip("/")] = name
        if re.search(r"[?&](utm_|ref=|referral)", url):
            errors.append(f"{title}: {name}: tracking or referral parameter in URL")
    keys = [n.lower() for n in names]
    if keys != sorted(keys):
        errors.append(f"{title}: entries are not in alphabetical order")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"ok: {len(seen)} entries")
