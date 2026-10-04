import sys


# --- clause: read_input :: () -> tuple[int, list[int], str, list[tuple[int, int]]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    n = int(fields[0])
    m = int(fields[1])
    parent = [0, 0] + [int(v) for v in fields[2:1 + n]]
    letters = fields[1 + n].decode()
    queries = []
    cursor = 2 + n
    for i in range(m):
        queries.append((int(fields[cursor + 2 * i]), int(fields[cursor + 1 + 2 * i])))
    return n, parent, letters, queries


# --- clause: euler_walk :: (n: int, parent: list[int]) -> tuple[list[int], list[int], list[int]] ---
def euler_walk(n, parent):
    children = [[] for _ in range(n + 1)]
    for v in range(2, n + 1):
        children[parent[v]].append(v)
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    depth = [0] * (n + 1)
    depth[1] = 1
    timer = 0
    stack = [(1, 0)]
    while stack:
        v, state = stack.pop()
        if state:
            tout[v] = timer
            continue
        timer += 1
        tin[v] = timer
        stack.append((v, 1))
        for u in children[v]:
            depth[u] = depth[v] + 1
            stack.append((u, 0))
    return tin, tout, depth


# --- clause: depth_tables :: (n: int, letters: str, tin: list[int], depth: list[int]) -> tuple[list[list[int]], list[list[int]]] ---
def depth_tables(n, letters, tin, depth):
    top = max(depth)
    spots = [[] for _ in range(top + 1)]
    for v in range(1, n + 1):
        spots[depth[v]].append((tin[v], 1 << (ord(letters[v - 1]) - 97)))
    times = [[] for _ in range(top + 1)]
    masks = [[] for _ in range(top + 1)]
    for level in range(1, top + 1):
        spots[level].sort()
        rolling = 0
        masks[level].append(0)
        for moment, bit in spots[level]:
            times[level].append(moment)
            rolling ^= bit
            masks[level].append(rolling)
    return times, masks


# --- clause: answer_queries :: (queries: list[tuple[int, int]], tin: list[int], tout: list[int], times: list[list[int]], masks: list[list[int]]) -> list[str] ---
def answer_queries(queries, tin, tout, times, masks):
    out = []
    for v, h in queries:
        if h >= len(times) or not times[h]:
            out.append("Yes")
            continue
        row = times[h]
        low = 0
        high = len(row)
        target = tin[v]
        while low < high:
            mid = (low + high) // 2
            if row[mid] < target:
                low = mid + 1
            else:
                high = mid
        left = low
        low = 0
        high = len(row)
        target = tout[v]
        while low < high:
            mid = (low + high) // 2
            if row[mid] <= target:
                low = mid + 1
            else:
                high = mid
        right = low
        mask = masks[h][right] ^ masks[h][left]
        out.append("Yes" if mask & (mask - 1) == 0 else "No")
    return out


# --- clause: main :: () -> None ---
def main():
    n, parent, letters, queries = read_input()
    tin, tout, depth = euler_walk(n, parent)
    times, masks = depth_tables(n, letters, tin, depth)
    sys.stdout.write("\n".join(answer_queries(queries, tin, tout, times, masks)) + "\n")


if __name__ == "__main__":
    main()
