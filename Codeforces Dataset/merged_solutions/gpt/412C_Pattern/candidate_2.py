# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    patterns = data[1:1 + n]
    m = len(patterns[0])
    ans = []
    for j in range(m):
        ch = None
        ok = True
        for s in patterns:
            if s[j] != '?':
                if ch is None:
                    ch = s[j]
                elif ch != s[j]:
                    ok = False
                    break
        if ok:
            ans.append(ch if ch is not None else 'a')
        else:
            ans.append('?')
    print(''.join(ans))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
