# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from collections import deque

        data = sys.stdin.read().split()
        if not data:
            sys.exit()

        s = data[0]
        n = len(s)
        cnt = [0] * 6
        for ch in s:
            cnt[ord(ch) - 97] += 1

        allowed = [(1 << 6) - 1] * n
        i = 1
        while i < len(data):
            token = data[i]
            j = 0
            while j < len(token) and token[j].isalpha():
                j += 1
            letters = token[:j]
            pos_part = token[j:]

            if pos_part:
                pos = int(pos_part) - 1
                i += 1
            else:
                pos = int(data[i + 1]) - 1
                i += 2

            mask = 0
            for ch in letters:
                mask |= 1 << (ord(ch) - 97)
            allowed[pos] = mask

        groups = [[] for _ in range(64)]
        for idx, mask in enumerate(allowed):
            groups[mask].append(idx)

        need = [len(groups[m]) for m in range(64)]

        def feasible(extra_pos=-1, fixed_letter=-1):
            src = 70
            sink = 71
            graph = [[] for _ in range(72)]

            def add_edge(v, u, cap):
                graph[v].append([u, cap, len(graph[u])])
                graph[u].append([v, 0, len(graph[v]) - 1])

            left = cnt[:]
            req = need[:]

            if extra_pos != -1:
                m = allowed[extra_pos]
                req[m] -= 1
                left[fixed_letter] -= 1
                if left[fixed_letter] < 0 or not (m >> fixed_letter & 1):
                    return False

            total = 0
            for c in range(6):
                add_edge(src, c, left[c])
            for m in range(64):
                if req[m]:
                    node = 6 + m
                    total += req[m]
                    for c in range(6):
                        if m >> c & 1:
                            add_edge(c, node, 10**9)
                    add_edge(node, sink, req[m])

            flow = 0
            while True:
                level = [-1] * 72
                level[src] = 0
                q = deque([src])
                while q:
                    v = q.popleft()
                    for to, cap, _ in graph[v]:
                        if cap and level[to] == -1:
                            level[to] = level[v] + 1
                            q.append(to)
                if level[sink] == -1:
                    break

                it = [0] * 72

                def dfs(v, pushed):
                    if v == sink:
                        return pushed
                    while it[v] < len(graph[v]):
                        e = graph[v][it[v]]
                        if e[1] and level[e[0]] == level[v] + 1:
                            got = dfs(e[0], min(pushed, e[1]))
                            if got:
                                e[1] -= got
                                graph[e[0]][e[2]][1] += got
                                return got
                        it[v] += 1
                    return 0

                while True:
                    pushed = dfs(src, 10**9)
                    if not pushed:
                        break
                    flow += pushed

            return flow == total

        if not feasible():
            print("Impossible")
            sys.exit()

        ans = [''] * n
        for pos in range(n):
            m = allowed[pos]
            need[m] -= 1
            for c in range(6):
                if cnt[c] and (m >> c & 1) and feasible(pos, c):
                    ans[pos] = chr(97 + c)
                    cnt[c] -= 1
                    break

        print(''.join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
