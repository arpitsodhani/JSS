import sys

def solve_case(n, s):
    i = 0
    operations = 0
    
    while i + 1 < n:
        if s[i] == '(' or s[i + 1] == ')':
            i += 2
            operations += 1
        else:
            j = i + 2
            while j < n and s[j] != ')':
                j += 1
            
            if j == n:
                break
            
            i = j + 1
            operations += 1
    
    return operations, n - i

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    result = []
    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2
        
        operations, remaining = solve_case(n, s)
        result.append(f"{operations} {remaining}")
    
    print('\n'.join(result))

if __name__ == "__main__":
    main()
