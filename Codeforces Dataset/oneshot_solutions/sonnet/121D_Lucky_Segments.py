import sys

def generate_lucky_numbers(max_val):
    if max_val < 4:
        return []
    lucky = []
    queue = [4, 7]
    idx = 0
    while idx < len(queue):
        num = queue[idx]
        idx += 1
        if num > max_val:
            continue
        lucky.append(num)
        next_4 = num * 10 + 4
        next_7 = num * 10 + 7
        if next_4 <= max_val:
            queue.append(next_4)
        if next_7 <= max_val:
            queue.append(next_7)
    return lucky

def cost_to_cover(segments, L, R):
    total_cost = 0
    for l, r in segments:
        if R - L > r - l:
            return float('inf')
        d_min = R - r
        d_max = L - l
        if d_min <= 0 <= d_max:
            d = 0
        elif d_min > 0:
            d = d_min
        else:
            d = d_max
        total_cost += abs(d)
    return total_cost

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    k = int(input_data[1])
    
    segments = []
    for i in range(n):
        l = int(input_data[2 + 2*i])
        r = int(input_data[2 + 2*i + 1])
        segments.append((l, r))
    
    min_l = min(l for l, r in segments)
    max_r = max(r for l, r in segments)
    
    search_max = max_r + k + 10000
    lucky_nums = generate_lucky_numbers(search_max)
    lucky_nums = [x for x in lucky_nums if x >= max(0, min_l - k - 10000)]
    
    if not lucky_nums:
        print(0)
        return
    
    max_count = 0
    m = len(lucky_nums)
    
    for i in range(m):
        left, right = i, m - 1
        best_j = i
        while left <= right:
            mid = (left + right) // 2
            cost = cost_to_cover(segments, lucky_nums[i], lucky_nums[mid])
            if cost <= k:
                best_j = mid
                left = mid + 1
            else:
                right = mid - 1
        max_count = max(max_count, best_j - i + 1)
    
    print(max_count)

solve()
