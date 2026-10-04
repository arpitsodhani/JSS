# CLAUSE: setup_environment
import sys

def common_number(a, b, c, d):
    result = 0
    count = 0
    if a == c or a == d:
        result = a
        count += 1
    if b == c or b == d:
        result = b
        count += 1
    if count == 1:
        return result
    return 0

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    numbers = list(map(int, raw))
    n = numbers[0]
    m = numbers[1]
    first = [(numbers[i], numbers[i + 1]) for i in range(2, 2 + 2 * n, 2)]
    base = 2 + 2 * n
    second = [(numbers[i], numbers[i + 1]) for i in range(base, base + 2 * m, 2)]

    by_first = [set() for _ in range(n)]
    by_second = [set() for _ in range(m)]
    total = set()

    for i, (a, b) in enumerate(first):
        for j, (c, d) in enumerate(second):
            value = common_number(a, b, c, d)
            if value:
                by_first[i].add(value)
                by_second[j].add(value)
                total.add(value)

    if len(total) == 1:
        sys.stdout.write(str(next(iter(total))))
        return

    if any(len(values) > 1 for values in by_first):
        sys.stdout.write("-1")
        return

    if any(len(values) > 1 for values in by_second):
        sys.stdout.write("-1")
        return

    sys.stdout.write("0")

# CLAUSE: finish_program
main()
