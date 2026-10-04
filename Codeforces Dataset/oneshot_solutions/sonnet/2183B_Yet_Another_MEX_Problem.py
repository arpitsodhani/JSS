import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        
        seen = set()
        for _ in range(n):
            seen.add(data[idx])
            idx += 1
        
        mex = 0
        while mex in seen:
            mex += 1
        
        answers.append(str(min(mex, k - 1)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
