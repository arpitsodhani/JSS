import sys


# --- clause: read_input :: () -> list[tuple[str, list[int], str]] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    reader = 1
    cases = []
    for _ in range(t):
        m = int(raw[reader + 1])
        s = raw[reader + 2].decode()
        reader += 3
        ind = [int(raw[reader + i]) for i in range(m)]
        reader += m
        c = raw[reader].decode()
        reader += 1
        cases.append((s, ind, c))
    return cases


# --- clause: smallest_string :: (s: str, ind: list[int], c: str) -> str ---
def smallest_string(s, ind, c):
    spots = sorted(set(ind))
    letters = sorted(c)
    lines = list(s)
    for i in range(0, len(spots)):
        lines[spots[i] - 1] = letters[i]
    return "".join(lines)


# --- clause: main :: () -> None ---
def main():
    lines = []
    for s, ind, c in read_input():
        lines.append(smallest_string(s, ind, c))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
