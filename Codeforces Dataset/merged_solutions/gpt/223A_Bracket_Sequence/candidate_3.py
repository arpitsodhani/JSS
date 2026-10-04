# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    s = sys.stdin.readline().strip()
    n = len(s)

    dp_len = [0] * n
    dp_cnt = [0] * n

    best_cnt = 0
    best_l = 0
    best_r = -1

    pairs = {')': '(', ']': '['}

    for i, ch in enumerate(s):
        if ch in pairs:
            prev_len = dp_len[i - 1] if i > 0 else 0
            j = i - prev_len - 1
            if j >= 0 and s[j] == pairs[ch]:
                dp_len[i] = prev_len + 2
                dp_cnt[i] = dp_cnt[i - 1] if i > 0 else 0
                if s[j] == '[':
                    dp_cnt[i] += 1
                if j > 0:
                    dp_len[i] += dp_len[j - 1]
                    dp_cnt[i] += dp_cnt[j - 1]

                if dp_cnt[i] > best_cnt:
                    best_cnt = dp_cnt[i]
                    best_l = i - dp_len[i] + 1
                    best_r = i

    print(best_cnt)
    if best_cnt > 0:
        print(s[best_l:best_r + 1])

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
