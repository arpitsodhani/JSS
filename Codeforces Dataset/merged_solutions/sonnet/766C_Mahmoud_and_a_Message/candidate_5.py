import sys

MOD = 10 ** 9 + 7


# --- clause: read_input :: () -> tuple[int, str, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s = data[1].decode()
    limits = list(map(int, data[2:28]))
    return n, s, limits

# --- clause: reach :: (n: int, s: str, limits: list[int]) -> list[int] ---
def reach(n, s, limits):
    span = [0] * (n + 1)
    for end in range(1, n + 1):
        allowed = n
        best = 0
        for start in range(end, 0, -1):
            cap = limits[ord(s[start - 1]) - 97]
            if cap < allowed:
                allowed = cap
            if end - start + 1 > allowed:
                break
            best = end - start + 1
        span[end] = best
    return span

# --- clause: solve :: (n: int, s: str, limits: list[int]) -> tuple[int, int, int] ---
def solve(n, s, limits):
    span = reach(n, s, limits)
    ways = [0] * (n + 1)
    ways[0] = 1
    pieces = [0] * (n + 1)
    longest = 0
    for end in range(1, n + 1):
        limit = span[end]
        if limit > longest:
            longest = limit
        running = 0
        best_parts = n + 1
        length = 1
        while length <= limit:
            start = end - length
            running += ways[start]
            if pieces[start] + 1 < best_parts:
                best_parts = pieces[start] + 1
            length += 1
        ways[end] = running % MOD
        pieces[end] = best_parts
    return ways[n], longest, pieces[n]

# --- clause: main :: () -> None ---
def main():
    n, s, limits = read_input()
    total, longest, parts = solve(n, s, limits)
    sys.stdout.write("%d\n%d\n%d\n" % (total, longest, parts))


if __name__ == "__main__":
    main()
