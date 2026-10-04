import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    q = int(input_data[idx])
    idx += 1
    
    for _ in range(q):
        n = int(input_data[idx])
        idx += 1
        s = input_data[idx]
        idx += 1
        
        if n == 2:
            if s[0] < s[1]:
                print("YES")
                print(2)
                print(s[0], s[1])
            else:
                print("NO")
        else:
            # n >= 3: divide as [first digit, rest]
            print("YES")
            print(2)
            print(s[0], s[1:])

solve()
