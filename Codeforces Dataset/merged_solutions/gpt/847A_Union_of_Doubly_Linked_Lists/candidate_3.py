# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]

    l = [0] * (n + 1)
    r = [0] * (n + 1)

    idx = 1
    for i in range(1, n + 1):
        l[i] = data[idx]
        r[i] = data[idx + 1]
        idx += 2

    heads = [i for i in range(1, n + 1) if l[i] == 0]
    tails = []

    for h in heads:
        cur = h
        while r[cur] != 0:
            cur = r[cur]
        tails.append(cur)

    for i in range(len(heads) - 1):
        r[tails[i]] = heads[i + 1]
        l[heads[i + 1]] = tails[i]

    out = []
    for i in range(1, n + 1):
        out.append(f"{l[i]} {r[i]}")

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
