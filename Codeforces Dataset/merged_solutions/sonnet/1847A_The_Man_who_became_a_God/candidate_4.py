import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        k = numbers[reader + 1]
        reader += 2
        cases.append((k, numbers[reader:reader + n]))
        reader += n
    return cases


# --- clause: least_power :: (k: int, a: list[int]) -> int ---
def least_power(k, a):
    gaps = []
    spot = 1
    while spot < len(a):
        gaps.append(abs(a[spot] - a[spot - 1]))
        spot += 1
    gaps.sort()
    keep = len(gaps) - (k - 1)
    total = 0
    for i in range(keep if keep > 0 else 0):
        total += gaps[i]
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, a in read_input():
        out.append(least_power(k, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
