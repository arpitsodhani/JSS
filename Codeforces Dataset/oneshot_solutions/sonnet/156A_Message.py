import sys

def main():
    data = sys.stdin.read().split()
    s = data[0]
    u = data[1]
    
    n = len(s)
    m = len(u)
    
    best = 0
    
    for shift in range(-m + 1, n):
        matches = 0
        
        start_s = max(0, shift)
        start_u = max(0, -shift)
        length = min(n - start_s, m - start_u)
        
        for k in range(length):
            if s[start_s + k] == u[start_u + k]:
                matches += 1
        
        best = max(best, matches)
    
    print(m - best)

if __name__ == "__main__":
    main()
