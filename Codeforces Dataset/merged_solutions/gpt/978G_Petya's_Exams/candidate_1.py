# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
exams = []
by_start = [[] for _ in range(n + 2)]
exam_day = [0] * (n + 2)

p = 2
ok = True

for i in range(1, m + 1):
    s, d, c = data[p], data[p + 1], data[p + 2]
    p += 3
    exams.append((s, d, c))
    by_start[s].append(i)
    if exam_day[d] != 0:
        ok = False
    exam_day[d] = i

if not ok:
    print(-1)
    sys.exit()

remaining = [0] * (m + 1)
deadline = [0] * (m + 1)

for i, (s, d, c) in enumerate(exams, 1):
    remaining[i] = c
    deadline[i] = d

ans = [0] * (n + 1)
heap = []

for day in range(1, n + 1):
    for idx in by_start[day]:
        heapq.heappush(heap, (deadline[idx], idx))

    if exam_day[day]:
        idx = exam_day[day]
        if remaining[idx] != 0:
            print(-1)
            sys.exit()
        ans[day] = m + 1
        continue

    while heap and remaining[heap[0][1]] == 0:
        heapq.heappop(heap)

    if heap:
        d, idx = heapq.heappop(heap)
        if d <= day:
            print(-1)
            sys.exit()
        ans[day] = idx
        remaining[idx] -= 1
        if remaining[idx] > 0:
            heapq.heappush(heap, (d, idx))

if any(remaining[i] for i in range(1, m + 1)):
    print(-1)
else:
    print(*ans[1:])

# CLAUSE: finish_program
RESULT_SENTINEL = None
