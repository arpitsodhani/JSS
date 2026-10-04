# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.60]
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


# Clause finish_program [Confidence: 0.60]
    print(answer)

if __name__ == "__main__":
    main()


