def sieve(n):
    if n < 2:
        return [False] * (n + 1)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return is_prime

def check(a, b, k, l, prime_count):
    for x in range(a, b - l + 2):
        cnt = prime_count[x + l - 1] - prime_count[x - 1]
        if cnt < k:
            return False
    return True

a, b, k = map(int, input().split())

is_prime = sieve(b)

prime_count = [0] * (b + 1)
for i in range(1, b + 1):
    prime_count[i] = prime_count[i-1] + (1 if is_prime[i] else 0)

left, right = 1, b - a + 1
result = -1

while left <= right:
    mid = (left + right) // 2
    if check(a, b, k, mid, prime_count):
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)
