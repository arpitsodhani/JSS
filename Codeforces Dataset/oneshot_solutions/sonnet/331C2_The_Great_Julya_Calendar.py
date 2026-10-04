import sys

def main():
    s = sys.stdin.readline().strip()
    n = int(s)
    
    answer = 0
    
    while n > 0:
        s = str(n)
        best = ord(max(s)) - 48
        
        if best == 9:
            pos = len(s) - 1 - s.rfind('9')
            place = 10 ** pos
            low = n % place
            steps = low // 9 + 1
        else:
            steps = 1
        
        n -= steps * best
        answer += steps
    
    print(answer)

if __name__ == "__main__":
    main()
