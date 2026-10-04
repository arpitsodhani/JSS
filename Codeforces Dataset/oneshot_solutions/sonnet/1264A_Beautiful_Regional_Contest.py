import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        p = list(map(int, input_data[idx:idx+n]))
        idx += n
        
        # Group consecutive equal scores
        groups = []
        i = 0
        while i < n:
            score = p[i]
            count = 0
            while i < n and p[i] == score:
                count += 1
                i += 1
            groups.append(count)
        
        # Need at least 4 groups (gold, silver, bronze, no medal)
        if len(groups) < 4:
            print("0 0 0")
            continue
        
        max_medals = n // 2
        
        # Gold gets first group(s) - start with just 1 group
        gold = groups[0]
        g_idx = 1
        
        # Silver gets groups until count > gold
        silver = 0
        while g_idx < len(groups) and silver <= gold:
            silver += groups[g_idx]
            g_idx += 1
        
        if silver <= gold or g_idx >= len(groups):
            print("0 0 0")
            continue
        
        # Bronze gets groups while possible
        bronze = 0
        while g_idx < len(groups) - 1:  # Must leave at least 1 group for no medal
            if gold + silver + bronze + groups[g_idx] > max_medals:
                break
            bronze += groups[g_idx]
            g_idx += 1
        
        # Verify all constraints
        if bronze <= gold or g_idx >= len(groups):
            print("0 0 0")
            continue
        
        print(gold, silver, bronze)

if __name__ == "__main__":
    main()
