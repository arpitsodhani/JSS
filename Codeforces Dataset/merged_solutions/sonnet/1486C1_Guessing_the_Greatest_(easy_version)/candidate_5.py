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
    two = ask(1, n)
    if two > 1 and ask(1, two) == two:
        floor_value = 1
        ceiling_value = two - 1
        while floor_value < ceiling_value:
            mid = (floor_value + ceiling_value + 1) // 2
            if ask(mid, two) == two:
                floor_value = mid
            else:
                ceiling_value = mid - 1
        return floor_value
    floor_value = two + 1
    ceiling_value = n
    while floor_value < ceiling_value:
        mid = (floor_value + ceiling_value) // 2
        if ask(two, mid) == two:
            ceiling_value = mid
        else:
            floor_value = mid + 1
    return floor_value


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    sys.stdout.write("! %d\n" % find_top(n))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
