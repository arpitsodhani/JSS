# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
class RangeMaximum:
    def __init__(self, size):
        self.size = size
        self.best = [0] * (size * 4 + 10)
        self.tag = [0] * (size * 4 + 10)
        stack = [(1, 1, size, 0)]
        while stack:
            node, left, right, seen = stack.pop()
            if left == right:
                self.best[node] = left
            elif seen:
                a = self.best[node * 2]
                b = self.best[node * 2 + 1]
                self.best[node] = a if a > b else b
            else:
                mid = (left + right) // 2
                stack.append((node, left, right, 1))
                stack.append((node * 2 + 1, mid + 1, right, 0))
                stack.append((node * 2, left, mid, 0))

    def bump(self, node, value):
        self.best[node] += value
        self.tag[node] += value

    def spread(self, node):
        value = self.tag[node]
        if value:
            self.bump(node * 2, value)
            self.bump(node * 2 + 1, value)
            self.tag[node] = 0

    def increase(self, left_need, right_need):
        stack = [(1, 1, self.size, 0)]
        touched = []
        while stack:
            node, left, right, state = stack.pop()
            if state:
                a = self.best[node * 2]
                b = self.best[node * 2 + 1]
                self.best[node] = a if a > b else b
                continue
            if right < left_need or right_need < left:
                continue
            if left_need <= left and right <= right_need:
                self.bump(node, 1)
                continue
            self.spread(node)
            mid = (left + right) // 2
            stack.append((node, left, right, 1))
            stack.append((node * 2 + 1, mid + 1, right, 0))
            stack.append((node * 2, left, mid, 0))
            touched.append(node)

    def maximum(self, left_need, right_need):
        ans = -10**18
        stack = [(1, 1, self.size)]
        while stack:
            node, left, right = stack.pop()
            if right < left_need or right_need < left:
                continue
            if left_need <= left and right <= right_need:
                if self.best[node] > ans:
                    ans = self.best[node]
                continue
            self.spread(node)
            mid = (left + right) // 2
            stack.append((node * 2 + 1, mid + 1, right))
            stack.append((node * 2, left, mid))
        return ans

def possible(count, groups, zero_total, distinct_total):
    if count == 0:
        return True
    if zero_total < count + count or distinct_total < count:
        return False
    begin_at = [[] for _ in range(count + 2)]
    center_low = count
    center_high = zero_total - count
    for seen_zeros in groups.values():
        left_block = 0
        right_block = count + 1
        usable = False
        for z in seen_zeros:
            if center_low <= z <= center_high:
                usable = True
                break
            if z < center_low:
                left_block = max(left_block, z)
            else:
                right_block = min(right_block, z - zero_total + count + 1)
        if not usable:
            first = left_block + 1
            last = right_block - 1
            if first <= last:
                begin_at[first].append(last)
    structure = RangeMaximum(count)
    for first in range(1, count + 1):
        for last in begin_at[first]:
            structure.increase(1, last)
        if structure.maximum(first, count) >= distinct_total + first:
            return False
    return True

def answer_one(values):
    zero_seen = 0
    groups = defaultdict(list)
    for value in values:
        if value == 0:
            zero_seen += 1
        else:
            groups[value].append(zero_seen)
    distinct = len(groups)
    left = 0
    right = min(distinct, zero_seen // 2)
    while left <= right:
        mid = (left + right) // 2
        if possible(mid, groups, zero_seen, distinct):
            left = mid + 1
        else:
            right = mid - 1
    return right

# CLAUSE: finish_program
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    t = nums[0]
    at = 1
    res = [""] * t
    for case in range(t):
        n = nums[at]
        at += 1
        res[case] = str(answer_one(nums[at:at + n]))
        at += n
    print("\n".join(res))

if __name__ == "__main__":
    main()
