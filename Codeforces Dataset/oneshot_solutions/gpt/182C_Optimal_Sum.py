import sys

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        n = self.n
        while i <= n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def lower_bound(self, target):
        idx = 0
        bit = 1 << (self.n.bit_length() - 1)
        while bit:
            nxt = idx + bit
            if nxt <= self.n and self.bit[nxt] < target:
                idx = nxt
                target -= self.bit[nxt]
            bit >>= 1
        return idx + 1

class TopK:
    def __init__(self, values):
        self.values = values
        self.index = {v: i + 1 for i, v in enumerate(values)}
        self.counts = Fenwick(len(values))
        self.sums = Fenwick(len(values))
        self.total_count = 0
        self.total_sum = 0

    def add(self, value, delta):
        i = self.index[value]
        self.counts.add(i, delta)
        self.sums.add(i, value * delta)
        self.total_count += delta
        self.total_sum += value * delta

    def top_sum(self, k):
        if k <= 0 or self.total_count == 0:
            return 0
        if k >= self.total_count:
            return self.total_sum
        small = self.total_count - k
        idx = self.counts.lower_bound(small)
        before_count = self.counts.sum(idx - 1)
        before_sum = self.sums.sum(idx - 1)
        value = self.values[idx - 1]
        smallest_sum = before_sum + (small - before_count) * value
        return self.total_sum - smallest_sum

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, length = data[0], data[1]
    arr = data[2:2 + n]
    k = data[2 + n]

    values = sorted({abs(x) for x in arr if x != 0})
    if not values:
        print(0)
        return

    positives = TopK(values)
    negatives = TopK(values)

    def include(x):
        if x > 0:
            positives.add(x, 1)
        elif x < 0:
            negatives.add(-x, 1)

    def exclude(x):
        if x > 0:
            positives.add(x, -1)
        elif x < 0:
            negatives.add(-x, -1)

    window_sum = 0
    for i in range(length):
        window_sum += arr[i]
        include(arr[i])

    ans = 0
    for left in range(n - length + 1):
        ans = max(
            ans,
            window_sum + 2 * negatives.top_sum(k),
            -window_sum + 2 * positives.top_sum(k)
        )

        right = left + length
        if right < n:
            old = arr[left]
            new = arr[right]
            exclude(old)
            include(new)
            window_sum += new - old

    print(ans)

if __name__ == "__main__":
    main()
