# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    occurrences = [0] * (n + 1)

    index = 1
    valid = True
    for _ in range(n - 1):
        a = int(tokens[index])
        b = int(tokens[index + 1])
        index += 2
        if a == n and b != n:
            occurrences[b] += 1
        elif b == n and a != n:
            occurrences[a] += 1
        else:
            valid = False
            break

    if not valid:
        sys.stdout.write("NO\n")
        return

    present = [False] * (n + 1)
    for vertex in range(1, n):
        present[vertex] = occurrences[vertex] > 0

    parent = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for vertex in range(1, n):
        if present[vertex]:
            parent[vertex] = find(vertex - 1)

    edges = []
    roots = []

    for top in range(1, n):
        times = occurrences[top]
        if times == 0:
            continue
        chain = []
        for _ in range(times - 1):
            candidate = find(top)
            if candidate == 0:
                sys.stdout.write("NO\n")
                return
            chain.append(candidate)
            parent[candidate] = find(candidate - 1)
        chain.append(top)
        roots.append(chain[0])
        for i in range(1, len(chain)):
            edges.append((chain[i - 1], chain[i]))

    for root in roots:
        edges.append((n, root))

    if len(edges) != n - 1:
        sys.stdout.write("NO\n")
        return

    result = ["YES"]
    result += ["{} {}".format(a, b) for a, b in edges]
    sys.stdout.write("\n".join(result) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
