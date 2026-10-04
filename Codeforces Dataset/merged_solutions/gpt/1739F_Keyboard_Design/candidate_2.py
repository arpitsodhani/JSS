import sys

ALPHA = "abcdefghijkl"
N = 12

# CLAUSE: compress_word_edge_masks
def compress_word_edge_masks(records):
    idx = [[-1] * N for _ in range(N)]
    q = 0
    for a in range(N):
        for b in range(a + 1, N):
            idx[a][b] = idx[b][a] = q
            q += 1
    masks = []
    for val, word in records:
        need = 0
        last = ord(word[0]) - 97
        for ch in word[1:]:
            cur = ord(ch) - 97
            need |= 1 << idx[last][cur]
            last = cur
        masks.append((need, val))
    return masks, idx

# CLAUSE: aggregate_mask_rewards
def aggregate_mask_rewards(raw):
    total = {}
    for mask, val in raw:
        total[mask] = total.setdefault(mask, 0) + val
    return total

# CLAUSE: enumerate_connected_layout_masks
def enumerate_connected_layout_masks(idx):
    table = []
    for a in range(N):
        row = []
        for b in range(N):
            row.append(0 if a == b else 1 << idx[a][b])
        table.append(row)
    return table

# CLAUSE: compute_subset_rewards
def compute_subset_rewards(total):
    keys = list(total.keys())
    vals = [total[k] for k in keys]
    memo = {}
    def calc(edge_mask):
        got = memo.get(edge_mask)
        if got is not None:
            return got
        s = 0
        for i, k in enumerate(keys):
            if k | edge_mask == edge_mask:
                s += vals[i]
        memo[edge_mask] = s
        return s
    return calc

# CLAUSE: extend_path_dp_states
def extend_path_dp_states(edge_bit, score):
    allmask = (1 << N) - 1
    dp = {}
    parent = {}
    for x in range(N):
        dp[(1 << x, x)] = (score(0), 0)
    for used in range(1 << N):
        entries = [(last, data) for (m, last), data in dp.items() if m == used]
        for last, data in entries:
            old_score, old_edges = data
            unused = allmask ^ used
            while unused:
                take = unused & -unused
                y = take.bit_length() - 1
                nm = used | take
                ne = old_edges | edge_bit[last][y]
                ns = score(ne)
                key = (nm, y)
                if key not in dp or ns > dp[key][0]:
                    dp[key] = (ns, ne)
                    parent[key] = (used, last)
                unused ^= take
    return dp, parent

# CLAUSE: select_best_hamiltonian_path
def select_best_hamiltonian_path(dp):
    full = (1 << N) - 1
    choice = max(range(N), key=lambda x: dp.get((full, x), (-1, 0))[0])
    return full, choice

# CLAUSE: reconstruct_keyboard_order
def reconstruct_keyboard_order(chosen, parent):
    path = []
    cur = chosen
    while True:
        path.append(ALPHA[cur[1]])
        if cur not in parent:
            break
        cur = parent[cur]
    path.reverse()
    return "".join(path)

def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    records = []
    pos = 1
    for _ in range(n):
        records.append((int(tokens[pos]), tokens[pos + 1].decode()))
        pos += 2
    compressed, idx = compress_word_edge_masks(records)
    totals = aggregate_mask_rewards(compressed)
    edge_bit = enumerate_connected_layout_masks(idx)
    score = compute_subset_rewards(totals)
    dp, parent = extend_path_dp_states(edge_bit, score)
    print(reconstruct_keyboard_order(select_best_hamiltonian_path(dp), parent))

main()
