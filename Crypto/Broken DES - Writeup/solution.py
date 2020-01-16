#Broken DES Hilltop CTF Solution
### Run using the terminal python3 command (e.g. python3 solution.py) if IDLE becomes unresponsive during execution.

roundkey12 = "010110010110110110011101000111111000011110100101" # WW2dH4el to binary
roundresult5 = "1001001111001010001010001110011101011000101010111011110011100010" # k8oo51irvOI= to binary

ls_scheme = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
pc2_table = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
inv_pc2_table = [5, 24, 7, 16, 6, 10, 20, 18, 12, 3, 15, 23, 1, 9, 19, 2, 14, 22, 11, 13, 4, 17, 21, 8, 47, 31, 27, 48, 35, 41, 46, 28, 39, 32, 25, 44, 37, 34, 43, 29, 36, 38, 45, 33, 26, 42, 30, 40] 
e_table = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
p_table = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
ip_inv_table = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
s_boxes = [[[14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9, 0,  7],
            [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5, 3,  8],
            [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10, 5,  0],
            [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0, 6, 13]],

           [[15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12, 0,  5, 10],
            [ 3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6, 9, 11,  5],
            [ 0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9, 3,  2, 15],
            [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0, 5, 14,  9]],

           [[10,  0,  9, 14, 6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
            [13,  7,  0,  9, 3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],
            [13,  6,  4,  9, 8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
            [ 1, 10, 13,  0, 6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]],

           [[ 7, 13, 14, 3,  0,  6,  9, 10,  1, 2, 8,  5, 11, 12,  4, 15],
            [13,  8, 11, 5,  6, 15,  0,  3,  4, 7, 2, 12,  1, 10, 14,  9],
            [10,  6,  9, 0, 12, 11,  7, 13, 15, 1, 3, 14,  5,  2,  8,  4],
            [ 3, 15,  0, 6, 10,  1, 13,  8,  9, 4, 5, 11, 12,  7,  2, 14]],

           [[ 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13, 0, 14,  9],
            [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3, 9,  8,  6],
            [ 4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6, 3,  0, 14],
            [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10, 4,  5,  3]],

           [[12,  1, 10, 15, 9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
            [10, 15,  4,  2, 7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],
            [ 9, 14, 15,  5, 2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
            [ 4,  3,  2, 12, 9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]],

           [[ 4, 11,  2, 14, 15, 0,  8, 13,  3, 12, 9,  7,  5, 10, 6,  1],
            [13,  0, 11,  7,  4, 9,  1, 10, 14,  3, 5, 12,  2, 15, 8,  6],
            [ 1,  4, 11, 13, 12, 3,  7, 14, 10, 15, 6,  8,  0,  5, 9,  2],
            [ 6, 11, 13,  8,  1, 4, 10,  7,  9,  5, 0, 15, 14,  2, 3, 12]],

           [[13,  2,  8, 4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
            [ 1, 15, 13, 8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
            [ 7, 11,  4, 1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
            [ 2,  1, 14, 7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]]]

def bin2dec(binary):
    return str(int(binary, 2))

def dec2bin(dec):
    return bin(dec)[2:].zfill(4)

def bin2ascii(binary):
    out = ""
    for i in range(int(len(binary) / 8)):
        byte = binary[i * 8:i * 8 + 8]
        out += chr(int(byte, 2))
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

def XOR(arg1, arg2):
    out = []
    for pos in range(len(arg1)):
        if arg1[pos] == arg2[pos]:
            out.append('0')
        else:
            out.append('1')
    return out

def permute(inp, table):
    output = []
    for pos in table:
        output.append(inp[pos - 1])
    return output

def substitute(inp, s_box):
    out = []
    for i in range(8):
        row = bin2dec(inp[i][0] + inp[i][5])
        col = bin2dec(list2string(inp[i][1:5]))
        cell = s_box[i][int(row)][int(col)]
        out += string2list(dec2bin(cell))
    return out

def right_shift(inp, num):
    for i in range(num):
        inp.insert(0, inp.pop())
    return inp

def bruteforce(seed):
    out = []
    seed = permute(seed, inv_pc2_table) # Inverse permute PC2-table

    for i in range(256):
        x = bin(i)[2:].zfill(8)
        key = seed.copy()
        
        key.insert(8, x[0]) # Add in missing digits 
        key.insert(17, x[1])
        key.insert(21, x[2])
        key.insert(24, x[3])
        key.insert(34, x[4])
        key.insert(37, x[5])
        key.insert(42, x[6])
        key.insert(53, x[7])

        out.append(key)
        
    return out

def subkey_gen(k12):
    global subkeys
    c = []
    d = []
    
    prev_c = k12[0:28]
    prev_d = k12[28:56]
    
    #1. Left shift c12 and d12 according to the LS Scheme to obtain c11 to c0 and d11 to d0
    for i in range(11, 0, -1):
        shifted = right_shift(prev_c, ls_scheme[i])
        c.append(shifted.copy())
        
    for i in range(11, 0, -1):
        shifted = right_shift(prev_d, ls_scheme[i])
        d.append(shifted.copy())
        
    c.reverse()
    d.reverse()

    #2. Permute cNdN using PC-2 Table to obtain the remaining 11 subkeys:
    #14    17   11    24     1    5
    # 3    28   15     6    21   10
    #23    19   12     4    26    8
    #16     7   27    20    13    2
    #41    52   31    37    47   55
    #30    40   51    45    33   48
    #44    49   39    56    34   53
    #46    42   50    36    29   32
    
    subkeys = []
    for i in range(11):
        cd = c[i] + d[i]
        subkey = permute(cd, pc2_table) 
        subkeys.append(subkey)

def DES_Round(l, r, n):
    #1. Expansion using E Table:
    #32     1    2     3     4    5
    # 4     5    6     7     8    9
    # 8     9   10    11    12   13
    #12    13   14    15    16   17
    #16    17   18    19    20   21
    #20    21   22    23    24   25
    #24    25   26    27    28   29
    #28    29   30    31    32    1
    expanded_r = permute(r, e_table)
    
    #2. XOR round key with expanded right half-block
    xor_r = XOR(subkeys[n], expanded_r)

    #3. Substitute XORed right half-block with S-boxes S1 to S8
    pre_sub = []
    for i in range(8):
        pre_sub.append(xor_r[i * 6: i * 6 + 6])
    sub_r = substitute(pre_sub, s_boxes)

    #4. Permute substituted right half-block using P Table:
    #16   7  20  21
    #29  12  28  17
    # 1  15  23  26
    # 5  18  31  10
    # 2   8  24  14
    #32  27   3   9
    #19  13  30   6
    #22  11   4  25
    permuted_r = permute(sub_r, p_table)

    #5. XOR L(n-1) with permuted right half-block
    ln = r
    rn = XOR(l, permuted_r)
    prev_lr["prev_l"] = ln
    prev_lr["prev_r"] = rn
    round_out = ln + rn

    #print(list2string(round_out)) #
    return round_out

def DES_decrypt(text):
    #1. Split the block in half
    l5 = text[0:32]
    r5 = text[32:64]
    
    #2. Perform the remaining 11 rounds
    global prev_lr
    prev_lr = {"prev_l" : l5, "prev_r" : r5}
    for n in range(10, -1, -1):
        final_block = DES_Round(prev_lr["prev_l"], prev_lr["prev_r"], n)

    #3. Switch the left and right half-blocks
    final_block = final_block[32:64] + final_block[0:32]

    #4. Inverse permute using IP-1 Table:
    #40     8   48    16    56   24    64   32
    #39     7   47    15    55   23    63   31
    #38     6   46    14    54   22    62   30
    #37     5   45    13    53   21    61   29
    #36     4   44    12    52   20    60   28
    #35     3   43    11    51   19    59   27
    #34     2   42    10    50   18    58   26
    #33     1   41     9    49   17    57   25
    block_out = permute(final_block, ip_inv_table)
    return block_out


def main():
    k12 = string2list(roundkey12)
    b5 = string2list(roundresult5)

    bruteforced_keys = bruteforce(k12)

    for i in range(256):
        subkey_gen(bruteforced_keys[i])
        print("#" + str(i + 1), bin2ascii(list2string(DES_decrypt(b5))))
        
        
if __name__ == "__main__":
    main()
