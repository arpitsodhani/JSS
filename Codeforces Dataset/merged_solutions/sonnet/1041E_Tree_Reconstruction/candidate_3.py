# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def read_case():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return 0, []
    return values[0], values[1:]

def construct(n, pairs):
    frequency = [0] * (n + 1)
    for i in range(0, 2 * (n - 1), 2):
        first = pairs[i]
        second = pairs[i + 1]
        if first != n and second != n:
            return None
        other = first if second == n else second
        if other == n:
            return None
        frequency[other] += 1

    required = [i for i in range(1, n) if frequency[i] > 0]
    occupied = [False] * (n + 1)
    for item in required:
        occupied[item] = True

    spare = [i for i in range(1, n) if not occupied[i]]
    spare_index = 0
    edges = []
    starts = []

    for endpoint in required:
        chain = []
        repeats = frequency[endpoint] - 1
        for _ in range(repeats):
            if spare_index == len(spare) or spare[spare_index] > endpoint:
                return None
            chain.append(spare[spare_index])
            spare_index += 1
        chain.append(endpoint)
        starts.append(chain[0])
        previous = chain[0]
        for current in chain[1:]:
            edges.append((previous, current))
            previous = current

    edges.extend((n, start) for start in starts)
    if len(edges) != n - 1:
        return None
    return edges

def main():
    n, pairs = read_case()
    if n == 0:
        return
    answer = construct(n, pairs)
    if answer is None:
        sys.stdout.write("NO\n")
        return
    lines = ["YES"]
    for edge in answer:
        lines.append(str(edge[0]) + " " + str(edge[1]))
    sys.stdout.write("\n".join(lines) + "\n")

# CLAUSE: finish_program
main()
