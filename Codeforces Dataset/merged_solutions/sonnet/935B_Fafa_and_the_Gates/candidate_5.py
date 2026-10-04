# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.read().split()
    sequence = raw[1] if len(raw) > 1 else "".join(c for c in raw[0] if c in "UR")

    x = 0
    y = 0
    last = None
    paid = 0

    index = 0
    while index < len(sequence):
        if sequence[index] == "R":
            x += 1
        else:
            y += 1

        if x != y:
            current = x > y
            if last is not None and current != last:
                paid += 1
            last = current

        index += 1

    sys.stdout.write(str(paid))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
