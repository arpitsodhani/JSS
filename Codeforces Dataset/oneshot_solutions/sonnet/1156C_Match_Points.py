import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    z = data[1]
    points = data[2:]
    
    points.sort()
    
    left = 0
    right = n // 2
    pairs = 0
    
    while left < n // 2 and right < n:
        if points[right] - points[left] >= z:
            pairs += 1
            left += 1
            right += 1
        else:
            right += 1
    
    print(pairs)

if __name__ == "__main__":
    main()
