#S-DES Original Key Recovery (given k2)

def toString(input_list):
    out = ""
    for i in input_list:
        out += i
    return out

k2 = input("K2: ")
k2_bits = []
for bit in k2:
    k2_bits.append(bit)

#Inverse permute
def p8_inverse_permute(inp, out):
    #P8-1 Table:
    #       6  3  7  4  8  5  10  9
    # 1  2  3  4  5  6  7  8  9  10

    #We do not know bits 1 & 2. We will brute force for them later.
    
    out[2] = inp[1]
    out[3] = inp[3]
    out[4] = inp[5]
    out[5] = inp[0]
    out[6] = inp[2]
    out[7] = inp[4]
    out[8] = inp[7]
    out[9] = inp[6]

combined_key = ['', '', '', '', '', '', '', '', '', '']
p8_inverse_permute(k2_bits, combined_key)

#Split combined key into halves
key_left = combined_key[0:5]
key_right = combined_key[5:10]

#Right shift 3 times, back to the original left & right keys
for i in range(3):
    l = key_left.pop()
    key_left.insert(0, l)

for i in range(3):
    r = key_right.pop()
    key_right.insert(0, r)

#Combine halves and inverse permute
permuted_key = key_left + key_right

def p10_inverse_permute(inp, out):
    #P10-1 Table:
    # 3  5  2  7  4  10 1  9  8  6
    # 1  2  3  4  5  6  7  8  9  10
    out[0] = inp[6]
    out[1] = inp[2]
    out[2] = inp[0]
    out[3] = inp[4]
    out[4] = inp[1]
    out[5] = inp[9]
    out[6] = inp[3]
    out[7] = inp[8]
    out[8] = inp[7]
    out[9] = inp[5]

key = ['', '', '', '', '', '', '', '', '', '']
p10_inverse_permute(permuted_key, key)

#Compute the 4 possible keys
key1 = key[:]
key1[3] = '0'
key1[6] = '0'

key2 = key[:]
key2[3] = '0'
key2[6] = '1'

key3 = key[:]
key3[3] = '1'
key3[6] = '0'

key4 = key[:]
key4[3] = '1'
key4[6] = '1'

#Attempt decryption with each of these keys
print("Key #1: " + toString(key1))
print("Key #2: " + toString(key2))
print("Key #3: " + toString(key3)) # correct key
print("Key #4: " + toString(key4))
