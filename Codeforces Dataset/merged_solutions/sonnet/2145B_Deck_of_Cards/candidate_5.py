# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_answer(n, moves):
    top_fixed = 0
    bottom_fixed = 0
    flexible = 0

    for move in moves:
        if move == "0":
            top_fixed += 1
        elif move == "1":
            bottom_fixed += 1
        else:
            flexible += 1

    answer = bytearray(b"+" * n)

    left_removed = top_fixed
    left_uncertain = top_fixed + flexible
    right_uncertain = n - bottom_fixed - flexible
    right_removed = n - bottom_fixed

    for idx in range(n):
        if idx < left_removed or idx >= right_removed:
            answer[idx] = 45
        elif idx < left_uncertain or idx >= right_uncertain:
            answer[idx] = 63

    return answer.decode()

def main():
    stream = sys.stdin.buffer.read().split()
    if not stream:
        return

    t = int(stream[0])
    p = 1
    result = []

    while t:
        n = int(stream[p])
        k = int(stream[p + 1])
        moves = stream[p + 2].decode()
        p += 3
        result.append(build_answer(n, moves))
        t -= 1

    sys.stdout.write("\n".join(result))

# CLAUSE: finish_program
main()
