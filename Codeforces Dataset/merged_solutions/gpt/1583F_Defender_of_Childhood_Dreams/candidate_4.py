# CLAUSE: derive_color_bound
import sys

def derive_color_bound(n, k):
    count = 0
    covered = 1
    while covered < max(1, n):
        covered *= k
        count += 1
    return count if n > 1 else 0

# CLAUSE: encode_vertices_base_k
def encode_vertices_base_k(n, k, c):
    rows = [[0 for _ in range(c)] for _ in range(n)]
    for v in range(n):
        x = v
        p = c - 1
        while p >= 0:
            rows[v][p] = x % k
            x //= k
            p -= 1
    return rows

# CLAUSE: select_discriminating_digit
def select_discriminating_digit(u, v, c):
    p = 0
    while p + 1 < c and u[p] == v[p]:
        p += 1
    return p + 1

# CLAUSE: emit_edge_coloring_order
def emit_edge_coloring_order(n, c, rows):
    buffer = []
    for u in range(n - 1):
        row_u = rows[u]
        segment = []
        for v in range(u + 1, n):
            segment.append(str(select_discriminating_digit(row_u, rows[v], c)))
        buffer.extend(segment)
    return buffer

# CLAUSE: verify_monochrome_path_limit
def verify_monochrome_path_limit(k, rows):
    return len(rows) == 0 or k > 0

# CLAUSE: handle_boundary_cases
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n, k = int(data[0]), int(data[1])
    c = derive_color_bound(n, k)
    rows = encode_vertices_base_k(n, k, c)
    output = [str(c), " ".join(emit_edge_coloring_order(n, c, rows))]
    sys.stdout.write("\n".join(output) + "\n")

main()
