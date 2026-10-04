import sys

def earliest(kicks):
    a = 0
    b = 0
    
    for i, val in enumerate(kicks):
        if i % 2 == 0:
            a += val
        else:
            b += val
        
        used_a = (i + 2) // 2
        used_b = (i + 1) // 2
        left_a = 5 - used_a
        left_b = 5 - used_b
        
        if a > b + left_b or b > a + left_a:
            return i + 1
    
    return 10

def solve_string(s):
    unknown = [i for i, c in enumerate(s) if c == '?']
    best = 10
    
    for mask in range(1 << len(unknown)):
        kicks = [0] * 10
        
        for i, c in enumerate(s):
            if c == '1':
                kicks[i] = 1
        
        for j, pos in enumerate(unknown):
            if (mask >> j) & 1:
                kicks[pos] = 1
        
        best = min(best, earliest(kicks))
    
    return best

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    
    ans = []
    for i in range(1, t + 1):
        ans.append(str(solve_string(data[i])))
    
    print('\n'.join(ans))

if __name__ == "__main__":
    main()
