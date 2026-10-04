import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    idx += 1
    
    stones = data[idx:idx + n]
    idx += n
    
    sorted_stones = sorted(stones)
    
    prefix = [0] * (n + 1)
    sorted_prefix = [0] * (n + 1)
    
    for i in range(n):
        prefix[i + 1] = prefix[i] + stones[i]
        sorted_prefix[i + 1] = sorted_prefix[i] + sorted_stones[i]
    
    m = data[idx]
    idx += 1
    
    answers = []
    for _ in range(m):
        query_type = data[idx]
        l = data[idx + 1]
        r = data[idx + 2]
        idx += 3
        
        if query_type == 1:
            answers.append(str(prefix[r] - prefix[l - 1]))
        else:
            answers.append(str(sorted_prefix[r] - sorted_prefix[l - 1]))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
