import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, w, k = data[0], data[1], data[2]
    a = data[3:3 + n]
    t = data[3 + n:3 + 2 * n]
    save = [x // 2 for x in t]

    small = []
    large = []
    alive = [False] * n
    loc = [''] * n
    size_small = 0
    size_large = 0
    sum_large = 0
    total = 0

    def prune_small():
        while small and not alive[small[0][1]]:
            heapq.heappop(small)

    def prune_large():
        while large and not alive[large[0][1]]:
            heapq.heappop(large)

    def move_small_to_large():
        nonlocal size_small, size_large, sum_large
        prune_small()
        val_neg, idx = heapq.heappop(small)
        val = -val_neg
        size_small -= 1
        size_large += 1
        sum_large += val
        loc[idx] = 'L'
        heapq.heappush(large, (val, idx))

    def move_large_to_small():
        nonlocal size_small, size_large, sum_large
        prune_large()
        val, idx = heapq.heappop(large)
        size_large -= 1
        sum_large -= val
        size_small += 1
        loc[idx] = 'S'
        heapq.heappush(small, (-val, idx))

    def rebalance():
        nonlocal sum_large
        prune_small()
        prune_large()

        need = min(w, total)

        while size_large > need:
            move_large_to_small()
            prune_large()

        while size_large < need and size_small > 0:
            move_small_to_large()
            prune_small()

        while small and large:
            prune_small()
            prune_large()
            if not small or not large:
                break
            low_val = -small[0][0]
            high_val = large[0][0]
            if low_val <= high_val:
                break

            _, low_idx = heapq.heappop(small)
            _, high_idx = heapq.heappop(large)

            size_small_dummy = None

            loc[low_idx] = 'L'
            loc[high_idx] = 'S'
            sum_large += low_val - high_val

            heapq.heappush(small, (-high_val, high_idx))
            heapq.heappush(large, (low_val, low_idx))

    def add(idx):
        nonlocal size_small, size_large, sum_large, total
        val = save[idx]
        alive[idx] = True
        total += 1

        prune_large()
        if large and val >= large[0][0]:
            loc[idx] = 'L'
            size_large += 1
            sum_large += val
            heapq.heappush(large, (val, idx))
        else:
            loc[idx] = 'S'
            size_small += 1
            heapq.heappush(small, (-val, idx))

        rebalance()

    def remove(idx):
        nonlocal size_small, size_large, sum_large, total
        val = save[idx]
        alive[idx] = False
        total -= 1

        if loc[idx] == 'L':
            size_large -= 1
            sum_large -= val
        else:
            size_small -= 1

        prune_small()
        prune_large()
        rebalance()

    ans = 0
    left = 0
    sum_t = 0
    sum_a = 0

    for right in range(n):
        add(right)
        sum_t += t[right]
        sum_a += a[right]

        while left <= right and sum_t - sum_large > k:
            remove(left)
            sum_t -= t[left]
            sum_a -= a[left]
            left += 1

        if sum_a > ans:
            ans = sum_a

    print(ans)

if __name__ == "__main__":
    main()
