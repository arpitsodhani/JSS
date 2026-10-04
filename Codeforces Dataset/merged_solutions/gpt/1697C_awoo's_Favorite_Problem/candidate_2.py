# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def can_transform(n, s, t):
    if s.replace('b', '') != t.replace('b', ''):
        return False
    i = j = 0
    while i < n or j < n:
        while i < n and s[i] == 'b':
            i += 1
        while j < n and t[j] == 'b':
            j += 1
        if i == n or j == n:
            return i == n and j == n
        if s[i] != t[j]:
            return False
        if s[i] == 'a' and i > j:
            return False
        if s[i] == 'c' and i < j:
            return False
        i += 1
        j += 1
    return True

def main():
    data = sys.stdin.read().split()
    q = int(data[0])
    idx = 1
    ans = []
    for _ in range(q):
        n = int(data[idx])
        s = data[idx + 1]
        t = data[idx + 2]
        idx += 3
        ans.append('YES' if can_transform(n, s, t) else 'NO')
    print('\n'.join(ans))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
