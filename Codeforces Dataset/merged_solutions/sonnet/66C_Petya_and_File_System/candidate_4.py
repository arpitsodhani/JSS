# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def split_input(raw):
    s = ''.join(raw.split())
    result = []
    last = -1

    for i in range(len(s) - 2):
        if s[i] in "CDEFG" and s[i + 1] == ":" and s[i + 2] == "\\":
            if last != -1:
                result.append(s[last:i])
            last = i

    if last != -1:
        result.append(s[last:])

    return result

def main():
    tree = {}
    best_dirs = 0
    best_files = 0

    for path in split_input(sys.stdin.read()):
        disk = path[0]
        folders = path[3:].split("\\")[:-1]

        branch = tree.setdefault(disk, {})
        for folder in folders:
            branch = branch.setdefault(folder, {})
        branch[""] = branch.get("", 0) + 1

    def walk(branch, folder_real):
        nonlocal best_dirs, best_files
        total_dirs = 0
        total_files = branch.get("", 0)

        for name, sub in branch.items():
            if name != "":
                dirs, found_files = walk(sub, True)
                total_dirs += dirs + 1
                total_files += found_files

        if folder_real:
            best_dirs = max(best_dirs, total_dirs)
            best_files = max(best_files, total_files)

        return total_dirs, total_files

    for disk_tree in tree.values():
        walk(disk_tree, False)

    print(str(best_dirs) + " " + str(best_files))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
