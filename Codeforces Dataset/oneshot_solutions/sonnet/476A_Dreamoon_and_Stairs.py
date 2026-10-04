import sys

def main():
    n, m = map(int, sys.stdin.read().split())
    
    min_moves = (n + 1) // 2
    moves = ((min_moves + m - 1) // m) * m
    
    print(moves if moves <= n else -1)

if __name__ == "__main__":
    main()
