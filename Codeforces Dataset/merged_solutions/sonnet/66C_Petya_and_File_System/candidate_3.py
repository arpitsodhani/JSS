# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
def read_paths(text):
    compact = ''.join(text.split())
    marks = []
    for pos in range(max(0, len(compact) - 2)):
        if compact[pos] in "CDEFG" and compact[pos + 1:pos + 3] == ":\\":
            marks.append(pos)
    for i, left in enumerate(marks):
        right = marks[i + 1] if i + 1 < len(marks) else len(compact)
        yield compact[left:right]

def main():
    child = defaultdict(dict)
    direct = defaultdict(int)
    node_count = 1
    folder_nodes = set()

    for path in read_paths(sys.stdin.read()):
        pieces = path[3:].split("\\")
        current = 0
        disk_key = ("disk", path[0])

        if disk_key not in child[current]:
            child[current][disk_key] = node_count
            node_count += 1
        current = child[current][disk_key]

        for folder in pieces[:-1]:
            key = ("folder", folder)
            if key not in child[current]:
                child[current][key] = node_count
                folder_nodes.add(node_count)
                node_count += 1
            current = child[current][key]

        direct[current] += 1

    best_subfolders = 0
    best_files = 0

    def count_inside(vertex):
        nonlocal best_subfolders, best_files
        subfolders = 0
        total_files = direct[vertex]

        for key, nxt in child[vertex].items():
            nested_folders, nested_files = count_inside(nxt)
            total_files += nested_files
            if key[0] == "folder":
                subfolders += nested_folders + 1
            else:
                subfolders += nested_folders

        if vertex in folder_nodes:
            best_subfolders = max(best_subfolders, subfolders)
            best_files = max(best_files, total_files)

        return subfolders, total_files

    count_inside(0)
    print(best_subfolders, best_files)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
