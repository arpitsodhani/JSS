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
        return "0" if k else s
    digits = list(s)
    budget = k
    if budget and digits[0] != "1":
        digits[0] = "1"
        budget -= 1
    for i, ch in enumerate(digits):
        if i == 0 or budget == 0:
            continue
        if ch != "0":
            digits[i] = "0"
            budget -= 1
    return "".join(digits)


# --- clause: main :: () -> None ---
def main():
    n, k, s = read_input()
    sys.stdout.write(smallest_value(n, k, s) + "\n")


if __name__ == "__main__":
    main()
