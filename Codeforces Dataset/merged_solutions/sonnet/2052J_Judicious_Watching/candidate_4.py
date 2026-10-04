# CLAUSE: setup_environment
import sys

raw = sys.stdin.buffer.read().split()
idx = 0

# CLAUSE: solve_logic
def can_take(wanted, call_at, ordered_tasks, lengths):
    clock = 0
    ti = 0
    ei = 0
    total_tasks = len(ordered_tasks)
    while ti < total_tasks:
        task_len, deadline = ordered_tasks[ti]
        while ei < wanted and clock + lengths[ei] <= call_at and clock + lengths[ei] + task_len <= deadline:
            clock += lengths[ei]
            ei += 1
        if clock + task_len > deadline:
            return False
        clock += task_len
        ti += 1
    while ei < wanted:
        if clock + lengths[ei] > call_at:
            return False
        clock += lengths[ei]
        ei += 1
    return True

def read_int():
    global idx
    value = int(raw[idx])
    idx += 1
    return value

def solve():
    cases = read_int()
    result_lines = []
    for _ in range(cases):
        n = read_int()
        m = read_int()
        q = read_int()
        tasks = []
        for _ in range(n):
            duration = read_int()
            deadline = read_int()
            tasks.append((duration, deadline))
        tasks.sort(key=lambda x: x[1])
        episodes = [read_int() for _ in range(m)]
        queries = [read_int() for _ in range(q)]
        line = []
        for call_at in queries:
            left = 0
            right = m
            while left < right:
                middle = (left + right + 1) // 2
                if can_take(middle, call_at, tasks, episodes):
                    left = middle
                else:
                    right = middle - 1
            line.append(str(left))
        result_lines.append(" ".join(line))
    return result_lines

# CLAUSE: finish_program
sys.stdout.write("\n".join(solve()))
