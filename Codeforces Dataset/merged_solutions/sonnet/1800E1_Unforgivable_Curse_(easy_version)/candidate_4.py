import sys


# --- clause: read_input :: () -> list[tuple[int, str, str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    cases = []
    cursor = 1
    for _ in range(t):
        n = int(numbers[cursor])
        k = int(numbers[cursor + 1])
        cases.append((k, numbers[cursor + 2].decode(), numbers[cursor + 3].decode()))
        cursor += 4
    return cases


# --- clause: can_change :: (k: int, s: str, t: str) -> bool ---
def can_change(k, s, t):
    n = len(s)
    left = [0] * 26
    right = [0] * 26
    i = 0
    while i < n:
        if i + k < n or i - k >= 0:
            left[ord(s[i]) - 97] += 1
            right[ord(t[i]) - 97] += 1
        elif s[i] != t[i]:
            return False
        i += 1
    return left == right


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, s, t in read_input():
        out.append("YES" if can_change(k, s, t) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
