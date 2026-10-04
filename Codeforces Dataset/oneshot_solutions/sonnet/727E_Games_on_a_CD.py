import sys

def main():
    lines = sys.stdin.read().strip().split('\n')
    idx = 0
    
    n, k = map(int, lines[idx].split())
    idx += 1
    
    cd = lines[idx]
    idx += 1
    
    g = int(lines[idx])
    idx += 1
    
    game_set = set()
    game_to_idx = {}
    for i in range(g):
        game = lines[idx]
        idx += 1
        if game not in game_to_idx:
            game_to_idx[game] = i + 1  # 1-indexed
        game_set.add(game)
    
    # Extend CD to handle wrap-around
    cd_len = n * k
    cd_extended = cd + cd
    
    # Try all starting positions
    for start in range(cd_len):
        used = set()
        result = []
        valid = True
        
        for i in range(n):
            pos = start + i * k
            substring = cd_extended[pos:pos+k]
            
            if substring not in game_set:
                valid = False
                break
            
            game_idx = game_to_idx[substring]
            if game_idx in used:
                valid = False
                break
            
            used.add(game_idx)
            result.append(game_idx)
        
        if valid:
            print("YES")
            print(' '.join(map(str, result)))
            return
    
    print("NO")

if __name__ == "__main__":
    main()
