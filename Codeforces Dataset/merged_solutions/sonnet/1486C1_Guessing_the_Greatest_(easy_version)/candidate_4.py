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
    right = second < n and ask(second, n) == second
    if right:
        low = second + 1
        high = n
        while low < high:
            mid = (low + high) // 2
            if ask(second, mid) == second:
                high = mid
            else:
                low = mid + 1
        return low
    low = 1
    high = second - 1
    while low < high:
        mid = (low + high + 1) // 2
        if ask(mid, second) == second:
            low = mid
        else:
            high = mid - 1
    return low


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    sys.stdout.write("! %d\n" % find_top(n))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
