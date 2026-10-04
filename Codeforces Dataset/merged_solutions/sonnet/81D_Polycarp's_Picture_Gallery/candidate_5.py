import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    albums = list(map(int, data[2:2 + m]))
    return n, m, albums


# --- clause: choose_counts :: (n: int, m: int, albums: list[int]) -> list[int] | None ---
def choose_counts(n, m, albums):
    half = n // 2
    take = [min(size, half) for size in albums]
    if sum(take) < n:
        return None
    excess = sum(take) - n
    for i in range(m):
        if excess == 0:
            break
        drop = min(take[i], excess)
        take[i] -= drop
        excess -= drop
    return take


# --- clause: arrange :: (n: int, m: int, take: list[int]) -> list[int] ---
def arrange(n, m, take):
    order = sorted(range(m), key=lambda i: -take[i])
    gallery = [0] * n
    slot = 0
    for i in order:
        for _ in range(take[i]):
            gallery[slot] = i + 1
            if slot + 2 < n:
                slot += 2
            else:
                slot = 1
    return gallery


# --- clause: main :: () -> None ---
def main():
    n, m, albums = read_input()
    take = choose_counts(n, m, albums)
    if take is None:
        sys.stdout.write("-1\n")
        return
    layout = arrange(n, m, take)
    sys.stdout.write(" ".join(map(str, layout)) + "\n")


if __name__ == "__main__":
    main()
