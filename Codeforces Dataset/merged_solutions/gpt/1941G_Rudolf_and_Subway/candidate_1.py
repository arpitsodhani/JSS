# CLAUSE: setup_environment
import sys
from collections import deque, defaultdict

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    t = next(it)
    ans = []

    for _ in range(t):
        n = next(it)
        m = next(it)

        station_colors = [[] for _ in range(n + 1)]
        color_stations = defaultdict(list)

        for _ in range(m):
            u = next(it)
            v = next(it)
            c = next(it)
            station_colors[u].append(c)
            station_colors[v].append(c)
            color_stations[c].append(u)
            color_stations[c].append(v)

        s = next(it)
        f = next(it)

        if s == f:
            ans.append("0")
            continue

        dist = [-1] * (n + 1)
        dist[s] = 0
        q = deque([s])
        used_colors = set()

        while q:
            v = q.popleft()
            if v == f:
                break

            for c in station_colors[v]:
                if c in used_colors:
                    continue
                used_colors.add(c)
                nd = dist[v] + 1

                for u in color_stations[c]:
                    if dist[u] == -1:
                        dist[u] = nd
                        q.append(u)

        ans.append(str(dist[f]))

    print("\n".join(ans))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
