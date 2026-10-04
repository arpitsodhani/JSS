# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.40]
def main():
    data = sys.stdin.read().strip()
    answer = data.count("1")


# Clause finish_program [Confidence: 0.20]
print(solve(sys.stdin.read()))


