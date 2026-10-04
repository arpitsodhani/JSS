import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: fewest_moves :: (a: list[int]) -> int ---
def fewest_moves(a):
    evens = []
    best_odd = 0
    for value in a:
        if value % 2:
            if value > best_odd:
                best_odd = value
        else:
            evens.append(value)
    if len(evens) == 0 or best_odd == 0:
        return 0
    evens.sort()
    running = best_odd
    done = 0
    for value in evens:
        if value > running:
            return len(evens) + 1
        running += value
        done += 1
    return done

# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(fewest_moves(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
