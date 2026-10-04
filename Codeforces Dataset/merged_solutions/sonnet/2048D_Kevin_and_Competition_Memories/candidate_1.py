# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from bisect import bisect_left

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    output = []
    
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        
        ratings = data[idx:idx + n]
        idx += n
        
        problems = data[idx:idx + m]
        idx += m
        
        kevin = ratings[0]
        ratings.sort()
        
        penalties = []
        for difficulty in problems:
            if difficulty > kevin:
                beaten_by = n - bisect_left(ratings, difficulty)
                if beaten_by > 0:
                    penalties.append(beaten_by)
        
        penalties.sort(reverse=True)
        h = len(penalties)
        
        answers = []
        for k in range(1, m + 1):
            contests = m // k
            unused = m % k
            
            total = contests
            start = min(unused, h)
            for i in range(start, h, k):
                total += penalties[i]
            
            answers.append(str(total))
        
        output.append(' '.join(answers))
    
    sys.stdout.write('\n'.join(output))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
