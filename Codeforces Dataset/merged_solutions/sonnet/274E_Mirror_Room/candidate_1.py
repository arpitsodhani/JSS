# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from bisect import bisect_left, bisect_right
from collections import defaultdict

def direction_value(s):
    dr = -1 if s[0] == 'N' else 1
    dc = 1 if s[1] == 'E' else -1
    return dr, dc

def add_segment(segments, r, c, dr, dc, length):
    if dr == dc:
        key = (0, r - c)
    else:
        key = (1, r + c)
    
    end_r = r + dr * length
    lo = min(r, end_r)
    hi = max(r, end_r)
    segments[key].append((lo, hi))

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    k = int(data[idx + 2])
    idx += 3
    
    blocked = set()
    diag_down = defaultdict(list)
    diag_up = defaultdict(list)
    
    for _ in range(k):
        r = int(data[idx])
        c = int(data[idx + 1])
        idx += 2
        
        blocked.add((r, c))
        diag_down[r - c].append(r)
        diag_up[r + c].append(r)
    
    xs = int(data[idx])
    ys = int(data[idx + 1])
    direction = data[idx + 2].decode()
    
    if n == 1:
        cols = sorted(c for r, c in blocked if r == 1)
        pos = bisect_left(cols, ys)
        left = cols[pos - 1] if pos > 0 else 0
        right = cols[pos] if pos < len(cols) else m + 1
        print(right - left - 1)
        return
    
    if m == 1:
        rows = sorted(r for r, c in blocked if c == 1)
        pos = bisect_left(rows, xs)
        top = rows[pos - 1] if pos > 0 else 0
        bottom = rows[pos] if pos < len(rows) else n + 1
        print(bottom - top - 1)
        return
    
    for rows in diag_down.values():
        rows.sort()
    for rows in diag_up.values():
        rows.sort()
    
    def blocked_ahead(sr, sc, dr, dc):
        if not (1 <= sr <= n and 1 <= sc <= m):
            return None
        
        if dr == dc:
            rows = diag_down.get(sr - sc)
        else:
            rows = diag_up.get(sr + sc)
        
        if not rows:
            return None
        
        if dr == 1:
            pos = bisect_left(rows, sr)
            if pos == len(rows):
                return None
            return rows[pos] - sr
        else:
            pos = bisect_right(rows, sr) - 1
            if pos < 0:
                return None
            return sr - rows[pos]
    
    def is_wall(r, c):
        return r < 1 or r > n or c < 1 or c > m or (r, c) in blocked
    
    r, c = xs, ys
    dr, dc = direction_value(direction)
    
    seen = set()
    segments = defaultdict(list)
    
    while True:
        state = (r, c, dr, dc)
        if state in seen:
            break
        seen.add(state)
        
        best = n + m + k + 5
        
        row_border = n - r if dr == 1 else r - 1
        col_border = m - c if dc == 1 else c - 1
        best = min(best, row_border, col_border)
        
        candidates = [
            blocked_ahead(r + dr, c, dr, dc),
            blocked_ahead(r, c + dc, dr, dc),
            blocked_ahead(r + dr, c + dc, dr, dc),
        ]
        
        for value in candidates:
            if value is not None:
                best = min(best, value)
        
        add_segment(segments, r, c, dr, dc, best)
        
        pr = r + dr * best
        pc = c + dc * best
        
        row_wall = is_wall(pr + dr, pc)
        col_wall = is_wall(pr, pc + dc)
        diag_wall = is_wall(pr + dr, pc + dc)
        
        if row_wall and col_wall:
            r, c = pr, pc
            dr, dc = -dr, -dc
        elif row_wall:
            r, c = pr, pc + dc
            dr = -dr
        elif col_wall:
            r, c = pr + dr, pc
            dc = -dc
        elif diag_wall:
            r, c = pr, pc
            dr, dc = -dr, -dc
        else:
            break
    
    answer = 0
    for intervals in segments.values():
        intervals.sort()
        cur_l = cur_r = -1
        
        for l, rr in intervals:
            if cur_l == -1:
                cur_l, cur_r = l, rr
            elif l <= cur_r + 1:
                if rr > cur_r:
                    cur_r = rr
            else:
                answer += cur_r - cur_l + 1
                cur_l, cur_r = l, rr
        
        if cur_l != -1:
            answer += cur_r - cur_l + 1
    
    print(answer)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
