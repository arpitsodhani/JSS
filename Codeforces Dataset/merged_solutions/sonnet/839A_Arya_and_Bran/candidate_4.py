import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    k = numbers[1]
    return k, numbers[2:2 + n]


# --- clause: last_day :: (k: int, a: list[int]) -> int ---
def last_day(k, a):
    saved = 0
    left = k
    day = 0
    while day < len(a):
        saved += a[day]
        day += 1
        hand = min(8, saved)
        saved -= hand
        left -= hand
        if left <= 0:
            return day
    return -1


# --- clause: main :: () -> None ---
def main():
    k, a = read_input()
    sys.stdout.write("%d\n" % last_day(k, a))


if __name__ == "__main__":
    main()
