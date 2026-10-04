# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def make_solver(n):
    parent = list(range(n))
    weight = [1] * n

    def leader(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def merge(x, y):
        x = leader(x)
        y = leader(y)
        if x == y:
            return False
        if weight[x] < weight[y]:
            x, y = y, x
        parent[y] = x
        weight[x] += weight[y]
        return True

    return leader, merge

def possible_edges(n, numbers):
    leader, merge = make_solver(n)
    stack = []

    for divisor in reversed(range(1, n)):
        seen = {}
        add_u = -1
        add_v = -1

        for vertex, number in enumerate(numbers):
            residue = number % divisor
            previous = seen.get(residue)

            if previous is None:
                seen[residue] = vertex
                continue

            if leader(vertex) != leader(previous):
                merge(vertex, previous)
                add_u = vertex + 1
                add_v = previous + 1
                break

        if add_u < 0:
            return None
        stack.append((add_u, add_v))

    return list(reversed(stack))

# CLAUSE: finish_program
def main():
    raw = sys.stdin.buffer.read().split()
    index = 0
    total = int(raw[index])
    index += 1
    output = []

    for _ in range(total):
        n = int(raw[index])
        index += 1
        numbers = [int(x) for x in raw[index:index + n]]
        index += n

        edges = possible_edges(n, numbers)
        if edges is None:
            output.append("NO")
        else:
            output.append("YES")
            output += [f"{u} {v}" for u, v in edges]

    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
