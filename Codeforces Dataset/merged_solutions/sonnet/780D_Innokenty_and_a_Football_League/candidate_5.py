import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    clubs = []
    for i in range(n):
        clubs.append((raw[1 + 2 * i].decode(), raw[2 + 2 * i].decode()))
    return clubs


# --- clause: club_options :: (clubs: list[tuple[str, str]]) -> list[list[str]] ---
def club_options(clubs):
    tally = {}
    for team, town in clubs:
        taken = team[:3]
        tally[taken] = tally.get(taken, 0) + 1
    options = []
    for team, town in clubs:
        taken = team[:3]
        two = team[:2] + town[0]
        if tally[taken] > 1:
            options.append([two])
        else:
            options.append([taken, two])
    return options


# --- clause: match_names :: (options: list[list[str]]) -> list[str] | None ---
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

    for club in range(0, len(options)):
        if not augment(club, set()):
            return None
    picked = [None] * len(options)
    for name in owner:
        picked[owner[name]] = name
    return picked


# --- clause: main :: () -> None ---
def main():
    clubs = read_input()
    picked = match_names(club_options(clubs))
    if picked is None:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n" + "\n".join(picked) + "\n")


if __name__ == "__main__":
    main()
