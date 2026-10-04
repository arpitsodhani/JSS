import sys

# CLAUSE: track_painted_cells
def prepare_board(n):
    return [[0] * n for _ in range(n)]

# CLAUSE: enumerate_affected_windows
def candidate_tops_lefts(r, c):
    for top in (r - 2, r - 1, r):
        for left in (c - 2, c - 1, c):
            yield top, left

# CLAUSE: validate_window_bounds
def is_usable(top, left, n):
    return 0 <= top and top + 3 <= n and 0 <= left and left + 3 <= n

# CLAUSE: update_window_occupancy
def count_window(board, top, left):
    total = 0
    for rr in range(top, top + 3):
        total += board[rr][left] + board[rr][left + 1] + board[rr][left + 2]
    return total

# CLAUSE: detect_completed_square
def creates_square(board, r, c, n):
    for top, left in candidate_tops_lefts(r, c):
        if is_usable(top, left, n) and count_window(board, top, left) == 9:
            return True
    return False

# CLAUSE: preserve_earliest_move
def main():
    tokens = tuple(map(int, sys.stdin.buffer.read().split()))
    if not tokens:
        return
    n, m = tokens[0], tokens[1]
    board = prepare_board(n)
    answer = -1
    pos = 2
    for step in range(1, m + 1):
        r = tokens[pos] - 1
        c = tokens[pos + 1] - 1
        pos += 2
        if answer == -1:
            board[r][c] = 1
            if creates_square(board, r, c, n):
                answer = step
    print(answer)

main()
