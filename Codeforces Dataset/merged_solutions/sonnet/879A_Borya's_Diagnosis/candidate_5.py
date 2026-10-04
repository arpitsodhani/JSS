# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    appointments = [(int(data[i]), int(data[i + 1])) for i in range(1, 2 * n, 2)]
    day = 0
    index = 0
    while index < n:
        start, interval = appointments[index]
        if start <= day:
            missed = day - start
            start += (missed // interval + 1) * interval
        day = start
        index += 1
    sys.stdout.write(f"{day}\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
