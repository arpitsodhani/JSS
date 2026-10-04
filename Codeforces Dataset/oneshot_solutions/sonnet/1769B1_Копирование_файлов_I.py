n = int(input())
a = list(map(int, input().split()))

total = sum(a)
matching = set()

# Initially both are 0
matching.add(0)

prefix_sum = 0
for i in range(n):
    for x in range(1, a[i] + 1):
        first_bar = (100 * x) // a[i]
        second_bar = (100 * (prefix_sum + x)) // total
        if first_bar == second_bar:
            matching.add(first_bar)
    prefix_sum += a[i]

result = sorted(matching)
for val in result:
    print(val)
