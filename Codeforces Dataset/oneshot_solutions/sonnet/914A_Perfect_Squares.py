def is_perfect_square(x):
    if x < 0:
        return False
    sqrt_x = int(x ** 0.5)
    return sqrt_x * sqrt_x == x or (sqrt_x + 1) * (sqrt_x + 1) == x

n = int(input())
arr = list(map(int, input().split()))

result = max(x for x in arr if not is_perfect_square(x))
print(result)
