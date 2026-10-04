# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def get_cases(data):
    if len(data) == 0:
        return []
    case_count = data[0]
    cursor = 1
    assembled = []
    remaining_ok = True
    for case_index in range(case_count):
        if cursor >= len(data):
            remaining_ok = False
            break
        n = data[cursor]
        cursor += 1
        size = n * 2 + 1
        if len(data) - cursor < size:
            remaining_ok = False
            break
        assembled.append((n, data[cursor:cursor + size]))
        cursor += size
    if remaining_ok and cursor == len(data):
        return assembled
    single_n = data[0]
    single_size = single_n * 2 + 1
    single_arr = data[1:1 + single_size]
    if len(single_arr) == single_size:
        return [(single_n, single_arr)]
    return []

def triple_positions(arr):
    seen = {}
    for pos, value in enumerate(arr, start=1):
        current = seen.get(value)
        if current is None:
            seen[value] = (pos,)
        elif len(current) == 1:
            seen[value] = (current[0], pos)
        else:
            return current + (pos,)
    return ()

# CLAUSE: finish_program
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    answers = []
    for n, arr in get_cases(data):
        positions = triple_positions(arr)
        if positions:
            answers.append(f"{positions[0]} {positions[1]} {positions[2]}")
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()
