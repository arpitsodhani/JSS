import sys

def main():
    line = sys.stdin.readline().split()
    n, a, b = int(line[0]), int(line[1]), int(line[2])
    s = sys.stdin.readline().strip()
    
    # Find segments of consecutive empty seats
    segments = []
    i = 0
    while i < n:
        if s[i] == '.':
            start = i
            while i < n and s[i] == '.':
                i += 1
            segments.append(i - start)
        else:
            i += 1
    
    total = 0
    for length in segments:
        # For alternating pattern: larger group gets (length+1)//2, smaller gets length//2
        larger = (length + 1) // 2
        smaller = length // 2
        
        # Assign larger allocation to the type with more students available
        if a >= b:
            use_a = min(larger, a)
            use_b = min(smaller, b)
        else:
            use_b = min(larger, b)
            use_a = min(smaller, a)
        
        total += use_a + use_b
        a -= use_a
        b -= use_b
    
    print(total)

main()
