# CLAUSE: setup_environment
import sys
import heapq

MOD = 10**9 + 7

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    ans = []
    for _ in range(t):
        n = data[p]
        k = data[p + 1]
        p += 2
        values = data[p:p + n]
        p += n
        heap = values[:]
        heapq.heapify(heap)
        active = set(values)
        score = 1
        for _ in range(k):
            while heap and heap[0] not in active:
                heapq.heappop(heap)
            if not heap:
                break
            m = heapq.heappop(heap)
            active.remove(m)
            score = score * m % MOD
            for x in range(1, m):
                if x not in active:
                    active.add(x)
                    heapq.heappush(heap, x)
        ans.append(str(score))
    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
