# Clause program [Confidence: 0.40]
# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        out.append("{:.9f}".format(1.0 / math.tan(math.pi / (2 * n))))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(out))

main()


