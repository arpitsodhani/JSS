# Clause setup_environment [Confidence: 0.60]
import sys
import heapq


# Clause solve_logic [Confidence: 1.00]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    pos = 1
    jobs = []
    used = set()
    special = -1

    for i in range(n):
        t, s, p = data[pos], data[pos + 1], data[pos + 2]
        pos += 3
        jobs.append([t, s, p])
        if p == -1:
            special = i
        else:
            used.add(p)

    wanted = data[pos]
    start = jobs[special][0]
    pages = jobs[special][1]
    ordered = sorted((jobs[i][0], jobs[i][1], jobs[i][2]) for i in range(n) if i != special)

    def finish_time(priority):
        cur = start
        need = pages
        backlog = 0
        last = None

        for t, s, p in ordered:
            if p <= priority:
                continue

            if t < start:
                if last is not None:
                    backlog = max(0, backlog - (t - last))
                backlog += s
                last = t
                continue

            if last is not None:
                backlog = max(0, backlog - (start - last))
                last = None

            if cur < t:
                take = min(backlog, t - cur)
                backlog -= take
                cur += take
                if cur < t:
                    free = t - cur
                    if need <= free:
                        return cur + need
                    need -= free
                    cur = t

            backlog += s

        if last is not None:
            backlog = max(0, backlog - (start - last))

        return cur + backlog + need

    lo, hi = -10 ** 18, 10 ** 18
    while lo < hi:
        mid = (lo + hi) // 2
        if finish_time(mid) <= wanted:
            hi = mid
        else:
            lo = mid + 1

    priority = lo
    while priority in used:
        priority += 1

    jobs[special][2] = priority
    arrivals = sorted((jobs[i][0], i) for i in range(n))
    remain = [job[1] for job in jobs]
    done = [0] * n
    heap = []
    cur = 0
    i = 0

    while i < n or heap:
        if not heap and cur < arrivals[i][0]:
            cur = arrivals[i][0]

        while i < n and arrivals[i][0] <= cur:
            task = arrivals[i][1]
            heapq.heappush(heap, (-jobs[task][2], task))
            i += 1

        negp, task = heapq.heappop(heap)
        nxt = arrivals[i][0] if i < n else 10 ** 30
        amount = nxt - cur

        if remain[task] <= amount:
            cur += remain[task]
            remain[task] = 0
            done[task] = cur
        else:
            remain[task] -= amount
            cur = nxt
            heapq.heappush(heap, (negp, task))

    sys.stdout.write(str(priority) + "\n" + " ".join(map(str, done)))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


