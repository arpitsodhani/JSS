import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    
    n = data[0]
    x = data[1]
    print(x)

if __name__ == "__main__":
    main()
