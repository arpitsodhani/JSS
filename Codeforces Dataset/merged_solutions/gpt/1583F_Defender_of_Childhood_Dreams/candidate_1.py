# CLAUSE: derive_color_bound
import sys

def derive_color_bound(n, k):
    if n <= 1:
        return 0
    c = 0
    power = 1
    while power < n:
        c += 1
        power *= k
    return c

# CLAUSE: encode_vertices_base_k
def encode_vertices_base_k(n, k, c):
    encoded = []
    for value in range(n):
        digits = [0] * c
        x = value
        for pos in range(c - 1, -1, -1):
            digits[pos] = x % k
            x //= k
        encoded.append(digits)
    return encoded

# CLAUSE: select_discriminating_digit
def select_discriminating_digit(a, b, c):
    for pos in range(c):
        if a[pos] != b[pos]:
            return pos + 1
    return 1

# CLAUSE: emit_edge_coloring_order
def emit_edge_coloring_order(n, c, digits):
    out = []
    for i in range(n):
        left = digits[i]
        for j in range(i + 1, n):
            out.append(str(select_discriminating_digit(left, digits[j], c)))
    return out

# CLAUSE: verify_monochrome_path_limit
def verify_monochrome_path_limit(k):
    return k - 1

# CLAUSE: handle_boundary_cases
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n, k = map(int, data[:2])
    c = derive_color_bound(n, k)
    if c == 0:
        sys.stdout.write("0\n\n")
        return
    digits = encode_vertices_base_k(n, k, c)
    colors = emit_edge_coloring_order(n, c, digits)
    sys.stdout.write(str(c) + "\n" + " ".join(colors) + "\n")

main()
