import sys


# --- clause: read_input :: () -> str ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return numbers[1].decode()


# --- clause: balance_tables :: (s: str) -> tuple[list[int], list[int]] ---
def balance_tables(s):
    n = len(s)
    running = [0 for _ in range(n + 1)]
    for i in range(n):
        running[i + 1] = running[i] + (1 if s[i] == "(" else -1)
    lowest = [0] * (n + 2)
    lowest[n + 1] = 1 << 40
    for i in range(n, -1, -1):
        lowest[i] = running[i] if running[i] < lowest[i + 1] else lowest[i + 1]
    return running, lowest


# --- clause: count_flips :: (s: str, running: list[int], lowest: list[int]) -> int ---
def count_flips(s, running, lowest):
    n = len(s)
    total = running[n]
    if total != 2 and total != -2:
        return 0
    want = "(" if total == 2 else ")"
    shift = 2 if total == 2 else -2
    limit = n
    for i in range(n + 1):
        if running[i] < 0:
            limit = i - 1
            break
    answer = 0
    tail = 1 << 40
    for i in range(n - 1, -1, -1):
        if running[i + 1] < tail:
            tail = running[i + 1]
        if s[i] != want or i > limit:
            continue
        if tail - shift >= 0:
            answer += 1
    return answer


# --- clause: main :: () -> None ---
def main():
    s = read_input()
    running, lowest = balance_tables(s)
    sys.stdout.write("%d\n" % count_flips(s, running, lowest))


if __name__ == "__main__":
    main()
