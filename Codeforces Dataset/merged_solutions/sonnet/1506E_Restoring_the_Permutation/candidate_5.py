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
        cases.append([int(token) for token in data[pos:pos + n]])
        pos += n
    return cases


# --- clause: smallest :: (prefix: list[int]) -> list[int] ---
def smallest(prefix):
    n = len(prefix)
    pool = []
    out = [0] * n
    top = 0
    cursor = 0
    for i in range(n):
        if top < prefix[i]:
            out[i] = prefix[i]
            value = top + 1
            while value < prefix[i]:
                pool.append(value)
                value += 1
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
            out[i] = stack.pop(-1)
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for prefix in read_input():
        out.append(" ".join(map(str, smallest(prefix))))
        out.append(" ".join(map(str, largest(prefix))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
