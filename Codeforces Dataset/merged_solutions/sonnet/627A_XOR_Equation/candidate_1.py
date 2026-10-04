import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: count_pairs :: (s: int, x: int) -> int ---
def count_pairs(s, x):
    if s < x or (s - x) % 2:
        return 0
    carry = (s - x) // 2
    if carry & x:
        return 0
    total = 1 << bin(x).count("1")
    if carry == 0:
        total -= 2
    return total if total > 0 else 0


# --- clause: main :: () -> None ---
def main():
    s, x = read_input()
    sys.stdout.write(str(count_pairs(s, x)) + "\n")


if __name__ == "__main__":
    main()
