import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    idx = 0
    n = int(input_data[idx])
    idx += 1
    
    predicted = []
    for _ in range(n):
        predicted.append(int(input_data[idx]))
        idx += 1
    
    adj = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input_data[idx]))
            idx += 1
        adj.append(row)
    
    # Try all possible subsets
    for mask in range(1 << n):
        valid = True
        for i in range(n):
            received = 0
            for j in range(n):
                if mask & (1 << j):
                    received += adj[j][i]
            if received == predicted[i]:
                valid = False
                break
        
        if valid:
            S = [i+1 for i in range(n) if mask & (1 << i)]
            print(len(S))
            if len(S) > 0:
                print(' '.join(map(str, S)))
            return

solve()
