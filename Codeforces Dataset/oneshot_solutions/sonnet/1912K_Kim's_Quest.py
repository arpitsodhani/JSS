import sys

MOD = 998244353

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    a = data[1:1 + n]
    
    one = [0, 0]
    two = [[0, 0], [0, 0]]
    ans = 0
    
    for value in a:
        x = value & 1
        
        old_one = one[:]
        old_two = [row[:] for row in two]
        
        for p in range(2):
            for q in range(2):
                if (p + q + x) % 2 == 0:
                    cnt = old_two[p][q]
                    ans = (ans + cnt) % MOD
                    two[q][x] = (two[q][x] + cnt) % MOD
        
        for p in range(2):
            two[p][x] = (two[p][x] + old_one[p]) % MOD
        
        one[x] = (one[x] + 1) % MOD
    
    print(ans % MOD)

if __name__ == "__main__":
    main()
