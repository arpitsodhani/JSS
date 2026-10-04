import sys

segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

a, b = map(int, sys.stdin.read().split())
total = 0

for n in range(a, b + 1):
    for ch in str(n):
        total += segments[ord(ch) - 48]

print(total)
