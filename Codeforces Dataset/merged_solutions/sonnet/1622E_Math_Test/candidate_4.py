import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[str]]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    reader = 1
    cases = []
    for _ in range(t):
        n = int(numbers[reader])
        m = int(numbers[reader + 1])
        reader += 2
        wanted = [int(v) for v in numbers[reader:reader + n]]
        reader += n
        sheets = [numbers[reader + i].decode() for i in range(n)]
        reader += n
        cases.append((m, wanted, sheets))
    return cases


# --- clause: question_groups :: (n: int, m: int, sheets: list[str]) -> list[int] ---
def question_groups(n, m, sheets):
    marks = [0] * m
    for i in range(n):
        row = sheets[i]
        bit = 1 << i
        for j in range(m):
            if row[j] == "1":
                marks[j] |= bit
    return marks


# --- clause: best_permutation :: (n: int, m: int, wanted: list[int], marks: list[int]) -> list[int] ---
def best_permutation(n, m, wanted, marks):
    groups = {}
    for j in range(m):
        if marks[j] in groups:
            groups[marks[j]].append(j)
        else:
            groups[marks[j]] = [j]
    keys = list(groups)
    best_value = None
    best_order = None
    for mask in range(1 << n):
        weight = []
        for key in keys:
            here = 0
            for i in range(n):
                if (key >> i) & 1:
                    here += 1 if (mask >> i) & 1 else -1
            weight.append(here)
        ranked = sorted(range(len(keys)), key=lambda idx: weight[idx])
        value = 0
        for i in range(n):
            value -= wanted[i] if (mask >> i) & 1 else -wanted[i]
        points = 1
        for idx in ranked:
            for _ in groups[keys[idx]]:
                value += weight[idx] * points
                points += 1
        if best_value is None or value > best_value:
            best_value = value
            best_order = ranked
    scores = [0] * m
    points = 1
    for idx in best_order:
        for j in groups[keys[idx]]:
            scores[j] = points
            points += 1
    return scores


# --- clause: main :: () -> None ---
def main():
    out = []
    for m, wanted, sheets in read_input():
        n = len(wanted)
        marks = question_groups(n, m, sheets)
        out.append(" ".join(map(str, best_permutation(n, m, wanted, marks))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
