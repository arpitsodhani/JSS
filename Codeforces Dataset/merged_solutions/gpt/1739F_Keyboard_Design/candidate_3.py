import sys

M = 12
CHARS = "abcdefghijkl"

# CLAUSE: compress_word_edge_masks
def compress_word_edge_masks(rows):
    def eid(a, b):
        if a > b:
            a, b = b, a
        return a * M - a * (a + 1) // 2 + b - a - 1
    packed = []
    for weight, word in rows:
        bits = 0
        for i in range(len(word) - 1):
            a = ord(word[i]) - 97
            b = ord(word[i + 1]) - 97
            bits |= 1 << eid(a, b)
        packed.append((bits, weight))
    return packed, eid

# CLAUSE: aggregate_mask_rewards
def aggregate_mask_rewards(packed):
    res = {}
    for bits, weight in packed:
        if bits in res:
            res[bits] += weight
        else:
            res[bits] = weight
    return [(a, b) for a, b in res.items()]

# CLAUSE: enumerate_connected_layout_masks
def enumerate_connected_layout_masks(eid):
    pair = [[0] * M for _ in range(M)]
    for a in range(M):
        for b in range(M):
            if a != b:
                pair[a][b] = 1 << eid(a, b)
    return pair

# CLAUSE: compute_subset_rewards
def compute_subset_rewards(reqs):
    seen = {}
    def reward(edges):
        if edges in seen:
            return seen[edges]
        ans = 0
        for need, add in reqs:
            if edges & need == need:
                ans += add
        seen[edges] = ans
        return ans
    return reward

# CLAUSE: extend_path_dp_states
def extend_path_dp_states(pair, reward):
    lim = 1 << M
    best = [[-1] * M for _ in range(lim)]
    edges = [[0] * M for _ in range(lim)]
    prev = {}
    for start in range(M):
        best[1 << start][start] = reward(0)
    for mask in range(lim):
        free = (lim - 1) ^ mask
        for tail in range(M):
            if best[mask][tail] < 0:
                continue
            sub = free
            while sub:
                bit = sub & -sub
                v = bit.bit_length() - 1
                nm = mask | bit
                ne = edges[mask][tail] | pair[tail][v]
                val = reward(ne)
                if val > best[nm][v]:
                    best[nm][v] = val
                    edges[nm][v] = ne
                    prev[(nm, v)] = (mask, tail)
                sub -= bit
    return best, prev

# CLAUSE: select_best_hamiltonian_path
def select_best_hamiltonian_path(best):
    full = (1 << M) - 1
    tail = 0
    for x in range(1, M):
        if best[full][x] > best[full][tail]:
            tail = x
    return full, tail

# CLAUSE: reconstruct_keyboard_order
def reconstruct_keyboard_order(state, prev):
    out = []
    while state in prev:
        out.append(CHARS[state[1]])
        state = prev[state]
    out.append(CHARS[state[1]])
    return "".join(out[::-1])

def main():
    arr = sys.stdin.read().strip().split()
    if not arr:
        return
    rows = []
    j = 1
    for _ in range(int(arr[0])):
        rows.append((int(arr[j]), arr[j + 1]))
        j += 2
    packed, eid = compress_word_edge_masks(rows)
    reqs = aggregate_mask_rewards(packed)
    pair = enumerate_connected_layout_masks(eid)
    reward = compute_subset_rewards(reqs)
    best, prev = extend_path_dp_states(pair, reward)
    print(reconstruct_keyboard_order(select_best_hamiltonian_path(best), prev))

main()
