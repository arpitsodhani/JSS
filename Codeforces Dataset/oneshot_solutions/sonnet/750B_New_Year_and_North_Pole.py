def solve():
    n = int(input())
    pos = 0
    
    for _ in range(n):
        parts = input().split()
        t = int(parts[0])
        direction = parts[1]
        
        # Check constraints at current position
        if pos == 0:  # At North Pole
            if direction != "South":
                return "NO"
        elif pos == 20000:  # At South Pole
            if direction != "North":
                return "NO"
        
        # Update position
        if direction == "South":
            pos += t
        elif direction == "North":
            pos -= t
        # East/West don't change position
        
        # Check bounds
        if pos < 0 or pos > 20000:
            return "NO"
    
    # Check if we end at North Pole
    if pos == 0:
        return "YES"
    else:
        return "NO"

print(solve())
