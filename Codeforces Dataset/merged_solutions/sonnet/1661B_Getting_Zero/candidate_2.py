# CLAUSE: setup_environment
import sys
from collections import deque

MOD = 32768

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    values = data[1:n + 1]

    dist = [-1] * MOD
    dist[0] = 0
    queue = deque([0])

    while queue:
        current = queue.popleft()
        step = dist[current] + 1

        before_add = (current - 1) & (MOD - 1)
        if dist[before_add] < 0:
            dist[before_add] = step
            queue.append(before_add)

        if current % 2 == 0:
            half = current // 2
            other_half = half + 16384

            if dist[half] < 0:
                dist[half] = step
                queue.append(half)

            if dist[other_half] < 0:
                dist[other_half] = step
                queue.append(other_half)

    sys.stdout.write(" ".join(str(dist[x]) for x in values))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
