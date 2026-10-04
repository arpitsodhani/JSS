import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    idx = 1
    
    results = []
    for _ in range(t):
        a, b, c, d = data[idx:idx + 4]
        idx += 4
        
        if min(a, c) >= min(b, d):
            results.append("Gellyfish")
        else:
            results.append("Flower")
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
