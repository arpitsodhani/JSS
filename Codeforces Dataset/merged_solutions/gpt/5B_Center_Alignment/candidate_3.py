# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    lines = sys.stdin.read().splitlines()
    w = max((len(s) for s in lines), default=0)

    out = ["*" * (w + 2)]
    flip = False

    for s in lines:
        d = w - len(s)
        left = d // 2
        right = d - left
        if d % 2:
            if flip:
                left, right = right, left
            flip = not flip
        out.append("*" + " " * left + s + " " * right + "*")

    out.append("*" * (w + 2))
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
