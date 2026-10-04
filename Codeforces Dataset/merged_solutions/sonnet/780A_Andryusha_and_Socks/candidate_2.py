# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    active = set()
    best = 0
    for sock in values[1:]:
        if sock in active:
            active.remove(sock)
        else:
            active.add(sock)
            if len(active) > best:
                best = len(active)

# CLAUSE: finish_program
    print(best)

if __name__ == "__main__":
    main()
