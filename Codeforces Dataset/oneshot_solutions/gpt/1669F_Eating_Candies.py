import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        l, r = 0, n - 1
        left_sum = 0
        right_sum = 0
        best = 0

        while l <= r:
            if left_sum <= right_sum:
                left_sum += a[l]
                l += 1
            else:
                right_sum += a[r]
                r -= 1

            if left_sum == right_sum:
                best = l + (n - 1 - r)

        ans.append(str(best))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
