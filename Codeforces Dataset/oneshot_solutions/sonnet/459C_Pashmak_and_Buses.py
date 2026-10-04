import sys

def main():
    n, k, d = map(int, sys.stdin.read().split())
    
    capacity = 1
    for _ in range(d):
        capacity *= k
        if capacity >= n:
            break
    
    if capacity < n:
        print(-1)
        return
    
    result = []
    for day in range(d):
        row = []
        block = k ** day
        for student in range(n):
            row.append((student // block) % k + 1)
        result.append(' '.join(map(str, row)))
    
    print('\n'.join(result))

if __name__ == "__main__":
    main()
