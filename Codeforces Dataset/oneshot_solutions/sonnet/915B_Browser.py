import sys

def main():
    n, pos, l, r = map(int, sys.stdin.read().split())
    
    if l == 1 and r == n:
        print(0)
    elif l == 1:
        print(abs(pos - r) + 1)
    elif r == n:
        print(abs(pos - l) + 1)
    else:
        print(min(abs(pos - l), abs(pos - r)) + (r - l) + 2)

main()
