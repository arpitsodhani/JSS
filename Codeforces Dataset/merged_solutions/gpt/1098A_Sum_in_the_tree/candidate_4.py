# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    sys.setrecursionlimit(300000)

    def main():
        input = sys.stdin.readline
        n = int(input())
        p = [0] + list(map(int, input().split()))
        s = [0] + list(map(int, input().split()))

        children = [[] for _ in range(n + 1)]
        for v in range(2, n + 1):
            children[p[v]].append(v)

        order = [1]
        for v in order:
            order.extend(children[v])

        for v in order:
            if s[v] == -1:
                if children[v]:
                    s[v] = min(s[u] for u in children[v])
                else:
                    s[v] = s[p[v]]

        ans = s[1]
        if s[1] < 0:
            print(-1)
            return

        for v in range(2, n + 1):
            diff = s[v] - s[p[v]]
            if diff < 0:
                print(-1)
                return
            ans += diff

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
