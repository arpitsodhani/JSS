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
    plain = 1
    flipped = 1
    for i in range(1, n):
        stay = 0
        turn = 0
        if a[i - 1] <= a[i] and b[i - 1] <= b[i]:
            stay += plain
            turn += flipped
        if b[i - 1] <= a[i] and a[i - 1] <= b[i]:
            stay += flipped
            turn += plain
        plain = stay % MOD
        flipped = turn % MOD
    return (plain + flipped) % MOD

# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        out.append(str(count_subsets(a, b)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
