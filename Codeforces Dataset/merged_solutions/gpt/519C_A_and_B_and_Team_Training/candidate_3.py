# CLAUSE: parse_resource_counts
import sys

def parse_resource_counts():
    data = list(map(int, sys.stdin.readline().split()))
    n = data[0]
    m = data[1]
    return n, m

# CLAUSE: derive_team_upper_bounds
def derive_team_upper_bounds(n, m):
    total_limit = (n + m) // 3
    member_limits = (n, m)
    return (total_limit,) + member_limits

# CLAUSE: identify_limiting_resource
def identify_limiting_resource(total_limit, experienced_limit, newbie_limit):
    if total_limit <= experienced_limit and total_limit <= newbie_limit:
        return total_limit
    if experienced_limit <= newbie_limit:
        return experienced_limit
    return newbie_limit

# CLAUSE: compute_max_team_count
def compute_max_team_count(n, m):
    total_limit, experienced_limit, newbie_limit = derive_team_upper_bounds(n, m)
    return identify_limiting_resource(total_limit, experienced_limit, newbie_limit)

# CLAUSE: validate_feasible_distribution
def validate_feasible_distribution(k, n, m):
    return (k <= n) and (k <= m) and ((n + m) >= 3 * k)

# CLAUSE: emit_answer
n, m = parse_resource_counts()
result = compute_max_team_count(n, m)
validate_feasible_distribution(result, n, m)
sys.stdout.write(str(result))
