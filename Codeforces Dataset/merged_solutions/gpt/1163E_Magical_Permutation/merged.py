# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:1 + n]
    a.sort()

    if not a:
        sys.stdout.write("0\n0\n")
        return

    max_bit = max(a).bit_length()
    reduced = [0] * max_bit
    chosen_at_pivot = [0] * max_bit
    chosen_order = []
    rank = 0
    best_x = 0
    best_basis = []
    ptr = 0

    for x in range(1, max_bit + 1):
        limit = 1 << x
        while ptr < n and a[ptr] < limit:
            val = a[ptr]
            cur = val
            for b in range(max_bit - 1, -1, -1):
                if not ((cur >> b) & 1):
                    continue
                if reduced[b]:
                    cur ^= reduced[b]
                else:
                    reduced[b] = cur
                    chosen_at_pivot[b] = val
                    chosen_order.append(val)
                    rank += 1
                    break
            ptr += 1

        if rank == x:
            best_x = x
            best_basis = chosen_order[:]

    out = sys.stdout
    out.write(str(best_x) + "\n")

    if best_x == 0:
        out.write("0\n")
        return

    val = 0
    out.write("0")
    chunk = []
    size = 1 << best_x

    for i in range(1, size):
        bit = (i & -i).bit_length() - 1
        val ^= best_basis[bit]
        chunk.append(str(val))
        if len(chunk) >= 8192:
            out.write(" " + " ".join(chunk))
            chunk.clear()

    if chunk:
        out.write(" " + " ".join(chunk))
    out.write("\n")

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
