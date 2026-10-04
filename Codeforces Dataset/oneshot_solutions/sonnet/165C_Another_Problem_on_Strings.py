import sys

def main():
    data = sys.stdin.read().split()
    k = int(data[0])
    s = data[1]
    
    n = len(s)
    
    if k == 0:
        result = 0
        run = 0
        for c in s:
            if c == '0':
                run += 1
            else:
                result += run * (run + 1) // 2
                run = 0
        result += run * (run + 1) // 2
        print(result)
        return
    
    ones = []
    for i, c in enumerate(s):
        if c == '1':
            ones.append(i)
    
    if len(ones) < k:
        print(0)
        return
    
    result = 0
    m = len(ones)
    
    for i in range(m - k + 1):
        left_prev = -1 if i == 0 else ones[i - 1]
        right_next = n if i + k == m else ones[i + k]
        
        left_choices = ones[i] - left_prev
        right_choices = right_next - ones[i + k - 1]
        result += left_choices * right_choices
    
    print(result)

if __name__ == "__main__":
    main()
