# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
def take_mex(freq):
    value = 0
    while freq[value]:
        freq[value] -= 1
        value += 1
    return value

def main():
    tokens = sys.stdin.buffer.read().split()
    tests = int(tokens[0])
    pos = 1
    result = []
    for _ in range(tests):
        n = int(tokens[pos])
        pos += 1
        arr = map(int, tokens[pos:pos + n])
        pos += n
        freq = Counter(arr)
        result.append(str(take_mex(freq) + take_mex(freq)))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
