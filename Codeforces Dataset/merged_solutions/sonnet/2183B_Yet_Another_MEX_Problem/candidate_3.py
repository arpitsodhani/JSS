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


# --- clause: whole_mex :: (a: list[int]) -> int ---
def whole_mex(a):
    known = [False] * (len(a) + 2)
    for value in a:
        if value < len(known):
            known[value] = True
    step = 0
    while known[step]:
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
