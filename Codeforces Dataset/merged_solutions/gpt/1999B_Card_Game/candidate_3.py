# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        a1, a2, b1, b2 = data[idx:idx + 4]
        idx += 4

        count = 0
        for x, y in ((a1, a2), (a2, a1)):
            for u, v in ((b1, b2), (b2, b1)):
                suneet = 0
                slavic = 0

                if x > u:
                    suneet += 1
                elif x < u:
                    slavic += 1

                if y > v:
                    suneet += 1
                elif y < v:
                    slavic += 1

                if suneet > slavic:
                    count += 1

        ans.append(str(count))

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
