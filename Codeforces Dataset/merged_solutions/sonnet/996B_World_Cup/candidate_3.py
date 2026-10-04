# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def arrival_time(index, queue, total):
    remaining = queue - index
    if remaining <= 0:
        return index
    return index + ((remaining + total - 1) // total) * total

def main():
    values = tuple(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    queues = values[1:]
    chosen = min(range(n), key=lambda pos: arrival_time(pos, queues[pos], n))
    print(chosen + 1)

# CLAUSE: finish_program
main()
