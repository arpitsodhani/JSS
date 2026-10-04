import sys
from collections import Counter

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    colors = data[2:2 + n]
    
    count = Counter(colors)
    ordered = []
    for color, freq in sorted(count.items(), key=lambda x: x[1], reverse=True):
        ordered.extend([color] * freq)
    
    max_freq = max(count.values())
    shift = max_freq
    
    right = ordered[shift:] + ordered[:shift]
    
    good = 0
    pairs = []
    for i in range(n):
        if ordered[i] != right[i]:
            good += 1
        pairs.append((ordered[i], right[i]))
    
    print(good)
    for a, b in pairs:
        print(a, b)

if __name__ == "__main__":
    main()
