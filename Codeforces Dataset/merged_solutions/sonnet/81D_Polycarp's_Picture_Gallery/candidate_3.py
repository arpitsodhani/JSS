import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    albums = []
    for token in data[2:m + 2]:
        albums.append(int(token))
    return n, m, albums


# --- clause: choose_counts :: (n: int, m: int, albums: list[int]) -> list[int] | None ---
def choose_counts(n, m, albums):
    half = n // 2
    take = []
    for size in albums:
        take.append(min(size, half))
    total = sum(take)
    if total < n:
        return None
    excess = total - n
    i = 0
    while excess > 0 and i < m:
        drop = min(take[i], excess)
        take[i] -= drop
        excess -= drop
        i += 1
    return take


# --- clause: arrange :: (n: int, m: int, take: list[int]) -> list[int] ---
def arrange(n, m, take):
    order = sorted(range(m), key=lambda i: -take[i])
    gallery = [0] * n
    slot = 0
    for i in order:
        remaining = take[i]
        while remaining > 0:
            gallery[slot] = i + 1
            slot += 2
            if slot >= n:
                slot = 1
            remaining -= 1
    return gallery


# --- clause: main :: () -> None ---
def main():
    n, m, albums = read_input()
    take = choose_counts(n, m, albums)
    if take is None:
        print(-1)
        return
    gallery = arrange(n, m, take)
    print(" ".join(map(str, gallery)))


if __name__ == "__main__":
    main()
