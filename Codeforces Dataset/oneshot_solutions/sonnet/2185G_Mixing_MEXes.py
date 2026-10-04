import sys
from collections import Counter

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        arrays = []
        total_count = Counter()
        total_len = 0
        
        for _ in range(n):
            m = data[idx]
            idx += 1
            arr = data[idx:idx + m]
            idx += m
            
            arrays.append(arr)
            total_len += m
            total_count.update(arr)
        
        base_sum = 0
        removal_sum = 0
        add_sum = 0
        
        infos = []
        
        for arr in arrays:
            count = Counter(arr)
            mex = 0
            while count[mex] > 0:
                mex += 1
            
            next_missing = mex + 1
            while count[next_missing] > 0:
                next_missing += 1
            
            base_sum += mex
            infos.append((count, mex, next_missing))
            
            for x in range(mex):
                if count[x] == 1:
                    removal_sum += x - mex
        
        for count, mex, next_missing in infos:
            outside = total_count[mex] - count[mex]
            add_sum += outside * (next_missing - mex)
        
        operations = total_len * (n - 1)
        answer = operations * base_sum + (n - 1) * removal_sum + add_sum
        answers.append(str(answer))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
