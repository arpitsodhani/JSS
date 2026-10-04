import sys

def solve():
    input_data = sys.stdin.buffer.read().decode().split()
    d = int(input_data[0])
    n = int(input_data[1])
    months = [int(input_data[i]) for i in range(2, 2 + n)]
    
    clock = 1
    adjustments = 0
    
    for month_days in months:
        # Adjust clock to 1 for the start of the month
        if clock != 1:
            adjustments += (1 - clock) % d
            clock = 1
        
        # After going through the month, clock auto-increments to month_days + 1
        clock = month_days + 1
        if clock > d:
            clock = clock - d
    
    print(adjustments)

solve()
