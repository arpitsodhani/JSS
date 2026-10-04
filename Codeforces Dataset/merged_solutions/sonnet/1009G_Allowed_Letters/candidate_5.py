# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class Solver:
    def __init__(self, items):
        self.items = items
        self.full = 63

    def read(self):
        self.text = self.items[0]
        self.n = len(self.text)
        self.rules = [self.full] * self.n
        m = int(self.items[1]) if len(self.items) > 1 else 0
        k = 2
        for _ in range(m):
            where = int(self.items[k]) - 1
            word = self.items[k + 1]
            k += 2
            mask = 0
            for ch in word:
                mask |= 1 << (ch - 97)
            self.rules[where] = mask

    def prepare(self):
        self.left = [0] * 6
        for ch in self.text:
            self.left[ch - 97] += 1

        exact = [0] * 64
        for rule in self.rules:
            exact[rule] += 1

        self.need = [0] * 64
        for mask, amount in enumerate(exact):
            if amount:
                rest = self.full ^ mask
                add = rest
                while True:
                    self.need[mask | add] += amount
                    if add == 0:
                        break
                    add = (add - 1) & rest

        self.cap = [0] * 64
        for c, amount in enumerate(self.left):
            if amount:
                bit = 1 << c
                for mask in range(1, 64):
                    if mask & bit:
                        self.cap[mask] += amount

        self.rule_hits = []
        for mask in range(64):
            current = []
            rest = self.full ^ mask
            add = rest
            while True:
                current.append(mask | add)
                if add == 0:
                    break
                add = (add - 1) & rest
            self.rule_hits.append(current)

        self.char_hits = [[mask for mask in range(1, 64) if mask & (1 << c)] for c in range(6)]

    def valid(self):
        for mask in range(1, 64):
            if self.need[mask] > self.cap[mask]:
                return False
        return True

    def run(self):
        self.read()
        self.prepare()

        if not self.valid():
            return "Impossible"

        result = []
        for rule in self.rules:
            for mask in self.rule_hits[rule]:
                self.need[mask] -= 1

            choice = None
            for c in range(6):
                if self.left[c] <= 0 or rule & (1 << c) == 0:
                    continue

                self.left[c] -= 1
                for mask in self.char_hits[c]:
                    self.cap[mask] -= 1

                if self.valid():
                    choice = c
                    break

                for mask in self.char_hits[c]:
                    self.cap[mask] += 1
                self.left[c] += 1

            if choice is None:
                return "Impossible"
            result.append(chr(97 + choice))

        return "".join(result)

# CLAUSE: finish_program
def main():
    data = sys.stdin.buffer.read().split()
    if data:
        sys.stdout.write(Solver(data).run() + "\n")

if __name__ == "__main__":
    main()
