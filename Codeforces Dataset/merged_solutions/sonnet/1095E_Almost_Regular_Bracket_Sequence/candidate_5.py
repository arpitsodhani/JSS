import sys


# --- clause: read_input :: () -> str ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    return raw[1].decode()


# --- clause: balance_tables :: (s: str) -> tuple[list[int], list[int]] ---
def balance_tables(s):
    n = len(s)
    running = [0] * (n + 1)
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
    result = 0
    floor = 0
    for i in range(n):
        if running[i] < floor:
            floor = running[i]
        if floor < 0:
            break
        if s[i] == "(":
            if total == 2 and lowest[i + 1] >= 2:
                result += 1
        else:
            if total == -2 and lowest[i + 1] >= -2:
                result += 1
    return result


# --- clause: main :: () -> None ---
def main():
    s = read_input()
    running, lowest = balance_tables(s)
    sys.stdout.write("%d\n" % count_flips(s, running, lowest))


if __name__ == "__main__":
    main()
