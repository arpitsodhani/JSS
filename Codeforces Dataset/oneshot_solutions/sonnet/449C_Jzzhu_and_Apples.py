import sys

def main():
    n = int(sys.stdin.readline())
    
    is_prime = [True] * (n + 1)
    if n >= 0:
        is_prime[0] = False
    if n >= 1:
        is_prime[1] = False
    
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            if i * i <= n:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
    
    used = [False] * (n + 1)
    pairs = []
    
    for p in primes:
        if p == 2:
            continue
        if p * 2 > n:
            break
        
        multiples = []
        for x in range(p, n + 1, p):
            if not used[x]:
                multiples.append(x)
        
        start = 0
        if len(multiples) % 2 == 1:
            pairs.append((multiples[0], multiples[2]))
            used[multiples[0]] = True
            used[multiples[2]] = True
            start = 3
        
        for i in range(start, len(multiples), 2):
            pairs.append((multiples[i], multiples[i + 1]))
            used[multiples[i]] = True
            used[multiples[i + 1]] = True
    
    evens = []
    for x in range(2, n + 1, 2):
        if not used[x]:
            evens.append(x)
    
    for i in range(0, len(evens) - 1, 2):
        pairs.append((evens[i], evens[i + 1]))
    
    print(len(pairs))
    for a, b in pairs:
        print(a, b)

if __name__ == "__main__":
    main()
