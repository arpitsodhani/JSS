# CLAUSE: setup_environment
import sys

def main():
    tokens = sys.stdin.buffer.read().split()
    strings = tokens[1:]
    coords = []
    for raw in strings:
        b = raw.count(b'B')
        total = len(raw)
        coords.append((total, b - (total - b)))

# CLAUSE: solve_logic
    def candidate(limit):
        a = 1
        b = 10 ** 18
        c = -10 ** 18
        d = 10 ** 18
        for x, y in coords:
            a = max(a, x - limit)
            b = min(b, x + limit)
            c = max(c, y - limit)
            d = min(d, y + limit)
        if a > b or c > d:
            return None
        x = a
        while x <= b and x < a + 2:
            y = c + ((x ^ c) & 1)
            if y <= d:
                blue = (x + y) // 2
                neutral = (x - y) // 2
                if blue >= 0 and neutral >= 0 and blue + neutral:
                    return blue, neutral
            x += 1
        return None

    lo, hi = 0, 1000000
    while lo != hi:
        center = (lo + hi) >> 1
        if candidate(center):
            hi = center
        else:
            lo = center + 1
    answer = candidate(lo)

# CLAUSE: finish_program
    print(lo)
    print("B" * answer[0] + "N" * answer[1])

if __name__ == "__main__":
    main()
