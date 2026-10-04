# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    ans = []
    idx = 1

    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2

        p = 1
        while True:
            cnt = (n // p + 1) // 2
            if k <= cnt:
                ans.append(str(p * (2 * k - 1)))
                break
            k -= cnt
            p *= 2

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
