import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: count_crossings :: (a: list[int]) -> int ---
def count_crossings(a):
    n = len(a)
    tree = [0] * (n + 2)
    total = 0
    for index in range(n - 1, -1, -1):
        spot = a[index]
        while spot > 0:
            total += tree[spot]
            spot -= spot & -spot
        spot = a[index]
        while spot <= n:
            tree[spot] += 1
            spot += spot & -spot
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(count_crossings(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
