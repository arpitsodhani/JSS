import sys

MOD = 998244353


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + n]
        pos += n
        cases.append((a, b))
    return cases

# --- clause: count_subsets :: (a: list[int], b: list[int]) -> int ---
def count_subsets(a, b):
    n = len(a)
    ways = [1, 1]
    pairs = [(a[i], b[i]) for i in range(n)]
    for i in range(1, n):
        prev_first, prev_second = pairs[i - 1]
        first, second = pairs[i]
        fresh = [0, 0]
        for state in (0, 1):
            count = ways[state]
            if count == 0:
                continue
            top = prev_first if state == 0 else prev_second
            bottom = prev_second if state == 0 else prev_first
            if top <= first and bottom <= second:
                fresh[0] = (fresh[0] + count) % MOD
            if top <= second and bottom <= first:
                fresh[1] = (fresh[1] + count) % MOD
        ways = fresh
    return (ways[0] + ways[1]) % MOD

# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        out.append(str(count_subsets(a, b)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
