# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_positions(cards):
    positions = {}
    for index, color in enumerate(cards, 1):
        if color not in positions:
            positions[color] = index
    return positions

def answer_queries(first, queries):
    out = []
    for target in queries:
        current = first[target]
        out.append(str(current))
        for color, place in list(first.items()):
            if place < current:
                first[color] = place + 1
        first[target] = 1
    return out

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    q = data[1]
    cards = data[2:2 + n]
    queries = data[2 + n:2 + n + q]
    sys.stdout.write(" ".join(answer_queries(build_positions(cards), queries)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
