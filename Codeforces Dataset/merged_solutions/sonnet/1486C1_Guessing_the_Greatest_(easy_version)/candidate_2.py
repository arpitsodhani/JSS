import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.readline())


# --- clause: ask :: (l: int, r: int) -> int ---
def ask(l, r):
    sys.stdout.write("? %d %d\n" % (l, r))
    sys.stdout.flush()
    return int(sys.stdin.readline())


# --- clause: find_top :: (n: int) -> int ---
def find_top(n):
    second = ask(1, n)
    if second > 1 and ask(1, second) == second:
        bottom = 1
        top_value = second - 1
        while bottom < top_value:
            mid = (bottom + top_value + 1) // 2
            if ask(mid, second) == second:
                bottom = mid
            else:
                top_value = mid - 1
        return bottom
    bottom = second + 1
    top_value = n
    while bottom < top_value:
        mid = (bottom + top_value) // 2
        if ask(second, mid) == second:
            top_value = mid
        else:
            bottom = mid + 1
    return bottom


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    sys.stdout.write("! %d\n" % find_top(n))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
