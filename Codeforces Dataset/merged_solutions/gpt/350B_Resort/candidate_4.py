# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    typ = [0] + data[1:n + 1]
    a = [0] + data[n + 1:2 * n + 1]

    outdeg = [0] * (n + 1)
    for i in range(1, n + 1):
        if a[i]:
            outdeg[a[i]] += 1

    best = []

    for i in range(1, n + 1):
        if typ[i] == 1:
            cur = [i]
            v = i
            while a[v] and typ[a[v]] == 0 and outdeg[a[v]] == 1:
                v = a[v]
                cur.append(v)
            if len(cur) > len(best):
                best = cur

    best.reverse()
    print(len(best))
    print(*best)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
