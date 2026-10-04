# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
def main():
    data = sys.stdin.readline().split()
    if not data:
        return
    n, m = map(int, data)

    if m < n - 1:
        print("Impossible")
        return

    edges = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if gcd(i, j) == 1:
                edges.append((i, j))
                if len(edges) == m:
                    print("Possible")
                    print("\n".join(f"{a} {b}" for a, b in edges))
                    return

    print("Impossible")

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
