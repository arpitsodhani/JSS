# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    s = [int(tokens[i + 1]) for i in range(n)]
    indexed = list(enumerate(s))
    indexed.sort(key=lambda item: item[1])

    a = [0 for _ in range(n)]
    b = [0 for _ in range(n)]
    occupied = {}

    rank = 0
    for position, total in indexed:
        other = total - rank
        if other < 0 or other in occupied:
            print("NO")
            return
        a[position] = rank
        b[position] = other
        occupied[other] = True
        rank += 1

    lines = ["YES", " ".join(str(x) for x in a), " ".join(str(x) for x in b)]
    print("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
