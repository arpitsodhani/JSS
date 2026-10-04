import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: split_points :: (skills: list[int]) -> tuple[int, list[int]] ---
def split_points(skills):
    n = len(skills)
    ranked = sorted(range(n), key=lambda i: skills[i])
    huge = 1 << 62
    finest = [huge] * (n + 1)
    cut = [0] * (n + 1)
    finest[0] = 0
    for i in range(3, n + 1):
        for extent in (3, 4, 5):
            j = i - extent
            if j < 0 or finest[j] == huge:
                continue
            here = finest[j] + skills[ranked[i - 1]] - skills[ranked[j]]
            if here < finest[i]:
                finest[i] = here
                cut[i] = j
    return finest[n], [ranked[i] for i in range(n)], cut


# --- clause: label_teams :: (order: list[int], cut: list[int], n: int) -> list[int] ---
def label_teams(order, cut, n):
    labels = [0] * n
    team = 0
    stop = n
    while stop > 0:
        start = cut[stop]
        team += 1
        for i in range(start, stop):
            labels[order[i]] = team
        stop = start
    return labels


# --- clause: main :: () -> None ---
def main():
    skills = read_input()
    total, order, cut = split_points(skills)
    labels = label_teams(order, cut, len(skills))
    teams = 0
    for value in labels:
        if value > teams:
            teams = value
    sys.stdout.write("%d %d\n%s\n" % (total, teams, " ".join(map(str, labels))))


if __name__ == "__main__":
    main()
