# Galois Galore! - Writeup

This cryptography challenge requires the solver to understand and implement the MixColumns() and InvMixColumns() functions of AES, and the Galois Field arithematic and matrix multiplication behind them.

# Galois Field Arithmatic

Galois Field is a finite field, meaning that all arithmatic done within the field stays within the field.
In simple terms, if my Galois Field had an order of 256, the results of any arithmatic done within my GF(256) cannot be larger than 255.
It may seem very strange that the result of 58 * 129 is less than 256 and to the extent of primary school maths, it is.
However, finite field arithmatic requires a re-definition of the common operations - addition, subtraction, multiplication and division.
For AES, only finite field addition and multiplication are required.

Galois Field Addition is very simple - A + B is equal to A XOR B.
For example, 0x57 + 0x83 = 0x57 ^ 0x83 = 0xd4.
Since XOR only flips bits and doesn't have the concept of 'carrying' digits over, the result of addition will always stay within the field.

Galois Field Multiplication is where it gets quite tricky.


# Matrix Multiplication

# MixColumns() & InvMixColumns()
