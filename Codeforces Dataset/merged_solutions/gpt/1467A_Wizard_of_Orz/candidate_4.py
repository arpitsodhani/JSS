# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = sys.stdin.read().strip().split()
    t = int(data[0])
    ans = []
    base = "989"

    for i in range(1, t + 1):
        n = int(data[i])
        if n <= 3:
            ans.append(base[:n])
        else:
            s = ["989"]
            for j in range(n - 3):
                s.append(str(j % 10))
            ans.append("".join(s))

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
