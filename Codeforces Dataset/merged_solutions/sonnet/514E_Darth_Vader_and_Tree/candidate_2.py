# CLAUSE: setup_environment
import sys

MOD = 10 ** 9 + 7

def mat_mul(left, right):
    size = len(left)
    out = [[0] * size for _ in range(size)]
    for i, row_left in enumerate(left):
        out_row = out[i]
        for k, val in enumerate(row_left):
            if val:
                row_right = right[k]
                for j in range(size):
                    out_row[j] = (out_row[j] + val * row_right[j]) % MOD
    return out

def mat_vec(mat, vec):
    size = len(vec)
    out = [0] * size
    for i in range(size):
        total = 0
        row = mat[i]
        for j in range(size):
            total += row[j] * vec[j]
        out[i] = total % MOD
    return out

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, x = data[0], data[1]
    distances = data[2:2 + n]
    longest = max(distances)
    ways = [0] * (longest + 1)
    for d in distances:
        ways[d] += 1

    size = longest + 1
    trans = [[0] * size for _ in range(size)]
    for d in range(1, longest + 1):
        trans[0][d - 1] = ways[d] % MOD
    for i in range(1, longest):
        trans[i][i - 1] = 1
    for j in range(longest):
        trans[longest][j] = trans[0][j]
    trans[longest][longest] = 1

    state = [0] * size
    state[0] = 1
    state[longest] = 1

    while x:
        if x & 1:
            state = mat_vec(trans, state)
        trans = mat_mul(trans, trans)
        x >>= 1

    sys.stdout.write(str(state[longest] % MOD))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
