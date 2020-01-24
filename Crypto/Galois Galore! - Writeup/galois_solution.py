#MixColumns() & InvMixColumns()

def XOR(arg1, arg2):
    out = []
    for pos in range(len(arg1)):
        if arg1[pos] == arg2[pos]:
            out.append('0')
        else:
            out.append('1')
    return out

def string2list(string):
    out = []
    for char in string:
        out.append(char)
    return out

def list2string(input_list):
    out = ""
    for i in input_list:
        out += i
    return out

def hex2bin(hexa):
    out = ""
    for digit in hexa:
        out += bin(int(digit, 16))[2:].zfill(4)
    return string2list(out)

def hex2bytes(hexa):
    out = []
    for i in range(0, len(hexa), 2):
        byte = string2list(bin(int(hexa[i], 16))[2:].zfill(4) + bin(int(hexa[i + 1], 16))[2:].zfill(4))
        out.append(byte)
    return out

def bytes2hex(binary): 
    out = ""
    for byte in binary:
        out += hex(int(list2string(byte)[0:4], 2))[2:]
        out += hex(int(list2string(byte)[4:8], 2))[2:]
    return out

def get_column(inp, col):
    out = []
    for i in range(4):
        out.append(inp[len(inp) // 4 * i + col - 1])
    return out

def galois_multiply(a, b):
    out = b
    b = int(list2string(b), 2)

    values = [b]
    for i in range(3):
        val = values[i]
        val <<= 1
        if val >= 256:
            val -= 256
            val ^= 0x1b
        values.append(val)

    if a == '02':
        out = hex2bin(hex(values[1])[2:].zfill(2))
    elif a == '03':
        out = hex2bin(hex(values[0] ^ values[1])[2:].zfill(2))
    elif a == '09':
        out = hex2bin(hex(values[0] ^ values[3])[2:].zfill(2))
    elif a == '0b':
        out = hex2bin(hex(values[0] ^ values[1] ^ values[3])[2:].zfill(2))
    elif a == '0d':
        out = hex2bin(hex(values[0] ^ values[2] ^ values[3])[2:].zfill(2))
    elif a == '0e':
        out = hex2bin(hex(values[1] ^ values[2] ^ values[3])[2:].zfill(2))

    return out

def mix_columns(inp):
    out = []
    pre_out = []
    matrix = [['02', '03', '01', '01'],
              ['01', '02', '03', '01'],
              ['01', '01', '02', '03'],
              ['03', '01', '01', '02']]
    
    for i in range(1, 5):
        col = get_column(inp, i)
        col_out = []
        for j in range(4):
            val = ['0', '0', '0', '0', '0', '0', '0', '0']
            for k in range(4):
                val = XOR(galois_multiply(matrix[j][k], col[k]), val)
            col_out.append(val)
        pre_out.append(col_out)

    for i in range(4):
        for j in range(4):
            out.append(pre_out[j][i])
            
    return out

def inv_mix_columns(inp):
    out = []
    pre_out = []
    matrix = [['0e', '0b', '0d', '09'],
              ['09', '0e', '0b', '0d'],
              ['0d', '09', '0e', '0b'],
              ['0b', '0d', '09', '0e']]

    for i in range(1, 5):
        col = get_column(inp, i)
        col_out = []
        for j in range(4):
            val = ['0', '0', '0', '0', '0', '0', '0', '0']
            for k in range(4):
                val = XOR(galois_multiply(matrix[j][k], col[k]), val)
            col_out.append(val)
        pre_out.append(col_out)
        
    for i in range(4):
        for j in range(4):
            out.append(pre_out[j][i])
    
    return out

def main():
    state = hex2bytes(input("State: "))
    print("MixColumns(): " + bytes2hex(mix_columns(state)))
    print("InvMixColumns(): " + bytes2hex(inv_mix_columns(state)))

if __name__ == "__main__":
    main()
