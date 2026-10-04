import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: gaps_of :: (a: list[int]) -> list[int] ---
def gaps_of(a):
    gaps = []
    for i in range(len(a) - 1):
        jump = a[i] - a[i + 1]
        gaps.append(jump if jump > 0 else -jump)
    return gaps


# --- clause: best_run :: (gaps: list[int]) -> int ---
def best_run(gaps):
    best = None
    for start in (0, 1):
        running = 0
        for i in range(len(gaps)):
            value = gaps[i] if (i - start) % 2 == 0 else -gaps[i]
            running += value
            if running < 0:
                running = 0
            if best is None or running > best:
                best = running
    return best


# --- clause: main :: () -> None ---
def main():
    gaps = gaps_of(read_input())
    sys.stdout.write("%d\n" % best_run(gaps))


if __name__ == "__main__":
    main()
