# CLAUSE: setup_environment
import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    s = int(data[1]) - 1
    k = int(data[2])
    nums = [int(x) for x in data[3:3 + n]]
    cols = data[3 + n].decode()
    inf = 10 ** 18

# CLAUSE: solve_logic
    dp = [[inf] * (k + 1) for _ in range(n)]
    buckets = sorted((nums[i], i, cols[i]) for i in range(n))

    for amount, idx, color in buckets:
        dp[idx][min(k, amount)] = abs(idx - s)

    for place, item in enumerate(buckets):
        amount, idx, color = item
        row = dp[idx]
        smaller = place - 1
        while smaller >= 0:
            prev_amount, prev_idx, prev_color = buckets[smaller]
            if prev_amount < amount and prev_color != color:
                previous = dp[prev_idx]
                distance = idx - prev_idx
                if distance < 0:
                    distance = -distance
                eaten = 0
                while eaten <= k:
                    old = previous[eaten]
                    if old != inf:
                        total = eaten + amount
                        if total > k:
                            total = k
                        candidate = old + distance
                        if candidate < row[total]:
                            row[total] = candidate
                    eaten += 1
            smaller -= 1

    answer = min(row[k] for row in dp)

# CLAUSE: finish_program
    sys.stdout.write("%d\n" % (-1 if answer == inf else answer))

if __name__ == "__main__":
    main()
