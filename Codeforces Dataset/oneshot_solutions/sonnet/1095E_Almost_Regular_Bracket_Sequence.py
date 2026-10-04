import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    s = data[1]
    
    if n % 2 == 1:
        print(0)
        return
    
    prefix = [0] * (n + 1)
    for i, c in enumerate(s, 1):
        prefix[i] = prefix[i - 1] + (1 if c == '(' else -1)
    
    total = prefix[n]
    if total not in (2, -2):
        print(0)
        return
    
    min_left = [0] * (n + 1)
    for i in range(1, n + 1):
        min_left[i] = min(min_left[i - 1], prefix[i])
    
    min_right = [0] * (n + 2)
    min_right[n] = prefix[n]
    for i in range(n - 1, 0, -1):
        min_right[i] = min(prefix[i], min_right[i + 1])
    
    answer = 0
    
    if total == 2:
        for i, c in enumerate(s, 1):
            if c == '(' and min_left[i - 1] >= 0 and min_right[i] >= 2:
                answer += 1
    else:
        for i, c in enumerate(s, 1):
            if c == ')' and min_left[i - 1] >= 0 and min_right[i] >= -2:
                answer += 1
    
    print(answer)

if __name__ == "__main__":
    main()
