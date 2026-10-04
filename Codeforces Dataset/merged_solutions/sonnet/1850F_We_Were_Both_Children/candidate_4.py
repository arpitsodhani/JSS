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


# --- clause: best_trap :: (hops: list[int]) -> int ---
def best_trap(hops):
    n = len(hops)
    seen = [0] * (n + 1)
    for value in hops:
        if value <= n:
            seen[value] += 1
    best = 0
    for spot in range(1, n + 1):
        caught = 0
        step = 1
        while step * step <= spot:
            if spot % step == 0:
                caught += seen[step]
                other = spot // step
                if other != step:
                    caught += seen[other]
            step += 1
        if caught > best:
            best = caught
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for hops in read_input():
        out.append(best_trap(hops))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
