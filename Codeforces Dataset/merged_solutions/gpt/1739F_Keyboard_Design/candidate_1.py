import sys

K = 12
LETTERS = "abcdefghijkl"

# CLAUSE: compress_word_edge_masks
def compress_word_edge_masks(items):
    edge_id = {}
    p = 0
    for i in range(K):
        for j in range(i + 1, K):
            edge_id[(i, j)] = p
            p += 1
    out = []
    for c, s in items:
        m = 0
        for a, b in zip(s, s[1:]):
            x = ord(a) - 97
            y = ord(b) - 97
            if x > y:
                x, y = y, x
            m |= 1 << edge_id[(x, y)]
        out.append((m, c))
    return out, edge_id

# CLAUSE: aggregate_mask_rewards
def aggregate_mask_rewards(pairs):
    mp = {}
    for m, c in pairs:
        mp[m] = mp.get(m, 0) + c
    return list(mp.items())

# CLAUSE: enumerate_connected_layout_masks
def enumerate_connected_layout_masks(edge_id):
    add = [[0] * K for _ in range(K)]
    for i in range(K):
        for j in range(K):
            if i != j:
                a, b = (i, j) if i < j else (j, i)
                add[i][j] = 1 << edge_id[(a, b)]
    return add

# CLAUSE: compute_subset_rewards
def compute_subset_rewards(groups):
    cache = {}
    def value(mask):
        if mask not in cache:
            total = 0
            for need, score in groups:
                if need & ~mask == 0:
                    total += score
            cache[mask] = total
        return cache[mask]
    return value

# CLAUSE: extend_path_dp_states
def extend_path_dp_states(add_edge, reward_of):
    size = 1 << K
    dp = [[None] * K for _ in range(size)]
    parent = {}
    for i in range(K):
        dp[1 << i][i] = (reward_of(0), 0)
    for mask in range(size):
        for last in range(K):
            cur = dp[mask][last]
            if cur is None:
                continue
            _, em = cur
            left = ((1 << K) - 1) ^ mask
            while left:
                bit = left & -left
                nxt = bit.bit_length() - 1
                nm = mask | bit
                ne = em | add_edge[last][nxt]
                ns = reward_of(ne)
                old = dp[nm][nxt]
                if old is None or ns > old[0]:
                    dp[nm][nxt] = (ns, ne)
                    parent[(nm, nxt)] = (mask, last)
                left -= bit
    return dp, parent

# CLAUSE: select_best_hamiltonian_path
def select_best_hamiltonian_path(dp):
    full = (1 << K) - 1
    best_last = 0
    best_score = -1
    for i in range(K):
        if dp[full][i] is not None and dp[full][i][0] > best_score:
            best_score = dp[full][i][0]
            best_last = i
    return full, best_last

# CLAUSE: reconstruct_keyboard_order
def reconstruct_keyboard_order(state, parent):
    mask, last = state
    ans = []
    while True:
        ans.append(LETTERS[last])
        key = (mask, last)
        if key not in parent:
            break
        mask, last = parent[key]
    return "".join(reversed(ans))

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    items = []
    at = 1
    for _ in range(n):
        items.append((int(data[at]), data[at + 1]))
        at += 2
    compressed, edge_id = compress_word_edge_masks(items)
    groups = aggregate_mask_rewards(compressed)
    add_edge = enumerate_connected_layout_masks(edge_id)
    reward_of = compute_subset_rewards(groups)
    dp, parent = extend_path_dp_states(add_edge, reward_of)
    state = select_best_hamiltonian_path(dp)
    print(reconstruct_keyboard_order(state, parent))

main()
