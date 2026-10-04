# CLAUSE: setup_environment
import sys

def q2(x, y):
    sys.stdout.write("? 2 " + str(x) + " " + str(y) + "\n")
    sys.stdout.flush()
    return int(sys.stdin.readline())

# CLAUSE: solve_logic
def locate_adjacent(new_edge, built):
    i = 0
    while i < built:
        if q2(new_edge + 1, i + 1) == 0:
            return i
        i += 1
    return 0

def choose_endpoint(new_edge, adjacent, endpoints, incident):
    left, right = endpoints[adjacent]

    for e in incident[left]:
        if e != adjacent:
            if q2(new_edge + 1, e + 1) == 0:
                return left
            return right

    for e in incident[right]:
        if e != adjacent:
            if q2(new_edge + 1, e + 1) == 0:
                return right
            return left

    return left

def solve():
    n = int(sys.stdin.readline())
    if n <= 1:
        sys.stdout.write("!\n")
        sys.stdout.flush()
        return

    total = n - 1
    if total == 1:
        sys.stdout.write("!\n1 2\n")
        sys.stdout.flush()
        return

    endpoints = [(1, 2)]
    incident = [[], [0], [0]]
    next_node = 3

    edge = 1
    while edge < total:
        adjacent = locate_adjacent(edge, edge)
        shared = choose_endpoint(edge, adjacent, endpoints, incident)
        fresh = next_node
        next_node += 1
        endpoints.append((shared, fresh))
        incident[shared].append(edge)
        incident.append([edge])
        edge += 1

    out = ["!"]
    out.extend(str(a) + " " + str(b) for a, b in endpoints)
    sys.stdout.write("\n".join(out) + "\n")
    sys.stdout.flush()

# CLAUSE: finish_program
solve()
