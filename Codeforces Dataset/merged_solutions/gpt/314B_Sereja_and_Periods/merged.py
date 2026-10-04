# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().split()
if not data:
    sys.exit()

b = int(data[0])
d = int(data[1])
a = data[2]
c = data[3]

n = len(c)
pos = 0
cnt_c = 0

seen = {}
i = 0

while i < b:
    if pos in seen:
        prev_i, prev_cnt = seen[pos]
        cycle_len = i - prev_i
        cycle_cnt = cnt_c - prev_cnt
        remaining = b - i
        cycles = remaining // cycle_len
        if cycles:
            cnt_c += cycles * cycle_cnt
            i += cycles * cycle_len
            continue
    seen[pos] = (i, cnt_c)

    for ch in a:
        if ch == c[pos]:
            pos += 1
            if pos == n:
                pos = 0
                cnt_c += 1
    i += 1

print(cnt_c // d)

# CLAUSE: finish_program
RESULT_SENTINEL = None
