"""350B accepts any longest chain of mountains ending at a hotel.

The checker recomputes the best length by walking back from every hotel and
then verifies the printed path is a real chain of that length.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n = data[0]
    kind = data[1:1 + n]
    source = data[1 + n:1 + 2 * n]
    outdeg = [0] * (n + 1)
    for v in range(1, n + 1):
        if source[v - 1]:
            outdeg[source[v - 1]] += 1
    best = 0
    for v in range(1, n + 1):
        if kind[v - 1] != 1:
            continue
        length = 1
        u = source[v - 1]
        while u and kind[u - 1] == 0 and outdeg[u] == 1:
            length += 1
            u = source[u - 1]
        best = max(best, length)

    def check(out):
        tokens = out.split()
        k = int(tokens[0])
        path = [int(v) for v in tokens[1:1 + k]]
        assert k == best, f"printed length {k}, the maximum is {best}"
        assert len(path) == k, f"expected {k} vertices, got {len(path)}"
        assert kind[path[-1] - 1] == 1, "the path must end at a hotel"
        for v in path[:-1]:
            assert kind[v - 1] == 0, f"vertex {v} is not a mountain"
            assert outdeg[v] == 1, f"vertex {v} has {outdeg[v]} outgoing tracks"
        for i in range(k - 1):
            assert source[path[i + 1] - 1] == path[i], f"no track {path[i]} -> {path[i+1]}"

    return check
