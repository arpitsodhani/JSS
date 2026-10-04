# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    t = data[pos]
    pos += 1
    out = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        found = False
        for value in data[pos:pos + n]:
            if value == 67:
                found = True
        pos += n
        out.append("YES" if found else "NO")

# CLAUSE: finish_program
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
