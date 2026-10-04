import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    at = 1
    cases = []
    for _ in range(t):
        n = tokens[at]
        at += 1
        cases.append(tokens[at:at + n])
        at += n
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
    out = []
    end = n
    while end > 0:
        start = top[end - 1]
        out.extend(p[start:end])
        end = start
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for p in read_input():
        out.append(" ".join(map(str, best_deck(p))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
