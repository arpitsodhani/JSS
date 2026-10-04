# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]
    a = data[2:2 + n]

    add = 0
    idx = 2 + n
    out = []

    for _ in range(m):
        t = data[idx]
        idx += 1

        if t == 1:
            v = data[idx] - 1
            x = data[idx + 1]
            idx += 2
            a[v] = x - add
        elif t == 2:
            y = data[idx]
            idx += 1
            add += y
        else:
            q = data[idx] - 1
            idx += 1
            out.append(str(a[q] + add))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
