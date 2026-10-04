import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    total = int(data[0])
    words = []
    for case in range(total):
        words.append(data[2 * case + 2].decode())
    return words


# --- clause: build_fb :: (limit: int) -> str ---
def build_fb(limit):
    text = ""
    for value in range(1, limit + 1):
        if value % 3 == 0:
            text += "F"
        if value % 5 == 0:
            text += "B"
    return text


# --- clause: solve_case :: (word: str, table: str) -> str ---
def solve_case(word, table):
    found = table.find(word)
    if found < 0:
        return "NO"
    return "YES"


# --- clause: main :: () -> None ---
def main():
    table = build_fb(300)
    out = []
    for word in read_input():
        out.append(solve_case(word, table))
    print("\n".join(out))


if __name__ == "__main__":
    main()
