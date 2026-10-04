import sys

def can_fit(parts, k, width):
    lines = 1
    current = 0
    
    for length in parts:
        if length > width:
            return False
        
        if current + length <= width:
            current += length
        else:
            lines += 1
            current = length
    
    return lines <= k

def main():
    data = sys.stdin.read().splitlines()
    k = int(data[0])
    text = data[1] if len(data) > 1 else ""
    
    parts = []
    current = 0
    
    for ch in text:
        current += 1
        if ch == ' ' or ch == '-':
            parts.append(current)
            current = 0
    
    if current:
        parts.append(current)
    
    low = max(parts)
    high = sum(parts)
    
    while low < high:
        mid = (low + high) // 2
        if can_fit(parts, k, mid):
            high = mid
        else:
            low = mid + 1
    
    print(low)

if __name__ == "__main__":
    main()
