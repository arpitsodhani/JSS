import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        q = int(data[pos + 1])
        s = data[pos + 2].decode()
        pos += 3
        asked = []
        for i in range(q):
            asked.append((int(data[pos + 2 * i]), int(data[pos + 1 + 2 * i])))
        pos += 2 * q
        cases.append((s, asked))
    return cases

# Clause reach_tables [Confidence: 1.00]
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

# Clause hash_tables [Confidence: 1.00]
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

# Clause answer_query [Confidence: 1.00]
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
    amount = (span - 1) * span // 2 - 1
    if forward != backward:
        amount += span
    return amount

# Clause main [Confidence: 1.00]
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

