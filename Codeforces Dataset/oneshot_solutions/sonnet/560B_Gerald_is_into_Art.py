import sys

def main():
    nums = list(map(int, sys.stdin.read().split()))
    a1, b1, a2, b2, a3, b3 = nums
    
    first = [(a2, b2), (b2, a2)]
    second = [(a3, b3), (b3, a3)]
    
    for x2, y2 in first:
        for x3, y3 in second:
            if max(x2, x3) <= a1 and y2 + y3 <= b1:
                print("YES")
                return
            if x2 + x3 <= a1 and max(y2, y3) <= b1:
                print("YES")
                return
    
    print("NO")

if __name__ == "__main__":
    main()
