import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    t = int(fields[0])
    return [fields[2 + 2 * i].decode() for i in range(t)]


# --- clause: chain_lengths :: (s: str) -> tuple[list[int], list[int]] ---
def chain_lengths(s):
    n = len(s)
    right_r = [0] * (n + 2)
    right_l = [0] * (n + 2)
    for i in range(n - 1, -1, -1):
        right_r[i] = 1 + right_l[i + 1] if s[i] == "R" else 0
        right_l[i] = 1 + right_r[i + 1] if s[i] == "L" else 0
    left_l = [0] * (n + 1)
    left_r = [0] * (n + 1)
    for j in range(n):
        back_l = left_l[j - 1] if j else 0
        back_r = left_r[j - 1] if j else 0
        left_l[j] = 1 + back_r if s[j] == "L" else 0
        left_r[j] = 1 + back_l if s[j] == "R" else 0
    return right_r, left_l


# --- clause: city_answers :: (s: str, ahead: list[int], behind: list[int]) -> list[int] ---
def city_answers(s, ahead, behind):
    n = len(s)
    collected = []
    for city in range(n + 1):
        stop = ahead[city] if city < n else 0
        left = behind[city - 1] if city else 0
        collected.append(1 + left + stop)
    return collected


# --- clause: main :: () -> None ---
def main():
    collected = []
    for s in read_input():
        ahead, behind = chain_lengths(s)
        collected.append(" ".join(map(str, city_answers(s, ahead, behind))))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()
