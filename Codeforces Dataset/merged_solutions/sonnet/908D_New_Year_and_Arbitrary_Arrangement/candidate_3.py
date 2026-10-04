import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1]), int(data[2])


# --- clause: expected_pairs :: (k: int, pa: int, pb: int) -> int ---
def expected_pairs(k, pa, pb):
    inv = pow(pa + pb, MOD - 2, MOD)
    add_a = pa * inv % MOD
    add_b = pb * inv % MOD
    tail = pa * pow(pb, MOD - 2, MOD) % MOD
    dp = [[0] * (k + 1) for _ in range(k + 2)]
    i = k
    while i >= 1:
        row = dp[i]
        above = dp[i + 1]
        j = k
        while j >= 0:
            if i + j >= k:
                row[j] = (i + j + tail) % MOD
            else:
                row[j] = (add_a * above[j] + add_b * row[j + i]) % MOD
            j -= 1
        i -= 1
    return dp[1][0]


# --- clause: main :: () -> None ---
def main():
    k, pa, pb = read_input()
    print(expected_pairs(k, pa, pb))


if __name__ == "__main__":
    main()
