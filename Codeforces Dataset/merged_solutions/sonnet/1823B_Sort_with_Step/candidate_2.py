import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    at = 1
    cases = []
    for _ in range(t):
        n = tokens[at]
        k = tokens[at + 1]
        at += 2
        cases.append((k, tokens[at:at + n]))
        at += n
    return cases


# --- clause: swaps_needed :: (k: int, p: list[int]) -> int ---
def swaps_needed(k, p):
    wrong = []
    for i in range(len(p)):
        if (p[i] - i - 1) % k:
            wrong.append(i)
        if len(wrong) > 2:
            return -1
    if not wrong:
        return 0
    if len(wrong) != 2:
        return -1
    i, j = wrong
    if (p[j] - i - 1) % k or (p[i] - j - 1) % k:
        return -1
    return 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, p in read_input():
        out.append(swaps_needed(k, p))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
