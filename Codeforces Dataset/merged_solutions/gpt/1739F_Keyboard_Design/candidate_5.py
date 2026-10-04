import sys

L = 12
S = "abcdefghijkl"

# CLAUSE: compress_word_edge_masks
def compress_word_edge_masks(words):
    ids = [[0] * L for _ in range(L)]
    z = 0
    for i in range(L):
        for j in range(i + 1, L):
            ids[i][j] = ids[j][i] = z
            z += 1
    result = []
    for freq, word in words:
        mask = 0
        before = None
        for ch in word:
            now = ord(ch) - 97
            if before is not None:
                mask |= 1 << ids[before][now]
            before = now
        result.append((mask, freq))
    return result, ids

# CLAUSE: aggregate_mask_rewards
def aggregate_mask_rewards(result):
    acc = {}
    for mask, freq in result:
        acc[mask] = acc.get(mask, 0) + freq
    masks = []
    freqs = []
    for k, v in acc.items():
        masks.append(k)
        freqs.append(v)
    return masks, freqs

# CLAUSE: enumerate_connected_layout_masks
def enumerate_connected_layout_masks(ids):
    bits = [[0] * L for _ in range(L)]
    for i in range(L):
        for j in range(L):
            if i != j:
                bits[i][j] = 1 << ids[i][j]
    return bits

# CLAUSE: compute_subset_rewards
def compute_subset_rewards(grouped):
    masks, freqs = grouped
    memory = {}
    def f(edge_mask):
        old = memory.get(edge_mask)
        if old is not None:
            return old
        total = 0
        for i in range(len(masks)):
            if masks[i] & edge_mask == masks[i]:
                total += freqs[i]
        memory[edge_mask] = total
        return total
    return f

# CLAUSE: extend_path_dp_states
def extend_path_dp_states(bits, f):
    mx = 1 << L
    score = [[-1] * L for _ in range(mx)]
    edge = [[0] * L for _ in range(mx)]
    par_last = [[-1] * L for _ in range(mx)]
    for i in range(L):
        score[1 << i][i] = f(0)
    for mask in range(mx):
        for last in range(L):
            if score[mask][last] == -1:
                continue
            available = (mx - 1) ^ mask
            while available:
                b = available & -available
                nxt = b.bit_length() - 1
                nm = mask | b
                ne = edge[mask][last] | bits[last][nxt]
                ns = f(ne)
                if ns > score[nm][nxt]:
                    score[nm][nxt] = ns
                    edge[nm][nxt] = ne
                    par_last[nm][nxt] = last
                available -= b
    return score, par_last

# CLAUSE: select_best_hamiltonian_path
def select_best_hamiltonian_path(score):
    full = (1 << L) - 1
    best = 0
    for i in range(L):
        if score[full][i] > score[full][best]:
            best = i
    return full, best

# CLAUSE: reconstruct_keyboard_order
def reconstruct_keyboard_order(state, par_last):
    mask, last = state
    seq = []
    while last != -1:
        seq.append(S[last])
        old = last
        last = par_last[mask][last]
        mask ^= 1 << old
    return "".join(seq[::-1])

def main():
    raw = sys.stdin.read().split()
    if not raw:
        return
    n = int(raw[0])
    words = []
    i = 1
    for _ in range(n):
        words.append((int(raw[i]), raw[i + 1]))
        i += 2
    compressed, ids = compress_word_edge_masks(words)
    grouped = aggregate_mask_rewards(compressed)
    bits = enumerate_connected_layout_masks(ids)
    f = compute_subset_rewards(grouped)
    score, par_last = extend_path_dp_states(bits, f)
    print(reconstruct_keyboard_order(select_best_hamiltonian_path(score), par_last))

main()
