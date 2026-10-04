# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    tasks = []
    known = set()
    unknown = None

    for i in range(n):
        base = 1 + 3 * i
        t = raw[base]
        s = raw[base + 1]
        p = raw[base + 2]
        tasks.append([t, s, p])
        if p < 0 and p == -1:
            unknown = i
        else:
            known.add(p)

    fixed_finish = raw[1 + 3 * n]
    begin = tasks[unknown][0]
    volume = tasks[unknown][1]
    others = [(task[0], task[1], task[2]) for i, task in enumerate(tasks) if i != unknown]
    others.sort(key=lambda x: x[0])

    def end_for(priority):
        time = begin
        need = volume
        load = 0
        last_before = -1

        for item in others:
            arrival, size, pr = item
            if pr <= priority:
                continue

            if arrival < begin:
                if last_before >= 0:
                    load = max(0, load - arrival + last_before)
                load += size
                last_before = arrival
            else:
                if last_before >= 0:
                    load = max(0, load - begin + last_before)
                    last_before = -1

                if time < arrival:
                    step = arrival - time
                    if load >= step:
                        load -= step
                        time = arrival
                    else:
                        time += load
                        step -= load
                        load = 0
                        if need <= step:
                            return time + need
                        need -= step
                        time = arrival

                load += size

        if last_before >= 0:
            load = max(0, load - begin + last_before)

        return time + load + need

    left = -10 ** 18
    right = 10 ** 18
    while left + 1 < right:
        mid = (left + right) // 2
        if end_for(mid) <= fixed_finish:
            right = mid
        else:
            left = mid

    chosen = right
    while chosen in known:
        chosen += 1

    tasks[unknown][2] = chosen

    incoming = {}
    for i, task in enumerate(tasks):
        incoming.setdefault(task[0], []).append(i)
    times = sorted(incoming)

    remaining = [task[1] for task in tasks]
    finished_at = [0] * n
    heap = []
    current = 0
    idx = 0

    while idx < len(times) or heap:
        if not heap and idx < len(times) and current < times[idx]:
            current = times[idx]

        while idx < len(times) and times[idx] <= current:
            for task_id in incoming[times[idx]]:
                heapq.heappush(heap, (-tasks[task_id][2], task_id))
            idx += 1

        neg_pr, task_id = heapq.heappop(heap)
        next_arrival = times[idx] if idx < len(times) else 10 ** 30
        delta = next_arrival - current

        if remaining[task_id] <= delta:
            current += remaining[task_id]
            finished_at[task_id] = current
            remaining[task_id] = 0
        else:
            remaining[task_id] -= delta
            current = next_arrival
            heapq.heappush(heap, (neg_pr, task_id))

    out = [str(chosen), " ".join(str(x) for x in finished_at)]
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
