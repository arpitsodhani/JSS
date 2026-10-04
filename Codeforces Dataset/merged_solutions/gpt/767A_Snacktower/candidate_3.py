# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    arr = data[1:]

    seen = [False] * (n + 1)
    need = n
    out = []

    for x in arr:
        seen[x] = True
        line = []
        while need > 0 and seen[need]:
            line.append(str(need))
            need -= 1
        out.append(" ".join(line))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
