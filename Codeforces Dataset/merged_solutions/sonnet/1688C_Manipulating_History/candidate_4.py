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
    seen = [False] * 26
    for piece in chunk:
        for code in piece:
            slot = code - 97
            seen[slot] = not seen[slot]
    for index, flag in enumerate(seen):
        if flag:
            return chr(97 + index)
    return "a"


# --- clause: main :: () -> None ---
def main():
    out = []
    for chunk in read_input():
        out.append(odd_letter(chunk))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
