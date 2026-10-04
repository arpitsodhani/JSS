# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def count_pairs(sticks):
    seen = set()
    pairs = 0
    for stick in sticks:
        if stick in seen:
            seen.remove(stick)
            pairs += 1
        else:
            seen.add(stick)
    return pairs

def main():
    tokens = sys.stdin.buffer.read().split()
    if len(tokens) == 0:
        return
    amount = int(tokens[0])
    sticks = [int(token) for token in tokens[1:amount + 1]]
    answer = count_pairs(sticks) // 2

# CLAUSE: finish_program
    print(answer)

if __name__ == "__main__":
    main()
