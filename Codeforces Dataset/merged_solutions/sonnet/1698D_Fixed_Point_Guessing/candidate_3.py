import sys


# --- clause: read_input :: () -> int ---
def read_input():
    line = sys.stdin.readline()
    while line.strip() == "":
        line = sys.stdin.readline()
    return int(line)


# --- clause: ask :: (l: int, r: int) -> list[int] ---
def ask(l, r):
    sys.stdout.write("? " + str(l) + " " + str(r) + "\n")
    sys.stdout.flush()
    values = []
    while len(values) < r - l + 1:
        line = sys.stdin.readline()
        if not line:
            break
        for token in line.split():
            values.append(int(token))
    return values


# --- clause: find_fixed :: (n: int) -> int ---
def find_fixed(n):
    low = 1
    high = n
    while low != high:
        mid = (low + high) >> 1
        values = ask(low, mid)
        outside = 0
        for value in values:
            if value < low or value > mid:
                outside += 1
        width = mid - low + 1
        if (width - outside) % 2:
            high = mid
        else:
            low = mid + 1
    return low


# --- clause: main :: () -> None ---
def main():
    for _ in range(read_input()):
        n = read_input()
        answer = find_fixed(n)
        sys.stdout.write("! " + str(answer) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
