# CLAUSE: setup_environment
import sys

class Reconstructor:
    def __init__(self, n):
        self.n = n
        self.children = []

    def ask(self, a, b, c):
        sys.stdout.write(str(a) + " " + str(b) + " " + str(c) + "\n")
        sys.stdout.flush()
        token = sys.stdin.readline().strip()
        if token == "X":
            return 0
        if token == "Y":
            return 1
        return 2

# CLAUSE: solve_logic
    def join(self, left, right):
        self.children.append((left, right))
        return self.n + len(self.children)

    def build(self, leaves):
        if len(leaves) < 3:
            if len(leaves) == 1:
                return leaves[0]
            return self.join(leaves[0], leaves[1])

        pivot_a = leaves[0]
        pivot_b = leaves[1]
        groups = [[pivot_a], [pivot_b]]

        pos = 2
        while pos < len(leaves):
            leaf = leaves[pos]
            reply = self.ask(pivot_a, pivot_b, leaf)
            if reply == 1:
                groups[1].append(leaf)
            else:
                groups[0].append(leaf)
            pos += 1

        return self.join(self.build(groups[0]), self.build(groups[1]))

    def parents(self, root):
        parent = [0] * (2 * self.n)
        label = self.n + 1
        for pair in self.children:
            parent[pair[0]] = label
            parent[pair[1]] = label
            label += 1
        parent[root] = -1
        return parent[1:]

def solve():
    size = int(sys.stdin.readline())
    reconstructor = Reconstructor(size)
    root = reconstructor.build(list(range(1, size + 1)))
    return reconstructor.parents(root)

# CLAUSE: finish_program
answer = solve()
sys.stdout.write("-1\n")
sys.stdout.flush()
sys.stdout.write(" ".join(map(str, answer)) + "\n")
sys.stdout.flush()
