import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        k = fields[offset + 1]
        offset += 2
        cases.append((k, fields[offset:offset + n]))
        offset += n
    return cases


# --- clause: count_gifts :: (k: int, gold: list[int]) -> int ---
def count_gifts(k, gold):
    purse = 0
    gifts = 0
    for entry in gold:
        if entry >= k:
            purse += entry
        elif entry == 0 and purse:
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
