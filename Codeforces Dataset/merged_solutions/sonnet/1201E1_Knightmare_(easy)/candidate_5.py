# CLAUSE: setup_environment
import sys
from collections import deque

MOVES = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return

    n, m = values[0], values[1]
    total = n * m

    rows = [i // m for i in range(total)]
    cols = [i % m for i in range(total)]
    graph = [[] for _ in range(total)]
    can_hit = [[False] * total for _ in range(total)]

    for p in range(total):
        r = rows[p]
        c = cols[p]
        for dr, dc in MOVES:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m:
                q = nr * m + nc
                graph[p].append(q)
                can_hit[p][q] = True

    white_home = (n // 2 - 1) * m + (m // 2 - 1)
    black_home = (n // 2) * m + (m // 2 - 1)
    state_count = total * total * 2
    who = bytearray(state_count)
    degree = bytearray(state_count)
    move = [-1] * state_count
    queue = deque()

    def encode(w, b, turn):
        return ((w * total + b) << 1) | turn

    def decode(x):
        turn = x & 1
        x >>= 1
        b = x - (x // total) * total
        w = x // total
        return w, b, turn

    def terminal(w, b, turn):
        if w == b:
            if turn == 0:
                return 2
            return 1
        ok_w = w == white_home and not can_hit[b][w]
        ok_b = b == black_home and not can_hit[w][b]
        if ok_w and ok_b:
            if turn == 0:
                return 2
            return 1
        if ok_w:
            return 1
        if ok_b:
            return 2
        return 0

    for w in range(total):
        for b in range(total):
            first = encode(w, b, 0)
            second = first | 1
            degree[first] = len(graph[w])
            degree[second] = len(graph[b])
            first_win = terminal(w, b, 0)
            second_win = terminal(w, b, 1)
            if first_win:
                who[first] = first_win
                queue.append(first)
            elif degree[first] == 0:
                who[first] = 2
                queue.append(first)
            if second_win:
                who[second] = second_win
                queue.append(second)
            elif degree[second] == 0:
                who[second] = 1
                queue.append(second)

    while queue:
        current = queue.popleft()
        w, b, turn = decode(current)
        current_winner = who[current]
        earlier_turn = turn ^ 1
        earlier_player = earlier_turn + 1
        if earlier_turn == 0:
            for candidate in graph[w]:
                previous = encode(candidate, b, 0)
                if who[previous]:
                    continue
                if current_winner == earlier_player:
                    who[previous] = earlier_player
                    move[previous] = w
                    queue.append(previous)
                else:
                    degree[previous] -= 1
                    if degree[previous] == 0:
                        who[previous] = current_winner
                        queue.append(previous)
        else:
            for candidate in graph[b]:
                previous = encode(w, candidate, 1)
                if who[previous]:
                    continue
                if current_winner == earlier_player:
                    who[previous] = earlier_player
                    move[previous] = b
                    queue.append(previous)
                else:
                    degree[previous] -= 1
                    if degree[previous] == 0:
                        who[previous] = current_winner
                        queue.append(previous)

    w = (values[2] - 1) * m + values[3] - 1
    b = (values[4] - 1) * m + values[5] - 1
    turn = 0
    preferred = 0 if who[encode(w, b, 0)] == 1 else 1
    answer = []
    answer.append("WHITE" if preferred == 0 else "BLACK")

    def output_own_move():
        nonlocal w, b, turn
        s = encode(w, b, turn)
        nxt = move[s]
        if nxt == -1:
            return False
        answer.append(f"{rows[nxt] + 1} {cols[nxt] + 1}")
        if turn:
            b = nxt
        else:
            w = nxt
        turn = 1 - turn
        return True

    if preferred == 0:
        if not output_own_move() or terminal(w, b, turn):
            sys.stdout.write("\n".join(answer))
            return

    at = 6
    while at + 1 < len(values):
        nr = values[at] - 1
        nc = values[at + 1] - 1
        at += 2
        if nr < 0 or nc < 0:
            break
        if turn == 0:
            w = nr * m + nc
        else:
            b = nr * m + nc
        turn = 1 - turn
        if terminal(w, b, turn):
            break
        if turn == preferred:
            if not output_own_move() or terminal(w, b, turn):
                break

    sys.stdout.write("\n".join(answer))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
