import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    return raw[0].decode(), raw[1].decode()


# --- clause: last_ends :: (s: str, t: str) -> list[int] ---
def last_ends(s, t):
    n = len(s)
    width = len(t)
    joined = t + "#" + s
    fail = [0] * len(joined)
    for i in range(1, len(joined)):
        advance = fail[i - 1]
        while advance and joined[i] != joined[advance]:
            advance = fail[advance - 1]
        if joined[i] == joined[advance]:
            advance += 1
        fail[i] = advance
    ends = [0] * (n + 1)
    last = 0
    for i in range(n):
        spot = width + 1 + i
        if fail[spot] == width:
            last = i + 1
        ends[i + 1] = last
    return ends


# --- clause: count_ways :: (s: str, t: str, ends: list[int]) -> int ---
def count_ways(s, t, ends):
    mod = 1000000007
    n = len(s)
    width = len(t)
    dp = [0] * (n + 1)
    prefix = [0] * (n + 2)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        stop = ends[i]
        if stop >= width:
            reach = stop - width
            dp[i] = (dp[i] + prefix[reach] + reach + 1) % mod
        prefix[i] = (prefix[i - 1] + dp[i]) % mod
    return dp[n] % mod


# --- clause: main :: () -> None ---
def main():
    s, t = read_input()
    sys.stdout.write("%d\n" % count_ways(s, t, last_ends(s, t)))


if __name__ == "__main__":
    main()
