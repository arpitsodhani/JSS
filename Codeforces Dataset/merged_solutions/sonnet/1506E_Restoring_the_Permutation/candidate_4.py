import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        cases.append([int(data[pos + i]) for i in range(n)])
        pos += n
    return cases


# --- clause: smallest :: (prefix: list[int]) -> list[int] ---
def smallest(prefix):
    n = len(prefix)
    out = [0] * n
    pool = []
    cursor = 0
    top = 0
    for i in range(n):
        if prefix[i] > top:
            out[i] = prefix[i]
            for value in range(top + 1, prefix[i]):
                pool.append(value)
            top = prefix[i]
        else:
            out[i] = pool[cursor]
            cursor += 1
    return out


# --- clause: largest :: (prefix: list[int]) -> list[int] ---
def largest(prefix):
    n = len(prefix)
    stack = []
    out = [0] * n
    top = 0
    for i in range(n):
        if prefix[i] > top:
            out[i] = prefix[i]
            for value in range(top + 1, prefix[i]):
                stack.append(value)
            top = prefix[i]
        else:
            out[i] = stack.pop()
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(" ".join(map(str, smallest(case))))
        out.append(" ".join(map(str, largest(case))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
