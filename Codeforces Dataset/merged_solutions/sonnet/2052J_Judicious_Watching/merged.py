# Clause setup_environment [Confidence: 0.60]
import sys


# Clause solve_logic [Confidence: 1.00]
def feasible(k, call_limit, work, watch):
    current = 0
    wi = 0
    si = 0
    work_len = len(work)
    while wi < work_len or si < k:
        if wi < work_len:
            need, due = work[wi]
        else:
            need, due = None, None
        if si < k:
            show = watch[si]
        else:
            show = None
        if show is None:
            if current + need > due:
                return False
            current += need
            wi += 1
        elif need is None:
            if current + show > call_limit:
                return False
            current += show
            si += 1
        elif current + show <= call_limit and current + show + need <= due:
            current += show
            si += 1
        elif current + need <= due:
            current += need
            wi += 1
        else:
            return False
    return True

def maximum_seen(call_limit, task_list, episode_list):
    lo = 0
    hi = len(episode_list)
    answer = 0
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if feasible(mid, call_limit, task_list, episode_list):
            answer = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return answer

def solve():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    t = numbers[p]
    p += 1
    lines = []
    for _ in range(t):
        n, m, q = numbers[p:p + 3]
        p += 3
        task_list = []
        for _ in range(n):
            task_list.append((numbers[p], numbers[p + 1]))
            p += 2
        task_list.sort(key=lambda pair: pair[1])
        episode_list = numbers[p:p + m]
        p += m
        query_list = numbers[p:p + q]
        p += q
        lines.append(" ".join(str(maximum_seen(x, task_list, episode_list)) for x in query_list))
    return "\n".join(lines)


# Clause finish_program [Confidence: 0.60]
sys.stdout.write(solve())


