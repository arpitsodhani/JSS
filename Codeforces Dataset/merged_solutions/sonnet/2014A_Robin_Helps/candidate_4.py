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


# --- clause: count_gifts :: (k: int, gold: list[int]) -> int ---
def count_gifts(k, gold):
    purse = 0
    gifts = 0
    for value in gold:
        if value == 0:
            if purse > 0:
                gifts += 1
                purse -= 1
            continue
        if value >= k:
            purse += value
    return gifts


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, gold in read_input():
        out.append(count_gifts(k, gold))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
