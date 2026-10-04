import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    k, pa, pb = int(data[0]), int(data[1]), int(data[2])
    return k, pa, pb


# --- clause: expected_pairs :: (k: int, pa: int, pb: int) -> int ---
def expected_pairs(k, pa, pb):
    inv = pow(pa + pb, MOD - 2, MOD)
    add_a = inv * pa % MOD
    add_b = inv * pb % MOD
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
    sys.stdout.write("%d\n" % expected_pairs(k, pa, pb))


if __name__ == "__main__":
    main()
