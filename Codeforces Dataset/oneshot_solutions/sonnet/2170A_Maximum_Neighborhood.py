import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    
    if n == 1:
        print(1)
        return
    
    answer = 3 * n * n - n - 1  # bottom-right corner
    
    if n >= 3:
        # Best inner cell is (n-1, n-1)
        answer = max(answer, 5 * (n * n - n - 1))
        
        # Best bottom edge non-corner is (n, n-1)
        answer = max(answer, 4 * (n * n - 1) - n)
    
    print(answer)

if __name__ == "__main__":
    main()
