# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    total = int(tokens[0])
    camels = set()
    pairs = []
    index = 1
    while len(pairs) < total:
        x = int(tokens[index])
        d = int(tokens[index + 1])
        pair = (x, d)
        pairs.append(pair)
        camels.add(pair)
        index += 2

    for pair in pairs:
        x, d = pair
        if d != 0:
            other = (x + d, -d)
            if other in camels:
                print("YES")
                return
    print("NO")

# CLAUSE: finish_program
main()
