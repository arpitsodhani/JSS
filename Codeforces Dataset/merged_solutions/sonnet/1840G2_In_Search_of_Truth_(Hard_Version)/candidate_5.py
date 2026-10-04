# CLAUSE: setup_environment
import sys

class Interactor:
    def __init__(self):
        self.input = sys.stdin.readline

    def read_int(self):
        return int(self.input())

    def query(self, direction, length):
        print(direction, length, flush=True)
        return self.read_int()

    def answer(self, value):
        print("!", value, flush=True)

# CLAUSE: solve_logic
def solve():
    io = Interactor()
    initial = io.read_int()
    visited = {initial: 0}

    for count in range(10):
        next_count = count + 1
        number = io.query("+", 1)
        if number == initial:
            io.answer(next_count)
            return
        if number not in visited:
            visited[number] = next_count

    block_size = 1010
    for block_count in range(1, 991):
        number = io.query("-", block_size)
        if number in visited:
            candidate = visited[number] + block_count * block_size - 10
            if candidate > 0:
                io.answer(candidate)
                return

# CLAUSE: finish_program
solve()
