import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        k = numbers[cursor + 1]
        cursor += 2
        cases.append((k, numbers[cursor:cursor + n]))
        cursor += n
    return cases


# --- clause: whole_mex :: (a: list[int]) -> int ---
def whole_mex(a):
    pool = set(a)
    step = 0
    while step in pool:
        step += 1
    return step


# --- clause: best_mex :: (k: int, a: list[int]) -> int ---
def best_mex(k, a):
    reach = whole_mex(a)
    return reach if reach < k - 1 else k - 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, a in read_input():
        out.append(best_mex(k, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
