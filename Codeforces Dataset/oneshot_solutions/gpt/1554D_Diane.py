import sys

n = int(sys.stdin.readline())
if n % 2:
    print("a" * (n // 2) + "b" + "a" * (n // 2))
else:
    print("a" * (n // 2 - 1) + "b" + "a" * (n // 2) + "c")
