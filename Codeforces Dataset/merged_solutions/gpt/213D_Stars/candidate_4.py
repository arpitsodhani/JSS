# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    import math

    def main():
        data = sys.stdin.read().strip().split()
        if not data:
            return
        n = int(data[0])

        points = []
        for i in range(n + 1):
            points.append((10.0 * i, 0.0))

        c72 = math.cos(2.0 * math.pi / 5.0)
        s72 = math.sin(2.0 * math.pi / 5.0)
        c144 = math.cos(4.0 * math.pi / 5.0)
        s144 = math.sin(4.0 * math.pi / 5.0)
        c216 = math.cos(6.0 * math.pi / 5.0)
        s216 = math.sin(6.0 * math.pi / 5.0)

        stars = []
        edges = []

        for i in range(n):
            sign = 1.0 if i % 2 == 0 else -1.0
            x = 10.0 * i

            a = i + 1
            b = i + 2

            cx = x + 10.0 + 10.0 * c72
            cy = sign * 10.0 * s72
            dx = cx + 10.0 * c144
            dy = cy + sign * 10.0 * s144
            ex = dx + 10.0 * c216
            ey = dy + sign * 10.0 * s216

            c = len(points) + 1
            points.append((cx, cy))
            d = len(points) + 1
            points.append((dx, dy))
            e = len(points) + 1
            points.append((ex, ey))

            star = [a, b, c, d, e]
            stars.append(star)

            cycle = [a, c, e, b, d, a]
            for j in range(5):
                edges.append((cycle[j], cycle[j + 1]))

        m = len(points)
        adj = [[] for _ in range(m + 1)]
        for idx, (u, v) in enumerate(edges):
            adj[u].append((v, idx))
            adj[v].append((u, idx))

        used = [False] * len(edges)
        stack = [1]
        path = []

        while stack:
            v = stack[-1]
            while adj[v] and used[adj[v][-1][1]]:
                adj[v].pop()
            if not adj[v]:
                path.append(stack.pop())
            else:
                to, eid = adj[v].pop()
                if not used[eid]:
                    used[eid] = True
                    stack.append(to)

        path.reverse()

        out = [str(m)]
        for x, y in points:
            out.append(f"{x:.15f} {y:.15f}")
        for star in stars:
            out.append(" ".join(map(str, star)))
        out.append(" ".join(map(str, path)))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
