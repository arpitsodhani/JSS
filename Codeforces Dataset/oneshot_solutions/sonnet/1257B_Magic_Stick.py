import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    
    ans = []
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        
        if x >= 4:
            ans.append("YES")
        elif x == 1:
            ans.append("YES" if y == 1 else "NO")
        else:
            ans.append("YES" if y <= 3 else "NO")
    
    print('\n'.join(ans))

main()
