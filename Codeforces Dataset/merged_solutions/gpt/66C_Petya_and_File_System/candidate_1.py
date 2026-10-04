# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
s = sys.stdin.read().strip()
if not s:
    sys.exit()

starts = []
for i in range(len(s) - 2):
    if s[i] in "CDEFG" and s[i + 1] == ":" and s[i + 2] == "\\":
        starts.append(i)

paths = []
for idx, st in enumerate(starts):
    en = starts[idx + 1] if idx + 1 < len(starts) else len(s)
    p = s[st:en].strip()
    if p:
        paths.append(p)

children = {}
file_count = {}

for path in paths:
    parts = path.split("\\")
    disk = parts[0]
    folders = parts[1:-1]

    cur = (disk,)
    children.setdefault(cur, set())
    file_count.setdefault(cur, 0)

    for folder in folders:
        nxt = cur + (folder,)
        children.setdefault(cur, set()).add(nxt)
        children.setdefault(nxt, set())
        file_count.setdefault(nxt, 0)
        cur = nxt

    file_count[cur] = file_count.get(cur, 0) + 1

sys.setrecursionlimit(1000000)
max_folders = 0
max_files = 0

def dfs(node):
    global max_folders, max_files
    total_folders = 0
    total_files = file_count.get(node, 0)

    for child in children.get(node, ()):
        cf, cfiles = dfs(child)
        total_folders += cf + 1
        total_files += cfiles

    if len(node) > 1:
        max_folders = max(max_folders, total_folders)
        max_files = max(max_files, total_files)

    return total_folders, total_files

for d in "CDEFG":
    root = (d + ":",)
    if root in children:
        dfs(root)

print(max_folders, max_files)

# CLAUSE: finish_program
RESULT_SENTINEL = None
