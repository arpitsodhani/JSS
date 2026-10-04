import sys

MOD = 10 ** 9 + 7


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: cyclic_count :: (n: int) -> int ---
def cyclic_count(n):
    total = 1
    for value in range(2, n + 1):
        total = total * value % MOD
    return (total - pow(2, n - 1, MOD)) % MOD


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(cyclic_count(read_input())) + "\n")


if __name__ == "__main__":
    main()
