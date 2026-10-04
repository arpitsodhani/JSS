import sys

MOD = 1_000_000_007

data = sys.stdin.read().split()
t = int(data[0])
pos = 1
ans = []

for _ in range(t):
    x = int(data[pos])
    s = data[pos + 1]
    pos += 2

    # CLAUSE: track_virtual_length
    current_len = len(s)
    buf = list(s)

    for i in range(1, x + 1):
        # CLAUSE: extract_repeat_factor
        extra = ord(buf[i - 1]) - ord('1')

        # CLAUSE: append_suffix_copies
        suffix_start = i
        suffix_end = len(buf)

        # CLAUSE: apply_modular_growth
        current_len = (current_len + (current_len - i) * extra) % MOD

        # CLAUSE: limit_buffer_expansion
        for _copy in range(extra):
            for j in range(suffix_start, suffix_end):
                if len(buf) >= x:
                    break
                buf.append(buf[j])
            if len(buf) >= x:
                break

    # CLAUSE: emit_final_length
    ans.append(str(current_len % MOD))

sys.stdout.write("\n".join(ans))
