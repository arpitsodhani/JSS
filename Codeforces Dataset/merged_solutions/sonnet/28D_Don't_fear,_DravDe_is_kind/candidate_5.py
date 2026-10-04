# CLAUSE: setup_environment
import sys

def reduce_states(states):
    states.sort(key=lambda state: (state[0], -state[1]))
    answer = []
    maximum = -1
    for state in states:
        if state[1] > maximum:
            answer.append(state)
            maximum = state[1]
    return answer

def main():
    content = sys.stdin.buffer.read().split()
    if not content:
        return
    data = list(map(int, content))
    n = data[0]
    trucks = []
    total = 0
    offset = 1
    truck_id = 1
    while truck_id <= n:
        value = data[offset]
        count = data[offset + 1]
        before = data[offset + 2]
        after = data[offset + 3]
        offset += 4
        total += count
        trucks.append({"id": truck_id, "v": value, "c": count, "l": before, "r": after})
        truck_id += 1

# CLAUSE: solve_logic
    parents = [-1]
    labels = [0]
    dp = {0: [(0, 0, 0)]}

    for truck in trucks:
        additions = {}
        for people, states in list(dp.items()):
            if people >= truck["l"]:
                new_people = people + truck["c"]
                if new_people <= total:
                    for needed, score, node in states:
                        required = max(needed, new_people + truck["r"])
                        if required <= total:
                            parents.append(node)
                            labels.append(truck["id"])
                            new_node = len(parents) - 1
                            additions.setdefault(new_people, []).append((required, score + truck["v"], new_node))
        for people, states in additions.items():
            if people in dp:
                dp[people].extend(states)
            else:
                dp[people] = states
            dp[people] = reduce_states(dp[people])

    best_value = -1
    cursor = 0
    for people in dp:
        feasible = dp[people]
        for needed, score, node in feasible:
            if needed <= people and score > best_value:
                best_value = score
                cursor = node

    sequence = []
    while cursor != 0:
        sequence.append(labels[cursor])
        cursor = parents[cursor]
    sequence = sequence[::-1]

# CLAUSE: finish_program
    lines = [str(len(sequence))]
    if sequence:
        lines.append(" ".join(str(x) for x in sequence))
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
