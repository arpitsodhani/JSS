import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    light = 0
    for weight in data[2:2 + n]:
        if weight == 50:
            light += 1
    return k, light, n - light

# Clause binomials [Confidence: 1.00]
def binomials(limit, mod):
    table = []
    for i in range(limit + 1):
        band = [1] * (i + 1)
        for j in range(1, i):
            band[j] = (table[i - 1][j - 1] + table[i - 1][j]) % mod
        table.append(band)
    return table

# Clause plan_rides [Confidence: 1.00]
def plan_rides(k, light, heavy):
    mod = 1000000007
    choose = binomials(max(light, heavy), mod)
    width = heavy + 1
    amount = 2 * (light + 1) * width
    dist = [-1] * amount
    ways = [0] * amount
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

# Clause main [Confidence: 1.00]
def main():
    k, light, heavy = read_input()
    rides, ways = plan_rides(k, light, heavy)
    sys.stdout.write("%d\n%d\n" % (rides, ways))


if __name__ == "__main__":
    main()

