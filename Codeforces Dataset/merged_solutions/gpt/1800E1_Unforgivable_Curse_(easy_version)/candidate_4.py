# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def find(parent, x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(parent, size, a, b):
        ra = find(parent, a)
        rb = find(parent, b)
        if ra == rb:
            return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    def solve():
        data = sys.stdin.read().split()
        if not data:
            return

        q = int(data[0])
        idx = 1
        ans = []

        for _ in range(q):
            n = int(data[idx])
            k = int(data[idx + 1])
            s = data[idx + 2]
            t = data[idx + 3]
            idx += 4

            parent = list(range(n))
            size = [1] * n

            for i in range(n - k):
                union(parent, size, i, i + k)
            for i in range(n - k - 1):
                union(parent, size, i, i + k + 1)

            cnt = {}

            for i in range(n):
                r = find(parent, i)
                if r not in cnt:
                    cnt[r] = [0] * 26
                cnt[r][ord(s[i]) - 97] += 1
                cnt[r][ord(t[i]) - 97] -= 1

            ok = True
            for v in cnt.values():
                if any(v):
                    ok = False
                    break

            ans.append("YES" if ok else "NO")

        sys.stdout.write("\n".join(ans))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
