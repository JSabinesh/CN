
FLAG = 0x7E
ESC  = 0x7D
XOR  = 0x20

def byte_stuff(payload: bytes) -> bytes:
    out = bytearray([FLAG])
    for b in payload:
        if b in (FLAG, ESC):
            out += bytes([ESC, b ^ XOR])
        else:
            out.append(b)
    out.append(FLAG)
    return bytes(out)

def byte_unstuff(frame: bytes) -> bytes:
    out = bytearray(); i = 1
    while i < len(frame) - 1:
        b = frame[i]
        if b == ESC:
            i += 1
            out.append(frame[i] ^ XOR)
        else:
            out.append(b)
        i += 1
    return bytes(out)

# Example
payload = b"Hi~}Test"
frame = byte_stuff(payload)
print("Frame sent:", frame)
print("Recovered :", byte_unstuff(frame))