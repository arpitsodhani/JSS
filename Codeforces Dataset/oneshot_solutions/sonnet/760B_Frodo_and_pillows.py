def calculate_pillows(x, left_dist, right_dist):
    total = x
    
    # Left side
    if left_dist > 0:
        if x > left_dist:
            # Sum from (x-1) down to (x-left_dist)
            total += left_dist * (2 * x - left_dist - 1) // 2
        else:
            # Sum from (x-1) down to 1, then add 1s for remaining
            total += (x - 1) * x // 2 + (left_dist - x + 1)
    
    # Right side
    if right_dist > 0:
        if x > right_dist:
            # Sum from (x-1) down to (x-right_dist)
            total += right_dist * (2 * x - right_dist - 1) // 2
        else:
            # Sum from (x-1) down to 1, then add 1s for remaining
            total += (x - 1) * x // 2 + (right_dist - x + 1)
    
    return total

n, m, k = map(int, input().split())

left = 1
right = m
answer = 1

left_dist = k - 1
right_dist = n - k

while left <= right:
    mid = (left + right) // 2
    total = calculate_pillows(mid, left_dist, right_dist)
    
    if total <= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
