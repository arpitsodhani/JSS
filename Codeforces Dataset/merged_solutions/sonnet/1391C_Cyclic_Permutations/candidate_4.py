import sys

MOD = 10 ** 9 + 7


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: cyclic_count :: (n: int) -> int ---
def cyclic_count(n):
    factorial = 1
    for value in range(2, n + 1):
        factorial = factorial * value % MOD
    power = 1
    for _ in range(n - 1):
        power = power * 2 % MOD
    return (factorial - power) % MOD

# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(cyclic_count(read_input())) + "\n")


if __name__ == "__main__":
    main()
