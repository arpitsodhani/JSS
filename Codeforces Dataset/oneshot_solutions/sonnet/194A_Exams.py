import sys

def main():
    n, k = map(int, sys.stdin.read().split())
    print(max(0, 3 * n - k))

main()
