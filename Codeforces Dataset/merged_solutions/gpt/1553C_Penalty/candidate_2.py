# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def earliest(s):
    ans = 10
    q = [i for i, c in enumerate(s) if c == '?']
    m = len(q)
    for mask in range(1 << m):
        a = b = 0
        rem_a = rem_b = 5
        for i in range(10):
            c = s[i]
            if c == '?':
                bit = mask >> q.index(i) & 1
                c = '1' if bit else '0'
            if i % 2 == 0:
                rem_a -= 1
                if c == '1':
                    a += 1
            else:
                rem_b -= 1
                if c == '1':
                    b += 1
            if a > b + rem_b or b > a + rem_a:
                ans = min(ans, i + 1)
                break
    return ans
data = sys.stdin.read().strip().split()
t = int(data[0])
out = []
for i in range(1, t + 1):
    out.append(str(earliest(data[i])))
print('\n'.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
