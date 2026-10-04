import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    result = []
    
    for i in range(1, t + 1):
        k = int(data[i])
        
        left, right = 1, 2 * k + 10
        answer = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid - int(mid ** 0.5) >= k:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        result.append(str(answer))
    
    print('\n'.join(result))

if __name__ == "__main__":
    main()
