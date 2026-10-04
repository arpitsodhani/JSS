# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = sys.stdin.read().split()
    s = data[0]
    u = data[1]

    n = len(s)
    m = len(u)
    best = 0

    for d in range(-m + 1, n):
        cnt = 0
        i = max(0, d)
        j = i - d
        while i < n and j < m:
            if s[i] == u[j]:
                cnt += 1
            i += 1
            j += 1
        if cnt > best:
            best = cnt

    print(m - best)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
