# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.80]
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    parts = data[1:]
    
    by_len = [[] for _ in range(n)]
    for i, s in enumerate(parts):
        by_len[len(s)].append((i, s))
    
    longest = by_len[n - 1]
    a = longest[0][1]
    b = longest[1][1]
    
    candidates = [a + b[-1], b + a[-1]]
    
    def try_string(original):
        ans = [''] * (2 * n - 2)
        
        for length in range(1, n):
            (i1, s1), (i2, s2) = by_len[length]
            pref = original[:length]
            suff = original[-length:]
            
            if s1 == pref and s2 == suff:
                ans[i1] = 'P'
                ans[i2] = 'S'
            elif s1 == suff and s2 == pref:
                ans[i1] = 'S'
                ans[i2] = 'P'
            else:
                return None
        
        return ''.join(ans)
    
    for candidate in candidates:
        result = try_string(candidate)
        if result is not None:
            print(result)
            return

if __name__ == "__main__":
    main()


# Clause finish_program [Confidence: 0.40]
main()


