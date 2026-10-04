import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    idx = 1
    
    lands = []
    best_twice_area = 0
    
    for _ in range(n):
        l = int(data[idx])
        w = int(data[idx + 1])
        idx += 2
        
        a = min(l, w)
        b = max(l, w)
        lands.append((a, b))
        
        best_twice_area = max(best_twice_area, l * w)
    
    lands.sort(reverse=True)
    
    max_big = 0
    for small, big in lands:
        if max_big:
            area = small * min(big, max_big)
            best_twice_area = max(best_twice_area, 2 * area)
        max_big = max(max_big, big)
    
    print(f"{best_twice_area / 2:.1f}")

if __name__ == "__main__":
    main()
