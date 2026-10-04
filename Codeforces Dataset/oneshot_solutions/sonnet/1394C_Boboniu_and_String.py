import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    
    points = []
    for s in data[1:]:
        b = s.count('B')
        c = len(s) - b
        points.append((b + c, b - c))
    
    def ok(radius):
        low_u = 1
        high_u = 10 ** 18
        low_v = -10 ** 18
        high_v = 10 ** 18
        
        for u, v in points:
            low_u = max(low_u, u - radius)
            high_u = min(high_u, u + radius)
            low_v = max(low_v, v - radius)
            high_v = min(high_v, v + radius)
        
        if low_u > high_u or low_v > high_v:
            return None
        
        u = low_u
        if u % 2 != low_v % 2:
            low_v += 1
        
        if low_v > high_v:
            u += 1
            if u > high_u:
                return None
            if u % 2 != low_v % 2:
                low_v += 1
            if low_v > high_v:
                return None
        
        v = low_v
        b = (u + v) // 2
        c = (u - v) // 2
        
        if b < 0 or c < 0 or b + c == 0:
            return None
        
        return b, c
    
    left = 0
    right = 10 ** 6
    
    while left < right:
        mid = (left + right) // 2
        if ok(mid) is not None:
            right = mid
        else:
            left = mid + 1
    
    b, c = ok(left)
    print(left)
    print('B' * b + 'N' * c)

if __name__ == "__main__":
    main()
