# CLAUSE: setup_environment
import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) == 0:
        return
    n, k, b, c = data[0], data[1], data[2], data[3]
    vals = data[4:4 + n]
    step = min(b, c * 5)
    answer = None

# CLAUSE: solve_logic
    for target_rem in range(5):
        records = []
        append = records.append
        for x in vals:
            q = x // 5
            rem = x - q * 5
            delta = target_rem - rem
            if delta < 0:
                delta += 5
                q += 1
            append((q, delta * c - q * step))

        records.sort()
        selected = []
        subtotal = 0
        last_q = None

        for q, offset in records:
            if last_q is not None and q != last_q and len(selected) == k:
                value = k * last_q * step + subtotal
                answer = value if answer is None or value < answer else answer

            if len(selected) < k:
                heapq.heappush(selected, -offset)
                subtotal += offset
            elif offset < -selected[0]:
                old = -heapq.heapreplace(selected, -offset)
                subtotal += offset - old

            last_q = q

        if last_q is not None and len(selected) == k:
            value = k * last_q * step + subtotal
            answer = value if answer is None or value < answer else answer

# CLAUSE: finish_program
    print(answer)

if __name__ == "__main__":
    main()
