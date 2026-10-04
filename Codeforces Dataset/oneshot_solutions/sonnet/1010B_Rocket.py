import sys

def main():
    data = sys.stdin.read().split()
    if len(data) < 2:
        return
    
    m = int(data[0])
    n = int(data[1])
    replies = list(map(int, data[2:]))
    pos = 0
    
    output = []
    pattern = []
    
    for _ in range(n):
        output.append("1")
        if pos >= len(replies):
            break
        ans = replies[pos]
        pos += 1
        
        if ans == 0:
            print("\n".join(output))
            return
        
        pattern.append(ans)
    
    left, right = 1, m
    step = 0
    
    while left <= right and pos < len(replies):
        mid = (left + right) // 2
        output.append(str(mid))
        
        ans = replies[pos]
        pos += 1
        
        if ans == 0:
            break
        
        ans *= pattern[step % n]
        step += 1
        
        if ans == 1:
            left = mid + 1
        else:
            right = mid - 1
    
    print("\n".join(output))

if __name__ == "__main__":
    main()
