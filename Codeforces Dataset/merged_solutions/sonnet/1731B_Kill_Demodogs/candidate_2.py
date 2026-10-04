import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: best_kills :: (n: int) -> int ---
def best_kills(n):
    mod = 1000000007
    six = pow(6, mod - 2, mod)
    squares = n % mod * ((n + 1) % mod) % mod * ((2 * n + 1) % mod) % mod * six % mod
    steps = (n - 1) % mod * (n % mod) % mod * ((n + 1) % mod) % mod * pow(3, mod - 2, mod) % mod
    return (squares + steps) % mod * 2022 % mod


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n in read_input():
        lines.append(best_kills(n))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()
