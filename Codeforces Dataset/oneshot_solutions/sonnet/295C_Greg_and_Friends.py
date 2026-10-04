import sys
from collections import deque

MOD = 1000000007

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n, k = data[0], data[1]
    weights = data[2:2 + n]
    
    total_50 = weights.count(50)
    total_100 = weights.count(100)
    
    comb = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        comb[i][0] = comb[i][i] = 1
        for j in range(1, i):
            comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD
    
    moves = []
    for c50 in range(total_50 + 1):
        for c100 in range(total_100 + 1):
            if c50 == 0 and c100 == 0:
                continue
            if 50 * c50 + 100 * c100 <= k:
                moves.append((c50, c100))
    
    dist = [[[-1] * 2 for _ in range(total_100 + 1)] for _ in range(total_50 + 1)]
    ways = [[[0] * 2 for _ in range(total_100 + 1)] for _ in range(total_50 + 1)]
    
    dist[total_50][total_100][0] = 0
    ways[total_50][total_100][0] = 1
    
    q = deque()
    q.append((total_50, total_100, 0))
    
    while q:
        left_50, left_100, side = q.popleft()
        
        for take_50, take_100 in moves:
            if side == 0:
                if take_50 > left_50 or take_100 > left_100:
                    continue
                
                next_50 = left_50 - take_50
                next_100 = left_100 - take_100
                mult = comb[left_50][take_50] * comb[left_100][take_100]
            else:
                right_50 = total_50 - left_50
                right_100 = total_100 - left_100
                
                if take_50 > right_50 or take_100 > right_100:
                    continue
                
                next_50 = left_50 + take_50
                next_100 = left_100 + take_100
                mult = comb[right_50][take_50] * comb[right_100][take_100]
            
            next_side = 1 - side
            next_dist = dist[left_50][left_100][side] + 1
            
            if dist[next_50][next_100][next_side] == -1:
                dist[next_50][next_100][next_side] = next_dist
                q.append((next_50, next_100, next_side))
            
            if dist[next_50][next_100][next_side] == next_dist:
                add = ways[left_50][left_100][side] * mult
                ways[next_50][next_100][next_side] = (ways[next_50][next_100][next_side] + add) % MOD
    
    print(dist[0][0][1])
    print(ways[0][0][1] if dist[0][0][1] != -1 else 0)

if __name__ == "__main__":
    main()
