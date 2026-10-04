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


# --- clause: is_bitonic :: (a: list[int]) -> bool ---
def is_bitonic(a):
    n = len(a)
    peak = 0
    for i in range(n):
        if a[i] > a[peak]:
            peak = i
    for i in range(1, peak + 1):
        if a[i] < a[i - 1]:
            return False
    for i in range(peak + 1, n):
        if a[i] > a[i - 1]:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("YES" if is_bitonic(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
