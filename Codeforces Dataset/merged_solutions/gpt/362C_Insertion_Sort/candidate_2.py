# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class Fenwick:

    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum_prefix(self, i):
        if i < 0:
            return 0
        i += 1
        res = 0
        while i:
            res += self.bit[i]
            i -= i & -i
        return res

    def range_sum(self, left, right):
        if left > right:
            return 0
        return self.sum_prefix(right) - self.sum_prefix(left - 1)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:1 + n]
    inv = 0
    seen = Fenwick(n)
    for i, value in enumerate(a):
        inv += i - seen.sum_prefix(value)
        seen.add(value, 1)
    best = 0
    ways = 0
    for i in range(n):
        left_value = a[i]
        between = Fenwick(n)
        for j in range(i + 1, n):
            right_value = a[j]
            if left_value > right_value:
                middle = between.range_sum(right_value + 1, left_value - 1)
                reduction = 2 * middle + 1
                if reduction > best:
                    best = reduction
                    ways = 1
                elif reduction == best:
                    ways += 1
            between.add(right_value, 1)
    print(inv - best, ways)
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
