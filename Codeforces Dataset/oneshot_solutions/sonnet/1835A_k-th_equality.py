import sys

def solve(A, B, C, k):
    a_min = 10**(A-1)
    a_max = 10**A - 1
    b_min = 10**(B-1)
    b_max = 10**B - 1
    c_min = 10**(C-1)
    c_max = 10**C - 1
    
    count = 0
    for a in range(a_min, a_max + 1):
        b_lo = max(b_min, c_min - a)
        b_hi = min(b_max, c_max - a)
        
        if b_lo <= b_hi:
            cnt = b_hi - b_lo + 1
            if count + cnt >= k:
                b = b_lo + (k - count - 1)
                c = a + b
                return f"{a} + {b} = {c}"
            count += cnt
    
    return "-1"

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        A = int(input_data[idx])
        B = int(input_data[idx + 1])
        C = int(input_data[idx + 2])
        k = int(input_data[idx + 3])
        idx += 4
        
        print(solve(A, B, C, k))

if __name__ == "__main__":
    main()
