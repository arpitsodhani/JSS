import sys


# --- clause: read_input :: () -> int ---
def read_input():
    line = sys.stdin.readline()
    while line.strip() == "":
        line = sys.stdin.readline()
    return int(line)


# --- clause: ask :: (l: int, r: int) -> list[int] ---
def ask(l, r):
    print("?", l, r)
    sys.stdout.flush()
    need = r - l + 1
    values = []
    while len(values) < need:
        chunk = sys.stdin.readline().split()
        if not chunk:
            break
        values.extend(int(token) for token in chunk)
    return values


# --- clause: find_fixed :: (n: int) -> int ---
def find_fixed(n):
    low = 1
    high = n
    while low < high:
        mid = (low + high) // 2
        values = ask(low, mid)
        inside = 0
        for value in values:
            if low <= value <= mid:
                inside += 1
        if inside % 2 == 1:
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
