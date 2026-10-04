import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        x = data[idx + 1]
        idx += 2
        a = data[idx:idx + n]
        idx += n

        if sum(a) % x != 0:
            ans.append(str(n))
            continue

        left = -1
        for i in range(n):
            if a[i] % x != 0:
                left = i
                break

        if left == -1:
            ans.append("-1")
            continue

        right = -1
        for i in range(n - 1, -1, -1):
            if a[i] % x != 0:
                right = i
                break

        ans.append(str(max(n - left - 1, right)))

    print("\n".join(ans))

if __name__ == "__main__":
    main()
