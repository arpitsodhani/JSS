# CLAUSE: parse_resource_counts
import sys

tokens = sys.stdin.read().strip().split()
n = int(tokens[0])
m = int(tokens[1])

# CLAUSE: derive_team_upper_bounds
people_bound = (n + m) // 3
experienced_bound = n
newbie_bound = m
all_bounds = [people_bound, experienced_bound, newbie_bound]

# CLAUSE: identify_limiting_resource
limiting_bound = all_bounds[0]
for candidate_bound in all_bounds[1:]:
    if candidate_bound < limiting_bound:
        limiting_bound = candidate_bound

# CLAUSE: compute_max_team_count
max_team_count = limiting_bound

# CLAUSE: validate_feasible_distribution
valid_distribution_exists = (
    max_team_count <= experienced_bound
    and max_team_count <= newbie_bound
    and max_team_count * 3 <= n + m
)

# CLAUSE: emit_answer
print(max_team_count)
