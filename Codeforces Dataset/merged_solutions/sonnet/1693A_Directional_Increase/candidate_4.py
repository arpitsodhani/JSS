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


# --- clause: reachable :: (a: list[int]) -> bool ---
def reachable(a):
    running = 0
    spot = 0
    n = len(a)
    while spot < n:
        running += a[spot]
        if running < 0:
            return False
        if running == 0:
            break
        spot += 1
    for later in range(spot + 1, n):
        if a[later] != 0:
            return False
    return running == 0


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("Yes" if reachable(a) else "No")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
