# CLAUSE: setup_environment
import sys

M = 998244353
H = (M + 1) // 2

# CLAUSE: solve_logic
def run_case(n, raw, edge_list):
    f = [0] * (n + 1)
    s = [0] * (n + 1)
    invf = [0] * (n + 1)

    for i in range(1, n + 1):
        p, q = raw[i - 1]
        val = (p % M) * pow(q % M, M - 2, M) % M
        f[i] = val
        s[i] = (1 - val) % M
        if val:
            invf[i] = pow(val, M - 2, M)

    adj = [[] for _ in range(n + 1)]
    for x, y in edge_list:
        adj[x].append(y)
        adj[y].append(x)

    zc = [0] * (n + 1)
    pp = [1] * (n + 1)
    rr = [0] * (n + 1)

    for node in range(1, n + 1):
        for nb in adj[node]:
            if f[nb]:
                pp[node] = pp[node] * f[nb] % M
                rr[node] = (rr[node] + s[nb] * invf[nb]) % M
            else:
                zc[node] += 1

    def without_all_fall(node, banned):
        z = zc[node] - (1 if f[banned] == 0 else 0)
        if z:
            return 0
        if f[banned]:
            return pp[node] * invf[banned] % M
        return pp[node]

    def without_single_alive(node, banned):
        z = zc[node]
        pr = pp[node]
        sm = rr[node]
        if f[banned] == 0:
            z -= 1
        else:
            pr = pr * invf[banned] % M
            sm = (sm - s[banned] * invf[banned]) % M
        if z > 1:
            return 0
        if z == 1:
            return pr
        return pr * sm % M

    lp = [0] * (n + 1)
    linear = 0
    square = 0

    for node in range(1, n + 1):
        if zc[node] == 0:
            e = pp[node] * rr[node] % M
        elif zc[node] == 1:
            e = pp[node]
        else:
            e = 0
        lp[node] = s[node] * e % M
        linear = (linear + lp[node]) % M
        square = (square + lp[node] * lp[node]) % M

    res = (linear * linear - square) * H % M

    for x, y in edge_list:
        real = s[x] * s[y] % M
        real = real * without_all_fall(x, y) % M
        real = real * without_all_fall(y, x) % M
        res = (res + real - lp[x] * lp[y]) % M

    for root in range(1, n + 1):
        a1 = a2 = b1 = b2 = c1 = c2 = 0
        for nb in adj[root]:
            av = s[nb] * without_all_fall(nb, root) % M
            bv = s[nb] * without_single_alive(nb, root) % M
            cv = lp[nb]
            a1 = (a1 + av) % M
            a2 = (a2 + av * av) % M
            b1 = (b1 + bv) % M
            b2 = (b2 + bv * bv) % M
            c1 = (c1 + cv) % M
            c2 = (c2 + cv * cv) % M
        real_pairs = (s[root] * (a1 * a1 - a2) + f[root] * (b1 * b1 - b2)) * H % M
        free_pairs = (c1 * c1 - c2) * H % M
        res = (res + real_pairs - free_pairs) % M

    return res % M

# CLAUSE: finish_program
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    at = 1
    answers = []
    for _ in range(nums[0]):
        n = nums[at]
        at += 1
        raw = [(nums[i], nums[i + 1]) for i in range(at, at + 2 * n, 2)]
        at += 2 * n
        edge_list = [(nums[i], nums[i + 1]) for i in range(at, at + 2 * (n - 1), 2)]
        at += 2 * (n - 1)
        answers.append(str(run_case(n, raw, edge_list)))
    print("\n".join(answers))

if __name__ == "__main__":
    main()
