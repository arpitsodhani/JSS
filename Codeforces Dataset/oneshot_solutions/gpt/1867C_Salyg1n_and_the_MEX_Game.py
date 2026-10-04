import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = set(a)

    mex = 0
    while mex in s:
        mex += 1

    print(mex, flush=True)

    while True:
        y_line = input()
        if not y_line:
            sys.exit()
        y = int(y_line)
        if y == -1:
            break
        print(y, flush=True)
