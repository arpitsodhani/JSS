# CLAUSE: setup_environment
import sys
from itertools import product

# CLAUSE: solve_logic
def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    ans = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2
        seen = set()
        for length in range(1, 4):
            for i in range(n - length + 1):
                seen.add(s[i:i + length])
            for chars in product(alphabet, repeat=length):
                cur = ''.join(chars)
                if cur not in seen:
                    ans.append(cur)
                    break
            if len(ans) == _ + 1:
                break
    print('\n'.join(ans))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
