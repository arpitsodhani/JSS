# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_answer(number, position):
    result = []
    last_index = len(number) - 1
    for index, character in enumerate(number):
        if index == position:
            result.append(number[last_index])
        elif index == last_index:
            result.append(number[position])
        else:
            result.append(character)
    return "".join(result)

def main():
    number = sys.stdin.readline().strip()
    last = int(number[-1])
    position = -1
    index = 0

    while index + 1 < len(number):
        digit = int(number[index])
        if digit % 2 == 0:
            position = index
            if digit < last:
                break
        index += 1

    if position == -1:
        print(-1)
    else:
        print(build_answer(number, position))

# CLAUSE: finish_program
main()
