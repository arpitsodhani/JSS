# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    p = [int(x) for x in raw[1:n + 1]]

    remaining = set(range(1, n + 1))
    total = 0
    largest = 0
    second = 0

    while remaining:
        node = next(iter(remaining))
        length = 0
        while node in remaining:
            remaining.remove(node)
            length += 1
            node = p[node - 1]

        total += length * length
        if length > largest:
            second = largest
            largest = length
        elif length > second:
            second = length

    total += 2 * largest * second
    sys.stdout.write(str(total))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
