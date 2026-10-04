import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    p = int(data[1])
    s = list(data[2])
    
    for i in range(n - p):
        a = s[i]
        b = s[i + p]
        
        if a != '.' and b != '.':
            if a != b:
                for j in range(n):
                    if s[j] == '.':
                        s[j] = '0'
                print(''.join(s))
                return
        elif a == '.' and b == '.':
            s[i] = '0'
            s[i + p] = '1'
            for j in range(n):
                if s[j] == '.':
                    s[j] = '0'
            print(''.join(s))
            return
        elif a == '.':
            s[i] = '1' if b == '0' else '0'
            for j in range(n):
                if s[j] == '.':
                    s[j] = '0'
            print(''.join(s))
            return
        else:
            s[i + p] = '1' if a == '0' else '0'
            for j in range(n):
                if s[j] == '.':
                    s[j] = '0'
            print(''.join(s))
            return
    
    print("No")

main()
