# CLAUSE: setup_environment
import sys

sys.setrecursionlimit(300000)

# CLAUSE: solve_logic
def main():
    def read_path_line():
        line = sys.stdin.readline()
        while line and line.strip() == "":
            line = sys.stdin.readline()
        return line

    def get_path(k):
        if k not in answers:
            print("?", k, flush=True)
            line = read_path_line()
            if line:
                values = list(map(int, line.split()))
                answers[k] = values[1:] if values[0] else []
            else:
                answers[k] = []
        return answers[k]

    def begins(path, prefix):
        return path[:len(prefix)] == prefix if len(path) >= len(prefix) else False

    def note_edge(parent, child):
        key = (parent, child)
        if key in seen_edges:
            return
        seen_edges.add(key)
        output_edges.append(key)
        ancestors = [parent]
        descendants = [child]
        for i in range(1, n + 1):
            if reachable[i][parent]:
                ancestors.append(i)
            if reachable[child][i]:
                descendants.append(i)
        for a in ancestors:
            cells = reachable[a]
            for b in descendants:
                cells[b] = True

    def find_open_child(v, lower):
        candidate = lower + 1
        while candidate <= n:
            if candidate != v and not reachable[candidate][v]:
                return candidate
            candidate += 1
        return 0

    def count_paths(prefix, first_pos):
        v = prefix[-1]
        if fixed[v]:
            return span[v]
        total = 1
        ask_pos = first_pos + 1
        lower = 0
        child = find_open_child(v, lower)
        while child:
            got = get_path(ask_pos)
            if not begins(got, prefix):
                span[v] = ask_pos - first_pos
                fixed[v] = True
                return span[v]
            child = got[len(prefix)]
            note_edge(v, child)
            block = span[child] if fixed[child] else count_paths(got, ask_pos)
            total += block
            ask_pos += block
            lower = child
            child = find_open_child(v, lower)
        span[v] = total
        fixed[v] = True
        return total

    first = read_path_line()
    if not first:
        return
    cases = int(first)
    for _ in range(cases):
        line = read_path_line()
        if not line:
            return
        n = int(line)
        answers = {}
        fixed = [False for _ in range(n + 1)]
        span = [0 for _ in range(n + 1)]
        reachable = [[False for _ in range(n + 1)] for _ in range(n + 1)]
        seen_edges = set()
        output_edges = []
        position = 1
        for start in range(1, n + 1):
            if fixed[start]:
                position += span[start]
            else:
                path = get_path(position)
                if not path:
                    break
                count_paths(path, position)
                position += span[start]
        print("!", len(output_edges), flush=True)
        for edge in output_edges:
            print(edge[0], edge[1], flush=True)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
