# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve(data):
    if not data:
        return ""

    n, m, h, t = data[0], data[1], data[2], data[3]
    adjacency = [[] for _ in range(n + 1)]
    edges = []

    p = 4
    for _ in range(m):
        x = data[p]
        y = data[p + 1]
        p += 2
        adjacency[x].append(y)
        adjacency[y].append(x)
        edges.append((x, y))

    label = [0] * (n + 1)
    step = 1

    def collect(center, other, need_center, need_other):
        nonlocal step
        if len(adjacency[center]) <= need_center:
            return None
        if len(adjacency[other]) <= need_other:
            return None
        if len(adjacency[center]) + len(adjacency[other]) - 2 < need_center + need_other:
            return None

        step += 2
        left_mark = step
        common_mark = step + 1

        for z in adjacency[center]:
            if z != other:
                label[z] = left_mark

        right_private = []
        common_nodes = []
        for z in adjacency[other]:
            if z == center:
                continue
            if label[z] == left_mark:
                label[z] = common_mark
                common_nodes.append(z)
            else:
                right_private.append(z)

        left_private = []
        for z in adjacency[center]:
            if z != other and label[z] == left_mark:
                left_private.append(z)

        missing_left = max(0, need_center - len(left_private))
        missing_right = max(0, need_other - len(right_private))
        if missing_left + missing_right > len(common_nodes):
            return None

        return left_private[:need_center] + common_nodes[:missing_left], right_private[:need_other] + common_nodes[missing_left:missing_left + missing_right]

    candidates = []
    for a, b in edges:
        if len(adjacency[a]) > h and len(adjacency[b]) > t:
            candidates.append((a, b))
        if len(adjacency[b]) > h and len(adjacency[a]) > t:
            candidates.append((b, a))

    for a, b in candidates:
        found = collect(a, b, h, t)
        if found is None:
            continue
        heads, tails = found
        return "YES\n{} {}\n{}\n{}\n".format(a, b, " ".join(map(str, heads)), " ".join(map(str, tails)))

    return "NO\n"

def main():
    sys.stdout.write(solve(list(map(int, sys.stdin.buffer.read().split()))))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
