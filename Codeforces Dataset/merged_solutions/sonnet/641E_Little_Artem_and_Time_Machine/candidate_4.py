import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    queries = []
    for i in range(n):
        queries.append((numbers[1 + 3 * i], numbers[2 + 3 * i], numbers[3 + 3 * i]))
    return queries


# --- clause: group_by_value :: (queries: list[tuple[int, int, int]]) -> dict[int, list[tuple[int, int, int]]] ---
def group_by_value(queries):
    groups = {}
    for spot in range(len(queries)):
        kind, moment, entry = queries[spot]
        if entry not in groups:
            groups[entry] = []
        groups[entry].append((spot, kind, moment))
    return groups


# --- clause: answer_group :: (rows: list[tuple[int, int, int]], answers: dict[int, int]) -> None ---
def answer_group(rows, answers):
    events = []
    for spot, kind, moment in rows:
        events.append((moment, spot, kind))
    order = sorted(range(len(rows)), key=lambda i: rows[i][2])
    place = {}
    rank = 0
    last = None
    for i in order:
        moment = rows[i][2]
        if last is None or moment != last:
            rank += 1
            last = moment
        place[moment] = rank
    tree = [0] * (rank + 1)
    for spot, kind, moment in rows:
        index = place[moment]
        if kind == 3:
            total = 0
            walk = index
            while walk > 0:
                total += tree[walk]
                walk -= walk & (-walk)
            answers[spot] = total
            continue
        delta = 1 if kind == 1 else -1
        walk = index
        while walk <= rank:
            tree[walk] += delta
            walk += walk & (-walk)


# --- clause: main :: () -> None ---
def main():
    queries = read_input()
    answers = {}
    groups = group_by_value(queries)
    for entry in groups:
        answer_group(groups[entry], answers)
    out = []
    for spot in sorted(answers):
        out.append(answers[spot])
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
