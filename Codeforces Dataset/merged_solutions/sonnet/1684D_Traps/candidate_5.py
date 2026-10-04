# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve_case(n, k, numbers, start):
    total = 0
    options = []
    for idx, x in enumerate(numbers[start:start + n]):
        total += x
        options.append(x + idx + 1)
    options = sorted(options, reverse=True)
    penalty = k * n - k * (k - 1) // 2
    return total + penalty - sum(options[:k])

def main():
    numbers = [int(x) for x in sys.stdin.buffer.read().split()]
    cases = numbers[0]
    pos = 1
    lines = []
    for _ in range(cases):
        n, k = numbers[pos], numbers[pos + 1]
        pos += 2
        lines.append(str(solve_case(n, k, numbers, pos)))
        pos += n
    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
main()
