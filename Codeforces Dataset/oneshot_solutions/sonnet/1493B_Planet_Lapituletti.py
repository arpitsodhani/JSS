import sys

def mirror_digit(d):
    mapping = {'0': '0', '1': '1', '2': '5', '5': '2', '8': '8'}
    return mapping.get(d, None)

def mirror_time(hh, mm):
    time_str = f"{hh:02d}:{mm:02d}"
    
    # Check if all digits can be mirrored
    for char in time_str:
        if char != ':' and mirror_digit(char) is None:
            return None
    
    # Mirror: reverse positions and mirror each digit
    # Original: d0 d1 : d3 d4
    # Mirrored: mirror(d4) mirror(d3) : mirror(d1) mirror(d0)
    mirrored = (mirror_digit(time_str[4]) + 
                mirror_digit(time_str[3]) + ':' + 
                mirror_digit(time_str[1]) + 
                mirror_digit(time_str[0]))
    
    mirror_hh, mirror_mm = map(int, mirrored.split(':'))
    return mirror_hh, mirror_mm

def solve(h, m, start_hh, start_mm):
    hh, mm = start_hh, start_mm
    
    for _ in range(h * m):
        result = mirror_time(hh, mm)
        
        if result is not None:
            mirror_hh, mirror_mm = result
            if mirror_hh < h and mirror_mm < m:
                return f"{hh:02d}:{mm:02d}"
        
        # Increment time
        mm += 1
        if mm >= m:
            mm = 0
            hh += 1
            if hh >= h:
                hh = 0
    
    return "00:00"

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    h, m = map(int, input().split())
    time_str = input().strip()
    hh, mm = map(int, time_str.split(':'))
    print(solve(h, m, hh, mm))
