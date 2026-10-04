import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 1
    t = int(data[0])
    words = []
    for _ in range(t):
        length = int(data[pos])
        pos += 1
        word = data[pos].decode()
        pos += 1
        words.append(word[:length])
    return words


# --- clause: build_fb :: (limit: int) -> str ---
def build_fb(limit):
    chars = []
    for value in range(1, limit + 1):
        if value % 3 == 0:
            chars.append("F")
        if value % 5 == 0:
            chars.append("B")
    return "".join(chars)


# --- clause: solve_case :: (word: str, table: str) -> str ---
def solve_case(word, table):
    if word not in table:
        return "NO"
    return "YES"


# --- clause: main :: () -> None ---
def main():
    table = build_fb(300)
    out = []
    for word in read_input():
        out.append(solve_case(word, table))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
