import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    nums = list(map(int, data))
    if len(nums) == 1:
        return

    n = nums[0]
    rest = nums[1:]

    if len(rest) >= 2 * n:
        x = rest[:n]
        b = rest[n:n + n]
        ans = 0
        for xi, bi in zip(x, b):
            ans ^= xi if bi else (1 ^ xi)
        print(ans)
    elif len(rest) >= n:
        b = rest[:n]
        print(sum(1 for v in b if v == 0) & 1)

if __name__ == "__main__":
    main()
