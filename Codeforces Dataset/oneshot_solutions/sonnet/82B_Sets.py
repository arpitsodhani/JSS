import sys
from collections import defaultdict

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    idx = 0
    n = data[idx]
    idx += 1
    
    m = n * (n - 1) // 2
    occur = {}
    all_numbers = []
    
    for paper in range(m):
        k = data[idx]
        idx += 1
        
        bit = 1 << paper
        for _ in range(k):
            x = data[idx]
            idx += 1
            
            if x not in occur:
                occur[x] = 0
                all_numbers.append(x)
            occur[x] |= bit
    
    if n == 1:
        print(len(all_numbers), *all_numbers)
        return
    
    if n == 2:
        first = all_numbers[0]
        rest = all_numbers[1:]
        print(1, first)
        print(len(rest), *rest)
        return
    
    groups = defaultdict(list)
    for x in all_numbers:
        groups[occur[x]].append(x)
    
    result = list(groups.values())
    
    out = []
    for group in result:
        out.append(str(len(group)) + " " + " ".join(map(str, group)))
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
