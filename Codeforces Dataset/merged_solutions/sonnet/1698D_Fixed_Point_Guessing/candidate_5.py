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
    while low < high:
        mid = low + (high - low) // 2
        stayed = sum(1 for value in ask(low, mid) if low <= value <= mid)
        if stayed & 1:
            high = mid
        else:
            low = mid + 1
    return low


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    while cases:
        cases -= 1
        n = read_input()
        print("!", find_fixed(n))
        sys.stdout.flush()


if __name__ == "__main__":
    main()
