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


# --- clause: best_jog :: (b: list[int]) -> int ---
def best_jog(b):
    huge = -(1 << 62)
    single = huge
    couple = huge
    best = huge
    for k in range(len(b)):
        if couple > huge:
            here = couple + b[k] - k
            if here > best:
                best = here
        if single > huge:
            here = single + b[k]
            if here > couple:
                couple = here
        here = b[k] + k
        if here > single:
            single = here
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for b in read_input():
        out.append(best_jog(b))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
