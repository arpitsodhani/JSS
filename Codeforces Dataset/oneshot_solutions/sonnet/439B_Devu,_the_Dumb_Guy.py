import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    x = data[1]
    chapters = data[2:2 + n]
    
    chapters.sort()
    
    total = 0
    power = x
    
    for c in chapters:
        total += c * power
        if power > 1:
            power -= 1
    
    print(total)

if __name__ == "__main__":
    main()
