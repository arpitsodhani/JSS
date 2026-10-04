n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
total = sum(a)
taken = 0

for i, coin in enumerate(a, 1):
    taken += coin
    if taken > total - taken:
        print(i)
        break
