# Clause setup_environment [Confidence: 0.40]
import sys

def ask(x, y):
    print(1, x, y, flush=True)
    return sys.stdin.readline().strip() == "TAK"


# Clause solve_logic [Confidence: 0.80]
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


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


