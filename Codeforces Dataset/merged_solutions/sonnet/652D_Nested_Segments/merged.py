# Clause setup_environment [Confidence: 0.40]
import sys

class CounterTree:
    def __init__(self, size):
        self.data = [0] * (size + 1)
        self.size = size

    def put(self, index):
        while index <= self.size:
            self.data[index] += 1
            index += index & -index

    def take(self, index):
        value = 0
        data = self.data
        while index:
            value += data[index]
            index -= index & -index
        return value


# Clause solve_logic [Confidence: 0.60]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    segs = []
    rights = []
    p = 1
    for i in range(n):
        l = data[p]
        r = data[p + 1]
        p += 2
        segs.append((l, r, i))
        rights.append(r)

    rank = {v: i + 1 for i, v in enumerate(sorted(rights))}
    segs.sort(key=lambda x: -x[0])

    tree = Fenwick(n)
    ans = [0] * n
    for l, r, i in segs:
        k = rank[r]
        ans[i] = tree.query(k - 1)
        tree.add(k, 1)

    sys.stdout.write("\n".join(map(str, ans)))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


