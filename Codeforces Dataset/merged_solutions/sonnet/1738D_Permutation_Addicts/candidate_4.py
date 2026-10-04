import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        cases.append(numbers[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: pick_threshold :: (b: list[int]) -> int ---
def pick_threshold(b):
    n = len(b)
    low = 0
    high = n
    for x in range(1, n + 1):
        other = b[x - 1]
        if other > x:
            if x > low:
                low = x
            if other - 1 < high:
                high = other - 1
        else:
            if other > low:
                low = other
            if x - 1 < high:
                high = x - 1
    return low


# --- clause: rebuild_order :: (b: list[int]) -> list[int] ---
def rebuild_order(b):
    n = len(b)
    children = [[] for _ in range(n + 2)]
    for x in range(1, n + 1):
        children[b[x - 1]].append(x)
    root = 0 if children[0] else n + 1
    order = []
    node = root
    while True:
        deeper = 0
        for child in children[node]:
            if children[child]:
                deeper = child
            else:
                order.append(child)
        if deeper == 0:
            break
        order.append(deeper)
        node = deeper
    return order


# --- clause: main :: () -> None ---
def main():
    out = []
    for b in read_input():
        out.append(str(pick_threshold(b)))
        out.append(" ".join(map(str, rebuild_order(b))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
