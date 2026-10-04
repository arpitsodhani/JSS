import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    
    m = data[0]
    counts = data[1:1 + m]
    x, y = data[1 + m], data[2 + m]
    
    total = sum(counts)
    beginners = 0
    
    for k in range(1, m + 1):
        intermediate = total - beginners
        if x <= beginners <= y and x <= intermediate <= y:
            print(k)
            return
        beginners += counts[k - 1]
    
    print(0)

if __name__ == "__main__":
    main()
