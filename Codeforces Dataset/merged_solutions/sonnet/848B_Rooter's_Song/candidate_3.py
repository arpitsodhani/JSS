import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[tuple[int, int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, w, h = int(data[0]), int(data[1]), int(data[2])
    dancers = []
    pos = 3
    for _ in range(n):
        dancers.append((int(data[pos]), int(data[pos + 1]), int(data[pos + 2])))
        pos += 3
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
            if g == 1:
                starts.append((p, 0, i))
                ends.append((p, h))
            else:
                starts.append((0, p, i))
                ends.append((w, p))
        starts.sort(key=lambda item: (item[0], -item[1]))
        ends.sort(key=lambda item: (item[0], -item[1]))
        for index in range(len(starts)):
            target = ends[index]
            answer[starts[index][2]] = str(target[0]) + " " + str(target[1])
    return answer


# --- clause: main :: () -> None ---
def main():
    n, w, h, dancers = read_input()
    groups = group_dancers(n, dancers)
    print("\n".join(final_spots(w, h, dancers, groups)))


if __name__ == "__main__":
    main()
