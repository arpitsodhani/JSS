# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    items = list(map(int, sys.stdin.buffer.read().split()))
    n = items[0]
    next_station = [0] + items[1:1 + n]

    sizes = []
    for start in range(1, n + 1):
        if next_station[start] < 0:
            continue
        station = start
        size = 0
        while next_station[station] > 0:
            following = next_station[station]
            next_station[station] = -following
            size += 1
            station = following
        sizes.append(size)

    first = 0
    second = 0
    answer = 0
    for size in sizes:
        answer += size * size
        if size >= first:
            second = first
            first = size
        elif size > second:
            second = size

    answer += 2 * first * second
    print(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
