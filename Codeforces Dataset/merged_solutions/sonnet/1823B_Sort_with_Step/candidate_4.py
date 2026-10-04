import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        k = numbers[cursor + 1]
        cursor += 2
        cases.append((k, numbers[cursor:cursor + n]))
        cursor += n
    return cases


# --- clause: swaps_needed :: (k: int, p: list[int]) -> int ---
def swaps_needed(k, p):
    n = len(p)
    wrong = [i for i in range(n) if (p[i] - i - 1) % k]
    if len(wrong) == 0:
        return 0
    if len(wrong) == 2 and (p[wrong[1]] - wrong[0] - 1) % k == 0:
        if (p[wrong[0]] - wrong[1] - 1) % k == 0:
            return 1
    return -1


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, p in read_input():
        out.append(swaps_needed(k, p))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
