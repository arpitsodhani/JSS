# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def acceptable(n, s):
    a = s[:n]
    b = s[n:]
    w = sum(ch == "W" for ch in a)
    if w & 1:
        return False
    if w == n:
        return True
    need = w // 2
    before_bad = 0
    for ch in a:
        if ch == "R":
            break
        before_bad += 1
    after_bad = 0
    for ch in reversed(b):
        if ch == "W":
            break
        after_bad += 1
    return before_bad >= need and after_bad >= need

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    ans = []
    p = 1
    for _ in range(t):
        n = int(data[p])
        s = data[p + 1].decode()
        p += 2
        ans.append("YES" if acceptable(n, s) else "NO")
    print("\n".join(ans))

# CLAUSE: finish_program
main()
