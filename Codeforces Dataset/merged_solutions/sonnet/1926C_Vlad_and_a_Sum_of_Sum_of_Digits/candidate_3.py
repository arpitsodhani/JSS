# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    count = values[0]
    queries = values[1:count + 1]
    top = max(queries) if queries else 0
    digit = [0] * (top + 1)
    total = [0] * (top + 1)
    for number in range(1, top + 1):
        digit[number] = digit[number // 10] + number % 10
        total[number] = total[number - 1] + digit[number]
    out = []
    for item in queries:
        out.append(str(total[item]))
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
main()
