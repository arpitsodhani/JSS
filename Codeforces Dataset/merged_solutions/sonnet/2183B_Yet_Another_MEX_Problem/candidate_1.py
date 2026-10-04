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


# --- clause: whole_mex :: (a: list[int]) -> int ---
def whole_mex(a):
    seen = [False] * (len(a) + 2)
    for value in a:
        if value < len(seen):
            seen[value] = True
    step = 0
    while seen[step]:
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
