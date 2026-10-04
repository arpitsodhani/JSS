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


# --- clause: count_gifts :: (k: int, gold: list[int]) -> int ---
def count_gifts(k, gold):
    purse = 0
    gifts = 0
    for item in gold:
        if item >= k:
            purse += item
        elif item == 0 and purse:
            purse -= 1
            gifts += 1
    return gifts


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, gold in read_input():
        out.append(count_gifts(k, gold))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
