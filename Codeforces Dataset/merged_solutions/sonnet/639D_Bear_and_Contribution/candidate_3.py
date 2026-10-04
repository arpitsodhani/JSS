# CLAUSE: setup_environment
import sys
from heapq import heappush, heapreplace

def candidate_for(value, residue, unit):
    q, rem = divmod(value, 5)
    add = residue - rem
    if add < 0:
        add += 5
        q += 1
    return q, add * unit - q * unit5

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, k, b, c = data[:4]
    arr = data[4:4 + n]
    global unit5
    unit5 = min(b, 5 * c)
    answer = 10 ** 30

# CLAUSE: solve_logic
    for residue in range(5):
        grouped = {}
        for value in arr:
            q, fixed = candidate_for(value, residue, c)
            grouped.setdefault(q, []).append(fixed)

        picked = []
        running = 0
        for q in sorted(grouped):
            for fixed in grouped[q]:
                neg = -fixed
                if len(picked) < k:
                    heappush(picked, neg)
                    running += fixed
                elif neg > picked[0]:
                    running += fixed + heapreplace(picked, neg)
            if len(picked) == k:
                cost = k * q * unit5 + running
                if cost < answer:
                    answer = cost

# CLAUSE: finish_program
    print(answer)

if __name__ == "__main__":
    main()
