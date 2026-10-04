# CLAUSE: setup_environment
import sys

sys.setrecursionlimit(1000000)


# CLAUSE: solve_logic
def main():
    data = tuple(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    start = data[0], data[1]
    count = data[2]
    radius = data[3]
    moves = [data[i:i + 2] for i in range(4, 4 + 2 * count, 2)]
    square_limit = radius * radius
    memo = {}
    pending = set()

    def allowed(px, py):
        return px * px + py * py <= square_limit

    def has_winning_move(px, py, used_first, used_second, side):
        key = px, py, used_first, used_second, side
        if key in memo:
            return memo[key]
        if key in pending:
            return False

        pending.add(key)

        candidates = []
        candidates.extend((px + dx, py + dy, used_first, used_second, side ^ 1) for dx, dy in moves)
        if side == 0 and used_first == 0:
            candidates.append((py, px, 1, used_second, 1))
        if side == 1 and used_second == 0:
            candidates.append((py, px, used_first, 1, 0))

        for nx, ny, next_first, next_second, next_side in candidates:
            if allowed(nx, ny) and not has_winning_move(nx, ny, next_first, next_second, next_side):
                pending.remove(key)
                memo[key] = True
                return True

        pending.remove(key)
        memo[key] = False
        return False

    print("Anton" if has_winning_move(start[0], start[1], 0, 0, 0) else "Dasha")


# CLAUSE: finish_program
if __name__ == "__main__":
    main()
