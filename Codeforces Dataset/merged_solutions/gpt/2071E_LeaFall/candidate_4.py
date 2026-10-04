# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    MOD = 998244353
    INV2 = (MOD + 1) // 2

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        it = iter(data)
        t = next(it)
        out = []

        for _ in range(t):
            n = next(it)

            fall = [0] * n
            alive = [0] * n
            inv_fall = [0] * n
            ratio = [0] * n

            for i in range(n):
                p = next(it)
                q = next(it)
                inv_q = pow(q, MOD - 2, MOD)
                inv_p = pow(p, MOD - 2, MOD)
                fall[i] = p * inv_q % MOD
                alive[i] = (q - p) * inv_q % MOD
                inv_fall[i] = q * inv_p % MOD
                ratio[i] = (q - p) * inv_p % MOD

            adj = [[] for _ in range(n)]
            edges = []

            for _ in range(n - 1):
                u = next(it) - 1
                v = next(it) - 1
                adj[u].append(v)
                adj[v].append(u)
                edges.append((u, v))

            prod = [1] * n
            sm = [0] * n

            for v in range(n):
                pval = 1
                sval = 0
                for u in adj[v]:
                    pval = pval * fall[u] % MOD
                    sval += ratio[u]
                prod[v] = pval
                sm[v] = sval % MOD

            leaf = [alive[v] * prod[v] % MOD * sm[v] % MOD for v in range(n)]

            s = sum(leaf) % MOD
            s2 = sum(x * x % MOD for x in leaf) % MOD
            ans = (s * s - s2) * INV2 % MOD

            for u, v in edges:
                both = alive[u] * alive[v] % MOD
                both = both * prod[u] % MOD * inv_fall[v] % MOD
                both = both * prod[v] % MOD * inv_fall[u] % MOD
                ans = (ans + both - leaf[u] * leaf[v]) % MOD

            for m in range(n):
                sc = sd = sa = 0
                sc2 = sd2 = sa2 = 0

                for u in adj[m]:
                    pe = prod[u] * inv_fall[m] % MOD
                    c = alive[u] * pe % MOD
                    d = c * ((sm[u] - ratio[m]) % MOD) % MOD
                    a = leaf[u]

                    sc = (sc + c) % MOD
                    sd = (sd + d) % MOD
                    sa = (sa + a) % MOD
                    sc2 = (sc2 + c * c) % MOD
                    sd2 = (sd2 + d * d) % MOD
                    sa2 = (sa2 + a * a) % MOD

                pair_c = (sc * sc - sc2) * INV2 % MOD
                pair_d = (sd * sd - sd2) * INV2 % MOD
                pair_a = (sa * sa - sa2) * INV2 % MOD

                ans = (ans + alive[m] * pair_c + fall[m] * pair_d - pair_a) % MOD

            out.append(str(ans % MOD))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
