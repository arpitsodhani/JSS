t = int(input())
for _ in range(t):
    n = int(input())
    result = 0
    for _ in range(2 * n + 1):
        s = input()
        for c in s:
            result ^= ord(c)
    print(chr(result))
