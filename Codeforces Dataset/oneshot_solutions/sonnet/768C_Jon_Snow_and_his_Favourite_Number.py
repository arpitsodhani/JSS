import sys

def transform(counts, x):
    new_counts = counts[:]
    parity = 0
    
    for value in range(1024):
        c = counts[value]
        if c == 0:
            continue
        
        changed = (c + 1) // 2 if parity == 0 else c // 2
        if changed:
            to_value = value ^ x
            new_counts[value] -= changed
            new_counts[to_value] += changed
        
        parity ^= c & 1
    
    return new_counts

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k, x = data[0], data[1], data[2]
    arr = data[3:3 + n]
    
    counts = [0] * 1024
    for a in arr:
        counts[a] += 1
    
    seen = {}
    step = 0
    
    while step < k:
        state = tuple(counts)
        if state in seen:
            cycle_len = step - seen[state]
            remaining = (k - step) % cycle_len
            for _ in range(remaining):
                counts = transform(counts, x)
            break
        
        seen[state] = step
        counts = transform(counts, x)
        step += 1
    
    minimum = next(i for i in range(1024) if counts[i])
    maximum = next(i for i in range(1023, -1, -1) if counts[i])
    
    print(maximum, minimum)

if __name__ == "__main__":
    main()
