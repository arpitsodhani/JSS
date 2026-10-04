# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        input = sys.stdin.readline
        n, x = map(int, input().split())
        a = list(map(int, input().split()))

        INF = 10 ** 18
        mn = [INF] * (x + 2)
        mx = [-INF] * (x + 2)

        for i, v in enumerate(a, 1):
            if i < mn[v]:
                mn[v] = i
            if i > mx[v]:
                mx[v] = i

        pref_max = [-INF] * (x + 2)
        pref_ok = [True] * (x + 2)
        for v in range(1, x + 1):
            pref_ok[v] = pref_ok[v - 1] and pref_max[v - 1] < mn[v]
            pref_max[v] = max(pref_max[v - 1], mx[v])

        suff_min = [INF] * (x + 3)
        suff_ok = [True] * (x + 3)
        for v in range(x, 0, -1):
            suff_ok[v] = suff_ok[v + 1] and mx[v] < suff_min[v + 1]
            suff_min[v] = min(suff_min[v + 1], mn[v])

        ans = 0
        r = 1

        for l in range(1, x + 1):
            if not pref_ok[l - 1]:
                break
            if r < l:
                r = l
            while r <= x and (not suff_ok[r + 1] or pref_max[l - 1] > suff_min[r + 1]):
                r += 1
            if r <= x:
                ans += x - r + 1

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
