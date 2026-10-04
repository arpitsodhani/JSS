def solve(n):
    for a in range(2, int(n**0.5) + 1):
        if n % a == 0:
            remaining = n // a
            for b in range(2, int(remaining**0.5) + 1):
                if b != a and remaining % b == 0:
                    c = remaining // b
                    if c >= 2 and c != a and c != b:
                        return True, a, b, c
    return False, 0, 0, 0

t = int(input())
for _ in range(t):
    n = int(input())
    success, a, b, c = solve(n)
    if success:
        print("YES")
        print(a, b, c)
    else:
        print("NO")
