# CLAUSE: setup_environment
import sys

MODULO = 998244353
TWO_INV = 499122177

# CLAUSE: solve_logic
def solve_case(n, probs, edges):
    fall = [0] * (n + 1)
    stay = [0] * (n + 1)
    inv = [0] * (n + 1)

    for i in range(n):
        p, q = probs[i]
        x = p % MODULO * pow(q % MODULO, MODULO - 2, MODULO) % MODULO
        v = i + 1
        fall[v] = x
        stay[v] = (1 - x) % MODULO
        if x:
            inv[v] = pow(x, MODULO - 2, MODULO)

    head = [-1] * (n + 1)
    to = []
    nxt = []

    def add(a, b):
        nxt.append(head[a])
        to.append(b)
        head[a] = len(to) - 1

    for a, b in edges:
        add(a, b)
        add(b, a)

    zero = [0] * (n + 1)
    mul = [1] * (n + 1)
    add_ratio = [0] * (n + 1)

    for v in range(1, n + 1):
        e = head[v]
        while e != -1:
            u = to[e]
            if fall[u] == 0:
                zero[v] += 1
            else:
                mul[v] = mul[v] * fall[u] % MODULO
                add_ratio[v] = (add_ratio[v] + stay[u] * inv[u]) % MODULO
            e = nxt[e]

    def zero_removed(v, u):
        if fall[u] == 0:
            return zero[v] - 1, mul[v], add_ratio[v]
        return zero[v], mul[v] * inv[u] % MODULO, (add_ratio[v] - stay[u] * inv[u]) % MODULO

    leaf = [0] * (n + 1)
    s_leaf = 0
    q_leaf = 0

    for v in range(1, n + 1):
        if zero[v] == 0:
            need = mul[v] * add_ratio[v] % MODULO
        elif zero[v] == 1:
            need = mul[v]
        else:
            need = 0
        leaf[v] = stay[v] * need % MODULO
        s_leaf = (s_leaf + leaf[v]) % MODULO
        q_leaf = (q_leaf + leaf[v] * leaf[v]) % MODULO

    ans = (s_leaf * s_leaf - q_leaf) * TWO_INV % MODULO

    for a, b in edges:
        za, pa, _ = zero_removed(a, b)
        zb, pb, _ = zero_removed(b, a)
        actual = 0
        if za == 0 and zb == 0:
            actual = stay[a] * stay[b] % MODULO * pa % MODULO * pb % MODULO
        ans = (ans + actual - leaf[a] * leaf[b]) % MODULO

    for center in range(1, n + 1):
        sa = sb = sc = 0
        aa = bb = cc = 0
        e = head[center]
        while e != -1:
            v = to[e]
            z, pr, rs = zero_removed(v, center)
            if z == 0:
                all_fall = pr
                one_alive = pr * rs % MODULO
            elif z == 1:
                all_fall = 0
                one_alive = pr
            else:
                all_fall = 0
                one_alive = 0
            x = stay[v] * all_fall % MODULO
            y = stay[v] * one_alive % MODULO
            zval = leaf[v]
            sa = (sa + x) % MODULO
            sb = (sb + y) % MODULO
            sc = (sc + zval) % MODULO
            aa = (aa + x * x) % MODULO
            bb = (bb + y * y) % MODULO
            cc = (cc + zval * zval) % MODULO
            e = nxt[e]
        real = (stay[center] * (sa * sa - aa) + fall[center] * (sb * sb - bb)) % MODULO
        real = real * TWO_INV % MODULO
        sep = (sc * sc - cc) * TWO_INV % MODULO
        ans = (ans + real - sep) % MODULO

    return ans % MODULO

# CLAUSE: finish_program
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
