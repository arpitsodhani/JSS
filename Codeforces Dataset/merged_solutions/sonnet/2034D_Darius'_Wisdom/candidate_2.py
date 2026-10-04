# CLAUSE: setup_environment
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    t = data[pos]
    pos += 1
    ans = []

# CLAUSE: solve_logic
    for _ in range(t):
        n = data[pos]
        pos += 1
        a = data[pos:pos + n]
        pos += n

        z = a.count(0)
        o = a.count(1)
        middle_end = z + o
        moves = []
        ones = {i for i, v in enumerate(a) if v == 1}
        zeros_after = {i for i, v in enumerate(a) if v == 0 and i >= z}

        def do_swap(i, j):
            for p in (i, j):
                if a[p] == 1:
                    ones.discard(p)
                if p >= z and a[p] == 0:
                    zeros_after.discard(p)

            if a[i] > a[j]:
                moves.append((i + 1, j + 1))
            else:
                moves.append((j + 1, i + 1))

            a[i], a[j] = a[j], a[i]

            for p in (i, j):
                if a[p] == 1:
                    ones.add(p)
                if p >= z and a[p] == 0:
                    zeros_after.add(p)

        for i in range(z):
            if a[i] == 0:
                continue
            j = next(iter(zeros_after))
            if a[i] == 1:
                do_swap(i, j)
            else:
                k = next(iter(ones))
                do_swap(i, k)
                do_swap(i, j)

        right_ones = {i for i in range(middle_end, n) if a[i] == 1}
        for i in range(z, middle_end):
            if a[i] == 2:
                j = right_ones.pop()
                do_swap(i, j)

        ans.append(str(len(moves)))
        for u, v in moves:
            ans.append(f"{u} {v}")

# CLAUSE: finish_program
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
