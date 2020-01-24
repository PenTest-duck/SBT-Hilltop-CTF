# Galois Galore! - Writeup

This cryptography challenge requires the solver to understand and implement the MixColumns() and InvMixColumns() functions of AES, and the Galois Field arithematic and matrix multiplication behind them.

# The Maths: Galois Field Arithmatic & Matrix Multiplication

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

For A * B in GF(256) and an irreducible polynomial m(x) = x^8 + x^4 + x^3 + x + 1:
1. Define the function xtime(n) as: n << 1; and if n > 0xff, do n - 256 and n XOR 0x1b.
2. A * 0x01 = X0; A * 0x02 = xtime(X0) = X1; A * 0x04 = xtime(X1) = X2; A * 0x08 = xtime(X2) = X3 ... and so on for Xn until 2^n >= B.
3. Xp XOR Xq XOR Xs XOR ... and so on until 2^p + 2^q + 2^s + ... = B.

For example, for 0x57 * 0x13:
1. X1 = 0x57 << 1 = 0xae
2. X2 = 0xae << 1 - 256 XOR 0x1b = 0x47
3. X3 = 0x47 << 1 = 0x8e
4. X4 = 0x8e << 1 - 256 XOR 0x1b = 0x07
5. X0 + X1 + x4 = 0x57 XOR 0xae XOR 0x07 = 0xfe

In addition to Galois Field arithmatic, MixColumns() and InvMixColumns() also uses matrix multiplication in its process.
Each column in the State is GFM-ed to the defined matrix to return a mixed column.
Each byte in the column is GFM-ed to an associated byte in the matrix, and the results are GFA-ed to result in a byte of the mixed column.

Figure 5.6 of FIPS 197 shows this process in greater detail.

# MixColumns() & InvMixColumns()

In essence, MixColumns() and InvMixColumns() are just a series of matrix multiplications with GFAs and GFMs, against predefined matrixes.
We can convert all the maths discussed above into a Python script and define additional functions to perform base conversion, solve minor implementation issues and take a State as input (keeping in mind that the State is read vertically).
This step mostly relies on the solver being able to convert concepts to programming language.

Once the MixColumns() and InvMixColumns() have been performed on the given States, the results should be concatenated and converted from hex to ASCII to give the flag.

Flag: HilltopCTF{th4nk_y0u_s0_much_ev4rist3_g4lo15!!!}
