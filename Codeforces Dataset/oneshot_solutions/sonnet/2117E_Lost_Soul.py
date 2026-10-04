import sys

def count_matches(n, a, b):
    if n == 0:
        return 0
    
    matches = 0
    for i in range(n):
        # possible_a: a[i], b[i+1], a[i+2], b[i+3], ...
        # possible_b: b[i], a[i+1], b[i+2], a[i+3], ...
        possible_a = set()
        possible_b = set()
        
        for j in range(i, n):
            if (j - i) % 2 == 0:
                possible_a.add(a[j])
                possible_b.add(b[j])
            else:
                possible_a.add(b[j])
                possible_b.add(a[j])
        
        if possible_a & possible_b:
            matches += 1
    
    return matches

def solve(n, a, b):
    max_matches = count_matches(n, a, b)
    
    for remove_idx in range(n):
        a_new = a[:remove_idx] + a[remove_idx+1:]
        b_new = b[:remove_idx] + b[remove_idx+1:]
        matches = count_matches(n-1, a_new, b_new)
        max_matches = max(max_matches, matches)
    
    return max_matches

def main():
    data = sys.stdin.read().strip().split()
    idx = 0
    
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        b = list(map(int, data[idx:idx+n]))
        idx += n
        
        result = solve(n, a, b)
        print(result)

if __name__ == "__main__":
    main()
