# CLAUSE: setup_environment
import sys

class Fenwick:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def sum(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    numbers = [int(x) for x in raw]
    swaps = numbers[0]
    where = {}

# CLAUSE: solve_logic
    for i in range(1, 2 * swaps + 1, 2):
        left = numbers[i]
        right = numbers[i + 1]
        where[left] = where.get(left, left)
        where[right] = where.get(right, right)
        where[left], where[right] = where[right], where[left]

    keys = sorted(where)
    order = {value: i for i, value in enumerate(keys)}
    ranks = {value: i + 1 for i, value in enumerate(keys)}
    bit = Fenwick(len(keys))
    answer = 0

    for seen, key in enumerate(keys):
        rank = ranks[where[key]]
        answer += seen - bit.sum(rank)
        bit.add(rank, 1)

    for key in keys:
        value = where[key]
        if value != key:
            answer += abs(value - key) - abs(order[value] - order[key])

# CLAUSE: finish_program
    print(answer)

if __name__ == "__main__":
    main()
