import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    q = data[1:]
    
    prefix = [0] * n
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + q[i - 1]
    
    min_val = min(prefix)
    start = 1 - min_val
    
    result = [start + x for x in prefix]
    
    if min(result) != 1 or max(result) != n or len(set(result)) != n:
        print(-1)
    else:
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
