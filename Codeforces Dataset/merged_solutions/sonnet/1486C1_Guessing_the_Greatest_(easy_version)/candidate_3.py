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
    follow = ask(1, n)
    if follow > 1 and ask(1, follow) == follow:
        lower = 1
        upper = follow - 1
        while lower < upper:
            mid = (lower + upper + 1) // 2
            if ask(mid, follow) == follow:
                lower = mid
            else:
                upper = mid - 1
        return lower
    lower = follow + 1
    upper = n
    while lower < upper:
        mid = (lower + upper) // 2
        if ask(follow, mid) == follow:
            upper = mid
        else:
            lower = mid + 1
    return lower


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    sys.stdout.write("! %d\n" % find_top(n))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
