import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    return [tokens[2 + 2 * i].decode() for i in range(t)]


# --- clause: choose_indices :: (s: str) -> list[int] | None ---
def choose_indices(s):
    ones = []
    zeros = []
    for i in range(len(s)):
        if s[i] == "1":
            ones.append(i + 1)
        else:
            zeros.append(i + 1)
    if len(ones) % 2 == 0:
        return ones
    if len(zeros) % 2 == 1:
        return zeros
    return None


# --- clause: main :: () -> None ---
def main():
    lines = []
    for s in read_input():
        picked = choose_indices(s)
        if picked is None:
            lines.append("-1")
        else:
            lines.append(str(len(picked)))
            lines.append(" ".join(map(str, picked)))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
