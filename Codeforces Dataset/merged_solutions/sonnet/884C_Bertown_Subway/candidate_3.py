# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def collect_lengths(permutation, count):
    used = bytearray(count + 1)
    result = []
    for start in range(1, count + 1):
        if used[start]:
            continue
        node = start
        size = 0
        while not used[node]:
            used[node] = 1
            size += 1
            node = permutation[node]
        result.append(size)
    return result

def main():
    values = [int(x) for x in sys.stdin.buffer.read().split()]
    n = values[0]
    permutation = [0]
    permutation.extend(values[1:n + 1])

    cycles = collect_lengths(permutation, n)
    cycles.sort()
    if len(cycles) >= 2:
        last = cycles.pop()
        cycles[-1] += last

    answer = 0
    for size in cycles:
        answer += size * size
    print(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
