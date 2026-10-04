# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def make_answer(a, b, heads, tails):
    return "YES\n{} {}\n{}\n{}\n".format(a, b, " ".join(map(str, heads)), " ".join(map(str, tails)))

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return

    n = values[0]
    m = values[1]
    h = values[2]
    t = values[3]

    graph = [[] for _ in range(n + 1)]
    edge_list = []
    i = 4
    while i < 4 + 2 * m:
        a = values[i]
        b = values[i + 1]
        i += 2
        graph[a].append(b)
        graph[b].append(a)
        edge_list.append((a, b))

    used = [0] * (n + 1)
    token = 10

    for original_a, original_b in edge_list:
        for a, b in ((original_a, original_b), (original_b, original_a)):
            if len(graph[a]) - 1 < h or len(graph[b]) - 1 < t:
                continue
            if len(graph[a]) + len(graph[b]) - 2 < h + t:
                continue

            token += 3
            a_token = token
            common_token = token + 1

            for node in graph[a]:
                if node != b:
                    used[node] = a_token

            only_b = []
            common = []
            for node in graph[b]:
                if node == a:
                    continue
                if used[node] == a_token:
                    used[node] = common_token
                    common.append(node)
                else:
                    only_b.append(node)

            only_a = []
            for node in graph[a]:
                if node != b and used[node] == a_token:
                    only_a.append(node)

            take_common_for_a = h - len(only_a)
            take_common_for_b = t - len(only_b)
            if take_common_for_a < 0:
                take_common_for_a = 0
            if take_common_for_b < 0:
                take_common_for_b = 0

            if take_common_for_a + take_common_for_b <= len(common):
                heads = only_a[:h]
                if take_common_for_a:
                    heads += common[:take_common_for_a]
                tails = only_b[:t]
                if take_common_for_b:
                    tails += common[take_common_for_a:take_common_for_a + take_common_for_b]
                sys.stdout.write(make_answer(a, b, heads, tails))
                return

    sys.stdout.write("NO\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
