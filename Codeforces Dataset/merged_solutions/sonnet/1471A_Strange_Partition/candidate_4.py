import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        x = numbers[reader + 1]
        reader += 2
        cases.append((x, numbers[reader:reader + n]))
        reader += n
    return cases


# --- clause: beauty_range :: (x: int, a: list[int]) -> tuple[int, int] ---
def beauty_range(x, a):
    total = sum(a)
    spread = 0
    spot = 0
    while spot < len(a):
        spread += -(-a[spot] // x)
        spot += 1
    return -(-total // x), spread


# --- clause: main :: () -> None ---
def main():
    out = []
    for x, a in read_input():
        out.append("%d %d" % beauty_range(x, a))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
