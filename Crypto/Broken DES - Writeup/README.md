# Broken DES - Writeup

This DES challenge requires a deep understanding of the inner-workings of the DES algorithm.
The solver must understand (step-by-step) how the DES key schedule works, and how DES decryption for a single block works.

This challenge gave a ciphertext which had only completed 5 out of the 16 rounds and k12 - or the 12th round key that was being used on the ciphertext in round 5 (DES decryption applies keys in reverse order) - and had the solver finish off the decryption, without knowledge of the initial key or ciphertext.

There were two major tasks the solver had to address:
  1. Generate round keys k1 to k11, by using k12.
  2. Finish the remaining 11 rounds of decryption.
