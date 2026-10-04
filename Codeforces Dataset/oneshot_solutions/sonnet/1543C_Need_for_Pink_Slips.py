import sys
sys.setrecursionlimit(100000)

def solve(c, m, p, v):
    memo = {}
    
    def expected(c, m, p):
        # Round for memoization to handle floating point
        key = (round(c * 1e9), round(m * 1e9), round(p * 1e9))
        if key in memo:
            return memo[key]
        
        # Base case: Pink Slip is certain
        if p > 1 - 1e-9:
            memo[key] = 1.0
            return 1.0
        
        result = 1.0
        
        # Draw Cash
        if c > 1e-9:
            if c <= v + 1e-9:
                new_c = 0
                dist = c
            else:
                new_c = c - v
                dist = v
            
            new_m, new_p = m, p
            
            # Count other valid items and distribute
            others = 0
            if m > 1e-9:
                others += 1
            if p > 1e-9:
                others += 1
            
            if others > 0:
                add = dist / others
                if m > 1e-9:
                    new_m = m + add
                if p > 1e-9:
                    new_p = p + add
            
            result += c * expected(new_c, new_m, new_p)
        
        # Draw Marker
        if m > 1e-9:
            if m <= v + 1e-9:
                new_m = 0
                dist = m
            else:
                new_m = m - v
                dist = v
            
            new_c, new_p = c, p
            
            # Count other valid items and distribute
            others = 0
            if c > 1e-9:
                others += 1
            if p > 1e-9:
                others += 1
            
            if others > 0:
                add = dist / others
                if c > 1e-9:
                    new_c = c + add
                if p > 1e-9:
                    new_p = p + add
            
            result += m * expected(new_c, new_m, new_p)
        
        memo[key] = result
        return result
    
    return expected(c, m, p)

def main():
    input_data = sys.stdin.read().strip().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        c = float(input_data[idx])
        m = float(input_data[idx + 1])
        p = float(input_data[idx + 2])
        v = float(input_data[idx + 3])
        idx += 4
        
        result = solve(c, m, p, v)
        print(f"{result:.12f}")

if __name__ == "__main__":
    main()
