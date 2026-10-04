# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    s = list(data[2])

    idx = 3
    for _ in range(m):
        l = int(data[idx])
        r = int(data[idx + 1])
        c1 = data[idx + 2]
        c2 = data[idx + 3]
        idx += 4

        for i in range(l - 1, r):
            if s[i] == c1:
                s[i] = c2

    print(''.join(s))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
