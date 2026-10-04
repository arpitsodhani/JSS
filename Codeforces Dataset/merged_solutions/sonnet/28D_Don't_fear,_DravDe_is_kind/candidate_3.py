# CLAUSE: setup_environment
import sys

def prune_layer(layer):
    layer.sort(key=lambda x: (x[0], -x[1]))
    result = []
    top_value = -1
    for required, worth, node in layer:
        if worth > top_value:
            result.append((required, worth, node))
            top_value = worth
    return result

def main():
    data = [int(x) for x in sys.stdin.buffer.read().split()]
    if not data:
        return
    n = data[0]
    items = []
    total = 0
    p = 1
    for number in range(1, n + 1):
        value, people, before, after = data[p], data[p + 1], data[p + 2], data[p + 3]
        p += 4
        total += people
        items.append((number, value, people, before, after))

# CLAUSE: solve_logic
    layers = [[] for _ in range(total + 1)]
    layers[0].append((0, 0, 0))
    previous = [-1]
    truck_at = [0]
    active = [0]
    active_flag = [False] * (total + 1)
    active_flag[0] = True

    for number, value, people, before, after in items:
        current_active = sorted(active, reverse=True)
        changed = []
        changed_flag = [False] * (total + 1)
        for already in current_active:
            if already < before:
                continue
            new_people = already + people
            if new_people > total:
                continue
            for required, worth, node in layers[already]:
                needed_total = required
                tail_requirement = new_people + after
                if tail_requirement > needed_total:
                    needed_total = tail_requirement
                if needed_total <= total:
                    previous.append(node)
                    truck_at.append(number)
                    new_node = len(previous) - 1
                    layers[new_people].append((needed_total, worth + value, new_node))
                    if not active_flag[new_people]:
                        active_flag[new_people] = True
                        active.append(new_people)
                    if not changed_flag[new_people]:
                        changed_flag[new_people] = True
                        changed.append(new_people)
        for people_count in changed:
            layers[people_count] = prune_layer(layers[people_count])

    best_value = -1
    end_node = 0
    for people_count in active:
        for required, worth, node in layers[people_count]:
            if required <= people_count and worth > best_value:
                best_value = worth
                end_node = node

    picked = []
    while end_node != 0:
        picked.append(truck_at[end_node])
        end_node = previous[end_node]
    picked.reverse()

# CLAUSE: finish_program
    result = [str(len(picked))]
    if picked:
        result.append(" ".join(str(x) for x in picked))
    print("\n".join(result))

if __name__ == "__main__":
    main()
