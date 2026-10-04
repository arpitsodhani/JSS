import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [int(token) for token in data[1:n + 1]]
    return n, values


# --- clause: tree_query :: (tree: list[int], index: int) -> int ---
def tree_query(tree, index):
    total = 0
    while index > 0:
        total += tree[index]
        index -= index & -index
    return total


# --- clause: count_takes :: (n: int, values: list[int]) -> int ---
def count_takes(n, values):
    tree = [0] * (n + 1)
    for i in range(1, n + 1):
        tree[i] = i & -i
    where = {}
    for i in range(n):
        where.setdefault(values[i], []).append(i)
    cur = 0
    takes = 0
    for value in sorted(where):
        spots = where[value]
        ahead = [p for p in spots if p >= cur]
        behind = [p for p in spots if p < cur]
        if ahead and not behind:
            takes += tree_query(tree, ahead[-1] + 1) - tree_query(tree, cur)
            nxt = ahead[-1] + 1
        elif ahead:
            takes += tree_query(tree, n) - tree_query(tree, cur)
            for p in ahead:
                index = p + 1
                while index <= n:
                    tree[index] -= 1
                    index += index & -index
            ahead = []
            takes += tree_query(tree, behind[-1] + 1)
            nxt = behind[-1] + 1
        else:
            takes += tree_query(tree, n) - tree_query(tree, cur)
            takes += tree_query(tree, behind[-1] + 1)
            nxt = behind[-1] + 1
        for p in ahead + behind:
            index = p + 1
            while index <= n:
                tree[index] -= 1
                index += index & -index
        cur = nxt
        if cur >= n:
            cur = 0
    return takes


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    sys.stdout.write(str(count_takes(n, values)) + "\n")


if __name__ == "__main__":
    main()
