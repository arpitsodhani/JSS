import sys

MOD = 998244353


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [int(token) for token in data[1:n + 1]]
    return n, values


# --- clause: weighted_xor :: (n: int, values: list[int]) -> int ---
def weighted_xor(n, values):
    total = 0
    for bit in range(30):
        weight = 1 << bit
        count = [1, 0]
        index_sum = [0, 0]
        running = 0
        subtotal = 0
        for r in range(1, n + 1):
            running ^= (values[r - 1] >> bit) & 1
            other = running ^ 1
            subtotal += count[other] * r - index_sum[other]
            count[running] += 1
            index_sum[running] += r
        total = (total + (subtotal % MOD) * weight) % MOD
    return total % MOD


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    sys.stdout.write(str(weighted_xor(n, values)) + "\n")


if __name__ == "__main__":
    main()
