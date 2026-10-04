# CLAUSE: setup_environment
import sys
from heapq import heappush, heappop

# CLAUSE: solve_logic
def read_input():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    tasks = []
    missing = 0
    occupied = set()
    k = 1

    for i in range(n):
        item = [values[k], values[k + 1], values[k + 2]]
        k += 3
        tasks.append(item)
        if item[2] == -1:
            missing = i
        else:
            occupied.add(item[2])

    return tasks, missing, occupied, values[k]

def main():
    tasks, missing, occupied, limit_time = read_input()
    target_t, target_s = tasks[missing][0], tasks[missing][1]
    rivals = []
    for i, task in enumerate(tasks):
        if i != missing:
            rivals.append((task[0], task[1], task[2]))
    rivals.sort()

    def possible_end(rank):
        current = target_t
        left = target_s
        pending = 0
        before_seen = False
        previous = 0

        for arrival, size, priority in rivals:
            if priority <= rank:
                continue

            if arrival < target_t:
                if before_seen:
                    pending -= arrival - previous
                    if pending < 0:
                        pending = 0
                else:
                    before_seen = True
                pending += size
                previous = arrival
            else:
                if before_seen:
                    pending -= target_t - previous
                    if pending < 0:
                        pending = 0
                    before_seen = False

                gap = arrival - current
                if gap > 0:
                    if pending:
                        spent = pending if pending < gap else gap
                        pending -= spent
                        current += spent
                        gap -= spent
                    if gap:
                        if left <= gap:
                            return current + left
                        left -= gap
                        current = arrival

                pending += size

        if before_seen:
            pending -= target_t - previous
            if pending < 0:
                pending = 0

        return current + pending + left

    low = -10 ** 18
    high = 10 ** 18
    while low != high:
        middle = (low + high) // 2
        if possible_end(middle) <= limit_time:
            high = middle
        else:
            low = middle + 1

    answer_priority = low
    while answer_priority in occupied:
        answer_priority += 1

    tasks[missing][2] = answer_priority
    order = sorted(range(len(tasks)), key=lambda x: tasks[x][0])
    left_pages = [x[1] for x in tasks]
    finished = [0] * len(tasks)
    queue = []
    clock = 0
    ptr = 0
    total = len(tasks)

    while ptr < total or queue:
        if not queue:
            clock = max(clock, tasks[order[ptr]][0])

        while ptr < total and tasks[order[ptr]][0] <= clock:
            j = order[ptr]
            heappush(queue, (-tasks[j][2], j))
            ptr += 1

        neg_priority, j = heappop(queue)
        border = tasks[order[ptr]][0] if ptr < total else 10 ** 30
        available = border - clock

        if left_pages[j] > available:
            left_pages[j] -= available
            clock = border
            heappush(queue, (neg_priority, j))
        else:
            clock += left_pages[j]
            left_pages[j] = 0
            finished[j] = clock

    sys.stdout.write("{}\n{}".format(answer_priority, " ".join(map(str, finished))))

# CLAUSE: finish_program
main()
