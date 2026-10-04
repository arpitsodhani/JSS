# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def steps_required(value):
    if value <= 1:
        return value
    return (value - 1).bit_length()

def build_rows(n, k):
    if n == 1:
        return ["1"] * k
    need = n - 1
    if k < steps_required(need):
        return None
    rows = []
    old_span = 1
    for _ in range(k):
        new_span = old_span * 2
        if new_span > need:
            new_span = need
        row = []
        for pos in range(1, n + 1):
            distance = n - pos
            gained = min(distance, new_span) - min(distance, old_span)
            row.append(str(n - gained))
        rows.append(" ".join(row))
        old_span = new_span
    return rows

# CLAUSE: finish_program
def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    k = int(tokens[1])
    rows = build_rows(n, k)
    if rows is None:
        sys.stdout.write("-1")
    else:
        sys.stdout.write("\n".join(rows))

if __name__ == "__main__":
    main()
