import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    queries = []
    for i in range(n):
        queries.append((tokens[1 + 3 * i], tokens[2 + 3 * i], tokens[3 + 3 * i]))
    return queries


# --- clause: group_by_value :: (queries: list[tuple[int, int, int]]) -> dict[int, list[tuple[int, int, int]]] ---
def group_by_value(queries):
    groups = {}
    for spot in range(len(queries)):
        kind, moment, item = queries[spot]
        if item not in groups:
            groups[item] = []
        groups[item].append((spot, kind, moment))
    return groups


# --- clause: answer_group :: (rows: list[tuple[int, int, int]], answers: dict[int, int]) -> None ---
def answer_group(rows, answers):
    moments = sorted(set(row[2] for row in rows))
    place = {}
    for i in range(len(moments)):
        place[moments[i]] = i + 1
    tree = [0] * (len(moments) + 1)
    for spot, kind, moment in rows:
        index = place[moment]
        if kind == 3:
            total = 0
            walk = index
            while walk > 0:
                total += tree[walk]
                walk -= walk & (-walk)
            answers[spot] = total
        else:
            delta = 1 if kind == 1 else -1
            walk = index
            while walk <= len(moments):
                tree[walk] += delta
                walk += walk & (-walk)


# --- clause: main :: () -> None ---
def main():
    queries = read_input()
    answers = {}
    groups = group_by_value(queries)
    for item in groups:
        answer_group(groups[item], answers)
    out = []
    for spot in sorted(answers):
        out.append(answers[spot])
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
