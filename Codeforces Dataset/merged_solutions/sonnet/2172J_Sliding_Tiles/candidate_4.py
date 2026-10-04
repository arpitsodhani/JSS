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
    weight = [1] * n
    edge = list(range(n))
    filled = [1 if tiles[i] else 0 for i in range(n)]
    since = [1] * n
    delta = [0] * (n + 2)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def flush(root, row):
        span = row - since[root]
        if span and filled[root]:
            end = edge[root]
            delta[end - filled[root] + 1] += span
            delta[end + 1] -= span
        since[root] = row

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
                filled[root] -= 1
        for i in bar_at[row - 1]:
            left_root = find(i)
            right_root = find(i + 1)
            if left_root == right_root:
                continue
            flush(left_root, row)
            flush(right_root, row)
            total = filled[left_root] + filled[right_root]
            end = edge[right_root] if edge[right_root] > edge[left_root] else edge[left_root]
            if weight[left_root] < weight[right_root]:
                parent[left_root] = right_root
                left_root, right_root = right_root, left_root
            else:
                parent[right_root] = left_root
            weight[left_root] += weight[right_root]
            filled[left_root] = total
            edge[left_root] = end
            since[left_root] = row

    for i in range(n):
        if find(i) == i:
            flush(i, n + 1)

    answer = [0] * n
    running = 0
    for i in range(n):
        running += delta[i]
        answer[i] = running
    return answer

# --- clause: main :: () -> None ---
def main():
    n, tiles, bars = read_input()
    sys.stdout.write(" ".join(map(str, settle(n, tiles, bars))) + "\n")


if __name__ == "__main__":
    main()
