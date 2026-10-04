# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    ans = []
    p = 1

    for _ in range(t):
        n = data[p]
        m = data[p + 1]
        p += 2

        k = m + 1
        res = 0
        done = False

        for b in range(31, -1, -1):
            nb = (n >> b) & 1
            kb = (k >> b) & 1

            if nb == kb:
                continue
            if nb < kb:
                res |= 1 << b
            else:
                done = True
                break

        if not done:
            res = n ^ k

        ans.append(str(res))

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
