# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        mx = a[0]
        total = 0
        biggest = 0

        for x in a:
            if x < mx:
                d = mx - x
                total += d
                if d > biggest:
                    biggest = d
            else:
                mx = x

        ans.append(str(total + biggest))

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
