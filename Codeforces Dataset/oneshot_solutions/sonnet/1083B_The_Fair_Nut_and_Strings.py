import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    s = data[2]
    t = data[3]
    
    answer = 0
    possible = 1
    
    for i in range(n):
        if s[i] != t[i]:
            possible *= 2
        
        answer += min(k, possible)
        
        if s[i] == 'b':
            possible -= 1
        if t[i] == 'a':
            possible -= 1
        
        possible = min(possible, k)
    
    print(answer)

if __name__ == "__main__":
    main()
