# CLAUSE: setup_environment
import sys

def solve_case(a):
    n = len(a)
    left_len = a.count(0)
    mid_len = a.count(1)
    mid_stop = left_len + mid_len
    moves = []
    loc = [set(), set(), set()]
    for i, x in enumerate(a):
        loc[x].add(i)

# CLAUSE: solve_logic
    def move_pair(i, j):
        x = a[i]
        y = a[j]
        loc[x].remove(i)
        loc[y].remove(j)
        if x > y:
            moves.append((i + 1, j + 1))
        else:
            moves.append((j + 1, i + 1))
        a[i], a[j] = y, x
        loc[y].add(i)
        loc[x].add(j)

    def outside_zero():
        for q in loc[0]:
            if q >= left_len:
                return q

    for i in range(left_len):
        if a[i] == 0:
            continue
        j = outside_zero()
        if a[i] == 2:
            k = next(iter(loc[1]))
            move_pair(i, k)
        move_pair(i, j)

    for i in range(left_len, mid_stop):
        if a[i] == 2:
            for j in loc[1]:
                if j >= mid_stop:
                    move_pair(i, j)
                    break

    return moves

def main():
    vals = list(map(int, sys.stdin.buffer.read().split()))
    at = 0
    t = vals[at]
    at += 1
    out = []
    for _ in range(t):
        n = vals[at]
        at += 1
        arr = vals[at:at + n]
        at += n
        got = solve_case(arr)
        out.append(str(len(got)))
        for u, v in got:
            out.append(f"{u} {v}")

# CLAUSE: finish_program
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
