# CLAUSE: setup_environment
import sys

class MexGame:
    def __init__(self, numbers):
        self.numbers = set(numbers)
        self.answer = 0
        self.advance()

    def advance(self):
        while self.answer in self.numbers:
            self.answer += 1

    def move(self):
        value = self.answer
        self.numbers.add(value)
        return value

    def remove(self, value):
        self.numbers.discard(value)
        if value < self.answer:
            self.answer = value
        self.advance()

# CLAUSE: solve_logic
reader = sys.stdin.readline
tests = int(reader())
for _ in range(tests):
    n = int(reader())
    game = MexGame(map(int, reader().split()))
    while True:
        sys.stdout.write(f"{game.move()}\n")
        sys.stdout.flush()
        removed = int(reader())
        if removed == -1:
            break
        game.remove(removed)

# CLAUSE: finish_program
