# Clause setup_environment [Confidence: 0.60]
import sys

MOD = 1000000007


# Clause solve_logic [Confidence: 0.80]
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    t = values[0]
    triples = []
    need = 1
    pos = 1

    for _ in range(t):
        n = values[pos]
        m = values[pos + 1]
        k = values[pos + 2]
        pos += 3
        triples.append((n, m, k))
        total = n + m
        if total > need:
            need = total

    inv = [0] * (need + 1)
    inv[1] = 1
    for x in range(2, need + 1):
        inv[x] = (MOD - MOD // x) * inv[MOD % x] % MOD

    out = []
    for n, m, k in triples:
        limit = k - 1
        if n * m <= limit:
            out.append("0")
            continue

        ans = 1
        start_w = limit // n + 1
        if start_w < 1:
            start_w = 1
        for w in range(start_w, m):
            ans += inv[w + limit // w]
            if ans >= MOD:
                ans -= MOD

        start_h = limit // m + 1
        if start_h < 1:
            start_h = 1
        for h in range(start_h, n):
            ans += inv[h + limit // h]
            if ans >= MOD:
                ans -= MOD

        out.append(str(ans))

    sys.stdout.write("\n".join(out))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


