import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        s = [int(input_data[idx + i]) for i in range(n)]
        idx += n
        
        # Group consecutive students with same shoe size
        groups = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            groups.append((i, j))  # [i, j) range of indices
            i = j
        
        # Check if any group has size 1 (impossible case)
        valid = True
        for start, end in groups:
            if end - start == 1:
                valid = False
                break
        
        if not valid:
            results.append("-1")
        else:
            # Build permutation by rotating each group
            p = [0] * n
            for start, end in groups:
                # Rotate: each student i gets shoes from i+1, last gets from first
                for i in range(start, end):
                    if i == end - 1:
                        p[i] = start + 1  # 1-indexed
                    else:
                        p[i] = i + 2  # 1-indexed
            results.append(' '.join(map(str, p)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
