# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    s = ''.join(sys.stdin.read().split())
    if not s:
        return
    
    starts = []
    for i in range(len(s) - 2):
        if s[i] in 'CDEFG' and s[i + 1] == ':' and s[i + 2] == '\\':
            starts.append(i)
    
    children = []
    direct_files = []
    children.append({})
    direct_files.append(0)
    
    max_subfolders = 0
    max_files = 0
    
    for pos, start in enumerate(starts):
        end = starts[pos + 1] if pos + 1 < len(starts) else len(s)
        path = s[start:end]
        
        parts = path[3:].split('\\')
        disk = path[0]
        folders = parts[:-1]
        
        root_key = (0, disk)
        if root_key not in children[0]:
            children[0][root_key] = len(children)
            children.append({})
            direct_files.append(0)
        node = children[0][root_key]
        
        for folder in folders:
            key = (1, folder)
            if key not in children[node]:
                children[node][key] = len(children)
                children.append({})
                direct_files.append(0)
            node = children[node][key]
        
        direct_files[node] += 1
    
    def dfs(v):
        nonlocal max_subfolders, max_files
        
        folder_count = 0
        file_count = direct_files[v]
        
        for child in children[v].values():
            child_folders, child_files = dfs(child)
            folder_count += 1 + child_folders
            file_count += child_files
        
        if v > 5:
            max_subfolders = max(max_subfolders, folder_count)
            max_files = max(max_files, file_count)
        
        return folder_count, file_count
    
    dfs(0)
    print(max_subfolders, max_files)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
