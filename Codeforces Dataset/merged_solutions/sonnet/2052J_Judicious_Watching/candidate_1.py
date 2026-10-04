# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def can_watch_e_episodes(e, t_k, tasks, episodes):
    sorted_tasks = sorted(tasks, key=lambda x: x[1])
    
    current_time = 0
    task_idx = 0
    episode_idx = 0
    
    while task_idx < len(sorted_tasks) or episode_idx < e:
        has_task = task_idx < len(sorted_tasks)
        has_episode = episode_idx < e
        
        if not has_task and not has_episode:
            break
        
        if has_task and not has_episode:
            duration, deadline = sorted_tasks[task_idx]
            if current_time + duration > deadline:
                return False
            current_time += duration
            task_idx += 1
        elif has_episode and not has_task:
            if current_time + episodes[episode_idx] > t_k:
                return False
            current_time += episodes[episode_idx]
            episode_idx += 1
        else:
            task_duration, task_deadline = sorted_tasks[task_idx]
            episode_duration = episodes[episode_idx]
            
            can_watch_episode_now = current_time + episode_duration <= t_k
            task_ok_after_episode = current_time + episode_duration + task_duration <= task_deadline
            task_ok_now = current_time + task_duration <= task_deadline
            
            if can_watch_episode_now and task_ok_after_episode:
                current_time += episode_duration
                episode_idx += 1
            elif task_ok_now:
                current_time += task_duration
                task_idx += 1
            else:
                return False
    
    return True

def solve():
    t = int(input())
    for _ in range(t):
        n, m, q = map(int, input().split())
        tasks = []
        for i in range(n):
            a, d = map(int, input().split())
            tasks.append((a, d))
        episodes = list(map(int, input().split()))
        queries = list(map(int, input().split()))
        
        results = []
        for t_k in queries:
            left, right = 0, m
            answer = 0
            while left <= right:
                mid = (left + right) // 2
                if can_watch_e_episodes(mid, t_k, tasks, episodes):
                    answer = mid
                    left = mid + 1
                else:
                    right = mid - 1
            results.append(answer)
        
        print(' '.join(map(str, results)))

solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
