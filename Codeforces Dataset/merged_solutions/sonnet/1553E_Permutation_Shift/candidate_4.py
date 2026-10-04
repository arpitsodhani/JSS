import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        m = numbers[reader + 1]
        reader += 2
        cases.append((m, numbers[reader:reader + n]))
        reader += n
    return cases


# --- clause: shift_matches :: (p: list[int]) -> list[int] ---
def shift_matches(p):
    n = len(p)
    matches = [0] * n
    for i in range(n):
        matches[(i - p[i] + 1) % n] += 1
    return matches


# --- clause: swaps_needed :: (p: list[int], shift: int) -> int ---
def swaps_needed(p, shift):
    n = len(p)
    seen = [False] * n
    moved = 0
    cycles = 0
    for i in range(n):
        if seen[i] or p[i] == (i - shift) % n + 1:
            continue
        cycles += 1
        j = i
        while not seen[j]:
            seen[j] = True
            moved += 1
            j = (p[j] - 1 + shift) % n
    return moved - cycles


# --- clause: possible_shifts :: (m: int, p: list[int]) -> list[int] ---
def possible_shifts(m, p):
    n = len(p)
    matches = shift_matches(p)
    found = []
    for shift in range(n):
        if matches[shift] < n - 2 * m:
            continue
        if swaps_needed(p, shift) <= m:
            found.append(shift)
    return found


# --- clause: main :: () -> None ---
def main():
    out = []
    for m, p in read_input():
        found = possible_shifts(m, p)
        out.append(" ".join(map(str, [len(found)] + found)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
