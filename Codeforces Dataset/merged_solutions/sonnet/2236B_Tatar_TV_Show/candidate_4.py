import sys


# --- clause: read_input :: () -> list[tuple[int, str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    cursor = 1
    cases = []
    for _ in range(t):
        k = int(numbers[cursor + 1])
        s = numbers[cursor + 2].decode()
        cursor += 3
        cases.append((k, s))
    return cases


# --- clause: can_clear :: (k: int, s: str) -> bool ---
def can_clear(k, s):
    parity = [0] * k
    for i in range(len(s)):
        if s[i] == "1":
            parity[i % k] ^= 1
    return sum(parity) == 0


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, s in read_input():
        out.append("YES" if can_clear(k, s) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
