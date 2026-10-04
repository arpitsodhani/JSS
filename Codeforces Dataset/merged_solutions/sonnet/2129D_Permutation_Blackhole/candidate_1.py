# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from collections import defaultdict

MOD = 998244353

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    idx = 0
    t = data[idx]
    idx += 1
    
    tests = []
    max_n = 0
    for _ in range(t):
        n = data[idx]
        idx += 1
        s = data[idx:idx + n]
        idx += n
        tests.append((n, s))
        max_n = max(max_n, n)
    
    comb = [[0] * (max_n + 1) for _ in range(max_n + 1)]
    for i in range(max_n + 1):
        comb[i][0] = comb[i][i] = 1
        for j in range(1, i):
            comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD
    
    answers = []
    
    for n, s in tests:
        base = n + 1
        
        def good(pos, value):
            fixed = s[pos - 1]
            return fixed == -1 or fixed == value
        
        both = [[defaultdict(int) for _ in range(n + 2)] for __ in range(n + 2)]
        right_open = [[defaultdict(int) for _ in range(n + 2)] for __ in range(n + 2)]
        left_open = [[defaultdict(int) for _ in range(n + 2)] for __ in range(n + 2)]
        
        for i in range(1, n + 1):
            right_open[i][i][0] = 1
            left_open[i][i][0] = 1
        
        for i in range(1, n):
            both[i][i + 1][0] = 1
        
        for length in range(1, n + 1):
            for l in range(1, n - length + 1):
                r = l + length
                cur = right_open[l][r]
                
                for x in range(l + 1, r + 1):
                    ways_split = comb[length - 1][x - l - 1]
                    
                    for key_left, ways_left in both[l][x].items():
                        add_l, add_x_left = divmod(key_left, base)
                        
                        for add_x_right, ways_right in right_open[x][r].items():
                            if good(x, add_x_left + add_x_right):
                                cur[add_l + 1] = (cur[add_l + 1] + ways_left * ways_right * ways_split) % MOD
            
            for l in range(1, n - length + 2):
                r = l + length
                cur = left_open[l][r]
                
                for x in range(l, r):
                    ways_split = comb[length - 1][x - l]
                    
                    for add_x_left, ways_left in left_open[l][x].items():
                        for key_right, ways_right in both[x][r].items():
                            add_x_right, add_r = divmod(key_right, base)
                            
                            if good(x, add_x_left + add_x_right):
                                cur[add_r + 1] = (cur[add_r + 1] + ways_left * ways_right * ways_split) % MOD
            
            gap = length + 1
            for l in range(1, n - gap + 2):
                r = l + gap
                cur = both[l][r]
                
                for x in range(l + 1, r):
                    left_size = x - l - 1
                    right_size = r - x - 1
                    ways_split = comb[left_size + right_size][left_size]
                    
                    to_left = 1 if x - l <= r - x else 0
                    to_right = 1 - to_left
                    
                    for key_left, ways_left in both[l][x].items():
                        add_l, add_x_left = divmod(key_left, base)
                        
                        for key_right, ways_right in both[x][r].items():
                            add_x_right, add_r = divmod(key_right, base)
                            
                            if good(x, add_x_left + add_x_right):
                                new_key = (add_l + to_left) * base + (add_r + to_right)
                                cur[new_key] = (cur[new_key] + ways_left * ways_right * ways_split) % MOD
        
        ans = 0
        for root in range(1, n + 1):
            ways_split = comb[n - 1][root - 1]
            
            for add_left, ways_left in left_open[1][root].items():
                for add_right, ways_right in right_open[root][n].items():
                    if good(root, add_left + add_right):
                        ans = (ans + ways_left * ways_right * ways_split) % MOD
        
        answers.append(str(ans))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
