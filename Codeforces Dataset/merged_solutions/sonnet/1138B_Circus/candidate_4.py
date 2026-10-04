import sys


# --- clause: read_input :: () -> tuple[int, str, str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    n = int(numbers[0])
    return n, numbers[1].decode(), numbers[2].decode()


# --- clause: group_artists :: (n: int, clowns: str, acrobats: str) -> list[list[int]] ---
def group_artists(n, clowns, acrobats):
    groups = [[], [], [], []]
    for i in range(n):
        kind = (1 if clowns[i] == "1" else 0) * 2 + (1 if acrobats[i] == "1" else 0)
        spot = 0
        if kind == 2:
            spot = 0
        elif kind == 1:
            spot = 1
        elif kind == 3:
            spot = 2
        else:
            spot = 3
        groups[spot].append(i + 1)
    return groups


# --- clause: pick_show :: (n: int, groups: list[list[int]]) -> list[int] | None ---
def pick_show(n, groups):
    na = len(groups[0])
    nb = len(groups[1])
    nc = len(groups[2])
    nd = len(groups[3])
    half = n // 2
    for x in range(na + 1):
        for z in range(nc + 1):
            y = nb + nc - 2 * z - x
            if y < 0 or y > nb:
                continue
            w = half - x - y - z
            if w < 0 or w > nd:
                continue
            return groups[0][:x] + groups[1][:y] + groups[2][:z] + groups[3][:w]
    return None


# --- clause: main :: () -> None ---
def main():
    n, clowns, acrobats = read_input()
    picked = pick_show(n, group_artists(n, clowns, acrobats))
    if picked is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(" ".join(map(str, picked)) + "\n")


if __name__ == "__main__":
    main()
