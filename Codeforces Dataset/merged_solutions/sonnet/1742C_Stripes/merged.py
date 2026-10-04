# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.60]
def main():
    tokens = sys.stdin.read().split()
    tests = int(tokens[0])
    pos = 1
    result = []
    for _ in range(tests):
        board = tokens[pos:pos + 8]
        pos += 8
        color = "B"
        for line in board:
            if line == "RRRRRRRR":
                color = "R"
                break
        result.append(color)


# Clause finish_program [Confidence: 0.20]
items = sys.stdin.read().split()
sys.stdout.write("\n".join(solve(items)))


