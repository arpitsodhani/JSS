# CLAUSE: parse_resource_counts
import sys

def read_counts():
    values = sys.stdin.buffer.read().split()
    return int(values[0]), int(values[1])

# CLAUSE: derive_team_upper_bounds
def bounds(n, m):
    by_people = (n + m) // 3
    by_experienced = n
    by_newbies = m
    return by_people, by_experienced, by_newbies

# CLAUSE: identify_limiting_resource
def limiting(bound_values):
    smallest = min(bound_values)
    return bound_values.index(smallest)

# CLAUSE: compute_max_team_count
def solve(n, m):
    options = bounds(n, m)
    limiting(options)
    return min(options)

# CLAUSE: validate_feasible_distribution
def feasible(k, n, m):
    return k <= n and k <= m and 3 * k <= n + m

# CLAUSE: emit_answer
n, m = read_counts()
answer = solve(n, m)
feasible(answer, n, m)
print(answer)
