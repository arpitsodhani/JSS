import sys

def can_fit(bottles, height):
    arr = sorted(bottles, reverse=True)
    needed = 0
    
    for i in range(0, len(arr), 2):
        needed += arr[i]
    
    return needed <= height

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    h = data[1]
    a = data[2:]
    
    low = 0
    high = n
    
    while low < high:
        mid = (low + high + 1) // 2
        
        if can_fit(a[:mid], h):
            low = mid
        else:
            high = mid - 1
    
    print(low)

if __name__ == "__main__":
    main()
