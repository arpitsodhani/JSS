import sys

def main():
    s = sys.stdin.read().strip()
    
    if len(s) % 2 == 1:
        print(-1)
        return
    
    left = s.count('L')
    right = s.count('R')
    up = s.count('U')
    down = s.count('D')
    
    answer = (abs(left - right) + abs(up - down)) // 2
    print(answer)

main()
