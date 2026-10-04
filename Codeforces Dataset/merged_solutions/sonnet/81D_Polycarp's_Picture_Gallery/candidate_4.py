import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    albums = [int(data[i + 2]) for i in range(m)]
    return n, m, albums


# --- clause: choose_counts :: (n: int, m: int, albums: list[int]) -> list[int] | None ---
def choose_counts(n, m, albums):
    half = n // 2
    take = [0] * m
    for i in range(m):
        if albums[i] < half:
            take[i] = albums[i]
        else:
            take[i] = half
    if sum(take) < n:
        return None
    excess = sum(take) - n
    for i in range(m):
        if excess == 0:
            break
        drop = take[i]
        if drop > excess:
            drop = excess
        take[i] -= drop
        excess -= drop
    return take


# --- clause: arrange :: (n: int, m: int, take: list[int]) -> list[int] ---
def arrange(n, m, take):
    order = sorted(range(m), key=lambda i: -take[i])
    gallery = [0] * n
    slot = 0
    for i in order:
        label = i + 1
        for _ in range(take[i]):
            gallery[slot] = label
            slot += 2
            if slot >= n:
                slot = 1
    return gallery


# --- clause: main :: () -> None ---
def main():
    n, m, albums = read_input()
    take = choose_counts(n, m, albums)
    if take is None:
        sys.stdout.write("-1\n")
        return
    gallery = arrange(n, m, take)
    sys.stdout.write(" ".join([str(value) for value in gallery]) + "\n")


if __name__ == "__main__":
    main()
