# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def displacement(text):
    total = 0
    unknown = 0
    for ch in text:
        if ch == "+":
            total += 1
        elif ch == "-":
            total -= 1
        else:
            unknown += 1
    return total, unknown

def choose(n, r):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    value = 1
    for i in range(1, r + 1):
        value = value * (n - r + i) // i
    return value

def main():
    parts = sys.stdin.read().split()
    target, _ = displacement(parts[0])
    current, unknown = displacement(parts[1])
    delta = target - current
    required_plus = (unknown + delta) // 2

    if unknown + delta < 0 or (unknown + delta) % 2 != 0:
        print("0.000000000000")
        return

    favorable = choose(unknown, required_plus)
    probability = favorable / (2 ** unknown)
    print("%.12f" % probability)

# CLAUSE: finish_program
main()
