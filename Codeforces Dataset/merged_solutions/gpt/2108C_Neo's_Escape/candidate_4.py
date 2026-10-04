# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def solve():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        t = data[0]
        idx = 1
        out = []

        for _ in range(t):
            n = data[idx]
            idx += 1
            a = data[idx:idx + n]
            idx += n

            order = sorted(range(n), key=lambda i: -a[i])
            parent = list(range(n))
            size = [1] * n
            active = [False] * n
            has_clone = [False] * n

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            def union(x, y):
                rx = find(x)
                ry = find(y)
                if rx == ry:
                    return
                if size[rx] < size[ry]:
                    rx, ry = ry, rx
                parent[ry] = rx
                size[rx] += size[ry]
                has_clone[rx] = has_clone[rx] or has_clone[ry]

            ans = 0
            p = 0
            while p < n:
                q = p
                while q < n and a[order[q]] == a[order[p]]:
                    q += 1

                for k in range(p, q):
                    i = order[k]
                    active[i] = True
                    parent[i] = i
                    size[i] = 1
                    has_clone[i] = False

                for k in range(p, q):
                    i = order[k]
                    if i > 0 and active[i - 1]:
                        union(i, i - 1)
                    if i + 1 < n and active[i + 1]:
                        union(i, i + 1)

                roots = set()
                for k in range(p, q):
                    roots.add(find(order[k]))

                for r in roots:
                    r = find(r)
                    if not has_clone[r]:
                        ans += 1
                        has_clone[r] = True

                p = q

            out.append(str(ans))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
