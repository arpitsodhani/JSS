# CLAUSE: derive_color_bound
import sys

def derive_color_bound(n, k):
    if n == 0 or n == 1:
        return 0
    colors = 0
    limit = 1
    while True:
        if limit >= n:
            return colors
        limit *= k
        colors += 1

# CLAUSE: encode_vertices_base_k
def encode_vertices_base_k(n, k, c):
    encoded = []
    for value in range(n):
        rev = []
        x = value
        for _ in range(c):
            rev.append(x % k)
            x //= k
        encoded.append(rev)
    return encoded

# CLAUSE: select_discriminating_digit
def select_discriminating_digit(left_rev, right_rev, c):
    for rev_pos in range(c - 1, -1, -1):
        if left_rev[rev_pos] != right_rev[rev_pos]:
            return c - rev_pos
    return 1

# CLAUSE: emit_edge_coloring_order
def emit_edge_coloring_order(n, c, encoded):
    ans = []
    append = ans.append
    for i, left in enumerate(encoded):
        for j in range(i + 1, n):
            append(str(select_discriminating_digit(left, encoded[j], c)))
    return ans

# CLAUSE: verify_monochrome_path_limit
def verify_monochrome_path_limit(k, c):
    return (k - 1) * max(1, c)

# CLAUSE: handle_boundary_cases
def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    k = int(tokens[1])
    c = derive_color_bound(n, k)
    encoded = encode_vertices_base_k(n, k, c)
    colors = emit_edge_coloring_order(n, c, encoded)
    sys.stdout.write(str(c))
    sys.stdout.write("\n")
    sys.stdout.write(" ".join(colors))
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()
