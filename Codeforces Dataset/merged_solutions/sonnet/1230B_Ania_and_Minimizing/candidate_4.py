import sys


# --- clause: read_input :: () -> tuple[int, int, str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    return n, k, data[2].decode()


# --- clause: smallest_value :: (n: int, k: int, s: str) -> str ---
def smallest_value(n, k, s):
    digits = list(s)
    left = k
    if n == 1:
        return "0" if left else s
    if left and digits[0] != "1":
        digits[0] = "1"
        left -= 1
    position = 1
    while left and position < n:
        if digits[position] != "0":
            digits[position] = "0"
            left -= 1
        position += 1
    return "".join(digits)


# --- clause: main :: () -> None ---
def main():
    n, k, s = read_input()
    sys.stdout.write(smallest_value(n, k, s) + "\n")


if __name__ == "__main__":
    main()
