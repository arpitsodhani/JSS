import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    return k, data[2:2 + n]

# Clause pick_team [Confidence: 1.00]
def pick_team(k, ratings):
    marked = set()
    team = []
    for i in range(len(ratings)):
        if ratings[i] in marked:
            continue
        marked.add(ratings[i])
        team.append(i + 1)
        if len(team) == k:
            return team
    return None

# Clause main [Confidence: 1.00]
def main():
    k, ratings = read_input()
    team = pick_team(k, ratings)
    if team is None:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n%s\n" % " ".join(map(str, team)))


if __name__ == "__main__":
    main()

