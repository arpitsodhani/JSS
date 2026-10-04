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
    keep = 1
    swap = 1
    for i in range(1, n):
        prev_keep = keep
        prev_swap = swap
        keep = 0
        swap = 0
        if a[i - 1] <= a[i] and b[i - 1] <= b[i]:
            keep += prev_keep
            swap += prev_swap
        if b[i - 1] <= a[i] and a[i - 1] <= b[i]:
            keep += prev_swap
            swap += prev_keep
        keep %= MOD
        swap %= MOD
    return (keep + swap) % MOD

# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        out.append(str(count_subsets(a, b)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
