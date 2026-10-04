# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 1.00]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    queries = []
    max_n = 0
    p = 1
    for _ in range(t):
        n = data[p]
        k = data[p + 1]
        p += 2
        queries.append((n, k))
        if n > max_n:
            max_n = n

    phi = list(range(max_n + 1))
    for x in range(2, max_n + 1):
        if phi[x] == x:
            for y in range(x, max_n + 1, x):
                phi[y] -= phi[y] // x

    pref = [0] * (max_n + 1)
    if max_n:
        pref[1] = 1
    for x in range(2, max_n + 1):
        pref[x] = pref[x - 1] + phi[x]

    cost = [[0] * (max_n + 1) for _ in range(max_n + 2)]
    for r in range(1, max_n + 1):
        column = r
        for l in range(r, 0, -1):
            cost[l][column] = cost[l + 1][column] + pref[column // l]

    out = []
    inf = 10 ** 30

    for n, k in queries:
        k = min(k, n)
        prev = [0] * (n + 1)
        first = cost[1]
        for i in range(1, n + 1):
            prev[i] = first[i]

        for parts in range(2, k + 1):
            cur = [0] * (n + 1)

            def compute(left, right, opt_left, opt_right):
                if left > right:
                    return
                mid = (left + right) // 2
                best = inf
                where = opt_left
                top = min(opt_right, mid - 1)
                for cut in range(opt_left, top + 1):
                    value = prev[cut] + cost[cut + 1][mid]
                    if value < best:
                        best = value
                        where = cut
                cur[mid] = best
                compute(left, mid - 1, opt_left, where)
                compute(mid + 1, right, where, opt_right)

            compute(parts, n, parts - 1, n - 1)
            prev = cur
        out.append(str(prev[n]))


# Clause finish_program [Confidence: 1.00]
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()


