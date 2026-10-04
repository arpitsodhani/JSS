# Clause setup_environment [Confidence: 0.80]
import sys

MODULO = 998244353
TWO_INV = 499122177


# Clause solve_logic [Confidence: 1.00]
def solve_case(n, probs, edges):
    fall = [0] * (n + 1)
    alive = [0] * (n + 1)
    for i, (p, q) in enumerate(probs, 1):
        x = (p % MOD) * pow(q % MOD, MOD - 2, MOD) % MOD
        fall[i] = x
        alive[i] = (1 - x) % MOD

    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    zeros = [0] * (n + 1)
    prod = [1] * (n + 1)
    ratios = [0] * (n + 1)

    for v in range(1, n + 1):
        z = 0
        pr = 1
        rs = 0
        for u in graph[v]:
            if fall[u] == 0:
                z += 1
            else:
                inv = pow(fall[u], MOD - 2, MOD)
                pr = pr * fall[u] % MOD
                rs = (rs + alive[u] * inv) % MOD
        zeros[v] = z
        prod[v] = pr
        ratios[v] = rs

    def all_down(v, skip):
        z = zeros[v]
        pr = prod[v]
        if fall[skip] == 0:
            z -= 1
        else:
            pr = pr * pow(fall[skip], MOD - 2, MOD) % MOD
        if z:
            return 0
        return pr

    def one_up(v, skip):
        z = zeros[v]
        pr = prod[v]
        rs = ratios[v]
        if fall[skip] == 0:
            z -= 1
        else:
            inv = pow(fall[skip], MOD - 2, MOD)
            pr = pr * inv % MOD
            rs = (rs - alive[skip] * inv) % MOD
        if z >= 2:
            return 0
        if z == 1:
            return pr
        return pr * rs % MOD

    leaf = [0] * (n + 1)
    total = 0
    total_sq = 0
    for v in range(1, n + 1):
        if zeros[v] >= 2:
            exact = 0
        elif zeros[v] == 1:
            exact = prod[v]
        else:
            exact = prod[v] * ratios[v] % MOD
        leaf[v] = alive[v] * exact % MOD
        total = (total + leaf[v]) % MOD
        total_sq = (total_sq + leaf[v] * leaf[v]) % MOD

    ans = (total * total - total_sq) * INV2 % MOD

    for u, v in edges:
        actual = alive[u] * alive[v] % MOD
        actual = actual * all_down(u, v) % MOD
        actual = actual * all_down(v, u) % MOD
        ans = (ans + actual - leaf[u] * leaf[v]) % MOD

    for c in range(1, n + 1):
        sa = sb = sc = 0
        qa = qb = qc = 0
        for v in graph[c]:
            a = alive[v] * all_down(v, c) % MOD
            b = alive[v] * one_up(v, c) % MOD
            d = leaf[v]
            sa = (sa + a) % MOD
            sb = (sb + b) % MOD
            sc = (sc + d) % MOD
            qa = (qa + a * a) % MOD
            qb = (qb + b * b) % MOD
            qc = (qc + d * d) % MOD
        got = (alive[c] * (sa * sa - qa) + fall[c] * (sb * sb - qb)) % MOD
        got = got * INV2 % MOD
        ind = (sc * sc - qc) * INV2 % MOD
        ans = (ans + got - ind) % MOD

    return ans % MOD


# Clause finish_program [Confidence: 0.80]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    k = 0
    t = data[k]
    k += 1
    result = []
    for _ in range(t):
        n = data[k]
        k += 1
        probs = []
        for _ in range(n):
            probs.append((data[k], data[k + 1]))
            k += 2
        edges = []
        for _ in range(n - 1):
            edges.append((data[k], data[k + 1]))
            k += 2
        result.append(str(solve_case(n, probs, edges)))
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()


