import sys

def solve(n, k):
    if k == (n + 1) // 2:
        return (1, [n])
    elif k % 2 == 0 and 2 <= k <= n - 1:
        return (3, [k - 1, 1, n - k])
    elif k % 2 == 1 and 3 <= k <= n - 2:
        return (3, [k - 2, 3, n - k - 1])
    else:
        return (-1, [])

def main():
    input_data = sys.stdin.read().strip().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    for _ in range(t):
        n = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2
        m, sizes = solve(n, k)
        if m == -1:
            print(-1)
        else:
            print(m)
            print(' '.join(map(str, sizes)))

if __name__ == "__main__":
    main()
