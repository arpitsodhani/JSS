import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    v1, v2, v3, vm = data
    
    smallest = max(v3, vm)
    if smallest > min(2 * v3, 2 * vm):
        print(-1)
        return
    
    middle = max(v2, smallest + 1, 2 * vm + 1)
    if middle > 2 * v2:
        print(-1)
        return
    
    largest = max(v1, middle + 1)
    if largest > 2 * v1:
        print(-1)
        return
    
    print(largest)
    print(middle)
    print(smallest)

if __name__ == "__main__":
    main()
