import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    
    n = data[idx]
    k = data[idx + 1]
    idx += 2
    
    good = 0
    
    for _ in range(k):
        length = data[idx]
        idx += 1
        
        chain = data[idx:idx + length]
        idx += length
        
        if chain[0] == 1:
            good = 1
            for i in range(1, length):
                if chain[i] == chain[i - 1] + 1:
                    good += 1
                else:
                    break
    
    removals = (n - k) - (good - 1)
    insertions = n - good
    
    print(removals + insertions)

if __name__ == "__main__":
    main()
