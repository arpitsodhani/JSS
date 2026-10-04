def is_sorted(a):
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            return False
    return True

def solve(n, a):
    iterations = 0
    while not is_sorted(a):
        iterations += 1
        if iterations % 2 == 1:  # odd iteration
            for i in range(0, n-1, 2):
                if a[i] > a[i+1]:
                    a[i], a[i+1] = a[i+1], a[i]
        else:  # even iteration
            for i in range(1, n-1, 2):
                if a[i] > a[i+1]:
                    a[i], a[i+1] = a[i+1], a[i]
    return iterations

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
