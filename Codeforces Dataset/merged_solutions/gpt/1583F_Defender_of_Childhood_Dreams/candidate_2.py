# CLAUSE: derive_color_bound
import sys

def derive_color_bound(n, k):
    if n < 2:
        return 0
    need = n
    colors = 0
    while need > 1:
        need = (need + k - 1) // k
        colors += 1
    return colors

# CLAUSE: encode_vertices_base_k
def encode_vertices_base_k(n, k, c):
    table = []
    divisors = [1] * c
    for idx in range(c - 2, -1, -1):
        divisors[idx] = divisors[idx + 1] * k
    for value in range(n):
        table.append([(value // base) % k for base in divisors])
    return table

# CLAUSE: select_discriminating_digit
def select_discriminating_digit(x_digits, y_digits, c):
    pos = 0
    while pos < c and x_digits[pos] == y_digits[pos]:
        pos += 1
    return pos + 1

# CLAUSE: emit_edge_coloring_order
def emit_edge_coloring_order(n, c, table):
    pieces = []
    append = pieces.append
    for start in range(n - 1):
        start_digits = table[start]
        for finish in range(start + 1, n):
            append(str(select_discriminating_digit(start_digits, table[finish], c)))
    return pieces

# CLAUSE: verify_monochrome_path_limit
def verify_monochrome_path_limit(k, color_count):
    return color_count >= 0 and k >= 1

# CLAUSE: handle_boundary_cases
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    n = int(raw[0])
    k = int(raw[1])
    c = derive_color_bound(n, k)
    if n <= 1:
        print(c)
        print()
        return
    table = encode_vertices_base_k(n, k, c)
    answer = emit_edge_coloring_order(n, c, table)
    print(c)
    print(" ".join(answer))

main()
