# CLAUSE: setup_environment
import sys
from collections import deque

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    n = int(raw[0])
    b = int(raw[1])
    busy_until = deque()
    out = [""] * n
    item = 2
    for i in range(n):
        arrival = int(raw[item])
        duration = int(raw[item + 1])
        item += 2
        while busy_until:
            if busy_until[0] > arrival:
                break
            busy_until.popleft()
        if len(busy_until) <= b:
            if busy_until:
                end_time = busy_until[-1] + duration
            else:
                end_time = arrival + duration
            busy_until.append(end_time)
            out[i] = str(end_time)
        else:
            out[i] = "-1"
    print(" ".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
