# Simplified DES - Writeup

In order to solve this challenge, you must first have an understanding of the round key generation process in S-DES.

Since S-DES uses two rounds per block, two round keys (k1 and k2) need to be generated.

In summary, the keygen process looks like this: 

1. Take a random 10-bit key as input

2. Perform permutation on the key (according to the P10 table)

3. Split the key in half (left & right)

4. Take the first bit of each subkey and shift it to the end (a.k.a. Left Shift 1, or LS-1)

5. Concatenate the left and right subkeys and perform permutation (according to the P8 table), which reduces the key size from 10 bits to 8 bits.

6. The result is k1, or the first round key.

6. Take the shifted subkeys again, and this time, shift the first two bits to the end (LS-2)

7. Concatenate the left and right subkeys and perform the same permutation. 

8. The result is k2, or the second round key.


Utilising this knowledge, you can reverse the k2 generation process to obtain the possible original keys.

The reversing steps look like the following:

1. Take k2 as input

2. Perform inverse permutation (according to the P8-1 table) to increase the key size from 8 bits to 10 bits - since we do not know what bits 1 & 2 were, leave them blank for now.

3. Split the key in half (left & right)

4. Shift the last three bits of each subkey to the front (a.k.a. Right Shift 3, or RS-3) - this reverses the LS-1 and LS-2 shifts.

5. Concatenate the left and right subkeys and perform inverse permutation (according to the P10-1 table)

6. Bits 4 & 7 should be blank - fill them in with the 4 different combinations of 0s and 1s

7. Try to decrypt the ciphertext with each of the 4 keys - one will produce a meaningful output, which is the flag
