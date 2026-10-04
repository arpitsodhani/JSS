# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = [int(x) for x in sys.stdin.buffer.read().split()]
    n = data[0]
    queues = data[1:1 + n]
    times = []
    for position, queue_size in enumerate(queues):
        deficit = queue_size - position
        rounds = 0 if deficit <= 0 else (deficit + n - 1) // n
        times.append((position + rounds * n, position + 1))
    sys.stdout.write(str(min(times)[1]))

# CLAUSE: finish_program
main()
