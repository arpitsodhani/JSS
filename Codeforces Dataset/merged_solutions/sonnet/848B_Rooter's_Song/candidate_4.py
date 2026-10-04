import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[tuple[int, int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    w = int(data[1])
    h = int(data[2])
    dancers = [(int(data[3 * i + 3]), int(data[3 * i + 4]), int(data[3 * i + 5]))
               for i in range(n)]
    return n, w, h, dancers


# --- clause: group_dancers :: (n: int, dancers: list[tuple[int, int, int]]) -> dict ---
def group_dancers(n, dancers):
    groups = {}
    for i in range(n):
        g, p, t = dancers[i]
        key = p - t
        if key in groups:
            groups[key].append(i)
        else:
            groups[key] = [i]
    return groups


# --- clause: final_spots :: (w: int, h: int, dancers: list, groups: dict) -> list[str] ---
def final_spots(w, h, dancers, groups):
    answer = [None] * len(dancers)
    for members in groups.values():
        starts = []
        ends = []
        for i in members:
            g, p, t = dancers[i]
            if g == 2:
                starts.append((0, p, i))
                ends.append((w, p))
            else:
                starts.append((p, 0, i))
                ends.append((p, h))
        starts.sort(key=lambda item: (item[0], -item[1]))
        ends.sort(key=lambda item: (item[0], -item[1]))
        for spot, target in zip(starts, ends):
            answer[spot[2]] = "%d %d" % (target[0], target[1])
    return answer


# --- clause: main :: () -> None ---
def main():
    n, w, h, dancers = read_input()
    groups = group_dancers(len(dancers), dancers)
    sys.stdout.write("\n".join(final_spots(w, h, dancers, groups)) + "\n")


if __name__ == "__main__":
    main()
