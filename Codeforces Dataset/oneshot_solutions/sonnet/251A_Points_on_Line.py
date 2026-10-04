import sys

def main():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    d = int(input_data[1])
    points = list(map(int, input_data[2:2+n]))
    
    points.sort()
    
    count = 0
    r = 0
    
    for i in range(n):
        # Move r to the right as far as possible
        while r < n and points[r] - points[i] <= d:
            r += 1
        # Now r is one past the rightmost valid index
        
        # Number of ways to choose 2 more points from i+1 to r-1
        valid_range = r - 1 - i
        if valid_range >= 2:
            count += valid_range * (valid_range - 1) // 2
    
    print(count)

if __name__ == "__main__":
    main()
