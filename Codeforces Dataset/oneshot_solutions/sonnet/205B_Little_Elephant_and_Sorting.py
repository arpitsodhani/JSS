import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:1 + n]
    
    moves = 0
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            moves += a[i] - a[i + 1]
    
    print(moves)

main()
