# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
def intersection_distance(first, second, px, py):
    a, b, c = first
    d, e, f = second
    den = a * e - d * b
    if -1e-12 <= den <= 1e-12:
        return None
    x = (b * f - e * c) / den
    y = (d * c - a * f) / den
    return math.hypot(x - px, y - py)

def main():
    values = sys.stdin.read().split()
    n = int(float(values[0]))
    px = float(values[1])
    py = float(values[2])
    need = int(float(values[3]))

    raw = values[4:]
    equations = []
    for k in range(0, 2 * n, 2):
        a = float(raw[k])
        b = float(raw[k + 1])
        equations.append((a, b, -a * a - b * b))

    answer_values = []
    for left in range(len(equations) - 1):
        base = equations[left]
        for right in equations[left + 1:]:
            dist = intersection_distance(base, right, px, py)
            if dist is not None:
                answer_values.append(dist)

    answer_values.sort()
    sys.stdout.write("%.9f\n" % sum(answer_values[:need]))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
