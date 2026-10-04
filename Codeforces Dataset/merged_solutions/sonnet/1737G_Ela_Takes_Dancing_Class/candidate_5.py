# CLAUSE: setup_environment
import sys

def main():
    items = sys.stdin.buffer.read().split()
    cursor = 0
    n = int(items[cursor])
    cursor += 1
    m = int(items[cursor])
    cursor += 1
    q = int(items[cursor])
    cursor += 1
    original = []
    for _ in range(n):
        original.append(int(items[cursor]))
        cursor += 1
    mask = items[cursor]
    cursor += 1
    movable_indexes = [i for i, b in enumerate(mask) if b == 49]
    result = []

# CLAUSE: solve_logic
    for _ in range(q):
        d = int(items[cursor])
        ask = int(items[cursor + 1]) - 1
        cursor += 2

        cur = list(original)
        remaining = movable_indexes[:]

        for _ in range(m):
            if not remaining:
                break

            take_pos = 0
            take = remaining[0]
            for r, idx in enumerate(remaining[1:], 1):
                if cur[idx] < cur[take]:
                    take = idx
                    take_pos = r

            x = cur[take]
            stop = None
            for val_index in range(n):
                y = cur[val_index]
                if val_index != take and y > x:
                    if stop is None or y < stop:
                        stop = y

            if stop is None:
                cur[take] = x + d
            else:
                cur[take] = min(x + d, stop - 1)

            remaining.pop(take_pos)

        result.append(str(cur[ask]))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
