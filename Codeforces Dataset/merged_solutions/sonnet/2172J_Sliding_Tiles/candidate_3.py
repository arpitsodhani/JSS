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
    count = [0] * n
    for i in range(n):
        if tiles[i]:
            count[i] = 1
    start = [1] * n
    diff = [0] * (n + 2)
    bar_at = [[] for _ in range(n)]
    for i, height in enumerate(bars):
        bar_at[height].append(i)
    leaves_at = [[] for _ in range(n + 1)]
    for i, height in enumerate(tiles):
        leaves_at[height].append(i)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def settle_up_to(root, row):
        span = row - start[root]
        if span and count[root]:
            diff[root - count[root] + 1] += span
            diff[root + 1] -= span
        start[root] = row

    for row in range(1, n + 1):
        for i in leaves_at[row - 1]:
            if row == 1:
                continue
            root = find(i)
            settle_up_to(root, row)
            count[root] -= 1
        for i in bar_at[row - 1]:
            head = find(i)
            tail = find(i + 1)
            if head == tail:
                continue
            settle_up_to(head, row)
            settle_up_to(tail, row)
            parent[head] = tail
            count[tail] += count[head]

    for root in range(n):
        if parent[root] == root:
            settle_up_to(root, n + 1)

    result = []
    running = 0
    for i in range(n):
        running += diff[i]
        result.append(running)
    return result

# --- clause: main :: () -> None ---
def main():
    n, tiles, bars = read_input()
    sys.stdout.write(" ".join(map(str, settle(n, tiles, bars))) + "\n")


if __name__ == "__main__":
    main()
