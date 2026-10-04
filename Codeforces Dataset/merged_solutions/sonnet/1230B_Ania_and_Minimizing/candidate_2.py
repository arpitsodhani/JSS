import sys


# --- clause: read_input :: () -> tuple[int, int, str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    return n, k, data[2].decode()


# --- clause: smallest_value :: (n: int, k: int, s: str) -> str ---
def smallest_value(n, k, s):
    if n == 1:
        return "0" if k >= 1 else s
    digits = bytearray(s, "ascii")
    budget = k
    if budget and digits[0] != 49:
        digits[0] = 49
        budget -= 1
    index = 1
    while index < n and budget:
        if digits[index] != 48:
            digits[index] = 48
            budget -= 1
        index += 1
    return digits.decode()


# --- clause: main :: () -> None ---
def main():
    n, k, s = read_input()
    sys.stdout.write(smallest_value(n, k, s) + "\n")


if __name__ == "__main__":
    main()
