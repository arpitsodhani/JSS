import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    if n < 3:
        print(-1)
        return

    black = set()
    cnt = {}
    idx = 2

    for move in range(1, m + 1):
        x = data[idx]
        y = data[idx + 1]
        idx += 2

        if (x, y) in black:
            continue
        black.add((x, y))

        for i in range(max(1, x - 2), min(x, n - 2) + 1):
            for j in range(max(1, y - 2), min(y, n - 2) + 1):
                key = (i, j)
                val = cnt.get(key, 0) + 1
                if val == 9:
                    print(move)
                    return
                cnt[key] = val

    print(-1)

if __name__ == "__main__":
    main()
