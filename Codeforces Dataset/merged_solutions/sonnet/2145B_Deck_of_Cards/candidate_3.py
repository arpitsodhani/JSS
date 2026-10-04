# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def fate_string(n, actions):
    counts = [0, 0, 0]
    for ch in actions:
        counts[ord(ch) - 48] += 1

    left, right, both = counts
    certain_left_end = left
    possible_left_end = left + both
    possible_right_start = n - right - both + 1
    certain_right_start = n - right + 1

    chars = ["+"] * n

    for i in range(certain_left_end):
        chars[i] = "-"
    for i in range(max(certain_right_start - 1, 0), n):
        chars[i] = "-"

    start = certain_left_end
    stop = min(possible_left_end, n)
    for i in range(start, stop):
        if chars[i] == "+":
            chars[i] = "?"

    start = max(possible_right_start - 1, 0)
    stop = max(certain_right_start - 1, 0)
    for i in range(start, stop):
        if chars[i] == "+":
            chars[i] = "?"

    return "".join(chars)

def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    tests = int(tokens[0])
    index = 1
    results = []

    for _ in range(tests):
        n = int(tokens[index])
        k = int(tokens[index + 1])
        actions = tokens[index + 2].decode()
        index += 3
        results.append(fate_string(n, actions))

    print("\n".join(results))

# CLAUSE: finish_program
main()
