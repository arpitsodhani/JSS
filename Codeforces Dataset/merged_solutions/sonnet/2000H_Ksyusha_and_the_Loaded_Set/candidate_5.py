# CLAUSE: setup_environment
import sys
from heapq import heappush, heappop

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    cursor = 0
    case_count = int(raw[cursor])
    cursor += 1
    lines = []
    infinite = 10 ** 30

    for _ in range(case_count):
        n = int(raw[cursor])
        m = int(raw[cursor + 1])
        cursor += 2

        initial = []
        candidates = [0]

        for _ in range(n):
            value = int(raw[cursor])
            cursor += 1
            initial.append(value)
            candidates.append(value)

        changes = []
        for _ in range(m):
            operation = raw[cursor]
            value = int(raw[cursor + 1])
            cursor += 2
            changes.append((operation, value))
            if operation in (b'+', b'-'):
                candidates.append(value)

        points = sorted(set(candidates))
        ids = {points[i]: i for i in range(len(points))}
        length = len(points)

        previous = [-1] * length
        following = [-1] * length
        alive = [False] * length
        choices = []

        def remember_gap(left_id, right_id):
            if right_id == -1:
                span = infinite
            else:
                span = points[right_id] - points[left_id] - 1
            if span > 0:
                heappush(choices, (-span, left_id, right_id))

        ordered_values = sorted(set(initial))
        ordered_values = [0] + ordered_values
        ordered_ids = []

        for value in ordered_values:
            node = ids[value]
            ordered_ids.append(node)
            alive[node] = True

        for a, b in zip(ordered_ids, ordered_ids[1:]):
            following[a] = b
            previous[b] = a

        for node in ordered_ids:
            remember_gap(node, following[node])

        def current_span(item):
            right_id = item[2]
            if right_id == -1:
                return infinite
            return points[right_id] - points[item[1]] - 1

        for operation, value in changes:
            if operation == b'?':
                while choices:
                    item = choices[0]
                    if alive[item[1]] and following[item[1]] == item[2] and current_span(item) == -item[0]:
                        break
                    heappop(choices)
                if choices and -choices[0][0] >= value:
                    lines.append(str(points[choices[0][1]] + 1))
                else:
                    lines.append(str(points[0] + 1))
            elif operation == b'+':
                node = ids[value]
                if alive[node]:
                    continue
                left_id = node - 1
                while not alive[left_id]:
                    left_id -= 1
                right_id = following[left_id]
                alive[node] = True
                previous[node] = left_id
                following[node] = right_id
                following[left_id] = node
                if right_id != -1:
                    previous[right_id] = node
                remember_gap(left_id, node)
                remember_gap(node, right_id)
            else:
                node = ids[value]
                if not alive[node]:
                    continue
                left_id = previous[node]
                right_id = following[node]
                alive[node] = False
                following[left_id] = right_id
                if right_id != -1:
                    previous[right_id] = left_id
                remember_gap(left_id, right_id)

    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
