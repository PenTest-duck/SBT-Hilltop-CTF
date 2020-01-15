# Broken DES - Writeup

This DES challenge requires a deep understanding of the inner-workings of the DES algorithm.
The solver must understand (step-by-step) how the DES key schedule works, and how DES decryption for a single block works.

This challenge gave a ciphertext which had only completed 5 out of the 16 rounds and k12 - or the 12th round key that was being used on the ciphertext in round 5 (DES decryption applies keys in reverse order) - and had the solver finish off the decryption, without knowledge of the initial key or ciphertext.

There were two major tasks the solver had to address:
  1. Generate round keys k1 to k11, by using k12.
  2. Finish the remaining 11 rounds of decryption.

# Generating the Round Keys

Before trying to reverse the key schedule process to obtain round keys k1 to k11, the solver must understand how normal key scheduling works. A normal key scheduling process with an initial 64-bit key is the following:
  1. Permute the initial key according to the PC-1 table (key size 64 -> 56).
  2. Split the key into halves c0 and d0.
  3. Left shift c0 and d0 according to the LS scheme to obtain c1 to c16 and d1 to d16.
  4. Permute cNdN according to the PC-2 table to obtain the 16 subkeys (key size 56 -> 48).
  
 
