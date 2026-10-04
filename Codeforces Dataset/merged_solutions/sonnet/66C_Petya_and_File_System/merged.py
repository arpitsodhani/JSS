# Clause setup_environment [Confidence: 0.75]
import sys


# Clause solve_logic [Confidence: 0.75]
def main():
    data = ''.join(sys.stdin.read().split())
    if not data:
        return

    roots = {}
    children = []
    files = []

    def new_node():
        children.append({})
        files.append(0)
        return len(children) - 1

    answer_folders = 0
    answer_files = 0
    starts = []

    for i in range(len(data) - 2):
        if data[i] in "CDEFG" and data[i + 1] == ":" and data[i + 2] == "\\":
            starts.append(i)

    for index, start in enumerate(starts):
        stop = starts[index + 1] if index + 1 < len(starts) else len(data)
        path = data[start:stop]
        disk = path[0]
        parts = path[3:].split("\\")
        folders = parts[:-1]

        if disk not in roots:
            roots[disk] = new_node()
        node = roots[disk]

        for name in folders:
            nxt = children[node].get(name)
            if nxt is None:
                nxt = new_node()
                children[node][name] = nxt
            node = nxt

        files[node] += 1

    def dfs(node, is_folder):
        nonlocal answer_folders, answer_files
        folder_total = 0
        file_total = files[node]

        for child in children[node].values():
            child_folders, child_files = dfs(child, True)
            folder_total += child_folders + 1
            file_total += child_files

        if is_folder:
            if folder_total > answer_folders:
                answer_folders = folder_total
            if file_total > answer_files:
                answer_files = file_total

        return folder_total, file_total

    for root in roots.values():
        dfs(root, False)

    print(answer_folders, answer_files)


# Clause finish_program [Confidence: 1.00]
if __name__ == "__main__":
    main()


