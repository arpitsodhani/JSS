# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    text = ''.join(sys.stdin.read().split())
    next_child = [{}]
    direct_files = [0]
    real_folder = [False]

    def add_node(folder_flag):
        next_child.append({})
        direct_files.append(0)
        real_folder.append(folder_flag)
        return len(next_child) - 1

    positions = [
        i for i in range(len(text) - 2)
        if text[i] in "CDEFG" and text[i + 1] == ":" and text[i + 2] == "\\"
    ]

    for order in range(len(positions)):
        begin = positions[order]
        end = positions[order + 1] if order + 1 < len(positions) else len(text)
        path = text[begin:end]
        current = 0

        disk_edge = "0" + path[0]
        if disk_edge not in next_child[current]:
            next_child[current][disk_edge] = add_node(False)
        current = next_child[current][disk_edge]

        for folder in path[3:].split("\\")[:-1]:
            edge = "1" + folder
            if edge not in next_child[current]:
                next_child[current][edge] = add_node(True)
            current = next_child[current][edge]

        direct_files[current] += 1

    stack = [(0, 0)]
    order = []

    while stack:
        vertex, seen = stack.pop()
        if seen:
            order.append(vertex)
        else:
            stack.append((vertex, 1))
            for child in next_child[vertex].values():
                stack.append((child, 0))

    subtree_folders = [0] * len(next_child)
    subtree_files = [0] * len(next_child)
    answer_folders = 0
    answer_files = 0

    for vertex in order:
        files_here = direct_files[vertex]
        folders_here = 0

        for child in next_child[vertex].values():
            files_here += subtree_files[child]
            folders_here += subtree_folders[child]
            if real_folder[child]:
                folders_here += 1

        subtree_files[vertex] = files_here
        subtree_folders[vertex] = folders_here

        if real_folder[vertex]:
            answer_folders = max(answer_folders, folders_here)
            answer_files = max(answer_files, files_here)

    print(answer_folders, answer_files)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
