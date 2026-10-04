import sys

# CLAUSE: parse_known_flow_edges
numbers = [int(x) for x in sys.stdin.buffer.read().split()]
if len(numbers) < 2:
    sys.exit()
n, m = numbers[:2]
known = []
pos = 2
idx = 1
while idx <= m:
    known.append((idx, numbers[pos], numbers[pos + 1], numbers[pos + 2], numbers[pos + 3]))
    pos += 4
    idx += 1

# CLAUSE: assign_edge_potentials
known = [(idx, a, b, c * d) for idx, a, b, c, d in known]

# CLAUSE: merge_weighted_components
parent = list(range(n + 1))
count = [1] * (n + 1)
potential_to_parent = [0] * (n + 1)
minimum = [0] * (n + 1)
maximum = [0] * (n + 1)
minimum_count = [1] * (n + 1)
maximum_count = [1] * (n + 1)
contains_start = [False] * (n + 1)
contains_finish = [False] * (n + 1)
contains_start[1] = True
contains_finish[n] = True

def locate(x):
    total = 0
    y = x
    while parent[y] != y:
        total += potential_to_parent[y]
        y = parent[y]
    r = y
    y = x
    done = 0
    while parent[y] != y:
        nxt = parent[y]
        step = potential_to_parent[y]
        parent[y] = r
        potential_to_parent[y] = total - done
        done += step
        y = nxt
    return r, total

def refresh(a, b, move):
    low_b = minimum[b] + move
    high_b = maximum[b] + move
    if low_b <= minimum[a]:
        if low_b < minimum[a]:
            minimum[a] = low_b
            minimum_count[a] = 0
        minimum_count[a] += minimum_count[b]
    if high_b >= maximum[a]:
        if high_b > maximum[a]:
            maximum[a] = high_b
            maximum_count[a] = 0
        maximum_count[a] += maximum_count[b]
    count[a] += count[b]
    contains_start[a] = contains_start[a] or contains_start[b]
    contains_finish[a] = contains_finish[a] or contains_finish[b]

# CLAUSE: detect_cycle_inconsistency
def constrain(a, b, diff):
    ra, pa = locate(a)
    rb, pb = locate(b)
    if ra == rb:
        return pb - pa == diff, ra
    if count[ra] > count[rb]:
        move = diff + pa - pb
        parent[rb] = ra
        potential_to_parent[rb] = move
        refresh(ra, rb, move)
        return True, ra
    move = pb - diff - pa
    parent[ra] = rb
    potential_to_parent[ra] = move
    refresh(rb, ra, move)
    return True, rb

# CLAUSE: enforce_terminal_ordering
def valid_terminal(component):
    if contains_start[component]:
        r, s_value = locate(1)
        if minimum[r] != s_value or minimum_count[r] > 1:
            return False
    if contains_finish[component]:
        r, t_value = locate(n)
        if maximum[r] != t_value or maximum_count[r] > 1:
            return False
    return True

bad_edge = None
for idx, a, b, diff in known:
    possible, component = constrain(a, b, diff)
    if not possible:
        bad_edge = idx
        break
    component = locate(a)[0]
    if not valid_terminal(component):
        bad_edge = idx
        break

# CLAUSE: derive_efficiency_state
efficiency = None
if bad_edge is None:
    r1, q1 = locate(1)
    r2, q2 = locate(n)
    if r1 == r2:
        efficiency = q2 - q1

# CLAUSE: emit_certified_result
if bad_edge is not None:
    print("BAD", bad_edge)
elif efficiency is None:
    print("UNKNOWN")
else:
    print(efficiency)
