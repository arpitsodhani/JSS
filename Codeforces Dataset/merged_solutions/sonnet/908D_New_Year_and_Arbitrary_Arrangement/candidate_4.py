import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    values = list(map(int, data[:3]))
    return values[0], values[1], values[2]


# --- clause: expected_pairs :: (k: int, pa: int, pb: int) -> int ---
def expected_pairs(k, pa, pb):
    inv = pow(pa + pb, MOD - 2, MOD)
    add_a = pa * inv % MOD
    add_b = pb * inv % MOD
    tail = pa * pow(pb, MOD - 2, MOD) % MOD
    dp = [[0] * (k + 1) for _ in range(k + 1)]
    for i in range(k, 0, -1):
        for j in range(k, -1, -1):
            if i + j >= k:
                dp[i][j] = (i + j + tail) % MOD
            else:
                nxt = dp[i + 1][j] if i + 1 <= k else 0
                dp[i][j] = (add_a * nxt + add_b * dp[i][j + i]) % MOD
    return dp[1][0]


# --- clause: main :: () -> None ---
def main():
    k, pa, pb = read_input()
    answer = expected_pairs(k, pa, pb)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
