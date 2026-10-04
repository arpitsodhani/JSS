# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1].strip()
        idx += 2

        p = list(range(1, n + 1))
        ok = True
        i = 0

        while i < n:
            if s[i] == '1':
                i += 1
                continue
            j = i
            while j < n and s[j] == '0':
                j += 1
            if j - i == 1:
                ok = False
                break
            for k in range(i, j - 1):
                p[k] = k + 2
            p[j - 1] = i + 1
            i = j

        if not ok:
            out.append("NO")
        else:
            out.append("YES")
            out.append(" ".join(map(str, p)))

    print("\n".join(out))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
