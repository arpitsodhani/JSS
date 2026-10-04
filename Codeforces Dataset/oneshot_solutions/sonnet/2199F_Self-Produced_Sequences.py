import sys

def is_self_produced(subseq):
    n = len(subseq)
    if n == 0:
        return True
    
    for i in range(n):
        left_sum = sum(subseq[:i])
        right_sum = sum(subseq[i+1:])
        if subseq[i] != left_sum and subseq[i] != right_sum:
            return False
    return True

def solve(a):
    n = len(a)
    MOD = 998244353
    count = 0
    
    for mask in range(1 << n):
        subseq = [a[i] for i in range(n) if mask & (1 << i)]
        if is_self_produced(subseq):
            count += 1
    
    return count % MOD

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        if n == 0:
            print(1)
        else:
            a = [int(input_data[idx + i]) for i in range(n)]
            idx += n
            print(solve(a))

if __name__ == "__main__":
    main()
