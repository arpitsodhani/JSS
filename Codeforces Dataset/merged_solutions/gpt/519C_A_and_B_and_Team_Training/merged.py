# Clause parse_resource_counts [Confidence: 0.60]
import sys

def parse_resource_counts():
    data = list(map(int, sys.stdin.readline().split()))
    n = data[0]
    m = data[1]
    return n, m


# Clause derive_team_upper_bounds [Confidence: 0.40]
def bounds(n, m):
    by_people = (n + m) // 3
    by_experienced = n
    by_newbies = m
    return by_people, by_experienced, by_newbies


# Clause identify_limiting_resource [Confidence: 0.40]
def identify_limiting_resource(limits):
    return min(limits, key=limits.get)


# Clause compute_max_team_count [Confidence: 0.40]
def compute_max_team_count(upper_bounds):
    position = identify_limiting_resource(upper_bounds)
    return upper_bounds[position]


# Clause validate_feasible_distribution [Confidence: 0.40]
def feasible(k, n, m):
    return k <= n and k <= m and 3 * k <= n + m


# Clause emit_answer [Confidence: 0.60]
n, m = read_counts()
answer = solve(n, m)
feasible(answer, n, m)
print(answer)


