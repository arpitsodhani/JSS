# CLAUSE: parse_resource_counts
def parse_resource_counts():
    n_text, m_text = input().split()
    return int(n_text), int(m_text)

# CLAUSE: derive_team_upper_bounds
def derive_team_upper_bounds(experienced, newbies):
    limits = {
        "total": (experienced + newbies) // 3,
        "experienced": experienced,
        "newbies": newbies,
    }
    return limits

# CLAUSE: identify_limiting_resource
def identify_limiting_resource(limits):
    return min(limits, key=limits.get)

# CLAUSE: compute_max_team_count
def compute_max_team_count(limits):
    return limits[identify_limiting_resource(limits)]

# CLAUSE: validate_feasible_distribution
def validate_feasible_distribution(teams, experienced, newbies):
    if teams > experienced or teams > newbies or teams * 3 > experienced + newbies:
        raise RuntimeError

# CLAUSE: emit_answer
n, m = parse_resource_counts()
upper_bounds = derive_team_upper_bounds(n, m)
k = compute_max_team_count(upper_bounds)
validate_feasible_distribution(k, n, m)
print(k)
