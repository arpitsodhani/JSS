# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        import heapq

        def dijkstra(start, graph, n):
            inf = 10**30
            dist = [inf] * n
            parent = [-1] * n
            parent_edge = [-1] * n
            order = []
            dist[start] = 0
            heap = [(0, start)]

            while heap:
                du, u = heapq.heappop(heap)
                if du != dist[u]:
                    continue
                order.append(u)
                for v, w, eid in graph[u]:
                    nd = du + w
                    if nd < dist[v]:
                        dist[v] = nd
                        parent[v] = u
                        parent_edge[v] = eid
                        heapq.heappush(heap, (nd, v))

            return dist, parent, parent_edge, order

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            it = iter(data)

            n = next(it)
            m = next(it)
            q = next(it)

            edges = []
            graph = [[] for _ in range(n)]

            for i in range(m):
                u = next(it) - 1
                v = next(it) - 1
                w = next(it)
                edges.append((u, v, w))
                graph[u].append((v, w, i))
                graph[v].append((u, w, i))

            ds, parent, parent_edge, order = dijkstra(0, graph, n)
            dt, _, _, _ = dijkstra(n - 1, graph, n)

            path_vertices = []
            path_edges = []
            cur = n - 1

            while True:
                path_vertices.append(cur)
                if cur == 0:
                    break
                path_edges.append(parent_edge[cur])
                cur = parent[cur]

            path_vertices.reverse()
            path_edges.reverse()

            path_len = len(path_edges)
            pos = [-1] * n
            for i, v in enumerate(path_vertices):
                pos[v] = i

            edge_pos = [-1] * m
            for i, eid in enumerate(path_edges):
                edge_pos[eid] = i

            label = [-1] * n
            for u in order:
                if pos[u] != -1:
                    label[u] = pos[u]
                else:
                    label[u] = label[parent[u]]

            events = [[] for _ in range(path_len + 1)]

            for eid, (u, v, w) in enumerate(edges):
                if edge_pos[eid] != -1:
                    continue

                lu = label[u]
                lv = label[v]

                if lu < lv:
                    events[lu].append((ds[u] + w + dt[v], lv))
                elif lv < lu:
                    events[lv].append((ds[v] + w + dt[u], lu))

            inf = 10**30
            best = [inf] * path_len
            heap = []

            for i in range(path_len):
                for item in events[i]:
                    heapq.heappush(heap, item)

                while heap and heap[0][1] <= i:
                    heapq.heappop(heap)

                if heap:
                    best[i] = heap[0][0]

            original = ds[n - 1]
            ans = []

            for _ in range(q):
                eid = next(it) - 1
                x = next(it)
                u, v, _ = edges[eid]

                through = min(ds[u] + x + dt[v], ds[v] + x + dt[u])
                p = edge_pos[eid]

                if p == -1:
                    ans.append(str(min(original, through)))
                else:
                    ans.append(str(min(best[p], through)))

            sys.stdout.write("\n".join(ans))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
