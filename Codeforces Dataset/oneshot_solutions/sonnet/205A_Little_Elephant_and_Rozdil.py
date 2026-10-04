import sys

n = int(input())
times = list(map(int, input().split()))

min_time = min(times)
count = times.count(min_time)

if count == 1:
    print(times.index(min_time) + 1)
else:
    print("Still Rozdil")
