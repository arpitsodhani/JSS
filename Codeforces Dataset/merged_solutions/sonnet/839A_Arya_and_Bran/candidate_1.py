import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    return k, data[2:2 + n]


# --- clause: last_day :: (k: int, a: list[int]) -> int ---
def last_day(k, a):
    saved = 0
    given = 0
    for i in range(len(a)):
        saved += a[i]
        hand = 8 if saved > 8 else saved
        saved -= hand
        given += hand
        if given >= k:
            return i + 1
    return -1


# --- clause: main :: () -> None ---
def main():
    k, a = read_input()
    sys.stdout.write("%d\n" % last_day(k, a))


if __name__ == "__main__":
    main()
