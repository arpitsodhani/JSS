import sys
from collections import Counter

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        nums = list(map(int, data[idx:idx + n]))
        idx += n
        
        count = Counter(nums)
        
        mex_a = 0
        while count[mex_a] > 0:
            count[mex_a] -= 1
            mex_a += 1
        
        mex_b = 0
        while count[mex_b] > 0:
            count[mex_b] -= 1
            mex_b += 1
        
        answers.append(str(mex_a + mex_b))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
