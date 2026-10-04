import sys

MOD = 10 ** 9 + 7

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    inv2 = (MOD + 1) // 2
    
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        
        values = data[idx:idx + n]
        idx += n
        
        special_sum = sum(values[:k]) % MOD
        normal_sum = sum(values[k:]) % MOD
        normal_count = n - k
        
        if normal_count == 0:
            alice = special_sum
        else:
            m = normal_count
            
            if m % 2 == 0:
                p_special = (m + 2) * pow(2 * (m + 1), MOD - 2, MOD)
                p_special %= MOD
                p_normal = inv2
            else:
                p_special = inv2
                p_normal = (m + 1) * pow(2 * m, MOD - 2, MOD)
                p_normal %= MOD
            
            alice = (special_sum * p_special + normal_sum * p_normal) % MOD
        
        total = (special_sum + normal_sum) % MOD
        bob = (total - alice) % MOD
        out.append(f"{alice} {bob}")
    
    print("\n".join(out))

if __name__ == "__main__":
    main()
