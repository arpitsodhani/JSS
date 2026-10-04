# CLAUSE: setup_environment
import sys

def read_int():
    return int(sys.stdin.readline())

def ask_distance(first, second):
    print("? 2", first, second)
    sys.stdout.flush()
    return read_int()

# CLAUSE: solve_logic
class Builder:
    def __init__(self):
        self.ends = [[1, 2]]
        self.at = {1: {0}, 2: {0}}
        self.next_id = 3

    def adjacent_edge(self, edge_id):
        for old_id in range(edge_id):
            if ask_distance(edge_id + 1, old_id + 1) == 0:
                return old_id
        return 0

    def shared_vertex(self, edge_id, base_edge):
        x, y = self.ends[base_edge]
        x_side = self.at[x] - {base_edge}
        if x_side:
            sample = next(iter(x_side))
            return x if ask_distance(edge_id + 1, sample + 1) == 0 else y

        y_side = self.at[y] - {base_edge}
        if y_side:
            sample = next(iter(y_side))
            return y if ask_distance(edge_id + 1, sample + 1) == 0 else x

        return x

    def add_edge(self, edge_id):
        base = self.adjacent_edge(edge_id)
        shared = self.shared_vertex(edge_id, base)
        fresh = self.next_id
        self.next_id += 1
        self.ends.append([shared, fresh])
        self.at[shared].add(edge_id)
        self.at[fresh] = {edge_id}

def solve():
    n = read_int()
    if n == 1:
        print("!")
        sys.stdout.flush()
        return

    m = n - 1
    if m == 1:
        print("!")
        print("1 2")
        sys.stdout.flush()
        return

    builder = Builder()
    for edge_id in range(1, m):
        builder.add_edge(edge_id)

    answer = ["!"]
    for a, b in builder.ends:
        answer.append(f"{a} {b}")
    sys.stdout.write("\n".join(answer) + "\n")
    sys.stdout.flush()

# CLAUSE: finish_program
solve()
