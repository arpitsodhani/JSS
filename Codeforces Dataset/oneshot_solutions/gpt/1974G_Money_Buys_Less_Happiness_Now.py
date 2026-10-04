import sys
import heapq

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        m = data[idx]
        x = data[idx + 1]
        idx += 2

        money = 0
        bought = []

        for _ in range(m):
            c = data[idx]
            idx += 1

            if money >= c:
                money -= c
                heapq.heappush(bought, -c)
            elif bought and -bought[0] > c:
                money += -heapq.heappop(bought) - c
                heapq.heappush(bought, -c)

            money += x

        ans.append(str(len(bought)))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
