# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class GarlandSet:
    def __init__(self, n, m, data, pos):
        self.n = n
        self.m = m
        self.tables = []
        self.pos = pos
        self.read_all(data)

    def read_all(self, data):
        width = self.m + 1
        for _ in range(self.count):
            amount = int(data[self.pos])
            self.pos += 1
            table = [[0] * width for _ in range(self.n + 1)]
            for _ in range(amount):
                r = int(data[self.pos])
                c = int(data[self.pos + 1])
                v = int(data[self.pos + 2])
                self.pos += 3
                table[r][c] = v

            for r in range(1, self.n + 1):
                row = table[r]
                prev = table[r - 1]
                left_sum = 0
                for c in range(1, width):
                    left_sum += row[c]
                    row[c] = left_sum + prev[c]
            self.tables.append(table)

    def configure_count(self, count):
        self.count = count

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])

    holder = GarlandSet.__new__(GarlandSet)
    holder.n = n
    holder.m = m
    holder.tables = []
    holder.pos = 3
    holder.configure_count(k)
    holder.read_all(data)

    pos = holder.pos
    q = int(data[pos])
    pos += 1
    state = bytearray(b"\x01" * k)
    answers = []

    for _ in range(q):
        cmd = data[pos]
        if cmd == b"ASK":
            r1 = int(data[pos + 1])
            c1 = int(data[pos + 2])
            r2 = int(data[pos + 3])
            c2 = int(data[pos + 4])
            pos += 5
            total = 0
            top = r1 - 1
            left = c1 - 1
            for i in range(k):
                if state[i]:
                    pref = holder.tables[i]
                    total += pref[r2][c2] - pref[top][c2] - pref[r2][left] + pref[top][left]
            answers.append(str(total))
        else:
            garland = int(data[pos + 1]) - 1
            pos += 2
            state[garland] = 1 - state[garland]

    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
main()
