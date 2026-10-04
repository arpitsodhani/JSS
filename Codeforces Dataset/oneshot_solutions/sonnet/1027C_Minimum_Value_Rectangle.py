import sys
from collections import Counter

def solve(sticks):
    counter = Counter(sticks)
    
    # Get all possible pairs (sorted)
    pairs = []
    for length in sorted(counter.keys()):
        count = counter[length]
        if count >= 2:
            pairs.append(length)
            if count >= 4:
                pairs.append(length)
    
    # Find the best two consecutive pairs (minimize ratio)
    best_idx = 0
    min_ratio = pairs[1] / pairs[0]
    
    for i in range(1, len(pairs) - 1):
        ratio = pairs[i + 1] / pairs[i]
        if ratio < min_ratio:
            min_ratio = ratio
            best_idx = i
    
    return [pairs[best_idx], pairs[best_idx], pairs[best_idx + 1], pairs[best_idx + 1]]

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        sticks = list(map(int, input_data[idx:idx+n]))
        idx += n
        
        answer = solve(sticks)
        results.append(' '.join(map(str, answer)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
