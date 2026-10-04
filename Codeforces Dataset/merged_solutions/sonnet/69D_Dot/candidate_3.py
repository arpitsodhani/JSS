# CLAUSE: setup_environment
import sys

sys.setrecursionlimit(1000000)


# CLAUSE: solve_logic
def read_case():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return None
    nums = [int(v) for v in raw]
    x, y, n, d = nums[0], nums[1], nums[2], nums[3]
    pairs = list(zip(nums[4::2], nums[5::2]))
    return x, y, pairs[:n], d


def main():
    case = read_case()
    if case is None:
        return

    start_x, start_y, moves, radius = case
    radius_squared = radius * radius
    solved = {}
    stack_marks = set()

    def inside(point):
        px, py = point
        return px * px + py * py <= radius_squared

    def next_states(px, py, used_a, used_d, player):
        for vx, vy in moves:
            nxt = (px + vx, py + vy)
            if inside(nxt):
                yield nxt[0], nxt[1], used_a, used_d, player ^ 1
        swapped = (py, px)
        if inside(swapped):
            if player == 0 and not used_a:
                yield py, px, 1, used_d, 1
            elif player == 1 and not used_d:
                yield py, px, used_a, 1, 0

    def winning(px, py, used_a, used_d, player):
        state = (px, py, used_a, used_d, player)
        cached = solved.get(state)
        if cached is not None:
            return cached
        if state in stack_marks:
            return False

        stack_marks.add(state)
        answer = False
        for child in next_states(px, py, used_a, used_d, player):
            if not winning(*child):
                answer = True
                break
        stack_marks.remove(state)
        solved[state] = answer
        return answer

    winner = "Anton" if winning(start_x, start_y, 0, 0, 0) else "Dasha"
    print(winner)


# CLAUSE: finish_program
main()
