# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def filtered_items(text):
    return [(ch, i) for i, ch in enumerate(text) if ch != "b"]

def valid(n, s, t):
    left = filtered_items(s)
    right = filtered_items(t)
    if len(left) != len(right):
        return False
    for (ch1, pos1), (ch2, pos2) in zip(left, right):
        if ch1 != ch2:
            return False
        if ch1 == "a":
            if pos1 > pos2:
                return False
        else:
            if pos1 < pos2:
                return False
    return True

# CLAUSE: finish_program
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
