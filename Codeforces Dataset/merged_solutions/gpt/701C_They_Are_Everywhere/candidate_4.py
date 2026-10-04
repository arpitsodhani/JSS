# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from collections import defaultdict

    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]

    need = len(set(s))
    cnt = defaultdict(int)
    have = 0
    left = 0
    ans = n

    for right, ch in enumerate(s):
        if cnt[ch] == 0:
            have += 1
        cnt[ch] += 1

        while have == need:
            ans = min(ans, right - left + 1)
            lc = s[left]
            cnt[lc] -= 1
            if cnt[lc] == 0:
                have -= 1
            left += 1

    print(ans)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
