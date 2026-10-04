# CLAUSE: setup_environment
import sys

class Interactor:
    def __init__(self):
        self.input = sys.stdin.readline

    def ask(self, x, y):
        print(1, x, y, flush=True)
        return self.input().strip() == "TAK"

    def answer(self, x, y):
        print(2, x, y, flush=True)

# CLAUSE: solve_logic
def lower_choice(io, left, right):
    low = left
    high = right
    while low < high:
        middle = low + (high - low) // 2
        ok = io.ask(middle, middle + 1)
        if ok:
            high = middle
            continue
        low = middle + 1
    return low

def run():
    io = Interactor()
    header = io.input().split()
    if not header:
        return
    n = int(header[0])
    first = lower_choice(io, 1, n)
    second = -1
    if first > 1:
        second = lower_choice(io, 1, first - 1)
        if not io.ask(second, first):
            second = -1
    if second < 0:
        if first < n:
            second = lower_choice(io, first + 1, n)
    io.answer(first, second)

# CLAUSE: finish_program
if __name__ == "__main__":
    run()
