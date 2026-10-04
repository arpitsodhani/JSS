# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
MOD = 10**9 + 7

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, x, y = data[0], data[1], data[2]
    shows = []
    idx = 3
    for _ in range(n):
        l, r = data[idx], data[idx + 1]
        idx += 2
        shows.append((l, r))

    shows.sort()

    active = []
    available = []
    ans = 0

    for l, r in shows:
        while active and active[0] < l:
            heapq.heappush(available, -heapq.heappop(active))

        while available:
            end = -available[0]
            if y * (l - end) < x:
                heapq.heappop(available)
                ans = (ans + y * (r - end)) % MOD
                heapq.heappush(active, r)
                break
            else:
                heapq.heappop(available)
        else:
            ans = (ans + x + y * (r - l)) % MOD
            heapq.heappush(active, r)

    print(ans % MOD)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
