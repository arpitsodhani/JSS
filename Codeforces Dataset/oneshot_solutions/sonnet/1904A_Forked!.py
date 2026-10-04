import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    for _ in range(t):
        a = data[idx]
        b = data[idx + 1]
        xk = data[idx + 2]
        yk = data[idx + 3]
        xq = data[idx + 4]
        yq = data[idx + 5]
        idx += 6
        
        moves = {
            (a, b), (a, -b), (-a, b), (-a, -b),
            (b, a), (b, -a), (-b, a), (-b, -a)
        }
        
        king_attackers = set()
        queen_attackers = set()
        
        for dx, dy in moves:
            king_attackers.add((xk + dx, yk + dy))
            queen_attackers.add((xq + dx, yq + dy))
        
        print(len(king_attackers & queen_attackers))

if __name__ == "__main__":
    main()
