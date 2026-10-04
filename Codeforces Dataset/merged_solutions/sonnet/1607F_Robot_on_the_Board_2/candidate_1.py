# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out = []
    moves = {
        ord('L'): (0, -1),
        ord('R'): (0, 1),
        ord('U'): (-1, 0),
        ord('D'): (1, 0),
    }
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        
        grid = data[idx:idx + n]
        idx += n
        
        total = n * m
        nxt = [-1] * total
        
        for i in range(n):
            row = grid[i]
            for j in range(m):
                di, dj = moves[row[j]]
                ni = i + di
                nj = j + dj
                v = i * m + j
                if 0 <= ni < n and 0 <= nj < m:
                    nxt[v] = ni * m + nj
        
        state = [0] * total
        dist = [0] * total
        pos = [-1] * total
        
        for start in range(total):
            if state[start]:
                continue
            
            path = []
            v = start
            
            while v != -1 and state[v] == 0:
                state[v] = 1
                pos[v] = len(path)
                path.append(v)
                v = nxt[v]
            
            if v == -1:
                length = 0
                for u in reversed(path):
                    length += 1
                    dist[u] = length
            elif state[v] == 2:
                length = dist[v]
                for u in reversed(path):
                    length += 1
                    dist[u] = length
            else:
                cycle_start = pos[v]
                cycle_len = len(path) - cycle_start
                
                for i in range(cycle_start, len(path)):
                    dist[path[i]] = cycle_len
                
                length = cycle_len
                for i in range(cycle_start - 1, -1, -1):
                    length += 1
                    dist[path[i]] = length
            
            for u in path:
                state[u] = 2
                pos[u] = -1
        
        best = 0
        best_cell = 0
        for i in range(total):
            if dist[i] > best:
                best = dist[i]
                best_cell = i
        
        out.append(f"{best_cell // m + 1} {best_cell % m + 1} {best}")
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
