# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    ans = []

    for n in data[1:1 + t]:
        seq = []
        b = 1
        while b <= n:
            if n & b:
                x = n ^ b
                if x > 0:
                    seq.append(x)
            b <<= 1
        seq.sort()
        seq.append(n)
        ans.append(str(len(seq)))
        ans.append(" ".join(map(str, seq)))

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
