# CLAUSE: setup_environment
import sys

data = list(map(int, sys.stdin.buffer.read().split()))
pos = 0

# CLAUSE: solve_logic
def possible(count, limit, jobs, shows):
    time = 0
    i = 0
    j = 0
    n = len(jobs)
    while i < n or j < count:
        if i == n:
            length = shows[j]
            if time + length > limit:
                return False
            time += length
            j += 1
        elif j == count:
            length, due = jobs[i]
            if time + length > due:
                return False
            time += length
            i += 1
        else:
            task_len, due = jobs[i]
            ep_len = shows[j]
            if time + ep_len <= limit and time + ep_len + task_len <= due:
                time += ep_len
                j += 1
            elif time + task_len <= due:
                time += task_len
                i += 1
            else:
                return False
    return True

def solve():
    global pos
    tests = data[pos]
    pos += 1
    output = []
    for _ in range(tests):
        n, m, q = data[pos], data[pos + 1], data[pos + 2]
        pos += 3
        jobs = []
        for _ in range(n):
            jobs.append((data[pos], data[pos + 1]))
            pos += 2
        jobs.sort(key=lambda item: item[1])
        shows = data[pos:pos + m]
        pos += m
        queries = data[pos:pos + q]
        pos += q
        ans = []
        for limit in queries:
            lo, hi, best = 0, m, 0
            while lo <= hi:
                mid = (lo + hi) // 2
                if possible(mid, limit, jobs, shows):
                    best = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            ans.append(str(best))
        output.append(" ".join(ans))
    return "\n".join(output)

# CLAUSE: finish_program
sys.stdout.write(solve())
