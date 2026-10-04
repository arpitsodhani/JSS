# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        odds = [x for x in a if x % 2]
        evens = sorted(x for x in a if x % 2 == 0)

        if not odds or not evens:
            out.append("0")
            continue

        cur = max(odds)
        ans = len(evens)

        for x in evens:
            if x < cur:
                cur += x
            else:
                ans += 1
                cur += 2 * x

        out.append(str(ans))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
