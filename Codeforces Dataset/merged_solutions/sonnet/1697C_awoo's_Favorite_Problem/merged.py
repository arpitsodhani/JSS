# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.40]
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


# Clause finish_program [Confidence: 0.80]
def main():
    parts = sys.stdin.read().strip().split()
    if not parts:
        return
    q = int(parts[0])
    result = []
    k = 1
    for _ in range(q):
        n = int(parts[k])
        s = parts[k + 1]
        t = parts[k + 2]
        k += 3
        result.append("YES" if valid(n, s, t) else "NO")
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()


