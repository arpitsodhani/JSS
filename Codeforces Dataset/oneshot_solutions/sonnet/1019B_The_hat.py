import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    values = data[1:]
    half = n // 2
    
    for i in range(half):
        if values[i] == values[i + half]:
            print(i + 1)
            return
    
    print(-1)

if __name__ == "__main__":
    main()
