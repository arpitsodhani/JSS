import sys

def digit_sum(x):
    total = 0
    while x:
        total += x % 10
        x //= 10
    return total

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    queries = data[1:]
    
    limit = max(queries)
    pref = [0] * (limit + 1)
    
    for i in range(1, limit + 1):
        pref[i] = pref[i - 1] + digit_sum(i)
    
    ans = []
    for n in queries:
        ans.append(str(pref[n]))
    
    print('\n'.join(ans))

if __name__ == "__main__":
    main()
