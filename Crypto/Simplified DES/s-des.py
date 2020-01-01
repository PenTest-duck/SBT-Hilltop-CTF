#Simplified DES (S-DES)

def toString(input_list):
    out = ""
    for i in input_list:
        out += i
    return out
    
print("Simplified DES (S-DES)")
method = input("(e)ncrypt or (d)ecrypt: ")

#1. Select random 10-bit key
key = input("10-bit Key: ")
key_bits = []
for bit in key:
    key_bits.append(bit)

#2. Permute key
#P10 Table:
# 1  2  3  4  5  6  7  8  9  10
# 3  5  2  7  4  10 1  9  8  6
permuted_key = ['', '', '', '', '', '', '', '', '', '']
permuted_key[0] = key_bits[2]
permuted_key[1] = key_bits[4]
permuted_key[2] = key_bits[1]
permuted_key[3] = key_bits[6]
permuted_key[4] = key_bits[3]
permuted_key[5] = key_bits[9]
permuted_key[6] = key_bits[0]
permuted_key[7] = key_bits[8]
permuted_key[8] = key_bits[7]
permuted_key[9] = key_bits[5]

print("P10:", toString(permuted_key))

#3. Divide key into halves
key_left = permuted_key[0:5]
key_right = permuted_key[5:10]

print("Left:", toString(key_left))
print("Right:", toString(key_right))

#4. 1-bit round shift for each half-key
l1 = key_left.pop(0)
key_left.append(l1)
r1 = key_right.pop(0)
key_right.append(r1)

print("LS-1 Left:", toString(key_left))
print("LS-1 Light:", toString(key_right))

#5. Combine and permute key
combined_key = key_left + key_right
k1 = ['', '', '', '', '', '', '', '']

def p8_permute(inp, out):
    #P8 Table:
    # 1  2  3  4  5  6  7  8  9  10
    # 6  3  7  4  8  5  10 9
    out[0] = inp[5]
    out[1] = inp[2]
    out[2] = inp[6]
    out[3] = inp[3]
    out[4] = inp[7]
    out[5] = inp[4]
    out[6] = inp[9]
    out[7] = inp[8]

p8_permute(combined_key, k1)
print("K1:", toString(k1))

#6. Generate second subkey
l1 = key_left.pop(0)
l2 = key_left.pop(0)
key_left.append(l1)
key_left.append(l2)

r1 = key_right.pop(0)
r2 = key_right.pop(0)
key_right.append(r1)
key_right.append(r2)

print("LS-2 Left:", toString(key_left))
print("LS-2 Right:", toString(key_right))
combined_key = key_left + key_right
k2 = ['', '', '', '', '', '', '', '']
p8_permute(combined_key, k2)
print("K2:", toString(k2))



#Encryption (same mechanism used for decryption, except in different order)
#1. Get 8-bit plaintext blocks
plaintext = input("Plaintext: ")
plaintext_bits = []
for bit in plaintext:
    plaintext_bits.append(bit)

blocks = []
for i in range(int(len(plaintext_bits)/8)):
    blocks.append(plaintext_bits[i*8:(i+1)*8])

