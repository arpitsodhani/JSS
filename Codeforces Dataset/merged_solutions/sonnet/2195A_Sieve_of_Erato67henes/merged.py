# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.60]
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


# Clause finish_program [Confidence: 0.80]
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()


