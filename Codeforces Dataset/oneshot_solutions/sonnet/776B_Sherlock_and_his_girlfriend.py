import sys

def main():
    n = int(sys.stdin.readline())
    
    if n <= 2:
        print(1)
        print(' '.join(['1'] * n))
        return
    
    limit = n + 1
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for x in range(p * p, limit + 1, p):
                is_prime[x] = False
        p += 1
    
    colors = []
    for value in range(2, limit + 1):
        colors.append(1 if is_prime[value] else 2)
    
    print(2)
    print(' '.join(map(str, colors)))

if __name__ == "__main__":
    main()
