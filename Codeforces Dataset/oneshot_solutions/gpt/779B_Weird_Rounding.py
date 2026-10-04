import sys

data = sys.stdin.read().split()
n = data[0]
k = int(data[1])

if k == 0:
    print(0)
else:
    zeros = 0
    deletions = 0

    for ch in reversed(n):
        if ch == '0':
            zeros += 1
            if zeros == k:
                print(deletions)
                break
        else:
            deletions += 1
    else:
        print(len(n) - 1)
