import sys

def main():
    s = list(sys.stdin.readline().strip())
    n = len(s)
    last = int(s[-1])
    
    best = -1
    
    for i in range(n - 1):
        digit = int(s[i])
        if digit % 2 == 0:
            best = i
            if digit < last:
                break
    
    if best == -1:
        print(-1)
        return
    
    s[best], s[-1] = s[-1], s[best]
    print(''.join(s))

main()
