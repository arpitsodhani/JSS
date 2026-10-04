# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def ints_from_bytes(raw):
    number = 0
    active = False
    for byte in raw:
        if 48 <= byte <= 57:
            number = number * 10 + byte - 48
            active = True
        elif active:
            yield number
            number = 0
            active = False
    if active:
        yield number

def main():
    stream = ints_from_bytes(sys.stdin.buffer.read())
    n = next(stream)

    running = 0
    limit = 0
    for count in range(1, n + 1):
        running += next(stream)
        needed_limit = (running + count - 1) // count
        if limit < needed_limit:
            limit = needed_limit

    total = running
    q = next(stream)
    lines = []

    for _ in range(q):
        t = next(stream)
        lines.append(str(-1 if t < limit else (total + t - 1) // t))

    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
