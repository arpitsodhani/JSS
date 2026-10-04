import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        reader += 1
        cases.append(numbers[reader:reader + n])
        reader += n
    return cases


# --- clause: build_partner :: (a: list[int]) -> list[int] ---
def build_partner(a):
    n = len(a)
    b = []
    start = 0
    if n % 2:
        head = a[:3]
        pick = 0
        while head[pick] + head[(pick + 1) % 3] == 0:
            pick += 1
        other = 3 - pick - (pick + 1) % 3
        triple = [0, 0, 0]
        triple[pick] = head[other]
        triple[(pick + 1) % 3] = head[other]
        triple[other] = -(head[pick] + head[(pick + 1) % 3])
        b.extend(triple)
        start = 3
    i = start
    while i < n:
        b.append(a[i + 1])
        b.append(-a[i])
        i += 2
    return b


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(" ".join(map(str, build_partner(a))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
