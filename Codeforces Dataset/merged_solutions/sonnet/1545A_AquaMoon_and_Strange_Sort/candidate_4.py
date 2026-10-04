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


# --- clause: can_sort :: (a: list[int]) -> bool ---
def can_sort(a):
    evens = sorted(a[0::2])
    odds = sorted(a[1::2])
    ranked = sorted(a)
    return evens == sorted(ranked[0::2]) and odds == sorted(ranked[1::2])


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("YES" if can_sort(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
