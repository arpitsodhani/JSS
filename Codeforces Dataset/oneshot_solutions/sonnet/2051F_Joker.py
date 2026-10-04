import sys

def solve():
    data = sys.stdin.buffer.read().decode().split()
    idx = 0
    
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        q = int(data[idx + 2])
        idx += 3
        
        positions = {m}
        results = []
        
        for _ in range(q):
            a = int(data[idx])
            idx += 1
            
            new_positions = set()
            for p in positions:
                if a < p:
                    new_positions.add(p)      # move to beginning
                    new_positions.add(p - 1)  # move to end
                elif a == p:
                    new_positions.add(1)      # move to beginning
                    new_positions.add(n)      # move to end
                else:  # a > p
                    new_positions.add(p + 1)  # move to beginning
                    new_positions.add(p)      # move to end
            
            positions = new_positions
            results.append(str(len(positions)))
        
        print(' '.join(results))

solve()
