# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def possible(n, s, t):
    if s.replace("b", "") != t.replace("b", ""):
        return False
    a_s = []
    a_t = []
    c_s = []
    c_t = []
    for i, ch in enumerate(s):
        if ch == "a":
            a_s.append(i)
        elif ch == "c":
            c_s.append(i)
    for i, ch in enumerate(t):
        if ch == "a":
            a_t.append(i)
        elif ch == "c":
            c_t.append(i)
    for x, y in zip(a_s, a_t):
        if x > y:
            return False
    for x, y in zip(c_s, c_t):
        if x < y:
            return False
    return True

# CLAUSE: finish_program
def main():
    data = sys.stdin.read().split()
    q = int(data[0])
    out = []
    p = 1
    for _ in range(q):
        n = int(data[p])
        s = data[p + 1]
        t = data[p + 2]
        p += 3
        out.append("YES" if possible(n, s, t) else "NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
