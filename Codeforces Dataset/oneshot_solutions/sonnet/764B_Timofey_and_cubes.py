import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:1 + n]
    
    for i in range(0, n // 2, 2):
        j = n - i - 1
        a[i], a[j] = a[j], a[i]
    
    print(' '.join(map(str, a)))

main()
