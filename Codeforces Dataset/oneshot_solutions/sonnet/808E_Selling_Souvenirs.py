import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    
    # Group by weight (assuming weights are 1, 2, or 3)
    items = [[], [], [], []]
    
    for _ in range(n):
        w = int(data[idx])
        c = int(data[idx + 1])
        idx += 2
        if 1 <= w <= 3 and w <= m:
            items[w].append(c)
    
    # Sort descending by cost
    for w in range(1, 4):
        items[w].sort(reverse=True)
    
    # Compute prefix sums for quick range sum queries
    prefix = [[], [], [], []]
    for w in range(1, 4):
        prefix[w] = [0]
        for cost in items[w]:
            prefix[w].append(prefix[w][-1] + cost)
    
    result = 0
    
    # Enumerate all valid combinations of items
    for cnt3 in range(min(len(items[3]) + 1, m // 3 + 1)):
        remaining = m - 3 * cnt3
        for cnt2 in range(min(len(items[2]) + 1, remaining // 2 + 1)):
            remaining2 = remaining - 2 * cnt2
            cnt1 = min(len(items[1]), remaining2)
            total = prefix[1][cnt1] + prefix[2][cnt2] + prefix[3][cnt3]
            result = max(result, total)
    
    print(result)

if __name__ == "__main__":
    main()
