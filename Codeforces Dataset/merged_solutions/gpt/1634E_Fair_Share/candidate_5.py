# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def main():
            input = sys.stdin.readline

            m = int(input())
            arrays = []
            value_count = {}
            value_id = {}
            edges_u = []
            edges_v = []
            edge_pos = []

            for i in range(m):
                n = int(input())
                a = list(map(int, input().split()))
                arrays.append(a)
                for j, x in enumerate(a):
                    value_count[x] = value_count.get(x, 0) + 1
                    if x not in value_id:
                        value_id[x] = len(value_id)

            for c in value_count.values():
                if c % 2:
                    print("NO")
                    return

            total_vertices = m + len(value_id)
            adj = [[] for _ in range(total_vertices)]

            eid = 0
            for i, a in enumerate(arrays):
                for j, x in enumerate(a):
                    v = m + value_id[x]
                    edges_u.append(i)
                    edges_v.append(v)
                    edge_pos.append((i, j))
                    adj[i].append(eid)
                    adj[v].append(eid)
                    eid += 1

            used = [False] * eid
            color = [0] * eid

            for start in range(total_vertices):
                while adj[start]:
                    e0 = adj[start].pop()
                    if used[e0]:
                        continue

                    stack = [(start, -1)]
                    cur = edges_u[e0] ^ edges_v[e0] ^ start
                    used[e0] = True
                    stack.append((cur, e0))
                    tour = []

                    while stack:
                        v, in_edge = stack[-1]
                        while adj[v] and used[adj[v][-1]]:
                            adj[v].pop()
                        if adj[v]:
                            e = adj[v].pop()
                            used[e] = True
                            to = edges_u[e] ^ edges_v[e] ^ v
                            stack.append((to, e))
                        else:
                            stack.pop()
                            if in_edge != -1:
                                tour.append(in_edge)

                    for idx, e in enumerate(tour):
                        color[e] = idx & 1

            ans = [[""] * len(a) for a in arrays]
            for e, (i, j) in enumerate(edge_pos):
                ans[i][j] = "L" if color[e] else "R"

            print("YES")
            print("\n".join("".join(row) for row in ans))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
