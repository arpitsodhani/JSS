import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return numbers[0].decode(), numbers[1].decode()


# --- clause: last_ends :: (s: str, t: str) -> list[int] ---
def last_ends(s, t):
    n = len(s)
    size = len(t)
    joined = t + "#" + s
    fail = [0] * len(joined)
    for i in range(1, len(joined)):
        jump = fail[i - 1]
        while jump and joined[i] != joined[jump]:
            jump = fail[jump - 1]
        if joined[i] == joined[jump]:
            jump += 1
        fail[i] = jump
    ends = [0 for _ in range(n + 1)]
    last = 0
    for i in range(n):
        spot = size + 1 + i
        if fail[spot] == size:
            last = i + 1
        ends[i + 1] = last
    return ends


# --- clause: count_ways :: (s: str, t: str, ends: list[int]) -> int ---
def count_ways(s, t, ends):
    mod = 1000000007
    n = len(s)
    size = len(t)
    dp = [0] * (n + 1)
    prefix = [0] * (n + 2)
    spot = 1
    while spot <= n:
        value = dp[spot - 1]
        stop = ends[spot]
        if stop >= size:
            reach = stop - size
            value += prefix[reach] + reach + 1
        dp[spot] = value % mod
        prefix[spot] = (prefix[spot - 1] + dp[spot]) % mod
        spot += 1
    return dp[n] % mod


# --- clause: main :: () -> None ---
def main():
    s, t = read_input()
    sys.stdout.write("%d\n" % count_ways(s, t, last_ends(s, t)))


if __name__ == "__main__":
    main()
