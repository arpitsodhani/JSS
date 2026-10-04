import sys

def parse_blocks(tokens):
    blocks = []
    for token in tokens:
        p = token.find(b'-')
        length = int(token[:p])
        ch = token[p + 1]
        if blocks and blocks[-1][1] == ch:
            blocks[-1] = (blocks[-1][0] + length, ch)
        else:
            blocks.append((length, ch))
    return blocks

def prefix_function(pattern):
    pi = [0] * len(pattern)
    for i in range(1, len(pattern)):
        j = pi[i - 1]
        while j and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    return pi

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])

    t = parse_blocks(data[2:2 + n])
    s = parse_blocks(data[2 + n:2 + n + m])

    if len(s) == 1:
        need_len, need_ch = s[0]
        ans = 0
        for length, ch in t:
            if ch == need_ch and length >= need_len:
                ans += length - need_len + 1
        print(ans)
        return

    if len(s) == 2:
        (l1, c1), (l2, c2) = s
        ans = 0
        for i in range(len(t) - 1):
            if t[i][1] == c1 and t[i + 1][1] == c2 and t[i][0] >= l1 and t[i + 1][0] >= l2:
                ans += 1
        print(ans)
        return

    middle = s[1:-1]
    pi = prefix_function(middle)
    ans = 0
    j = 0
    mid_len = len(middle)

    for i, block in enumerate(t):
        while j and block != middle[j]:
            j = pi[j - 1]
        if block == middle[j]:
            j += 1

        if j == mid_len:
            start = i - mid_len + 1
            left = start - 1
            right = i + 1

            if left >= 0 and right < len(t):
                if (
                    t[left][1] == s[0][1]
                    and t[left][0] >= s[0][0]
                    and t[right][1] == s[-1][1]
                    and t[right][0] >= s[-1][0]
                ):
                    ans += 1

            j = pi[j - 1]

    print(ans)

if __name__ == "__main__":
    main()
