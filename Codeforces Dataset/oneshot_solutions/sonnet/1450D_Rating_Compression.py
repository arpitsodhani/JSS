import sys
from collections import Counter

def solve_case(n, a):
    freq = [0] * (n + 1)
    pos = [-1] * (n + 1)
    
    for i, value in enumerate(a):
        if 1 <= value <= n:
            freq[value] += 1
            pos[value] = i
    
    is_perm = True
    for value in range(1, n + 1):
        if freq[value] != 1:
            is_perm = False
            break
    
    possible = [False] * (n + 1)
    possible[n] = is_perm
    
    if n == 1:
        return "1" if is_perm else "0"
    
    possible[1] = freq[1] > 0
    
    prefix_ok = [False] * n
    prefix_ok[0] = True
    
    left = 0
    right = n - 1
    
    for value in range(1, n):
        if prefix_ok[value - 1] and freq[value] == 1 and (pos[value] == left or pos[value] == right):
            prefix_ok[value] = True
            if pos[value] == left:
                left += 1
            else:
                right -= 1
        else:
            prefix_ok[value] = False
    
    for length in range(2, n):
        possible[length] = prefix_ok[length - 1] and freq[length] > 0
    
    result = []
    for k in range(1, n + 1):
        length = n - k + 1
        result.append('1' if possible[length] else '0')
    
    return ''.join(result)

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        answers.append(solve_case(n, a))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
