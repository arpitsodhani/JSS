import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = data[1]
    b = data[2]
    
    answer = 0
    
    for i in range(n // 2):
        j = n - i - 1
        
        top = [a[i], a[j]]
        bottom = [b[i], b[j]]
        
        if bottom[0] == bottom[1]:
            if top[0] != top[1]:
                answer += 1
        else:
            need1, need2 = bottom[0], bottom[1]
            keep = 0
            
            if top[0] == need1 and top[1] == need2:
                keep = 2
            elif top[0] == need2 and top[1] == need1:
                keep = 2
            elif top[0] == need1 or top[0] == need2 or top[1] == need1 or top[1] == need2:
                keep = 1
            
            answer += 2 - keep
    
    if n % 2 == 1 and a[n // 2] != b[n // 2]:
        answer += 1
    
    print(answer)

if __name__ == "__main__":
    main()
