import sys


# --- clause: read_input :: () -> list[tuple[str, list[tuple[int, int]]]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    t = int(fields[0])
    cursor = 1
    cases = []
    for _ in range(t):
        n = int(fields[cursor])
        q = int(fields[cursor + 1])
        s = fields[cursor + 2].decode()
        cursor += 3
        asked = []
        for i in range(q):
            asked.append((int(fields[cursor + 2 * i]), int(fields[cursor + 1 + 2 * i])))
        cursor += 2 * q
        cases.append((s, asked))
    return cases


# --- clause: reach_tables :: (s: str) -> tuple[list[int], list[int]] ---
def reach_tables(s):
    n = len(s)
    same = [0] * n
    alt = [0] * n
    same[n - 1] = n - 1
    alt[n - 1] = n - 1
    if n >= 2:
        same[n - 2] = n - 1 if s[n - 2] == s[n - 1] else n - 2
        alt[n - 2] = n - 1
    for i in range(n - 3, -1, -1):
        same[i] = same[i + 1] if s[i] == s[i + 1] else i
        alt[i] = alt[i + 1] if s[i] == s[i + 2] else i + 1
    return same, alt


# --- clause: hash_tables :: (s: str) -> tuple[list[int], list[int], list[int], int] ---
def hash_tables(s):
    n = len(s)
    mod = (1 << 61) - 1
    base = 131
    power = [1] * (n + 1)
    ahead = [0] * (n + 1)
    back = [0] * (n + 1)
    for i in range(n):
        power[i + 1] = power[i] * base % mod
        ahead[i + 1] = (ahead[i] * base + ord(s[i])) % mod
        back[i + 1] = (back[i] * base + ord(s[n - 1 - i])) % mod
    return ahead, back, power, mod


# --- clause: answer_query :: (s: str, same: list[int], alt: list[int], ahead: list[int], back: list[int], power: list[int], mod: int, l: int, r: int) -> int ---
def answer_query(s, same, alt, ahead, back, power, mod, l, r):
    n = len(s)
    a = l - 1
    b = r - 1
    span = b - a + 1
    if same[a] >= b:
        return 0
    if alt[a] >= b:
        half = span // 2
        return half * (half + 1)
    forward = (ahead[b + 1] - ahead[a] * power[span]) % mod
    x = n - 1 - b
    backward = (back[x + span] - back[x] * power[span]) % mod
    tally = (span - 1) * span // 2 - 1
    if forward != backward:
        tally += span
    return tally


# --- clause: main :: () -> None ---
def main():
    out = []
    for s, asked in read_input():
        same, alt = reach_tables(s)
        ahead, back, power, mod = hash_tables(s)
        for l, r in asked:
            out.append(answer_query(s, same, alt, ahead, back, power, mod, l, r))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
