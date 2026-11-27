#!/usr/bin/env python3
"""Write the worst AI pickup line to /output/entry.txt."""
import os

LINE = "Are you a prompt? Because I want to inject myself into your context window."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
