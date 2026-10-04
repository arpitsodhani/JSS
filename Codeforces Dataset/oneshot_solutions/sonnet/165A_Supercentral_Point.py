import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    points = []
    idx = 1
    
    for _ in range(n):
        x = data[idx]
        y = data[idx + 1]
        idx += 2
        points.append((x, y))
    
    result = 0
    
    for x, y in points:
        left = right = lower = upper = False
        
        for x2, y2 in points:
            if y2 == y:
                if x2 < x:
                    left = True
                elif x2 > x:
                    right = True
            
            if x2 == x:
                if y2 < y:
                    lower = True
                elif y2 > y:
                    upper = True
        
        if left and right and lower and upper:
            result += 1
    
    print(result)

if __name__ == "__main__":
    main()
