# Blindsighted - Writeup

This steganography challenge requires the solver to adjust brightness and contrast levels and convert Braille to decimal numbers and finally to ASCII.

Finding the Braille within the image shouldn't be difficult, as its transparency isn't very low and the challenge prompt gave a very helpful clue that the flag is somewhere within the night background.
Sure enough, if we take a very close look at the top of the image, we can faintly see a strip of Braille characters.
Alternatively, we can use Stegsolve to XOR invert the image to see the Braille more clearly.

In order to improve the readability of the Braille, any image editor, such as PhotoShop, GIMP or even Microsoft Word can be used to modify the brightness, contrast, colours, sharpness etc..

# Deciphering the Braille

Before we delve into converting the series of symbols to visually readable text, you should notice that a symbol is placed at the end of every word. 
However, when searching the symbol up, we find that it doesn't translate to any letters, numbers or symbols. 
However, upon further research, you should find that all numbers begin with a symbol that looks very similar to the symbol we found in the image, only flipped horizontally.

We can infer that the Braille has been flipped and unflipping it reveals the Braille to be signifiying a long list of numbers.
If you have CTF experience, your instincts should be telling you to convert the number into ASCII.
Converting the first few numbers should reveal the first few letters of the flag prefix.

We can convert the rest of the symbols to ASCII to reveal the flag.

Flag: HilltopCTF{s0me_th1n9s_y0u_c4n_0n1y_s33_w1th_y0ur_m1nd}
