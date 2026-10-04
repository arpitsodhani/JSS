# Clause setup_environment [Confidence: 0.80]
import sys

sys.setrecursionlimit(1000000)


# Clause solve_logic [Confidence: 1.00]
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return

    x, y, n, d = values[:4]
    vectors = []
    pos = 4
    for _ in range(n):
        vectors.append((values[pos], values[pos + 1]))
        pos += 2

    bound = d * d
    memo = {}
    active = set()

    def ok(a, b):
        return a * a + b * b <= bound

    def can_win(a, b, anton_reflected, dasha_reflected, turn):
        state = (a, b, anton_reflected, dasha_reflected, turn)
        if state in memo:
            return memo[state]
        if state in active:
            return False

        active.add(state)

        for dx, dy in vectors:
            nx = a + dx
            ny = b + dy
            if ok(nx, ny) and not can_win(nx, ny, anton_reflected, dasha_reflected, turn ^ 1):
                active.remove(state)
                memo[state] = True
                return True

        if turn == 0:
            if anton_reflected == 0 and ok(b, a) and not can_win(b, a, 1, dasha_reflected, 1):
                active.remove(state)
                memo[state] = True
                return True
        else:
            if dasha_reflected == 0 and ok(b, a) and not can_win(b, a, anton_reflected, 1, 0):
                active.remove(state)
                memo[state] = True
                return True

        active.remove(state)
        memo[state] = False
        return False

    sys.stdout.write("Anton\n" if can_win(x, y, 0, 0, 0) else "Dasha\n")


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


