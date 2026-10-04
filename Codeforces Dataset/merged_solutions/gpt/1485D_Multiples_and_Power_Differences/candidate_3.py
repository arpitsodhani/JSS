# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = sys.stdin.read().strip().split()
    if data:
        n = int(data[0])
        m = int(data[1])
        vals = list(map(int, data[2:]))
        base = 720720
        out = []
        p = 0
        for i in range(n):
            row = []
            for j in range(m):
                x = vals[p]
                p += 1
                if (i + j) % 2 == 0:
                    row.append(str(base))
                else:
                    row.append(str(base + x ** 4))
            out.append(" ".join(row))
        print("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
