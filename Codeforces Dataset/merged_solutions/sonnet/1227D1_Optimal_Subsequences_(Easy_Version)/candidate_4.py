# CLAUSE: setup_environment
import sys

def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    it = iter(nums)
    n = next(it)
    a = [next(it) for _ in range(n)]

# CLAUSE: solve_logic
    pairs = [(-a[i], i) for i in range(n)]
    pairs.sort()
    selected_indices = []
    optimal = [[] for _ in range(n + 1)]
    for length in range(1, n + 1):
        selected_indices.append(pairs[length - 1][1])
        selected_indices.sort()
        optimal[length] = [a[index] for index in selected_indices]

    m = next(it)
    result = []
    for _ in range(m):
        k = next(it)
        pos = next(it)
        result.append(str(optimal[k][pos - 1]))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
