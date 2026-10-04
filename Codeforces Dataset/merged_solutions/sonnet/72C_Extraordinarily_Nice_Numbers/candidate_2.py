import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    x = int(data[0])
    return x


# --- clause: count_divisors :: (x: int) -> tuple[int, int] ---
def count_divisors(x):
    even = 0
    odd = 0
    for d in range(1, x + 1):
        if x % d == 0:
            if d % 2:
                odd += 1
            else:
                even += 1
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
    sys.stdout.write("%s\n" % verdict(even, odd))


if __name__ == "__main__":
    main()
