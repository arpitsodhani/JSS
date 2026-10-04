# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    queries = []
    max_n = 0
    max_layer = 1
    p = 1
    for _ in range(t):
        n = data[p]
        k = data[p + 1]
        p += 2
        queries.append((n, k))
        if n > max_n:
            max_n = n
        if k < 17 and (1 << k) - 1 < n and (k > max_layer):
            max_layer = k
    ans = [[0] * (max_n + 1) for _ in range(max_layer + 1)]
    for i in range(1, max_n + 1):
        ans[1][i] = i * (i + 1) // 2
    if max_layer >= 2:
        phi = [0] * (max_n + 1)
        comp = [False] * (max_n + 1)
        primes = []
        phi[1] = 1
        for i in range(2, max_n + 1):
            if not comp[i]:
                primes.append(i)
                phi[i] = i - 1
            for q in primes:
                x = i * q
                if x > max_n:
                    break
                comp[x] = True
                if i % q == 0:
                    phi[x] = phi[i] * q
                    break
                phi[x] = phi[i] * (q - 1)
        divs = [[] for _ in range(max_n + 1)]
        for d in range(1, max_n + 1):
            for m in range(d, max_n + 1, d):
                divs[m].append(d)
        size = max_n
        tree_n = 4 * (size + 5)
        mn = [0] * tree_n
        lazy = [0] * tree_n
        sys.setrecursionlimit(1000000)

        def build(o, l, r, arr):
            lazy[o] = 0
            if l == r:
                mn[o] = arr[l]
                return
            mid = l + r >> 1
            build(o << 1, l, mid, arr)
            build(o << 1 | 1, mid + 1, r, arr)
            a = mn[o << 1]
            b = mn[o << 1 | 1]
            mn[o] = a if a < b else b

        def add_suffix(o, l, r, x, val):
            if x <= l:
                lazy[o] += val
                mn[o] += val
                return
            mid = l + r >> 1
            if x <= mid:
                add_suffix(o << 1, l, mid, x, val)
                ro = o << 1 | 1
                lazy[ro] += val
                mn[ro] += val
            else:
                add_suffix(o << 1 | 1, mid + 1, r, x, val)
            a = mn[o << 1]
            b = mn[o << 1 | 1]
            mn[o] = (a if a < b else b) + lazy[o]
        inf = 10 ** 30
        for layer in range(2, max_layer + 1):
            prev = ans[layer - 1]
            cur = ans[layer]
            build(1, 1, size, prev)
            total = 0
            for j in range(1, size + 1):
                total += j
                for d in divs[j]:
                    add_suffix(1, 1, size, d, -phi[j // d])
                cur[j] = total + mn[1]
    out = []
    for n, k in queries:
        if k >= 17 or (1 << k) - 1 >= n:
            out.append(str(n))
        else:
            out.append(str(ans[k][n]))
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
