# CLAUSE: setup_environment
import sys
from itertools import accumulate

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    case_count = int(raw[0])
    cursor = 1
    lines = []
    for _ in range(case_count):
        size = int(raw[cursor])
        cursor += 1
        arr = [int(x) for x in raw[cursor:cursor + size]]
        cursor += size
        prefixes = [0]
        prefixes.extend(accumulate(arr[:-1]))
        order = sorted(range(size), key=prefixes.__getitem__)
        ans = [None] * size
        number = size
        for index in order:
            ans[index] = str(number)
            number -= 1
        lines.append(" ".join(ans))
    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
