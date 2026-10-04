# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.read().split()
    pos = 0
    t = int(tokens[pos])
    pos += 1
    out = []
    for _ in range(t):
        n = int(tokens[pos])
        s = tokens[pos + 1]
        pos += 2
        left = s[:n]
        right = s[n:]
        whites_left = left.count("W")
        reds_left = n - whites_left
        possible = whites_left % 2 == 0
        if possible and reds_left:
            need = whites_left // 2
            first_red = left.find("R")
            last_white = right.rfind("W")
            possible = left[:first_red].count("W") >= need and right[last_white + 1:].count("R") >= need
        out.append("YES" if possible else "NO")
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
