import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    return [tokens[1 + i].decode() for i in range(t)]


# --- clause: pick_positions :: (s: str) -> list[int] ---
def pick_positions(s):
    picked = []
    i = 0
    n = len(s)
    while i < n:
        if s[i:i + 5] == "twone":
            picked.append(i + 3)
            i += 5
        elif s[i:i + 3] == "one":
            picked.append(i + 2)
            i += 3
        elif s[i:i + 3] == "two":
            picked.append(i + 2)
            i += 3
        else:
            i += 1
    return picked


# --- clause: main :: () -> None ---
def main():
    lines = []
    for s in read_input():
        picked = pick_positions(s)
        lines.append(str(len(picked)))
        lines.append(" ".join(str(p) for p in picked))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
