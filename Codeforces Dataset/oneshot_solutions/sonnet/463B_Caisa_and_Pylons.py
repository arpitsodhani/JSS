import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    heights = data[1:1 + n]
    print(max(heights) if heights else 0)

if __name__ == "__main__":
    main()
