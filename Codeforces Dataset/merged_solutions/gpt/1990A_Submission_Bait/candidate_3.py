# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from collections import Counter

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    ans = []

    for _ in range(t):
        n = data[p]
        p += 1
        a = data[p:p + n]
        p += n

        cnt = Counter(a)
        win = False
        for x in sorted(cnt):
            if cnt[x] % 2 == 1:
                win = True
                break
            else:
                break

        ans.append("YES" if win else "NO")

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
