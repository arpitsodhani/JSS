# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
def maximum_perimeter(sticks):
    freq = {}
    total = 0
    for x in sticks:
        total += x
        freq[x] = freq.get(x, 0) + 1

    ascending = sorted(freq)
    descending = ascending[::-1]
    odd_heap = [x for x in ascending if freq[x] & 1]
    heapq.heapify(odd_heap)
    removed = 0

    while len(odd_heap) > 2:
        removed += heapq.heappop(odd_heap)

    odds = set(odd_heap)

    while removed < total:
        perimeter = total - removed
        biggest = 0

        for x in descending:
            if x in odds:
                biggest = x
                break
            if freq[x] > 0:
                biggest = x
                break

        if biggest * 2 < perimeter and perimeter - removed >= 3:
            return perimeter

        if odd_heap:
            x = heapq.heappop(odd_heap)
            odds.remove(x)
            removed += x
        else:
            chosen = None
            for x in ascending:
                if freq[x] >= 2:
                    chosen = x
                    break
            if chosen is None:
                return 0
            freq[chosen] -= 2
            removed += chosen * 2

    return 0

# CLAUSE: finish_program
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    nums = [int(x) for x in data]
    t = nums[0]
    p = 1
    result = []
    for _ in range(t):
        n = nums[p]
        p += 1
        result.append(str(maximum_perimeter(nums[p:p + n])))
        p += n
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
