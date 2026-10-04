import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n, b, d = data[0], data[1], data[2]
    oranges = data[3:3 + n]
    
    waste = 0
    emptied = 0
    
    for size in oranges:
        if size > b:
            continue
        
        waste += size
        if waste > d:
            emptied += 1
            waste = 0
    
    print(emptied)

if __name__ == "__main__":
    main()
