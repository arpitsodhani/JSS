# CLAUSE: setup_environment
import sys

sys.setrecursionlimit(300000)

# CLAUSE: solve_logic
class Solver:
    def __init__(self, n):
        self.n = n
        self.cache = {}
        self.finished = [False] * (n + 1)
        self.amount = [0] * (n + 1)
        self.reach = [[False] * (n + 1) for _ in range(n + 1)]
        self.edges = []
        self.edge_set = set()

    def line(self):
        s = sys.stdin.readline()
        while s and s.strip() == "":
            s = sys.stdin.readline()
        return s

    def ask(self, k):
        if k in self.cache:
            return self.cache[k]
        print("?", k, flush=True)
        s = self.line()
        if not s:
            path = []
        else:
            data = list(map(int, s.split()))
            path = data[1:] if data[0] != 0 else []
        self.cache[k] = path
        return path

    def attach(self, u, v):
        if (u, v) in self.edge_set:
            return
        self.edge_set.add((u, v))
        self.edges.append((u, v))
        left = [a for a in range(1, self.n + 1) if a == u or self.reach[a][u]]
        right = [b for b in range(1, self.n + 1) if b == v or self.reach[v][b]]
        for a in left:
            row = self.reach[a]
            for b in right:
                row[b] = True

    def still_possible(self, v, seen_until):
        return any(x != v and not self.reach[x][v] for x in range(seen_until + 1, self.n + 1))

    def prefixed(self, path, prefix):
        return len(path) >= len(prefix) and all(path[i] == prefix[i] for i in range(len(prefix)))

    def expand(self, prefix, pos):
        v = prefix[-1]
        if self.finished[v]:
            return self.amount[v]
        total = 1
        next_index = pos + 1
        last = 0
        while self.still_possible(v, last):
            path = self.ask(next_index)
            if not self.prefixed(path, prefix):
                total = next_index - pos
                self.amount[v] = total
                self.finished[v] = True
                return total
            child = path[len(prefix)]
            self.attach(v, child)
            gained = self.amount[child] if self.finished[child] else self.expand(path, next_index)
            total += gained
            next_index += gained
            last = child
        self.amount[v] = total
        self.finished[v] = True
        return total

    def run(self):
        pos = 1
        for vertex in range(1, self.n + 1):
            if self.finished[vertex]:
                pos += self.amount[vertex]
                continue
            path = self.ask(pos)
            if not path:
                break
            self.expand(path, pos)
            pos += self.amount[vertex]
        print("!", len(self.edges), flush=True)
        for u, v in self.edges:
            print(u, v, flush=True)

def read_nonempty():
    s = sys.stdin.readline()
    while s and s.strip() == "":
        s = sys.stdin.readline()
    return s

def main():
    first = read_nonempty()
    if not first:
        return
    t = int(first)
    for _ in range(t):
        line = read_nonempty()
        if not line:
            return
        Solver(int(line)).run()

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
