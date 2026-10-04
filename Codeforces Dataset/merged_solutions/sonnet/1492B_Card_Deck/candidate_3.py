import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        offset += 1
        cases.append(fields[offset:offset + n])
        offset += n
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
    pieces = []
    end = n
    while end > 0:
        start = top[end - 1]
        pieces.extend(p[start:end])
        end = start
    return pieces


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for p in read_input():
        pieces.append(" ".join(map(str, best_deck(p))))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
