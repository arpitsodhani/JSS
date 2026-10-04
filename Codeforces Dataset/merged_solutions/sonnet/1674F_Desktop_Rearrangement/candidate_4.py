# CLAUSE: setup_environment
import sys

class Fenwick:
    def __init__(self, size):
        self.size = size
        self.data = [0] * (size + 1)

    def change(self, index, delta):
        size = self.size
        data = self.data
        while index <= size:
            data[index] += delta
            index += index & -index

    def sum(self, index):
        data = self.data
        value = 0
        while index > 0:
            value += data[index]
            index -= index & -index
        return value

def main():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    m = int(raw[1])
    q = int(raw[2])
    cells = [list(raw[3 + i]) for i in range(n)]
    fenwick = Fenwick(n * m)
    icons = 0

# CLAUSE: solve_logic
    for r, row in enumerate(cells):
        base = r + 1
        for c, value in enumerate(row):
            if value == 42:
                icons += 1
                fenwick.change(c * n + base, 1)

    answers = []
    ptr = n + 3
    for _ in range(q):
        r = int(raw[ptr]) - 1
        c = int(raw[ptr + 1]) - 1
        ptr += 2
        pos = c * n + r + 1
        delta = -1 if cells[r][c] == 42 else 1
        cells[r][c] = 42 if delta == 1 else 46
        icons += delta
        fenwick.change(pos, delta)
        answers.append(str(icons - fenwick.sum(icons)))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()
