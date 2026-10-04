# CLAUSE: setup_environment
import sys

def emit(prefix, values):
    sys.stdout.write(prefix + " " + " ".join(map(str, values)) + "\n")
    sys.stdout.flush()

# CLAUSE: solve_logic
def solve():
    n_line = sys.stdin.readline().strip()
    n = int(n_line)
    total = n * n + 1
    saved_rows = []
    for block in range(n):
        start = block * (n + 1) + 1
        stop = start + n
        if start > total:
            break
        if stop > total:
            stop = total
        query = list(range(start, stop + 1))
        emit("?", [len(query)] + query)
        reply = list(map(int, sys.stdin.readline().split()))
        visible_count = reply[0]
        visible = reply[1:1 + visible_count]
        if visible_count >= n + 1:
            emit("!", visible[:n + 1])
            return
        saved_rows.append((query, frozenset(visible)))
    by_position = [[] for _ in range(n + 1)]
    for query, visible in saved_rows:
        for offset, index in enumerate(query):
            if index not in visible:
                by_position[offset].append(index)
    chosen = []
    for candidate in by_position:
        if len(candidate) >= n + 1:
            chosen = candidate[:n + 1]
            break
    if not chosen:
        chosen = list(range(1, n + 2))
    emit("!", chosen)

# CLAUSE: finish_program
solve()
