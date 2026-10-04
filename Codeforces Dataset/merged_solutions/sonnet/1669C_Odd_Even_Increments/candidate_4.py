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


# --- clause: can_align :: (a: list[int]) -> bool ---
def can_align(a):
    odd = set()
    even = set()
    for i in range(len(a)):
        if i % 2:
            even.add(a[i] % 2)
        else:
            odd.add(a[i] % 2)
    return len(odd) == 1 and len(even) == 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("YES" if can_align(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
