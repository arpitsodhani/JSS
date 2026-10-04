import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [int(token) for token in data[1:n + 1]]
    return n, values

# Clause tree_query [Confidence: 1.00]
def tree_query(tree, index):
    total = 0
    while index > 0:
        total += tree[index]
        index -= index & -index
    return total

# Clause count_takes [Confidence: 1.00]
def count_takes(n, values):
    tree = [0] * (n + 1)
    for i in range(1, n + 1):
        tree[i] += 1
        parent = i + (i & -i)
        if parent <= n:
            tree[parent] += tree[i]
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
        cur = nxt if nxt < n else 0
    return takes

# Clause main [Confidence: 1.00]
def main():
    n, values = read_input()
    sys.stdout.write(str(count_takes(n, values)) + "\n")


if __name__ == "__main__":
    main()

