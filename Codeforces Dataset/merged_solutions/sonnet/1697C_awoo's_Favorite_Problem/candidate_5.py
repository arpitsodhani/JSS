# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve_case(n, s, t):
    order_s = []
    order_t = []
    a_pairs = []
    c_pairs = []
    for i in range(n):
        if s[i] != "b":
            order_s.append(s[i])
        if t[i] != "b":
            order_t.append(t[i])
    if order_s != order_t:
        return "NO"
    for i in range(n):
        if s[i] == "a":
            a_pairs.append([i])
        elif s[i] == "c":
            c_pairs.append([i])
    ai = 0
    ci = 0
    for i in range(n):
        if t[i] == "a":
            a_pairs[ai].append(i)
            ai += 1
        elif t[i] == "c":
            c_pairs[ci].append(i)
            ci += 1
    for x, y in a_pairs:
        if x > y:
            return "NO"
    for x, y in c_pairs:
        if x < y:
            return "NO"
    return "YES"

# CLAUSE: finish_program
def main():
    data = sys.stdin.readline
    q_line = data().strip()
    if not q_line:
        return
    q = int(q_line)
    ans = []
    for _ in range(q):
        n = int(data())
        s = data().strip()
        t = data().strip()
        ans.append(solve_case(n, s, t))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
