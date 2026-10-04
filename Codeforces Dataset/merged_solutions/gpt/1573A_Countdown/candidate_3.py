# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    ans = []

    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2
        total = sum(int(c) for c in s)
        total += sum(1 for c in s[:-1] if c != '0')
        ans.append(str(total))

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
