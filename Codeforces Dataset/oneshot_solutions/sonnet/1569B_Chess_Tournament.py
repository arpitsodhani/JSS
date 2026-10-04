import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        s = input_data[idx]
        idx += 1
        
        # Find Type 2 players
        type2 = [i for i in range(n) if s[i] == '2']
        k = len(type2)
        
        if k == 1 or k == 2:
            print("NO")
            continue
        
        print("YES")
        
        # Build the result matrix
        result = [['X'] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                
                if s[i] == '1' and s[j] == '1':
                    result[i][j] = '='
                elif s[i] == '1' and s[j] == '2':
                    result[i][j] = '+'
                elif s[i] == '2' and s[j] == '1':
                    result[i][j] = '-'
        
        # For Type 2 vs Type 2: create a cycle so each Type 2 player wins at least once
        if k >= 3:
            for idx_in_list in range(k):
                i = type2[idx_in_list]
                j = type2[(idx_in_list + 1) % k]
                result[i][j] = '+'
                result[j][i] = '-'
            
            # For remaining Type 2 vs Type 2 pairs, make them draws
            for i in type2:
                for j in type2:
                    if i != j and result[i][j] == 'X':
                        result[i][j] = '='
        
        # Print the result matrix
        for row in result:
            print(''.join(row))

solve()
