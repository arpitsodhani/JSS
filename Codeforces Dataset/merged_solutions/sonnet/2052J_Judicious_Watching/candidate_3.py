# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def check(episodes_needed, call_time, tasks, episodes):
    now = 0
    task_index = 0
    episode_index = 0
    task_count = len(tasks)
    while True:
        task_left = task_index < task_count
        episode_left = episode_index < episodes_needed
        if not task_left and not episode_left:
            return True
        if task_left and episode_left:
            episode_time = episodes[episode_index]
            task_time, deadline = tasks[task_index]
            if now + episode_time <= call_time and now + episode_time + task_time <= deadline:
                now += episode_time
                episode_index += 1
                continue
            if now + task_time <= deadline:
                now += task_time
                task_index += 1
                continue
            return False
        if task_left:
            task_time, deadline = tasks[task_index]
            if now + task_time > deadline:
                return False
            now += task_time
            task_index += 1
        else:
            episode_time = episodes[episode_index]
            if now + episode_time > call_time:
                return False
            now += episode_time
            episode_index += 1

def solve_case(n, m, q, tasks, episodes, queries):
    tasks = sorted(tasks, key=lambda pair: pair[1])
    values = []
    for call_time in queries:
        low = 0
        high = m + 1
        while high - low > 1:
            middle = (low + high) // 2
            if check(middle, call_time, tasks, episodes):
                low = middle
            else:
                high = middle
        values.append(str(low))
    return " ".join(values)

def solve():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = next(tokens)
    lines = []
    for _ in range(t):
        n = next(tokens)
        m = next(tokens)
        q = next(tokens)
        tasks = [(next(tokens), next(tokens)) for _ in range(n)]
        episodes = [next(tokens) for _ in range(m)]
        queries = [next(tokens) for _ in range(q)]
        lines.append(solve_case(n, m, q, tasks, episodes, queries))
    return "\n".join(lines)

# CLAUSE: finish_program
print(solve())
