import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    lines = sys.stdin.buffer.read().split()
    first = lines[0].decode()
    second = lines[1].decode()
    return first, second


# --- clause: compute_answer :: (x: str, y: str) -> str ---
def compute_answer(x, y):
    answer = []
    for pos, ch in enumerate(y):
        if ch > x[pos]:
            return "-1"
        answer.append(ch)
    return "".join(answer)


# --- clause: main :: () -> None ---
def main():
    first, second = read_input()
    print(compute_answer(first, second))


if __name__ == "__main__":
    main()
