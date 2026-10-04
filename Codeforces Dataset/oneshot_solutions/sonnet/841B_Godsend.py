n = int(input())
a = list(map(int, input().split()))

odd_count = sum(1 for x in a if x % 2 == 1)

if odd_count >= 1:
    print("First")
else:
    print("Second")
