import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    n = int(fields[0])
    clubs = []
    for i in range(n):
        clubs.append((fields[1 + 2 * i].decode(), fields[2 + 2 * i].decode()))
    return clubs


# --- clause: club_options :: (clubs: list[tuple[str, str]]) -> list[list[str]] ---
def club_options(clubs):
    tally = {}
    for team, town in clubs:
        read_at = team[:3]
        tally[read_at] = tally.get(read_at, 0) + 1
    options = []
    for team, town in clubs:
        read_at = team[:3]
        follow = team[:2] + town[0]
        if tally[read_at] > 1:
            options.append([follow])
        else:
            options.append([read_at, follow])
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

    for club in range(len(options)):
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
