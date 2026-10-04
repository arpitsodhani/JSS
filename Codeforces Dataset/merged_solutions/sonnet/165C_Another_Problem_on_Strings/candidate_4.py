import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return int(numbers[0]), numbers[1].decode()


# --- clause: count_substrings :: (k: int, s: str) -> int ---
def count_substrings(k, s):
    spots = [-1]
    for i in range(len(s)):
        if s[i] == "1":
            spots.append(i)
    spots.append(len(s))
    ones = len(spots) - 2
    total = 0
    if k == 0:
        for i in range(len(spots) - 1):
            gap = spots[i + 1] - spots[i] - 1
            total += gap * (gap + 1) // 2
        return total
    for start in range(1, ones - k + 2):
        left = spots[start] - spots[start - 1]
        stop = spots[start + k] - spots[start + k - 1]
        total += left * stop
    return total


# --- clause: main :: () -> None ---
def main():
    k, s = read_input()
    sys.stdout.write("%d\n" % count_substrings(k, s))


if __name__ == "__main__":
    main()
