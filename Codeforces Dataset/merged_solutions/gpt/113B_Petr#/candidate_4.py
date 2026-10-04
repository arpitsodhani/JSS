# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = sys.stdin.read().split()
    t, a, b = data[0], data[1], data[2]

    n = len(t)
    la = len(a)
    lb = len(b)

    starts = [False] * n
    ends = [False] * n

    for i in range(n - la + 1):
        if t[i:i + la] == a:
            starts[i] = True

    for i in range(n - lb + 1):
        if t[i:i + lb] == b:
            ends[i] = True

    base1 = 911382323
    base2 = 972663749
    mod1 = 1000000007
    mod2 = 1000000009

    p1 = [1] * (n + 1)
    p2 = [1] * (n + 1)
    h1 = [0] * (n + 1)
    h2 = [0] * (n + 1)

    for i, ch in enumerate(t):
        x = ord(ch)
        p1[i + 1] = p1[i] * base1 % mod1
        p2[i + 1] = p2[i] * base2 % mod2
        h1[i + 1] = (h1[i] * base1 + x) % mod1
        h2[i + 1] = (h2[i] * base2 + x) % mod2

    def get_hash(l, r):
        x1 = (h1[r] - h1[l] * p1[r - l]) % mod1
        x2 = (h2[r] - h2[l] * p2[r - l]) % mod2
        return x1, x2, r - l

    seen = set()

    for i in range(n):
        if not starts[i]:
            continue
        for j in range(i, n - lb + 1):
            if ends[j] and j + lb - i >= la:
                seen.add(get_hash(i, j + lb))

    print(len(seen))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
