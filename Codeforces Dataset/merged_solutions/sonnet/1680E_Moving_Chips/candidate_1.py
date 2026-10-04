# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def solve_case(n, top, bottom):
    masks = []
    for i in range(n):
        mask = 0
        if top[i] == '*':
            mask |= 1
        if bottom[i] == '*':
            mask |= 2
        masks.append(mask)
    
    left = 0
    while masks[left] == 0:
        left += 1
    
    right = n - 1
    while masks[right] == 0:
        right -= 1
    
    first = masks[left]
    dp = [
        1 if first & 2 else 0,
        1 if first & 1 else 0
    ]
    
    for i in range(left + 1, right + 1):
        mask = masks[i]
        new_dp = [0, 0]
        
        for row in range(2):
            other_chip = mask & (2 if row == 0 else 1)
            need_vertical = 1 if other_chip else 0
            
            stay = dp[row] + 1 + need_vertical
            switch = dp[1 - row] + 2
            
            if need_vertical:
                switch -= 1
            
            new_dp[row] = min(stay, switch)
        
        dp = new_dp
    
    return min(dp)

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        top = data[idx]
        bottom = data[idx + 1]
        idx += 2
        
        answers.append(str(solve_case(n, top, bottom)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
