import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0])


# --- clause: count_divisors :: (x: int) -> tuple[int, int] ---
def count_divisors(x):
    even = 0
    odd = 0
    for d in range(1, x + 1):
        if x % d == 0:
            if d % 2 == 0:
                even += 1
            else:
                odd += 1
    return even, odd


# --- clause: verdict :: (even: int, odd: int) -> str ---
def verdict(even, odd):
    if even == odd:
        return "yes"
    return "no"


# --- clause: main :: () -> None ---
def main():
    x = read_input()
    even, odd = count_divisors(x)
    sys.stdout.write(verdict(even, odd) + "\n")


if __name__ == "__main__":
    main()
