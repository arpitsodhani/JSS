# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def xor_upto(n):
    if n < 0:
        return 0
    rem = n % 4
    if rem == 0:
        return n
    if rem == 1:
        return 1
    if rem == 2:
        return n + 1
    return 0

def bad_xor_upto(n, i, k):
    mod = 1 << i
    if n < k:
        return 0
    
    q = (n - k) // mod
    count = q + 1
    
    result = xor_upto(q) << i
    if count % 2 == 1:
        result ^= k
    
    return result

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(t):
        l = int(data[idx])
        r = int(data[idx + 1])
        i = int(data[idx + 2])
        k = int(data[idx + 3])
        idx += 4
        
        total = xor_upto(r) ^ xor_upto(l - 1)
        bad = bad_xor_upto(r, i, k) ^ bad_xor_upto(l - 1, i, k)
        answers.append(str(total ^ bad))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
