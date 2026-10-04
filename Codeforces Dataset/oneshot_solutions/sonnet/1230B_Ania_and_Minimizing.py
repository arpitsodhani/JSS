import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    n = int(input_data[0])
    k = int(input_data[1])
    s = list(input_data[2])
    
    if n == 1:
        if k >= 1:
            print("0")
        else:
            print(s[0])
        return
    
    # For n > 1
    changes = k
    
    # Handle first digit
    if s[0] != '1' and changes > 0:
        s[0] = '1'
        changes -= 1
    
    # Handle remaining digits
    for i in range(1, n):
        if changes == 0:
            break
        if s[i] != '0':
            s[i] = '0'
            changes -= 1
    
    print(''.join(s))

solve()
