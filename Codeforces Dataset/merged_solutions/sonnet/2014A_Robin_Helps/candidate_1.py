import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        k = data[pos + 1]
        pos += 2
        cases.append((k, data[pos:pos + n]))
        pos += n
    return cases


# --- clause: count_gifts :: (k: int, gold: list[int]) -> int ---
def count_gifts(k, gold):
    purse = 0
    gifts = 0
    for value in gold:
        if value >= k:
            purse += value
        elif value == 0 and purse:
            purse -= 1
            gifts += 1
    return gifts


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, gold in read_input():
        out.append(count_gifts(k, gold))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
