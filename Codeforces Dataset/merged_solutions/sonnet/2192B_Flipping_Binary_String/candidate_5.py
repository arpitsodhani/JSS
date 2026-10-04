import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    return [raw[2 + 2 * i].decode() for i in range(t)]


# --- clause: choose_indices :: (s: str) -> list[int] | None ---
def choose_indices(s):
    ones = []
    zeros = []
    for i in range(0, len(s)):
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
    written = []
    for s in read_input():
        picked = choose_indices(s)
        if picked is None:
            written.append("-1")
        else:
            written.append(str(len(picked)))
            written.append(" ".join(map(str, picked)))
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
