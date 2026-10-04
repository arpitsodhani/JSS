import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    
    pos_odd = 1
    pos_even = 2
    
    for _ in range(m):
        move_type = int(data[idx])
        idx += 1
        
        if move_type == 1:
            x = int(data[idx])
            idx += 1
            pos_odd = (pos_odd + x - 1) % n + 1
            pos_even = (pos_even + x - 1) % n + 1
        else:
            if pos_odd % 2 == 1:
                pos_odd += 1
            else:
                pos_odd -= 1
            
            if pos_even % 2 == 1:
                pos_even += 1
            else:
                pos_even -= 1
    
    result = [0] * n
    for i in range(n // 2):
        odd_boy = 2 * i + 1
        odd_pos = (pos_odd + 2 * i - 1) % n
        result[odd_pos] = odd_boy
        
        even_boy = 2 * i + 2
        even_pos = (pos_even + 2 * i - 1) % n
        result[even_pos] = even_boy
    
    print(' '.join(map(str, result)))

solve()
