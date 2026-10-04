from math import comb

def prob(N, k):
    total = comb(N, 3)
    result = 0.0
    
    # s = 1: prob_s = 1/2
    if k >= 1 and N - k >= 2:
        result += comb(k, 1) * comb(N - k, 2) / total * 0.5
    
    # s = 2: prob_s = 1
    if k >= 2 and N - k >= 1:
        result += comb(k, 2) * comb(N - k, 1) / total
    
    # s = 3: prob_s = 1
    if k >= 3:
        result += comb(k, 3) / total
    
    return result

N, P = input().split()
N = int(N)
P = float(P)

for k in range(N + 1):
    if prob(N, k) >= P - 1e-9:
        print(k)
        break
