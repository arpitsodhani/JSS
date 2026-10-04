import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    a = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(data[idx]))
            idx += 1
        a.append(row)
    
    def can_achieve(threshold):
        # Create bitmask for each array
        masks = []
        for i in range(n):
            mask = 0
            for j in range(m):
                if a[i][j] >= threshold:
                    mask |= (1 << j)
            masks.append(mask)
        
        full_mask = (1 << m) - 1
        
        # Map unique masks to array indices
        mask_to_idx = {}
        for i in range(n):
            if masks[i] not in mask_to_idx:
                mask_to_idx[masks[i]] = i
        
        # Check if any pair of masks ORs to full_mask
        for mask1 in mask_to_idx:
            for mask2 in mask_to_idx:
                if (mask1 | mask2) == full_mask:
                    return True, mask_to_idx[mask1], mask_to_idx[mask2]
        
        return False, -1, -1
    
    # Get all unique values
    all_values = set()
    for i in range(n):
        for j in range(m):
            all_values.add(a[i][j])
    all_values = sorted(all_values)
    
    # Binary search
    best_i, best_j = 0, 0
    left, right = 0, len(all_values) - 1
    
    while left <= right:
        mid = (left + right) // 2
        threshold = all_values[mid]
        success, i, j = can_achieve(threshold)
        if success:
            best_i, best_j = i, j
            left = mid + 1
        else:
            right = mid - 1
    
    print(best_i + 1, best_j + 1)

main()
