import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    idx = 2
    
    left = 1
    right = n
    
    for _ in range(m):
        direction = data[idx + 2]
        box = int(data[idx + 4])
        idx += 5
        
        if direction == "left":
            right = min(right, box - 1)
        else:
            left = max(left, box + 1)
    
    if left > right:
        print(-1)
    else:
        print(right - left + 1)

if __name__ == "__main__":
    main()
