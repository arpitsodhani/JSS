import sys

A = 12
ABC = "abcdefghijkl"

# CLAUSE: compress_word_edge_masks
def compress_word_edge_masks(data):
    number = {}
    cur = 0
    for r in range(A):
        for c in range(r + 1, A):
            number[r, c] = cur
            number[c, r] = cur
            cur += 1
    ans = []
    for cost, s in data:
        mask = 0
        codes = [ord(x) - 97 for x in s]
        for u, v in zip(codes, codes[1:]):
            mask |= 1 << number[u, v]
        ans.append((mask, cost))
    return ans, number

# CLAUSE: aggregate_mask_rewards
def aggregate_mask_rewards(ans):
    d = {}
    for mask, cost in ans:
        d[mask] = d.get(mask, 0) + cost
    return d

# CLAUSE: enumerate_connected_layout_masks
def enumerate_connected_layout_masks(number):
    made = [[0 for _ in range(A)] for _ in range(A)]
    for u in range(A):
        for v in range(A):
            if u != v:
                made[u][v] = 1 << number[u, v]
    return made

# CLAUSE: compute_subset_rewards
def compute_subset_rewards(d):
    entries = tuple(d.items())
    cache = {}
    def get(mask):
        try:
            return cache[mask]
        except KeyError:
            s = 0
            for need, cost in entries:
                if not need & ~mask:
                    s += cost
            cache[mask] = s
            return s
    return get

# CLAUSE: extend_path_dp_states
def extend_path_dp_states(made, get):
    full = (1 << A) - 1
    layer = {(1 << i, i): (get(0), 0) for i in range(A)}
    parent = {}
    for _ in range(1, A):
        nxt_layer = {}
        for (mask, end), (_, emask) in layer.items():
            rest = full ^ mask
            while rest:
                bit = rest & -rest
                v = bit.bit_length() - 1
                nm = mask | bit
                ne = emask | made[end][v]
                val = get(ne)
                key = (nm, v)
                if key not in nxt_layer or val > nxt_layer[key][0]:
                    nxt_layer[key] = (val, ne)
                    parent[key] = (mask, end)
                rest ^= bit
        layer = nxt_layer
    return layer, parent

# CLAUSE: select_best_hamiltonian_path
def select_best_hamiltonian_path(layer):
    return max(layer, key=lambda k: layer[k][0])

# CLAUSE: reconstruct_keyboard_order
def reconstruct_keyboard_order(state, parent):
    seq = []
    while True:
        seq.append(ABC[state[1]])
        if state not in parent:
            break
        state = parent[state]
    return "".join(reversed(seq))

def main():
    t = sys.stdin.buffer.read().split()
    if not t:
        return
    n = int(t[0])
    data = []
    k = 1
    for _ in range(n):
        data.append((int(t[k]), t[k + 1].decode()))
        k += 2
    compressed, number = compress_word_edge_masks(data)
    grouped = aggregate_mask_rewards(compressed)
    made = enumerate_connected_layout_masks(number)
    get = compute_subset_rewards(grouped)
    layer, parent = extend_path_dp_states(made, get)
    print(reconstruct_keyboard_order(select_best_hamiltonian_path(layer), parent))

main()
