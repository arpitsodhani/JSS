# CLAUSE: setup_environment
import sys

BITS = 22
LIMIT = 1 << BITS
ALL_BITS = LIMIT - 1

# CLAUSE: solve_logic
def build_answers(values):
    table = [-1] * LIMIT
    for value in values:
        table[value] = value

    stride = 1
    for _ in range(BITS):
        block = stride * 2
        for base in range(0, LIMIT, block):
            source = base
            target = base + stride
            end = target + stride
            while target < end:
                if table[target] < 0:
                    table[target] = table[source]
                source += 1
                target += 1
        stride = block

    return [table[ALL_BITS ^ value] for value in values]

def main():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    values = [int(item) for item in raw[1:1 + n]]
    answers = build_answers(values)
    sys.stdout.write(" ".join(map(str, answers)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
