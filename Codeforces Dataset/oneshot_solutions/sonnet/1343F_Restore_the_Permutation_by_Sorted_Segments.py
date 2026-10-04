import sys

def solve_case(n, segments):
    by_size = {}
    for segment in segments:
        by_size.setdefault(len(segment), []).append(set(segment))
    
    all_values = set(range(1, n + 1))
    
    def check_prefix(prefix):
        m = len(prefix)
        used = set(prefix)
        
        for segment in segments:
            k = len(segment)
            if k > m:
                continue
            
            found = False
            for r in range(k - 1, m):
                if set(prefix[r - k + 1:r + 1]) == segment:
                    found = True
                    break
            
            if not found:
                possible = False
                for r in range(m, n):
                    l = r - k + 1
                    if l < 0:
                        continue
                    
                    left = max(l, 0)
                    right = min(r, m - 1)
                    if left > right:
                        possible = True
                        break
                    
                    need = set(prefix[left:right + 1])
                    if need.issubset(segment):
                        possible = True
                        break
                
                if not possible:
                    return False
        
        return True
    
    def dfs(prefix):
        if len(prefix) == n:
            for segment in segments:
                k = len(segment)
                ok = False
                for r in range(k - 1, n):
                    if set(prefix[r - k + 1:r + 1]) == segment:
                        ok = True
                        break
                if not ok:
                    return None
            return prefix
        
        remaining = all_values - set(prefix)
        for x in remaining:
            nxt = prefix + [x]
            if check_prefix(nxt):
                result = dfs(nxt)
                if result is not None:
                    return result
        
        return None
    
    result = dfs([])
    return result

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        segments = []
        for _ in range(n - 1):
            k = int(data[idx])
            idx += 1
            segment = frozenset(map(int, data[idx:idx + k]))
            idx += k
            segments.append(segment)
        
        answer = solve_case(n, segments)
        answers.append(' '.join(map(str, answer)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
