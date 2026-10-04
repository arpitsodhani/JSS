import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    idx = 1
    cases = int(data[0])
    words = []
    for _ in range(cases):
        idx += 1
        words.append(data[idx].decode())
        idx += 1
    return words


# --- clause: build_fb :: (limit: int) -> str ---
def build_fb(limit):
    pieces = []
    for number in range(1, limit + 1):
        if number % 3 == 0:
            pieces.append("F")
        if number % 5 == 0:
            pieces.append("B")
    return "".join(pieces)


# --- clause: solve_case :: (word: str, table: str) -> str ---
def solve_case(word, table):
    if word in table:
        return "YES"
    return "NO"


# --- clause: main :: () -> None ---
def main():
    table = build_fb(300)
    answers = []
    for word in read_input():
        answers.append(solve_case(word, table))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
