# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.40]
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


# Clause finish_program [Confidence: 0.40]
main()


