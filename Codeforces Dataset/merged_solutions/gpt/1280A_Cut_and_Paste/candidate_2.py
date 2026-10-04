import sys

MOD = 1000000007

tokens = sys.stdin.buffer.read().split()
tests = int(tokens[0])
out = []
k = 1

for _ in range(tests):
    x = int(tokens[k])
    text = bytearray(tokens[k + 1])
    k += 2

    # CLAUSE: track_virtual_length
    virtual = len(text)

    cursor = 0
    while cursor < x:
        # CLAUSE: materialize_needed_prefix
        digit_byte = text[cursor]

        # CLAUSE: extract_repeat_factor
        times = digit_byte - 49

        # CLAUSE: append_suffix_copies
        tail = text[cursor + 1:]

        # CLAUSE: apply_modular_growth
        right = (virtual - (cursor + 1)) % MOD
        virtual = (virtual + right * times) % MOD

        # CLAUSE: limit_buffer_expansion
        while times and len(text) < x:
            need = x - len(text)
            text.extend(tail[:need])
            times -= 1

        cursor += 1

    # CLAUSE: emit_final_length
    out.append(str(virtual))

sys.stdout.write("\n".join(out))
