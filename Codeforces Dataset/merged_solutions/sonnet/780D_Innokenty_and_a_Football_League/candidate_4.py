import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    n = int(numbers[0])
    clubs = []
    for i in range(n):
        clubs.append((numbers[1 + 2 * i].decode(), numbers[2 + 2 * i].decode()))
    return clubs


# --- clause: club_options :: (clubs: list[tuple[str, str]]) -> list[list[str]] ---
def club_options(clubs):
    tally = {}
    for team, town in clubs:
        front = team[:3]
        tally[front] = tally.get(front, 0) + 1
    options = []
    for team, town in clubs:
        front = team[:3]
        second = team[:2] + town[0]
        if tally[front] > 1:
            options.append([second])
        else:
            options.append([front, second])
    return options


# --- clause: match_names :: (options: list[list[str]]) -> list[str] | None ---
def match_names(options):
    owner = {}
    picked = [None] * len(options)

    def flip(parent, club, name):
        while True:
            owner[name] = club
            picked[club] = name
            step = parent[club]
            if step is None:
                return
            club, name = step

    for start in range(len(options)):
        parent = {start: None}
        queue = [start]
        head = 0
        found = None
        while head < len(queue) and found is None:
            club = queue[head]
            head += 1
            for name in options[club]:
                if name not in owner:
                    found = (club, name)
                    break
                other = owner[name]
                if other not in parent:
                    parent[other] = (club, name)
                    queue.append(other)
        if found is None:
            return None
        flip(parent, found[0], found[1])
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
