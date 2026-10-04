import sys
from bisect import bisect_left

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        lefts = data[idx:idx + n]
        idx += n
        
        rights = data[idx:idx + n]
        idx += n
        
        costs = data[idx:idx + n]
        idx += n
        
        lefts.sort()
        rights.sort()
        
        available = []
        p = 0
        lengths = []
        
        for r in rights:
            while p < n and lefts[p] < r:
                available.append(lefts[p])
                p += 1
            
            l = available.pop()
            lengths.append(r - l)
        
        lengths.sort()
        costs.sort(reverse=True)
        
        total = 0
        for length, cost in zip(lengths, costs):
            total += length * cost
        
        answers.append(str(total))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
