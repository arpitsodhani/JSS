# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class BalancedReversals:
    def __init__(self, source, target):
        self.source = [source[i:i + 2] for i in range(0, len(source), 2)]
        self.target = [target[i:i + 2] for i in range(0, len(target), 2)]
        self.moves = []

    def group(self, pair):
        return pair if pair[0] == pair[1] else "M"

    def mirror(self, pair):
        return pair[1] + pair[0]

    def reverse_prefix(self, amount):
        updated = []
        for pair in reversed(self.source[:amount]):
            updated.append(self.mirror(pair))
        self.source[:amount] = updated

    def compatible(self):
        left = {"00": 0, "11": 0, "M": 0}
        right = {"00": 0, "11": 0, "M": 0}
        for pair in self.source:
            left[self.group(pair)] += 1
        for pair in self.target:
            right[self.group(pair)] += 1
        return left == right

    def first_matching(self, end, wanted):
        wanted_group = self.group(wanted)
        backup = -1
        for idx in range(end + 1):
            pair = self.source[idx]
            if self.group(pair) != wanted_group:
                continue
            if backup == -1:
                backup = idx
            if wanted_group != "M":
                return idx
            if idx == 0 and self.mirror(pair) == wanted:
                return idx
            if idx > 0 and pair == wanted:
                return idx
        if backup != -1:
            self.moves.append(2)
            self.reverse_prefix(1)
        return backup

    def run(self):
        if not self.compatible():
            return None

        for end in reversed(range(len(self.source))):
            wanted = self.target[end]
            if self.source[end] == wanted:
                continue

            idx = self.first_matching(end, wanted)

            if idx != 0:
                self.moves.append(2 * (idx + 1))
                self.reverse_prefix(idx + 1)

            self.moves.append(2 * (end + 1))
            self.reverse_prefix(end + 1)

        return self.moves

def solve_one(a, b):
    return BalancedReversals(a, b).run()

# CLAUSE: finish_program
def main():
    data = sys.stdin.read().split()
    if len(data) == 0:
        return
    cases = int(data[0])
    cursor = 1
    answer = []
    for _ in range(cases):
        moves = solve_one(data[cursor], data[cursor + 1])
        cursor += 2
        if moves is None:
            answer.append("-1")
        else:
            answer.append(str(len(moves)))
            answer.append(" ".join(str(move) for move in moves))
    print("\n".join(answer))

if __name__ == "__main__":
    main()
