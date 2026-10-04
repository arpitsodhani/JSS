# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

sys.setrecursionlimit(1000000)

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    n = int(data[0])
    idx = 1
    
    pattern_weight = {}
    
    for _ in range(n):
        c = int(data[idx])
        word = data[idx + 1].decode()
        idx += 2
        
        letters = [ord(ch) - 97 for ch in word]
        if len(letters) <= 1:
            continue
        
        adj = [set() for _ in range(12)]
        used = set(letters)
        
        ok = True
        for a, b in zip(letters, letters[1:]):
            if a == b:
                ok = False
                break
            adj[a].add(b)
            adj[b].add(a)
        
        if not ok:
            continue
        
        vertices = [v for v in range(12) if adj[v] or v in used]
        edge_count = sum(len(adj[v]) for v in range(12)) // 2
        
        if any(len(adj[v]) > 2 for v in range(12)):
            continue
        if edge_count != len(vertices) - 1:
            continue
        
        if len(vertices) == 2:
            path = vertices[:]
        else:
            ends = [v for v in vertices if len(adj[v]) == 1]
            if len(ends) != 2:
                continue
            
            path = []
            prev = -1
            cur = ends[0]
            while cur != -1:
                path.append(cur)
                nxt = -1
                for to in adj[cur]:
                    if to != prev:
                        nxt = to
                        break
                prev, cur = cur, nxt
        
        rev = path[::-1]
        key = tuple(path) if tuple(path) < tuple(rev) else tuple(rev)
        pattern_weight[key] = pattern_weight.get(key, 0) + c
    
    children = []
    terminal = []
    
    def new_node():
        children.append({})
        terminal.append(0)
        return len(children) - 1
    
    new_node()
    
    for path, weight in pattern_weight.items():
        for seq in (path, path[::-1]):
            node = 0
            for ch in seq:
                if ch not in children[node]:
                    children[node][ch] = new_node()
                node = children[node][ch]
            terminal[node] += weight
    
    full_mask = (1 << 12) - 1
    memo = {}
    choice = {}
    
    def dfs(mask, active):
        if mask == full_mask:
            return 0
        
        state = (mask, active)
        if state in memo:
            return memo[state]
        
        best = -1
        best_ch = 0
        
        for ch in range(12):
            if (mask >> ch) & 1:
                continue
            
            new_active = []
            gain = 0
            
            nxt = children[0].get(ch)
            if nxt is not None:
                new_active.append(nxt)
                gain += terminal[nxt]
            
            for node in active:
                nxt = children[node].get(ch)
                if nxt is not None:
                    new_active.append(nxt)
                    gain += terminal[nxt]
            
            value = gain + dfs(mask | (1 << ch), tuple(new_active))
            if value > best:
                best = value
                best_ch = ch
        
        memo[state] = best
        choice[state] = best_ch
        return best
    
    result = []
    mask = 0
    active = ()
    
    for _ in range(12):
        state = (mask, active)
        dfs(mask, active)
        ch = choice[state]
        result.append(chr(97 + ch))
        
        new_active = []
        nxt = children[0].get(ch)
        if nxt is not None:
            new_active.append(nxt)
        
        for node in active:
            nxt = children[node].get(ch)
            if nxt is not None:
                new_active.append(nxt)
        
        mask |= 1 << ch
        active = tuple(new_active)
    
    print(''.join(result))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
