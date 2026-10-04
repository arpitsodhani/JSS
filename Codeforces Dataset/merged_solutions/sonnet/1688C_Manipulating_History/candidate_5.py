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
    parity = [0] * 26
    for piece in chunk:
        for code in piece:
            parity[code - 97] ^= 1
    index = 0
    while index < 26 and not parity[index]:
        index += 1
    return chr(97 + index) if index < 26 else "a"


# --- clause: main :: () -> None ---
def main():
    out = []
    for chunk in read_input():
        out.append(odd_letter(chunk))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
