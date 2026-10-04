import sys


# --- clause: read_input :: () -> tuple[int, list[int], list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    tiles = list(map(int, data[1:1 + n]))
    bars = list(map(int, data[1 + n:2 * n]))
    return n, tiles, bars


# --- clause: settle :: (n: int, tiles: list[int], bars: list[int]) -> list[int] ---
def settle(n, tiles, bars):
    parent = list(range(n))
    rank = [1] * n
    right = list(range(n))
    count = [1 if tiles[i] else 0 for i in range(n)]
    start = [1] * n
    diff = [0] * (n + 2)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def flush(root, row):
        span = row - start[root]
        if span and count[root]:
            end = right[root]
            diff[end - count[root] + 1] += span
            diff[end + 1] -= span
        start[root] = row

    bar_at = [[] for _ in range(n)]
    for i in range(n - 1):
        bar_at[bars[i]].append(i)
    leaves_at = [[] for _ in range(n + 1)]
    for i in range(n):
        leaves_at[tiles[i]].append(i)

    for row in range(1, n + 1):
        if row > 1:
            for i in leaves_at[row - 1]:
                root = find(i)
                flush(root, row)
                count[root] -= 1
        for i in bar_at[row - 1]:
            left_root = find(i)
            right_root = find(i + 1)
            if left_root == right_root:
                continue
            flush(left_root, row)
            flush(right_root, row)
            merged = count[left_root] + count[right_root]
            edge = right[left_root] if right[left_root] > right[right_root] else right[right_root]
            if rank[left_root] < rank[right_root]:
                parent[left_root] = right_root
                left_root, right_root = right_root, left_root
            else:
                parent[right_root] = left_root
            rank[left_root] += rank[right_root]
            count[left_root] = merged
            right[left_root] = edge
            start[left_root] = row

    for i in range(n):
        if find(i) == i:
            flush(i, n + 1)

    result = [0] * n
    running = 0
    for i in range(n):
        running += diff[i]
        result[i] = running
    return result


# --- clause: main :: () -> None ---
def main():
    n, tiles, bars = read_input()
    sys.stdout.write(" ".join(map(str, settle(n, tiles, bars))) + "\n")


if __name__ == "__main__":
    main()
