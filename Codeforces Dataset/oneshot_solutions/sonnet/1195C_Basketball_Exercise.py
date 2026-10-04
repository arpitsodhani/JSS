import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    top = data[1:1 + n]
    bottom = data[1 + n:1 + 2 * n]
    
    take_top = 0
    take_bottom = 0
    skip = 0
    
    for i in range(n):
        new_top = max(skip, take_bottom) + top[i]
        new_bottom = max(skip, take_top) + bottom[i]
        new_skip = max(skip, take_top, take_bottom)
        
        take_top = new_top
        take_bottom = new_bottom
        skip = new_skip
    
    print(max(skip, take_top, take_bottom))

if __name__ == "__main__":
    main()
