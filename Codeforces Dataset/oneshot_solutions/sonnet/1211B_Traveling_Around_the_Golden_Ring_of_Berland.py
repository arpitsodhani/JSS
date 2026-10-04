n = int(input())
a = list(map(int, input().split()))

max_visits = 1  # We always visit city 1 at least once

for i in range(n):
    if a[i] > 0:
        # Last selfie at city i (0-indexed) is taken at visit: (i+1) + (a[i]-1) * n
        last_visit = (i + 1) + (a[i] - 1) * n
        max_visits = max(max_visits, last_visit)

print(max_visits)
