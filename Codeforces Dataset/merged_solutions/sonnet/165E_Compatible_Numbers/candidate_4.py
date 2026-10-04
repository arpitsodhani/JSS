# CLAUSE: setup_environment
import sys

BITS = 22
SIZE = 1 << BITS
FULL_MASK = SIZE - 1

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))

    known = [-1] * SIZE
    for number in arr:
        known[number] = number

    for bit in range(BITS):
        bit_value = 1 << bit
        mask = bit_value
        while mask < SIZE:
            if known[mask] == -1:
                known[mask] = known[mask ^ bit_value]
            mask += 1
            if mask & bit_value == 0:
                mask += bit_value

    out = []
    append = out.append
    for number in arr:
        append(str(known[FULL_MASK ^ number]))
    sys.stdout.write(" ".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
