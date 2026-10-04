import sys
from math import isqrt

def digit_sum(x):
    total = 0
    while x:
        total += x % 10
        x //= 10
    return total

def main():
    n = int(sys.stdin.readline())
    
    root = isqrt(n)
    answer = -1
    
    for x in range(max(1, root - 200), root + 1):
        if x * x + digit_sum(x) * x == n:
            answer = x
            break
    
    print(answer)

if __name__ == "__main__":
    main()
