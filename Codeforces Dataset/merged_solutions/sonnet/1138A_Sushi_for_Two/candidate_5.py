# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    arr = data[1:n + 1]
    best = 0
    previous = 0
    current = 0
    last = None
    for item in arr:
        if item == last:
            current += 1
        else:
            if last is not None:
                possible = 2 * min(previous, current)
                if possible > best:
                    best = possible
                previous = current
            last = item
            current = 1
    possible = 2 * min(previous, current)
    if possible > best:
        best = possible
    print(best)

# CLAUSE: finish_program
main()
