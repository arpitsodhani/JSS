import sys

def solve_case(n, songs):
    can_follow = [[False] * n for _ in range(n)]
    
    for i in range(n):
        gi, wi = songs[i]
        for j in range(n):
            if i != j:
                gj, wj = songs[j]
                can_follow[i][j] = (gi == gj or wi == wj)
    
    size = 1 << n
    dp = [[False] * n for _ in range(size)]
    
    for i in range(n):
        dp[1 << i][i] = True
    
    best = 1
    
    for mask in range(size):
        used = mask.bit_count()
        for last in range(n):
            if not dp[mask][last]:
                continue
            
            best = max(best, used)
            
            for nxt in range(n):
                if (mask >> nxt) & 1:
                    continue
                if can_follow[last][nxt]:
                    dp[mask | (1 << nxt)][nxt] = True
    
    return n - best

def main():
    data = sys.stdin.read().split()
    idx = 0
    
    t = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        songs = []
        for _ in range(n):
            genre = data[idx]
            writer = data[idx + 1]
            idx += 2
            songs.append((genre, writer))
        
        answers.append(str(solve_case(n, songs)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
