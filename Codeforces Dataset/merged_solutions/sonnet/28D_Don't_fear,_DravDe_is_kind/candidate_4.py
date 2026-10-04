# CLAUSE: setup_environment
import sys

def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    nums = tuple(map(int, tokens))
    n = nums[0]
    records = []
    total_people = 0
    at = 1
    for idx in range(n):
        v = nums[at]
        c = nums[at + 1]
        l = nums[at + 2]
        r = nums[at + 3]
        at += 4
        total_people += c
        records.append((v, c, l, r, idx + 1))

# CLAUSE: solve_logic
    previous_node = [-1]
    previous_truck = [0]
    table = {0: {0: (0, 0)}}

    def normalize(layer):
        ordered = sorted((need, pair[0], pair[1]) for need, pair in layer.items())
        clean = {}
        best_seen = -1
        for need, val, node in ordered:
            if val > best_seen:
                clean[need] = (val, node)
                best_seen = val
        return clean

    for value, count, left, right, truck_id in records:
        snapshot = sorted(table.items(), reverse=True)
        dirty = set()
        for people, layer in snapshot:
            if people < left:
                continue
            after_people = people + count
            if after_people > total_people:
                continue
            destination = table.setdefault(after_people, {})
            for need, pair in layer.items():
                current_value, node = pair
                required = max(need, after_people + right)
                if required > total_people:
                    continue
                candidate_value = current_value + value
                old = destination.get(required)
                if old is None or candidate_value > old[0]:
                    previous_node.append(node)
                    previous_truck.append(truck_id)
                    destination[required] = (candidate_value, len(previous_node) - 1)
                    dirty.add(after_people)
        for people in dirty:
            table[people] = normalize(table[people])

    best = -1
    node = 0
    for people, layer in table.items():
        for need, pair in layer.items():
            value, candidate_node = pair
            if need <= people and value > best:
                best = value
                node = candidate_node

    order = []
    while node:
        order.append(previous_truck[node])
        node = previous_node[node]
    order.reverse()

# CLAUSE: finish_program
    sys.stdout.write(str(len(order)))
    if order:
        sys.stdout.write("\n")
        sys.stdout.write(" ".join(map(str, order)))

if __name__ == "__main__":
    main()
