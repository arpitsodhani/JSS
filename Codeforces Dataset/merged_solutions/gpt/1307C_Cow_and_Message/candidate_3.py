# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    s = sys.stdin.readline().strip()

    cnt = [0] * 26
    pairs = [[0] * 26 for _ in range(26)]
    ans = 0

    for ch in s:
        x = ord(ch) - 97
        for i in range(26):
            pairs[i][x] += cnt[i]
            if pairs[i][x] > ans:
                ans = pairs[i][x]
        cnt[x] += 1
        if cnt[x] > ans:
            ans = cnt[x]

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
