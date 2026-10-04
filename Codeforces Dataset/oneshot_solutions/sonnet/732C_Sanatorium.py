import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    a = data[:3]
    
    total = sum(a)
    if total == 0:
        print(0)
        return
    
    def possible(length, start):
        q, r = divmod(length, 3)
        have = [q, q, q]
        for i in range(r):
            have[(start + i) % 3] += 1
        
        for i in range(3):
            if have[i] < a[i]:
                return False
        return True
    
    best = 3 * max(a) + 2
    for start in range(3):
        low, high = 0, best
        while low < high:
            mid = (low + high) // 2
            if possible(mid, start):
                high = mid
            else:
                low = mid + 1
        best = min(best, low)
    
    print(best - total)

if __name__ == "__main__":
    main()
