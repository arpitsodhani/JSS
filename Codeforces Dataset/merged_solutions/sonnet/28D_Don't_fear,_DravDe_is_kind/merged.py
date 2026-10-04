# Clause setup_environment [Confidence: 0.40]
import sys

def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    values = list(map(int, raw))
    n = values[0]
    trucks = []
    pos = 1
    total_people = 0
    for i in range(1, n + 1):
        v = values[pos]
        c = values[pos + 1]
        l = values[pos + 2]
        r = values[pos + 3]
        pos += 4
        total_people += c
        trucks.append((v, c, l, r, i))


# Clause solve_logic [Confidence: 0.60]
    parent = [-1]
    chosen = [0]
    states_by_people = {0: [(0, 0, 0)]}

    def compact(items):
        items.sort(key=lambda item: (item[0], -item[1]))
        kept = []
        best = -1
        for need, score, node in items:
            if score > best:
                kept.append((need, score, node))
                best = score
        return kept

    for value, count, left_need, right_need, index in trucks:
        keys = sorted(states_by_people.keys(), reverse=True)
        touched = []
        seen = set()
        for people in keys:
            if people < left_need:
                continue
            new_people = people + count
            if new_people > total_people:
                continue
            target = states_by_people.setdefault(new_people, [])
            for need, score, node in states_by_people[people]:
                new_need = max(need, new_people + right_need)
                if new_need <= total_people:
                    parent.append(node)
                    chosen.append(index)
                    new_node = len(parent) - 1
                    target.append((new_need, score + value, new_node))
                    if new_people not in seen:
                        seen.add(new_people)
                        touched.append(new_people)
        for people in touched:
            states_by_people[people] = compact(states_by_people[people])

    best_score = -1
    best_node = 0
    for people, entries in states_by_people.items():
        for need, score, node in entries:
            if need <= people and score > best_score:
                best_score = score
                best_node = node

    answer = []
    while best_node:
        answer.append(chosen[best_node])
        best_node = parent[best_node]
    answer.reverse()


# Clause finish_program [Confidence: 0.80]
    lines = [str(len(sequence))]
    if sequence:
        lines.append(" ".join(str(x) for x in sequence))
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()


