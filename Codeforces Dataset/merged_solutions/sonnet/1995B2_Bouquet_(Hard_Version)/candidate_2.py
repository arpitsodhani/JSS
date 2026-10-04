import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    at = 1
    cases = []
    for _ in range(t):
        n = tokens[at]
        m = tokens[at + 1]
        at += 2
        petals = tokens[at:at + n]
        at += n
        stock = tokens[at:at + n]
        at += n
        cases.append((m, petals, stock))
    return cases


# --- clause: best_bouquet :: (m: int, petals: list[int], stock: list[int]) -> int ---
def best_bouquet(m, petals, stock):
    kinds = {}
    for i in range(len(petals)):
        kinds[petals[i]] = kinds.get(petals[i], 0) + stock[i]
    best = 0
    for size in kinds:
        taken = m // size
        if taken > kinds[size]:
            taken = kinds[size]
        spent = taken * size
        partner = kinds.get(size + 1, 0)
        left = m - spent
        extra = left // (size + 1)
        if extra > partner:
            extra = partner
        spent += extra * (size + 1)
        left -= extra * (size + 1)
        swaps = taken
        if partner - extra < swaps:
            swaps = partner - extra
        if left < swaps:
            swaps = left
        spent += swaps
        if spent > best:
            best = spent
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for m, petals, stock in read_input():
        out.append(best_bouquet(m, petals, stock))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
