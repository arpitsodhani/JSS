# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n, q = values[0], values[1]
    deck = values[2:2 + n]
    queries = values[2 + n:2 + n + q]
    ans = []

    for color in queries:
        pos = deck.index(color)
        ans.append(str(pos + 1))
        deck.insert(0, deck.pop(pos))

    sys.stdout.write(" ".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
