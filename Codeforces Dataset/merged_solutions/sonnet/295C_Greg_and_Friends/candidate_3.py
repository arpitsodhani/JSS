import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    k = fields[1]
    light = 0
    for weight in fields[2:2 + n]:
        if weight == 50:
            light += 1
    return k, light, n - light


# --- clause: binomials :: (limit: int, mod: int) -> list[list[int]] ---
def binomials(limit, mod):
    table = []
    for i in range(limit + 1):
        entry_row = [1] * (i + 1)
        for j in range(1, i):
            entry_row[j] = (table[i - 1][j - 1] + table[i - 1][j]) % mod
        table.append(entry_row)
    return table


# --- clause: plan_rides :: (k: int, light: int, heavy: int) -> tuple[int, int] ---
def plan_rides(k, light, heavy):
    mod = 1000000007
    choose = binomials(max(light, heavy), mod)
    width = heavy + 1
    summed = 2 * (light + 1) * width
    dist = [-1] * summed
    ways = [0] * summed
    start = (light * width + heavy) * 2
    dist[start] = 0
    ways[start] = 1
    queue = [start]
    head = 0
    while head < len(queue):
        state = queue[head]
        head += 1
        side = state & 1
        rest = state >> 1
        a = rest // width
        b = rest % width
        here = ways[state]
        if side == 0:
            pool_light = a
            pool_heavy = b
        else:
            pool_light = light - a
            pool_heavy = heavy - b
        for i in range(pool_light + 1):
            for j in range(pool_heavy + 1):
                if i + j == 0 or 50 * i + 100 * j > k:
                    continue
                if side == 0:
                    nxt = ((a - i) * width + (b - j)) * 2 + 1
                else:
                    nxt = ((a + i) * width + (b + j)) * 2
                moves = here * choose[pool_light][i] % mod * choose[pool_heavy][j] % mod
                if dist[nxt] < 0:
                    dist[nxt] = dist[state] + 1
                    ways[nxt] = moves
                    queue.append(nxt)
                elif dist[nxt] == dist[state] + 1:
                    ways[nxt] = (ways[nxt] + moves) % mod
    goal = 1
    if dist[goal] < 0:
        return -1, 0
    return dist[goal], ways[goal] % mod


# --- clause: main :: () -> None ---
def main():
    k, light, heavy = read_input()
    rides, ways = plan_rides(k, light, heavy)
    sys.stdout.write("%d\n%d\n" % (rides, ways))


if __name__ == "__main__":
    main()
