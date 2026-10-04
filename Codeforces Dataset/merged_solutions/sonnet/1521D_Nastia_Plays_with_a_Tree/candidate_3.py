# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def run_solution():
    import sys

    def main():
        data = sys.stdin.buffer.read().split()
        idx = 0
        t = int(data[idx])
        idx += 1
        out = []
    
        for _ in range(t):
            n = int(data[idx])
            idx += 1
        
            adj = [[] for _ in range(n + 1)]
            edges = []
            for _ in range(n - 1):
                u = int(data[idx])
                v = int(data[idx + 1])
                idx += 2
                adj[u].append(v)
                adj[v].append(u)
                edges.append((u, v))
        
            parent = [0] * (n + 1)
            order = [1]
            for v in order:
                for to in adj[v]:
                    if to != parent[v]:
                        parent[to] = v
                        order.append(to)
        
            dp0 = [0] * (n + 1)
            dp1 = [0] * (n + 1)
        
            for v in reversed(order):
                base = 0
                gains = []
                for to in adj[v]:
                    if parent[to] == v:
                        base += dp0[to]
                        gains.append(1 + dp1[to] - dp0[to])
            
                gains.sort(reverse=True)
                dp0[v] = base + sum(g for g in gains[:2] if g > 0)
                dp1[v] = base + (gains[0] if gains and gains[0] > 0 else 0)
        
            keep = set()
        
            def restore(v, has_parent):
                limit = 1 if has_parent else 2
                choices = []
                for to in adj[v]:
                    if parent[to] == v:
                        gain = 1 + dp1[to] - dp0[to]
                        choices.append((gain, to))
            
                choices.sort(reverse=True)
                chosen = set()
                for gain, to in choices[:limit]:
                    if gain > 0:
                        chosen.add(to)
                        keep.add((min(v, to), max(v, to)))
            
                for to in adj[v]:
                    if parent[to] == v:
                        restore(to, to in chosen)
        
            restore(1, False)
        
            removed = []
            kept_adj = [[] for _ in range(n + 1)]
            for u, v in edges:
                key = (min(u, v), max(u, v))
                if key in keep:
                    kept_adj[u].append(v)
                    kept_adj[v].append(u)
                else:
                    removed.append((u, v))
        
            seen = [False] * (n + 1)
            endpoints = []
        
            for start in range(1, n + 1):
                if seen[start]:
                    continue
            
                stack = [start]
                seen[start] = True
                comp = []
            
                while stack:
                    v = stack.pop()
                    comp.append(v)
                    for to in kept_adj[v]:
                        if not seen[to]:
                            seen[to] = True
                            stack.append(to)
            
                ends = [v for v in comp if len(kept_adj[v]) <= 1]
                endpoints.append((ends[0], ends[-1]))
        
            out.append(str(len(removed)))
            for i, (u, v) in enumerate(removed):
                a = endpoints[i][0]
                b = endpoints[i + 1][0]
                endpoints[i + 1] = (endpoints[i][1], endpoints[i + 1][1])
                out.append(f"{u} {v} {a} {b}")
    
        print("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    run_solution()
