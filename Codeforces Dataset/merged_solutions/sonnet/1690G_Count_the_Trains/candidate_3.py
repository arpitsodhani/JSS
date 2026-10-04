# CLAUSE: setup_environment
import sys

class SegmentTree:
    def __init__(self, n):
        self.n = n
        size = 1
        while size < n:
            size <<= 1
        self.size = size
        self.data = [0] * (size << 1)

    def set_one(self, pos):
        i = pos + self.size - 1
        if self.data[i] == 1:
            return
        self.data[i] = 1
        i >>= 1
        while i:
            self.data[i] = self.data[i << 1] + self.data[i << 1 | 1]
            i >>= 1

    def set_zero(self, pos):
        i = pos + self.size - 1
        if self.data[i] == 0:
            return
        self.data[i] = 0
        i >>= 1
        while i:
            self.data[i] = self.data[i << 1] + self.data[i << 1 | 1]
            i >>= 1

    def prefix(self, right):
        if right <= 0:
            return 0
        l = self.size
        r = self.size + right
        s = 0
        data = self.data
        while l < r:
            if l & 1:
                s += data[l]
                l += 1
            if r & 1:
                r -= 1
                s += data[r]
            l >>= 1
            r >>= 1
        return s

    def kth(self, order):
        node = 1
        while node < self.size:
            left = node << 1
            if self.data[left] >= order:
                node = left
            else:
                order -= self.data[left]
                node = left | 1
        return node - self.size + 1

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    at = 0
    cases = nums[at]
    at += 1
    result_lines = []
    for _ in range(cases):
        n = nums[at]
        m = nums[at + 1]
        at += 2
        speed = [0]
        speed.extend(nums[at:at + n])
        at += n
        seg = SegmentTree(n)
        mark = [0] * (n + 1)
        lowest = None
        trains = 0
        for pos, val in enumerate(speed[1:], 1):
            if lowest is None or val < lowest:
                lowest = val
                mark[pos] = 1
                seg.set_one(pos)
                trains += 1
        row = []
        for _ in range(m):
            pos = nums[at]
            dec = nums[at + 1]
            at += 2
            speed[pos] -= dec
            if mark[pos] == 0:
                prior = seg.prefix(pos - 1)
                pred = seg.kth(prior)
                if speed[pos] >= speed[pred]:
                    row.append(str(trains))
                    continue
                mark[pos] = 1
                seg.set_one(pos)
                trains += 1
            upto = seg.prefix(pos)
            while upto != trains:
                candidate = seg.kth(upto + 1)
                if speed[candidate] < speed[pos]:
                    break
                mark[candidate] = 0
                seg.set_zero(candidate)
                trains -= 1
            row.append(str(trains))
        result_lines.append(" ".join(row))
    print("\n".join(result_lines))

# CLAUSE: finish_program
main()
