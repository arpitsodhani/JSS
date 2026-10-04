import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = tokens[cursor]
        cursor += 1
        cases.append(tokens[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: fewest_inversions :: (a: list[int]) -> int ---
def fewest_inversions(a):
    order = sorted(set(a))
    rank = {}
    for i in range(len(order)):
        rank[order[i]] = i + 1
    size = len(order) + 1
    tree = [0] * (size + 1)
    total = 0
    placed = 0
    for value in a:
        at = rank[value]
        smaller = 0
        i = at - 1
        while i > 0:
            smaller += tree[i]
            i -= i & (-i)
        same = 0
        i = at
        while i > 0:
            same += tree[i]
            i -= i & (-i)
        bigger = placed - same
        total += smaller if smaller < bigger else bigger
        i = at
        while i <= size:
            tree[i] += 1
            i += i & (-i)
        placed += 1
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(fewest_inversions(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
