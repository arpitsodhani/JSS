# CLAUSE: setup_environment
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    n = data[p]
    p += 1
    a = data[p:p + n]
    p += n

# CLAUSE: solve_logic
    order = sorted(range(n), key=lambda i: (-a[i], i))
    best = [[] for _ in range(n + 1)]
    chosen = []
    for k in range(1, n + 1):
        chosen.append(order[k - 1])
        values = []
        for i in sorted(chosen):
            values.append(a[i])
        best[k] = values

    m = data[p]
    p += 1
    out = []
    for _ in range(m):
        k = data[p]
        pos = data[p + 1]
        p += 2
        out.append(str(best[k][pos - 1]))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
