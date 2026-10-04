# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    tasks = []
    known = []
    x = -1
    pos = 1
    for i in range(n):
        t = data[pos]
        s = data[pos + 1]
        p = data[pos + 2]
        pos += 3
        tasks.append((t, s, p))
        if p == -1:
            x = i
        else:
            known.append(p)
    target = data[pos]
    known.sort()
    reps = []
    cur = 1
    for p in known:
        if cur <= p - 1:
            reps.append(cur)
        cur = p + 1
    if cur <= 10 ** 9:
        reps.append(cur)
    inf = 10 ** 30

    def simulate(px, need_all=False):
        jobs = []
        for i, (t, s, p) in enumerate(tasks):
            if i == x:
                p = px
            jobs.append((t, i, s, p))
        jobs.sort()
        ans = [0] * n if need_all else None
        heap = []
        idx = 0
        now = 0
        while idx < n or heap:
            if not heap and idx < n and (now < jobs[idx][0]):
                now = jobs[idx][0]
            while idx < n and jobs[idx][0] <= now:
                t, i, s, p = jobs[idx]
                heapq.heappush(heap, (-p, i, s))
                idx += 1
            if not heap:
                continue
            next_time = jobs[idx][0] if idx < n else inf
            neg_p, i, rem = heapq.heappop(heap)
            can = next_time - now
            if rem <= can:
                now += rem
                if need_all:
                    ans[i] = now
                elif i == x:
                    return now
            else:
                now = next_time
                rem -= can
                heapq.heappush(heap, (neg_p, i, rem))
        return ans if need_all else None
    lo, hi = (0, len(reps) - 1)
    chosen = reps[0]
    while lo <= hi:
        mid = (lo + hi) // 2
        finish = simulate(reps[mid])
        if finish <= target:
            chosen = reps[mid]
            hi = mid - 1
        else:
            lo = mid + 1
    finished = simulate(chosen, True)
    sys.stdout.write(str(chosen) + '\n')
    sys.stdout.write(' '.join(map(str, finished)))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
