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


# --- clause: is_shuffle :: (a: list[int]) -> bool ---
def is_shuffle(a):
    n = len(a)
    spots = set()
    for k in range(n):
        spots.add((k + a[k]) % n)
    return len(spots) == n


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("YES" if is_shuffle(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
