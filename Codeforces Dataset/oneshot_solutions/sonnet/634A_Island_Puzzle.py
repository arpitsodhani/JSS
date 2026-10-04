import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:1 + n]
    b = data[1 + n:1 + 2 * n]
    
    first = [x for x in a if x != 0]
    second = [x for x in b if x != 0]
    
    doubled = first + first
    m = n - 1
    
    possible = False
    for i in range(m):
        if doubled[i:i + m] == second:
            possible = True
            break
    
    print("YES" if possible else "NO")

main()
