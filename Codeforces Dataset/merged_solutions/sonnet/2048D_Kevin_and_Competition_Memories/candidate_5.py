# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def dangerous_counts(ratings, problems):
    kevin = ratings[0]
    useful = []
    for d in problems:
        if d > kevin:
            useful.append(d)
    useful.sort(reverse=True)
    ratings.sort(reverse=True)
    penalties = []
    r = 0
    n = len(ratings)
    for d in useful:
        while r < n and ratings[r] >= d:
            r += 1
        if r:
            penalties.append(r)
    return penalties

def build_output(penalties, m):
    penalties.sort(reverse=True)
    h = len(penalties)
    row = []
    k = 1
    while k <= m:
        total = m // k
        remainder = m - total * k
        pos = remainder if remainder < h else h
        while pos < h:
            total += penalties[pos]
            pos += k
        row.append(str(total))
        k += 1
    return " ".join(row)

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    t = values[pos]
    pos += 1
    rows = []
    for _ in range(t):
        n = values[pos]
        m = values[pos + 1]
        pos += 2
        ratings = values[pos:pos + n]
        pos += n
        problems = values[pos:pos + m]
        pos += m
        rows.append(build_output(dangerous_counts(ratings, problems), m))
    sys.stdout.write("\n".join(rows))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