def Block(block):    
    #2. Permute plaintext
    #IP8 Table:
    # 1 2 3 4 5 6 7 8
    # 2 6 3 1 4 8 5 7
    permuted_plaintext = ['', '', '', '', '', '', '', '']
    permuted_plaintext[0] = block[1]
    permuted_plaintext[1] = block[5]
    permuted_plaintext[2] = block[2]
    permuted_plaintext[3] = block[0]
    permuted_plaintext[4] = block[3]
    permuted_plaintext[5] = block[7]
    permuted_plaintext[6] = block[4]
    permuted_plaintext[7] = block[6]

    print("Initial Permutation:", toString(permuted_plaintext))

    def Round(permuted_plaintext, key, round_no):
        #3. Divide plaintext into halves
        plaintext_left = permuted_plaintext[0:4]
        plaintext_right = permuted_plaintext[4:8]

        print("Left:", toString(plaintext_left))
        print("Right:", toString(plaintext_right))

        #4. Expand and permutate right half
        #EP Table:
        # 1 2 3 4
        # 4 1 2 3 2 3 4 1
        expanded_right = ['', '', '', '', '', '', '', '']
        expanded_right[0] = plaintext_right[3]
        expanded_right[1] = plaintext_right[0]
        expanded_right[2] = plaintext_right[1]
        expanded_right[3] = plaintext_right[2]
        expanded_right[4] = plaintext_right[1]
        expanded_right[5] = plaintext_right[2]
        expanded_right[6] = plaintext_right[3]
        expanded_right[7] = plaintext_right[0]

        print("Expanded right:", toString(expanded_right))

        #5. XOR expanded right half with first round key
        def XOR(arg1, arg2):
            out = []
            for position in range(len(arg1)):
                if arg1[position] == arg2[position]:
                    out.append('0')
                else:
                    out.append('1')
            return out

        xor = XOR(expanded_right, key)

        print("XOR with round key:", toString(xor))

        #6. Split XOR-ed plaintext into halves and substitute with S-boxes
        xor_left = xor[0:4]
        xor_right = xor[4:8]

        print("Left:", toString(xor_left))
        print("Right:", toString(xor_right))

        #S-0 S-box
        #   0  1  2  3
        # 0 01 00 11 10
        # 1 11 10 01 00
        # 2 00 10 01 11
        # 3 11 01 11 10
        s0 = {'00' : {'00' : '01', '01' : '00', '10' : '11', '11' : '10'}, '01' : {'00' : '11', '01' : '10', '10' : '01', '11' : '00'}, '10' : {'00' : '00', '01' : '10', '10' : '01', '11' : '11'}, '11' : {'00' : '11', '01' : '01', '10' : '11', '11' : '10'}}

        #S-1 S-box
        #   0  1  2  3
        # 0 00 01 10 11
        # 1 10 00 01 11
        # 2 11 00 01 00
        # 3 10 01 00 11
        s1 = {'00' : {'00' : '00', '01' : '01', '10' : '10', '11' : '11'}, '01' : {'00' : '10', '01' : '00', '10' : '01', '11' : '11'}, '10' : {'00' : '11', '01' : '00', '10' : '01', '11' : '00'}, '11' : {'00' : '10', '01' : '01', '10' : '00', '11' : '11'}}

        s0_row = xor_left[0] + xor_left[3]
        s0_column = xor_left[1] + xor_left[2]
        s1_row = xor_right[0] + xor_right[3]
        s1_column = xor_right[1] + xor_right[2]
            
        sub_left = s0[s0_row][s0_column]
        sub_right = s1[s1_row][s1_column]

        print("Substituted left:", sub_left)
        print("Substituted right:", sub_right)

        #7. Combine substituted output
        sub = sub_left + sub_right

        #8. Permute substituted bits
        #P4 Table:
        # 1 2 3 4
        # 2 4 3 1
        permuted_bits = ['', '', '', '']
        permuted_bits[0] = sub[1]
        permuted_bits[1] = sub[3]
        permuted_bits[2] = sub[2]
        permuted_bits[3] = sub[0]

        print("P4:", toString(permuted_bits))

        #9. XOR permuted bits with initial left bits
        xor_output = XOR(permuted_bits, plaintext_left)

        print("XOR with initial left:", toString(xor_output))

        #10. Combine XOR output with initial right bits and swap halves
        if round_no == 1:
            combined_output = plaintext_right + xor_output
        else:
            combined_output = xor_output + plaintext_right

        print("Round result:", toString(combined_output))
        print("==========END OF ROUND==========")

        return combined_output

    #11. Perform 2 rounds
    if method == "e":
        round_output = Round(Round(permuted_plaintext, k1, 1), k2, 2)
    elif method == "d":
        round_output = Round(Round(permuted_plaintext, k2, 1), k1, 2)
    else:
        print("Error: choose between encryption or decryption.")
        import sys
        sys.exit()

    #12. Perform inverse permutation
    #IP-1 Table:
    # 1 2 3 4 5 6 7 8
    # 4 1 3 5 7 2 8 6
    cipher_block = ['', '', '', '', '', '', '', '']
    cipher_block[0] = round_output[3]
    cipher_block[1] = round_output[0]
    cipher_block[2] = round_output[2]
    cipher_block[3] = round_output[4]
    cipher_block[4] = round_output[6]
    cipher_block[5] = round_output[1]
    cipher_block[6] = round_output[7]
    cipher_block[7] = round_output[5]

    print("++++++++++END OF BLOCK++++++++++")

    return toString(cipher_block)

output = ""
for i in range(len(blocks)):
    output += Block(blocks[i])

print(output)
