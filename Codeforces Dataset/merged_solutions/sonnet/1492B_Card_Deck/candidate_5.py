import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        reader += 1
        cases.append(raw[reader:reader + n])
        reader += n
    return cases


# --- clause: best_deck :: (p: list[int]) -> list[int] ---
def best_deck(p):
    n = len(p)
    top = [0] * n
    where = 0
    for i in range(n):
        if p[i] > p[where]:
            where = i
        top[i] = where
    lines = []
    end = n
    while end > 0:
        start = top[end - 1]
        lines.extend(p[start:end])
        end = start
    return lines


# --- clause: main :: () -> None ---
def main():
    lines = []
    for p in read_input():
        lines.append(" ".join(map(str, best_deck(p))))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
