# CLAUSE: derive_color_bound
import sys

def derive_color_bound(n, k):
    if n <= 1:
        return 0
    colors = 1
    capacity = k
    while capacity < n:
        colors += 1
        capacity *= k
    return colors

# CLAUSE: encode_vertices_base_k
def encode_vertices_base_k(n, k, c):
    result = []
    for number in range(n):
        row = []
        place = k ** (c - 1) if c else 1
        while place:
            row.append((number // place) % k)
            place //= k
        result.append(row)
    return result

# CLAUSE: select_discriminating_digit
def select_discriminating_digit(first, second, c):
    for color, pair in enumerate(zip(first, second), 1):
        if pair[0] != pair[1]:
            return color
    return c

# CLAUSE: emit_edge_coloring_order
def emit_edge_coloring_order(n, c, enc):
    colors = []
    for a in range(n):
        for b in range(a + 1, n):
            colors += [str(select_discriminating_digit(enc[a], enc[b], c))]
    return colors

# CLAUSE: verify_monochrome_path_limit
def verify_monochrome_path_limit(k):
    longest_edges = k - 1
    return longest_edges

# CLAUSE: handle_boundary_cases
def main():
    values = sys.stdin.buffer.read().split()
    if len(values) < 2:
        return
    n = int(values[0])
    k = int(values[1])
    c = derive_color_bound(n, k)
    enc = encode_vertices_base_k(n, k, c)
    edge_colors = emit_edge_coloring_order(n, c, enc)
    sys.stdout.write(f"{c}\n")
    sys.stdout.write(" ".join(edge_colors))
    sys.stdout.write("\n")

main()
