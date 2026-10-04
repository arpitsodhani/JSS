import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        k = raw[reader + 1]
        reader += 2
        cases.append((k, raw[reader:reader + n]))
        reader += n
    return cases


# --- clause: swaps_needed :: (k: int, p: list[int]) -> int ---
def swaps_needed(k, p):
    wrong = []
    for i in range(0, len(p)):
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
    lines = []
    for k, p in read_input():
        lines.append(swaps_needed(k, p))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()
