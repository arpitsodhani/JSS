import sys
from collections import deque
from array import array

KNIGHT_STEPS = (
    (1, 2), (1, -2), (-1, 2), (-1, -2),
    (2, 1), (2, -1), (-2, 1), (-2, -1)
)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n, m = data[0], data[1]
    x1, y1, x2, y2 = data[2] - 1, data[3] - 1, data[4] - 1, data[5] - 1
    idx = 6
    
    total = n * m
    
    def pos(r, c):
        return r * m + c
    
    def row_col(p):
        return divmod(p, m)
    
    moves = [[] for _ in range(total)]
    attacks = [bytearray(total) for _ in range(total)]
    
    for r in range(n):
        for c in range(m):
            p = pos(r, c)
            for dr, dc in KNIGHT_STEPS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    q = pos(nr, nc)
                    moves[p].append(q)
                    attacks[p][q] = 1
    
    white_goal = pos(n // 2 - 1, m // 2 - 1)
    black_goal = pos(n // 2, m // 2 - 1)
    
    states = total * total * 2
    winner = bytearray(states)
    remaining = bytearray(states)
    chosen = array('i', [-1]) * states
    queue = deque()
    
    def state_id(w, b, turn):
        return ((w * total + b) << 1) | turn
    
    def decode(s):
        turn = s & 1
        v = s >> 1
        b = v % total
        w = v // total
        return w, b, turn
    
    def terminal_winner(w, b, turn):
        if w == b:
            return 2 if turn == 0 else 1
        
        white_safe = w == white_goal and not attacks[b][w]
        black_safe = b == black_goal and not attacks[w][b]
        
        if white_safe and black_safe:
            return 2 if turn == 0 else 1
        if white_safe:
            return 1
        if black_safe:
            return 2
        return 0
    
    for w in range(total):
        for b in range(total):
            base = (w * total + b) << 1
            
            remaining[base] = len(moves[w])
            remaining[base | 1] = len(moves[b])
            
            for turn in range(2):
                sid = base | turn
                win = terminal_winner(w, b, turn)
                if win:
                    winner[sid] = win
                    queue.append(sid)
                elif remaining[sid] == 0:
                    winner[sid] = 2 if turn == 0 else 1
                    queue.append(sid)
    
    while queue:
        sid = queue.popleft()
        w, b, turn = decode(sid)
        cur_win = winner[sid]
        prev_turn = turn ^ 1
        mover_win = prev_turn + 1
        
        if prev_turn == 0:
            for pw in moves[w]:
                pid = state_id(pw, b, 0)
                if winner[pid]:
                    continue
                
                if cur_win == mover_win:
                    winner[pid] = mover_win
                    chosen[pid] = w
                    queue.append(pid)
                else:
                    remaining[pid] -= 1
                    if remaining[pid] == 0:
                        winner[pid] = cur_win
                        queue.append(pid)
        else:
            for pb in moves[b]:
                pid = state_id(w, pb, 1)
                if winner[pid]:
                    continue
                
                if cur_win == mover_win:
                    winner[pid] = mover_win
                    chosen[pid] = b
                    queue.append(pid)
                else:
                    remaining[pid] -= 1
                    if remaining[pid] == 0:
                        winner[pid] = cur_win
                        queue.append(pid)
    
    w = pos(x1, y1)
    b = pos(x2, y2)
    turn = 0
    
    initial = state_id(w, b, turn)
    alice = 0 if winner[initial] == 1 else 1
    
    out = []
    out.append("WHITE" if alice == 0 else "BLACK")
    
    def make_move():
        nonlocal w, b, turn
        sid = state_id(w, b, turn)
        to = chosen[sid]
        
        if to == -1:
            return False
        
        r, c = row_col(to)
        out.append(f"{r + 1} {c + 1}")
        
        if turn == 0:
            w = to
        else:
            b = to
        turn ^= 1
        return True
    
    if turn == alice:
        if not make_move() or terminal_winner(w, b, turn):
            print('\n'.join(out))
            return
    
    while idx + 1 < len(data):
        nr, nc = data[idx] - 1, data[idx + 1] - 1
        idx += 2
        
        if nr < 0 or nc < 0:
            break
        
        if turn == 0:
            w = pos(nr, nc)
        else:
            b = pos(nr, nc)
        turn ^= 1
        
        if terminal_winner(w, b, turn):
            break
        
        if turn == alice:
            if not make_move() or terminal_winner(w, b, turn):
                break
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
