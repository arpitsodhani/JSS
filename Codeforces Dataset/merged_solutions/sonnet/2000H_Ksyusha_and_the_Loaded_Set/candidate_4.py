# CLAUSE: setup_environment
import sys
from heapq import heappush, heappop

# CLAUSE: solve_logic
class Engine:
    def __init__(self, values, initial):
        self.values = values
        self.index = {v: i for i, v in enumerate(values)}
        self.inf = 10 ** 30
        self.left = [-1] * len(values)
        self.right = [-1] * len(values)
        self.active = [False] * len(values)
        self.heap = []

        chain = [0]
        chain.extend(sorted(set(initial)))
        previous = -1
        for value in chain:
            node = self.index[value]
            self.active[node] = True
            if previous != -1:
                self.left[node] = previous
                self.right[previous] = node
            previous = node

        for value in chain:
            node = self.index[value]
            self.add_gap(node, self.right[node])

    def size_of_gap(self, a, b):
        if b == -1:
            return self.inf
        return self.values[b] - self.values[a] - 1

    def add_gap(self, a, b):
        length = self.size_of_gap(a, b)
        if length > 0:
            heappush(self.heap, (-length, a, b))

    def insert(self, value):
        node = self.index[value]
        if self.active[node]:
            return
        before = node - 1
        while before >= 0 and not self.active[before]:
            before -= 1
        after = self.right[before]
        self.active[node] = True
        self.left[node] = before
        self.right[node] = after
        self.right[before] = node
        if after != -1:
            self.left[after] = node
        self.add_gap(before, node)
        self.add_gap(node, after)

    def remove(self, value):
        node = self.index[value]
        if not self.active[node]:
            return
        before = self.left[node]
        after = self.right[node]
        self.active[node] = False
        self.right[before] = after
        if after != -1:
            self.left[after] = before
        self.add_gap(before, after)

    def query(self, need):
        while self.heap:
            neg, a, b = self.heap[0]
            if self.active[a] and self.right[a] == b and self.size_of_gap(a, b) == -neg:
                if -neg >= need:
                    return self.values[a] + 1
                return self.values[0] + 1
            heappop(self.heap)
        return self.values[0] + 1

def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    cases = int(data[pos])
    pos += 1
    result = []

    for _ in range(cases):
        n = int(data[pos])
        m = int(data[pos + 1])
        pos += 2

        initial = []
        collected = {0}

        for _ in range(n):
            x = int(data[pos])
            pos += 1
            initial.append(x)
            collected.add(x)

        operations = []
        for _ in range(m):
            op = data[pos]
            x = int(data[pos + 1])
            pos += 2
            operations.append((op, x))
            if op != b'?':
                collected.add(x)

        engine = Engine(sorted(collected), initial)

        for op, x in operations:
            if op == b'+':
                engine.insert(x)
            elif op == b'-':
                engine.remove(x)
            else:
                result.append(str(engine.query(x)))

    sys.stdout.write("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
