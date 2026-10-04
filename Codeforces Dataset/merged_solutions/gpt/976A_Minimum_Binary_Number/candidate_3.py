# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = sys.stdin.read().split()

    if len(data) >= 2:
        s = data[1]
    else:
        t = data[0] if data else ""
        s = t
        for i in range(1, len(t) + 1):
            if t[:i].isdigit() and int(t[:i]) == len(t) - i:
                s = t[i:]
                break

    zeros = s.count("0")
    if zeros == 0:
        print("1")
    else:
        print("1" + "0" * zeros)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
