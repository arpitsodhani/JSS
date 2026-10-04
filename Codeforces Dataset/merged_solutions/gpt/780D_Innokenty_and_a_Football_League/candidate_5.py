# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from collections import defaultdict, deque

        data = sys.stdin.read().split()
        if not data:
            sys.exit()

        n = int(data[0])
        a = []
        b = []

        p = 1
        for _ in range(n):
            s = data[p]
            t = data[p + 1]
            p += 2
            a.append(s[:3])
            b.append(s[:2] + t[0])

        by_a = defaultdict(list)
        for i, x in enumerate(a):
            by_a[x].append(i)

        forced = [False] * n
        q = deque()

        for ids in by_a.values():
            if len(ids) > 1:
                for i in ids:
                    forced[i] = True
                    q.append(i)

        while q:
            i = q.popleft()
            for j in by_a.get(b[i], []):
                if not forced[j]:
                    forced[j] = True
                    q.append(j)

        used = set()
        ans = []

        for i in range(n):
            name = b[i] if forced[i] else a[i]
            if name in used:
                print("NO")
                sys.exit()
            used.add(name)
            ans.append(name)

        print("YES")
        print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
