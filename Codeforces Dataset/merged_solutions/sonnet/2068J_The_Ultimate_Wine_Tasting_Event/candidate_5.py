# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def verdict(n, s):
    left = s[:n]
    cnt = left.count("W")
    if cnt % 2:
        return "NO"
    if "R" not in left:
        return "YES"
    need = cnt // 2
    prefix = len(left) - len(left.lstrip("W"))
    right = s[n:]
    suffix = len(right) - len(right.rstrip("R"))
    return "YES" if prefix >= need and suffix >= need else "NO"

def main():
    parts = sys.stdin.read().split()
    total = int(parts[0])
    answers = [None] * total
    j = 1
    for case in range(total):
        n = int(parts[j])
        s = parts[j + 1]
        answers[case] = verdict(n, s)
        j += 2
    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
