import sys

def solve_case(n, a):
    prefix_good = [False] * (n + 1)
    suffix_good = [False] * (n + 2)
    
    seen = set()
    ok = True
    current_max = 0
    
    for i in range(1, n + 1):
        x = a[i - 1]
        if x in seen:
            ok = False
        seen.add(x)
        current_max = max(current_max, x)
        
        if ok and current_max == i:
            prefix_good[i] = True
    
    seen.clear()
    ok = True
    current_max = 0
    
    for i in range(n, 0, -1):
        x = a[i - 1]
        if x in seen:
            ok = False
        seen.add(x)
        current_max = max(current_max, x)
        
        length = n - i + 1
        if ok and current_max == length:
            suffix_good[i] = True
    
    answer = []
    for first_len in range(1, n):
        second_len = n - first_len
        if prefix_good[first_len] and suffix_good[first_len + 1]:
            answer.append((first_len, second_len))
    
    return answer

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    output = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        answer = solve_case(n, a)
        output.append(str(len(answer)))
        for x, y in answer:
            output.append(f"{x} {y}")
    
    print('\n'.join(output))

if __name__ == "__main__":
    main()
