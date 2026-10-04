import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        cases.append(numbers[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: best_sum :: (a: list[int]) -> int ---
def best_sum(a):
    total = sum(a)
    pairs = set()
    for i in range(len(a) - 1):
        pairs.add(a[i] + a[i + 1])
    if -2 in pairs:
        return total + 4
    if 0 in pairs:
        return total
    return total - 4


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(best_sum(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
