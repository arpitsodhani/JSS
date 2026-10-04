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
        if left:
            digits[0] = "0"
        return "".join(digits)
    if left and digits[0] != "1":
        digits[0] = "1"
        left -= 1
    for i in range(1, n):
        if left == 0:
            break
        if digits[i] != "0":
            digits[i] = "0"
            left -= 1
    return "".join(digits)


# --- clause: main :: () -> None ---
def main():
    n, k, s = read_input()
    sys.stdout.write(smallest_value(n, k, s) + "\n")


if __name__ == "__main__":
    main()
