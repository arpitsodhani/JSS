import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    h = data[1:1 + n]
    
    suffix_min = [0] * n
    suffix_min[-1] = h[-1]
    for i in range(n - 2, -1, -1):
        suffix_min[i] = min(h[i], suffix_min[i + 1])
    
    blocks = 1
    prefix_max = h[0]
    
    for i in range(n - 1):
        prefix_max = max(prefix_max, h[i])
        if prefix_max <= suffix_min[i + 1]:
            blocks += 1
    
    print(blocks)

main()
