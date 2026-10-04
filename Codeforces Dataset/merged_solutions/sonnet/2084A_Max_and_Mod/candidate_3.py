import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    count = tokens[0]
    return tokens[1:count + 1]


# --- clause: solve_case :: (n: int) -> str ---
def solve_case(n):
    if n & 1 == 0:
        return "-1"
    body = list(range(1, n))
    body.insert(0, n)
    return " ".join(str(v) for v in body)


# --- clause: main :: () -> None ---
def main():
    chunks = []
    for n in read_input():
        chunks.append(solve_case(n))
    print("\n".join(chunks))


if __name__ == "__main__":
    main()
