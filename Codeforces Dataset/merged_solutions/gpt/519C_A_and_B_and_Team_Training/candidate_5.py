# CLAUSE: parse_resource_counts
import sys

def parse_resource_counts():
    raw = sys.stdin.buffer.readline()
    experienced, newbies = (int(part) for part in raw.split())
    return experienced, newbies

# CLAUSE: derive_team_upper_bounds
def derive_team_upper_bounds(pair):
    experienced, newbies = pair
    return [
        (experienced + newbies) // 3,
        experienced,
        newbies,
    ]

# CLAUSE: identify_limiting_resource
def identify_limiting_resource(upper_bounds):
    lowest_position = 0
    for position, value in enumerate(upper_bounds):
        if value < upper_bounds[lowest_position]:
            lowest_position = position
    return lowest_position

# CLAUSE: compute_max_team_count
def compute_max_team_count(upper_bounds):
    position = identify_limiting_resource(upper_bounds)
    return upper_bounds[position]

# CLAUSE: validate_feasible_distribution
def validate_feasible_distribution(team_count, pair):
    experienced, newbies = pair
    checks = (team_count <= experienced, team_count <= newbies, 3 * team_count <= experienced + newbies)
    return all(checks)

# CLAUSE: emit_answer
counts = parse_resource_counts()
limits = derive_team_upper_bounds(counts)
teams = compute_max_team_count(limits)
validate_feasible_distribution(teams, counts)
sys.stdout.write(f"{teams}\n")
