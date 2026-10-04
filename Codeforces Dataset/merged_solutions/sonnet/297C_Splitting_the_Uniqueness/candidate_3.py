# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_split(numbers):
    n = numbers[0]
    s = numbers[1:1 + n]
    pairs = sorted((value, pos) for pos, value in enumerate(s))
    first = [0] * n
    second = [0] * n

    for rank in range(n):
        value, pos = pairs[rank]
        if value < rank:
            return None
        first[pos] = rank
        second[pos] = value - rank

    if len(set(second)) != n:
        return None

    return first, second

def main():
    numbers = [int(x) for x in sys.stdin.read().split()]
    if not numbers:
        return

    result = build_split(numbers)
    if result is None:
        print("NO")
        return

    first, second = result
    print("YES")
    print(*first)
    print(*second)

# CLAUSE: finish_program
main()
