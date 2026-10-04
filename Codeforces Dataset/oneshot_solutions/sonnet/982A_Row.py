import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]
    
    ok = True
    
    if '11' in s:
        ok = False
    
    for i in range(n):
        if s[i] == '0':
            left_free = (i == 0 or s[i - 1] == '0')
            right_free = (i == n - 1 or s[i + 1] == '0')
            if left_free and right_free:
                ok = False
                break
    
    print("Yes" if ok else "No")

main()
