import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    ratings = data[1:]
    
    ratings.sort()
    
    if ratings[n - 1] < ratings[n]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
