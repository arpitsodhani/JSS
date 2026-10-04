import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    clubs = []
    for i in range(n):
        clubs.append((data[1 + 2 * i].decode(), data[2 + 2 * i].decode()))
    return clubs

# Clause club_options [Confidence: 1.00]
def club_options(clubs):
    tally = {}
    for team, town in clubs:
        cursor = team[:3]
        tally[cursor] = tally.get(cursor, 0) + 1
    options = []
    for team, town in clubs:
        cursor = team[:3]
        second = team[:2] + town[0]
        if tally[cursor] > 1:
            options.append([second])
        else:
            options.append([cursor, second])
    return options

# Clause match_names [Confidence: 0.80]
def match_names(options):
    sys.setrecursionlimit(5000)
    owner = {}

    def augment(club, seen):
        for name in options[club]:
            if name in seen:
                continue
            seen.add(name)
            if name not in owner or augment(owner[name], seen):
                owner[name] = club
                return True
        return False

    for club in range(len(options)):
        if not augment(club, set()):
            return None
    picked = [None] * len(options)
    for name in owner:
        picked[owner[name]] = name
    return picked

# Clause main [Confidence: 1.00]
def main():
    clubs = read_input()
    picked = match_names(club_options(clubs))
    if picked is None:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n" + "\n".join(picked) + "\n")


if __name__ == "__main__":
    main()

