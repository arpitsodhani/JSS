# CLAUSE: setup_environment
import sys
from bisect import bisect_right
from collections import deque

LIMIT = 10 ** 45

# CLAUSE: solve_logic
class RangeMinimum:
    def __init__(self, items):
        self.n = len(items)
        self.base = 1
        while self.base < self.n:
            self.base *= 2
        self.values = [LIMIT] * (2 * self.base)
        for i, item in enumerate(items):
            self.values[self.base + i] = item
        for i in range(self.base - 1, 0, -1):
            self.values[i] = min(self.values[2 * i], self.values[2 * i + 1])

    def clear(self, pos):
        pos += self.base
        self.values[pos] = LIMIT
        pos //= 2
        while pos:
            self.values[pos] = min(self.values[pos * 2], self.values[pos * 2 + 1])
            pos //= 2

    def find(self, right, cap):
        if right < 0 or self.values[1] > cap:
            return -1
        node = 1
        left = 0
        high = self.base - 1
        while left < high:
            mid = (left + high) // 2
            first = node * 2
            if left <= right and self.values[first] <= cap:
                node = first
                high = mid
            else:
                node = first + 1
                left = mid + 1
        if left < self.n and left <= right and self.values[node] <= cap:
            return left
        return -1

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return
    n = nums[0]
    cards = [(0, 0, 0, 0)]
    at = 1
    for _ in range(n):
        cards.append((nums[at], nums[at + 1], nums[at + 2], nums[at + 3]))
        at += 4

    positions = sorted(range(1, n + 1), key=lambda card: cards[card][0])
    sorted_need_x = [cards[card][0] for card in positions]
    rmq = RangeMinimum([cards[card][1] for card in positions])

    parent = [-1] * (n + 1)
    distance = [-1] * (n + 1)
    pending = deque([(0, 0, 0)])

    while pending and distance[n] == -1:
        x, y, origin = pending.popleft()
        edge_limit = bisect_right(sorted_need_x, x) - 1
        while True:
            hit = rmq.find(edge_limit, y)
            if hit == -1:
                break
            card = positions[hit]
            parent[card] = origin
            distance[card] = 1 if origin == 0 else distance[origin] + 1
            rmq.clear(hit)
            pending.append((cards[card][2], cards[card][3], card))

    if distance[n] == -1:
        sys.stdout.write("-1\n")
        return

    path = []
    while n:
        path.append(n)
        n = parent[n]
    path.reverse()
    sys.stdout.write("{}\n{}\n".format(len(path), " ".join(map(str, path))))

# CLAUSE: finish_program
main()
