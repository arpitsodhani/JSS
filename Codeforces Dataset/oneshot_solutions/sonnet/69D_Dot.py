import sys
sys.setrecursionlimit(1000000)

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    
    x, y, n, d = data[:4]
    moves = []
    idx = 4
    for _ in range(n):
        moves.append((data[idx], data[idx + 1]))
        idx += 2
    
    limit2 = d * d
    memo = {}
    visiting = set()
    
    def inside(a, b):
        return a * a + b * b <= limit2
    
    def win(a, b, used_anton, used_dasha, turn):
        key = (a, b, used_anton, used_dasha, turn)
        if key in memo:
            return memo[key]
        if key in visiting:
            return False
        
        visiting.add(key)
        
        # Shift moves
        for dx, dy in moves:
            na, nb = a + dx, b + dy
            if not inside(na, nb):
                continue
            if not win(na, nb, used_anton, used_dasha, turn ^ 1):
                visiting.remove(key)
                memo[key] = True
                return True
        
        # Reflection move
        if turn == 0 and not used_anton:
            if inside(b, a) and not win(b, a, 1, used_dasha, 1):
                visiting.remove(key)
                memo[key] = True
                return True
        
        if turn == 1 and not used_dasha:
            if inside(b, a) and not win(b, a, used_anton, 1, 0):
                visiting.remove(key)
                memo[key] = True
                return True
        
        visiting.remove(key)
        memo[key] = False
        return False
    
    print("Anton" if win(x, y, 0, 0, 0) else "Dasha")

if __name__ == "__main__":
    main()
