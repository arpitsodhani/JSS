# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def process(sequence):
    waiting = {}
    current = 0
    maximum = 0
    for number in sequence:
        if waiting.get(number, False):
            waiting[number] = False
            current -= 1
        else:
            waiting[number] = True
            current += 1
            maximum = max(maximum, current)
    return maximum

def main():
    data = sys.stdin.buffer.read().split()
    socks = (int(x) for x in data[1:])
    answer = process(socks)

# CLAUSE: finish_program
    sys.stdout.write(str(answer))

if __name__ == "__main__":
    main()
