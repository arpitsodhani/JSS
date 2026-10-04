# CLAUSE: setup_environment
import sys

input_stream = sys.stdin
output_stream = sys.stdout

def ask_triplet(a, b, c):
    output_stream.write(f"{a} {b} {c}\n")
    output_stream.flush()
    response = input_stream.readline().strip()
    if response == "X":
        return "ab"
    if response == "Y":
        return "bc"
    return "ca"

# CLAUSE: solve_logic
def new_internal(left_child, right_child):
    built_nodes.append((left_child, right_child))
    return total_leaves + len(built_nodes)

def construct(segment):
    length = len(segment)
    if length == 1:
        return segment[0]
    if length == 2:
        return new_internal(segment[0], segment[1])

    anchor_left = segment[0]
    anchor_right = segment[1]
    left_part = [anchor_left]
    right_part = [anchor_right]

    for candidate in segment[2:]:
        chosen = ask_triplet(anchor_left, anchor_right, candidate)
        target = right_part if chosen == "bc" else left_part
        target.append(candidate)

    left_id = construct(left_part)
    right_id = construct(right_part)
    return new_internal(left_id, right_id)

def run():
    global total_leaves, built_nodes
    total_leaves = int(input_stream.readline())
    built_nodes = []
    root_id = construct(list(range(1, total_leaves + 1)))

    result = [0] * (2 * total_leaves - 1)
    current = total_leaves + 1
    for left_child, right_child in built_nodes:
        result[left_child - 1] = current
        result[right_child - 1] = current
        current += 1
    result[root_id - 1] = -1
    return result

# CLAUSE: finish_program
final_answer = run()
output_stream.write("-1\n")
output_stream.flush()
output_stream.write(" ".join(map(str, final_answer)) + "\n")
output_stream.flush()
