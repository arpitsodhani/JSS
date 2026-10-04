import sys

def ask(y):
    print(y, flush=True)
    s = sys.stdin.readline()
    if not s:
        sys.exit(0)
    return int(s)

def main():
    line = sys.stdin.readline().split()
    if not line:
        return
    m, n = map(int, line)

    sign = []
    for _ in range(n):
        res = ask(1)
        if res == 0:
            return
        sign.append(res)

    left, right = 1, m
    idx = 0

    while left <= right:
        mid = (left + right) // 2
        res = ask(mid)
        if res == 0:
            return

        res *= sign[idx]
        idx = (idx + 1) % n

        if res == 1:
            left = mid + 1
        else:
            right = mid - 1

if __name__ == "__main__":
    main()
