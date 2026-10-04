# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class LazyTree:
    def __init__(self, n):
        self.n = n
        self.val = [0] * (4 * n + 16)
        self.add = [0] * (4 * n + 16)
        self.make(1, 1, n)

    def make(self, node, left, right):
        if left == right:
            self.val[node] = left
            return
        middle = (left + right) // 2
        self.make(node + node, left, middle)
        self.make(node + node + 1, middle + 1, right)
        self.val[node] = max(self.val[node + node], self.val[node + node + 1])

    def apply(self, node, delta):
        self.val[node] += delta
        self.add[node] += delta

    def push(self, node):
        delta = self.add[node]
        if delta:
            self.apply(node + node, delta)
            self.apply(node + node + 1, delta)
            self.add[node] = 0

    def update(self, need_left, need_right, node, left, right):
        if need_left <= left and right <= need_right:
            self.apply(node, 1)
            return
        self.push(node)
        middle = (left + right) // 2
        if need_left <= middle:
            self.update(need_left, need_right, node + node, left, middle)
        if need_right > middle:
            self.update(need_left, need_right, node + node + 1, middle + 1, right)
        self.val[node] = max(self.val[node + node], self.val[node + node + 1])

    def ask(self, need_left, need_right, node, left, right):
        if need_left <= left and right <= need_right:
            return self.val[node]
        self.push(node)
        middle = (left + right) // 2
        best = -10**18
        if need_left <= middle:
            best = self.ask(need_left, need_right, node + node, left, middle)
        if need_right > middle:
            other = self.ask(need_left, need_right, node + node + 1, middle + 1, right)
            best = other if other > best else best
        return best

def feasible(m, buckets, zero_count):
    color_count = len(buckets)
    if m == 0:
        return True
    if zero_count < 2 * m or color_count < m:
        return False
    start_limits = [[] for _ in range(m + 2)]
    middle_right = zero_count - m
    for positions in buckets:
        before = 0
        after = m + 1
        free = False
        for z in positions:
            if z >= m and z <= middle_right:
                free = True
                break
            if z < m:
                before = max(before, z)
            else:
                after = min(after, z - zero_count + m + 1)
        if free:
            continue
        left = before + 1
        right = after - 1
        if left <= right:
            start_limits[left].append(right)
    tree = LazyTree(m)
    need = color_count
    left = 1
    while left <= m:
        for right in start_limits[left]:
            tree.update(1, right, 1, 1, m)
        if tree.ask(left, m, 1, 1, m) - left + 1 > need:
            return False
        left += 1
    return True

def compute(a):
    zero_count = 0
    where = {}
    for value in a:
        if value == 0:
            zero_count += 1
        else:
            where.setdefault(value, []).append(zero_count)
    buckets = list(where.values())
    lo = 0
    hi = min(zero_count // 2, len(buckets))
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if feasible(mid, buckets, zero_count):
            lo = mid
        else:
            hi = mid - 1
    if feasible(hi, buckets, zero_count):
        return hi
    return lo

# CLAUSE: finish_program
def main():
    stream = list(map(int, sys.stdin.buffer.read().split()))
    cases = stream[0]
    ptr = 1
    ans = []
    for _ in range(cases):
        n = stream[ptr]
        ptr += 1
        arr = stream[ptr:ptr + n]
        ptr += n
        ans.append(str(compute(arr)))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
