import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: count_pairs :: (s: int, x: int) -> int ---
def count_pairs(s, x):
    diff = s - x
    if diff < 0 or diff % 2:
        return 0
    carry = diff >> 1
    if carry & x:
        return 0
    bits = bin(x).count("1")
    answer = 1 << bits
    if not carry:
        answer -= 2
    return max(answer, 0)

# --- clause: main :: () -> None ---
def main():
    s, x = read_input()
    sys.stdout.write(str(count_pairs(s, x)) + "\n")


if __name__ == "__main__":
    main()
