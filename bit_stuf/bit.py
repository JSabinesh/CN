
def bit_stuff(data: str) -> str:
    out, c = [], 0
    for b in data:
        out.append(b)
        if b == '1':
            c += 1
            if c == 5:
                out.append('0'); c = 0
        else:
            c = 0
    return ''.join(out)


def bit_unstuff(stuffed: str) -> str:
    out, c, i = [], 0, 0
    while i < len(stuffed):
        b = stuffed[i]; out.append(b)
        if b == '1':
            c += 1
            if c == 5:
                # skip next bit if stuffed zero
                if i+1 < len(stuffed) and stuffed[i+1] == '0':
                    i += 1
                c = 0
        else:
            c = 0
        i += 1
    return ''.join(out)

# quick demo
payload = "011111101111110"
s = bit_stuff(payload)
print("payload:", payload)
print("stuffed :", s)
print("recovered:", bit_unstuff(s))