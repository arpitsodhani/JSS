# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    buy = []
    sell = []
    cnt = []

    for _ in range(n):
        next(it)
        a_row = []
        b_row = []
        c_row = []
        for _ in range(m):
            a_row.append(int(next(it)))
            b_row.append(int(next(it)))
            c_row.append(int(next(it)))
        buy.append(a_row)
        sell.append(b_row)
        cnt.append(c_row)

    ans = 0

    for i in range(n):
        for t in range(n):
            if i == t:
                continue

            goods = []
            for j in range(m):
                profit = sell[t][j] - buy[i][j]
                if profit > 0 and cnt[i][j] > 0:
                    goods.append((profit, cnt[i][j]))

            goods.sort(reverse=True)

            left = k
            cur = 0
            for profit, amount in goods:
                take = min(left, amount)
                cur += take * profit
                left -= take
                if left == 0:
                    break

            if cur > ans:
                ans = cur

    print(ans)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
