# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    n, k = map(int, input().split())
    s = input().strip()

    cnt = [0] * 26
    i = 0

    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        cnt[ord(s[i]) - 97] += (j - i) // k
        i = j

    print(max(cnt))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
