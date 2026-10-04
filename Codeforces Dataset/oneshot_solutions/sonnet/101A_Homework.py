import sys
from collections import Counter

def main():
    data = sys.stdin.read().split()
    s = data[0]
    k = int(data[1])
    
    freq = Counter(s)
    letters = sorted(freq.keys(), key=lambda c: freq[c])
    
    removed = set()
    for c in letters:
        if freq[c] <= k:
            k -= freq[c]
            removed.add(c)
        else:
            break
    
    result = []
    for c in s:
        if c not in removed:
            result.append(c)
    
    print(len(set(result)))
    if result:
        print(''.join(result))

if __name__ == "__main__":
    main()
