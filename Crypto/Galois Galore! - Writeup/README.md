# Galois Galore! - Writeup

This cryptography challenge requires the solver to understand and implement the MixColumns() and InvMixColumns() functions of AES, and the Galois Field arithematic and matrix multiplication behind them.

# Galois Field Arithmatic

Galois Field is a finite field, meaning that all arithmatic done within the field stays within the field.
In simple terms, if my Galois Field had an order of 256, the results of any arithmatic done within my GF(256) cannot be larger than 255.
It may seem very strange that the result of 58 * 129 is less than 256 and to the extent of primary school maths, it is.
However, finite field arithmatic requires a re-definition of the common operations - addition, subtraction, multiplication and division.
For AES, only finite field addition and multiplication are required.

Galois Field Addition (GFA) is very simple - A + B is equal to A XOR B.
For example, 0x57 + 0x83 = 0x57 XOR 0x83 = 0xd4.
Since XOR only flips bits and doesn't have the concept of 'carrying' digits over, the result of addition will always stay within the field.

Galois Field Multiplication (GFM) is where it gets quite tricky.
It consists of a series of bitwise left shifts, XORs and GFAs. 
Instead of directly multiplying two numbers, intermediate results are calculated, then added at the end to get the result.

For A * B in GF(256) and an irreductible polynomial m(x) = x^8 + x^4 + x^3 + x + 1:
1. Define the function xtime(n) as: n << 1; and if n > 0xff, do n - 0xff and n XOR 0x1b.
2. A * 0x02 = xtime(B) = X1; A * 0x04 = xtime(X1) = X2; A * 0x08 = xtime(X2) = X3 ... and so on until A * 0x80.
3. Xp + Xq + Xs ... and so on until p + q + s + ... = B.

# Matrix Multiplication

# MixColumns() & InvMixColumns()
