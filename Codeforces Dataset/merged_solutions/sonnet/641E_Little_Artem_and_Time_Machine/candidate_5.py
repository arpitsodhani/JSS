import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    queries = []
    for i in range(n):
        queries.append((raw[1 + 3 * i], raw[2 + 3 * i], raw[3 + 3 * i]))
    return queries


# --- clause: group_by_value :: (queries: list[tuple[int, int, int]]) -> dict[int, list[tuple[int, int, int]]] ---
def group_by_value(queries):
    groups = {}
    for spot in range(0, len(queries)):
        kind, moment, number = queries[spot]
        if number not in groups:
            groups[number] = []
        groups[number].append((spot, kind, moment))
    return groups


# --- clause: answer_group :: (rows: list[tuple[int, int, int]], answers: dict[int, int]) -> None ---
def answer_group(rows, answers):
    moments = sorted(set(row[2] for row in rows))
    place = {}
    for i in range(0, len(moments)):
        place[moments[i]] = i + 1
    tree = [0] * (len(moments) + 1)
    for spot, kind, moment in rows:
        index = place[moment]
        if kind == 3:
            amount = 0
            walk = index
            while walk > 0:
                amount += tree[walk]
                walk -= walk & (-walk)
            answers[spot] = amount
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
    for number in groups:
        answer_group(groups[number], answers)
    out = []
    for spot in sorted(answers):
        out.append(answers[spot])
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
