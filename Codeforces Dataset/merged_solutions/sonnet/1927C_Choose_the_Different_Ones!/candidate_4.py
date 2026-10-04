import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        m = numbers[reader + 1]
        k = numbers[reader + 2]
        reader += 3
        a = numbers[reader:reader + n]
        reader += n
        b = numbers[reader:reader + m]
        reader += m
        cases.append((k, a, b))
    return cases


# --- clause: can_pick :: (k: int, a: list[int], b: list[int]) -> bool ---
def can_pick(k, a, b):
    here = [False] * (k + 2)
    there = [False] * (k + 2)
    for value in a:
        if value <= k:
            here[value] = True
    for value in b:
        if value <= k:
            there[value] = True
    need_left = 0
    need_right = 0
    for value in range(1, k + 1):
        if here[value] and there[value]:
            continue
        if here[value]:
            need_left += 1
        elif there[value]:
            need_right += 1
        else:
            return False
    return need_left * 2 <= k and need_right * 2 <= k


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, a, b in read_input():
        out.append("YES" if can_pick(k, a, b) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
