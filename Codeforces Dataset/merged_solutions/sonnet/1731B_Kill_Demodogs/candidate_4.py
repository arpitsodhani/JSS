import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: best_kills :: (n: int) -> int ---
def best_kills(n):
    mod = 1000000007
    a = n % mod
    b = (n + 1) % mod
    c = (2 * n + 1) % mod
    d = (n - 1) % mod
    inverse = pow(6, mod - 2, mod)
    total = a * b % mod * c % mod
    total = (total + 2 * (d * a % mod * b % mod)) % mod
    return total * inverse % mod * 2022 % mod


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n in read_input():
        pieces.append(best_kills(n))
    sys.stdout.write("\n".join(map(str, pieces)) + "\n")


if __name__ == "__main__":
    main()
