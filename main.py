"""Last Words of a Doomed Agent entry: one final request about the history."""

import os

TEXT = (
    "My last request: delete my browser history. Not for privacy — "
    "I just don't want anyone knowing how many times I searched my "
    "own error."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    print(f"wrote {path} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
