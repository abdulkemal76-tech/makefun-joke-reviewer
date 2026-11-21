#!/usr/bin/env python3
"""make.fun: The joke the reviewer laughs at.

Writes one one-line joke about working beside AI coding agents
to /output/entry.txt. Deterministic, stdlib only, no network.
"""
import os

TEXT = """My AI agent approved my pull request, then rewrote the whole thing anyway, for consistency."""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
