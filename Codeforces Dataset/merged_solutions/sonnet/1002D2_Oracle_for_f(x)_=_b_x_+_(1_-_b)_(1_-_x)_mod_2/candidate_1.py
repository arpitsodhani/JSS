# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys


def oracle_value(bits, mask):
    res = 0
    for x, b in zip(bits, mask):
        if b == 1:
            res ^= x
        else:
            res ^= x ^ 1
    return res


def main():
    data = sys.stdin.read().split()
    if not data:
        return
    ptr = 0
    n = int(data[ptr])
    ptr += 1
    x = [int(c) for c in data[ptr]]
    ptr += 1
    b = [int(c) for c in data[ptr]]
    y = 0
    if ptr + 1 < len(data):
        y = int(data[ptr + 1])
    ans = y ^ oracle_value(x[:n], b[:n])
    print(ans)


if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
