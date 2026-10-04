import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    k = data[idx]
    n = data[idx + 1]
    idx += 2
    
    marks = data[idx:idx + k]
    idx += k
    
    remembered = data[idx:idx + n]
    
    prefixes = []
    cur = 0
    for x in marks:
        cur += x
        prefixes.append(cur)
    
    prefix_set = set(prefixes)
    starts = set()
    
    first = remembered[0]
    for p in prefixes:
        start = first - p
        
        ok = True
        for score in remembered:
            if score - start not in prefix_set:
                ok = False
                break
        
        if ok:
            starts.add(start)
    
    print(len(starts))

if __name__ == "__main__":
    main()
