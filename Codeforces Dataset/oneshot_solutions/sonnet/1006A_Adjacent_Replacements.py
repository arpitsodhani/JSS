import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:1 + n]
    
    result = []
    for x in a:
        if x % 2 == 0:
            result.append(x - 1)
        else:
            result.append(x)
    
    print(' '.join(map(str, result)))

main()
