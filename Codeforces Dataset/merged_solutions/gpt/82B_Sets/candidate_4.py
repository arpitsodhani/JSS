# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        sys.exit()

    n = data[0]
    m = n * (n - 1) // 2
    p = 1

    occ = {}
    for i in range(m):
        c = data[p]
        p += 1
        bit = 1 << i
        for _ in range(c):
            x = data[p]
            p += 1
            occ[x] = occ.get(x, 0) | bit

    groups = {}
    for x, mask in occ.items():
        groups.setdefault(mask, []).append(x)

    ans = []
    for v in groups.values():
        ans.append(str(len(v)))
        ans.extend(map(str, v))

    sys.stdout.write(" ".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
