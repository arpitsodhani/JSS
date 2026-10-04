# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from collections import defaultdict

MOD = 998244353

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx])
    idx += 1
    
    ops = []
    max_health = 0
    
    for _ in range(n):
        typ = int(data[idx])
        idx += 1
        
        if typ == 3:
            ops.append((3, 0))
        else:
            x = int(data[idx])
            idx += 1
            ops.append((typ, x))
            if typ == 1:
                max_health = max(max_health, x)
    
    cap = max_health + 1
    total_damage = 0
    count = defaultdict(int)
    
    for typ, x in ops:
        if typ == 1:
            count[x] = (count[x] + 1) % MOD
        
        elif typ == 2:
            if x >= max_health:
                count.clear()
            else:
                new_count = defaultdict(int)
                for health, ways in count.items():
                    if health > x:
                        new_count[health - x] = (new_count[health - x] + ways) % MOD
                count = new_count
            
            total_damage = min(cap, total_damage + x)
        
        else:
            new_count = defaultdict(int)
            
            for health, ways in count.items():
                new_count[health] = (new_count[health] + ways) % MOD
                
                if health > total_damage:
                    new_health = health - total_damage
                    new_count[new_health] = (new_count[new_health] + ways) % MOD
            
            count = new_count
            total_damage = min(cap, total_damage * 2)
    
    print(sum(count.values()) % MOD)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
