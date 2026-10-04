import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    q = data[1]
    return n, q, data[2:]


# --- clause: final_offsets :: (n: int, q: int, moves: list[int]) -> tuple[int, int] ---
def final_offsets(n, q, moves):
    odd = 0
    even = 0
    index = 0
    for _ in range(q):
        kind = moves[index]
        index += 1
        if kind == 1:
            step = moves[index]
            index += 1
            odd += step
            even += step
            odd %= n
            even %= n
        elif odd % 2:
            odd = (odd + n - 1) % n
            even = (even + 1) % n
        else:
            odd = (odd + 1) % n
            even = (even + n - 1) % n
    return odd, even


# --- clause: arrange :: (n: int, odd: int, even: int) -> list[int] ---
def arrange(n, odd, even):
    result = [0] * n
    for boy in range(1, n + 1, 2):
        result[(boy - 1 + odd) % n] = boy
    for boy in range(2, n + 1, 2):
        result[(boy - 1 + even) % n] = boy
    return result


# --- clause: main :: () -> None ---
def main():
    n, q, moves = read_input()
    odd, even = final_offsets(n, q, moves)
    sys.stdout.write(" ".join(map(str, arrange(n, odd, even))) + "\n")


if __name__ == "__main__":
    main()
