import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    boys = int(tokens[0])
    girls = int(tokens[1])
    return boys, girls


# --- clause: compute_answer :: (n: int, m: int) -> int ---
def compute_answer(n, m):
    limit = (n + m) // 3
    return min(limit, min(n, m))


# --- clause: main :: () -> None ---
def main():
    boys, girls = read_input()
    answer = compute_answer(boys, girls)
    print(answer)


if __name__ == "__main__":
    main()
