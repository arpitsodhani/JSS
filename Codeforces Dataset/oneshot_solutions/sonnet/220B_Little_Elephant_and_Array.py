import sys
from math import isqrt

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    
    a = [0] + data[idx:idx + n]
    idx += n
    
    block = max(1, isqrt(n))
    queries = []
    for qi in range(m):
        l = data[idx]
        r = data[idx + 1]
        idx += 2
        queries.append((l, r, qi))
    
    queries.sort(key=lambda q: (q[0] // block, q[1] if (q[0] // block) % 2 == 0 else -q[1]))
    
    freq = [0] * (n + 1)
    answers = [0] * m
    current_answer = 0
    left = 1
    right = 0
    
    def add(pos):
        nonlocal current_answer
        x = a[pos]
        if x > n:
            return
        if freq[x] == x:
            current_answer -= 1
        freq[x] += 1
        if freq[x] == x:
            current_answer += 1
    
    def remove(pos):
        nonlocal current_answer
        x = a[pos]
        if x > n:
            return
        if freq[x] == x:
            current_answer -= 1
        freq[x] -= 1
        if freq[x] == x:
            current_answer += 1
    
    for l, r, qi in queries:
        while right < r:
            right += 1
            add(right)
        while right > r:
            remove(right)
            right -= 1
        while left < l:
            remove(left)
            left += 1
        while left > l:
            left -= 1
            add(left)
        
        answers[qi] = current_answer
    
    sys.stdout.write('\n'.join(map(str, answers)))

if __name__ == "__main__":
    main()
