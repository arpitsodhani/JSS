import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    s = data[2]
    
    best = 0
    i = 0
    
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        
        length = j - i
        best = max(best, length // k)
        i = j
    
    print(best)

if __name__ == "__main__":
    main()
