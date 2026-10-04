import sys


# --- clause: read_input :: () -> list[list[bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        chunk = data[pos:pos + 2 * n + 1]
        pos += 2 * n + 1
        cases.append(chunk)
    return cases


# --- clause: odd_letter :: (chunk: list[bytes]) -> str ---
def odd_letter(chunk):
    mask = 0
    for piece in chunk:
        for code in piece:
            mask ^= 1 << (code - 97)
    index = 0
    while not mask & 1:
        mask >>= 1
        index += 1
    return chr(97 + index)


# --- clause: main :: () -> None ---
def main():
    out = []
    for chunk in read_input():
        out.append(odd_letter(chunk))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
